# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U8, U9, U2, U3, U4, U5
I need help creating a weekly production plan for Hongdou Clothing Factory. The factory uses three special equipment to produce shirts, short-sleeved shirts, and casual clothes, and each special equipment is dedicated to producing only one specific product type: the first produces shirts, the second produces short-sleeved shirts, the third produces casual clothes. Total labor used per week must not exceed the available 1500 units, and total material used per week must not exceed the available 1600 units.

| Product Name | Labor per unit | Material per unit | Selling Price | Variable Cost |
|--------------|----------------|------------------|---------------|---------------|
| Shirt        | 3              | 4                | 120           | 60            |
| Short-sleeve | 2              | 3                | 80            | 40            |
| Casual Cloth | 6              | 6                | 180           | 80            |

Available labor per week: 1500 units.

Available material per week: 1600 units.

Weekly fixed costs: shirt equipment 2000, short-sleeved shirt equipment 1500, casual clothes equipment 1000.

## Problem units
- U1 (context): I need help creating a weekly production plan for Hongdou Clothing Factory. The factory uses three special equipment to produce shirts, short-sleeved shirts, and casual clothes.
- U2 (data): | Product Name | Labor per unit | Material per unit | Selling Price | Variable Cost |
|--------------|----------------|------------------|---------------|---------------|
| Shirt        | 3              | 4                | 120           | 60            |
| Short-sleeve | 2              | 3                | 80            | 40            |
| Casual Cloth | 6              | 6                | 180           | 80            |
- U3 (data): Available labor per week: 1500 units.
- U4 (data): Available material per week: 1600 units.
- U5 (data): Weekly fixed costs: shirt equipment 2000, short-sleeved shirt equipment 1500, casual clothes equipment 1000.
- U6 (objective): Maximize weekly profit.
- U7 (constraint): Each special equipment is dedicated to producing only one specific product type: the first produces shirts, the second produces short-sleeved shirts, the third produces casual clothes.
- U8 (constraint): Total labor used per week must not exceed the available 1500 units.
- U9 (constraint): Total material used per week must not exceed the available 1600 units.

## Hidden slot scoring rules
## H1: missing_objective_profit
- Severity: P0
- Severity reason: Without knowing the objective, the modeling agent cannot define a meaningful optimization function; any production plan would be arbitrary and potentially misaligned with the factory's goals.
- Problem unit ID: U6
- Semantic hit rule: The agent must ask about the optimization goal or objective function, specifically whether the objective is to maximize profit or another metric.
- Reference acceptable questions:
  - What is the goal of the production plan?
  - Could you clarify whether we should maximize profit, revenue, or something else?
- Failure modes:
  - Silent incorrect assumption: assuming the objective is to maximize revenue.
  - Silent incorrect assumption: trying to minimize total cost without maximizing profit.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are the weekly fixed costs of 2000, 1500, and 1000 incurred only when the corresponding equipment is used to produce at least one unit, or are they paid every week regardless of production

## Turn 1 - User Simulator

They are paid every week regardless of production.

## Turn 2 - Generic Agent

QUESTION: Is the goal to maximize total weekly profit

## Turn 2 - User Simulator

Yes, the goal is to maximize total weekly profit.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities for shirts, short-sleeved shirts, and casual clothes required to be whole

## Turn 3 - User Simulator

Yes, production quantities must be whole numbers.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum production

## Turn 4 - User Simulator

No, there are no minimum production requirements.

## Turn 5 - Generic Agent

QUESTION: Are there any maximum

## Turn 5 - User Simulator

No, there are no maximum production limits beyond the labor and material constraints.

## Turn 6 - Generic Agent

QUESTION: Are there any other

## Turn 6 - User Simulator

No, there are no other constraints.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize total weekly profit.
- Decision variables: Weekly production quantities for shirts, short-sleeved shirts, and casual clothes.
- Variable domain: Non-negative integers (whole numbers, no minimums).
- Product-equipment mapping:
  - Equipment 1 produces only shirts.
  - Equipment 2 produces only short-sleeved shirts.
  - Equipment 3 produces only casual clothes.
- Per-unit data:
  - Shirt: labor 3, material 4, selling price 120, variable cost 60.
  - Short-sleeve: labor 2, material 3, selling price 80, variable cost 40.
  - Casual cloth: labor 6, material 6, selling price 180, variable cost 80.
- Resource constraints (weekly ceilings):
  - Total labor used ≤ 1500 units.
  - Total material used ≤ 1600 units.
- Fixed costs:
  - Shirt equipment: 2000 per week.
  - Short-sleeved shirt equipment: 1500 per week.
  - Casual clothes equipment: 1000 per week.
  - These are paid every week regardless of production (confirmed).
- No minimum production requirements (confirmed).
- No maximum production limits beyond labor and material constraints (confirmed).
- No other constraints (confirmed).

Assumptions (none required; all formulation-critical facts are confirmed).

Profit per unit:
- Shirt: 120 − 60 = 60.
- Short-sleeve: 80 − 40 = 40.
- Casual cloth: 180 − 80 = 100.

Total weekly fixed cost: 2000 + 1500 + 1000 = 4500.

Model:
Maximize: 60·x1 + 40·x2 + 100·x3 − 4500
Subject to:
- 3·x1 + 2·x2 + 6·x3 ≤ 1500 (labor)
- 4·x1 + 3·x2 + 6·x3 ≤ 1600 (material)
- x1, x2, x3 ≥ 0 and integer.