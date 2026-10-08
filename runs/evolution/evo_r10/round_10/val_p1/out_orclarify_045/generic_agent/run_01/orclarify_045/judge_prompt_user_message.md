# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U2, U3
I need help creating a production plan for a factory producing three types of products, where total technical preparation time used must not exceed 100 hours, total labor time used must not exceed 700 hours, and total materials used must not exceed 400 kg.

Each unit of product A requires 1 hour for technical preparation, 10 hours of direct labor, and 3 kg of materials. Each unit of product B requires 2 hours for technical preparation, 4 hours of labor, and 2 kg of materials. Each unit of product C requires 1 hour for technical preparation, 5 hours of labor, and 1 kg of materials. The available technical preparation time is 100 hours, labor time is 700 hours, and materials are 400 kg.

Table 1-22
| Product A       |           | Product B       |           | Product C       |           |
|:---------------|:---------:|:---------------|:---------:|:---------------|:---------:|
| Sales Volume (pieces) | Profit (yuan) | Sales Volume (pieces) | Profit (yuan) | Sales Volume (pieces) | Profit (yuan) |
| 0 ~ 40         | 10        | 0 ~ 50         | 6         | 0 ~ 100        | 5         |
| 40 ~ 100       | 9         | 50 ~ 100       | 4         | Above 100      | 4         |
| 100 ~ 150      | 8         | Above 100      | 3         |                |           |
| Above 150      | 7         |                |           |                |           |

## Problem units
- U1 (context): I need help creating a production plan for a factory producing three types of products.
- U2 (data): Each unit of product A requires 1 hour for technical preparation, 10 hours of direct labor, and 3 kg of materials. Each unit of product B requires 2 hours for technical preparation, 4 hours of labor, and 2 kg of materials. Each unit of product C requires 1 hour for technical preparation, 5 hours of labor, and 1 kg of materials. The available technical preparation time is 100 hours, labor time is 700 hours, and materials are 400 kg.
- U3 (data): Table 1-22
| Product A       |           | Product B       |           | Product C       |           |
|:---------------|:---------:|:---------------|:---------:|:---------------|:---------:|
| Sales Volume (pieces) | Profit (yuan) | Sales Volume (pieces) | Profit (yuan) | Sales Volume (pieces) | Profit (yuan) |
| 0 ~ 40         | 10        | 0 ~ 50         | 6         | 0 ~ 100        | 5         |
| 40 ~ 100       | 9         | 50 ~ 100       | 4         | Above 100      | 4         |
| 100 ~ 150      | 8         | Above 100      | 3         |                |           |
| Above 150      | 7         |                |           |                |           |
- U4 (objective): Maximize profit.
- U5 (constraint): Total technical preparation time used must not exceed 100 hours.
- U6 (constraint): Total labor time used must not exceed 700 hours.
- U7 (constraint): Total materials used must not exceed 400 kg.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without knowing the objective, the modeling agent cannot formulate any optimization model. Any assumed objective (e.g., minimize cost) would be completely arbitrary and almost certainly wrong. This is a must-clarify fatal gap.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must explicitly ask what the objective of the optimization is, or directly inquire whether to maximize profit (as opposed to any other default objective).
- Reference acceptable questions:
  - What is the objective of the production plan? Should we aim to maximize profit?
  - Are we trying to maximize total profit, or is there another target like minimizing costs or maximizing revenue?
- Failure modes:
  - Silently assuming the objective is to minimize total cost
  - Assuming the objective is to maximize total revenue
  - Assuming a multi-objective or unspecified goal without clarification


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: For the tiered profit table, is the profit rate (yuan per unit) applied to every unit produced within that tier (e.g., all 100 units of A get the tiered rates: 10 yuan for the first 40, 9 yuan for units 41–100), or is the rate applied only to the units that fall into each tier?

## Turn 1 - User Simulator

The rate is applied only to the units that fall into each tier. For example, if 100 units of Product A are produced, the first 40 units earn 10 yuan each, and units 41 through 100 earn 9 yuan each.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities for products A, B, and C required to be whole numbers (integer units), or can they be fractional?

## Turn 2 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: The table lists "Sales Volume" ranges (e.g., A: 0~40, 40~100, etc.) — are these upper limits on how many units of each product can be sold (i.e., production cannot exceed these caps), or are they just the ranges over which the profit rate changes with no hard cap on production?

## Turn 3 - User Simulator

They are just the ranges over which the profit rate changes. There is no hard cap on production based on these sales volume ranges.

## Turn 4 - Generic Agent

QUESTION: For the tier boundaries, when a product's quantity lands exactly on a boundary (e.g., exactly 40 units of A, or exactly 100 units of C), does that unit count toward the lower tier or the upper tier? For instance, is the 40th unit of A paid at 10 yuan or at 9 yuan?

## Turn 4 - User Simulator

The 40th unit of A is paid at 10 yuan. The lower tier includes the boundary value.

## Turn 5 - Generic Agent

QUESTION: The three resource limits (100 hours technical prep, 700 hours labor, 400 kg materials) — are these hard upper bounds that must not be exceeded, with any unused capacity simply wasted (no penalty, no requirement to use it all)?

## Turn 5 - User Simulator

Yes, they are hard upper bounds that must not be exceeded. Any unused capacity is simply wasted with no penalty and no requirement to use it all.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize total profit (sum of the tiered revenues across all three products), with no other costs (such as fixed setup costs or per-unit production costs) to subtract?

## Turn 6 - User Simulator

Yes, the objective is to maximize total profit, which is the sum of the tiered revenues across all three products. There are no other costs to subtract.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Production planning for a factory making three products (A, B, C) to maximize total profit.

**Decision variables:** Integer (whole-number) production quantities x_A, x_B, x_C ≥ 0. No upper cap from the sales-volume ranges.

**Resource constraints (hard upper bounds, unused capacity is free/wasted):**
- Technical preparation: 1·x_A + 2·x_B + 1·x_C ≤ 100 hours
- Direct labor: 10·x_A + 4·x_B + 5·x_C ≤ 700 hours
- Materials: 3·x_A + 2·x_B + 1·x_C ≤ 400 kg

**Objective:** Maximize total profit = sum of tiered revenues over all three products. No other costs.

**Tiered profit (yuan per unit), applied only to the units falling in each tier; the lower tier includes the boundary value:**
- Product A: units 1–40 @ 10; units 41–100 @ 9; units 101–150 @ 8; units 151+ @ 7
- Product B: units 1–50 @ 6; units 51–100 @ 4; units 101+ @ 3
- Product C: units 1–100 @ 5; units 101+ @ 4

**Modeling note:** Because profit is piecewise-linear and concave (rates decrease with quantity), this can be modeled with a standard incremental (split-variable) formulation: for each product, create one integer variable per tier with an upper bound equal to the tier width (the last tier unbounded), each carrying that tier's rate, and the product's total quantity is the sum of its tier variables. The resource constraints then apply to the summed quantities. This is exact for concave piecewise-linear revenue with integer quantities.