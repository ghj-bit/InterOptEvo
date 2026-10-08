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

QUESTION: 关于"农场活动和外出打工的总人天数"这一约束，外出打工的人天是否也计入秋季/冬季 3,500 和春季/夏季 4,000 的人天上限（即：作物+奶牛+鸡的用工 + 外出打工人天 ≤ 上限），还是说 3,500/4,000 只是农场内部活动的上限，外出打工的人天是另外单独计算的？

## Turn 1 - User Simulator

外出打工的人天也计入上限。也就是说，秋季/冬季的总人天（作物+奶牛+鸡的用工 + 外出打工人天）≤ 3,500，春季/夏季的总人天（作物+奶牛+鸡的用工 + 外出打工人天）≤ 4,000。

## Turn 2 - Generic Agent

QUESTION: 关于土地约束，"作物和奶牛使用的总土地不得超过100公顷"——鸡是否也需要占用土地（比如鸡舍用地），还是说鸡不占用这100公顷土地，只有作物用地和奶牛饲料地（每头1.5公顷）计入土地约束？

## Turn 2 - User Simulator

鸡不占用这100公顷土地。只有作物用地和奶牛饲料地（每头1.5公顷）计入土地约束。

## Turn 3 - Generic Agent

QUESTION: 关于投资约束，"动物总投资不得超过15,000元"——这里的投资是否只包括奶牛（每头400元）和鸡（每只3元）的投入，即 400×奶牛数 + 3×鸡数 ≤ 15,000？还是说这15,000元是农场总可用资金，还需要扣除其他用途（比如外出打工的机会成本或其他开支）？

## Turn 3 - User Simulator

这里的投资只包括奶牛和鸡的投入，即 400×奶牛数 + 3×鸡数 ≤ 15,000。这15,000元是专门用于动物投资的资金，不需要扣除其他用途。

## Turn 4 - Generic Agent

QUESTION: 关于目标函数，这个农场经营计划是要最大化年度总净收入（作物收入 + 奶牛收入 + 鸡收入 + 外出打工收入）吗？

## Turn 4 - User Simulator

是的，目标是最大化年度总净收入，包括作物收入、奶牛收入、鸡收入和外出打工收入。

## Turn 5 - Generic Agent

QUESTION: 关于外出打工的人天，是否有一个上限（比如最多只能外出打工多少天），还是说只要农场活动用不完的人天都可以用于外出打工，没有额外限制？

## Turn 5 - User Simulator

没有额外限制。只要农场活动用不完的人天都可以用于外出打工，唯一的上限就是秋季/冬季3,500人天和春季/夏季4,000人天的总人天约束。

## Turn 6 - Generic Agent

QUESTION: 关于变量取整要求，"所有劳动日分配（作物和动物）必须是整数天"——这是否意味着作物种植面积（公顷）也必须是整数，还是说只有最终计算出的劳动日总数需要是整数，而种植面积可以是小数？

## Turn 6 - User Simulator

只有最终计算出的劳动日总数需要是整数，种植面积可以是小数。

## Turn 7 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否必须是整数（即不能养0.5头奶牛或1.5只鸡），还是说可以取小数？

## Turn 7 - User Simulator

奶牛和鸡的数量必须是整数，不能取小数。

## Turn 8 - Generic Agent

QUESTION: 关于外出打工的人天，是否也必须是整数，还是说可以是小数（比如外出打工0.5天）？

## Turn 8 - User Simulator

外出打工的人天也必须是整数。

## Turn 9 - Generic Agent

QUESTION: 关于作物种植面积，是否每块作物（大豆、玉米、小麦）的种植面积都必须非负（即不能为负数），且没有最低种植要求（即可以完全不种某种作物）？

## Turn 9 - User Simulator

是的，每种作物的种植面积必须非负，且没有最低种植要求，可以完全不种某种作物。

## Turn 10 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否也必须非负（即不能为负数），且没有最低饲养要求（即可以完全不养奶牛或完全不养鸡）？

## Turn 10 - User Simulator

是的，奶牛和鸡的数量必须非负，且没有最低饲养要求，可以完全不养奶牛或完全不养鸡。

## Turn 11 - Generic Agent

READY_TO_MODEL

以下是我确认的完整理解：

**决策变量：**
- 大豆、玉米、小麦的种植面积（公顷），连续非负变量
- 奶牛数量（头），非负整数
- 鸡的数量（只），非负整数
- 秋季/冬季外出打工的人天数，非负整数
- 春季/夏季外出打工的人天数，非负整数

**目标函数：**
最大化年度总净收入 = 作物收入（175×大豆面积 + 300×玉米面积 + 120×小麦面积）+ 奶牛收入（400×奶牛数）+ 鸡收入（2×鸡数）+ 外出打工收入（1.8×秋冬打工人天 + 2.1×春夏打工人天）

**约束条件：**
1. 土地：大豆面积 + 玉米面积 + 小麦面积 + 1.5×奶牛数 ≤ 100 公顷
2. 动物投资：400×奶牛数 + 3×鸡数 ≤ 15,000 元
3. 秋冬人天：20×大豆面积 + 35×玉米面积 + 10×小麦面积 + 100×奶牛数 + 0.6×鸡数 + 秋冬打工人天 ≤ 3,500
4. 春夏人天：50×大豆面积 + 75×玉米面积 + 40×小麦面积 + 50×奶牛数 + 0.3×鸡数 + 春夏打工人天 ≤ 4,000
5. 鸡数量 ≤ 3,000
6. 奶牛数量 ≤ 32
7. 所有劳动日分配（作物、动物、外出打工）为整数
8. 所有变量非负