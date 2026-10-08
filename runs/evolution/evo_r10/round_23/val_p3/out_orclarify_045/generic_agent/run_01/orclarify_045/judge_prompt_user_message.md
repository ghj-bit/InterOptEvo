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

QUESTION: Is the goal to maximize total profit (in yuan) from the three products, subject to the resource limits and the sales-volume/profit table?

## Turn 1 - User Simulator

Yes.

## Turn 2 - Generic Agent

QUESTION: In the profit table, do the ranges like "0~40" mean the first 40 units of product A earn 10 yuan each and the next units (41~100) earn 9 yuan each, i.e., a tiered/marginal profit that applies only to units within that range?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities of products A, B, and C required to be whole numbers (integer units), or can they be fractional?

## Turn 3 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: For product C, the table shows profit of 5 yuan for the 0~100 range and 4 yuan for "above 100" — does that mean the first 100 units of C earn 5 yuan each and every unit beyond 100 earns 4 yuan each?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: The table gives sales-volume ranges for each product (A up to 150, B up to 100, C above 100) — are these hard upper limits on how many units of each product can be produced, or are they just the ranges over which the tiered profit rates are defined (so production could exceed 150 of A or 100 of B at the last tier's profit)?

## Turn 5 - User Simulator

They are just the ranges over which the tiered profit rates are defined. Production can exceed 150 units of A or 100 units of B, with the last tier's profit rate applying to all units beyond those thresholds.

## Turn 6 - Generic Agent

QUESTION: Are the three resource limits (100 hours technical preparation, 700 hours labor, 400 kg materials) the only constraints, or are there any other limits such as minimum production requirements, demand caps, or per-product maximums I should include?

## Turn 6 - User Simulator

The three resource limits are the only constraints. There are no minimum production requirements, demand caps, or per-product maximums.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total profit (yuan) from producing products A, B, and C.

**Decision variables:** Integer (whole-number) production quantities x_A, x_B, x_C ≥ 0.

**Resource constraints (the only constraints):**
- Technical preparation: 1·x_A + 2·x_B + 1·x_C ≤ 100 hours
- Labor: 10·x_A + 4·x_B + 5·x_C ≤ 700 hours
- Materials: 3·x_A + 2·x_B + 1·x_C ≤ 400 kg

**Tiered (marginal) profit structure** — each unit's profit depends on which tier it falls into, and tiers apply cumulatively:
- Product A: first 40 units @ 10 yuan, next 60 (41–100) @ 9 yuan, next 50 (101–150) @ 8 yuan, all units beyond 150 @ 7 yuan.
- Product B: first 50 units @ 6 yuan, next 50 (51–100) @ 4 yuan, all units beyond 100 @ 3 yuan.
- Product C: first 100 units @ 5 yuan, all units beyond 100 @ 4 yuan.

The tier ranges are not production caps — production may exceed 150 of A or 100 of B, with the last tier's rate applying to all units beyond the threshold. There are no minimums, demand caps, or per-product maximums.