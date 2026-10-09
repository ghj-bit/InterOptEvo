#!/usr/bin/env python3
"""Open / FreeQA baseline × deepseek-v4-pro（全角色同模型，2026-10-09 新建）。

口径（对齐上游 .env.example 的 reported local runs）：
  - 执行 agent / user simulator / detector / judge 以及 selector、ready-gate
    **全部 = deepseek-v4-pro**（GENERIC_AGENT_MODEL 等六个角色变量同值）；
  - 直连 DEEPSEEK_BASE_URL（默认 https://api.deepseek.com），**不经任何本地代理**；
  - prompts_dir = 仓库原生 baseline（experiments/evaluation_protocol/prompts，无 Interaction Strategy 段）；
  - 题集 = orclarify_001–100（全部 100 题），单遍 k=1，max_turns 默认 20（论文口径），并发默认 20。
计分：复用演化线 score_many（同一条判分口径）+ eligibility 修正。

用法:
  python tools/freeqa_baseline_eval.py --cases 1            # 冒烟单题（case 001）
  python tools/freeqa_baseline_eval.py                      # 全量 1-100（已完成题自动跳过）
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
ROOT = Path(os.getenv("FREEQA_OUT_ROOT") or (REPO / "runs" / "freeqa_baseline_v4pro"))
CASES = [f"orclarify_{i:03d}" for i in range(1, 101)]
MODEL = "deepseek-v4-pro"
BASE_URL = os.getenv("FREEQA_BASE_URL", "https://api.deepseek.com")


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
        "DEEPSEEK_BASE_URL": BASE_URL,
        # 六个角色变量同值 = 全链路同模型（对齐 .env.example 的 reported 口径）
        "GENERIC_AGENT_MODEL": MODEL,
        "USER_SIMULATOR_MODEL": MODEL,
        "DETECTOR_MODEL": MODEL,
        "JUDGE_MODEL": MODEL,
        "FORMULATION_QUESTION_SELECTOR_MODEL": MODEL,
        "READY_GATE_MODEL": MODEL,
        # DEEPSEEK_API_KEY 不在此注入：由仓库根 .env 提供（load_env_file, setdefault 语义）
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
    ap.add_argument("--max-turns", type=int, default=20)
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--cases", default="1-100", help="题号范围/列表，如 1-100 或 1,55")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    global CASES
    CASES = parse_cases(args.cases)
    out_root: Path = ROOT
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "logs").mkdir(exist_ok=True)
    t0 = time.time()

    try:
        with urllib.request.urlopen(BASE_URL.rstrip("/") + "/models", timeout=8) as r:
            ok = r.status == 200
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[freeqa:v4pro] /models 预检未过（{exc}）——继续（部分端点不提供该路由）", flush=True)
    print(f"[freeqa:v4pro] prompts=upstream-baseline 全角色={MODEL} base={BASE_URL} "
          f"max_turns={args.max_turns} 预检={'OK' if ok else 'skipped'}", flush=True)

    pending, done = [], {}
    for cid in CASES:
        od = out_root / f"out_{cid}"
        if list(od.glob("**/judge_result.json")):
            done[cid] = od
        else:
            pending.append((cid, od))
    print(f"[freeqa:v4pro] 共 {len(CASES)} 题：已完成 {len(done)}，待跑 {len(pending)}（并发 {args.concurrency}）", flush=True)
    if args.dry_run:
        return

    for attempt in range(1, args.attempts + 1):
        queue = list(pending)
        running: list[tuple] = []
        while queue or running:
            while queue and len(running) < args.concurrency:
                cid, od = queue.pop(0)
                log_path = out_root / "logs" / f"v4pro-{cid}.log"
                running.append((cid, od, launch(cid, od, log_path, args.max_turns)))
            time.sleep(3)
            still = []
            for cid, od, proc in running:
                if proc.poll() is None:
                    still.append((cid, od, proc))
                elif list(od.glob("**/judge_result.json")):
                    done[cid] = od
                    print(f"[freeqa:v4pro] {cid} 完成（{len(done)}/{len(CASES)}）", flush=True)
                else:
                    print(f"[freeqa:v4pro] {cid} 未完成（attempt {attempt}）", flush=True)
            running = still
        pending = [(c, o) for c, o in pending if c not in done]
        if not pending:
            break
        print(f"[freeqa:v4pro] 第 {attempt} 轮结束仍缺 {len(pending)} 条，重试", flush=True)

    # ---- 计分（复用演化线 score_many）----
    sys.path.insert(0, str(THIS.parent))
    import orclarify_evolution as OE  # noqa: E402
    run_dirs = {(cid, 1): od for cid, od in done.items()}
    agg, case_runs = OE.score_many(run_dirs, CASES, 1)
    print(f"\n[freeqa:v4pro] 完成 {agg['cases']}/{len(CASES)} 题；缺失: {[c for c in CASES if c not in case_runs]}", flush=True)
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
        "arm": "freeqa_baseline_v4pro",
        "agent_model": MODEL, "user_model": MODEL, "detector_model": MODEL, "judge_model": MODEL,
        "policy": "upstream-baseline(no strategy)",
        "prompts_dir": str(PROMPTS.relative_to(REPO)),
        "base_url": BASE_URL, "max_turns": args.max_turns,
        "cases_total": len(CASES), "cases_done": agg["cases"],
        "aggregate": agg, "aggregate_eligibility_fixed": fixed, "ineligible_cases": inelig,
        "per_case": per_case, "elapsed_min": round((time.time() - t0) / 60, 1),
        "finished_at": time.strftime("%F %T"),
    }
    (out_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[freeqa:v4pro] summary -> {out_root / 'summary.json'}（用时 {summary['elapsed_min']} 分钟）", flush=True)


if __name__ == "__main__":
    main()
