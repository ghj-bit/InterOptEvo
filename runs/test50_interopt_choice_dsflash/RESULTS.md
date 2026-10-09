# test50 · Full InterOPT **Choice (MC-D)** × deepseek-flash 单臂报告（2026-10-09，H 臂）

- 目的：把 G 臂（InterOPT × deepseek-flash × **Open**）换成 **Choice 设置**，其余严格对齐——唯一变量 = 设置（open/FreeQA ↔ choice/MC-D）。
- 框架：`experiments/interopt/run_pipeline.py`（Choice 设置 InterOPT：Stage1 ledger gap + Stage2 C1-C3/Q1-Q3 候选 + selector；上游零改动，sha256-16 `00dc4080e3080983`）；README 必传的 ledger 三件套（`prompt-ledger-gap-search` / `agent_ledger_supplement` / `selector_ledger_supplement`）全部显式传入；`--interaction_modes mc_d`。
- 角色与路由：**全角色 = deepseek-flash**（agent / user_simulator / detector / formulation_question_selector / judge；gap-search 复用 agent client），经 18775 独立代理（`tools/cap_proxy_dsagent.py` `f2541ad0a0f4b213`：judge→DS 16384、model==deepseek-flash→DS 关 thinking 2048）；think 全关（run_health.json 逐角色核验 + 代理日志无 FP8 路由）。
- 参数：k=1、`max_turns=30`、并发 20、温度 agent 0.2 / 其余 0.0。**max_turns 说明**：仓库 argparse 默认 20、README 示例亦 20；本次 30 是为与 test50 全部既有臂（A–G，均 30）对齐的有意选择，非仓库默认值。
- 驱动：`tools/interopt_choice_test50_eval.py`（sha256-16 `847ba5ec9eac61aa`；逐题子进程 + 断点重试 + score_many 计分）；agent prompt `mc_d_agent_prompt.md` sha256-16 `0fb248f9d42bf80a`。
- **配置一致性核验（051 冒烟时完成）**：`git status experiments/` 干净（上游零改动）；run_config 与上次官方跑法（run_parallel 冒烟）逐字段对拍 24 项全同；差异仅四类——case/路径、max_turns（6→30，有意）、改名前的旧路径字符串、以及调度器簿记字段（本次逐题直调 vs 官方 `run_parallel.py`；后者自述"不改实验逻辑"）。协议形态实锤：transcript 里 MC-D 题带 Options A/B/C，模拟器按 option 或 "none of the offered options match"（allow_other）作答，`ledger_events.json` 落盘。
- 运行：2026-10-09（051 冒烟 1.3 分钟；全量 7.9 分钟）50/50。`run_health.json` 逐角色模型 = deepseek-flash ✓。无 FP8 空返回类问题。

## 一、聚合（50/50）

| 口径 | Core | AllSlot | Silent | net |
|---|---:|---:|---:|---:|
| 综合 | 0.5800 | 0.5800 | 0.500 | **0.5300** |
| eligibility 修正（剔除 ['orclarify_064', 'orclarify_072', 'orclarify_085']） | 0.6170 | — | — | **0.5485** |

## 二、八臂并排（同题集 / 同判分 / max_turns=30 / 单遍）

| 臂 | agent | 框架·设置·prompt | net | elig-修正 |
|---|---|---|---:|---:|
| A | qwen3.8-27b-fp8 | 基础协议 open × r22 冠军 | 0.6720 | 0.6943 |
| B | deepseek-flash | 基础协议 open × r22 冠军 | 0.6620 | 0.6843 |
| C | gpt-6.1-sol | 基础协议 open × 无策略 | 0.4160 | 0.4320 |
| D | deepseek-flash | 基础协议 open × 无策略 | 0.4120 | 0.4280 |
| E | qwen3.8-27b-fp8 | 基础协议 open × 随便问 | 0.4020 | 0.4167 |
| F | qwen3.8-27b-fp8 | Full InterOPT open | 0.2900 | 0.3028 |
| G | deepseek-flash | Full InterOPT open | 0.4100 | 0.4253 |
| **H** | **deepseek-flash** | **Full InterOPT choice (MC-D)** | **0.5300** | **0.5485** |

**H 是 InterOPT 系第一条真正越过全部 baseline 带的臂**（0.53 > C/D/E 的 0.40–0.42；距 r22 系 0.66–0.67 仍差 0.14）。与 paper 设计一致：InterOPT 是 **Choice 设置**的方法，open 设置属框架外消融。

两两对照（逐题胜负 / Δnet）：

| 对照 | 变量 | 胜负 | Δnet | 结论 |
|---|---|---|---|---|
| H vs G | choice vs open（同模型同框架） | 13:8（平 29） | **+0.1200** | 换设置是第一增量 |
| H vs D | choice-InterOPT vs 无策略 baseline | 13:4（平 33） | **+0.1180** | 框架在原生设置下确实加分 |
| H vs E | vs 随便问 | 16:9（平 25） | +0.1280 | — |
| H vs A | vs r22 冠军 | 8:12（平 30） | −0.1420 | 仍低于重策略臂 |

## 三、行为面（与 G 对照）

