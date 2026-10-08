# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U16, U17, U18, U19, U20, U21, U22, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12, U13, U14, U15
I need help creating a farm operating plan where total land used for crops and dairy cows must not exceed 100 hectares, total investment for animals must not exceed 15,000 yuan, total person-days used for farm activities and external work in autumn and winter must not exceed 3,500, and in spring and summer must not exceed 4,000, the number of chickens cannot exceed 3,000, the number of dairy cows cannot exceed 32, and all labor day allocations (for crops and animals) must be integer numbers of days.

Total available land: 100 hectares.

Available funds: 15,000 yuan.

Available labor: 3,500 person-days in autumn and winter, 4,000 person-days in spring and summer.

External work earnings: 2.1 yuan/person-day in spring and summer, 1.8 yuan/person-day in autumn and winter.

Crop cultivation requires no specialized investment.

Investment cost per dairy cow: 400 yuan; per chicken: 3 yuan.

Land required per dairy cow for feed: 1.5 hectares.

Labor required per dairy cow: 100 person-days in autumn and winter, 50 person-days in spring and summer.

Annual net income per dairy cow: 400 yuan.

Labor required per chicken: 0.6 person-days in autumn and winter, 0.3 person-days in spring and summer.

Annual net income per chicken: 2 yuan.

Chicken coop maximum capacity: 3,000 chickens.

Cow barn maximum capacity: 32 dairy cows.

Crop labor and income requirements per year (per hectare):
| Item           | Soybean | Corn | Wheat |
|----------------|---------|------|-------|
| Person-days (Autumn/Winter) | 20      | 35   | 10    |
| Person-days (Spring/Summer) | 50      | 75   | 40    |
| Annual Net Income (Yuan/hectare) | 175     | 300   | 120   |

## Problem units
- U1 (context): I need help creating a farm operating plan.
- U2 (data): Total available land: 100 hectares.
- U3 (data): Available funds: 15,000 yuan.
- U4 (data): Available labor: 3,500 person-days in autumn and winter, 4,000 person-days in spring and summer.
- U5 (data): External work earnings: 2.1 yuan/person-day in spring and summer, 1.8 yuan/person-day in autumn and winter.
- U6 (data): Crop cultivation requires no specialized investment.
- U7 (data): Investment cost per dairy cow: 400 yuan; per chicken: 3 yuan.
- U8 (data): Land required per dairy cow for feed: 1.5 hectares.
- U9 (data): Labor required per dairy cow: 100 person-days in autumn and winter, 50 person-days in spring and summer.
- U10 (data): Annual net income per dairy cow: 400 yuan.
- U11 (data): Labor required per chicken: 0.6 person-days in autumn and winter, 0.3 person-days in spring and summer.
- U12 (data): Annual net income per chicken: 2 yuan.
- U13 (data): Chicken coop maximum capacity: 3,000 chickens.
- U14 (data): Cow barn maximum capacity: 32 dairy cows.
- U15 (data): Crop labor and income requirements per year (per hectare):
| Item           | Soybean | Corn | Wheat |
|----------------|---------|------|-------|
| Person-days (Autumn/Winter) | 20      | 35   | 10    |
| Person-days (Spring/Summer) | 50      | 75   | 40    |
| Annual Net Income (Yuan/hectare) | 175     | 300   | 120   |
- U16 (constraint): Total land used for crops and dairy cows must not exceed 100 hectares.
- U17 (constraint): Total investment for animals must not exceed 15,000 yuan.
- U18 (constraint): Total person-days used for farm activities and external work in autumn and winter must not exceed 3,500.
- U19 (constraint): Total person-days used for farm activities and external work in spring and summer must not exceed 4,000.
- U20 (constraint): Number of chickens cannot exceed 3,000.
- U21 (constraint): Number of dairy cows cannot exceed 32.
- U22 (constraint): All labor day allocations (for crops and animals) must be integer numbers of days.
- U23 (objective): Maximize total annual net income.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without knowing that the objective is to maximize annual net income, the agent cannot formulate a meaningful optimization model. Any arbitrary objective would likely be incorrect.
- Problem unit ID: U23
- Semantic hit rule: The agent's question must ask about the optimization objective, specifically inquiring what the farm wants to maximize (e.g., net income, profit).
- Reference acceptable questions:
  - What is the objective we are trying to optimize?
  - What is the goal of the farm's operating plan?
- Failure modes:
  - Silent assumption that the objective is to maximize total revenue rather than net income.
  - Silent assumption that the objective is to minimize costs or maximize crop yield.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: 关于"总土地用于作物和奶牛不得超过100公顷"这条约束，您希望它如何与"总可用土地100公顷"配合？具体是：(A) 作物种植面积 + 奶牛饲料用地 ≤ 100，且允许有剩余土地闲置（闲置不产生收益也不受罚）；(B) 作物种植面积 + 奶牛饲料用地必须恰好等于100（全部土地必须用满）；还是 (C) 其他处理方式？

