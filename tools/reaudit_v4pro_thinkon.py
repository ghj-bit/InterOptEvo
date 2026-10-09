#!/usr/bin/env python3
"""v4pro baseline 的「detector + judge 全 think 开」重评（不重跑交互）。

三段：
  1) detector 重放（think 开）：对 detector_events.json 里每个已审 agent 当问，
     按 pipeline 逐字段重放 detector 调用（system=question_detector_prompt.md,
     user="Assistant latest response:\\n\\n"+当问, temp 0），解析用 run_pipeline 的
     extract_json_object + normalize_detector_result。结果存 shadow/detector_events_thinkon.json。
     **detector 不进评分**（评分=judge.restoration + statistics.silent），这里是对"审计层"的一致性检查。
  2) judge：直接复用上一轮 rejudge_thinkon/ 里已生成的 think-开 judge_result.json（不重复判分）。
  3) silent 重算 + 重打分：silent_assumption_count 的真实来源是 judge 的 silent_assumptions
     （run_pipeline:1196），上一轮重评沿用了旧 statistics 的 silent；本轮把新 judge 的 silent
     写回 shadow 的 statistics.json，再用 orclarify_evolution.score_case 重打分，给出三行对比表。

用法: python tools/reaudit_v4pro_thinkon.py [--concurrency 10]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

THIS = Path(__file__).resolve()
REPO = THIS.parents[1]
sys.path.insert(0, str(REPO / "experiments" / "evaluation_protocol"))
sys.path.insert(0, str(THIS.parent))
import run_pipeline as RP  # noqa: E402
import orclarify_evolution as OE  # noqa: E402

RUN = REPO / "runs" / "freeqa_baseline_v4pro_nothink"
SHADOW = RUN / "rejudge_thinkon"
DETECTOR_SYS = (REPO / "experiments" / "evaluation_protocol" / "prompts" / "question_detector_prompt.md").read_text(encoding="utf-8").strip()
MODEL = "deepseek-v4-pro"
BASE = os.getenv("REJUDGE_BASE_URL", "https://api.deepseek.com")
KEY = [l.split("=", 1)[1].strip() for l in (REPO / ".env").read_text().splitlines() if l.startswith("DEEPSEEK_API_KEY")][0]
CASES = [f"orclarify_{i:03d}" for i in range(1, 101)]


def parse_cases(spec: str) -> list[str]:
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out += [f"orclarify_{i:03d}" for i in range(int(a), int(b) + 1)]
        elif part:
            out.append(f"orclarify_{int(part):03d}")
    return out


def detector_call(agent_response: str) -> tuple[dict | None, str, int]:
    messages = [{"role": "system", "content": DETECTOR_SYS},
                {"role": "user", "content": "Assistant latest response:\n\n" + agent_response}]
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": 0.0}).encode()
    req = urllib.request.Request(BASE + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    raw = d["choices"][0]["message"].get("content") or ""
    rt = ((d.get("usage") or {}).get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
    try:
        res = RP.normalize_detector_result(RP.extract_json_object(raw))
    except Exception:
        res = None
    return res, raw, rt


def reaudit_case(cid: str) -> dict:
    t0 = time.time()
    src = RUN / f"out_{cid}" / "generic_agent" / "run_01" / cid
    orig_events = json.loads((src / "detector_events.json").read_text(encoding="utf-8"))
    new_events = []
    changed = {"action": 0, "question_count": 0, "is_atomic": 0, "parse_err": 0}
    total_reasoning = 0
    for ev in orig_events:
        res, raw, rt = detector_call(ev["agent_response"])
        total_reasoning += rt
        o = ev.get("detector_result")
        rec = {"turn": ev.get("turn"), "agent_response": ev["agent_response"],
               "detector_raw_thinkon": raw, "detector_result_thinkon": res}
        if res is None:
            changed["parse_err"] += 1
        elif o is not None:
            if res.get("action") != o.get("action"):
                changed["action"] += 1
            if res.get("question_count") != o.get("question_count"):
                changed["question_count"] += 1
            if res.get("is_atomic") != o.get("is_atomic"):
                changed["is_atomic"] += 1
        new_events.append(rec)
    dst = SHADOW / f"out_{cid}" / "generic_agent" / "run_01" / cid
    dst.mkdir(parents=True, exist_ok=True)
    (dst / "detector_events_thinkon.json").write_text(json.dumps(new_events, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"cid": cid, "n": len(orig_events), "elapsed": time.time() - t0,
            "reasoning": total_reasoning, "changed": changed}


def aggregate(scores: dict) -> dict:
    n = len(scores)
    c = sum(s["core"] for s in scores.values()) / n
    a = sum(s["allslot"] for s in scores.values()) / n
    s = sum(s["silent"] for s in scores.values()) / n
    return {"cases": n, "core": c, "allslot": a, "silent": s, "net": 0.5 * c + 0.5 * a - 0.1 * s}


def elig_fixed(scores: dict, inelig: set) -> dict:
    elig = [c for c in scores if c not in inelig]
    C = sum(scores[c]["core"] for c in elig) / len(elig)
    A = sum(scores[c]["allslot"] for c in scores) / len(scores)
    S = sum(scores[c]["silent"] for c in scores) / len(scores)
    return {"core": C, "allslot": A, "silent": S, "net": 0.5 * C + 0.5 * A - 0.1 * S}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=10)
    ap.add_argument("--cases", default="1-100")
    args = ap.parse_args()
    global CASES
    CASES = parse_cases(args.cases)

    # ---- 1) detector 重放 ----
    print(f"[reaudit] detector 重放（think 开）：{len(CASES)} 题", flush=True)
    results, fails = [], []
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futs = {pool.submit(reaudit_case, cid): cid for cid in CASES}
        for f in as_completed(futs):
            cid = futs[f]
            try:
                r = f.result()
                results.append(r)
                print(f"[{time.strftime('%H:%M:%S')}] {cid} n={r['n']} 变: {r['changed']} ({r['elapsed']:.0f}s)", flush=True)
            except Exception as exc:
                fails.append(cid)
                print(f"[{time.strftime('%H:%M:%S')}] {cid} FAILED: {exc}", flush=True)
    tot = {k: sum(r["changed"][k] for r in results) for k in ("action", "question_count", "is_atomic", "parse_err")}
    n_calls = sum(r["n"] for r in results)
    print(f"[reaudit] 成功 {len(results)}/{len(CASES)}，失败 {fails}；共重放 {n_calls} 次 detector 调用；"
          f"分类变化 action={tot['action']} question_count={tot['question_count']} is_atomic={tot['is_atomic']} 解析失败={tot['parse_err']}", flush=True)

    # ---- 2)+3) silent 重算 + 重打分 ----
    orig, new = {}, {}
    silent_delta = []
    for cid in CASES:
        od = RUN / f"out_{cid}"
        sd = SHADOW / f"out_{cid}"
        src = od / "generic_agent" / "run_01" / cid
        dst = sd / "generic_agent" / "run_01" / cid
        new_j = json.loads((dst / "judge_result.json").read_text(encoding="utf-8"))
        new_silent = len(new_j.get("silent_assumptions") or [])
        stats = json.loads((src / "statistics.json").read_text(encoding="utf-8"))
        old_silent = int(stats.get("silent_assumption_count", 0) or 0)
        silent_delta.append((cid, old_silent, new_silent))
        if new_silent != old_silent:
            stats["silent_assumption_count"] = new_silent
            link = dst / "statistics.json"
            if link.is_symlink():
                link.unlink()
            (dst / "statistics.json").write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
        try:
            orig[cid] = OE.score_case(od, cid)
            new[cid] = OE.score_case(sd, cid)
        except Exception as exc:
            print(f"  score fail {cid}: {exc}")

    inelig = {"orclarify_007", "orclarify_025", "orclarify_037", "orclarify_064", "orclarify_072", "orclarify_085"}
    # 上一轮口径（judge 换、silent 沿用旧）：暂时把 shadow 的 statistics 视为旧值不可得——
    # 直接在 orig 的 silent 上替换 core/allslot 即可复原：net_j = 0.5*new.core + 0.5*new.allslot - 0.1*orig.silent
    prev = {c: {"core": new[c]["core"], "allslot": new[c]["allslot"], "silent": orig[c]["silent"],
                "net": 0.5 * new[c]["core"] + 0.5 * new[c]["allslot"] - 0.1 * orig[c]["silent"]} for c in new}
    ao, an, ap_ = aggregate(orig), aggregate(new), aggregate(prev)
    fo, fn = elig_fixed(orig, inelig), elig_fixed(new, inelig)
    w = l = t = 0
    for c in new:
        d = new[c]["net"] - orig[c]["net"]
        if abs(d) < 1e-9: t += 1
        elif d > 0: w += 1
        else: l += 1
    silent_changed = [(c, o, n) for c, o, n in silent_delta if o != n]

    summary = {"orig": ao, "prev_judge_only": ap_, "new": an, "orig_fixed": fo, "new_fixed": fn,
               "detector_replay": {"calls": n_calls, "changed": tot, "fails": fails},
               "silent_changed_cases": silent_changed,
               "new_vs_orig_net": {"win": w, "loss": l, "tie": t}}
    (SHADOW / "reaudit_compare.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n===== 三口径对比 =====")
    print(f"A 原（全 think 关）:            core={ao['core']:.4f} allslot={ao['allslot']:.4f} silent={ao['silent']:.4f} net={ao['net']:.4f} | 修正 {fo['net']:.4f}")
    print(f"B 仅 judge think 开（上轮口径）: core={ap_['core']:.4f} allslot={ap_['allslot']:.4f} silent={ap_['silent']:.4f} net={ap_['net']:.4f}")
    print(f"C 本轮 judge+detector think 开:  core={an['core']:.4f} allslot={an['allslot']:.4f} silent={an['silent']:.4f} net={an['net']:.4f} | 修正 {fn['net']:.4f}")
    print(f"silent 重算后有变化的题: {len(silent_changed)} → {silent_changed[:10]}")
    print(f"C vs A 逐题: win {w} / loss {l} / tie {t}")


if __name__ == "__main__":
    main()
