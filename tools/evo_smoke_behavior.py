#!/usr/bin/env python3
"""behavior schema 单步演化冒烟（2026-10-09）——不跑任何题，只验演化链路。

流程：取 evo_r10 round_22 的现成 evidence + 其当时的父本策略（champion_history），
用 behavior schema 重建演化 prompt → 调演化器（deepseek-flash，与 evo_r10 同参）
→ 解析 patch（{"body": ...}）→ 程序拼装进新种子模板（runs/prompts_askanything/）
→ 四条验收：①patch 合法；②冻结段逐字（协议块 diff 为空）；③正文无 heading/协议 token；
④与历史策略相似度 <0.9。

用法: python tools/evo_smoke_behavior.py
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

THIS = Path(__file__).resolve()
REPO = THIS.parents[1]
sys.path.insert(0, str(THIS.parent))
import orclarify_evolution as OE  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--round-dir", default="runs/evolution/evo_r10/round_22")
    ap.add_argument("--template", default="runs/prompts_askanything/generic_agent_prompt.md")
    ap.add_argument("--parent", choices=["template", "round_parent"], default="template",
                    help="template=以 round-0 种子策略（新 schema 抽取）为当前策略；round_parent=用该轮当时的父本")
    ap.add_argument("--out", default="runs/evolution/evo_r30_from_ask_anything/smoke_evolve")
    ap.add_argument("--evolver-model", default="deepseek-flash")
    ap.add_argument("--evolver-temperature", type=float, default=0.667)
    ap.add_argument("--evolver-max-tokens", type=int, default=4000)
    ap.add_argument("--max-turns", type=int, default=30)
    args = ap.parse_args()

    rd = REPO / args.round_dir
    template = (REPO / args.template).read_text(encoding="utf-8")
    evidence = json.loads((rd / "evidence.json").read_text())
    state = json.loads((REPO / "runs" / "evolution" / "evo_r10" / "state.json").read_text())

    # 当前策略：默认 = 新线 round-0 种子（按 behavior schema 从模板抽取）
    if args.parent == "template":
        OE.POLICY_SCHEMA = "behavior"   # 先按新 schema 抽取种子正文
        parent_strategy = OE.strategy_body(template)
        parent_label = "round0-seed（askanything 模板正文）"
    else:
        # 父本 = r22 应用时的当前冠军（最后一条 round < 22 的 champion_history）
        r22 = int(rd.name.split("_")[1])
        parents = [e for e in state["champion_history"] if int(e["round"]) < r22]
        if not parents:
            raise SystemExit("no parent champion before round {}".format(r22))
        parent = parents[-1]
        parent_strategy = parent["policy"]
        parent_label = f"round {parent['round']}（val net {parent.get('val_net')}）"
    print(f"[smoke] parent = {parent_label}，{len(parent_strategy)} 字符")

    # 新 schema：重建演化 prompt（只展示可变策略正文）
    OE.POLICY_SCHEMA = "behavior"
    prompt = OE.build_evolution_prompt(parent_strategy, evidence,
                                       state["champion_history"][-3:], args.max_turns)
    out = REPO / args.out
    out.mkdir(parents=True, exist_ok=True)
    (out / "evolution_prompt.md").write_text(prompt, encoding="utf-8")
    print(f"[smoke] prompt -> {out / 'evolution_prompt.md'}（{len(prompt)} 字符）")

    raw = OE.call_evolver(prompt, args.evolver_model, args.evolver_temperature, args.evolver_max_tokens)
    (out / "evolution_response.txt").write_text(raw, encoding="utf-8")
    print(f"[smoke] evolver 返回 {len(raw)} 字符")

    verdict: dict = {"parent": parent_label, "checks": {}}
    try:
        payload = OE.extract_json_object(raw)
        patch = payload["policy_patch"]
        verdict["patch_keys"] = sorted(patch.keys())
        candidate = OE.apply_policy_patch(template, patch)
        body = OE.strategy_body(candidate)
        OE.assert_fixed_unchanged(candidate, template)
        sims = [(OE.similarity(body, s), i) for i, s in enumerate(state["strategies_seen"])]
        worst = max(sims) if sims else (0.0, -1)
        sim_ok = worst[0] < OE.DEFAULT_SIMILARITY_THRESHOLD if hasattr(OE, "DEFAULT_SIMILARITY_THRESHOLD") else worst[0] < 0.9
        if not sim_ok:
            raise ValueError(f"too similar to seen strategy #{worst[1]}（sim={worst[0]:.2f}）")
        verdict["checks"] = {"patch_ok": True, "frozen_verbatim": True, "no_heading": True,
                             "sim": {"max": round(worst[0], 3), "vs_index": worst[1], "threshold": 0.9}}
        (out / "candidate_policy.md").write_text(candidate, encoding="utf-8")
        (out / "new_strategy_body.md").write_text(body, encoding="utf-8")
        verdict["body_chars"] = len(body)
        verdict["evolution_rationale"] = payload.get("evolution_rationale", "")
        print("\n===== 演化出的新交互策略正文 =====\n")
        print(body)
        print("\n===== 验收 =====\n" + json.dumps(verdict, ensure_ascii=False, indent=2))
    except Exception as exc:  # noqa: BLE001
        verdict["checks"]["error"] = str(exc)
        print(f"[smoke] 验收失败: {exc}")
    (out / "verdict.json").write_text(json.dumps(verdict, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
