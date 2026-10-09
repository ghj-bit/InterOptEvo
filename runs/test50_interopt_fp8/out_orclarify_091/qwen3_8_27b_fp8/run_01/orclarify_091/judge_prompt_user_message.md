# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U2, U3, U4
I need help creating a production plan for two products, where total assembly time per week must not exceed 30 hours and we aim to maximize total profit, which is £3 per unit of A sold plus £5 per unit of B sold.

Profit per unit sold: Product A: £3, Product B: £5.

Assembly time per unit: Product A: 12 minutes, Product B: 25 minutes.

Effective machine working time per week: 30 hours.

## Problem units
- U1 (context): I need help creating a production plan for two products.
- U2 (data): Profit per unit sold: Product A: £3, Product B: £5.
- U3 (data): Assembly time per unit: Product A: 12 minutes, Product B: 25 minutes.
- U4 (data): Effective machine working time per week: 30 hours.
- U5 (constraint): Total assembly time per week must not exceed 30 hours.
- U6 (constraint): For every five units of product A produced, at least two units of product B must be produced.
- U7 (objective): Maximize total profit: £3 per unit of A sold + £5 per unit of B sold.

## Hidden slot scoring rules
## H1: missing_production_ratio_constraint
- Severity: P1
- Severity reason: Without this constraint, the model would yield a production plan that might not satisfy the required product mix, making it inaccurate for the real-world scenario. However, a valid optimization model can still be formulated without it.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must explicitly inquire about a required production ratio or proportional constraint linking the quantities of products A and B.
- Reference acceptable questions:
  - Is there any required production ratio between product A and product B?
  - Do we need to maintain a specific mix, like at least 2 units of B for every 5 units of A?
- Failure modes:
  - Silently assuming no production mix requirement, leading to a solution that might only produce product A.
  - Assuming the two products are independent and only limited by machine time.


# Atomic Question Map

Q1 (turn 1): Are there any other resource constraints, such as raw material availability or machine capacity, that must be respected in addition to the 30-hour assembly limit?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are there any other resource constraints, such as raw material availability or machine capacity, that must be respected in addition to the 30-hour assembly limit?

## Turn 1 - User Simulator

No. The only resource constraint is the 30-hour weekly assembly limit.

## Turn 2 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 1.000

Confidence rationale: The request is fully specified. The objective (maximize profit), decision variables (units of A and B), single constraint (30-hour assembly limit), and all necessary parameters (profit per unit, assembly time per unit) are clearly defined. No other constraints or complexities were identified.

Summary: Maximize total profit (3*A + 5*B) subject to the assembly time constraint (12*A + 25*B <= 1800 minutes), where A and B are non-negative integers representing the number of units of Product A and Product B produced per week.