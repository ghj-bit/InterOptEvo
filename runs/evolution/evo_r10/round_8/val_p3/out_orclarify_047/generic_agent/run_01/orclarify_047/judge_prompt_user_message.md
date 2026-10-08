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

Let me build the requirement ledger before asking.

**Objective:** Maximize total annual net income (crops + animals + external work earnings). Direction: maximize. Horizon: one year.

**Decision variables:**
- Hectares of soybean, corn, wheat (continuous? integer? — UNKNOWN)
- Number of dairy cows (integer? bounded 0–32)
- Number of chickens (integer? bounded 0–3000)
- Person-days allocated to external work in autumn/winter and spring/summer (continuous? integer?)

**Constraints:**
- Land: crops + 1.5×cows ≤ 100 ha
- Investment: 400×cows + 3×chickens ≤ 15,000
- Labor autumn/winter: crops + 100×cows + 0.6×chickens + external ≤ 3,500
- Labor spring/summer: crops + 50×cows + 0.3×chickens + external ≤ 4,000
- Chickens ≤ 3,000
- Cows ≤ 32
- All labor day allocations (for crops and animals) must be integer

**Key uncertainties:**
1. Are crop hectares continuous or integer? (severity: changes feasible set)
2. Are external work person-days continuous or integer? (severity: changes feasible set)
3. Is the objective to maximize total income including external work earnings, or just farm income? (severity: changes optimal decision)
4. "All labor day allocations (for crops and animals) must be integer" — does this mean the total person-days per crop type must be integer, or per-hectare rates are fixed and only the total allocation is integer? (severity: changes feasible set)
5. Can land be left unused? (severity: minor, likely free)
6. Can funds be left unused? (severity: minor, likely free)

The most load-bearing question is whether external work earnings are part of the objective, because if they are, the model will always allocate remaining labor to external work, which fundamentally changes the structure.

QUESTION: Is the objective to maximize total annual income including earnings from external work, or only the net income from crops and animals (excluding external work earnings)?

## Turn 1 - User Simulator

The objective is to maximize total annual net income, which includes earnings from external work.

## Turn 2 - Generic Agent

Good, that's confirmed. Now let me think about the next highest-severity unknown.

The brief says "all labor day allocations (for crops and animals) must be integer numbers of days." This is a bit ambiguous. The labor requirements per hectare and per animal are given as fixed rates (e.g., 20 person-days per hectare of soybean in autumn/winter). If the number of hectares is continuous, then the total labor for that crop would be 20×hectares, which could be non-integer. The constraint says labor day allocations must be integer.

I think the most natural reading is: the total person-days allocated to each activity (each crop type, each animal type, and external work) must be an integer. But this could also mean that the decision variables representing labor must be integer, which would be a different formulation.

Actually, let me reconsider. The decision variables are likely: hectares of each crop, number of cows, number of chickens, and person-days of external work. The labor constraints are then linear combinations of these. The statement "all labor day allocations must be integer" most likely means that the total person-days used for each crop and animal category must be integer. But since labor per unit is fixed, this effectively constrains the product (e.g., 20 × soybean_hectares must be integer in autumn/winter).

Wait, but that's a very unusual constraint. More likely, the intent is that the number of cows and chickens are integers (which is natural), and the external work person-days are integers. The crop hectares might be continuous.

Let me ask about whether crop hectares must be integer or can be continuous, since that's a significant structural question.

QUESTION: Can the number of hectares allocated to each crop (soybean, corn, wheat) be any non-negative real number, or must they be whole numbers of hectares?

## Turn 2 - User Simulator

The number of hectares allocated to each crop can be any non-negative real number.

## Turn 3 - Generic Agent

Good. So crop hectares are continuous. Now, the brief states "all labor day allocations (for crops and animals) must be integer numbers of days." Since crop hectares are continuous, the labor for crops (e.g., 20 × soybean_hectares) would generally be non-integer. This constraint is a bit puzzling.

Let me think about what this could mean. Perhaps it means that the total person-days allocated to external work must be integer, and the number of cows and chickens must be integer. The "labor day allocations for crops and animals" being integer might just be a way of saying that cows and chickens are counted in whole units (so their labor contributions are automatically determined), and external work days are integer.

