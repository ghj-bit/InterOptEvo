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

QUESTION: Are the weekly fixed costs (2000 / 1500 / 1000) incurred only when the corresponding equipment is actually used to produce a positive quantity of its product, or are they paid every week regardless of whether that equipment runs?

## Turn 1 - User Simulator

They are incurred only when the corresponding equipment is actually used to produce a positive quantity of its product.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum weekly production quantities for each product (for example, a minimum order commitment or a maximum demand cap), or can each product's weekly output be any nonnegative amount up to what the labor and material limits allow?

## Turn 2 - User Simulator

There are no minimum or maximum weekly production quantities for each product. Each product's weekly output can be any nonnegative amount up to what the labor and material limits allow.

## Turn 3 - Generic Agent

QUESTION: Should the production quantities be whole numbers of units, or is it acceptable to treat them as continuous (fractional) values in the plan?

## Turn 3 - User Simulator

The production quantities should be whole numbers of units.

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize the factory's weekly profit, where profit equals total selling revenue minus total variable costs minus the fixed costs of the equipment actually used?

## Turn 4 - User Simulator

Yes, the goal is to maximize the factory's weekly profit, where profit equals total selling revenue minus total variable costs minus the fixed costs of the equipment actually used.

## Turn 5 - Generic Agent

QUESTION: Is the plan for a single week only, with no carryover of inventory or work-in-progress to other weeks, so that everything produced in the week is sold in that same week?

## Turn 5 - User Simulator

Yes, the plan is for a single week only, with no carryover of inventory or work-in-progress to other weeks. Everything produced in the week is sold in that same week.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three products, each made only on its dedicated equipment: shirts (equipment 1), short-sleeved shirts (equipment 2), casual clothes (equipment 3).
- **Decision variables:** Weekly production quantity of each product, x1 (shirts), x2 (short-sleeves), x3 (casual clothes), each a nonnegative integer.
- **Objective:** Maximize weekly profit = total revenue − total variable cost − fixed costs of equipment actually used.
  - Per-unit contribution: shirt 120−60 = 60; short-sleeve 80−40 = 40; casual 180−80 = 100.
  - Fixed costs (2000 / 1500 / 1000) are incurred only when the corresponding product's quantity is positive.
- **Resource constraints (per week):**
  - Labor: 3·x1 + 2·x2 + 6·x3 ≤ 1500.
  - Material: 4·x1 + 3·x2 + 6·x3 ≤ 1600.
- **No other bounds:** No minimum or maximum production quantities; no inventory or carryover; single-week horizon; everything produced is sold in the same week.
- **Integrality:** All production quantities must be whole numbers.

This is a mixed-integer program: the fixed-cost terms make it a fixed-charge problem, so I will introduce a binary variable for each product indicating whether its equipment is used, link it to the production quantity (quantity positive only if the binary is 1), and subtract the corresponding fixed cost when the binary is 1.