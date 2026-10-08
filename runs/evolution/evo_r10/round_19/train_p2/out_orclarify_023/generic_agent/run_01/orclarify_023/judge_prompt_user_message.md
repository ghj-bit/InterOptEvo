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

QUESTION: Are there any minimum or maximum production quantity requirements for each product type (e.g., must each product be produced at least some amount, or is there a cap on how many units of each can be made per week)?

## Turn 1 - User Simulator

No. There are no minimum or maximum production quantity requirements for any of the three product types. The only limits are the total weekly labor and material availability, and the fact that each piece of equipment is dedicated to one product.

## Turn 2 - Generic Agent

QUESTION: Are the weekly fixed equipment costs (2000, 1500, 1000) incurred only if that equipment is actually used to produce its product (i.e., if production of that product is greater than zero), or are they paid every week regardless of whether the equipment is used?

## Turn 2 - User Simulator

They are incurred only if the equipment is actually used to produce its product. If production of a product is zero, its associated weekly fixed cost is not incurred.

## Turn 3 - Generic Agent

QUESTION: Should the production quantities of shirts, short-sleeved shirts, and casual clothes be whole numbers (integer units), or can they be fractional?

## Turn 3 - User Simulator

The production quantities should be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit, where profit equals total revenue (selling price × quantity) minus total variable costs (variable cost × quantity) minus the fixed equipment costs for the products actually produced?

## Turn 4 - User Simulator

Yes, that is correct. The objective is to maximize total weekly profit, calculated as total revenue minus total variable costs minus the fixed equipment costs for the products actually produced.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products & equipment:** Three dedicated equipment, one per product: equipment 1 → shirts, equipment 2 → short-sleeved shirts, equipment 3 → casual clothes. Each product can only be made on its own equipment.

- **Decision variables:** Weekly production quantity of each product (x_shirt, x_short, x_casual), each a non-negative integer (whole units). No minimum or maximum per-product quantity limits.

- **Objective:** Maximize total weekly profit = (revenue − variable cost) for each product produced − fixed equipment costs for the products actually produced.
  - Per-unit contribution: shirt 120−60 = 60; short-sleeve 80−40 = 40; casual 180−80 = 100.
  - Fixed costs: shirt equipment 2000, short-sleeve equipment 1500, casual equipment 1000 — each incurred only if that product's production is greater than zero (otherwise not incurred).

- **Resource constraints (weekly totals):**
  - Labor: 3·x_shirt + 2·x_short + 6·x_casual ≤ 1500
  - Material: 4·x_shirt + 3·x_short + 6·x_casual ≤ 1600

- **Fixed-cost linkage:** A binary variable per product indicating whether the equipment is used; fixed cost is charged only when the corresponding production quantity is positive (production > 0 ⇔ equipment used).

- **No other constraints** (no demand caps, no minimums, no carryover/stocking).