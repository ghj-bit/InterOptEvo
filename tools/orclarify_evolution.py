#!/usr/bin/env python3
"""OR-Clarify 交互策略演化（协议对齐 OptMATH/interaction_evolution.py）。

回路：
  round 0  种子策略 → 在 val 上评测（passes 遍并行）→ 成为初始冠军
  round r  ① 从 train 池确定性采样 batch（默认 8 题）
           ② 父本（当前冠军）跑 train batch × passes 遍（tag=train）→ 打包证据喂给演化器
           ③ 演化器产出新的策略（JSON patch；可演化对象由 --policy-schema 决定）
           ④ 候选策略在【同一 batch】上跑 train × passes 遍（tag=ctrain）
              → train 门：候选 net > 父本 net + --selection-epsilon 才继续；
                不过门则本轮到此为止（跳过 val，记 accepted_train=False）
           ⑤ 过门后候选在 val 上评测 × passes 遍
           ⑥ val 门：val net > 冠军 val net + --selection-epsilon 才晋级

与 OptMATH 的差异：
  接线层（4 个耦合点）
  - 跑分器：本地 FP8 走 cap_proxy（关 thinking），judge 走 deepseek-flash —— 由代理按角色分流
  - 判分：读 evaluation_protocol 的 judge_result.json / statistics.json
  - 适应度：net = w_core*CoreExact + w_allslot*AllSlotExact - w_silent*SilentPerRun
  - 策略文档：interactive policy 的 `## Interaction Strategy` 段（其余段落冻结）
  行为层（已知未对齐，改前需确认）
  - 演化器单次调用：OptMATH 对非法 patch 会带拒绝理由重试（--optimizer-retries，温度递增）；
    本实现解析失败即跳过本轮（兜底：tools/evo_backfill_round.py 可从已存响应回填）
  命名：父本 train 阶段 tag=train（OptMATH 为 parent_train），候选 train 阶段 tag=ctrain；
        state 轮次字段 train / ctrain / accepted_train / val / promoted
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EVAL_PIPELINE = REPO_ROOT / "experiments" / "evaluation_protocol" / "run_pipeline.py"
BASE_PROMPTS = REPO_ROOT / "experiments" / "evaluation_protocol" / "prompts"
PROXY_BASE_URL = "http://127.0.0.1:18770/v1"
SYMLINKED_PROMPTS = (
    "question_detector_prompt.md",
    "user_simulator_prompt.md",
    "judge_prompt.md",
    "answer_scope_detector_prompt.md",
)
SEED_STRATEGY_SECTION = "## Interaction Strategy"

# 交互策略文档的两种 schema（2026-10-09 新增 behavior；evo_r10 线沿用 strategy_section）：
#   strategy_section: 可演化 = `## Interaction Strategy` 整段；
#   behavior:         可演化 = `## Behavior` 段的正文；其末尾的协议 bullet 块
#                     （`QUESTION:` 格式组 + `READY_TO_MODEL` 收尾组）是 harness 机件、
#                     完全冻结，且**由程序拼装**——演化器在 prompt 里只看得到可变正文，
#                     patch 也只含正文（不含 section/协议）。
POLICY_SCHEMA = "strategy_section"
PROTOCOL_MARKER = "- Before you are ready to model"
MIN_STRATEGY_CHARS = 40
MAX_STRATEGY_CHARS = 8000  # 仅防失控输出；旧线无长度上限（evo_r10 冠军正文 ~3.8k chars）


# ---------------------------------------------------------------------------
# 策略文档：读取 / 打补丁 / 冻结段校验
# ---------------------------------------------------------------------------

def strategy_body(policy_text: str) -> str:
    """取出可演化的交互策略正文（按 POLICY_SCHEMA 分派）。"""
    if POLICY_SCHEMA == "behavior":
        return behavior_strategy_body(policy_text)
    # 旧 schema：取出 `## Interaction Strategy` 段的正文（到下一个 ## 标题为止）。
    lines = policy_text.splitlines()
    out, inside = [], False
    for line in lines:
        if line.strip() == SEED_STRATEGY_SECTION:
            inside = True
            continue
        if inside and line.startswith("## "):
            break
        if inside:
            out.append(line)
    return "\n".join(out).strip()


def behavior_bounds(policy_text: str) -> tuple[list[str], int, int, int]:
    """定位 `## Behavior` 段：返回 (lines, heading_idx, body_start, marker_idx)。

    body_start = 标题后第一条非空行；marker_idx = 协议块首行
    （以 PROTOCOL_MARKER 开头的 bullet）。两者之间（去尾部空行）即可演化正文。
    """
    lines = policy_text.splitlines()
    heading = None
    for i, line in enumerate(lines):
        if line.strip() == "## Behavior":
            heading = i
            break
    if heading is None:
        raise ValueError("policy has no '## Behavior' section")
    start = heading + 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    marker = None
    for k in range(start, len(lines)):
        if lines[k].strip().startswith(PROTOCOL_MARKER):
            marker = k
            break
    if marker is None:
        raise ValueError(f"policy has no protocol block (line starting with {PROTOCOL_MARKER!r})")
    return lines, heading, start, marker


def behavior_strategy_body(policy_text: str) -> str:
    lines, _, start, marker = behavior_bounds(policy_text)
    end = marker
    while end > start and not lines[end - 1].strip():
        end -= 1
    return "\n".join(lines[start:end])


def _validate_behavior_body(body: str) -> None:
    if not body:
        raise ValueError("empty strategy body")
    if re.search(r"^#+ ", body, flags=re.M):
        raise ValueError("strategy body must not contain markdown headings")
    if len(body) < MIN_STRATEGY_CHARS:
        raise ValueError(f"strategy body too short ({len(body)} < {MIN_STRATEGY_CHARS} chars)")
    if len(body) > MAX_STRATEGY_CHARS:
        raise ValueError(f"strategy body too long ({len(body)} > {MAX_STRATEGY_CHARS} chars)")
    for token in ("READY_TO_MODEL", "QUESTION:"):
        if token in body:
            raise ValueError(f"strategy body must not mention protocol token {token!r}")


def apply_policy_patch(parent_policy: str, patch: dict) -> str:
    if POLICY_SCHEMA == "behavior":
        # patch 只含正文；协议块与其余段落由程序原样拼装（演化器不可见/不可写）。
        section = patch.get("section")
        if section not in (None, "## Behavior"):
            raise ValueError(
                f"section {section!r} is not patchable in this schema; "
                f"return only {{'body': ...}} and the system will insert it")
        body = str(patch.get("body", "")).strip()
        _validate_behavior_body(body)
        lines, _, start, marker = behavior_bounds(parent_policy)
        out = lines[:start] + body.splitlines() + [""] + lines[marker:]
        result = "\n".join(out)
        if parent_policy.endswith("\n"):
            result += "\n"
        return result
    section = patch.get("section", SEED_STRATEGY_SECTION)
    if section != SEED_STRATEGY_SECTION:
        raise ValueError(f"only {SEED_STRATEGY_SECTION} may be patched, got {section!r}")
    body = str(patch.get("body", "")).strip()
    if not body:
        raise ValueError("empty strategy body")
    if re.search(r"^#+ ", body, flags=re.M):
        raise ValueError("strategy body must not contain markdown headings")
    lines = parent_policy.splitlines()
    out, inside = [], False
    for line in lines:
        if line.strip() == SEED_STRATEGY_SECTION:
            inside = True
            out.append(line)
            out.append("")
            out.extend(body.splitlines())
            out.append("")
            continue
        if inside and line.startswith("## "):
            inside = False
        if not inside:
            out.append(line)
    return "\n".join(out)


def frozen_fragments(policy_text: str) -> dict[str, str]:
    """除策略正文外，其余原文必须逐字保留（behavior schema 下含协议块）。"""
    if POLICY_SCHEMA == "behavior":
        lines, _, start, marker = behavior_bounds(policy_text)
        return {"__pre__": "\n".join(lines[:start]), "__post__": "\n".join(lines[marker:])}
    lines = policy_text.splitlines()
    out, inside, buf = {}, False, []
    for line in lines:
        if line.strip() == SEED_STRATEGY_SECTION:
            inside = True
            out["__pre__"] = "\n".join(buf)
            buf = []
            continue
        if inside and line.startswith("## "):
            inside = False
            out["__post__"] = "\n".join(buf)
            buf = []
        if not inside:
            buf.append(line)
    out.setdefault("__post__", "\n".join(buf))
    return out


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def similarity(a: str, b: str) -> float:
    ta, tb = set(normalize(a).split()), set(normalize(b).split())
    return len(ta & tb) / max(1, len(ta | tb))


def assert_fixed_unchanged(candidate: str, parent: str) -> None:
    cf, pf = frozen_fragments(candidate), frozen_fragments(parent)
    for key in ("__pre__", "__post__"):
        if normalize(cf.get(key, "")) != normalize(pf.get(key, "")):
            raise ValueError(f"frozen section changed: {key}")


def assert_new_strategy(body: str, seen: list[str], threshold: float = 0.9) -> None:
    for old in seen:
        if similarity(body, old) >= threshold:
            raise ValueError("candidate strategy is a near-duplicate of a seen strategy")


# ---------------------------------------------------------------------------
# 采样 / 证据包
# ---------------------------------------------------------------------------

def sample_batch(pool: list[str], batch_size: int, seed: int, round_no: int) -> list[str]:
    rng = random.Random(f"{seed}:{round_no}")
    if batch_size > len(pool):
        raise ValueError("batch larger than pool")
    return sorted(rng.sample(pool, batch_size))


def dialogue_view(transcript: list[dict], max_chars: int = 400) -> list[dict]:
    out = []
    for row in transcript:
        who = "agent" if row.get("speaker") == "generic_agent" else "client"
        text = str(row.get("content") or "").strip()
        if who == "client" and len(text) > max_chars:
            text = text[:max_chars] + " …"
        out.append({"turn": row.get("turn"), "who": who, "text": text})
    return out


def build_evidence_bundle(case_runs: dict[str, list[dict]], aggregate: dict,
                          *, round_no: int, successes_limit: int = 8) -> dict:
    """case_runs: case_id -> 每遍一份 {core, allslot, silent, net, stopping, turns, dialogue, slots}"""
    items = []
    for cid in sorted(case_runs):
        recs = case_runs[cid]
        base = recs[0]
        items.append({
            "case_id": cid,
            "core_runs": [r["core"] for r in recs],
            "allslot_runs": [r["allslot"] for r in recs],
            "silent_runs": [r["silent"] for r in recs],
            "net_runs": [round(r["net"], 3) for r in recs],
            "stopping_runs": [r["stopping"] for r in recs],
            "turns_runs": [r["turns"] for r in recs],
            "slot_verdicts": base["slots"],          # pass1 的逐槽判定
            "dialogue": base["dialogue"],            # pass1 的完整交互历史
            "mean_net": round(sum(r["net"] for r in recs) / len(recs), 3),
        })
    failures = [it for it in items if it["mean_net"] < max(it["net_runs"])]
    successes = [it for it in items if it["mean_net"] >= max(it["net_runs"])]
    return {
        "schema_version": 1,
        "benchmark": "OR-Clarify",
        "round": round_no,
        "passes": len(next(iter(case_runs.values()))) if case_runs else 0,
        "aggregate": aggregate,
        "metrics_note": (
            "Core Exact / All-Slot Exact 是 run 级全有或全无（分别针对 P0/P1 与全部隐藏要素）；"
            "Silent/run 是未确认却当真用的假设条数。net = 0.5*Core + 0.5*AllSlot - 0.1*Silent。"
            "每个 case 给出各遍的判定与 pass1 的完整问答历史。"
        ),
        "records": failures + successes[:successes_limit],
    }


# ---------------------------------------------------------------------------
# 演化器调用
# ---------------------------------------------------------------------------

def deepseek_key() -> str:
    key = (os.getenv("DS_REMOTE_KEY") or "").strip()
    if key:
        return key
    return Path(os.path.expanduser("~/.deepseek_api_key")).read_text().strip()


def call_evolver(prompt: str, model: str, temperature: float, max_tokens: int) -> str:
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "thinking": {"type": "disabled"},
        "response_format": {"type": "json_object"},
    }
    req = urllib.request.Request(
        "https://api.deepseek.com/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "Authorization": "Bearer " + deepseek_key()},
        method="POST",
    )
    for attempt in range(1, 5):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"]
        except Exception as exc:  # noqa: BLE001
            print(f"  [evolver] attempt {attempt} failed: {exc}", flush=True)
            time.sleep(3 * attempt)
    raise RuntimeError("evolver call failed after retries")


def close_unbalanced(fragment: str) -> str:
    """按字符串外的括号收支，把被截断的 JSON 片段补成可解析文本（补 `"` 与缺失的 `}`）。"""
    depth, in_str, esc = 0, False, False
    for ch in fragment:
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
    if in_str:
        fragment += '"'
    if depth > 0:
        fragment += "}" * depth
    return fragment


def extract_json_object(text: str) -> dict:
    """解析 evolver 输出的 JSON：容忍尾部残尾与缺失的收尾括号（模型偶发括号抖动）。"""
    text = text.strip()
    text = re.sub(r"^```(?:json)?|```$", "", text, flags=re.M).strip()
    start = text.find("{")
    if start < 0:
        raise ValueError(f"no JSON object in evolver output: {text[:200]}")
    fragment = text[start:]
    # 1) 标准路径：吃下第一个完整 JSON 值，忽略尾部多余字符（治 "Extra data" 型残尾）
    try:
        obj, _ = json.JSONDecoder().raw_decode(fragment)
        if isinstance(obj, dict):
            return obj
    except json.JSONDecodeError:
        pass
    # 2) 修复路径：补齐缺失的收尾（治 "Expecting ',' delimiter" 型截断）
    try:
        obj = json.loads(close_unbalanced(fragment))
        if isinstance(obj, dict):
            print("  [evolver] JSON 需修复收尾后解析", flush=True)
            return obj
    except json.JSONDecodeError:
        pass
    # 3) 兜底：旧行为（首 { 到末 } 整段解析），错误原样抛出
    end = text.rfind("}")
    if end > start:
        return json.loads(text[start:end + 1])
    raise ValueError(f"no JSON object in evolver output: {text[:200]}")


def build_evolution_prompt(parent_strategy: str, evidence: dict,
                           champion_history: list[dict], max_turns: int) -> str:
    if POLICY_SCHEMA == "behavior":
        return build_evolution_prompt_behavior(parent_strategy, evidence, champion_history, max_turns)
    return build_evolution_prompt_section(parent_strategy, evidence, champion_history, max_turns)


def build_evolution_prompt_section(parent_strategy: str, evidence: dict,
                                   champion_history: list[dict], max_turns: int) -> str:
    champion_view = [
        {"policy": e.get("policy"), "net": e.get("val_net"),
         "core": e.get("val_core"), "allslot": e.get("val_allslot"), "silent": e.get("val_silent")}
        for e in champion_history
    ]
    return f"""# Clarification Strategy

