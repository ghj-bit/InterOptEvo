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

QUESTION: Is the objective to maximize total profit (sum of (selling price − production cost) × quantity, minus the activation costs for products that are produced)?

## Turn 1 - User Simulator

No. The objective is to maximize total revenue from selling the products.

## Turn 2 - Generic Agent

QUESTION: When maximizing total revenue, should the production costs and activation costs be excluded entirely from the objective (i.e., objective is just sum of selling price × quantity), or should they be subtracted as costs?

## Turn 2 - User Simulator

The objective is to maximize total revenue, which is the sum of selling price times quantity. Production costs and activation costs are not subtracted in the objective.

## Turn 3 - Generic Agent

QUESTION: The minimum batch sizes are 20, 20, and 16 units, which are very small compared to the maximum demands (5300, 4500, 5400). Is the intent that if a product is produced, its quantity must be at least this minimum batch size (e.g., at least 20 units for A1), or is there a different interpretation of "minimum batch size" you had in mind?

## Turn 3 - User Simulator

Yes, if a product is produced, its quantity must be at least its minimum batch size.

## Turn 4 - Generic Agent

QUESTION: Should the production quantities be required to be integers (whole units), or can they be continuous (fractional) values?

## Turn 4 - User Simulator

I

## Turn 5 - Generic Agent

QUESTION: Should the production quantities be required to be integers (whole units), or can they be continuous (fractional) values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the production days constraint, is the formula exactly (quantity of A1 / 500) + (quantity of A2 / 450) + (quantity of A3 / 550) ≤ 22, where each product's quota is its daily production rate?

## Turn 6 - User Simulator

Yes, the total number of production days used is calculated as the sum over products of quantity produced divided by production quota, and this total must not exceed 22 days.

## Turn 7 - Generic Agent

QUESTION: Is there any other constraint or business rule I should include in the model besides: (1) quantity ≤ maximum demand, (2) quantity is zero or at least the minimum batch size, (3) activation cost incurred if produced, (4) total production days ≤ 22, and (5) maximize total revenue?

## Turn 7 - User Simulator

No, those are the only constraints and business rules to include.

## Turn 8 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total revenue = 124·x₁ + 109·x₂ + 115·x₃ (production costs and activation costs are NOT subtracted).

**Decision variables:**
- x₁, x₂, x₃: production quantities for A1, A2, A3 (continuous, non-negative — integrality deferred to internal confirmation).
- y₁, y₂, y₃: binary activation indicators (1 if product is produced, 0 otherwise).

**Constraints:**
1. **Demand upper bounds:** x₁ ≤ 5300, x₂ ≤ 4500, x₃ ≤ 5400.
2. **Minimum batch (semi-continuous):** If yᵢ = 1 then xᵢ ≥ minimum batch (20, 20, 16 respectively); if yᵢ = 0 then xᵢ = 0. Formally: xᵢ ≥ min_batchᵢ · yᵢ and xᵢ ≤ max_demandᵢ · yᵢ.
3. **Production days:** x₁/500 + x₂/450 + x₃/550 ≤ 22.
4. **Activation cost:** Incurred when yᵢ = 1 (170000, 150000, 100000 respectively) — noted as a cost but NOT included in the objective per client confirmation.

**No other constraints or business rules apply.**