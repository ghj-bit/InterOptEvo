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

QUESTION: Is the objective to maximize total profit (revenue from selling price minus production cost per unit, minus activation costs for products that are produced)?

## Turn 1 - User Simulator

No. The objective is to maximize total revenue from selling the products.

## Turn 2 - Generic Agent

QUESTION: Should the production cost per unit and the activation costs be treated as constraints (e.g., a budget limit) or are they simply not part of this model at all?

## Turn 2 - User Simulator

The production cost per unit and the activation costs are not part of this model at all.

## Turn 3 - Generic Agent

QUESTION: For the minimum batch size rule, is the production quantity required to be a multiple of the minimum batch size (e.g., A1 must be 0 or 20, 40, 60, ...), or is it simply that if produced, the quantity must be at least the minimum batch size (e.g., A1 can be any value from 20 up to 5300)?

## Turn 3 - User Simulator

It is simply that if produced, the quantity must be at least the minimum batch size.

## Turn 4 - Generic Agent

QUESTION: Is the production quantity for each product required to be an integer (whole units), or can it be any real number?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: For the production days constraint, is the 22-day limit a hard constraint (total days must be ≤ 22), or is it a target that can be exceeded with some penalty?

## Turn 5 - User Simulator

The 22-day limit is a hard constraint.

## Turn 6 - Generic Agent

QUESTION: Is the production quantity for each product required to be an integer (whole units), or can it be any real number?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or business rules I should be aware of, such as a minimum total production requirement, a maximum total production, or any relationship between the three products (e.g., they share a resource beyond the 22 days)?

## Turn 7 - User Simulator

No, there are no other constraints or business rules beyond those already specified.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** A1, A2, A3.
- **Decision variables:** Production quantity for each product (x1, x2, x3). Domain: to be confirmed internally (integer vs. real); I will model as continuous real numbers unless the client specifies otherwise.
- **Objective:** Maximize total revenue = 124·x1 + 109·x2 + 115·x3.
- **Constraints:**
  1. **Demand cap:** x1 ≤ 5300, x2 ≤ 4500, x3 ≤ 5400.
  2. **Minimum batch (semi-continuous):** For each product, x_i = 0 or x_i ≥ minimum batch (20 for A1, 20 for A2, 16 for A3).
  3. **Production days (hard):** x1/500 + x2/450 + x3/550 ≤ 22.
- **Not in the model:** Production cost per unit, activation costs, and any other business rules.
- **No other constraints** beyond the above.