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

QUESTION: Are the production quantities of products A, B, and C required to be integers (whole units), or can they be treated as continuous values?

## Turn 1 - User Simulator

The production quantities can be treated as continuous values.

## Turn 2 - Generic Agent

QUESTION: In the profit table, the first row for each product (e.g., A: 0~40 at 10 yuan, B: 0~50 at 6 yuan, C: 0~100 at 5 yuan) — does this mean the profit rate applies to ALL units produced within that range (i.e., if you produce 30 units of A, all 30 earn 10 yuan each), or does it mean the profit rate applies only to the units that fall within that specific bracket (i.e., the first 40 units of A earn 10 yuan each, the next 60 earn 9 yuan each, etc.)?

## Turn 2 - User Simulator

The profit rate applies only to the units that fall within that specific bracket. For example, the first 40 units of A earn 10 yuan each, the next 60 earn 9 yuan each, and so on.

## Turn 3 - Generic Agent

QUESTION: For product C, the table shows "0~100" at 5 yuan and "Above 100" at 4 yuan — does this mean the first 100 units of C earn 5 yuan each, and any units beyond 100 earn 4 yuan each?

## Turn 3 - User Simulator

Yes, the first 100 units of C earn 5 yuan each, and any units beyond 100 earn 4 yuan each.

## Turn 4 - Generic Agent

QUESTION: The table lists "Sales Volume" ranges for each product (e.g., A: 0~40, 40~100, 100~150, Above 150). Are these ranges also upper bounds on how many units of each product can be produced (i.e., you cannot produce more than 150 units of A, more than 100 units of B, or more than 100 units of C), or are they purely profit-tier brackets with no hard cap on production?

## Turn 4 - User Simulator

They are purely profit-tier brackets with no hard cap on production.

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize total profit (in yuan) from the three products, subject to the three resource constraints (technical preparation ≤ 100 hours, labor ≤ 700 hours, materials ≤ 400 kg)?

## Turn 5 - User Simulator

Yes, the objective is to maximize total profit (in yuan) from the three products, subject to the three resource constraints: technical preparation ≤ 100 hours, labor ≤ 700 hours, and materials ≤ 400 kg.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:** Continuous production quantities for products A, B, and C (non-negative).

**Objective:** Maximize total profit (in yuan), where profit is piecewise-linear per product based on bracketed tiers:
- Product A: first 40 units at 10 yuan/unit, next 60 units (40–100) at 9 yuan/unit, next 50 units (100–150) at 8 yuan/unit, units above 150 at 7 yuan/unit.
- Product B: first 50 units at 6 yuan/unit, next 50 units (50–100) at 4 yuan/unit, units above 100 at 3 yuan/unit.
- Product C: first 100 units at 5 yuan/unit, units above 100 at 4 yuan/unit.

**Resource constraints:**
- Technical preparation: 1·A + 2·B + 1·C ≤ 100 hours
- Labor: 10·A + 4·B + 5·C ≤ 700 hours
- Materials: 3·A + 2·B + 1·C ≤ 400 kg

**Other notes:**
- No hard upper caps on production quantities (the table ranges are purely profit-tier brackets).
- All quantities are continuous and non-negative.
- The profit tiers apply only to the units falling within each bracket (marginal/bracketed profit, not flat rate).