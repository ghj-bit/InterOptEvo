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

QUESTION: Are the weekly fixed equipment costs (2000, 1500, 1000) incurred only when the corresponding equipment is actually used to produce a positive quantity of its product, or are they paid every week regardless of whether that equipment runs?

## Turn 1 - User Simulator

They are paid every week regardless of whether that equipment runs.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum weekly production quantities for any of the three products, or can each product's weekly output be any non-negative amount (including zero)?

## Turn 2 - User Simulator

Each product's weekly output can be any non-negative amount, including zero.

## Turn 3 - Generic Agent

QUESTION: Is the goal of the weekly plan to maximize total weekly profit, where profit equals total revenue minus total variable costs minus the fixed equipment costs?

## Turn 3 - User Simulator

Yes, the goal is to maximize total weekly profit, where profit equals total revenue minus total variable costs minus the fixed equipment costs.

## Turn 4 - Generic Agent

QUESTION: Do the labor and material constraints apply to the total across all three products combined, or does each product have its own separate labor and material limit?

## Turn 4 - User Simulator

The labor and material constraints apply to the total across all three products combined.

## Turn 5 - Generic Agent

QUESTION: Can the weekly production quantities be fractional (e.g., 10.5 shirts), or must they be whole numbers?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or business rules I should account for, such as demand limits, storage capacity, or minimum order requirements?

## Turn 6 - User Simulator

No, there are no other constraints or business rules to account for beyond the labor, material, and equipment dedication rules already mentioned.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products & equipment:** Three products, each made only on its dedicated equipment: shirts (equipment 1), short-sleeved shirts (equipment 2), casual clothes (equipment 3).
- **Decision variables:** Weekly production quantity of each product, non-negative, no minimum or maximum bounds. Integrality is still pending internal confirmation, so I will model quantities as continuous non-negative variables and note that if whole units are required, the variables should be made integer.
- **Objective:** Maximize total weekly profit = total revenue − total variable costs − fixed equipment costs.
  - Unit contribution: shirt 120−60 = 60; short-sleeve 80−40 = 40; casual 180−80 = 100.
  - Fixed costs: 2000 + 1500 + 1000 = 4500 per week, paid regardless of whether any equipment runs (constant, so it does not affect the optimal quantities but is included in the reported profit).
- **Constraints (shared across all products):**
  - Labor: 3·x_shirt + 2·x_short + 6·x_casual ≤ 1500
  - Material: 4·x_shirt + 3·x_short + 6·x_casual ≤ 1600
- **No other constraints:** no demand caps, storage limits, or minimum orders.