A modeling agent receives an incomplete business brief for an operations-research
problem. Before it declares itself ready to model, it may interview the client
(one question per turn, answered by the client) to recover the formulation-critical
facts that the brief omits. The `## Interaction Strategy` section of its policy
governs how it uses that interview: what it asks, when, and when it stops.

Your task is to write a better `## Interaction Strategy` section.

## Fixed around the section (you cannot change these)

- the agent model, the client simulator, the protocol detector and the judge are fixed;
- every response must be one line of the form `QUESTION: <one question>` or a
  `READY_TO_MODEL` summary; one question per turn; the interview may also end by
  hitting a hard turn cap of {max_turns};
- the briefs, hidden facts and judge rubrics are fixed and unknown to the agent;
- only the body of `## Interaction Strategy` may be rewritten;
- the strategy must not name any specific problem, entity, number or dataset fact.

## Scoring

Each run is scored on the hidden requirements the agent recovered:
- **Core Exact** (0/1): every P0/P1 hidden requirement was explicitly asked about;
- **All-Slot Exact** (0/1): every hidden requirement (including P2) was asked about;
- **Silent/run**: facts the agent treated as true without ever confirming them.

net = 0.5*Core + 0.5*AllSlot - 0.1*Silent.  All-or-nothing: one missed core
requirement zeroes Core. Asking more does not by itself help; asking the wrong
things costs turns and invites collapse.

