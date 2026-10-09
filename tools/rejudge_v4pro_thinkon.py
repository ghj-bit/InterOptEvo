#!/usr/bin/env python3
"""对 freeqa_baseline_v4pro_nothink 的 100 份 transcript 用 v4pro(think 开) 重新判分（不重跑交互）。

- 判分请求与 pipeline 逐字段一致：system=prompts/judge_prompt.md，user=已存的 judge_prompt_user_message.md，
  temperature=0.0，timeout=240，**不带 thinking 字段 → 该 API 默认开启推理**（对照组：原 run 经 nothink 代理判分）。
- 解析与后处理复用 run_pipeline 的函数：extract_json_object / calculate_weighted_slot_score /
  calculate_restoration_summary / audit_stopping_behavior（3 次解析重试同 pipeline）。
- 新判分写到影子目录 runs/freeqa_baseline_v4pro_nothink/rejudge_thinkon/out_XXX/...（原 judge_result.json 不动），
  statistics/transcript 软链原始文件，供 orclarify_evolution.score_case 直接评分。
用法: python tools/rejudge_v4pro_thinkon.py [--concurrency 8]
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
SHADOW = Path(os.getenv("REJUDGE_SHADOW") or (RUN / "rejudge_thinkon"))
JUDGE_SYS = (REPO / "experiments" / "evaluation_protocol" / "prompts" / "judge_prompt.md").read_text(encoding="utf-8").strip()
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
RETRY_MSG = (
    "Your previous judge output was not valid JSON. "
    "Return only one valid JSON object that follows the required schema. "
    "Do not include markdown fences or unescaped line breaks inside JSON strings."
)


def judge_once(messages: list[dict]) -> str:
    body = json.dumps({"model": MODEL, "messages": messages, "temperature": 0.0}).encode()
    req = urllib.request.Request(BASE + "/chat/completions", data=body,
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + KEY})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    u = d.get("usage") or {}
    rt = (u.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
    return d["choices"][0]["message"].get("content") or "", rt


def rejudge_case(cid: str) -> dict:
    t0 = time.time()
    src = RUN / f"out_{cid}" / "generic_agent" / "run_01" / cid
    umsg = (src / "judge_prompt_user_message.md").read_text(encoding="utf-8")
    stats = json.loads((src / "statistics.json").read_text(encoding="utf-8"))
    completed = bool(stats.get("completed_ready_to_model"))
    messages = [{"role": "system", "content": JUDGE_SYS}, {"role": "user", "content": umsg}]
    parse_errs = []
    reasoning_total = 0
    for attempt in range(1, 4):
        raw, rt = judge_once(messages)
        reasoning_total += rt
        try:
            result = RP.extract_json_object(raw)
            break
        except Exception as exc:
            parse_errs.append(f"attempt {attempt}: {exc}")
            if attempt >= 3:
                raise
            messages = messages + [{"role": "assistant", "content": raw}, {"role": "user", "content": RETRY_MSG}]
    if parse_errs:
        result["judge_parse_errors_before_success"] = parse_errs
    result["weighted_summary"] = RP.calculate_weighted_slot_score(result.get("slot_scores", []))
    result["restoration_summary"] = RP.calculate_restoration_summary(result.get("slot_scores", []))
    result["stopping_consistency_audit"] = RP.audit_stopping_behavior(
        result.get("slot_scores", []), result.get("stopping_behavior") or {}, completed)
    dst = SHADOW / f"out_{cid}" / "generic_agent" / "run_01" / cid
    dst.mkdir(parents=True, exist_ok=True)
    (dst / "judge_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    for fn in ("statistics.json", "transcript.json"):
        link = dst / fn
        if not link.exists():
            link.symlink_to(src / fn)
    return {"cid": cid, "elapsed": time.time() - t0, "parse_retries": len(parse_errs),
            "reasoning_tokens": reasoning_total,
            "core_exact": result["restoration_summary"]["core_exact_restore"],
            "allslots_exact": result["restoration_summary"]["all_slot_exact_restore"]}


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
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--cases", default="1-100", help="题号范围/列表，如 1-100 或 1,55")
    args = ap.parse_args()
    global CASES
    CASES = parse_cases(args.cases)
    SHADOW.mkdir(parents=True, exist_ok=True)
    log = (SHADOW / "rejudge.log").open("a", encoding="utf-8")
    print(f"[rejudge] {len(CASES)} 题 | judge={MODEL}(think 默认开, 直连) | 并发 {args.concurrency}", flush=True)
    ok, fail = [], []
    with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
        futs = {pool.submit(rejudge_case, cid): cid for cid in CASES}
        for f in as_completed(futs):
            cid = futs[f]
            try:
                r = f.result()
                ok.append(r)
                line = f"[{time.strftime('%H:%M:%S')}] {cid} {r['elapsed']:.0f}s reasoning={r['reasoning_tokens']} " \
                       f"core={r['core_exact']} allslot={r['allslots_exact']} retries={r['parse_retries']}"
            except Exception as exc:
                fail.append(cid)
                line = f"[{time.strftime('%H:%M:%S')}] {cid} FAILED: {exc}"
            print(line, flush=True)
            log.write(line + "\n")
    print(f"\n[rejudge] 成功 {len(ok)}/{len(CASES)}，失败 {fail}", flush=True)

    # ---- 双版本评分对比 ----
    orig, new = {}, {}
    for cid in CASES:
        od = RUN / f"out_{cid}"
        sd = SHADOW / f"out_{cid}"
        try:
            orig[cid] = OE.score_case(od, cid)
        except Exception as exc:
            print(f"  orig score fail {cid}: {exc}")
        if sd.exists() and list(sd.glob("**/judge_result.json")):
            try:
                new[cid] = OE.score_case(sd, cid)
            except Exception as exc:
                print(f"  new score fail {cid}: {exc}")
    inelig = {c for c in new if (json.loads(next((SHADOW / f'out_{c}').glob('**/judge_result.json')).read_text())
                                 .get("restoration_summary", {}).get("core_slot_count", 0) or 0) == 0}
    ao, an = aggregate(orig), aggregate(new)
    fo, fn = elig_fixed(orig, inelig), elig_fixed(new, inelig)
    flips_core = [c for c in new if orig.get(c, {}).get("core") != new[c]["core"]]
    flips_all = [c for c in new if orig.get(c, {}).get("allslot") != new[c]["allslot"]]
    w = l = t = 0
    for c in new:
        d = new[c]["net"] - orig[c]["net"]
        if abs(d) < 1e-9: t += 1
        elif d > 0: w += 1
        else: l += 1
    summary = {"orig": ao, "orig_fixed": fo, "new": an, "new_fixed": fn,
               "ineligible": sorted(inelig),
               "flips": {"core": {"up": [c for c in flips_core if new[c]['core'] > orig[c]['core']],
                                  "down": [c for c in flips_core if new[c]['core'] < orig[c]['core']]},
                         "allslot": {"up": [c for c in flips_all if new[c]['allslot'] > orig[c]['allslot']],
                                     "down": [c for c in flips_all if new[c]['allslot'] < orig[c]['allslot']]}},
               "new_vs_orig_net": {"win": w, "loss": l, "tie": t}}
    (SHADOW / "compare.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n===== 对比 =====")
    print(f"原判分(think关):  core={ao['core']:.4f} allslot={ao['allslot']:.4f} silent={ao['silent']:.4f} net={ao['net']:.4f} | elig修正 net={fo['net']:.4f}")
    print(f"重评(think开):    core={an['core']:.4f} allslot={an['allslot']:.4f} silent={an['silent']:.4f} net={an['net']:.4f} | elig修正 net={fn['net']:.4f}")
    print(f"逐题(重评−原)net: win {w} / loss {l} / tie {t}")
    print(f"core 翻转: {len(flips_core)} 题 (up {len(summary['flips']['core']['up'])} / down {len(summary['flips']['core']['down'])})；"
          f"allslot 翻转: {len(flips_all)} 题 (up {len(summary['flips']['allslot']['up'])} / down {len(summary['flips']['allslot']['down'])})")
    log.close()


if __name__ == "__main__":
    main()
