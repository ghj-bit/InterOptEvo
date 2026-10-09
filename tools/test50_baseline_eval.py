#!/usr/bin/env python3
"""test50 × deepseek-flash「无策略 baseline」评测驱动（2026-10-09 新建）。

与 tools/test50_eval.py 的 ds 臂逐字段一致，**唯一差异 = prompts_dir**：
用仓库原生 baseline（experiments/evaluation_protocol/prompts，无 Interaction Strategy 段）。
即与 runs/test50_gpt61（gpt-6.1-sol baseline）同设计的 deepseek-flash 版——
两者只差 agent 模型（gpt-6.1-sol vs deepseek-flash）。

臂：agent=deepseek-flash（经 127.0.0.1:18772 cap_proxy_dsagent 路由），
    user_simulator / detector = qwen3.8-27b-fp8（本地 FP8），judge = deepseek-flash（远端）。
题集：orclarify_051–100（与 train/val 零重叠，== splits["test"]）。
计分：复用演化线 score_many（同一判分口径）+ eligibility 修正（无 P0/P1 槽的题从 C 项剔除）。

用法: python tools/test50_baseline_eval.py [--concurrency 20] [--cases 51-100] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

THIS = Path(__file__).resolve()
REPO = THIS.parents[1]
EVAL_PIPELINE = REPO / "experiments" / "evaluation_protocol" / "run_pipeline.py"
PROMPTS = REPO / "experiments" / "evaluation_protocol" / "prompts"  # 原生 baseline，无策略段
ROOT = REPO / "runs" / "test50_baseline_dsflash"
CASES = [f"orclarify_{i:03d}" for i in range(51, 101)]
ARM = {"agent": "deepseek-flash", "base": "http://127.0.0.1:18772/v1", "out": ROOT}


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


def case_dir(cid: str) -> Path:
    d = ROOT / "cases" / cid
    d.mkdir(parents=True, exist_ok=True)
    link = d / f"{cid}.toml"
    tgt = REPO / "data" / f"{cid}.toml"
    if link.is_symlink():
        if link.resolve() != tgt.resolve():
            link.unlink(); link.symlink_to(tgt)
    elif not link.exists():
        link.symlink_to(tgt)
    return d


def launch(cid: str, out_dir: Path, log_path: Path, max_turns: int) -> subprocess.Popen:
    env = os.environ.copy()
    env.update({
        "DEEPSEEK_BASE_URL": ARM["base"],
        "DEEPSEEK_API_KEY": "x",
        "GENERIC_AGENT_MODEL": ARM["agent"],
        "USER_SIMULATOR_MODEL": "qwen3.8-27b-fp8",
        "DETECTOR_MODEL": "qwen3.8-27b-fp8",
        "JUDGE_MODEL": "deepseek-flash",
    })
    cmd = [sys.executable, "-u", str(EVAL_PIPELINE),
           "--toml_dirs", str(case_dir(cid)), "--limit", "1", "--k", "1",
           "--max_turns", str(max_turns), "--prompts_dir", str(PROMPTS),
           "--output_dir", str(out_dir)]
    log = open(log_path, "a", encoding="utf-8")
    return subprocess.Popen(cmd, cwd=str(REPO), env=env, stdout=log, stderr=subprocess.STDOUT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=20)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--cases", default="51-100", help="题号范围/列表，如 51-100 或 51,55,60")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    global CASES
    CASES = parse_cases(args.cases)
    out_root: Path = ARM["out"]
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "logs").mkdir(exist_ok=True)
    t0 = time.time()

    # 预检：代理可达
    try:
        with urllib.request.urlopen(ARM["base"] + "/models", timeout=5) as r:
            ok = r.status == 200
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[baseline:ds] 预检失败：{ARM['base']} 不可达（{exc}）", flush=True)
    print(f"[baseline:ds] prompts=upstream-baseline agent={ARM['agent']} base={ARM['base']} 预检={'OK' if ok else 'FAIL'}", flush=True)

    pending, done = [], {}
    for cid in CASES:
        od = out_root / f"out_{cid}"
        if list(od.glob("**/judge_result.json")):
            done[cid] = od
        else:
            pending.append((cid, od))
    print(f"[baseline:ds] 共 {len(CASES)} 题：已完成 {len(done)}，待跑 {len(pending)}（并发 {args.concurrency}）", flush=True)
    if args.dry_run:
        return

    for attempt in range(1, args.attempts + 1):
        queue = list(pending)
        running: list[tuple] = []
        while queue or running:
            while queue and len(running) < args.concurrency:
                cid, od = queue.pop(0)
                log_path = out_root / "logs" / f"ds-{cid}.log"
                running.append((cid, od, launch(cid, od, log_path, args.max_turns)))
            time.sleep(3)
            still = []
            for cid, od, proc in running:
                if proc.poll() is None:
                    still.append((cid, od, proc))
                elif list(od.glob("**/judge_result.json")):
                    done[cid] = od
                    print(f"[baseline:ds] {cid} 完成（{len(done)}/{len(CASES)}）", flush=True)
                else:
                    print(f"[baseline:ds] {cid} 未完成（attempt {attempt}）", flush=True)
            running = still
        pending = [(c, o) for c, o in pending if c not in done]
        if not pending:
            break
        print(f"[baseline:ds] 第 {attempt} 轮结束仍缺 {len(pending)} 条，重试", flush=True)

    # ---- 计分（复用演化线 score_many，与 A/B/C 臂同口径）----
    sys.path.insert(0, str(THIS.parent))
    import orclarify_evolution as OE  # noqa: E402
    run_dirs = {(cid, 1): od for cid, od in done.items()}
    agg, case_runs = OE.score_many(run_dirs, CASES, 1)
    print(f"\n[baseline:ds] 完成 {agg['cases']}/{len(CASES)} 题；缺失: {[c for c in CASES if c not in case_runs]}", flush=True)
    print(f"{'case':<16}{'core':>7}{'allslot':>8}{'silent':>7}{'net':>8}{'turns':>7}", flush=True)
    per_case = {}
    inelig = []
    for cid in CASES:
        if cid not in case_runs:
            continue
        r = case_runs[cid][0]
        per_case[cid] = {k: r[k] for k in ("core", "allslot", "silent", "net")}
        per_case[cid]["stopping"] = r.get("stopping")
        per_case[cid]["turns"] = r.get("turns")
        jr = json.loads(next((done[cid]).glob("**/judge_result.json")).read_text())
        rs = jr.get("restoration_summary") or {}
        if (rs.get("core_slot_count", 0) or 0) == 0:
            inelig.append(cid)
        print(f"{cid:<16}{r['core']:>7}{r['allslot']:>8}{r['silent']:>7}{r['net']:>8}{str(r.get('turns')):>7}", flush=True)
    print(f"aggregate: core={agg['core']} allslot={agg['allslot']} silent={agg['silent']} net={agg['net']}", flush=True)

    fixed = None
    if inelig:
        elig = [c for c in per_case if c not in inelig]
        C = sum(per_case[c]["core"] for c in elig) / len(elig)
        A = sum(per_case[c]["allslot"] for c in per_case) / len(per_case)
        S = sum(per_case[c]["silent"] for c in per_case) / len(per_case)
        fixed = {"core": round(C, 4), "allslot": round(A, 4), "silent": round(S, 3),
                 "net": round(0.5 * C + 0.5 * A - 0.1 * S, 4)}
        print(f"eligibility 修正（剔除 {inelig}）: core={fixed['core']} net={fixed['net']}", flush=True)

    summary = {
        "arm": "dsflash_baseline", "agent_model": ARM["agent"], "policy": "upstream-baseline(no strategy)",
        "prompts_dir": str(PROMPTS.relative_to(REPO)),
        "cases_total": len(CASES), "cases_done": agg["cases"],
        "aggregate": agg, "aggregate_eligibility_fixed": fixed, "ineligible_cases": inelig,
        "per_case": per_case, "elapsed_min": round((time.time() - t0) / 60, 1),
        "finished_at": time.strftime("%F %T"),
    }
    (out_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[baseline:ds] summary -> {out_root / 'summary.json'}（用时 {summary['elapsed_min']} 分钟）", flush=True)


if __name__ == "__main__":
    main()