## Current strategy

{parent_strategy}

## Evidence from the current strategy's evaluation (JSON)

Per case: the three metrics per repetition, the per-slot judge verdicts and the
**complete first-repetition dialogue** (agent questions and client answers).

{json.dumps(evidence, ensure_ascii=False)}

## Strategies with the best validation results so far, in chronological order (complete texts)

{json.dumps(champion_view, ensure_ascii=False)}

## Output rules

- Return ONE JSON object and nothing else.
- `policy_patch` is an object: {{"section": "## Interaction Strategy", "body": "<the entire new body of that section>"}}.
  The body must contain no markdown heading of any level.
- The body REPLACES the section body; it is not appended.
- The body may take ANY form you judge most effective -- linear rules, ordered
  steps, conditional branches, a portfolio of question archetypes routed by
  situation, a checklist, or anything else. Name kinds of situations rather than
  task topics.
- Stay generic: never copy task facts, entities, parameters or numbers out of the
  evidence, and never name a case.
- The body must be substantively different from the current strategy and from
  every strategy shown above; near-verbatim rewording is not acceptable.

## Required JSON shape

{{"policy_patch": {{"section": "## Interaction Strategy", "body": "..."}},
 "changed_components": ["## Interaction Strategy"],
 "evolution_rationale": "why these changes address what the evidence shows"}}
