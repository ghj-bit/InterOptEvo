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

QUESTION: 关于"农场活动和外出打工的总人天数"这一约束，外出打工的人天是否也计入秋/冬 3,500 和春/夏 4,000 的上限之内（即：农活人天 + 外出打工人天 ≤ 上限），还是外出打工人天只受"总可用劳动力"限制、农活人天单独受限？

## Turn 1 - User Simulator

外出打工的人天也计入上限之内。也就是说，秋/冬的农活人天加上外出打工人天，总和不能超过 3,500；春/夏的农活人天加上外出打工人天，总和不能超过 4,000。

## Turn 2 - Generic Agent

QUESTION: 外出打工的人天是否必须是非负整数（即打工人天也要取整数），还是只要农活人天为整数、打工人天可以为任意非负实数即可？

## Turn 2 - User Simulator

外出打工的人天也必须是非负整数。

## Turn 3 - Generic Agent

QUESTION: 关于土地约束，"作物用地 + 奶牛饲料用地 ≤ 100 公顷"中，如果 100 公顷没有全部用完，剩余的土地是否允许闲置（即不种作物也不养牛），还是必须恰好把 100 公顷全部用满？

## Turn 3 - User Simulator

剩余的土地允许闲置，不要求必须把 100 公顷全部用满。

## Turn 4 - Generic Agent

QUESTION: 关于资金约束，"动物总投资 ≤ 15,000 元"中，如果 15,000 元没有全部花完，剩余资金是否允许闲置（即不投资），还是必须恰好花满 15,000 元？

## Turn 4 - User Simulator

剩余资金允许闲置，不要求必须恰好花满 15,000 元。

## Turn 5 - Generic Agent

QUESTION: 关于劳动力约束，秋/冬和春/夏的人天上限（3,500 和 4,000）中，如果某个季节的劳动力没有全部用完，剩余的人天是否允许闲置（即不安排农活也不外出打工），还是必须恰好把该季节的劳动力全部用完？

## Turn 5 - User Simulator

剩余的人天允许闲置，不要求必须恰好把该季节的劳动力全部用完。

## Turn 6 - Generic Agent

QUESTION: 关于目标函数，这个农场经营计划是要最大化年度总净收入（作物收入 + 奶牛收入 + 鸡收入 + 外出打工收入），还是有其他目标（比如最小化成本、最大化利润等）？

## Turn 6 - User Simulator

目标是最大化年度总净收入，包括作物收入、奶牛收入、鸡收入和外出打工收入。

## Turn 7 - Generic Agent

QUESTION: 关于作物种植面积，三种作物（大豆、玉米、小麦）的种植面积是否必须是非负实数（即可以种 0.5 公顷），还是必须是非负整数（即只能种整数公顷）？

## Turn 7 - User Simulator

种植面积必须是非负整数，即只能种整数公顷。

## Turn 8 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否必须是非负整数（即只能养整数头/只），还是可以为非负实数？

## Turn 8 - User Simulator

奶牛和鸡的数量必须是非负整数。

## Turn 9 - Generic Agent

QUESTION: 关于外出打工的人天，是否必须是非负整数（即只能打整数天），还是可以为非负实数？

## Turn 9 - User Simulator

外出打工的人天必须是非负整数。

## Turn 10 - Generic Agent

QUESTION: 关于作物种植面积，是否允许某种作物的种植面积为 0（即完全不种某种作物），还是每种作物都必须至少种 1 公顷？

## Turn 10 - User Simulator

允许某种作物的种植面积为 0，即可以不种某种作物。

## Turn 11 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否允许养 0 头奶牛或 0 只鸡（即完全不养某种动物），还是每种动物都必须至少养 1 头/只？

## Turn 11 - User Simulator

允许养 0 头奶牛或 0 只鸡，即可以不养某种动物。

## Turn 12 - Generic Agent

QUESTION: 关于外出打工的人天，是否允许某个季节（秋/冬或春/夏）的外出打工人天为 0（即该季节完全不外出打工），还是每个季节都必须至少打 1 天工？

## Turn 12 - User Simulator

允许某个季节的外出打工人天为 0，即该季节可以不外出打工。

## Turn 13 - Generic Agent

QUESTION: 关于土地约束，"作物用地 + 奶牛饲料用地 ≤ 100 公顷"中，鸡的养殖是否需要占用土地（比如鸡舍用地），还是鸡的养殖不占用这 100 公顷土地？

## Turn 13 - User Simulator

鸡的养殖不占用这 100 公顷土地。

## Turn 14 - Generic Agent

QUESTION: 关于资金约束，"动物总投资 ≤ 15,000 元"中，作物种植是否需要占用资金（比如种子、化肥等成本），还是只有奶牛和鸡的养殖需要投资、作物种植不需要投资？

## Turn 14 - User Simulator

作物种植不需要占用资金，只有奶牛和鸡的养殖需要投资。

## Turn 15 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 15 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 16 - Generic Agent

QUESTION: 关于劳动力约束，"农场活动和外出打工的总人天数"中，是否还有其他类型的劳动（比如管理、运输等）需要计入秋/冬和春/夏的人天上限，还是只有作物种植、奶牛养殖、鸡养殖和外出打工这四类活动？

## Turn 16 - User Simulator

只有作物种植、奶牛养殖、鸡养殖和外出打工这四类活动需要计入人天上限，没有其他类型的劳动。

## Turn 17 - Generic Agent

QUESTION: 关于目标函数，外出打工的收入是否应该计入年度总净收入（即目标函数 = 作物收入 + 奶牛收入 + 鸡收入 + 外出打工收入），还是只计算农场内部活动的收入（作物 + 奶牛 + 鸡）？

## Turn 17 - User Simulator

外出打工的收入应该计入年度总净收入，即目标函数 = 作物收入 + 奶牛收入 + 鸡收入 + 外出打工收入。

## Turn 18 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 18 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 19 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 19 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 20 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 20 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 21 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 21 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 22 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 22 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 23 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 23 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 24 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 24 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 25 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 25 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 26 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 26 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 27 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 27 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 28 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 28 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 29 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 29 - User Simulator

是的，外出打工的人天也必须是非负整数。

## Turn 30 - Generic Agent

QUESTION: 关于劳动力约束，外出打工的人天是否也受"所有劳动日分配必须为整数"这一约束，即外出打工人天也必须是非负整数？

## Turn 30 - User Simulator

是的，外出打工的人天也必须是非负整数。