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

QUESTION: Is the goal to maximize total profit, and are the profit figures in the table the profit per unit sold at each volume tier?

## Turn 1 - User Simulator

Yes, the goal is to maximize total profit. The profit figures in the table are the profit per unit sold at each corresponding volume tier.

## Turn 2 - Generic Agent

QUESTION: For the profit tiers, does the profit rate apply to all units of that product up to the tier's upper limit, or only to the units that fall within that specific tier range?

## Turn 2 - User Simulator

The profit rate applies only to the units that fall within that specific tier range.

## Turn 3 - Generic Agent

QUESTION: Are the production quantities for products A, B, and C required to be whole numbers, or can they be fractional?

## Turn 3 - User Simulator

The production quantities for products A, B, and C must be whole numbers.

## Turn 4 - Generic Agent

QUESTION: Are the sales volume ranges in the table (e.g., 0~40, 40~100) hard upper limits on how many units of each product can be produced, or are they just the boundaries where the profit rate changes?

## Turn 4 - User Simulator

They are just the boundaries where the profit rate changes.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or requirements for the production plan besides the technical preparation, labor, and material limits?

## Turn 5 - User Simulator

No, there are no other constraints or requirements besides the technical preparation, labor, and material limits.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total profit.
2.  **Decision Variables:** Let $x_A, x_B, x_C$ be the number of units produced for products A, B, and C, respectively.
3.  **Variable Domain:** $x_A, x_B, x_C$ must be non-negative integers.
4.  **Profit Structure (Piecewise Linear):** The profit per unit depends on the total quantity produced for that specific product, applying only to units within that tier.
    *   **Product A:**
        *   First 40 units: 10 yuan/unit
        *   Units 41–100: 9 yuan/unit
        *   Units 101–150: 8 yuan/unit
        *   Units >150: 7 yuan/unit
    *   **Product B:**
        *   First 50 units: 6 yuan/unit
        *   Units 51–100: 4 yuan/unit
        *   Units >100: 3 yuan/unit
    *   **Product C:**
        *   First 100 units: 5 yuan/unit
        *   Units >100: 4 yuan/unit
5.  **Resource Constraints:**
    *   **Technical Preparation:** $1x_A + 2x_B + 1x_C \le 100$ hours
    *   **Labor:** $10x_A + 4x_B + 5x_C \le 700$ hours
    *   **Materials:** $3x_A + 2x_B + 1x_C \le 400$ kg
6.  **Other Constraints:** None.

**Assumptions:**
*   The "Sales Volume" ranges in the table define the production volume tiers for profit calculation, not hard caps on production (confirmed by user).
*   The resource consumption rates (1h, 10h, 3kg for A, etc.) are constant per unit regardless of the production volume tier.