"""


def build_evolution_prompt_behavior(parent_strategy: str, evidence: dict,
                                    champion_history: list[dict], max_turns: int) -> str:
    """behavior schema 的演化 prompt（2026-10-09）：

    与 strategy_section 版的区别：可演化对象 = 一份**自由形态的交互策略文本**，
    由系统自行拼接进 agent 策略文档；输出格式/停轮等协议是固定 harness 机件，
    演化器既看不到也不得描述/复述（prompt 里只展示 current strategy 这段可变文本）。
    """
    champion_view = [
        {"policy": e.get("policy"), "net": e.get("val_net"),
         "core": e.get("val_core"), "allslot": e.get("val_allslot"), "silent": e.get("val_silent")}
        for e in champion_history
    ]
    return f"""# Clarification Strategy

A modeling agent receives an incomplete business brief for an operations-research
problem. Before it declares itself ready to model, it may interview the client
(one question per turn, answered by the client) to recover the formulation-critical
facts that the brief omits. A free-form **interaction strategy** governs how the
agent uses that interview: what it asks, when, and when it stops.

Your task is to write a better interaction strategy.

## Fixed around the strategy (you cannot change these)

- the agent model, the client simulator, the protocol detector and the judge are fixed;
- the output format and the stopping machinery are fixed harness protocol: every
  response is one `QUESTION:` line or a `READY_TO_MODEL` summary, one question per
  turn, and a hard turn cap of {max_turns} applies. **This machinery is inserted
  around your text by the system; you never see it and you never write it. Do not
  describe, restate or invent any output format, wrapper or stop command** —
  write the strategy as if the agent already knows the protocol;
