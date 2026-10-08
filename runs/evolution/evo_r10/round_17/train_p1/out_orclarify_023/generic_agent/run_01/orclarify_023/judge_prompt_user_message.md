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

QUESTION: Are the weekly fixed costs (2000, 1500, 1000) incurred only when the corresponding equipment is actually used (i.e., when production of that product is positive), or are they paid every week regardless of whether that product is produced?

## Turn 1 - User Simulator

They are paid every week regardless of whether that product is produced.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum weekly production quantities for each product (for example, a minimum order that must be met, or a maximum the equipment can produce per week), or can each product's weekly output be any non-negative amount?

## Turn 2 - User Simulator

Each product's weekly output can be any non-negative amount.

## Turn 3 - Generic Agent

QUESTION: Should the weekly production quantities be whole numbers (integer units), or is it acceptable to plan fractional units of each product?

## Turn 3 - User Simulator

The weekly production quantities should be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize the factory's total weekly profit (total revenue minus total variable costs, with the fixed equipment costs treated as constant and therefore not affecting the decision)?

## Turn 4 - User Simulator

Yes, the goal is to maximize the factory's total weekly profit.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products & equipment:** Three dedicated pieces of equipment, one per product type:
  - Equipment 1 → Shirts
  - Equipment 2 → Short-sleeved shirts
  - Equipment 3 → Casual clothes
- **Decision variables:** Weekly production quantity of each product (x_shirt, x_short, x_casual), each a **non-negative integer**. No minimum or maximum per-product limits.
- **Resources (weekly caps):**
  - Labor: 3·x_shirt + 2·x_short + 6·x_casual ≤ 1500
  - Material: 4·x_shirt + 3·x_short + 6·x_casual ≤ 1600
- **Objective:** Maximize total weekly profit = (120−60)·x_shirt + (80−40)·x_short + (180−80)·x_casual = 60·x_shirt + 40·x_short + 100·x_casual.
- **Fixed costs:** 2000 (shirt equipment) + 1500 (short-sleeve equipment) + 1000 (casual equipment) = 4500 per week, paid regardless of production. Since they are constant, they do not affect the optimization decision (they can be subtracted from the optimal objective to report net profit if desired).

I will now formulate and solve this integer linear program.