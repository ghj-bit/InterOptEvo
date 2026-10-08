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

QUESTION: Are the weekly fixed costs of 2000, 1500, and 1000 incurred only when the corresponding equipment is actually used (i.e., when production of that product is positive), or are they paid every week regardless of whether the equipment runs?

## Turn 1 - User Simulator

They are paid every week regardless of whether the equipment runs.

## Turn 2 - Generic Agent

QUESTION: Should the production quantities of shirts, short-sleeved shirts, and casual clothes be whole numbers (you can't produce half a shirt), or is it fine to treat them as continuous values?

## Turn 2 - User Simulator

The production quantities should be whole numbers.

## Turn 3 - Generic Agent

QUESTION: Is the goal to maximize the weekly profit (total revenue minus variable costs, with the fixed equipment costs being constant), or is there some other objective such as maximizing total revenue or minimizing cost?

## Turn 3 - User Simulator

The goal is to maximize the weekly profit.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how many units of each product can be produced per week (for example, a maximum demand or a capacity ceiling per equipment), or are the only limits the 1500 labor units and 1600 material units?

## Turn 4 - User Simulator

The only limits are the 1500 labor units and 1600 material units.

## Turn 5 - Generic Agent

QUESTION: For the weekly profit, should it be calculated as (selling price − variable cost) per unit times quantity, with the fixed equipment costs subtracted as a constant, or should the fixed equipment costs be treated as part of the profit calculation in some other way?

## Turn 5 - User Simulator

Weekly profit is calculated as (selling price − variable cost) per unit times quantity, with the fixed equipment costs subtracted as a constant.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products and equipment:** Three products, each made on its own dedicated equipment: shirts (equipment 1), short-sleeved shirts (equipment 2), casual clothes (equipment 3).
- **Decision variables:** Weekly production quantities of shirts, short-sleeved shirts, and casual clothes, each a non-negative whole number.
- **Objective:** Maximize weekly profit = (selling price − variable cost) per unit × quantity for each product, minus the constant weekly fixed equipment costs (2000 + 1500 + 1000 = 4500). Since the fixed costs are paid regardless of production, they are a constant offset.
  - Shirt contribution: 120 − 60 = 60 per unit
  - Short-sleeve contribution: 80 − 40 = 40 per unit
  - Casual cloth contribution: 180 − 80 = 100 per unit
- **Constraints:**
  - Labor: 3·(shirts) + 2·(short-sleeves) + 6·(casual) ≤ 1500
  - Material: 4·(shirts) + 3·(short-sleeves) + 6·(casual) ≤ 1600
- **No other limits:** No per-product demand caps or equipment capacity ceilings beyond the labor and material constraints.
- **Fixed costs:** Paid every week regardless of whether equipment runs, so they do not affect the optimization choice, only the final profit figure.