# test50 两臂评测 · 实验通用配置（导出留档）

- 导出时间：2026-10-08 22:25（主机 login1；python = /public1/home/stu52275901007/anaconda3/bin/python）
- 仓库：`/public1/home/stu52275901007/workspace/ghj_workspace/InterOptEvo` @ git `dc97d1f8`
  （`tools/cap_proxy_dsagent.py`、`tools/test50_eval.py` 为未跟踪的新增文件）
- 目的：把 evo_r10 演化冠军（r22 策略）作为交互策略，在**从未触碰的 test 集**（orclarify_051–100）上评测；
  两臂对照**唯一变量 = 执行 agent 模型**。

## 一、实验设计

| 项 | 臂 1 `champion_qwen` | 臂 2 `champion_dsflash` |
|---|---|---|
| 执行 agent | qwen3.8-27b-fp8（本地 FP8） | deepseek-flash（远端 API） |
| 策略 | evo_r10 冠军 r22：`policies/r27_champion`（与 champion.md 逐字一致） | 同左（一字不改） |
| 题集 | orclarify_051–100（50 题；与 train 001–030 / val 031–050 零重叠） | 同左 |
| pass / 并发 | 1 / 20 | 1 / 20 |
| user simulator / detector | qwen3.8-27b-fp8（本地 FP8） | 同左 |
| judge | deepseek-flash（远端） | 同左 |

## 二、协议与生成参数（与 evo_r10 逐字段一致，已对拍）

- 协议：Open/FreeQA 自由问答（`evaluation_protocol/run_pipeline.py`）
- `pipeline_mode=passive_question_audit`；`detector_feedback_mode=none`；`retry_limit_behavior=pass_through`；
  `max_agent_retries=0`；`monitor_user_answers=false`
- 温度：agent 0.2；user / detector / judge 0.0
- `max_turns=30`；`k=1`；`limit=1`
- 判分：复用演化线 scorer（`orclarify_evolution.score_many`，同一个 judge）；
  `net = 0.5·Core + 0.5·AllSlot − 0.1·Silent`；另附 eligibility 修正口径（无 P0/P1 槽的题从 C 项剔除）

## 三、模型路由（本实验的关键接线）

- 臂 1 子进程：`DEEPSEEK_BASE_URL=http://127.0.0.1:18770/v1`
  （cap_proxy：judge→api.deepseek.com〔关 thinking，cap 16384〕；其余→本地 FP8 `gpu6:18764`〔关 thinking，cap 2048〕）
- 臂 2 子进程：`DEEPSEEK_BASE_URL=http://127.0.0.1:18772/v1`
  （`tools/cap_proxy_dsagent.py`：judge→ds〔16384〕；**agent（model=deepseek-flash）→ds〔关 thinking，2048〕**；其余→FP8〔2048〕）
- 两臂四个角色 env 全部显式钉死：`GENERIC_AGENT_MODEL`（唯一差异）、`USER_SIMULATOR_MODEL=qwen3.8-27b-fp8`、
  `DETECTOR_MODEL=qwen3.8-27b-fp8`、`JUDGE_MODEL=deepseek-flash`；`DEEPSEEK_API_KEY=x`（真实 key 由代理注入）
- 说明：仓库根 `.env` 当前为"deepseek-flash 实验"档；pipeline 以 **setdefault** 方式加载 .env——
  本实验所有关键变量均由驱动显式注入覆盖，`.env` 实际不生效（已对拍验证）；pipeline 不使用 .env 的 selector/ready-gate 项

## 四、对拍验证（2026-10-08，对拍用例 orclarify_051）

- `run_config.json` 18 字段 vs evo_r10 round_27 实际记录：除 `toml_dirs`/`output_dir`（路径类，预期）外**全部一致**；
- `statistics.json` 15 个关键字段：臂 1 与基线全同；臂 2 **仅 `agent_model=deepseek-flash`** 不同（预期）；
- 两臂 051 实跑得分：`core=1.0 / allslot=1.0 / silent=0 / net=1.0`；
- ds 代理实弹路由行已确认：`AGENT->ds`、`JUDGE->ds`。

## 五、运行命令与输出

```
臂 1: python -u tools/test50_eval.py --arm qwen --concurrency 20
臂 2: python -u tools/test50_eval.py --arm ds   --concurrency 20
（对拍单题模式: --cases 51 --out-root runs/test50_eval/parity_{qwen,dsflash}）
```

输出布局：`runs/test50_eval/{champion_qwen,champion_dsflash}/out_orclarify_0XX/` + `logs/` + `summary.json`（含逐题与 aggregate、eligibility 修正）

## 六、文件指纹（sha256 前 16 位）

| 文件 | sha256-16 |
|---|---|
| `runs/evolution/evo_r10/champion.md`（r22 冠军策略） | d7faa8ee52067be4 |
| `runs/evolution/evo_r10/policies/r27_champion/generic_agent_prompt.md` | 2de1f7a5c1ac431a |
| `tools/orclarify_evolution.py`（演化驱动，含软链接自愈） | 49f679db9cc51943 |
| `tools/test50_eval.py`（两臂评测驱动） | 72e2dd809d691df6 |
| `tools/cap_proxy_dsagent.py`（ds-agent 路由代理） | f2541ad0a0f4b213 |

