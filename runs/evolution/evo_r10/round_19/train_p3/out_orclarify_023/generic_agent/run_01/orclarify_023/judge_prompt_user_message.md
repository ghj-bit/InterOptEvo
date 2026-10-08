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

QUESTION: Are there any minimum or maximum weekly production quantities for each product (shirt, short-sleeved shirt, casual clothes), or can each product's weekly output be any non-negative amount?

## Turn 2 - User Simulator

Each product's weekly output can be any non-negative amount.

## Turn 3 - Generic Agent

QUESTION: Should the weekly production quantities be whole numbers (integer units), or can they be fractional amounts?

## Turn 3 - User Simulator

The weekly production quantities should be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize the weekly total profit, where profit equals total selling revenue minus total variable costs minus the fixed equipment costs?

## Turn 4 - User Simulator

Yes, the goal is to maximize the weekly total profit, where profit equals total selling revenue minus total variable costs minus the fixed equipment costs.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three dedicated equipment, each producing exactly one product type:
  - Equipment 1 → Shirts
  - Equipment 2 → Short-sleeved shirts
  - Equipment 3 → Casual clothes

- **Decision variables:** Weekly production quantity of each product (shirt, short-sleeved shirt, casual clothes), each a non-negative **integer**.

- **Objective:** Maximize weekly total profit = total selling revenue − total variable costs − fixed equipment costs.
  - Per-unit contribution (selling price − variable cost):
    - Shirt: 120 − 60 = 60
    - Short-sleeve: 80 − 40 = 40
    - Casual cloth: 180 − 80 = 100
  - Fixed equipment costs are paid every week regardless of usage: 2000 (shirt) + 1500 (short-sleeve) + 1000 (casual) = 4500 total.

- **Constraints:**
  - Labor: 3·(shirts) + 2·(short-sleeves) + 6·(casual) ≤ 1500
  - Material: 4·(shirts) + 3·(short-sleeves) + 6·(casual) ≤ 1600
  - Non-negativity and integrality: all production quantities ≥ 0 and integer.

- **No** minimum/maximum production bounds beyond non-negativity.

This is a small integer linear program with three variables and two resource constraints.