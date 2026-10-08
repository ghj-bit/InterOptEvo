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

QUESTION: For the tiered profit table, is the profit rate (yuan per unit) applied only to the units within that tier's range (e.g., the first 40 units of A earn 10 yuan each, units 41–100 earn 9 yuan each, etc.), or is a single rate applied to all units of a product based on its total production level (e.g., if 60 units of A are produced, all 60 earn 9 yuan each)?

## Turn 1 - User Simulator

The profit rate is applied only to the units within that tier's range. For example, the first 40 units of Product A earn 10 yuan each, units 41–100 earn 9 yuan each, and so on.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities of products A, B, and C required to be whole numbers (integer units), or can they be fractional?

## Turn 2 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: The tier boundaries in the table (e.g., "0~40", "40~100") overlap at the boundary values — for example, does the 40th unit of Product A earn 10 yuan (belonging to the first tier) or 9 yuan (belonging to the second tier)?

## Turn 3 - User Simulator

The 40th unit of Product A earns 10 yuan, belonging to the first tier.

## Turn 4 - Generic Agent

QUESTION: The table lists "Sales Volume" ranges for each product (A: 0~150+, B: 0~100+, C: 0~100+) — are these hard upper limits on how many units of each product can be produced, or are they merely the ranges over which the tiered profit rates are defined (meaning production could exceed 150 for A, 100 for B, or 100 for C, with the last tier's rate applying to all units beyond)?

## Turn 4 - User Simulator

They are merely the ranges over which the tiered profit rates are defined. Production could exceed 150 for A, 100 for B, or 100 for C, with the last tier's rate applying to all units beyond.

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize total profit (sum of tiered profits across all three products), or is there another objective such as maximizing total units produced or minimizing cost?

## Turn 5 - User Simulator

The objective is to maximize total profit, which is the sum of the tiered profits across all three products.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem type:** Integer linear programming (ILP) — maximize total profit.

**Decision variables:** Production quantities of products A, B, C, all non-negative integers.

**Objective:** Maximize total profit, where profit is tiered (marginal) per product:
- Product A: first 40 units earn 10 yuan each; units 41–100 earn 9 yuan each; units 101–150 earn 8 yuan each; units above 150 earn 7 yuan each.
- Product B: first 50 units earn 6 yuan each; units 51–100 earn 4 yuan each; units above 100 earn 3 yuan each.
- Product C: first 100 units earn 5 yuan each; units above 100 earn 4 yuan each.

The tier boundaries are inclusive of the lower endpoint of the next tier (i.e., the 40th unit of A earns 10 yuan, the 41st earns 9 yuan). Production is not capped at the last listed boundary; the final tier's rate applies to all units beyond.

**Constraints (resource limits):**
- Technical preparation: 1·A + 2·B + 1·C ≤ 100 hours
- Labor: 10·A + 4·B + 5·C ≤ 700 hours
- Materials: 3·A + 2·B + 1·C ≤ 400 kg

**Integrality:** All production quantities must be whole numbers (non-negative integers).

**Modeling approach:** Introduce auxiliary variables to represent the number of units produced in each tier for each product, with ordering constraints ensuring lower tiers are filled before higher tiers. The objective sums (tier quantity × tier rate) across all tiers and products.