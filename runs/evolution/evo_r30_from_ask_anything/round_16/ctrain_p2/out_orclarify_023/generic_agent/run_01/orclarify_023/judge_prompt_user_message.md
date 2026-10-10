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

QUESTION: Should the weekly fixed costs for each equipment be incurred only if that product type is produced (i.e., a fixed charge tied to activating the equipment), or are they incurred every week regardless of whether any units of that product are made

## Turn 1 - User Simulator

The weekly fixed costs are incurred every week regardless of whether any units of that product are made.

## Turn 2 - Generic Agent

QUESTION: Should the production quantities for shirts, short-sleeved shirts, and casual clothes be restricted to whole numbers (integer units), or can they be fractional

## Turn 2 - User Simulator

The production quantities should be restricted to whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: Are there any additional requirements the brief omits, such as minimum production quantities for any product, demand caps on how many units of each product can be sold per week, or any rule linking the production of one product to another

## Turn 3 - User Simulator

There are no additional requirements such as minimum production quantities, demand caps, or rules linking the production of one product to another.

## Turn 4 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- Objective: Maximize weekly net profit (total revenue minus total variable cost minus total fixed cost).
- Decision variables: Weekly production quantity for each of the three products (shirts, short-sleeved shirts, casual clothes).
- Variable domain: Non-negative integers (whole units only).
- Product-to-equipment mapping: Each product is produced exclusively by its dedicated equipment (shirt equipment → shirts, short-sleeve equipment → short-sleeved shirts, casual equipment → casual clothes).
- Labor constraint: Total labor used per week ≤ 1500 units (shirt 3/unit, short-sleeve 2/unit, casual 6/unit).
- Material constraint: Total material used per week ≤ 1600 units (shirt 4/unit, short-sleeve 3/unit, casual 6/unit).
- Fixed costs: Shirt equipment 2000, short-sleeve equipment 1500, casual equipment 1000 — all incurred every week regardless of production volume (confirmed).
- Profit per unit (selling price − variable cost): shirt 60, short-sleeve 40, casual 100.
- No minimum production quantities, no demand caps, and no inter-product linkage rules (confirmed).

Assumptions (none material — all formulation-critical facts were confirmed):
- None. Every slot was confirmed by the client.