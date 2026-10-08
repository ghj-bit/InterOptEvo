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

QUESTION: For the profit tiers, is the profit rate (yuan per unit) applied to every unit produced in that tier (e.g., if 60 units of A are produced, the first 40 earn 10 yuan each and the next 20 earn 9 yuan each), or is a single profit rate chosen based on the total quantity produced?

## Turn 1 - User Simulator

The profit rate is applied to every unit produced in that tier. For example, if 60 units of Product A are produced, the first 40 units earn 10 yuan each, and the next 20 units earn 9 yuan each.

## Turn 2 - Generic Agent

QUESTION: Are the production quantities of products A, B, and C required to be whole numbers (integers), or can they be fractional values?

## Turn 2 - User Simulator

The production quantities must be whole numbers (integers).

## Turn 3 - Generic Agent

QUESTION: The table lists "Sales Volume" ranges for each product (e.g., A: 0~40, 40~100, etc.). Are these ranges hard upper limits on how many units can be produced (i.e., you cannot produce more than 150 units of A, more than 100 units of B, or more than 100 units of C), or are they merely the tiers over which the profit rate changes with no additional production cap beyond the resource constraints?

## Turn 3 - User Simulator

The ranges are merely the tiers over which the profit rate changes. There are no additional production caps beyond the resource constraints.

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize total profit (sum of revenue from all units produced), or is there another objective such as minimizing cost or meeting a demand target?

## Turn 4 - User Simulator

The objective is to maximize total profit.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** A, B, C, with integer (whole-number) production quantities.
- **Objective:** Maximize total profit.
- **Profit structure (tiered, marginal):**
  - Product A: first 40 units at 10 yuan each, next 60 (41–100) at 9 yuan each, next 50 (101–150) at 8 yuan each, units above 150 at 7 yuan each.
  - Product B: first 50 units at 6 yuan each, next 50 (51–100) at 4 yuan each, units above 100 at 3 yuan each.
  - Product C: first 100 units at 5 yuan each, units above 100 at 4 yuan each.
- **Resource constraints (upper bounds on total usage):**
  - Technical preparation: 1 hr/unit A + 2 hr/unit B + 1 hr/unit C ≤ 100 hours.
  - Labor: 10 hr/unit A + 4 hr/unit B + 5 hr/unit C ≤ 700 hours.
  - Materials: 3 kg/unit A + 2 kg/unit B + 1 kg/unit C ≤ 400 kg.
- **No additional production caps** beyond the resource constraints; the tier ranges only define where the profit rate changes.
- **Variables:** Non-negative integers for units of A, B, C (or equivalently, tier-split variables to linearize the piecewise-linear profit).