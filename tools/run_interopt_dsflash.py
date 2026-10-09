#!/usr/bin/env python3
"""InterOPT（open_interopt）× deepseek-flash 跑法包装（2026-10-09 新建，不改上游任何文件）。

与 tools/run_interopt_fp8.py 同构，只有 profile 不同：
  deepseek_v4_flash -> model_version "deepseek-flash"
      （DS 官方目录只有 deepseek-flash / deepseek-v4-pro 两个 id；"v4-flash" 即 flash 档。
       provider=deepseek，base 取 env DEEPSEEK_BASE_URL；指向本地路由代理时：
       judge 标记 -> DS（thinking disabled, 16384）；model==deepseek-flash -> DS（thinking disabled, 2048））

用法（与上游一致）：
  DEEPSEEK_BASE_URL=http://127.0.0.1:18775/v1 DEEPSEEK_API_KEY=x \
  python tools/run_interopt_dsflash.py --toml_dir <dir> --limit 1 --k 1 --max_turns 30 \
      --agent_profiles deepseek_v4_flash --detector_profile deepseek_v4_flash \
      --user_profile deepseek_v4_flash --judge_profile deepseek_v4_flash \
      --output_dir <out>
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "experiments" / "open_interopt"))

import run_pipeline as RP  # noqa: E402

RP.MODEL_PROFILES["deepseek_v4_flash"] = {"provider": "deepseek", "model_version": "deepseek-flash"}

if __name__ == "__main__":
    RP.main()
