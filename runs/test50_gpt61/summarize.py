#!/usr/bin/env python3
"""汇总 runs/test50_gpt61：逐题 core/allslot/silent/net + 聚合（与演化线同口径 score_many）。"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../InterOpt/runs/test50_gpt61
REPO = HERE.parents[1]                          # .../InterOpt
sys.path.insert(0, str(REPO / "tools"))
import orclarify_evolution as OE  # noqa: E402

splits = json.loads((REPO / "runs/evolution/splits.json").read_text())
cases = splits["test"]
runs = {}
for cid in cases:
    od = HERE / f"out_{cid}"
    if od.exists() and list(od.glob("**/judge_result.json")):
        runs[(cid, 1)] = od
agg, case_runs = OE.score_many(runs, cases, 1)
print(f"完成 {len(runs)}/{len(cases)}")
rows = {}
for cid in cases:
    rs = case_runs.get(cid)
    if not rs:
        print(f"  {cid}  MISSING")
        continue
    r = rs[0]
    rows[cid] = {"core": r["core"], "allslot": r["allslot"], "silent": r["silent"], "net": round(r["net"], 4),
                 "stopping": r["stopping"], "turns": r["turns"]}
    print(f"  {cid}  core={r['core']} allslot={r['allslot']} silent={r['silent']} net={r['net']:.3f}")
print("聚合:", agg)
(HERE / "summary.json").write_text(json.dumps({"agg": agg, "cases": rows}, ensure_ascii=False, indent=2), encoding="utf-8")
print("已写", HERE / "summary.json")
