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

QUESTION: For the crops, is the land allocation a single annual area per crop (so each hectare of soybean, corn, or wheat uses its full annual labor in both seasons and earns its full annual income once per year), or is the land split into separate spring/summer and autumn/winter plantings that each consume their own season's labor and earn income separately?

## Turn 1 - User Simulator

It is a single annual area per crop. Each hectare of soybean, corn, or wheat uses its full annual labor in both seasons and earns its full annual income once per year.

## Turn 2 - Generic Agent

QUESTION: For the external work, is the person-days spent on external work a decision variable that you can choose up to the seasonal labor cap (earning the given wage per day), or is it simply whatever labor remains unused after crops and animals are assigned?

## Turn 2 - User Simulator

It is a decision variable that you can choose up to the seasonal labor cap, earning the given wage per day.

## Turn 3 - Generic Agent

QUESTION: Is the objective to maximize total annual net income, where total income equals the sum of crop income (per hectare), animal income (per cow and per chicken), and external work earnings (person-days times the seasonal wage)?

## Turn 3 - User Simulator

Yes, the objective is to maximize total annual net income, where total income equals the sum of crop income (per hectare), animal income (per cow and per chicken), and external work earnings (person-days times the seasonal wage).

## Turn 4 - Generic Agent

QUESTION: For the land constraint, is the 100-hectare limit the sum of the three crop areas plus the 1.5 hectares of feed land per dairy cow (i.e., crops + 1.5 × cows ≤ 100), with chickens using no land?

## Turn 4 - User Simulator

Yes, the 100-hectare limit is the sum of the three crop areas plus the 1.5 hectares of feed land per dairy cow, with chickens using no land.

## Turn 5 - Generic Agent

QUESTION: For the investment constraint, is the 15,000-yuan limit the sum of 400 yuan per dairy cow plus 3 yuan per chicken (i.e., 400 × cows + 3 × chickens ≤ 15,000), with crops requiring no investment?

## Turn 5 - User Simulator

Yes, the 15,000-yuan limit is the sum of 400 yuan per dairy cow plus 3 yuan per chicken, with crops requiring no investment.

## Turn 6 - Generic Agent

QUESTION: For the labor constraints, is the autumn/winter limit the sum of crop labor (per-hectare rates times areas), cow labor (100 per cow), chicken labor (0.6 per chicken), and external work person-days, all ≤ 3,500, with the spring/summer limit similarly ≤ 4,000?

## Turn 6 - User Simulator

Yes, the autumn/winter limit is the sum of crop labor (per-hectare rates times areas), cow labor (100 per cow), chicken labor (0.6 per chicken), and external work person-days, all ≤ 3,500, with the spring/summer limit similarly ≤ 4,000.

## Turn 7 - Generic Agent

QUESTION: You said all labor day allocations for crops and animals must be integers. Does this mean the crop areas (hectares) and the numbers of cows and chickens must be integers, or does it mean the resulting labor person-days (e.g., 20 × soybean area) must be whole numbers while the areas themselves could be fractional?

## Turn 7 - User Simulator

It means the crop areas (hectares) and the numbers of cows and chickens must be integers.

## Turn 8 - Generic Agent

QUESTION: For the external work person-days, must these also be integers, or can they be any non-negative value (continuous) up to the seasonal labor cap?

## Turn 8 - User Simulator

The external work person-days must also be integers.

## Turn 9 - Generic Agent

QUESTION: Are there any lower bounds on the decisions — for example, must you plant at least some hectares of each crop, keep at least some cows or chickens, or do all crop areas, cow count, chicken count, and external work days simply have to be non-negative (zero allowed)?

## Turn 9 - User Simulator

All crop areas, cow count, chicken count, and external work days simply have to be non-negative (zero allowed).

## Turn 10 - Generic Agent

QUESTION: Is there any additional rule linking the seasons — for example, must the external work person-days be the same in both seasons, or is there any other cross-season constraint — or are the two seasons completely independent except that they share the same crop/animal decisions?

## Turn 10 - User Simulator

The two seasons are completely independent except that they share the same crop/animal decisions.

## Turn 11 - Generic Agent

QUESTION: One last check on the income figures: are the given annual net incomes (175/300/120 yuan per hectare for crops, 400 yuan per cow, 2 yuan per chicken) already net of all costs, so I should use them directly as revenue in the objective without subtracting any additional expenses?

## Turn 11 - User Simulator

Yes, the given annual net incomes are already net of all costs, so they should be used directly as revenue in the objective without subtracting any additional expenses.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decisions (all non-negative integers):**
- Crop areas: soybean, corn, wheat (hectares)
- Number of dairy cows
- Number of chickens
- External work person-days in autumn/winter and in spring/summer

**Objective:** Maximize total annual net income =
- Crop income: 175·soybean + 300·corn + 120·wheat (yuan)
- Cow income: 400·cows
- Chicken income: 2·chickens
- External work: 1.8·(AW external days) + 2.1·(SS external days)

**Constraints:**
1. Land: soybean + corn + wheat + 1.5·cows ≤ 100
2. Investment: 400·cows + 3·chickens ≤ 15,000
3. Autumn/winter labor: 20·soybean + 35·corn + 10·wheat + 100·cows + 0.6·chickens + AW external days ≤ 3,500
4. Spring/summer labor: 50·soybean + 75·corn + 40·wheat + 50·cows + 0.3·chickens + SS external days ≤ 4,000
5. Chicken capacity: chickens ≤ 3,000
6. Cow capacity: cows ≤ 32
7. All decision variables are non-negative integers

**Notes:**
- Each crop is a single annual area (full annual labor in both seasons, income once per year)
- The two seasons are independent except for shared crop/animal decisions
- All income figures are net of costs, used directly in the objective
- No lower bounds (zero allowed for all decisions)