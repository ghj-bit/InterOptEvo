#!/usr/bin/env python3
"""回填某个被跳过的轮次：从已存的 evolution_response.txt 解析候选策略，补跑 ctrain 门 + val。

用法: python tools/evo_backfill_round.py --run evo_r10 --round 8 [--dry-run]

严格镜像 orclarify_evolution.main() 里 round r 的候选路径（解析 → 打补丁 → 冻结段/去重
校验 → 候选目录 → 同批 ctrain 门 → [过门] val 评测 → 记分 → 更新 state / 冠军）；区别
只在：不重跑父本 train、不调演化器——父本 train 结果复用 state 中该轮已存的记录。适用于
解析失败被 skip、但响应文件里的候选其实可修复的轮次。ctrain 的 batch 按 state config 的
train_batch_size / sampling_seed 与原轮一致地重建。--dry-run 只构建候选并校验，不跑任何评测。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import orclarify_evolution as OE  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True, help="runs/evolution/ 下的实验名，如 evo_r10")
    ap.add_argument("--round", type=int, required=True)
    ap.add_argument("--splits", default="runs/evolution/splits.json")
    ap.add_argument("--passes", type=int, default=3)
    ap.add_argument("--max-turns", type=int, default=30)
    ap.add_argument("--concurrency", type=int, default=10)
    ap.add_argument("--selection-epsilon", type=float, default=0.0,
                    help="train 门/val 门的净分裕量（默认 0.0，对齐 orclarify_evolution.py）")
    ap.add_argument("--dry-run", action="store_true", help="只构建候选并校验，不跑任何评测、不写 state")
    args = ap.parse_args()

    root = (OE.REPO_ROOT / "runs" / "evolution" / args.run).resolve()
    state = json.loads((root / "state.json").read_text(encoding="utf-8"))
    r = args.round
    entry = state["rounds"].get(str(r))
    if entry is None or "train" not in entry:
        raise SystemExit(f"round {r} 没有 train 记录，拒绝回填")
    if "val" in entry:
        raise SystemExit(f"round {r} 已有 val 结果，拒绝重复回填")
    if entry.get("status") != "done" or not entry.get("skipped"):
        raise SystemExit(f"round {r} 不是「被跳过的轮次」，拒绝回填")

    sconf = state.get("config", {})
    splits = json.loads((OE.REPO_ROOT / (sconf.get("splits") or args.splits)).read_text())
    val = splits["val"]
    batch = OE.sample_batch(splits["train"], int(sconf.get("train_batch_size", 8)),
                            int(sconf.get("sampling_seed", 0)), r)
    template = (root / "seed_template.md").read_text(encoding="utf-8")

    raw = (root / f"round_{r}" / "evolution_response.txt").read_text(encoding="utf-8")
    payload = OE.extract_json_object(raw)
    patch = payload["policy_patch"]
    candidate_policy = OE.apply_policy_patch(template, patch)
    candidate_body = OE.strategy_body(candidate_policy)
    OE.assert_fixed_unchanged(candidate_policy, template)
    OE.assert_new_strategy(candidate_body, state["strategies_seen"])

    cand_dir = OE.make_policy_dir(root, f"r{r}_candidate", candidate_policy)
    print(f"[backfill r{r}] 候选解析与校验通过（body {len(candidate_body)} 字符），候选目录 {cand_dir}", flush=True)
    print(f"[backfill r{r}] 重建 train batch ({len(batch)}): {batch}", flush=True)
    if args.dry_run:
        print("[backfill] dry-run 结束（未跑任何评测，未写 state）", flush=True)
        return

    ctruns = OE.run_cases(cand_dir, batch, args.passes, root / f"round_{r}", "ctrain",
                          args.max_turns, args.concurrency)
    cagg, _ = OE.score_many(ctruns, batch, args.passes)
    parent_net = entry["train"]["net"]
    accepted_train = cagg["net"] > parent_net + args.selection_epsilon
    print(f"[round {r}] ctrain: core={cagg['core']} allslot={cagg['allslot']} silent={cagg['silent']} net={cagg['net']} "
          f"vs 父本 {parent_net} → {'过门 ✅' if accepted_train else '未过门 ❌（跳过 val）'}", flush=True)
    if not accepted_train:
        entry.pop("skipped", None)
        entry.update({"ctrain": cagg, "accepted_train": False, "promoted": False,
                      "candidate_body": candidate_body})
        state["strategies_seen"].append(candidate_body)
        OE.write_state(root / "state.json", state)
        print(f"[backfill r{r}] state 已更新（train 门未过，promoted=False）", flush=True)
        return

    vruns = OE.run_cases(cand_dir, val, args.passes, root / f"round_{r}", "val",
                         args.max_turns, args.concurrency)
    vagg, _ = OE.score_many(vruns, val, args.passes)
    promoted = vagg["net"] > state["champion"]["val_net"] + args.selection_epsilon
    print(f"[round {r}] val: core={vagg['core']} allslot={vagg['allslot']} silent={vagg['silent']} net={vagg['net']} "
          f"→ {'晋级 ✅' if promoted else '未超过冠军 ❌'}", flush=True)

    entry.pop("skipped", None)
    entry.update({"ctrain": cagg, "accepted_train": True, "val": vagg, "promoted": promoted,
                  "candidate_body": candidate_body})
    state["strategies_seen"].append(candidate_body)
    if promoted:
        state["champion"] = {"round": r, "val_net": vagg["net"], "strategy": candidate_body}
        state["champion_history"].append({"round": r, "policy": candidate_body, "val_net": vagg["net"],
                                          "val_core": vagg["core"], "val_allslot": vagg["allslot"],
                                          "val_silent": vagg["silent"]})
        (root / "champion.md").write_text(candidate_body, encoding="utf-8")
    OE.write_state(root / "state.json", state)
    print(f"[backfill r{r}] state 已更新（promoted={promoted}）", flush=True)


if __name__ == "__main__":
    main()
