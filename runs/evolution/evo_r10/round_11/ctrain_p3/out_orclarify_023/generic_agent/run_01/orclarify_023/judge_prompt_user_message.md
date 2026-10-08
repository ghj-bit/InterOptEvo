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

QUESTION: Are the weekly fixed costs of 2000, 1500, and 1000 incurred only when the corresponding equipment is actually used to produce a positive quantity of its product, or are they incurred every week regardless of whether that equipment is used?

## Turn 1 - User Simulator

They are incurred only when the corresponding equipment is actually used to produce a positive quantity of its product.

## Turn 2 - Generic Agent

QUESTION: Should the production quantities of shirts, short-sleeved shirts, and casual clothes be whole numbers (integer units), or can they be fractional?

## Turn 2 - User Simulator

The production quantities should be whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: Is there any minimum or maximum production quantity per week for each product, or can any product's weekly production be zero (meaning that equipment is simply not used that week)?

## Turn 3 - User Simulator

There is no minimum or maximum production quantity per week for each product. Any product's weekly production can be zero, meaning that equipment is simply not used that week.

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit, where profit is total revenue minus total variable costs minus the fixed costs of the equipment actually used?

## Turn 4 - User Simulator

Yes, the objective is to maximize total weekly profit, where profit is total revenue minus total variable costs minus the fixed costs of the equipment actually used.

## Turn 5 - Generic Agent

QUESTION: Are the labor and material constraints the only resource limits, or are there any other weekly limits (such as machine hours, storage capacity, or demand caps) that the plan must also respect?

## Turn 5 - User Simulator

The labor and material constraints are the only resource limits. There are no other weekly limits such as machine hours, storage capacity, or demand caps that the plan must respect.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three products, each tied to one dedicated piece of equipment: shirts (equipment 1), short-sleeved shirts (equipment 2), casual clothes (equipment 3). Each equipment can only produce its own product.

- **Decision variables:** Weekly production quantities x1 (shirts), x2 (short-sleeved shirts), x3 (casual clothes), each a non-negative integer. Any can be zero.

- **Objective:** Maximize total weekly profit = total revenue − total variable cost − fixed costs of equipment actually used.
  - Unit contribution: shirt 120−60 = 60; short-sleeve 80−40 = 40; casual 180−80 = 100.
  - Fixed costs (2000, 1500, 1000) are incurred only when the corresponding product's quantity is positive.

- **Constraints:**
  - Labor: 3·x1 + 2·x2 + 6·x3 ≤ 1500.
  - Material: 4·x1 + 3·x2 + 6·x3 ≤ 1600.
  - No other limits (no demand caps, storage, machine hours, or min/max per product).

- **Fixed-cost linkage:** A binary variable per product indicates whether that equipment is used; fixed cost is charged only when the corresponding production quantity is positive (quantity > 0 forces the binary to 1; binary 0 forces quantity to 0).

This is a mixed-integer linear program (MILP) with three integer production variables and three binary usage variables.