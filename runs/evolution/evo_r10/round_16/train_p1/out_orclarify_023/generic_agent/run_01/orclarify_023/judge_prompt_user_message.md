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

QUESTION: Are there any minimum or maximum production quantity requirements for each product type (e.g., must we produce at least some units of each, or is there a cap on how many of any one product we can make per week)?

## Turn 1 - User Simulator

No. There are no minimum or maximum production quantity requirements for any of the three product types. We can produce zero units of a product, and there is no cap on how many units of any single product we can make in a week, aside from the overall labor and material limits.

## Turn 2 - Generic Agent

QUESTION: If we choose to produce zero units of a product, do we still have to pay that product's equipment fixed cost for the week, or is the fixed cost incurred only when we actually produce at least one unit of that product?

## Turn 2 - User Simulator

The fixed cost is incurred only when we actually produce at least one unit of that product. If we produce zero units, we do not pay that equipment's fixed cost for the week.

## Turn 3 - Generic Agent

QUESTION: Should the weekly production quantities be whole numbers (integer units), or is it acceptable to plan fractional units of a product?

## Turn 3 - User Simulator

The weekly production quantities should be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit, where profit is calculated as total revenue minus total variable costs minus the fixed costs of the equipment actually used?

## Turn 4 - User Simulator

Yes, that is correct. The objective is to maximize total weekly profit, calculated as total revenue minus total variable costs minus the fixed costs of the equipment actually used.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Weekly production planning for Hongdou Clothing Factory.

**Products and equipment:** Three dedicated pieces of equipment, one per product type:
- Equipment 1 → Shirts
- Equipment 2 → Short-sleeved shirts
- Equipment 3 → Casual clothes

**Decision variables:** Weekly production quantity of each product (integer, non-negative, no upper or lower bounds other than 0).

**Objective:** Maximize total weekly profit = total revenue − total variable costs − fixed costs of equipment actually used.

Per-unit economics:
| Product | Labor/unit | Material/unit | Price | Variable cost | Unit contribution |
|---|---|---|---|---|---|
| Shirt | 3 | 4 | 120 | 60 | 60 |
| Short-sleeve | 2 | 3 | 80 | 40 | 40 |
| Casual cloth | 6 | 6 | 180 | 80 | 100 |

**Fixed costs (incurred only if at least one unit of that product is produced):**
- Shirt equipment: 2000
- Short-sleeve equipment: 1500
- Casual clothes equipment: 1000

**Resource constraints (per week):**
- Total labor ≤ 1500 units
- Total material ≤ 1600 units

**Other confirmed facts:**
- No minimum or maximum production quantity per product (zero is allowed).
- Production quantities must be whole numbers (integer).
- Fixed cost is paid only when production of that product is positive (otherwise zero).

This is a mixed-integer linear program: three integer production variables, three binary "equipment used" variables linking each product's positive production to its fixed cost, two resource constraints, and a profit-maximizing objective.