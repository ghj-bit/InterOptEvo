#!/bin/bash
# test50（orclarify_051–100）× gpt-6.1-sol(agent) —— 完全并发，一题一进程
#   agent     = gpt-6.1-sol（rightapi.ai，经 cap_proxy 18771 的 extra route）
#   simulator = 本地 FP8（gpu6:18764，经同一代理）
#   detector  = 本地 FP8
#   judge     = deepseek-flash（远端，经同一代理）
#   prompts_dir = experiments/evaluation_protocol/prompts（仓库原生 upstream baseline，无 Interaction Strategy 段）
# 每 case 最多 3 次尝试（pipeline 自带 resume 续跑）
set -u
cd /public1/home/stu52275901007/workspace/ghj_workspace/InterOpt
export DEEPSEEK_BASE_URL=http://127.0.0.1:18771/v1 DEEPSEEK_API_KEY=x
export GENERIC_AGENT_MODEL=gpt-6.1-sol
export USER_SIMULATOR_MODEL=qwen3.8-27b-fp8
export DETECTOR_MODEL=qwen3.8-27b-fp8
export JUDGE_MODEL=deepseek-flash
# gpt-6.1-sol 单次 45–100s+，且 rightapi 实测有过 ~19 分钟的整段 stall（19:18–19:37）；
# 默认 180s 超时会把慢调用/短暂停摆判死，这里放宽到 600s（不影响 judge 的 240s 显式超时）
export LLM_TIMEOUT=600
CASES=$(seq -w 51 100)
for c in $CASES; do
  d="runs/test50_gpt61/cases/$c"
  mkdir -p "$d"
  ln -sfn "../../../../data/orclarify_$c.toml" "$d/orclarify_$c.toml"
done
run_case() {
  local c=$1
  for attempt in 1 2 3; do
    python -u experiments/evaluation_protocol/run_pipeline.py \
      --toml_dirs "runs/test50_gpt61/cases/$c" --limit 1 --k 1 --max_turns 30 \
      --prompts_dir experiments/evaluation_protocol/prompts \
      --output_dir "runs/test50_gpt61/out_orclarify_$c" >> "runs/test50_gpt61/logs/t50-$c.log" 2>&1
    if find "runs/test50_gpt61/out_orclarify_$c" -name judge_result.json | grep -q .; then return 0; fi
    echo "[$c] attempt $attempt 未完成，重试" >> "runs/test50_gpt61/logs/t50-$c.log"
  done
}
pids=""
for c in $CASES; do run_case "$c" & pids="$pids $!"; done
echo "已启动 $(echo $pids | wc -w) 个进程 $(date '+%F %H:%M:%S')"
for p in $pids; do wait "$p"; done
echo "ALL DONE $(date '+%F %H:%M:%S')"
