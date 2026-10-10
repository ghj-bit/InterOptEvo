# evo_r30_from_ask_anything · 运行说明（2026-10-09）

- 目的：**全新实验**——从 **r0 新初始策略（随便问）** 出发跑 30 轮演化；配置与 evo_r10 一致，
  **唯一差异 = judge（deepseek-flash）开启 thinking**。旧的 evo_askanything 保持 SIGSTOP 冻结、未动。
- 种子/模板：`runs/prompts_askanything/generic_agent_prompt.md`（Behavior 正文 = "Given the problem statement, you may ask any question you want to ask."）
- schema：`--policy-schema behavior`（可演化 = `## Behavior` 正文；协议 bullet 块冻结、由程序拼装）
- 评测链路：agent/simulator/detector = qwen3.8-27b-fp8（本地 FP8，think 关）；
  **judge = deepseek-flash（thinking=ENABLED，经 18776 judge-think 代理）**；
  k=1、max_turns=30、passes=3、train 批 8/轮、并发 24/pass、evolver=deepseek-flash temp 0.667
- 门机制：**保留完整门流程（所有轮次含 train 门）**——父本 train batch → 证据 → 候选同 batch（ctrain）
  → **train 门（候选 net > 父本 + ε 才继续）** → val 门。候选不会直接跑 val。
- 口径注记：judge 由 think-off 改 think-on，**本线分数与 evo_r10（think-off 判分）不可直接横比**；线内各轮可比。
- 文件指纹（sha256-16）：代理 `tools/cap_proxy_judge_think.py` = 0c28200d8ffa18fb；
  演化器 `tools/orclarify_evolution.py` = 1d5a042686b144eb；
  种子 = 9f58f0fe77b1a6c4
- 启动：`python3 -u tools/orclarify_evolution.py --name evo_r30_from_ask_anything --rounds 30
  --template <REPO>/runs/prompts_askanything/generic_agent_prompt.md --policy-schema behavior
  --proxy-base-url http://127.0.0.1:18776/v1 --concurrency 24`（重发同命令即断点续跑）
- 前提服务：18776 judge-think 代理（`python3 tools/cap_proxy_judge_think.py 18776 2048`）

## 补跑记录（2026-10-09 晚）

- 规则：单调用 5 次空返回重试 + case 级 3 attempts 仍缺 → **只补该 case×pass，绝不重跑其他成功 run**；
  补跑经 18777（judge-think + FP8 空返回守卫，`tools/cap_proxy_guard_jt.py`，sha 见下）断点续跑。
- 本次补跑 2 条（工具 `tools/evo_rescue_missing.py`）：
  - round_0/val_p2/orclarify_048（resume 自第 20 轮）→ +1.0，守卫实弹救 2 回合；
  - round_1/val_p2/orclarify_040（resume 自第 7 轮）→ +1.0，守卫救 1 回合。
- 复算附注（**不改写 state 门槛历史**）：round_0 val net 0.5700 → **0.5783**（补齐 048 后）；
  round_1 val 0.6183 不变（040 另两遍本就满格）。