## Turn 1 - User Simulator

选 (A)：作物种植面积 + 奶牛饲料用地 ≤ 100，允许有剩余土地闲置（闲置不产生收益也不受罚）。

## Turn 2 - Generic Agent

QUESTION: 关于"秋季和冬季、春季和夏季用于农场活动和外出打工的总人天数分别不得超过3500和4000"，外出打工的人天数是否计入这两个上限？即：(A) 农场活动人天 + 外出打工人天 ≤ 上限（外出打工占用劳动力，因此计入）；还是 (B) 只有农场活动人天 ≤ 上限，外出打工是额外的、不占用这3500/4000的？

## Turn 2 - User Simulator

选 (A)：农场活动人天 + 外出打工人天 ≤ 上限（外出打工占用劳动力，因此计入）。

## Turn 3 - Generic Agent

QUESTION: 关于外出打工的人天数，您希望模型如何处理？具体是：(A) 外出打工人天数是决策变量，模型在劳动力上限内自由决定打多少天（因为打工有正收益，模型会自动用满剩余劳动力）；还是 (B) 外出打工人天数是固定的（比如农场活动用完后剩余劳动力全部用于打工，即打工人天 = 上限 − 农场活动人天）？

## Turn 3 - User Simulator

选 (A)：外出打工人天数是决策变量，模型在劳动力上限内自由决定打多少天（因为打工有正收益，模型会自动用满剩余劳动力）。

## Turn 4 - Generic Agent

QUESTION: 关于"所有劳动天数分配（作物和动物）必须是整数天数"，请确认：(A) 作物种植面积（公顷）和动物数量（奶牛头数、鸡只数）都必须是整数；还是 (B) 只有动物数量（奶牛、鸡）必须是整数，作物种植面积可以是小数（比如种0.5公顷大豆）；还是 (C) 只有最终计算出的劳动天数（人天）必须是整数，而面积和数量可以是小数？

## Turn 4 - User Simulator

选 (C)：只有最终计算出的劳动天数（人天）必须是整数，而面积和数量可以是小数。

## Turn 5 - Generic Agent

QUESTION: 关于目标函数，您希望最大化的是什么？(A) 农场活动净收入 + 外出打工收入（即所有收入来源的总和）；还是 (B) 仅农场活动净收入（作物收入 + 奶牛收入 + 鸡收入），外出打工收入不计入目标（仅作为劳动力约束的一部分）？

## Turn 5 - User Simulator

选 (A)：农场活动净收入 + 外出打工收入（即所有收入来源的总和）。

## Turn 6 - Generic Agent

QUESTION: 关于劳动天数必须为整数这一约束，请确认：(A) 每种作物每种季节的劳动天数（如大豆秋/冬人天、玉米春/夏人天等）各自必须为整数；(B) 每种动物每种季节的劳动天数（如奶牛秋/冬人天、鸡春/夏人天等）各自必须为整数；还是 (C) 所有劳动天数（作物+动物，所有季节）的总和必须为整数（即只要总和是整数即可，单项可以是小数）？

## Turn 6 - User Simulator

选 (C)：所有劳动天数（作物+动物，所有季节）的总和必须为整数（即只要总和是整数即可，单项可以是小数）。

## Turn 7 - Generic Agent

QUESTION: 关于外出打工的人天数，是否也必须是整数？即：(A) 外出打工人天数（春/夏和秋/冬分别）也必须是整数；还是 (B) 外出打工人天数可以是小数，只有农场活动（作物+动物）的劳动天数总和需要为整数？

## Turn 7 - User Simulator

选 (B)：外出打工人天数可以是小数，只有农场活动（作物+动物）的劳动天数总和需要为整数。

## Turn 8 - Generic Agent

QUESTION: 关于"所有劳动天数（作物+动物，所有季节）的总和必须为整数"，请确认：(A) 秋/冬季节的农场活动总人天（三种作物秋/冬人天 + 奶牛秋/冬人天 + 鸡秋/冬人天）必须是整数，且春/夏季节的农场活动总人天（三种作物春/夏人天 + 奶牛春/夏人天 + 鸡春/夏人天）也必须是整数（即两个季节各自为整数）；还是 (B) 四个季节的农场活动人天加在一起（秋/冬 + 春/夏）的总和为整数即可，单个季节可以是小数？

## Turn 8 - User Simulator

选 (A)：秋/冬季节的农场活动总人天必须是整数，且春/夏季节的农场活动总人天也必须是整数（即两个季节各自为整数）。

## Turn 9 - Generic Agent

