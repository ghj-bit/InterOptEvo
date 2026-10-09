# test50 · Full InterOPT × deepseek-flash 单臂报告（2026-10-09，G 臂）

- 目的：与 F 臂（InterOPT × qwen3.8-27b-fp8）严格对齐、只换"被测模型"——把四个非 judge 角色从本地 FP8 换成 deepseek-flash。
- 模型 id 说明：DS 官方目录只有 `deepseek-flash` 与 `deepseek-v4-pro`，**无 `deepseek-v4-flash`**；本臂按 `deepseek-flash`（v4 系 flash 档）执行，profile 名沿用 `deepseek_v4_flash`。
- 框架：`experiments/open_interopt/`（Full InterOPT：Stage1 gap memory + Stage2 ask-or-stop；原生 prompts，上游未改动 `c428dd6c222c2b9c`；prompts `generic_agent_prompt.md` sha256-16 `e85eb351a046940c`）
- 角色与路由：agent / user_simulator / detector / gap-search = **deepseek-flash**，judge = **deepseek-flash**（全角色同模型；judge 由 "Judge Prompt" 标记优先路由）。经 18775 独立代理实例（`tools/cap_proxy_dsagent.py`，sha256-16 `f2541ad0a0f4b213`：judge→DS 16384；model==deepseek-flash→DS **关 thinking** 2048）。全部 think 关
- 参数：k=1、`max_turns=30`、并发 20、温度 agent 0.2 / 其余 0.0；题集 orclarify_051–100；单遍，计分 `score_many` + eligibility 修正（与五臂同口径）
- 驱动：`tools/interopt_test50_eval.py`（sha256-16 `6a41a1f29f87b33f`，本次加 `--base-url/--agent-profile/--judge-profile/--wrapper` 参数化，默认值不变）+ 包装 `tools/run_interopt_dsflash.py`（sha256-16 `d95fadcd05453465`，向上游注入 `deepseek_v4_flash` profile）
- 运行：2026-10-09 17:55–18:01（**4.9 分钟**，50/50；051 冒烟 0.4 分钟先行验证路由与产物）。无 FP8 空返回类问题（远端 API）

## 一、聚合（50/50）

| 口径 | Core | AllSlot | Silent | net |
|---|---:|---:|---:|---:|
| 综合 | 0.4800 | 0.4400 | 0.500 | **0.4100** |
| eligibility 修正（剔除 ['orclarify_064', 'orclarify_072', 'orclarify_085']） | 0.5106 | — | — | **0.4253** |

## 二、七臂并排（同题集 / 同判分 / 同 max_turns=30 / 单遍）

| 臂 | agent | 框架·prompt | net | elig-修正 |
|---|---|---|---:|---:|
| A | qwen3.8-27b-fp8 | 基础协议 × r22 冠军 | 0.6720 | 0.6943 |
| B | deepseek-flash | 基础协议 × r22 冠军 | 0.6620 | 0.6843 |
| C | gpt-6.1-sol | 基础协议 × 无策略 | 0.4160 | 0.4320 |
| D | deepseek-flash | 基础协议 × 无策略 | 0.4120 | 0.4280 |
| E | qwen3.8-27b-fp8 | 基础协议 × 随便问 | 0.4020 | 0.4167 |
| F | qwen3.8-27b-fp8 | Full InterOPT | 0.2900 | 0.3028 |
| **G** | **deepseek-flash** | **Full InterOPT** | **0.4100** | **0.4253** |

**G ≈ C/D/E（baseline 带）**：换掉弱模型后，InterOPT 的框架惩罚基本消失（F→G +0.12），但**仍拿不到超过基础协议基线的增益**。2×2 视角：框架×模型 = (qwen: 0.29 | dsflash: 0.41)，基础协议×模型 = (0.402 | 0.412)——**框架在两种模型下都没赚分；对弱模型是负增益**。

## 三、行为面（50 题，与 F 对照）

| 指标 | G（dsflash） | F（qwen FP8） |
|---|---:|---:|
| avg turns | 11.14 | 6.12 |
| ready（主动收尾） | 29/50 | 46/50 |
| stopping | appropriate 20 / premature 16 / no_stop 14 | appropriate 21 / premature 25 / no_stop 4 |
| silent 均值 | 0.50 | 1.00 |
| turns 分布 | 1–14 轮为主（≤2 轮 5 题）、30 轮 9 题 | ≤2 轮 18 题、30 轮 4 题 |

**解读**：dsflash 的 stop 校准远好于 27B FP8——提前拍板率减半（premature 16 vs 25）、silent 减半（0.50 vs 1.00）；另一端它更少早停（no_stop 14 vs 4，撞顶多）。结果就是落回 baseline 带：**没有多问出分，也没多罚分**。

## 四、逐题