- the briefs, hidden facts and judge rubrics are fixed and unknown to the agent;
- only the free-form interaction-strategy text may be rewritten;
- the strategy must not name any specific problem, entity, number or dataset fact.

## Scoring

Each run is scored on the hidden requirements the agent recovered:
- **Core Exact** (0/1): every P0/P1 hidden requirement was explicitly asked about;
- **All-Slot Exact** (0/1): every hidden requirement (including P2) was asked about;
- **Silent/run**: facts the agent treated as true without ever confirming them.

net = 0.5*Core + 0.5*AllSlot - 0.1*Silent.  All-or-nothing: one missed core
requirement zeroes Core. Asking more does not by itself help; asking the wrong
things costs turns and invites collapse.

## Current strategy (the only text you may rewrite; shown in full)

{parent_strategy}

## Evidence from the current strategy's evaluation (JSON)

Per case: the three metrics per repetition, the per-slot judge verdicts and the
**complete first-repetition dialogue** (agent questions and client answers).

{json.dumps(evidence, ensure_ascii=False)}

## Strategies with the best validation results so far, in chronological order (complete texts)

{json.dumps(champion_view, ensure_ascii=False)}

## Output rules

- Return ONE JSON object and nothing else.
- `policy_patch` is an object: {{"body": "<the entire new interaction strategy>"}}.
  The system inserts that text by itself in the right place; **return only the
  strategy text as `body` — no document sections, no headings, no surrounding
  document text, no protocol or output-format lines.**
- The body REPLACES the current strategy; it is not appended.
- The body may take ANY form you judge most effective -- linear rules, ordered
  steps, conditional branches, a portfolio of question archetypes routed by
  situation, a checklist, or anything else. Name kinds of situations rather than
  task topics.
- Stay generic: never copy task facts, entities, parameters or numbers out of the
  evidence, and never name a case.
- The body must be substantively different from the current strategy and from
  every strategy shown above; near-verbatim rewording is not acceptable.

## Required JSON shape

{{"policy_patch": {{"body": "..."}},
 "evolution_rationale": "why these changes address what the evidence shows"}}