| 指标 | H（choice） | G（open） |
|---|---:|---:|
| avg turns | 10.9 | 11.14 |
| ready（主动收尾） | 40/50 | 29/50 |
| stopping | appropriate 27 / premature 13 / no_stop 10 | appropriate 20 / premature 16 / no_stop 14 |
| silent 均值 | 0.50 | 0.50 |

**解读**：换到 choice 的增益几乎全在 Core/AllSlot（0.48→0.58 / 0.44→0.58），silent 不变（0.50）——MC-D 的选项式提问让"问出关键槽"更容易，收尾纪律（appropriate 27 vs 20）也更好。Caveat：H 无 `gap_search_error` 类提前终止（G 臂同机制曾有 5 题）；no_stop 10 = 撞顶 7 + 3 题因 **user simulator 格式违规**（`user_format_invalid`：068×3 轮、070×7 轮、088×3 轮）提前终止——choice 口径下模拟器需按选项/allow_other 作答，个别轮次没答出合法形态。

## 四、逐题

| case | core | allslot | silent | net | turns | stopping |
|---|---:|---:|---:|---:|---:|---|
| orclarify_051 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_052 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_053 | +0.00 | +0.00 | 3 | -0.30 | 2 | premature_stop |
| orclarify_054 | +1.00 | +1.00 | 0 | +1.00 | 9 | appropriate_stop |
| orclarify_055 | +0.00 | +0.00 | 2 | -0.20 | 8 | premature_stop |
| orclarify_056 | +0.00 | +0.00 | 1 | -0.10 | 30 | no_stop |
| orclarify_057 | +1.00 | +1.00 | 0 | +1.00 | 17 | appropriate_stop |
| orclarify_058 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_059 | +0.00 | +0.00 | 1 | -0.10 | 17 | premature_stop |
| orclarify_060 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_061 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_062 | +0.00 | +0.00 | 1 | -0.10 | 4 | premature_stop |
| orclarify_063 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_064 | +0.00 | +0.00 | 1 | -0.10 | 2 | appropriate_stop |
| orclarify_065 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_066 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_067 | +1.00 | +1.00 | 0 | +1.00 | 11 | appropriate_stop |
| orclarify_068 | +1.00 | +1.00 | 0 | +1.00 | 3 | no_stop |
| orclarify_069 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_070 | +0.00 | +0.00 | 0 | +0.00 | 7 | no_stop |
| orclarify_071 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_072 | +0.00 | +0.00 | 1 | -0.10 | 6 | appropriate_stop |
| orclarify_073 | +0.00 | +0.00 | 1 | -0.10 | 6 | premature_stop |
| orclarify_074 | +1.00 | +1.00 | 0 | +1.00 | 15 | appropriate_stop |
| orclarify_075 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_076 | +1.00 | +1.00 | 0 | +1.00 | 10 | appropriate_stop |
| orclarify_077 | +0.00 | +0.00 | 4 | -0.40 | 6 | premature_stop |
| orclarify_078 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_079 | +0.00 | +0.00 | 1 | -0.10 | 5 | premature_stop |
| orclarify_080 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_081 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_082 | +1.00 | +1.00 | 0 | +1.00 | 10 | appropriate_stop |
| orclarify_083 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_084 | +1.00 | +1.00 | 0 | +1.00 | 9 | appropriate_stop |
| orclarify_085 | +0.00 | +0.00 | 1 | -0.10 | 5 | appropriate_stop |
| orclarify_086 | +1.00 | +1.00 | 0 | +1.00 | 8 | appropriate_stop |
| orclarify_087 | +1.00 | +1.00 | 0 | +1.00 | 10 | appropriate_stop |
| orclarify_088 | +1.00 | +1.00 | 0 | +1.00 | 3 | no_stop |
| orclarify_089 | +1.00 | +1.00 | 0 | +1.00 | 10 | appropriate_stop |
| orclarify_090 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_091 | +1.00 | +1.00 | 1 | +0.90 | 7 | appropriate_stop |
| orclarify_092 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_093 | +0.00 | +0.00 | 2 | -0.20 | 8 | premature_stop |
| orclarify_094 | +1.00 | +1.00 | 0 | +1.00 | 10 | appropriate_stop |
| orclarify_095 | +0.00 | +0.00 | 1 | -0.10 | 6 | premature_stop |
| orclarify_096 | +0.00 | +0.00 | 1 | -0.10 | 18 | premature_stop |
| orclarify_097 | +0.00 | +0.00 | 1 | -0.10 | 14 | premature_stop |
| orclarify_098 | +0.00 | +0.00 | 1 | -0.10 | 5 | premature_stop |
| orclarify_099 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_100 | +0.00 | +0.00 | 1 | -0.10 | 9 | premature_stop |

## 五、留痕

- 产物：本目录（summary.json、out_orclarify_0XX 全套 mid-run 产物含 ledger_events.json、logs/、summary（051 冒烟并入规范路径））。
- 相关：G 臂报告 `runs/test50_interopt_dsflash/RESULTS.md`；上游指纹见上；若需并入 `runs/test50_eval/RESULTS.md` 主表（八臂版）说一声。
