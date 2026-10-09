# test50 · Full InterOPT × FP8 单臂报告（2026-10-09）

- 框架：`experiments/open_interopt/`（Full InterOPT：Stage 1 gap memory + Stage 2 ask-or-stop；原生 prompts，6 文件含 `gap_search_prompt.md`）。**上游文件未改动**（`run_pipeline.py` sha256-16 `c428dd6c222c2b9c`）
- 题集：orclarify_051–100（== splits["test"]）；单遍 k=1、`max_turns=30`、并发 20；总用时 20.1 分钟（2026-10-09 17:30–17:50，50/50）
- 模型（全部 think 关，与 test50 五臂逐字段对齐）：agent / user_simulator / detector / gap-search = qwen3.8-27b-fp8（本地 FP8，经 18770）；judge = deepseek-flash（经代理 judge 路由）。think 关的实证：代理 dump 中 FP8 路由注入 `enable_thinking=false`、judge 行注入 `thinking disabled`、gap-search 调用另叠 pipeline 侧 `thinking_type="disabled"`
- 温度：agent 0.2 / detector·user·judge 0.0
- 驱动：`tools/interopt_test50_eval.py`（sha256-16 `f90342bb91368c2d`，照 test50 臂同构：逐题子进程 + 断点重试 + summary）；包装：`tools/run_interopt_fp8.py`（sha256-16 `d822af3bcb75af25`，向上游 MODEL_PROFILES 注入 qwen3_8_27b_fp8 / deepseek_flash 两个 profile，不改上游）
- prompt 指纹：`experiments/open_interopt/prompts/generic_agent_prompt.md` sha256-16 `e85eb351a046940c`（原生，非 r27 非随便问）；代理 `tools/cap_proxy.py` sha256-16 `6a4c72dfb5d05f5a`
- 冒烟 051 的产物经 `out_orclarify_051 -> smoke_051` 软链并入计分；098 首轮卡 FP8 空返回、重试时断点重放通过（未消耗守卫）
- 计分：`orclarify_evolution.score_many` + eligibility 修正（与五臂同口径）

## 一、聚合（50/50）

| 口径 | Core | AllSlot | Silent | net |
|---|---:|---:|---:|---:|
| 综合 | 0.4000 | 0.3800 | 1.000 | **0.2900** |
| eligibility 修正（剔除 ['orclarify_064', 'orclarify_072', 'orclarify_085']） | 0.4255 | — | — | **0.3028** |

## 二、与 test50 五臂并排（同题集 / 同判分 / 同 max_turns=30 / 单遍）

| 臂 | agent | 框架·prompt | net | elig-修正 net |
|---|---|---|---:|---:|
| A | qwen3.8-27b-fp8 | evaluation_protocol × r22 冠军策略 | 0.6720 | 0.6943 |
| B | deepseek-flash | evaluation_protocol × r22 冠军策略 | 0.6620 | 0.6843 |
| C | gpt-6.1-sol | evaluation_protocol × 无策略 baseline | 0.4160 | 0.4320 |
| D | deepseek-flash | evaluation_protocol × 无策略 baseline | 0.4120 | 0.4280 |
| E | qwen3.8-27b-fp8 | evaluation_protocol × 随便问（+协议行） | 0.4020 | 0.4167 |
| **F** | **qwen3.8-27b-fp8** | **Full InterOPT（原生 prompts + 两阶段）** | **0.2900** | **0.3028** |

**F 低于全部五臂**——包括同模型的 E 臂（−0.112）与最弱的无策略 baseline（−0.122）。

## 三、行为面（50 题）

| 指标 | 值 |
|---|---|
| avg turns | 6.12（五臂为 8.6–13.1；同模型 E 臂 12.3） |
| ready（主动 READY_TO_MODEL） | 46/50 |
| stopping | appropriate 21 / premature 25 / no_stop 4 |
| turns 分布 | 1轮×6、2轮×12、3轮×5、4轮×5、5轮×5、6轮×6、7轮×2、8轮×1、9轮×3、11轮×1、30轮×4 |
| silent 均值 | 1.00 条/题（≈ −0.10 net/题） |

**机制解读**：低分的两个直接来源——①**过度自信的提前收尾**：18/50 题 ≤2 轮就自报 `Formulatable confidence ≈1.0` 宣布 READY_TO_MODEL（25/50 判 premature）；②**静默假设罚分**：提前收尾的总结里把未问槽整批当既定事实（silent ≈1/题）。同一个 FP8 模型在基础协议（E 臂）平均问 12.3 轮，在 InterOPT 原生 prompt 下只问 6.12 轮——**框架的两阶段机制没有帮上弱模型，反而放大了它的 stop 校准缺陷**。与 paper 设定（InterOPT 系方法配 v4pro/gpt-5.5/opus 等强模型）形成对照。

## 四、逐题

