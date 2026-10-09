#!/usr/bin/env python3
"""InterOPT（open_interopt）FP8 跑法包装（2026-10-09 新建，不改上游任何文件）。

上游 experiments/open_interopt/run_pipeline.py 的模型走硬编码 MODEL_PROFILES；
本包装在导入后仅追加两个 profile，其余参数与行为全部透传给上游 main()：
  qwen3_8_27b_fp8 -> model_version "qwen3.8-27b-fp8"
      （provider=deepseek，base 取 env DEEPSEEK_BASE_URL；指向本地代理时落到 FP8 端点，think 由代理关）
  deepseek_flash  -> model_version "deepseek-flash"
      （同样经代理；judge 角色由代理按 "Judge Prompt" 标记路由到远端，thinking disabled）

用法（与上游一致，只是 profile 名换成本包装的两个）：
  DEEPSEEK_BASE_URL=http://127.0.0.1:18770/v1 DEEPSEEK_API_KEY=x \
  python tools/run_interopt_fp8.py --toml_dir <dir> --limit 1 --k 1 --max_turns 30 \
      --agent_profiles qwen3_8_27b_fp8 --detector_profile qwen3_8_27b_fp8 \
      --user_profile qwen3_8_27b_fp8 --judge_profile deepseek_flash \
      --output_dir <out>
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "experiments" / "open_interopt"))

import run_pipeline as RP  # noqa: E402

RP.MODEL_PROFILES["qwen3_8_27b_fp8"] = {"provider": "deepseek", "model_version": "qwen3.8-27b-fp8"}
RP.MODEL_PROFILES["deepseek_flash"] = {"provider": "deepseek", "model_version": "deepseek-flash"}

if __name__ == "__main__":
    RP.main()
