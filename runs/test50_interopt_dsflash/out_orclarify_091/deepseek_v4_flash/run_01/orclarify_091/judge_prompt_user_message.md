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

Q1 (turn 1): Should the weekly production plan allow fractional units of A and B, or must it produce only whole units?
Q2 (turn 2): Are there any maximum weekly demand or sales limits for Product A and Product B, or can all produced units be sold?
Q3 (turn 3): Can weekly production quantities be zero or any nonnegative whole number, or are there minimum weekly production or setup requirements for either product?
Q4 (turn 4): Is the 30-hour weekly assembly time limit a strict maximum that must never be exceeded, or can it be exceeded with overtime or additional cost?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Should the weekly production plan allow fractional units of A and B, or must it produce only whole units?

## Turn 1 - User Simulator

We must produce only whole units.

## Turn 2 - Generic Agent

QUESTION: Are there any maximum weekly demand or sales limits for Product A and Product B, or can all produced units be sold?

## Turn 2 - User Simulator

There are no maximum weekly demand or sales limits mentioned — we can sell all units produced.

## Turn 3 - Generic Agent

QUESTION: Can weekly production quantities be zero or any nonnegative whole number, or are there minimum weekly production or setup requirements for either product?

## Turn 3 - User Simulator

There are no minimum weekly production or setup requirements mentioned, so zero or any nonnegative whole number is fine.

## Turn 4 - Generic Agent

QUESTION: Is the 30-hour weekly assembly time limit a strict maximum that must never be exceeded, or can it be exceeded with overtime or additional cost?

## Turn 4 - User Simulator

It’s a strict maximum that must not be exceeded.

## Turn 5 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.950

Confidence rationale: The request now specifies the decision variables (weekly whole-unit production quantities of A and B), the objective (maximize £3 per unit of A plus £5 per unit of B), the only stated resource constraint (assembly time must not exceed 30 hours per week), the integer domain, no demand caps, no minimum production or setup requirements, and a strict capacity limit. No material formulation-changing ambiguity remains.

Summary: Formulate an integer linear program to maximize weekly profit from producing whole units of Product A and Product B. Product A earns £3 per unit and uses 12 minutes of assembly time; Product B earns £5 per unit and uses 25 minutes. Total weekly assembly time must not exceed 30 hours. There are no demand limits, no minimum production requirements, and no overtime. Decision variables are nonnegative integer weekly production quantities for A and B.