Or perhaps it means that the external work person-days must be integer. Let me ask about this.

QUESTION: When you say "all labor day allocations (for crops and animals) must be integer numbers of days," does this mean the person-days allocated to external work must be a whole number, or does it impose an additional integrality constraint on the total labor used by each crop and animal category?

## Turn 3 - User Simulator

It means the person-days allocated to external work must be a whole number.

## Turn 4 - Generic Agent

Good, that clarifies it. So external work person-days are integer. Now let me think about what else is uncertain.

Let me check the ledger:
- Objective: maximize total annual net income including external work earnings. STATED.
- Crop hectares: continuous, non-negative. STATED.
- Cows: integer, 0–32. The brief says "number of dairy cows cannot exceed 32" and "cow barn maximum capacity: 32 dairy cows." It's natural that cows are integer. But is it explicitly stated? The brief says "all labor day allocations (for crops and animals) must be integer numbers of days" which we've now clarified means external work days are integer. But cows and chickens are naturally integer (you can't have half a cow). I'll assume integer.
- Chickens: integer, 0–3000. Same reasoning.
- External work person-days: integer. STATED.
- Land: crops + 1.5×cows ≤ 100. STATED.
- Investment: 400×cows + 3×chickens ≤ 15,000. STATED.
- Labor constraints: STATED.
- Can land be left unused? The constraint is "must not exceed 100 hectares," so yes, it can be unused. STATED (by the "must not exceed" phrasing).
- Can funds be left unused? "Must not exceed 15,000 yuan," so yes. STATED.
- Can labor be left unused? "Must not exceed 3,500" and "must not exceed 4,000," so yes. STATED.

Wait, but if external work is part of the objective and earns positive income, then the model will always want to use all available labor for external work (since it's the only way to use leftover labor productively). So the labor constraints will be binding.

Actually, let me reconsider. The labor constraints are:
- Autumn/winter: crop_labor + 100×cows + 0.6×chickens + external_aw ≤ 3,500
- Spring/summer: crop_labor + 50×cows + 0.3×chickens + external_ss ≤ 4,000

Since external work earns positive income (2.1 and 1.8 yuan per person-day), the model will always allocate as much labor to external work as possible, up to the remaining labor after crops and animals. So the labor constraints will be binding (equality) in the optimal solution.

I think the model is now well-defined. Let me check if there's anything else.

One thing: the brief says "total land used for crops and dairy cows must not exceed 100 hectares." This means crop_hectares + 1.5×cows ≤ 100. The 1.5 hectares per cow is for feed. This is clear.

Another thing: "total investment for animals must not exceed 15,000 yuan." This is 400×cows + 3×chickens ≤ 15,000. Clear.

I think I have enough to model this. Let me declare ready.

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total annual net income, which is the sum of:
- Crop income: 175×soybean_ha + 300×corn_ha + 120×wheat_ha
- Animal income: 400×cows + 2×chickens
- External work earnings: 1.8×external_aw + 2.1×external_ss

**Decision variables:**
- soybean_ha, corn_ha, wheat_ha: continuous, ≥ 0
- cows: integer, 0 ≤ cows ≤ 32
- chickens: integer, 0 ≤ chickens ≤ 3,000
- external_aw: integer, ≥ 0 (person-days of external work in autumn/winter)
- external_ss: integer, ≥ 0 (person-days of external work in spring/summer)

**Constraints:**
1. Land: soybean_ha + corn_ha + wheat_ha + 1.5×cows ≤ 100
2. Investment: 400×cows + 3×chickens ≤ 15,000
3. Labor (autumn/winter): 20×soybean_ha + 35×corn_ha + 10×wheat_ha + 100×cows + 0.6×chickens + external_aw ≤ 3,500
4. Labor (spring/summer): 50×soybean_ha + 75×corn_ha + 40×wheat_ha + 50×cows + 0.3×chickens + external_ss ≤ 4,000
5. Chicken capacity: chickens ≤ 3,000
6. Cow capacity: cows ≤ 32