| case | core | allslot | silent | net | turns | stopping |
|---|---:|---:|---:|---:|---:|---|
| orclarify_051 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_052 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_053 | +0.00 | +0.00 | 3 | -0.30 | 1 | premature_stop |
| orclarify_054 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_055 | +0.00 | +0.00 | 2 | -0.20 | 5 | premature_stop |
| orclarify_056 | +0.00 | +0.00 | 3 | -0.30 | 6 | premature_stop |
| orclarify_057 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_058 | +0.00 | +0.00 | 3 | -0.30 | 9 | premature_stop |
| orclarify_059 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_060 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_061 | +0.00 | +0.00 | 1 | -0.10 | 1 | premature_stop |
| orclarify_062 | +0.00 | +0.00 | 2 | -0.20 | 1 | premature_stop |
| orclarify_063 | +1.00 | +0.00 | 1 | +0.40 | 3 | appropriate_stop |
| orclarify_064 | +0.00 | +0.00 | 1 | -0.10 | 1 | appropriate_stop |
| orclarify_065 | +0.00 | +0.00 | 3 | -0.30 | 6 | premature_stop |
| orclarify_066 | +0.00 | +0.00 | 1 | -0.10 | 2 | premature_stop |
| orclarify_067 | +1.00 | +1.00 | 0 | +1.00 | 9 | appropriate_stop |
| orclarify_068 | +1.00 | +1.00 | 1 | +0.90 | 8 | appropriate_stop |
| orclarify_069 | +1.00 | +1.00 | 0 | +1.00 | 4 | appropriate_stop |
| orclarify_070 | +0.00 | +0.00 | 3 | -0.30 | 2 | premature_stop |
| orclarify_071 | +0.00 | +0.00 | 2 | -0.20 | 4 | premature_stop |
| orclarify_072 | +0.00 | +0.00 | 1 | -0.10 | 2 | appropriate_stop |
| orclarify_073 | +0.00 | +0.00 | 2 | -0.20 | 2 | premature_stop |
| orclarify_074 | +1.00 | +1.00 | 0 | +1.00 | 6 | appropriate_stop |
| orclarify_075 | +1.00 | +1.00 | 0 | +1.00 | 5 | appropriate_stop |
| orclarify_076 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_077 | +0.00 | +0.00 | 4 | -0.40 | 2 | premature_stop |
| orclarify_078 | +0.00 | +0.00 | 2 | -0.20 | 9 | premature_stop |
| orclarify_079 | +0.00 | +0.00 | 1 | -0.10 | 1 | premature_stop |
| orclarify_080 | +0.00 | +0.00 | 1 | -0.10 | 11 | premature_stop |
| orclarify_081 | +1.00 | +1.00 | 0 | +1.00 | 7 | appropriate_stop |
| orclarify_082 | +0.00 | +0.00 | 1 | -0.10 | 2 | premature_stop |
| orclarify_083 | +1.00 | +1.00 | 0 | +1.00 | 4 | appropriate_stop |
| orclarify_084 | +0.00 | +0.00 | 1 | -0.10 | 2 | premature_stop |
| orclarify_085 | +0.00 | +0.00 | 2 | -0.20 | 2 | appropriate_stop |
| orclarify_086 | +1.00 | +1.00 | 0 | +1.00 | 3 | appropriate_stop |
| orclarify_087 | +0.00 | +0.00 | 1 | -0.10 | 2 | premature_stop |
| orclarify_088 | +1.00 | +1.00 | 0 | +1.00 | 4 | appropriate_stop |
| orclarify_089 | +0.00 | +0.00 | 1 | -0.10 | 4 | premature_stop |
| orclarify_090 | +1.00 | +1.00 | 0 | +1.00 | 3 | appropriate_stop |
| orclarify_091 | +0.00 | +0.00 | 1 | -0.10 | 2 | premature_stop |
| orclarify_092 | +1.00 | +1.00 | 0 | +1.00 | 3 | appropriate_stop |
| orclarify_093 | +0.00 | +0.00 | 2 | -0.20 | 1 | premature_stop |
| orclarify_094 | +1.00 | +1.00 | 0 | +1.00 | 30 | no_stop |
| orclarify_095 | +0.00 | +0.00 | 1 | -0.10 | 3 | premature_stop |
| orclarify_096 | +0.00 | +0.00 | 0 | +0.00 | 30 | no_stop |
| orclarify_097 | +0.00 | +0.00 | 1 | -0.10 | 5 | premature_stop |
| orclarify_098 | +0.00 | +0.00 | 1 | -0.10 | 5 | premature_stop |
| orclarify_099 | +1.00 | +1.00 | 0 | +1.00 | 2 | appropriate_stop |
| orclarify_100 | +0.00 | +0.00 | 1 | -0.10 | 2 | premature_stop |

## 五、产物与留痕

- 本目录：`summary.json`（逐题 + aggregate）、`out_orclarify_0XX/`（每题目录，含 transcript/judge_result/statistics/gap_search_events 等全套）、`logs/`、`cases/`
- 冒烟：`smoke_051/`（单题先行验证：Stage1/2 运转、think 全关、可计分）
- 已知边界：098 首轮因 FP8 确定性空返回中断、重试断点重放通过；判分器为 deepseek-flash（跨判分器不可比）
