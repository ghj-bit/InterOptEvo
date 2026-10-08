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

QUESTION: Are the weekly fixed costs (2000, 1500, 1000) incurred only when the corresponding equipment is actually used to produce a positive quantity of its product, or are they paid every week regardless of whether that equipment runs?

## Turn 1 - User Simulator

They are paid every week regardless of whether that equipment runs.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units of each product can be produced per week (for example, a maximum demand or a machine capacity), or can each product be produced in any non-negative amount as long as the labor and material totals stay within their limits?

## Turn 2 - User Simulator

There is no limit on how many units of each product can be produced per week. Each product can be produced in any non-negative amount as long as the total labor and material usage stay within their limits.

## Turn 3 - Generic Agent

QUESTION: Should the production quantities be whole numbers (you can only make a whole shirt), or is it fine to treat them as continuous amounts?

## Turn 3 - User Simulator

The production quantities should be whole numbers.

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize the weekly total profit (total revenue minus total variable costs, with the fixed equipment costs treated as a constant that does not affect the decision), or is there a different objective you want optimized?

## Turn 4 - User Simulator

The goal is to maximize the weekly total profit.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products & equipment:** Three dedicated equipment, one per product type — equipment 1 makes shirts, equipment 2 makes short-sleeved shirts, equipment 3 makes casual clothes.
- **Decision variables:** Weekly production quantity of each product (shirt, short-sleeve, casual cloth), each a non-negative integer (whole units).
- **Objective:** Maximize weekly total profit = total revenue − total variable costs. Profit per unit: shirt 120−60 = 60, short-sleeve 80−40 = 40, casual cloth 180−80 = 100.
- **Fixed costs:** The equipment fixed costs (shirt 2000, short-sleeve 1500, casual 1000) are paid every week regardless of usage, so they are a constant and do not affect the production decision (they can be subtracted from the final profit figure if a net profit number is desired).
- **Resource constraints (per week):**
  - Labor: 3·(shirts) + 2·(short-sleeves) + 6·(casual) ≤ 1500
  - Material: 4·(shirts) + 3·(short-sleeves) + 6·(casual) ≤ 1600
- **No per-product upper bounds** (no demand or machine-capacity limits); quantities are only bounded by the labor and material constraints.
- **Horizon:** One week.

I will now formulate the integer linear program.