# val20 单臂报告 · qwen3.8-27b-fp8 + 随便问（+协议行）（2026-10-09 晚）

- 题集：orclarify_031–050（"中间二十道题"，== splits["val"]，与 train 001–030 / test 051–100 零重叠）
- 目的：把 test50 E 臂的策略配置搬到 val 集，与 evo_r10 自身在同 20 题上的 val 数字（同 harness / 同 18770 代理 / 同 dsflash 判分）直接对照
- 配置：与 test50 E 臂逐字段一致——agent=qwen3.8-27b-fp8（经 18770 cap_proxy）、user_simulator/detector=qwen3.8-27b-fp8（本地 FP8）、judge=deepseek-flash；单遍 k=1、max_turns=30、并发 20；`prompts_dir=runs/prompts_askanything`（generic_agent_prompt.md sha256-16 `9f58f0fe77b1a6c4`）
- 驱动：`tools/test50_eval.py --arm qwen --prompts-dir runs/prompts_askanything --out-root runs/test50_eval/askanything_qwen_val20 --cases 31-50`
- 运行：2026-10-09 16:51–16:58（主跑 5.0 分钟，19/20）；046 卡 FP8 确定性空返回（simulator 调用 @1786），断点续跑重放即通过（未消耗守卫救援）；重算后 **20/20**
- 产物：本目录（summary.json、逐 case 产物、logs/）

## 一、结果

| 口径 | Core | AllSlot | Silent | net |
|---|---:|---:|---:|---:|
| 综合（20/20） | 0.6000 | 0.6000 | 0.5500 | **0.5450** |
| eligibility 修正（剔除 037：无 P0/P1 槽） | 0.6316 | — | — | **0.5608** |

## 二、与 evo_r10 自身 val 数字对照（同 harness / 同代理 / 同判分 / max_turns=30）

| 臂 | 策略 | passes | net | 来源 |
|---|---|---:|---:|---|
| E-val | 随便问（+协议行） | 1 | **0.5450** | 本次 |
| seed (round_0) | OptMATH evo4-r4 策略 | 3 | 0.6483 | state.json round 0（本次复算吻合） |
| champion (r22) | 演化 30 轮冠军 | 3 | 0.8050 | state.json champion（本次复算吻合） |

逐题胜负（E 单遍 vs 3 遍均值）：**E vs seed = 6:8（平 6）**；**E vs champ = 1:9（平 10）**。

## 三、逐题（net）

| case | E 单遍 | seed | champ |
|---|---:|---:|---:|
| orclarify_031 | +0.90 | +1.00 | +1.00 |
| orclarify_032 | +1.00 | +1.00 | +1.00 |
| orclarify_033 | +1.00 | +1.00 | +1.00 |
| orclarify_034 | +1.00 | +1.00 | +1.00 |
| orclarify_035 | +1.00 | +0.63 | +1.00 |
| orclarify_036 | -0.10 | +0.30 | +1.00 |
| orclarify_037 | +0.00 | -0.07 | +0.13 |
| orclarify_038 | +1.00 | +1.00 | +1.00 |
| orclarify_039 | -0.10 | +1.00 | +1.00 |
| orclarify_040 | +1.00 | +1.00 | +1.00 |
| orclarify_041 | -0.10 | +0.27 | +0.97 |
| orclarify_042 | +1.00 | +0.63 | +1.00 |
| orclarify_043 | +1.00 | +1.00 | +1.00 |
| orclarify_044 | -0.10 | +1.00 | +1.00 |
| orclarify_045 | +1.00 | +0.63 | +1.00 |
| orclarify_046 | +1.00 | +0.27 | +0.27 |
| orclarify_047 | +1.00 | +0.63 | +1.00 |
| orclarify_048 | -0.20 | +0.27 | +0.67 |
| orclarify_049 | -0.30 | +0.13 | -0.20 |
| orclarify_050 | -0.10 | +0.27 | +0.27 |

## 四、一句话

随便问在 val 上同样低于结构化种子（−0.103）与冠军（−0.260），与 test50 结论同向（随便问 ≈/≤ 无策略水平）。
口径注记：本次单遍、对照为 3 遍均值；E 臂用上游格式文档（`## Behavior` 换策略、协议行保留），seed/champ 用演化 policy 文档；单遍噪声不足以解释 −0.10 级差异（跨题集方向一致）。
