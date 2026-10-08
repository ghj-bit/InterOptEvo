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

QUESTION: Should the weekly production quantities of shirts, short-sleeved shirts, and casual clothes be required to be whole numbers (integer units), or can they be treated as continuous (fractional) values in the plan?

## Turn 1 - User Simulator

They should be whole numbers. We produce individual garments, so fractional units don’t make sense for the weekly plan.

## Turn 2 - Generic Agent

QUESTION: If a product's planned weekly quantity is zero, is that product's equipment fixed cost (2000 / 1500 / 1000) still incurred, or is the fixed cost charged only when that product is actually produced (quantity greater than zero)?

## Turn 2 - User Simulator

The fixed cost is charged only when that product is actually produced (quantity greater than zero).

## Turn 3 - Generic Agent

QUESTION: Are there any minimum or maximum weekly production requirements for each product (for example, a minimum order to keep an equipment running, or a maximum demand cap), or is the only limit on each product the shared labor and material availability?

## Turn 3 - User Simulator

There are no minimum or maximum weekly production requirements for each product. The only limits are the shared labor and material availability.

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize the total weekly profit, where profit is calculated as total revenue (selling price times quantity) minus total variable costs (variable cost times quantity) minus the fixed costs of the equipment that are actually used?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: Are there any other costs, constraints, or business rules (such as demand limits, labor/material carryover, or equipment capacity caps) that I should include, or are the labor cap (1500), material cap (1600), integer production quantities, and conditional fixed costs the complete set of considerations?

## Turn 5 - User Simulator

No, there are no other costs, constraints, or business rules. The labor cap (1500), material cap (1600), integer production quantities, and conditional fixed costs are the complete set of considerations.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three products, each made on its own dedicated equipment: shirts (equipment 1), short-sleeved shirts (equipment 2), casual clothes (equipment 3).
- **Decision variables:** Weekly production quantity of each product, required to be non-negative integers (whole garments).
- **Objective:** Maximize total weekly profit = total revenue (selling price × quantity) − total variable cost (variable cost × quantity) − fixed costs of the equipment that are actually used.
- **Per-unit data:**
  - Shirt: labor 3, material 4, price 120, variable cost 60 (unit contribution 60).
  - Short-sleeve: labor 2, material 3, price 80, variable cost 40 (unit contribution 40).
  - Casual cloth: labor 6, material 6, price 180, variable cost 80 (unit contribution 100).
- **Resource constraints (weekly):**
  - Total labor ≤ 1500.
  - Total material ≤ 1600.
- **Fixed costs (conditional):** Shirt equipment 2000, short-sleeve equipment 1500, casual equipment 1000 — each charged only if that product's quantity is greater than zero (i.e., the equipment is used).
- **No other constraints:** No minimum/maximum production per product, no demand caps, no carryover, no equipment capacity caps, no other costs or business rules.

This is a mixed-integer linear program: integer production quantities plus binary "equipment used" indicators linking each fixed cost to whether its product quantity is positive.