| case | core | allslot | silent | net | turns | stopping |
|---|---:|---:|---:|---:|---:|---|
| orclarify_051 | +1.00 | +1.00 | 0 | +1.00 | 3 | appropriate_stop |
| orclarify_052 | +1.00 | +1.00 | 0 | +1.00 | 10 | appropriate_stop |
| orclarify_053 | +0.00 | +0.00 | 3 | -0.30 | 2 | premature_stop |
| orclarify_054 | +1.00 | +1.00 | 0 | +1.00 | 8 | appropriate_stop |
| orclarify_055 | +0.00 | +0.00 | 2 | -0.20 | 11 | premature_stop |
| orclarify_056 | +0.00 | +0.00 | 0 | +0.00 | 20 | no_stop |
| orclarify_057 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_058 | +0.00 | +0.00 | 2 | -0.20 | 9 | premature_stop |
| orclarify_059 | +0.00 | +0.00 | 1 | -0.10 | 11 | premature_stop |
| orclarify_060 | +1.00 | +1.00 | 0 | +1.00 | 8 | appropriate_stop |
| orclarify_061 | +0.00 | +0.00 | 1 | -0.10 | 3 | premature_stop |
| orclarify_062 | +0.00 | +0.00 | 2 | -0.20 | 5 | premature_stop |
| orclarify_063 | +1.00 | +0.00 | 1 | +0.40 | 4 | appropriate_stop |
| orclarify_064 | +0.00 | +0.00 | 1 | -0.10 | 5 | appropriate_stop |
| orclarify_065 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_066 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_067 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_068 | +1.00 | +1.00 | 0 | +1.00 | 9 | appropriate_stop |
| orclarify_069 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_070 | +1.00 | +0.00 | 0 | +0.50 | 9 | appropriate_stop |
| orclarify_071 | +1.00 | +1.00 | 0 | +1.00 | 11 | appropriate_stop |
| orclarify_072 | +0.00 | +0.00 | 1 | -0.10 | 4 | appropriate_stop |
| orclarify_073 | +0.00 | +0.00 | 2 | -0.20 | 4 | premature_stop |
| orclarify_074 | +1.00 | +1.00 | 0 | +1.00 | 9 | appropriate_stop |
| orclarify_075 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_076 | +0.00 | +0.00 | 0 | +0.00 | 3 | no_stop |
| orclarify_077 | +0.00 | +0.00 | 2 | -0.20 | 8 | premature_stop |
| orclarify_078 | +0.00 | +0.00 | 0 | +0.00 | 1 | premature_stop |
| orclarify_079 | +0.00 | +0.00 | 1 | -0.10 | 4 | premature_stop |
| orclarify_080 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_081 | +0.00 | +0.00 | 0 | +0.00 | 1 | no_stop |
| orclarify_082 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_083 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_084 | +0.00 | +0.00 | 0 | +0.00 | 3 | premature_stop |
| orclarify_085 | +0.00 | +0.00 | 2 | -0.20 | 7 | appropriate_stop |
| orclarify_086 | +1.00 | +1.00 | 0 | +1.00 | 24 | no_stop |
| orclarify_087 | +1.00 | +1.00 | 0 | +1.00 | 12 | appropriate_stop |
| orclarify_088 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_089 | +0.00 | +0.00 | 1 | -0.10 | 6 | premature_stop |
| orclarify_090 | +1.00 | +1.00 | 0 | +1.00 | 2 | appropriate_stop |
| orclarify_091 | +0.00 | +0.00 | 1 | -0.10 | 5 | premature_stop |
| orclarify_092 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_093 | +0.00 | +0.00 | 1 | -0.10 | 7 | premature_stop |
| orclarify_094 | +0.00 | +0.00 | 0 | +0.00 | 4 | no_stop |
| orclarify_095 | +1.00 | +1.00 | 0 | +1.00 | 14 | appropriate_stop |
| orclarify_096 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_097 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_098 | +0.00 | +0.00 | 1 | -0.10 | 13 | premature_stop |
| orclarify_099 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_100 | +0.00 | +0.00 | 0 | +0.00 | 1 | premature_stop |

## 五、留痕与口径注记

- 产物：本目录（summary.json、out_orclarify_0XX 全套 mid-run 产物、logs/、proxy_dsflash_18775.log）；051 冒烟直接落在规范路径（无需软链）。
- 口径注记：paper 的 InterOPT 系方法主表在 **Choice 设置**；本臂是"Full InterOPT 跑 Open/FreeQA 设置"的消融，跨框架数字（如 README 表 1 的 v4pro 0.426）不与本表混比。
- 上游零改动（open_interopt 指纹在案）；新增文件 `tools/run_interopt_dsflash.py`、驱动参数化改动（默认行为不变）。
