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

QUESTION: Is the objective to maximize total profit (sum over products of (selling price − production cost) × quantity, minus the activation costs of produced products)?

## Turn 1 - User Simulator

No. The objective is to maximize total revenue from selling the products.

## Turn 2 - Generic Agent

QUESTION: When maximizing total revenue, should the production costs and activation costs be included as deductions in the objective, or should the objective be purely the sum of selling price times quantity with costs handled only as constraints?

## Turn 2 - User Simulator

The objective is purely the sum of selling price times quantity. Production costs and activation costs are not deducted in the objective.

## Turn 3 - Generic Agent

QUESTION: For the minimum batch size rule, is the lower bound a hard constraint (if produced, quantity must be at least the minimum batch), or is it just a typical batch size that production may fall below?

## Turn 3 - User Simulator

It is a hard constraint. If a product is produced, its quantity must be at least its minimum batch size.

## Turn 4 - Generic Agent

QUESTION: The production days constraint uses quantity divided by production quota for each product. Is the production quota a fixed daily capacity (i.e., at most 500 units of A1 per day, 450 of A2, 550 of A3), and can multiple products be produced on the same day, or is the 22-day limit a shared resource where each product's days are additive?

## Turn 4 - User Simulator

The 22-day limit is a shared resource where each product's days are additive. The production quota is the daily capacity for that product.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities required to be integers (whole units), or can they be any non-negative real number?

## Turn 5 - User Simulator

I

## Turn 6 - Generic Agent

QUESTION: Did you mean to say the production quantities must be integers (whole units), or can they be any non-negative real number?

## Turn 6 - User Simulator

The production quantities can be any non-negative real number.

## Turn 7 - Generic Agent

QUESTION: Is there any other constraint or business rule I should be aware of, such as a minimum total production requirement, a budget limit, or a requirement that at least one product must be produced?

## Turn 7 - User Simulator

No, there are no other constraints or business rules beyond those already specified.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:**
- x_i = production quantity of product i (i = A1, A2, A3), continuous, non-negative.
- y_i = binary activation variable for product i (1 if produced, 0 otherwise).

**Objective:**
- Maximize total revenue: 124·x_A1 + 109·x_A2 + 115·x_A3.
- Production costs and activation costs are NOT deducted from the objective.

**Constraints:**
1. **Demand cap:** x_A1 ≤ 5300, x_A2 ≤ 4500, x_A3 ≤ 5400.
2. **Minimum batch (hard):** If y_i = 1, then x_i ≥ minimum batch (20 for A1, 20 for A2, 16 for A3). If y_i = 0, then x_i = 0. (Standard big-M or indicator formulation.)
3. **Production days (shared, additive):** x_A1/500 + x_A2/450 + x_A3/550 ≤ 22.
4. **Domains:** x_i ≥ 0 continuous; y_i ∈ {0, 1}.

**Not in the model:** Production costs, activation costs, and selling prices beyond the revenue objective. No other constraints.