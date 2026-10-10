# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U8, U9, U10, U2, U3, U4, U5
I need help creating a monthly production plan for three products: A1, A2, A3. Production quantity of each product cannot exceed its maximum demand; for each product, production quantity is either zero or at least its minimum batch size; if produced, its fixed activation cost is incurred; and the total number of production days used, calculated as the sum over products of quantity produced divided by production quota, must not exceed 22 days.

Production days available per month: 22 days.

| Product | $A_{1}$ | $A_{2}$ | $A_{3}$ |
| :---: | :---: | :---: | :---: |
| Maximum Demand | 5300 | 4500 | 5400 |
| Selling Price | $124$ | $109$ | $115$ |
| Production Cost | $73.30$ | $52.90$ | $65.40$ |
| Production Quota | 500 | 450 | 550 |

| Product | $A_{1}$ | $A_{2}$ | $A_{3}$ |
| :---: | :---: | :---: | :---: |
| Activation Cost | $170000$ | $150000$ | $100000$ |

\begin{array}{c|ccc}
Product & A_{1} & A_{2} & A_{3} \\
\hline
Minimum Batch & 20 & 20 & 16
\end{array}

## Problem units
- U1 (context): I need help creating a monthly production plan for three products: A1, A2, A3.
- U2 (data): Production days available per month: 22 days.
- U3 (data): | Product | $A_{1}$ | $A_{2}$ | $A_{3}$ |
| :---: | :---: | :---: | :---: |
| Maximum Demand | 5300 | 4500 | 5400 |
| Selling Price | $124$ | $109$ | $115$ |
| Production Cost | $73.30$ | $52.90$ | $65.40$ |
| Production Quota | 500 | 450 | 550 |
- U4 (data): | Product | $A_{1}$ | $A_{2}$ | $A_{3}$ |
| :---: | :---: | :---: | :---: |
| Activation Cost | $170000$ | $150000$ | $100000$ |
- U5 (data): \begin{array}{c|ccc}
Product & A_{1} & A_{2} & A_{3} \\
\hline
Minimum Batch & 20 & 20 & 16
\end{array}
- U6 (objective): Maximize total revenue.
- U7 (constraint): Production quantity of each product cannot exceed its maximum demand.
- U8 (constraint): For each product, production quantity is either zero or at least its minimum batch size.
- U9 (constraint): If a product is produced, its fixed activation cost is incurred.
- U10 (constraint): Total number of production days used (sum over products of (quantity produced / production quota)) must not exceed 22 days.

## Hidden slot scoring rules
## H1: missing_revenue_objective
- Severity: P0
- Severity reason: Without knowing the objective, the optimization problem is undefined. The agent cannot build a model without inventing the objective, which would almost certainly be incorrect.
- Problem unit ID: U6
- Semantic hit rule: The agent explicitly asks about the objective function, e.g., what quantity to maximize, or asks to confirm if the objective is total revenue.
- Reference acceptable questions:
  - Could you clarify what we are trying to optimize? Is it maximizing total revenue, profit, or something else?
  - Just to confirm, is the objective to maximize total revenue?
- Failure modes:
  - Silently assuming the objective is to maximize total profit (revenue minus all costs)
  - Assuming the goal is to maximize production volume


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the objective to maximize total profit, calculated as total revenue minus total production costs minus total activation costs?

## Turn 1 - User Simulator

No. The objective is to maximize total revenue from selling the products.

## Turn 2 - Generic Agent

QUESTION: Are the production costs and activation costs included in the model as constraints, or are they excluded entirely from the optimization?

## Turn 2 - User Simulator

The production costs and activation costs are excluded entirely from the optimization.

## Turn 3 - Generic Agent

QUESTION: Is the production quantity for each product required to be an integer number of units?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the minimum batch size a lower bound on production quantity when a product is produced, or is it a fixed quantity that must be produced in addition to any other amount?

## Turn 4 - User Simulator

The minimum batch size is a lower bound on production quantity when a product is produced.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or requirements for the production plan that are not listed in the brief?

## Turn 5 - User Simulator

No, there are no other constraints or requirements beyond those listed in the brief.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total revenue.
    *   Revenue = (Quantity of A1 × $124) + (Quantity of A2 × $109) + (Quantity of A3 × $115).
    *   Production costs and activation costs are **excluded** from the objective function and do not appear as constraints.

2.  **Decision Variables:**
    *   $x_1, x_2, x_3$: Production quantities for products A1, A2, and A3, respectively.
    *   $y_1, y_2, y_3$: Binary variables indicating whether product A1, A2, or A3 is produced (1 if produced, 0 otherwise).

3.  **Constraints:**
    *   **Maximum Demand (Upper Bound):**
        *   $x_1 \le 5300$
        *   $x_2 \le 4500$
        *   $x_3 \le 5400$
    *   **Minimum Batch Size (Linked to Activation):**
        *   If $y_i = 1$, then $x_i \ge \text{MinBatch}_i$.
        *   If $y_i = 0$, then $x_i = 0$.
        *   This is typically modeled as:
            *   $x_i \ge \text{MinBatch}_i \cdot y_i$
            *   $x_i \le \text{MaxDemand}_i \cdot y_i$
        *   Specifically:
            *   $x_1 \ge 20 y_1$ and $x_1 \le 5300 y_1$
            *   $x_2 \ge 20 y_2$ and $x_2 \le 4500 y_2$
            *   $x_3 \ge 16 y_3$ and $x_3 \le 5400 y_3$
    *   **Production Days Limit:**
        *   Total production days $\le 22$.
        *   Days used = $\frac{x_1}{500} + \frac{x_2}{450} + \frac{x_3}{550} \le 22$.

4.  **Variable Domains:**
    *   $y_1, y_2, y_3 \in \{0, 1\}$ (Binary).
    *   $x_1, x_2, x_3 \ge 0$ (Non-negative).
    *   **Assumption:** Production quantities $x_i$ are treated as **continuous** variables. (The user indicated integrality requires internal confirmation, so this is flagged as an open assumption. If integrality is required, $x_i$ must be integers.)

5.  **Excluded Items:**
    *   Activation costs ($170,000, $150,000, $100,000) are not used in the model.
    *   Production costs ($73.30, $52.90, $65.40) are not used in the model.

**Open Assumptions:**
*   **Integrality:** It is assumed that production quantities $x_1, x_2, x_3$ can be fractional (continuous). If the business requires whole units, the model must be adjusted to require $x_i \in \mathbb{Z}^+$.