## 七、二期补跑附录（2026-10-09，补 ds 臂 orclarify_065/075）

- 背景：一期 B 臂两题未完成，根因为本地 FP8 在 thinking-off 下对特定「(对话前缀, 本轮问句)」组合确定性吐 EOS（空串，`completion_tokens=1`）。prompt_tokens 精确对齐重放可稳定复现（065→1497、075→1821）。
- 补跑代理：`tools/cap_proxy_dsagent_fill.py`（sha256-16 `f56568f6a13862de`）——母本 `cap_proxy_dsagent.py` 未改动（指纹见上表）；唯一增量为空返回守卫：**仅当 FP8 路由响应 content 为空串**时，原样重发同一请求并加 `min_tokens=16` 重解码一次。正常请求零影响；其余 48 题产物与判分未动（rescore 复用存量 judge_result.json）。
- 执行：`python -u tools/test50_eval.py --arm ds --concurrency 4`（同臂断点续跑，自动只补缺题）；2026-10-09 13:58 起，0.5 分钟完成。守卫共救援 4 个回合（prompt≈1496/1821/1896/2085）。
- 救援语义交叉验证：同一触发对在 thinking 开 / 温和 nudge / min_tokens=16 三种扰动下给出一致内容（"The point still needs internal confirmation. …"）。
- 日志与留档：`proxy_dsagent_fill.log`、`arm_dsflash_fill.log`、`RESULTS_20261008_一期两臂48题.md`（一期报告原件）。

## 八、D 臂附录：deepseek-flash baseline（2026-10-09 新增）

- 目的：补齐"deepseek-flash × 无策略 prompt"对照（与 C 臂 gpt-6.1-sol baseline 同设计，两者只差 agent 模型）。
- 配置：agent=deepseek-flash（经 18772 代理路由至 api.deepseek.com，thinking disabled，cap 2048）；user_simulator/detector=qwen3.8-27b-fp8（本地 FP8）；judge=deepseek-flash；`prompts_dir=experiments/evaluation_protocol/prompts`（原生 baseline，无 Interaction Strategy 段）。题集 orclarify_051–100，单遍 k=1、max_turns=30、并发 20。
- 对拍：case 051 的 run_config 18 字段与 A/B/C 臂逐字段比对，**仅路径类字段（output_dir/toml_dirs/prompts_dir）不同**；协议字段全同。
- 驱动：`tools/test50_baseline_eval.py`（sha256-16 `3b8ea94bae428ce6`；独立新文件，未改动 test50_eval.py）。
- 运行：2026-10-09 14:02–14:09（6.4 分钟），50/50；结果 net 0.4120（elig 修正 0.4280）。跑动期间 FP8 空返回守卫（§七）救援 **10 个回合**。
- 产物：`runs/test50_baseline_dsflash/`（summary.json、逐 case 产物、logs/、arm_baseline.log）。

## 九、E 臂附录：随便问策略（2026-10-09 晚新增）

- 目的：以"最简策略"（OptMATH 参考线种子逐字"Given the problem statement, you may ask any question you want to ask."，`QUESTION:`/`READY_TO_MODEL` 两组协议行保留）对照 r22 重策略，量"被允许随便问"本身值多少分。
- 配置：agent=qwen3.8-27b-fp8（经 18770，同 A 臂路由与四个角色 env）；user_simulator/detector=qwen3.8-27b-fp8；judge=deepseek-flash；`prompts_dir=runs/prompts_askanything`（generic_agent_prompt.md sha256-16 `9f58f0fe77b1a6c4`——上游 baseline 文件格式，`## Behavior` 正文替换，其余 4 文件软链同源）。题集 orclarify_051–100，单遍 k=1、max_turns=30、并发 20（run_config 对拍 case 060 逐字段核验：协议/温度字段全同 A 臂）。
- 驱动：`tools/test50_eval.py --arm qwen --prompts-dir runs/prompts_askanything --out-root runs/test50_eval/askanything_qwen`；该文件 2026-10-09 新增 `--prompts-dir`（默认仍 r27_champion，默认行为不变），加后 sha256-16 `ddb97bb119e8e3ad`（此前 `72e2dd809d691df6`）。
- 运行：2026-10-09 16:32–16:42（8.2 分钟主跑 49/50）；081 卡 FP8 确定性空返回（同 §七 机制），经 18774 守卫代理实例（`cap_proxy_dsagent_fill.py`，sha256-16 同 §七）救援 2 回合补齐；重算后 50/50。
- 结果：net **0.4020**（elig 修正 0.4167）；E vs A Δ−0.27（6:18:26）、E vs D Δ−0.01（9:9:32）→ **随便问≈不配策略**；结论：r22 的 +0.25 来自策略内容而非"被允许提问"。
- 五臂总表、逐题与逐臂配置汇总：`RESULTS.md`（五臂终版，本目录）。
