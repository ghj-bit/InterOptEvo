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

QUESTION: 除了奶牛和鸡之外，是否还有其他动物（例如猪、羊等）需要纳入计划，还是本次计划只涉及奶牛、鸡和三种作物（大豆、玉米、小麦）？

## Turn 1 - User Simulator

本次计划只涉及奶牛、鸡和三种作物（大豆、玉米、小麦），没有其他动物需要纳入。

## Turn 2 - Generic Agent

QUESTION: 关于土地约束，"作物和奶牛用地合计不超过100公顷"是否意味着鸡的鸡舍用地不计入这100公顷（即鸡舍用地是独立的、不占用耕地），还是鸡舍用地也需要从100公顷中扣除？

## Turn 2 - User Simulator

鸡舍用地不计入这100公顷，鸡舍用地是独立的，不占用耕地。

## Turn 3 - Generic Agent

QUESTION: 关于劳动力约束，"农场活动和外出打工的用工合计"是否意味着外出打工的工时可以自由分配（即外出打工是吸收剩余劳动力的手段，其工时 = 可用工时 − 农场用工），还是外出打工的工时也是一个需要单独决策的变量？

## Turn 3 - User Simulator

外出打工的工时是吸收剩余劳动力的手段，其工时等于可用工时减去农场用工，不需要单独决策。

## Turn 4 - Generic Agent

QUESTION: 目标函数是最大化年度总净收入（作物收入 + 奶牛收入 + 鸡收入 + 外出打工收入），还是只最大化农场内部收入（作物 + 奶牛 + 鸡），外出打工收入不计入目标？

## Turn 4 - User Simulator

目标函数是最大化年度总净收入，包括作物收入、奶牛收入、鸡收入和外出打工收入。

## Turn 5 - Generic Agent

QUESTION: 关于"所有劳动日分配（作物和动物）必须为整数天"这一约束，是否意味着每种作物种植面积（公顷）和每种动物数量（头/只）都必须是整数，还是仅要求每种作物和动物所消耗的总劳动日数为整数（即面积和数量可以是小数，只要乘出来的总工数是整数）？

## Turn 5 - User Simulator

仅要求每种作物和动物所消耗的总劳动日数为整数，面积和数量可以是小数，只要乘出来的总工数是整数即可。

## Turn 6 - Generic Agent

QUESTION: 关于劳动力约束，是否要求每个季节（秋/冬和春/夏）的农场用工（作物+奶牛+鸡）分别不超过该季节的可用工时（3500和4000），还是只要求两个季节的农场用工合计不超过总可用工时（7500）？

## Turn 6 - User Simulator

要求每个季节（秋/冬和春/夏）的农场用工分别不超过该季节的可用工时（3500和4000）。

## Turn 7 - Generic Agent

QUESTION: 关于土地约束，是否要求每种作物的种植面积（大豆、玉米、小麦）各自非负即可，还是存在某种最低种植面积要求（例如每种作物至少种一定面积）？

## Turn 7 - User Simulator

每种作物的种植面积各自非负即可，不存在最低种植面积要求。

## Turn 8 - Generic Agent

QUESTION: 关于奶牛和鸡的数量，是否允许为0（即可以不养奶牛或不养鸡），还是必须至少养一定数量？

## Turn 8 - User Simulator

奶牛和鸡的数量允许为0，即可以不养奶牛或不养鸡，没有最低数量要求。

## Turn 9 - Generic Agent

QUESTION: 关于外出打工收入，是否假设外出打工的工时可以完全利用（即只要农场用工不超过可用工时，剩余工时全部用于外出打工并获得对应收入），还是存在外出打工的工时上限（例如每年最多只能外出打工一定天数）？

## Turn 9 - User Simulator

外出打工的工时可以完全利用，只要农场用工不超过可用工时，剩余工时全部用于外出打工并获得对应收入，不存在外出打工的工时上限。

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables (all continuous, non-negative):**
- x₁, x₂, x₃: hectares of soybean, corn, wheat
- x₄: number of dairy cows
- x₅: number of chickens

**Objective: Maximize total annual net income**
= 175x₁ + 300x₂ + 120x₃ + 400x₄ + 2x₅ + 2.1×(4000 − spring/summer farm labor) + 1.8×(3500 − autumn/winter farm labor)

**Constraints:**

1. **Land:** x₁ + x₂ + x₃ + 1.5x₄ ≤ 100 (chicken coop land is separate, not counted)
2. **Investment:** 400x₄ + 3x₅ ≤ 15000
3. **Autumn/Winter labor:** 20x₁ + 35x₂ + 10x₃ + 100x₄ + 0.6x₅ ≤ 3500
4. **Spring/Summer labor:** 50x₁ + 75x₂ + 40x₃ + 50x₄ + 0.3x₅ ≤ 4000
5. **Chicken capacity:** x₅ ≤ 3000
6. **Cow capacity:** x₄ ≤ 32
7. **Integer labor days:** The total labor days consumed by each crop and each animal type must be integers:
   - 20x₁, 35x₂, 10x₃, 100x₄, 0.6x₅ (autumn/winter) are integers
   - 50x₁, 75x₂, 40x₃, 50x₄, 0.3x₅ (spring/summer) are integers
8. **Non-negativity:** all variables ≥ 0

**Notes:**
- External work absorbs all remaining labor; no upper bound on external work hours.
- No minimum area or minimum animal count required.
- Only dairy cows, chickens, and three crops are in scope.