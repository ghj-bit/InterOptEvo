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

QUESTION: Are the weekly fixed costs (2000 / 1500 / 1000) incurred only when the corresponding equipment is actually used to produce at least one unit of its product, or are they paid every week regardless of whether that equipment runs?

## Turn 1 - User Simulator

They are paid every week regardless of whether that equipment runs.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum weekly production quantities for each product (for example, a demand cap on how many units of each product can be sold, or a minimum run size), or can each product's weekly output be any nonnegative amount up to what the labor and material limits allow?

## Turn 2 - User Simulator

Each product's weekly output can be any nonnegative amount up to what the labor and material limits allow.

## Turn 3 - Generic Agent

QUESTION: Should the weekly production quantities be whole numbers (integer units), or is it fine to treat them as continuous values (allowing fractional units)?

## Turn 3 - User Simulator

The weekly production quantities should be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize weekly profit, where profit equals total revenue minus total variable costs minus the three fixed equipment costs (which are constant each week)?

## Turn 4 - User Simulator

Yes, the objective is to maximize weekly profit, where profit equals total revenue minus total variable costs minus the three fixed equipment costs.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three dedicated equipment, one per product:
  - Equipment 1 → Shirts
  - Equipment 2 → Short-sleeved shirts
  - Equipment 3 → Casual clothes
- **Decision variables:** Weekly production quantity of each product, each a nonnegative integer (whole units). No minimum or maximum per-product limits beyond the resource constraints.
- **Resources (weekly, hard ceilings):**
  - Labor ≤ 1500 units
  - Material ≤ 1600 units
- **Per-unit data:**
  - Shirt: labor 3, material 4, price 120, variable cost 60
  - Short-sleeve: labor 2, material 3, price 80, variable cost 40
  - Casual cloth: labor 6, material 6, price 180, variable cost 80
- **Fixed costs:** 2000 (shirt equipment) + 1500 (short-sleeve equipment) + 1000 (casual equipment) = 4500 per week, paid every week regardless of whether the equipment runs.
- **Objective:** Maximize weekly profit = total revenue − total variable costs − 4500 fixed costs.

Since the fixed costs are constant, maximizing profit is equivalent to maximizing total contribution margin (revenue − variable costs) subject to the labor and material constraints, with integer production quantities.