#!/usr/bin/env python3
"""test50 两臂评测驱动（新建文件，不改动演化线任何脚本）。

臂：
  qwen : GENERIC_AGENT_MODEL=qwen3.8-27b-fp8，经 cap_proxy 18770
  ds   : GENERIC_AGENT_MODEL=deepseek-flash，经 cap_proxy_dsagent 18772（agent 请求转远端 DeepSeek）
两臂其余角色完全一致：user_simulator / detector = qwen3.8-27b-fp8（本地 FP8），judge = deepseek-flash（远端）。
策略：默认 = evo_r10 演化冠军（r22 文本，取 policies/r27_champion，已验证 == champion.md）；
     --prompts-dir 可换成任意 prompts 目录（2026-10-09 加，随便问臂 E 用）。
题集：orclarify_051–100（50 题，与 train/val 零重叠）。单 pass，并发 --concurrency（默认 20）。
计分：复用演化线的 score_many（同一条判分口径），另附 eligibility 修正口径（无 P0/P1 槽的题从 C 项剔除）。

用法: python tools/test50_eval.py --arm qwen|ds [--concurrency 20] [--dry-run]
      python tools/test50_eval.py --arm qwen --prompts-dir runs/prompts_askanything \
          --out-root runs/test50_eval/askanything_qwen        # 随便问臂 E
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
POLICY = REPO / "runs" / "evolution" / "evo_r10" / "policies" / "r27_champion"
ROOT = REPO / "runs" / "test50_eval"
CASES = [f"orclarify_{i:03d}" for i in range(51, 101)]


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

ARMS = {
    "qwen": {"agent": "qwen3.8-27b-fp8", "base": "http://127.0.0.1:18770/v1", "out": ROOT / "champion_qwen"},
    "ds":   {"agent": "deepseek-flash",  "base": "http://127.0.0.1:18772/v1", "out": ROOT / "champion_dsflash"},
}


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


def launch(cid: str, out_dir: Path, log_path: Path, max_turns: int, arm: dict,
           prompts_dir: Path) -> subprocess.Popen:
    env = os.environ.copy()
    env.update({
        "DEEPSEEK_BASE_URL": arm["base"],
        "DEEPSEEK_API_KEY": "x",
        "GENERIC_AGENT_MODEL": arm["agent"],
        "USER_SIMULATOR_MODEL": "qwen3.8-27b-fp8",
        "DETECTOR_MODEL": "qwen3.8-27b-fp8",
        "JUDGE_MODEL": "deepseek-flash",
    })
    cmd = [sys.executable, "-u", str(EVAL_PIPELINE),
           "--toml_dirs", str(case_dir(cid)), "--limit", "1", "--k", "1",
           "--max_turns", str(max_turns), "--prompts_dir", str(prompts_dir),
           "--output_dir", str(out_dir)]
    log = open(log_path, "a", encoding="utf-8")
    return subprocess.Popen(cmd, cwd=str(REPO), env=env, stdout=log, stderr=subprocess.STDOUT)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, choices=["qwen", "ds"])
    ap.add_argument("--concurrency", type=int, default=20)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--attempts", type=int, default=3)
    ap.add_argument("--cases", default="51-100", help="题号范围/列表，如 51-100 或 51,55,60")
    ap.add_argument("--out-root", default=None, help="覆盖输出根目录（默认用臂的目录）")
    ap.add_argument("--prompts-dir", default=None,
                    help="覆盖 prompts 目录（默认 = evo_r10 冠军策略 r27_champion）")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    global CASES
    CASES = parse_cases(args.cases)
    arm = ARMS[args.arm]
    prompts_dir: Path = Path(args.prompts_dir).resolve() if args.prompts_dir else POLICY
    if not (prompts_dir / "generic_agent_prompt.md").is_file():
        ap.error(f"--prompts-dir 下缺 generic_agent_prompt.md: {prompts_dir}")
    out_root: Path = Path(args.out_root).resolve() if args.out_root else arm["out"]
    out_root.mkdir(parents=True, exist_ok=True)
    (out_root / "logs").mkdir(exist_ok=True)
    t0 = time.time()

    # 预检：臂的 base_url 可达
    try:
        with urllib.request.urlopen(arm["base"] + "/models", timeout=5) as r:
            ok = r.status == 200
    except Exception as exc:  # noqa: BLE001
        ok = False
        print(f"[test50:{args.arm}] 预检失败：{arm['base']} 不可达（{exc}）", flush=True)
    print(f"[test50:{args.arm}] prompts={prompts_dir} agent={arm['agent']} base={arm['base']} 预检={'OK' if ok else 'FAIL'}", flush=True)

    pending, done = [], {}
    for cid in CASES:
        od = out_root / f"out_{cid}"
        if list(od.glob("**/judge_result.json")):
            done[cid] = od
        else:
            pending.append((cid, od))
    print(f"[test50:{args.arm}] 共 {len(CASES)} 题：已完成 {len(done)}，待跑 {len(pending)}（并发 {args.concurrency}）", flush=True)
    if args.dry_run:
        return

    for attempt in range(1, args.attempts + 1):
        queue = list(pending)
        running: list[tuple] = []
        while queue or running:
            while queue and len(running) < args.concurrency:
                cid, od = queue.pop(0)
                log_path = out_root / "logs" / f"{args.arm}-{cid}.log"
                running.append((cid, od, launch(cid, od, log_path, args.max_turns, arm, prompts_dir)))
            time.sleep(3)
            still = []
            for cid, od, proc in running:
                if proc.poll() is None:
                    still.append((cid, od, proc))
                elif list(od.glob("**/judge_result.json")):
                    done[cid] = od
                    print(f"[test50:{args.arm}] {cid} 完成（{len(done)}/{len(CASES)}）", flush=True)
                else:
                    print(f"[test50:{args.arm}] {cid} 未完成（attempt {attempt}）", flush=True)
            running = still
        pending = [(c, o) for c, o in pending if c not in done]
        if not pending:
            break
        print(f"[test50:{args.arm}] 第 {attempt} 轮结束仍缺 {len(pending)} 条，重试", flush=True)

    # ---- 计分（复用演化线 score_many）----
    sys.path.insert(0, str(THIS.parent))
    import orclarify_evolution as OE  # noqa: E402
    run_dirs = {(cid, 1): od for cid, od in done.items()}
    agg, case_runs = OE.score_many(run_dirs, CASES, 1)
    print(f"\n[test50:{args.arm}] 完成 {agg['cases']}/{len(CASES)} 题；缺失: {[c for c in CASES if c not in case_runs]}", flush=True)
    print(f"{'case':<16}{'core':>7}{'allslot':>8}{'silent':>7}{'net':>8}", flush=True)
    per_case = {}
    inelig = []
    for cid in CASES:
        if cid not in case_runs:
            continue
        r = case_runs[cid][0]
        per_case[cid] = {k: r[k] for k in ("core", "allslot", "silent", "net")}
        jr = json.loads(next((done[cid]).glob("**/judge_result.json")).read_text())
        rs = jr.get("restoration_summary") or {}
        if (rs.get("core_slot_count", 0) or 0) == 0:
            inelig.append(cid)
        print(f"{cid:<16}{r['core']:>7}{r['allslot']:>8}{r['silent']:>7}{r['net']:>8}", flush=True)
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

    try:
        policy_rel = str(prompts_dir.relative_to(REPO))
    except ValueError:
        policy_rel = str(prompts_dir)
    summary = {
        "arm": args.arm, "agent_model": arm["agent"], "policy": policy_rel,
        "cases_total": len(CASES), "cases_done": agg["cases"],
        "aggregate": agg, "aggregate_eligibility_fixed": fixed, "ineligible_cases": inelig,
        "per_case": per_case, "elapsed_min": round((time.time() - t0) / 60, 1),
        "finished_at": time.strftime("%F %T"),
    }
    (out_root / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[test50:{args.arm}] summary -> {out_root / 'summary.json'}（用时 {summary['elapsed_min']} 分钟）", flush=True)


if __name__ == "__main__":
    main()
