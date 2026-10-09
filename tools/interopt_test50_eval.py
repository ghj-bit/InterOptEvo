#!/usr/bin/env python3
"""InterOPT（open_interopt 两阶段）× FP8 评测驱动（2026-10-09 新建，不改上游文件）。

臂：agent / user_simulator / detector / gap-search = qwen3.8-27b-fp8（经 18770，think 关）；
    judge = deepseek-flash（经代理 judge 路由，think 关）。
框架 = experiments/open_interopt（Full InterOPT：Stage 1 gap memory + Stage 2 ask-or-stop），
prompts = 该框架原生 prompts（6 文件，含 gap_search_prompt.md；不是 r27 / 随便问）。
题集：orclarify_051–100（== splits["test"]）；单遍 k=1、max_turns=30、并发 --concurrency（默认 20）。
计分：复用演化线 score_many + eligibility 修正（与 test50 五臂同口径）。

用法: python tools/interopt_test50_eval.py [--concurrency 20] [--cases 51-100] [--dry-run]
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
WRAPPER = REPO / "tools" / "run_interopt_fp8.py"
ROOT = REPO / "runs" / "test50_interopt_fp8"
CASES = [f"orclarify_{i:03d}" for i in range(51, 101)]
BASE_URL = "http://127.0.0.1:18770/v1"
AGENT_PROFILE = "qwen3_8_27b_fp8"
JUDGE_PROFILE = "deepseek_flash"
WRAPPER_OVERRIDE = None  # --wrapper 可换 run_interopt_*.py（dsflash 臂用 run_interopt_dsflash.py）


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


def launch(cid: str, out_dir: Path, log_path: Path, max_turns: int,
           base_url: str, agent_profile: str, judge_profile: str, wrapper: Path) -> subprocess.Popen:
    env = os.environ.copy()
    env.update({
        "DEEPSEEK_BASE_URL": base_url,
        "DEEPSEEK_API_KEY": "x",   # 真实 key 由本地代理按角色注入
    })
    cmd = [sys.executable, "-u", str(wrapper),
           "--toml_dir", str(case_dir(cid)), "--limit", "1", "--k", "1",
           "--max_turns", str(max_turns),
           "--agent_profiles", agent_profile,
           "--detector_profile", agent_profile,
           "--user_profile", agent_profile,
           "--judge_profile", judge_profile,
           "--output_dir", str(out_dir)]
    log = open(log_path, "a", encoding="utf-8")
    return subprocess.Popen(cmd, cwd=str(REPO), env=env, stdout=log, stderr=subprocess.STDOUT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=20)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--cases", default="51-100", help="题号范围/列表，如 51-100 或 51,55,60")
    ap.add_argument("--out-root", default=None, help="覆盖输出根目录（默认 runs/test50_interopt_fp8）")
    ap.add_argument("--base-url", default=BASE_URL, help="覆盖代理 base（默认 18770/FP8 臂）")
    ap.add_argument("--agent-profile", default=AGENT_PROFILE, help="agent/detector/user profile 名")
    ap.add_argument("--judge-profile", default=JUDGE_PROFILE, help="judge profile 名")
    ap.add_argument("--wrapper", default=None, help="覆盖包装器（默认 tools/run_interopt_fp8.py）")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    global CASES
    CASES = parse_cases(args.cases)
    out_root: Path = Path(args.out_root).resolve() if args.out_root else ROOT
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "logs").mkdir(exist_ok=True)
    wrapper: Path = Path(args.wrapper).resolve() if args.wrapper else WRAPPER
    t0 = time.time()

    # 预检：代理 base 可达
    try:
        with urllib.request.urlopen(args.base_url + "/models", timeout=5) as r:
            ok = r.status == 200
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[interopt] 预检失败：{args.base_url} 不可达（{exc}）", flush=True)
    print(f"[interopt] framework=open_interopt(native prompts) wrapper={wrapper.name} "
          f"agent={args.agent_profile} judge={args.judge_profile} base={args.base_url} 预检={'OK' if ok else 'FAIL'}", flush=True)

    pending, done = [], {}
    for cid in CASES:
        od = out_root / f"out_{cid}"
        if list(od.glob("**/judge_result.json")):
            done[cid] = od
        else:
            pending.append((cid, od))
    print(f"[interopt] 共 {len(CASES)} 题：已完成 {len(done)}，待跑 {len(pending)}（并发 {args.concurrency}）", flush=True)
    if args.dry_run:
        return

    for attempt in range(1, args.attempts + 1):
        queue = list(pending)
        running: list[tuple] = []
        while queue or running:
            while queue and len(running) < args.concurrency:
                cid, od = queue.pop(0)
                log_path = out_root / "logs" / f"interopt-{cid}.log"
                running.append((cid, od, launch(cid, od, log_path, args.max_turns,
                                                args.base_url, args.agent_profile,
                                                args.judge_profile, wrapper)))
            time.sleep(3)
            still = []
            for cid, od, proc in running:
                if proc.poll() is None:
                    still.append((cid, od, proc))
                elif list(od.glob("**/judge_result.json")):
                    done[cid] = od
                    print(f"[interopt] {cid} 完成（{len(done)}/{len(CASES)}）", flush=True)
                else:
                    print(f"[interopt] {cid} 未完成（attempt {attempt}）", flush=True)
            running = still
        pending = [(c, o) for c, o in pending if c not in done]
        if not pending:
            break
        print(f"[interopt] 第 {attempt} 轮结束仍缺 {len(pending)} 条，重试", flush=True)

    # ---- 计分（复用演化线 score_many）----
    sys.path.insert(0, str(THIS.parent))
    import orclarify_evolution as OE  # noqa: E402
    run_dirs = {(cid, 1): od for cid, od in done.items()}
    agg, case_runs = OE.score_many(run_dirs, CASES, 1)
    print(f"\n[interopt] 完成 {agg['cases']}/{len(CASES)} 题；缺失: {[c for c in CASES if c not in case_runs]}", flush=True)
    print(f"{'case':<16}{'core':>7}{'allslot':>8}{'silent':>7}{'net':>8}{'turns':>7}{'stop':>16}", flush=True)
    per_case = {}
    inelig = []
    for cid in CASES:
        if cid not in case_runs:
            continue
        r = case_runs[cid][0]
        per_case[cid] = {k: r[k] for k in ("core", "allslot", "silent", "net")}
        per_case[cid]["stopping"] = r.get("stopping")
        per_case[cid]["ready"] = r.get("ready")
        per_case[cid]["turns"] = r.get("turns")
        jr = json.loads(next((done[cid]).glob("**/judge_result.json")).read_text())
        rs = jr.get("restoration_summary") or {}
        if (rs.get("core_slot_count", 0) or 0) == 0:
            inelig.append(cid)
        print(f"{cid:<16}{r['core']:>7}{r['allslot']:>8}{r['silent']:>7}{r['net']:>8}"
              f"{str(r.get('turns')):>7}{str(r.get('stopping')):>16}", flush=True)
    print(f"aggregate: core={agg['core']} allslot={agg['allslot']} silent={agg['silent']} net={agg['net']}", flush=True)

    # eligibility 修正（无 P0/P1 槽的题从 C 项剔除；A/S 口径不变）
    fixed = None
    if inelig:
        elig = [c for c in per_case if c not in inelig]
        C = sum(per_case[c]["core"] for c in elig) / len(elig)
        A = sum(per_case[c]["allslot"] for c in per_case) / len(per_case)
        S = sum(per_case[c]["silent"] for c in per_case) / len(per_case)
        fixed = {"core": round(C, 4), "allslot": round(A, 4), "silent": round(S, 3),
                 "net": round(0.5 * C + 0.5 * A - 0.1 * S, 4)}
        print(f"eligibility 修正（剔除 {inelig}）: core={fixed['core']} net={fixed['net']}", flush=True)

    turns = [per_case[c]["turns"] for c in per_case if per_case[c]["turns"]]
    summary = {
        "arm": f"interopt_{args.agent_profile}", "framework": "open_interopt (native prompts)",
        "agent_profile": args.agent_profile, "judge_profile": args.judge_profile,
        "wrapper": str(wrapper), "base_url": args.base_url,
        "cases_total": len(CASES), "cases_done": agg["cases"],
        "aggregate": agg, "aggregate_eligibility_fixed": fixed, "ineligible_cases": inelig,
        "per_case": per_case,
        "avg_turns": round(sum(turns) / len(turns), 2) if turns else None,
        "elapsed_min": round((time.time() - t0) / 60, 1),
        "finished_at": time.strftime("%F %T"),
    }
    (out_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[interopt] summary -> {out_root / 'summary.json'}（用时 {summary['elapsed_min']} 分钟）", flush=True)


if __name__ == "__main__":
    main()