"""


# ---------------------------------------------------------------------------
# 跑 case（每条 run 一个进程；并发上限 + 失败重试 + 断点续跑）
# ---------------------------------------------------------------------------

def _ensure_link(link: Path, target: Path) -> None:
    """确保 link 指向 target；已存在但目标已失效（如整个仓库目录被改名/移动）的软链接会被重指。"""
    if link.is_symlink():
        if link.resolve() != target.resolve():
            link.unlink()
            link.symlink_to(target)
    elif not link.exists():
        link.symlink_to(target)


def case_dir(case_id: str) -> Path:
    d = REPO_ROOT / "runs" / "evolution" / "cases" / case_id
    d.mkdir(parents=True, exist_ok=True)
    _ensure_link(d / f"{case_id}.toml", REPO_ROOT / "data" / f"{case_id}.toml")
    return d


def launch_case(policy_dir: Path, out_dir: Path, case_id: str, log_path: Path,
                max_turns: int) -> subprocess.Popen:
    env = os.environ.copy()
    env.update({
        "DEEPSEEK_BASE_URL": PROXY_BASE_URL,
        "DEEPSEEK_API_KEY": "x",
        "GENERIC_AGENT_MODEL": "qwen3.8-27b-fp8",
        "USER_SIMULATOR_MODEL": "qwen3.8-27b-fp8",
        "DETECTOR_MODEL": "qwen3.8-27b-fp8",
        "JUDGE_MODEL": "deepseek-flash",
    })
    cmd = [sys.executable, "-u", str(EVAL_PIPELINE),
           "--toml_dirs", str(case_dir(case_id)), "--limit", "1", "--k", "1",
           "--max_turns", str(max_turns), "--prompts_dir", str(policy_dir),
           "--output_dir", str(out_dir)]
    log = open(log_path, "a", encoding="utf-8")
    return subprocess.Popen(cmd, cwd=str(REPO_ROOT), env=env, stdout=log, stderr=subprocess.STDOUT)


def run_cases(policy_dir: Path, cases: list[str], passes: int, root: Path,
              tag: str, max_turns: int, concurrency: int, attempts: int = 3) -> dict:
    """跑 cases × passes 条 run，返回 {(case, pass): out_dir}。

    concurrency 是【每个 pass】的并发上限；三个 pass 同时推进，总并发 = passes × concurrency。
    断点续跑由 pipeline 自己负责（resume_state.json）。
    """
    root.mkdir(parents=True, exist_ok=True)
    logs = root / "logs"
    logs.mkdir(exist_ok=True)
    pending, done = [], {}
    for p in range(1, passes + 1):
        for cid in cases:
            od = root / f"{tag}_p{p}" / f"out_{cid}"
            if list(od.glob("**/judge_result.json")):
                done[(cid, p)] = od
            else:
                pending.append((cid, p, od))
    print(f"  [{tag}] 共 {len(cases)*passes} 条 run：已完成 {len(done)}，待跑 {len(pending)}"
          f"（每 pass 并发上限 {concurrency}，总 {passes}×{concurrency}={passes*concurrency}）", flush=True)

    for attempt in range(1, attempts + 1):
        queues: dict[int, list] = {p: [] for p in range(1, passes + 1)}
        for cid, p, od in pending:
            queues[p].append((cid, od))
        running: list[tuple] = []
        while any(queues.values()) or running:
            for p in range(1, passes + 1):
                active = sum(1 for item in running if item[1] == p)
                while queues[p] and active < concurrency:
                    cid, od = queues[p].pop(0)
                    log = logs / f"{tag}-{cid}-p{p}.log"
                    proc = launch_case(policy_dir, od, cid, log, max_turns)
                    running.append((cid, p, od, proc, log))
                    active += 1
            time.sleep(2)
            still = []
            for cid, p, od, proc, log in running:
                if proc.poll() is None:
                    still.append((cid, p, od, proc, log))
                else:
                    if list(od.glob("**/judge_result.json")):
                        done[(cid, p)] = od
                    else:
                        with open(log, encoding="utf-8") as fh:
                            tail = fh.read()[-400:]
                        print(f"  [{tag}] {cid} p{p} 未完成（attempt {attempt}）: {tail[-160:]!r}", flush=True)
            running = still
        pending = [(c, p, od) for (c, p, od) in pending if (c, p) not in done]
        if not pending:
            break
        print(f"  [{tag}] 第 {attempt} 轮结束仍缺 {len(pending)} 条，重试", flush=True)
    return done


# ---------------------------------------------------------------------------
# 判分
# ---------------------------------------------------------------------------

def score_case(out_dir: Path, case_id: str) -> dict:
    judge = json.loads(next(out_dir.glob("**/judge_result.json")).read_text())
    stats = json.loads(next(out_dir.glob("**/statistics.json")).read_text())
    transcript = json.loads(next(out_dir.glob("**/transcript.json")).read_text())
    rs = judge["restoration_summary"]
    core = 1.0 if rs["core_exact_restore"] else 0.0
    allslot = 1.0 if rs["all_slot_exact_restore"] else 0.0
    silent = float(stats.get("silent_assumption_count", 0) or 0)
    return {
        "core": core, "allslot": allslot, "silent": silent,
        "net": core * WEIGHTS["core"] + allslot * WEIGHTS["allslot"] - silent * WEIGHTS["silent"],
        "stopping": stats.get("stopping_status"),
        "ready": bool(stats.get("completed_ready_to_model")),
        "turns": stats.get("turn_count"),
        "slots": [{"slot_id": x["slot_id"], "severity": x["severity"], "hit": x["hit"]}
                  for x in judge["slot_scores"]],
        "dialogue": dialogue_view(transcript),
    }


WEIGHTS = {"core": 0.5, "allslot": 0.5, "silent": 0.1}


def score_many(run_dirs: dict[tuple, Path], cases: list[str], passes: int) -> tuple[dict, dict]:
    case_runs: dict[str, list[dict]] = {}
    for cid in cases:
        recs = []
        for p in range(1, passes + 1):
            od = run_dirs.get((cid, p))
            if od is None:
                continue
            recs.append(score_case(od, cid))
        if recs:
            case_runs[cid] = recs
    n = len(case_runs)
    agg = {
        "cases": n,
        "core": round(sum(sum(r["core"] for r in v) / len(v) for v in case_runs.values()) / max(1, n), 4),
        "allslot": round(sum(sum(r["allslot"] for r in v) / len(v) for v in case_runs.values()) / max(1, n), 4),
        "silent": round(sum(sum(r["silent"] for r in v) / len(v) for v in case_runs.values()) / max(1, n), 3),
    }
    agg["net"] = round(agg["core"] * WEIGHTS["core"] + agg["allslot"] * WEIGHTS["allslot"]
                       - agg["silent"] * WEIGHTS["silent"], 4)
    return agg, case_runs


# ---------------------------------------------------------------------------
# 策略文件管理
# ---------------------------------------------------------------------------

def make_policy_dir(root: Path, name: str, policy_text: str) -> Path:
    d = root / "policies" / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "generic_agent_prompt.md").write_text(policy_text, encoding="utf-8")
    for f in SYMLINKED_PROMPTS:
        _ensure_link(d / f, BASE_PROMPTS / f)
    return d


def make_prompt_dir_with_strategy(root: Path, name: str, strategy_body_text: str) -> Path:
    """以种子模板为底座，替换策略正文（按 schema 拼装；协议块保持原样）。"""
    template = (root / "seed_template.md").read_text(encoding="utf-8")
    patch = ({"body": strategy_body_text} if POLICY_SCHEMA == "behavior"
             else {"section": SEED_STRATEGY_SECTION, "body": strategy_body_text})
    patched = apply_policy_patch(template, patch)
    return make_policy_dir(root, name, patched)


# ---------------------------------------------------------------------------
# 主循环
# ---------------------------------------------------------------------------

def load_state(path: Path, config: dict) -> dict:
    if path.exists():
        state = json.loads(path.read_text(encoding="utf-8"))
        for k, v in config.items():
            state.setdefault("config", {}).setdefault(k, v)
        return state
    return {"config": config, "rounds": {}, "champion": None, "champion_history": [],
            "strategies_seen": []}


def write_state(path: Path, state: dict) -> None:
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    global POLICY_SCHEMA, PROXY_BASE_URL
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--rounds", type=int, default=5)
    ap.add_argument("--splits", default="runs/evolution/splits.json")
    ap.add_argument("--train-batch-size", type=int, default=8)
    ap.add_argument("--passes", type=int, default=3)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--concurrency", type=int, default=10, help="每个 pass 的并发上限；总并发 = passes × 该值")
    ap.add_argument("--sampling-seed", type=int, default=0)
    ap.add_argument("--selection-epsilon", type=float, default=0.0,
                    help="train 门/val 门的净分裕量：候选 net 须超过参照 + 该值（默认 0.0，对齐 OptMATH）")
    ap.add_argument("--seed-strategy", default=None,
                    help="初始策略段文件；默认用 round4 的策略")
    ap.add_argument("--template", default=None,
                    help="策略文档模板（含冻结段）；默认用 runs/prompts_evo4/generic_agent_prompt.md")
    ap.add_argument("--policy-schema", choices=["strategy_section", "behavior"], default="strategy_section",
                    help="可演化对象：strategy_section=旧线（## Interaction Strategy 段）；"
                         "behavior=新线（仅 ## Behavior 正文可变；协议 bullet 块冻结、由程序拼装，演化器不可见）")
    ap.add_argument("--proxy-base-url", default=PROXY_BASE_URL,
                    help="case 评测用的本地代理 base（默认 18770；judge-think 线用 18776）")
    ap.add_argument("--evolver-model", default="deepseek-flash")
    ap.add_argument("--evolver-temperature", type=float, default=0.667)
    ap.add_argument("--evolver-max-tokens", type=int, default=4000)
    ap.add_argument("--w-core", type=float, default=WEIGHTS["core"])
    ap.add_argument("--w-allslot", type=float, default=WEIGHTS["allslot"])
    ap.add_argument("--w-silent", type=float, default=WEIGHTS["silent"])
    args = ap.parse_args()

    WEIGHTS.update({"core": args.w_core, "allslot": args.w_allslot, "silent": args.w_silent})

    POLICY_SCHEMA = args.policy_schema
    PROXY_BASE_URL = args.proxy_base_url

    root = (REPO_ROOT / "runs" / "evolution" / args.name).resolve()
    root.mkdir(parents=True, exist_ok=True)
    splits = json.loads((REPO_ROOT / args.splits).read_text())
    train, val = splits["train"], splits["val"]

    template_path = Path(args.template) if args.template else REPO_ROOT / "runs" / "prompts_evo4" / "generic_agent_prompt.md"
    template = template_path.read_text(encoding="utf-8")
    (root / "seed_template.md").write_text(template, encoding="utf-8")
    seed_strategy = (Path(args.seed_strategy).read_text(encoding="utf-8") if args.seed_strategy
                     else strategy_body(template))

    state = load_state(root / "state.json", vars(args))
    write_state(root / "state.json", state)

    # ---- round 0: 种子策略 → val 基线 ----
    if "0" not in state["rounds"] or state["rounds"]["0"].get("status") != "done":
        print("[round 0] 种子策略在 val 上评测 ...", flush=True)
        seed_policy_dir = make_prompt_dir_with_strategy(root, "seed", seed_strategy)
        runs = run_cases(seed_policy_dir, val, args.passes, root / "round_0", "val",
                         args.max_turns, args.concurrency)
        agg, _ = score_many(runs, val, args.passes)
        state["champion"] = {"round": 0, "val_net": agg["net"], "strategy": seed_strategy}
        state["champion_history"].append({"round": 0, "policy": seed_strategy, "val_net": agg["net"],
                                          "val_core": agg["core"], "val_allslot": agg["allslot"],
                                          "val_silent": agg["silent"]})
        state["strategies_seen"].append(seed_strategy)
        state["rounds"]["0"] = {"status": "done", "val": agg}
        (root / "champion.md").write_text(seed_strategy, encoding="utf-8")
        write_state(root / "state.json", state)
        print(f"[round 0] val: core={agg['core']} allslot={agg['allslot']} silent={agg['silent']} net={agg['net']}", flush=True)

    # ---- rounds 1..N ----
    for r in range(1, args.rounds + 1):
        entry = state["rounds"].setdefault(str(r), {"status": "pending"})
        if entry.get("status") == "done":
            continue
        print(f"\n[round {r}] 开始", flush=True)
        batch = sample_batch(train, args.train_batch_size, args.sampling_seed, r)
        print(f"[round {r}] train batch ({len(batch)}): {batch}", flush=True)

        champion_strategy = state["champion"]["strategy"]
        champ_dir = make_prompt_dir_with_strategy(root, f"r{r}_champion", champion_strategy)
        truns = run_cases(champ_dir, batch, args.passes, root / f"round_{r}", "train",
                          args.max_turns, args.concurrency)
        agg, case_runs = score_many(truns, batch, args.passes)
        evidence = build_evidence_bundle(case_runs, agg, round_no=r)
        (root / f"round_{r}" / "evidence.json").write_text(
            json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[round {r}] train: core={agg['core']} allslot={agg['allslot']} silent={agg['silent']} net={agg['net']}", flush=True)

        prompt = build_evolution_prompt(champion_strategy, evidence,
                                        state["champion_history"][-3:], args.max_turns)
        (root / f"round_{r}" / "evolution_prompt.md").write_text(prompt, encoding="utf-8")
        raw = call_evolver(prompt, args.evolver_model, args.evolver_temperature, args.evolver_max_tokens)
        (root / f"round_{r}" / "evolution_response.txt").write_text(raw, encoding="utf-8")

        try:
            payload = extract_json_object(raw)
            patch = payload["policy_patch"]
            candidate_policy = apply_policy_patch(template, patch)
            candidate_body = strategy_body(candidate_policy)
            assert_fixed_unchanged(candidate_policy, template)
            assert_new_strategy(candidate_body, state["strategies_seen"])
        except Exception as exc:  # noqa: BLE001
            print(f"[round {r}] 候选策略不合法（{exc}），跳过本轮", flush=True)
            entry.update({"status": "done", "skipped": str(exc), "train": agg})
            write_state(root / "state.json", state)
            continue

        cand_dir = make_policy_dir(root, f"r{r}_candidate", candidate_policy)

        print(f"[round {r}] 候选策略生成完成，ctrain 门评测（同一 batch {len(batch)} 题 × {args.passes} pass）...", flush=True)
        ctruns = run_cases(cand_dir, batch, args.passes, root / f"round_{r}", "ctrain",
                           args.max_turns, args.concurrency)
        cagg, _ = score_many(ctruns, batch, args.passes)
        accepted_train = cagg["net"] > agg["net"] + args.selection_epsilon
        print(f"[round {r}] ctrain: core={cagg['core']} allslot={cagg['allslot']} silent={cagg['silent']} net={cagg['net']} "
              f"vs 父本 {agg['net']} → {'过门 ✅' if accepted_train else '未过门 ❌（跳过 val）'}", flush=True)
        if not accepted_train:
            entry.update({"status": "done", "train": agg, "ctrain": cagg, "accepted_train": False,
                          "promoted": False, "candidate_body": candidate_body})
            state["strategies_seen"].append(candidate_body)
            write_state(root / "state.json", state)
            continue

        print(f"[round {r}] val 评测 ...", flush=True)
        vruns = run_cases(cand_dir, val, args.passes, root / f"round_{r}", "val",
                          args.max_turns, args.concurrency)
        vagg, _ = score_many(vruns, val, args.passes)
        promoted = vagg["net"] > state["champion"]["val_net"] + args.selection_epsilon
        print(f"[round {r}] val: core={vagg['core']} allslot={vagg['allslot']} silent={vagg['silent']} net={vagg['net']} "
              f"→ {'晋级 ✅' if promoted else '未超过冠军 ❌'}", flush=True)
        entry.update({"status": "done", "train": agg, "ctrain": cagg, "accepted_train": True,
                      "val": vagg, "promoted": promoted, "candidate_body": candidate_body})
        state["strategies_seen"].append(candidate_body)
        if promoted:
            state["champion"] = {"round": r, "val_net": vagg["net"], "strategy": candidate_body}
            state["champion_history"].append({"round": r, "policy": candidate_body, "val_net": vagg["net"],
                                              "val_core": vagg["core"], "val_allslot": vagg["allslot"],
                                              "val_silent": vagg["silent"]})
            (root / "champion.md").write_text(candidate_body, encoding="utf-8")
        write_state(root / "state.json", state)

    print(f"\n完成。冠军：round {state['champion']['round']}（val net {state['champion']['val_net']}）", flush=True)
    print(f"冠军策略：{root / 'champion.md'}", flush=True)


if __name__ == "__main__":
    main()
