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

QUESTION: Is the goal to maximize total profit (in yuan) from the three products, subject to the stated resource limits and the sales-volume-dependent profit rates?

## Turn 1 - User Simulator

Yes.

## Turn 2 - Generic Agent

QUESTION: For the sales-volume brackets, do the profit rates apply to every unit produced within that bracket (e.g., all 100 units of A get the rate of their bracket), or only to the units that fall within each bracket (e.g., the first 40 units of A earn 10 yuan each, the next 60 earn 9 yuan each, etc.)?

## Turn 2 - User Simulator

The profit rates apply only to the units that fall within each bracket. For example, the first 40 units of A earn 10 yuan each, the next 60 earn 9 yuan each, and so on.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities of products A, B, and C required to be whole numbers (integer units), or can they be fractional?

## Turn 3 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 4 - Generic Agent

QUESTION: The table lists sales-volume brackets for each product (e.g., A up to 150, B up to 100, C above 100). Are these brackets meant to be hard upper limits on how many units of each product can be produced, or are they just the ranges over which the profit rates change, with no cap on total production beyond the resource limits?

## Turn 4 - User Simulator

They are just the ranges over which the profit rates change, with no cap on total production beyond the resource limits.

## Turn 5 - Generic Agent

QUESTION: For product C, the table shows a profit of 5 yuan for units 0–100 and 4 yuan for units above 100. Does the 4-yuan rate continue for all units beyond 100 (with no further brackets), or are there additional lower rates for higher quantities?

## Turn 5 - User Simulator

The 4-yuan rate continues for all units beyond 100, with no further brackets.

## Turn 6 - Generic Agent

QUESTION: For product A, the table shows brackets up to "above 150" at 7 yuan. Does the 7-yuan rate continue for all units beyond 150 (with no further brackets), or are there additional lower rates for higher quantities?

## Turn 6 - User Simulator

The 7-yuan rate continues for all units beyond 150, with no further brackets.

## Turn 7 - Generic Agent

QUESTION: For product B, the table shows brackets up to "above 100" at 3 yuan. Does the 3-yuan rate continue for all units beyond 100 (with no further brackets), or are there additional lower rates for higher quantities?

## Turn 7 - User Simulator

The 3-yuan rate continues for all units beyond 100, with no further brackets.

## Turn 8 - Generic Agent

QUESTION: The resource limits (100 hours technical prep, 700 hours labor, 400 kg materials) — are these strict upper bounds that must not be exceeded, with any unused capacity simply left idle (no penalty, no requirement to use it all)?

## Turn 8 - User Simulator

Yes, they are strict upper bounds that must not be exceeded, with any unused capacity simply left idle.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total profit (in yuan) from producing products A, B, and C.

**Decision variables:** Whole-number (integer, non-negative) units of A, B, and C to produce.

**Profit structure (marginal, per-unit, by bracket):**
- Product A: first 40 units earn 10 yuan each; units 41–100 earn 9 yuan each; units 101–150 earn 8 yuan each; units above 150 earn 7 yuan each (continues indefinitely).
- Product B: first 50 units earn 6 yuan each; units 51–100 earn 4 yuan each; units above 100 earn 3 yuan each (continues indefinitely).
- Product C: first 100 units earn 5 yuan each; units above 100 earn 4 yuan each (continues indefinitely).

The brackets are only the ranges over which the profit rate changes — they are NOT caps on production. Production is limited only by the resource constraints.

**Resource constraints (strict upper bounds, unused capacity left idle with no penalty):**
- Technical preparation: 1 hr/unit A, 2 hr/unit B, 1 hr/unit C → total ≤ 100 hours.
- Labor: 10 hr/unit A, 4 hr/unit B, 5 hr/unit C → total ≤ 700 hours.
- Materials: 3 kg/unit A, 2 kg/unit B, 1 kg/unit C → total ≤ 400 kg.

**Modeling approach:** Because profit is piecewise-linear (marginal) in each product's quantity, I will split each product's production into bracket sub-variables (e.g., A1 ≤ 40 at 10 yuan, A2 ≤ 60 at 9 yuan, A3 ≤ 50 at 8 yuan, A4 ≥ 0 at 7 yuan), with the constraint that a higher bracket can only be used if all lower brackets are filled (standard piecewise-linear formulation). All variables are non-negative integers. The three resource constraints apply to the sum of the sub-variables.