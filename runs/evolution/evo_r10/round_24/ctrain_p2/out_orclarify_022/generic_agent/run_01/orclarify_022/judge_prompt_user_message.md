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

QUESTION: When maximizing total revenue, should the production costs and activation costs be excluded entirely from the objective (i.e., objective is just sum of selling price × quantity), or should they still be subtracted as costs?

## Turn 2 - User Simulator

The objective is to maximize total revenue, which is the sum of selling price times quantity. Production costs and activation costs are not subtracted in the objective.

## Turn 3 - Generic Agent

QUESTION: The minimum batch sizes are 20, 20, and 16, which are very small compared to the maximum demands of 5300, 4500, and 5400. Are these minimum batch sizes in the same units as the demands (i.e., a product, if produced, must be made in a quantity of at least 20/20/16 units), or are they in different units (e.g., hundreds of units) that I should scale?

## Turn 3 - User Simulator

The minimum batch sizes are in the same units as the demands. If a product is produced, its quantity must be at least 20, 20, or 16 units, respectively.

## Turn 4 - Generic Agent

QUESTION: For the production-day constraint, is the total number of production days calculated as the sum over all three products of (quantity produced / production quota), and this sum must be ≤ 22 days?

## Turn 4 - User Simulator

Yes.

## Turn 5 - Generic Agent

QUESTION: Should the production quantities be integer values, or can they be continuous (fractional) values?

## Turn 5 - User Simulator

I

## Turn 6 - Generic Agent

QUESTION: Should the production quantities be integer values, or can they be continuous (fractional) values?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the production-day constraint, is the 22-day limit a hard cap that must not be exceeded, or is it a soft target where exceeding it is allowed with some penalty?

## Turn 7 - User Simulator

The 22-day limit is a hard cap that must not be exceeded.

## Turn 8 - Generic Agent

QUESTION: If a product is not produced (quantity = 0), is its activation cost also zero (i.e., activation cost is incurred only when the product is actually produced)?

## Turn 8 - User Simulator

Yes.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as minimum production requirements for all products, shared resource limitations beyond the 22-day cap, or any other business rules?

## Turn 9 - User Simulator

No.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total revenue = 124·x₁ + 109·x₂ + 115·x₃ (production costs and activation costs are NOT subtracted).

**Decision variables:** x₁, x₂, x₃ = production quantities of A₁, A₂, A₃ (integer vs. continuous still pending internal confirmation — I will model them as continuous by default and note the integer option).

**Constraints:**
1. **Upper bound (max demand):** x₁ ≤ 5300, x₂ ≤ 4500, x₃ ≤ 5400.
2. **Semi-continuous (min batch):** For each product i, xᵢ = 0 or xᵢ ≥ bᵢ, where b = (20, 20, 16). Modeled with binary yᵢ: xᵢ ≥ bᵢ·yᵢ and xᵢ ≤ Mᵢ·yᵢ.
3. **Production-day cap (hard):** x₁/500 + x₂/450 + x₃/550 ≤ 22.
4. **Activation cost:** Incurred only when yᵢ = 1 (i.e., product is produced). Since activation costs are not in the objective, this is purely a bookkeeping note — no constraint needed beyond the semi-continuous formulation.

**Parameters:**
| | A₁ | A₂ | A₃ |
|---|---|---|---|
| Max demand | 5300 | 4500 | 5400 |
| Selling price | 124 | 109 | 115 |
| Production cost | 73.30 | 52.90 | 65.40 |
| Production quota | 500 | 450 | 550 |
| Activation cost | 170000 | 150000 | 100000 |
| Min batch | 20 | 20 | 16 |

**Note:** Production costs and activation costs are provided for reference but do not enter the objective or any constraint.