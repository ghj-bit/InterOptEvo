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

QUESTION: If a product's weekly production is zero, is its equipment's fixed cost still incurred, or is the fixed cost charged only when that product is actually produced?

## Turn 1 - User Simulator

The fixed cost is charged only when that product is actually produced. If a product's weekly production is zero, its equipment's fixed cost is not incurred.

## Turn 2 - Generic Agent

QUESTION: Are the weekly production quantities of shirts, short-sleeved shirts, and casual clothes required to be whole numbers, or can they be fractional?

## Turn 2 - User Simulator

The weekly production quantities must be whole numbers.

## Turn 3 - Generic Agent

QUESTION: Is there any demand limit or maximum weekly production cap for any of the three products, or can the factory produce as many units as the labor and material constraints allow?

## Turn 3 - User Simulator

There is no demand limit or maximum weekly production cap for any of the three products. The factory can produce as many units as the labor and material constraints allow.

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit, where profit equals total revenue minus total variable costs minus the fixed costs of the equipment that are used?

## Turn 4 - User Simulator

Yes, the objective is to maximize total weekly profit, where profit equals total revenue minus total variable costs minus the fixed costs of the equipment that are used.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment**: Three products — shirts, short-sleeved shirts, casual clothes — each produced on its own dedicated equipment (one product per equipment).
- **Decision variables**: Weekly production quantity of each product, all non-negative integers.
- **Objective**: Maximize total weekly profit = total revenue − total variable costs − fixed costs of equipment that are actually used.
- **Fixed costs**: Shirt equipment 2000, short-sleeved shirt equipment 1500, casual clothes equipment 1000. A fixed cost is incurred only if that product's production is positive; if production is zero, no fixed cost is charged.
- **Resource constraints (per week)**:
  - Labor: 3·(shirts) + 2·(short-sleeves) + 6·(casual) ≤ 1500
  - Material: 4·(shirts) + 3·(short-sleeves) + 6·(casual) ≤ 1600
- **Per-unit economics**:
  - Shirt: labor 3, material 4, price 120, variable cost 60 (unit contribution 60)
  - Short-sleeve: labor 2, material 3, price 80, variable cost 40 (unit contribution 40)
  - Casual: labor 6, material 6, price 180, variable cost 80 (unit contribution 100)
- **No demand limits or production caps** beyond the labor and material constraints.
- **Integrality**: All production quantities must be whole numbers.

This is a mixed-integer program: integer production variables plus binary "equipment used" indicators linking each product's positive production to its fixed cost.