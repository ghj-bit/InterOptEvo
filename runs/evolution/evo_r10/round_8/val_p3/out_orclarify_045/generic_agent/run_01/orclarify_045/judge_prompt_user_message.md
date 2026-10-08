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

QUESTION: For the profit tiers in Table 1-22, is the profit value the per-unit profit that applies to every unit produced within that tier (e.g., the first 40 units of A each earn 10 yuan, units 41–100 each earn 9 yuan, etc.), or is it a total profit for the whole tier?

## Turn 1 - User Simulator

It is the per-unit profit that applies to every unit produced within that tier.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities of products A, B, and C required to be whole numbers (integer units), or can they be fractional?

## Turn 2 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 3 - Generic Agent

QUESTION: The table lists "Sales Volume" ranges (e.g., 0~40, 40~100) for each product. Should I treat these as upper bounds on how many units of each product can be produced (i.e., production cannot exceed the sales volume), or are they just describing the profit tiers with no actual production cap?

## Turn 3 - User Simulator

They are just describing the profit tiers with no actual production cap.

## Turn 4 - Generic Agent

QUESTION: For the profit tier boundaries, is the boundary value included in the lower tier or the upper tier? For example, is the 40th unit of product A earning 10 yuan (the 0~40 tier) or 9 yuan (the 40~100 tier)?

## Turn 4 - User Simulator

The 40th unit of product A earns 10 yuan.

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize total profit, and is there any other goal or constraint (such as meeting a minimum production level, minimizing cost, or a secondary tie-breaker) besides the three resource limits?

## Turn 5 - User Simulator

The objective is to maximize total profit. There are no other goals or constraints besides the three resource limits.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Production planning for a factory producing three products (A, B, C).

**Decision variables:** x_A, x_B, x_C — integer (whole-number) units produced of each product, each ≥ 0.

**Objective:** Maximize total profit.

**Profit structure (per-unit, tiered, marginal):**
- Product A: units 1–40 earn 10 yuan each; units 41–100 earn 9 yuan each; units 101–150 earn 8 yuan each; units 151+ earn 7 yuan each.
- Product B: units 1–50 earn 6 yuan each; units 51–100 earn 4 yuan each; units 101+ earn 3 yuan each.
- Product C: units 1–100 earn 5 yuan each; units 101+ earn 4 yuan each.
- Boundary convention: the boundary value belongs to the lower tier (e.g., the 40th unit of A earns 10 yuan).

**Resource constraints:**
- Technical preparation: 1·x_A + 2·x_B + 1·x_C ≤ 100 hours
- Labor: 10·x_A + 4·x_B + 5·x_C ≤ 700 hours
- Materials: 3·x_A + 2·x_B + 1·x_C ≤ 400 kg

**No other constraints:** No production caps beyond the resource limits, no minimum production requirements, no secondary objectives or tie-breakers.

**Formulation approach:** Introduce tier-split variables (e.g., x_A1 for units 1–40, x_A2 for units 41–100, etc.) with linking constraints to enforce the sequential filling of tiers, then maximize the linear profit expression subject to the three resource constraints and integrality.