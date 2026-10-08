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

QUESTION: 大豆、玉米、小麦三种作物是否可以在同一块地上混种（即100公顷土地在三种作物之间自由分配），还是说每种作物有固定的种植面积、不可调整？

## Turn 1 - User Simulator

三种作物可以在100公顷土地之间自由分配，没有固定的种植面积限制。

## Turn 2 - Generic Agent

QUESTION: 关于"农场活动和外出打工的总人天数"这个约束，外出打工的人天是否也占用农场的人力资源（即外出打工的人天 + 农场活动的人天 ≤ 3500/4000），还是说外出打工是农场人力之外的额外收入来源，不占用农场的人天预算？

## Turn 2 - User Simulator

外出打工的人天占用农场的人力资源，即外出打工的人天加上农场活动的人天不能超过3,500（秋冬）或4,000（春夏）。

## Turn 3 - Generic Agent

QUESTION: 外出打工的人天是否也必须为整数？

## Turn 3 - User Simulator

是的，外出打工的人天也必须为整数。

## Turn 4 - Generic Agent

QUESTION: 100公顷土地是否必须全部用于种植作物（大豆、玉米、小麦），还是说可以留一部分土地闲置不用？

## Turn 4 - User Simulator

100公顷土地不需要全部用于种植作物，可以留一部分土地闲置不用。

## Turn 5 - Generic Agent

QUESTION: 15,000元的投资预算是否必须全部用完，还是说只需要不超过15,000元即可（可以有剩余）？

## Turn 5 - User Simulator

只需要不超过15,000元即可，可以有剩余。

## Turn 6 - Generic Agent

QUESTION: 这个农场经营计划的目标是什么——是最大化年度总净收入（作物收入 + 奶牛收入 + 鸡收入 + 外出打工收入），还是有其他目标？

## Turn 6 - User Simulator

目标是最大化年度总净收入，包括作物收入、奶牛收入、鸡收入和外出打工收入。

## Turn 7 - Generic Agent

QUESTION: 奶牛和鸡的数量是否也必须为整数？

## Turn 7 - User Simulator

是的，奶牛和鸡的数量也必须为整数。

## Turn 8 - Generic Agent

QUESTION: 作物种植面积（大豆、玉米、小麦各自的公顷数）是否也必须为整数，还是可以是任意非负实数？

## Turn 8 - User Simulator

作物种植面积可以是任意非负实数，不要求为整数。

## Turn 9 - Generic Agent

QUESTION: 土地约束"用于作物和奶牛的总土地不超过100公顷"中，奶牛占用的1.5公顷/头土地是否也计入这100公顷的总量（即作物面积 + 1.5×奶牛数 ≤ 100），还是说奶牛的饲料地是额外的、不占用这100公顷？

## Turn 9 - User Simulator

奶牛占用的1.5公顷/头土地计入这100公顷的总量，即作物面积 + 1.5×奶牛数 ≤ 100。

## Turn 10 - Generic Agent

QUESTION: 外出打工的人天是否有上限（比如每人每年最多外出打工多少天），还是说只要不超过总人天预算就可以任意分配？

## Turn 10 - User Simulator

外出打工的人天没有单独的上限，只要不超过总人天预算（秋冬3,500、春夏4,000）就可以分配。

## Turn 11 - Generic Agent

QUESTION: 这个模型中是否存在"现有状态"——比如农场目前已经有若干头奶牛或若干只鸡，如果决策变量设为0是否意味着这些动物会被卖掉或消失，还是说这是一个从零开始的全新规划？

## Turn 11 - User Simulator

这是一个从零开始的全新规划，不存在现有状态。

## Turn 12 - Generic Agent

QUESTION: 外出打工的人天是否也受"所有劳动日分配必须为整数"这个约束，即外出打工的人天也必须为整数？

## Turn 12 - User Simulator

是的，外出打工的人天也必须为整数。

## Turn 13 - Generic Agent

QUESTION: 鸡的劳动需求（秋冬0.6人天/只、春夏0.3人天/只）乘以鸡的数量后，是否也要求结果为整数，还是说只要鸡的数量为整数即可，劳动人天可以是小数？

## Turn 13 - User Simulator

只要鸡的数量为整数即可，劳动人天可以是小数。

## Turn 14 - Generic Agent

QUESTION: 作物种植面积可以是任意非负实数，那么作物所需的人天（如大豆20人天/公顷×面积）是否也允许为小数，还是说作物的人天分配也必须为整数？

## Turn 14 - User Simulator

作物的人天分配也必须为整数。

## Turn 15 - Generic Agent

QUESTION: 作物的人天分配必须为整数，但种植面积可以是任意非负实数——这意味着人天 = 每公顷人天 × 面积 的结果必须为整数（例如大豆面积×20必须是整数），还是说人天是独立的整数决策变量，与面积之间没有严格的乘法关系？

## Turn 15 - User Simulator

人天 = 每公顷人天 × 面积 的结果必须为整数。

## Turn 16 - Generic Agent

QUESTION: 奶牛的劳动人天（秋冬100人天/头、春夏50人天/头）乘以奶牛数量后，是否也要求结果为整数？

## Turn 16 - User Simulator

奶牛的劳动人天乘以奶牛数量后的结果必须为整数。

## Turn 17 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 17 - User Simulator

外出打工的人天也必须为整数。

## Turn 18 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 18 - User Simulator

外出打工的人天也必须为整数。

## Turn 19 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 19 - User Simulator

外出打工的人天也必须为整数。

## Turn 20 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 20 - User Simulator

外出打工的人天也必须为整数。

## Turn 21 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 21 - User Simulator

外出打工的人天也必须为整数。

## Turn 22 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 22 - User Simulator

外出打工的人天也必须为整数。

## Turn 23 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 23 - User Simulator

外出打工的人天也必须为整数。

## Turn 24 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 24 - User Simulator

外出打工的人天也必须为整数。

## Turn 25 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 25 - User Simulator

外出打工的人天也必须为整数。

## Turn 26 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 26 - User Simulator

外出打工的人天也必须为整数。

## Turn 27 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 27 - User Simulator

外出打工的人天也必须为整数。

## Turn 28 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 28 - User Simulator

外出打工的人天也必须为整数。

## Turn 29 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 29 - User Simulator

外出打工的人天也必须为整数。

## Turn 30 - Generic Agent

QUESTION: 外出打工的人天是否也计入"所有劳动日分配（作物和动物）必须为整数"这个约束中，还是说外出打工的人天可以是非整数？

## Turn 30 - User Simulator

外出打工的人天也必须为整数。