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

QUESTION: Are the weekly fixed costs (2000 / 1500 / 1000) incurred only when the corresponding equipment is actually used to produce a positive quantity of its product, or are they paid every week regardless of whether that product is produced at all?

## Turn 1 - User Simulator

They are incurred only when the corresponding equipment is actually used to produce a positive quantity of its product.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units of each product can be sold per week (e.g., a maximum demand or market cap for shirts, short-sleeved shirts, or casual clothes), or can the factory sell whatever quantity it produces?

## Turn 2 - User Simulator

There is no limit on how many units of each product can be sold per week. The factory can sell whatever quantity it produces.

## Turn 3 - Generic Agent

QUESTION: Should the production quantities of shirts, short-sleeved shirts, and casual clothes be whole numbers (you can only produce complete garments), or is it acceptable to treat them as continuous values (e.g., 123.5 units) for planning purposes?

## Turn 3 - User Simulator

The production quantities should be whole numbers, since you can only produce complete garments.

## Turn 4 - Generic Agent

QUESTION: Is the goal to maximize the weekly total profit (total revenue minus total variable costs minus the fixed costs of the equipment actually used), or is there some other objective you want to optimize?

## Turn 4 - User Simulator

The goal is to maximize the weekly total profit, which is total revenue minus total variable costs minus the fixed costs of the equipment actually used.

## Turn 5 - Generic Agent

QUESTION: If a product's profit contribution per unit is positive but producing it would require paying its equipment's fixed cost, is it acceptable for the plan to produce zero of that product (and thus avoid its fixed cost), or must each of the three products be produced at least one unit every week?

## Turn 5 - User Simulator

It is acceptable for the plan to produce zero of a product and thus avoid its fixed cost. There is no requirement that each of the three products must be produced at least one unit every week.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products & equipment:** Three dedicated pieces of equipment, one per product: equipment 1 → shirts, equipment 2 → short-sleeved shirts, equipment 3 → casual clothes. Each product can only be made on its own equipment.

- **Decision variables:** Weekly production quantity of each product (shirt, short-sleeve, casual cloth), each a non-negative **integer** (whole garments only).

- **Objective:** Maximize weekly total profit = total revenue (selling price × quantity) − total variable cost (variable cost × quantity) − fixed costs of the equipment actually used.
  - Per-unit profit contributions: shirt 120−60 = 60; short-sleeve 80−40 = 40; casual 180−80 = 100.

- **Fixed costs (conditional):** Shirt equipment 2000, short-sleeve equipment 1500, casual equipment 1000. Each is incurred **only if** that product's production quantity is positive; if a product is produced at zero, its fixed cost is avoided. Producing zero of any product is allowed (no minimum production requirement).

- **Resource constraints (per week):**
  - Labor: 3·(shirts) + 2·(short-sleeves) + 6·(casual) ≤ 1500
  - Material: 4·(shirts) + 3·(short-sleeves) + 6·(casual) ≤ 1600

- **No demand caps:** The factory can sell whatever it produces; there is no upper bound on sales/production from the market side.

- **Horizon:** Single week (all quantities and costs are weekly).

This is a fixed-charge (semi-continuous) integer program: each product's quantity is either zero (no fixed cost) or a positive integer (fixed cost paid), subject to the two shared resource limits.