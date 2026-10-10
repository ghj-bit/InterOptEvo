#!/usr/bin/env python3
"""演化线「缺跑」外科补跑器（2026-10-09）。

规则（用户拍板）：某条 run 走完"单调用 5 次空返回重试 → case 级 3 次 attempt 仍缺"后，
**只补跑那一支小实验（单个 case×pass），绝不重跑任何已成功的 run**。

实现：
  1) 扫描 <root>/round_N/{train,ctrain,val}_pK/out_orclarify_XXX 中缺 judge_result.json 的；
  2) 按 phase 推断 prompts_dir：round 0 → policies/seed；train → policies/r{N}_champion；
     ctrain/val → policies/r{N}_candidate；
  3) 经 18777（judge-think + FP8 空返回守卫）断点续跑该 run（resume_state 自动接管），
     只写它自己的 output_dir；
  4) 逐条核验 judge_result.json 并打印 score_case。

用法: python tools/evo_rescue_missing.py [--name evo_r30_from_ask_anything] [--base http://127.0.0.1:18777/v1]
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

THIS = Path(__file__).resolve()
REPO = THIS.parents[1]
sys.path.insert(0, str(THIS.parent))
import orclarify_evolution as OE  # noqa: E402

EVAL_PIPELINE = REPO / "experiments" / "evaluation_protocol" / "run_pipeline.py"


def policy_dir_for(root: Path, phase_dir: Path) -> Path:
    r = int(re.search(r"round_(\d+)", phase_dir.parent.name).group(1))
    ph = phase_dir.name.split("_")[0]  # train / ctrain / val
    if r == 0:
        name = "seed"
    else:
        name = f"r{r}_champion" if ph == "train" else f"r{r}_candidate"
    d = root / "policies" / name
    if not d.exists():
        raise SystemExit(f"policy dir missing: {d}")
    return d


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", default="evo_r30_from_ask_anything")
    ap.add_argument("--base", default="http://127.0.0.1:18777/v1")
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    root = REPO / "runs" / "evolution" / args.name
    missing = []
    for ph in sorted(root.glob("round_*/???_p*")):
        for od in sorted(ph.glob("out_orclarify_*")):
            if not list(od.glob("**/judge_result.json")):
                missing.append(od)
    print(f"[rescue] {args.name}: 缺 {len(missing)} 条", flush=True)
    if args.dry_run or not missing:
        for od in missing:
            print("  ", od.relative_to(root))
        return

    log_dir = root / "_rescue_logs"
    log_dir.mkdir(exist_ok=True)
    env = os.environ.copy()
    env.update({"DEEPSEEK_BASE_URL": args.base, "DEEPSEEK_API_KEY": "x",
                "GENERIC_AGENT_MODEL": "qwen3.8-27b-fp8",
                "USER_SIMULATOR_MODEL": "qwen3.8-27b-fp8",
                "DETECTOR_MODEL": "qwen3.8-27b-fp8",
                "JUDGE_MODEL": "deepseek-flash"})
    ok = 0
    for od in missing:
        cid = od.name.replace("out_", "")
        pd = policy_dir_for(root, od)
        tag = f"{od.parent.parent.name}-{od.parent.name}-{cid}"
        log = open(log_dir / f"{tag}.log", "a", encoding="utf-8")
        print(f"[rescue] 补跑 {tag}（prompts={pd.name}）...", flush=True)
        cmd = [sys.executable, "-u", str(EVAL_PIPELINE),
               "--toml_dirs", str(REPO / "runs" / "evolution" / "cases" / cid),
               "--limit", "1", "--k", "1", "--max_turns", str(args.max_turns),
               "--prompts_dir", str(pd), "--output_dir", str(od)]
        subprocess.run(cmd, cwd=str(REPO), env=env, stdout=log, stderr=subprocess.STDOUT)
        log.close()
        if list(od.glob("**/judge_result.json")):
            r = OE.score_case(od, cid)
            print(f"    ✅ 补齐 core={r['core']} net={r['net']} turns={r['turns']}", flush=True)
            ok += 1
        else:
            print("    ❌ 仍缺（查看 _rescue_logs）", flush=True)
    print(f"[rescue] 完成 {ok}/{len(missing)}；注意：不外推改 state 历史（门槛已定），"
          f"如需复算受影响轮次请单独核对。", flush=True)


if __name__ == "__main__":
    main()
