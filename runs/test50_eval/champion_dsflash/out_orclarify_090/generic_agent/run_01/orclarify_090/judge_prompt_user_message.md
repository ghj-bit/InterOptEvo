# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U8, U2, U3, U4
I need help designing promotional packages to clear out last season's inventory. Total shirts used in packages cannot exceed 200, total pants used in packages cannot exceed 100, and the number of A packages sold must be at least 20 while the number of B packages sold must be at least 10.

Available inventory: 200 shirts, 100 pairs of pants.

Package A: 1 shirt, 2 pairs of pants, price £30. Package B: 3 shirts, 1 pair of pants, price £50.

Minimum desired sales: 20 package A, 10 package B.

## Problem units
- U1 (context): I need help designing promotional packages to clear out last season's inventory.
- U2 (data): Available inventory: 200 shirts, 100 pairs of pants.
- U3 (data): Package A: 1 shirt, 2 pairs of pants, price £30. Package B: 3 shirts, 1 pair of pants, price £50.
- U4 (data): Minimum desired sales: 20 package A, 10 package B.
- U5 (constraint): Total shirts used in packages cannot exceed 200.
- U6 (constraint): Total pants used in packages cannot exceed 100.
- U7 (constraint): Number of A packages sold must be at least 20.
- U8 (constraint): Number of B packages sold must be at least 10.
- U9 (objective): Maximize total revenue from selling packages A and B.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without knowing the objective, a modeling agent cannot define the optimization criterion. The entire problem formulation is impossible without specifying what should be maximized.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must explicitly ask about the optimization goal, mentioning "revenue" or "objective" or "maximize" in the context of what to optimize.
- Reference acceptable questions:
  - What exactly are we trying to maximize? Is it total revenue, profit, or something else?
  - Should we just focus on getting the most money from selling the packages?
- Failure modes:
  - Silent assumption that the goal is to maximize profit rather than revenue.
  - Incorrectly assuming the objective is to minimize leftover inventory.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective — maximize total revenue from packages sold, or something else such as clearing as much inventory as possible?

## Turn 1 - User Simulator

The objective is to maximize total revenue from selling packages A and B.

## Turn 2 - Generic Agent

QUESTION: Can the number of packages sold be fractional (e.g., 20.5), or must they be whole numbers?

## Turn 2 - User Simulator

The number of packages sold must be whole numbers.

## Turn 3 - Generic Agent

QUESTION: For the inventory limits — is it acceptable to leave shirts or pants unused (not sold in any package), or must all 200 shirts and 100 pants be used?

## Turn 3 - User Simulator

It is acceptable to leave shirts or pants unused. The limits are maximums: total shirts used cannot exceed 200, and total pants used cannot exceed 100.

## Turn 4 - Generic Agent

QUESTION: Are the minimums of 20 A packages and 10 B packages hard requirements that must always be met, or just targets you'd like to hit if possible?

## Turn 4 - User Simulator

They are hard requirements that must always be met.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on how many A or B packages can be sold (beyond the inventory constraints), or can you sell as many as the inventory allows?

## Turn 5 - User Simulator

There is no upper limit on the number of A or B packages sold beyond the inventory constraints.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total revenue from packages A and B.
- **Decision variables:** Number of package A sold (integer ≥ 0), number of package B sold (integer ≥ 0).
- **Prices:** A = £30, B = £50.
- **Resource use per package:** A uses 1 shirt + 2 pants; B uses 3 shirts + 1 pant.
- **Inventory limits (maximums):** total shirts used ≤ 200; total pants used ≤ 100. Unused inventory is allowed.
- **Minimum sales (hard):** A ≥ 20, B ≥ 10.
- **No upper bounds** on package counts other than those implied by inventory.
- **Integrality:** package counts must be whole numbers.

Model:

maximize 30·A + 50·B
subject to
  A + 3B ≤ 200        (shirts)
  2A + B ≤ 100        (pants)
  A ≥ 20
  B ≥ 10
  A, B integer ≥ 0