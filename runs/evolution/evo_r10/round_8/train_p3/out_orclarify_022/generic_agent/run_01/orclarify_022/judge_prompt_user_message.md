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

QUESTION: Is the objective to maximize total profit (sum over products of (selling price − production cost) × quantity, minus the activation costs of the products that are produced)?

## Turn 1 - User Simulator

No. The objective is to maximize total revenue from selling the products.

## Turn 2 - Generic Agent

QUESTION: When maximizing total revenue, should the production costs and activation costs be excluded entirely from the objective (i.e., revenue = selling price × quantity only), or should they be subtracted from revenue in the objective?

## Turn 2 - User Simulator

The production costs and activation costs should be excluded entirely from the objective. The objective is to maximize total revenue, which is selling price times quantity only.

## Turn 3 - Generic Agent

QUESTION: For the minimum batch size rule, is the minimum batch a lower bound on the production quantity (i.e., if a product is produced, its quantity must be at least the minimum batch, and can be any value up to its maximum demand), or must the production quantity be an exact multiple of the minimum batch size?

## Turn 3 - User Simulator

The minimum batch is a lower bound on the production quantity. If a product is produced, its quantity must be at least the minimum batch size and can be any value up to its maximum demand.

## Turn 4 - Generic Agent

QUESTION: Should the production quantities be required to be integers (whole units), or can they be any continuous (fractional) values?

## Turn 4 - User Simulator

I don't have a specific business fact confirming whether production quantities must be whole units or can be fractional. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: For the production days constraint, is the "production quota" (500, 450, 550) the number of units produced per day for each product, so that production days for a product equals its quantity divided by its quota?

## Turn 5 - User Simulator

Yes. The production quota is the number of units produced per day for each product, so the production days for a product equals its quantity divided by its quota.

## Turn 6 - Generic Agent

QUESTION: Is the maximum demand for each product a hard upper bound on its production quantity (i.e., production quantity ≤ maximum demand), or is it a target that can be exceeded if profitable?

## Turn 6 - User Simulator

The maximum demand is a hard upper bound on the production quantity.

## Turn 7 - Generic Agent

QUESTION: If a product is not produced (quantity = 0), is its activation cost also zero, or is the activation cost incurred regardless of whether the product is produced?

## Turn 7 - User Simulator

If a product is not produced, its activation cost is zero. The activation cost is incurred only if the product is produced.

## Turn 8 - Generic Agent

QUESTION: Since the objective is revenue only (excluding costs), and the activation costs are excluded from the objective, are the activation costs still relevant to the model at all, or should they be completely ignored in the formulation?

## Turn 8 - User Simulator

The activation costs are still relevant to the model. They are incurred if a product is produced, even though they are excluded from the revenue objective.

## Turn 9 - Generic Agent

QUESTION: Since the activation costs are excluded from the objective but still "relevant to the model," should they be included as a constraint (e.g., a budget limit on total activation costs), or are they simply informational and do not affect the optimization at all?

## Turn 9 - User Simulator

The activation costs are simply informational and do not affect the optimization at all.

## Turn 10 - Generic Agent

QUESTION: Should the production quantities be required to be integers (whole units), or can they be any continuous (fractional) values?

## Turn 10 - User Simulator

I don't have a specific business fact confirming whether production quantities must be whole units or can be fractional. That point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is the total production days constraint a hard limit (total days ≤ 22) or a soft limit that can be violated with a penalty?

## Turn 11 - User Simulator

The total production days constraint is a hard limit: total days must not exceed 22.

## Turn 12 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as minimum production requirements for all products, shared resources beyond the 22 days, or any other business rules?

## Turn 12 - User Simulator

No. The only constraints are:
- Production quantity of each product cannot exceed its maximum demand.
- For each product, production quantity is either zero or at least its minimum batch size.
- Total production days used must not exceed 22 days.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

**Objective:** Maximize total revenue = 124·x₁ + 109·x₂ + 115·x₃, where x₁, x₂, x₃ are the production quantities of A₁, A₂, A₃ respectively.

**Decision variables:** x₁, x₂, x₃ (production quantities) — continuous (integrality not confirmed by client; will treat as continuous). Binary variables y₁, y₂, y₃ to model the "zero or at least minimum batch" logic.

**Constraints:**
1. **Upper bound (demand):** x₁ ≤ 5300, x₂ ≤ 4500, x₃ ≤ 5400.
2. **Minimum batch / semi-continuous:** For each product i, xᵢ = 0 or xᵢ ≥ minimum batch. Modeled as:
   - xᵢ ≥ 20·y₁ (for A₁), xᵢ ≥ 20·y₂ (for A₂), xᵢ ≥ 16·y₃ (for A₃)
   - xᵢ ≤ 5300·y₁, xᵢ ≤ 4500·y₂, xᵢ ≤ 5400·y₃ (upper bound tied to activation)
   - yᵢ ∈ {0, 1}
3. **Production days:** x₁/500 + x₂/450 + x₃/550 ≤ 22.

**Not in the model:** Production costs, activation costs (informational only, do not affect optimization).

**No other constraints** beyond the three listed above.