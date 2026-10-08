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

QUESTION: Should the weekly production quantities of shirts, short-sleeved shirts, and casual clothes be required to be whole numbers (integer units), or is it acceptable for the plan to use fractional units?

## Turn 1 - User Simulator

The weekly production quantities should be whole numbers (integer units). We cannot produce a fraction of a shirt, short-sleeved shirt, or casual clothes.

## Turn 2 - Generic Agent

QUESTION: Are the weekly fixed costs of 2000, 1500, and 1000 incurred only when the corresponding equipment is actually used (i.e., when production of that product is greater than zero), or are they incurred every week regardless of whether the equipment is used?

## Turn 2 - User Simulator

The weekly fixed costs are incurred only when the corresponding equipment is actually used (i.e., when production of that product is greater than zero).

## Turn 3 - Generic Agent

QUESTION: Is the objective to maximize the total weekly profit, where profit is calculated as total revenue (selling price times quantity) minus total variable costs minus the fixed costs of the equipment that are used?

## Turn 3 - User Simulator

Yes, the objective is to maximize the total weekly profit, where profit is calculated as total revenue (selling price times quantity) minus total variable costs minus the fixed costs of the equipment that are used.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum production requirements for each product type, or is it acceptable for the factory to produce zero units of any product in a given week?

## Turn 4 - User Simulator

There are no minimum production requirements. It is acceptable for the factory to produce zero units of any product in a given week.

## Turn 5 - Generic Agent

QUESTION: Are there any maximum production limits (upper bounds) for each product type per week, or are the only constraints the total labor (1500) and total material (1600) availability?

## Turn 5 - User Simulator

There are no maximum production limits for each product type. The only constraints are the total labor (1500) and total material (1600) availability.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three products, each tied to one dedicated piece of equipment: shirts (equipment 1), short-sleeved shirts (equipment 2), casual clothes (equipment 3).
- **Decision variables:** Weekly production quantities for each product, required to be non-negative integers (whole units). Zero production of any product is allowed.
- **Objective:** Maximize total weekly profit = total revenue (selling price × quantity) − total variable costs (variable cost × quantity) − fixed costs of equipment that are actually used.
- **Fixed costs:** Shirt equipment 2000, short-sleeve equipment 1500, casual clothes equipment 1000. Each is incurred only if the corresponding product's production is greater than zero (otherwise 0).
- **Resource constraints (per week):**
  - Labor: 3·(shirts) + 2·(short-sleeves) + 6·(casual) ≤ 1500
  - Material: 4·(shirts) + 3·(short-sleeves) + 6·(casual) ≤ 1600
- **No other constraints:** No minimum production requirements and no per-product maximum production limits.
- **Unit economics:**
  - Shirt: labor 3, material 4, price 120, variable cost 60 (unit contribution 60)
  - Short-sleeve: labor 2, material 3, price 80, variable cost 40 (unit contribution 40)
  - Casual: labor 6, material 6, price 180, variable cost 80 (unit contribution 100)

This is a mixed-integer linear program: integer production quantities coupled with binary "equipment used" indicators that gate the fixed costs.