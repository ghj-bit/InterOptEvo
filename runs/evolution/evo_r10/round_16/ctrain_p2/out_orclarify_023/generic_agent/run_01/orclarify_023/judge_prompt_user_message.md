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

QUESTION: Are the weekly fixed costs (2000, 1500, 1000) incurred only when the corresponding equipment is actually used to produce a positive quantity of its product, or are they paid every week regardless of whether that product is produced?

## Turn 1 - User Simulator

The weekly fixed costs are incurred only when the corresponding equipment is actually used to produce a positive quantity of its product.

## Turn 2 - Generic Agent

QUESTION: Is there a minimum production quantity that must be met once a piece of equipment is turned on, or can any positive quantity (even 1 unit) be produced once the equipment is used?

## Turn 2 - User Simulator

There is no minimum production quantity. Once a piece of equipment is used, any positive quantity can be produced.

## Turn 3 - Generic Agent

QUESTION: Should the production quantities of shirts, short-sleeved shirts, and casual clothes be whole numbers (you can't produce a fraction of a garment), or is it acceptable to treat them as continuous values?

## Turn 3 - User Simulator

The production quantities should be whole numbers.

## Turn 4 - Generic Agent

QUESTION: Is there any demand limit or maximum number of units that can be sold for each product per week, or can the factory produce and sell unlimited quantities of each product as long as labor and material constraints are satisfied?

## Turn 4 - User Simulator

There is no demand limit or maximum number of units that can be sold for each product per week. The factory can produce and sell unlimited quantities of each product as long as the labor and material constraints are satisfied.

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize total weekly profit, where profit equals total revenue minus total variable costs minus the fixed costs of the equipment actually used?

## Turn 5 - User Simulator

Yes, the objective is to maximize total weekly profit, where profit equals total revenue minus total variable costs minus the fixed costs of the equipment actually used.

## Turn 6 - Generic Agent

QUESTION: Are the labor and material constraints the only resource limits, or are there any other constraints (such as machine capacity in units per week, storage limits, or minimum production requirements) that I should include in the model?

## Turn 6 - User Simulator

The labor and material constraints are the only resource limits. There are no other constraints such as machine capacity in units per week, storage limits, or minimum production requirements.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Weekly production planning for Hongdou Clothing Factory.

**Products and equipment:**
- Equipment 1 → Shirts (dedicated)
- Equipment 2 → Short-sleeved shirts (dedicated)
- Equipment 3 → Casual clothes (dedicated)

**Decision variables:**
- x₁ = number of shirts produced (non-negative integer)
- x₂ = number of short-sleeved shirts produced (non-negative integer)
- x₃ = number of casual clothes produced (non-negative integer)
- y₁, y₂, y₃ = binary variables indicating whether each equipment is used (1 if xᵢ > 0, 0 otherwise)

**Objective:** Maximize total weekly profit
= (120 − 60)x₁ + (80 − 40)x₂ + (180 − 80)x₃ − 2000·y₁ − 1500·y₂ − 1000·y₃
= 60x₁ + 40x₂ + 100x₃ − 2000y₁ − 1500y₂ − 1000y₃

**Constraints:**
1. Labor: 3x₁ + 2x₂ + 6x₃ ≤ 1500
2. Material: 4x₁ + 3x₂ + 6x₃ ≤ 1600
3. Linking (equipment used only if producing): x₁ ≤ M·y₁, x₂ ≤ M·y₂, x₃ ≤ M·y₃ (where M is a sufficiently large upper bound, e.g., derived from labor/material limits)
4. Integrality: x₁, x₂, x₃ are non-negative integers; y₁, y₂, y₃ are binary.

**No other constraints** (no demand caps, no machine capacity limits, no minimum production, no storage limits).