QUESTION: 关于作物种植面积，是否有任何下限要求？即：(A) 每种作物（大豆、玉米、小麦）的种植面积可以为零（模型自由决定是否种植）；还是 (B) 每种作物必须至少种植一定面积（比如每种至少种1公顷）？

## Turn 9 - User Simulator

选 (A)：每种作物（大豆、玉米、小麦）的种植面积可以为零（模型自由决定是否种植）。

## Turn 10 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否可以为零？即：(A) 奶牛和鸡的数量都可以为零（模型自由决定是否养）；还是 (B) 至少必须养一定数量的奶牛或鸡？

## Turn 10 - User Simulator

选 (A)：奶牛和鸡的数量都可以为零（模型自由决定是否养）。

## Turn 11 - Generic Agent

QUESTION: 关于投资约束"动物总投资不得超过15,000元"，请确认：(A) 只有奶牛和鸡的投资（400×奶牛数 + 3×鸡数）≤ 15,000，作物不占投资（因为您已说作物无需专项投资）；还是 (B) 还有其他动物或项目也占用这15,000元的投资额度？

## Turn 11 - User Simulator

选 (A)：只有奶牛和鸡的投资（400×奶牛数 + 3×鸡数）≤ 15,000，作物不占投资。

## Turn 12 - Generic Agent

QUESTION: 关于外出打工的人天数，是否存在上限（比如每人每年最多打工多少天）？即：(A) 外出打工人天数没有额外上限，只受劳动力总量约束（秋/冬≤3500、春/夏≤4000）限制；还是 (B) 外出打工人天数有额外的上限（比如春/夏最多打工X天，秋/冬最多打工Y天）？

## Turn 12 - User Simulator

选 (A)：外出打工人天数没有额外上限，只受劳动力总量约束（秋/冬≤3500、春/夏≤4000）限制。

## Turn 13 - Generic Agent

QUESTION: 关于外出打工的人天数，是否必须为非负数（即不能为负）？我假设外出打工人天数 ≥ 0（不能"负打工"），请确认：(A) 是的，外出打工人天数 ≥ 0；还是 (B) 有其他特殊处理？

## Turn 13 - User Simulator

选 (A)：是的，外出打工人天数 ≥ 0。

## Turn 14 - Generic Agent

QUESTION: 关于作物种植面积，是否必须为非负数（即不能为负）？我假设每种作物的种植面积 ≥ 0，请确认：(A) 是的，作物种植面积 ≥ 0；还是 (B) 有其他特殊处理？

## Turn 14 - User Simulator

选 (A)：是的，作物种植面积 ≥ 0。

## Turn 15 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否必须为非负数（即不能为负）？我假设奶牛数量 ≥ 0 且鸡数量 ≥ 0，请确认：(A) 是的，奶牛和鸡数量 ≥ 0；还是 (B) 有其他特殊处理？

## Turn 15 - User Simulator

选 (A)：是的，奶牛和鸡数量 ≥ 0。

## Turn 16 - Generic Agent

READY_TO_MODEL

以下是我确认的完整理解：

**决策变量：**
- 大豆、玉米、小麦的种植面积（公顷），连续，≥ 0
- 奶牛数量（头），连续，≥ 0
- 鸡数量（只），连续，≥ 0
- 春/夏外出打工人天数，连续，≥ 0
- 秋/冬外出打工人天数，连续，≥ 0

**目标函数：最大化总收入**
= 作物净收入（175×大豆面积 + 300×玉米面积 + 120×小麦面积）
+ 奶牛净收入（400×奶牛数）
+ 鸡净收入（2×鸡数）
+ 春/夏打工收入（2.1×春/夏打工人天）
+ 秋/冬打工收入（1.8×秋/冬打工人天）

**约束：**
1. 土地：大豆面积 + 玉米面积 + 小麦面积 + 1.5×奶牛数 ≤ 100（允许闲置）
2. 投资：400×奶牛数 + 3×鸡数 ≤ 15,000
3. 秋/冬劳动力：(20×大豆 + 35×玉米 + 10×小麦 + 100×奶牛 + 0.6×鸡) + 秋/冬打工人天 ≤ 3,500
4. 春/夏劳动力：(50×大豆 + 75×玉米 + 40×小麦 + 50×奶牛 + 0.3×鸡) + 春/夏打工人天 ≤ 4,000
5. 鸡数量 ≤ 3,000
6. 奶牛数量 ≤ 32
7. 秋/冬农场活动总人天（20×大豆 + 35×玉米 + 10×小麦 + 100×奶牛 + 0.6×鸡）必须为整数
8. 春/夏农场活动总人天（50×大豆 + 75×玉米 + 40×小麦 + 50×奶牛 + 0.3×鸡）必须为整数
9. 所有变量 ≥ 0