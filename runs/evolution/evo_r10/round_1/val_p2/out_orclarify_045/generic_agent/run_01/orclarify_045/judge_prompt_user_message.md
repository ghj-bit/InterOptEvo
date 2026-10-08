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

QUESTION: Is the objective to maximize total profit (sum of per-unit profit times units produced for each product), with the per-unit profit determined by the tiered sales-volume table (i.e., the first 40 units of A earn 10 yuan each, the next 60 earn 9, the next 50 earn 8, and any beyond 150 earn 7, and similarly for B and C)?

## Turn 1 - User Simulator

Yes, that is correct.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities of products A, B, and C required to be integers (whole units), or can they be treated as continuous values?

## Turn 2 - User Simulator

The production quantities must be integers (whole units).

## Turn 3 - Generic Agent

QUESTION: In the tiered profit table, are the upper bounds of each tier (e.g., 40, 100, 150 for product A) inclusive in that tier, meaning the 40th unit of A earns 10 yuan and the 41st earns 9 yuan?

## Turn 3 - User Simulator

Yes, the upper bounds are inclusive. The 40th unit of A earns 10 yuan, and the 41st unit earns 9 yuan.

## Turn 4 - Generic Agent

QUESTION: Are the three resource limits (100 hours technical preparation, 700 hours labor, 400 kg materials) hard ceilings that must not be exceeded, with any unused capacity simply allowed to go unused?

## Turn 4 - User Simulator

Yes, they are hard ceilings that must not be exceeded, and any unused capacity is allowed to go unused.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum production requirement for any product (e.g., must produce at least some units of A, B, or C), or is it acceptable to produce zero units of any product?

## Turn 5 - User Simulator

It is acceptable to produce zero units of any product.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or business rules I should account for, such as demand caps (maximum units that can be sold), minimum order quantities, or relationships between products?

## Turn 6 - User Simulator

No, there are no other constraints or business rules beyond the resource limits, the integer requirement, and the tiered profit structure.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total profit from producing products A, B, and C.

**Decision variables:** Integer (whole-unit) production quantities x_A, x_B, x_C ≥ 0.

**Resource constraints (hard ceilings, unused capacity allowed):**
- Technical preparation: 1·x_A + 2·x_B + 1·x_C ≤ 100 hours
- Labor: 10·x_A + 4·x_B + 5·x_C ≤ 700 hours
- Materials: 3·x_A + 2·x_B + 1·x_C ≤ 400 kg

**Tiered profit structure (upper bounds inclusive in each tier):**
- Product A: first 40 units @ 10 yuan, next 60 (units 41–100) @ 9 yuan, next 50 (units 101–150) @ 8 yuan, units above 150 @ 7 yuan
- Product B: first 50 units @ 6 yuan, next 50 (units 51–100) @ 4 yuan, units above 100 @ 3 yuan
- Product C: first 100 units @ 5 yuan, units above 100 @ 4 yuan

**Other:** No minimum production, no demand caps, no inter-product relationships. Zero production of any product is allowed.