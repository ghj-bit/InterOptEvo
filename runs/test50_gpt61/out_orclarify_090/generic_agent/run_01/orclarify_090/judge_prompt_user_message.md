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

QUESTION: Should I optimize the package mix for maximum total revenue while respecting the inventory limits and minimum sales?

## Turn 1 - User Simulator

Yes.

## Turn 2 - Generic Agent

READY_TO_MODEL

Confirmed understanding: maximize total revenue from whole A and B packages, subject to the inventory limits and minimum sales of 20 A packages and 10 B packages.

Let:
- \(A\) = number of Package A sold
- \(B\) = number of Package B sold

Constraints:

\[
A+3B\le 200 \quad \text{(shirts)}
\]

\[
2A+B\le 100 \quad \text{(pants)}
\]

\[
A\ge20,\quad B\ge10
\]

Maximize:

\[
30A+50B
\]

## Optimal package mix

- **20 Package A**
- **60 Package B**

Inventory used:

- Shirts: \(20+(3\times60)=200\)
- Pants: \((2\times20)+60=100\)

Revenue:

\[
(20\times£30)+(60\times£50)=£3,600
\]

**Recommendation: sell 20 Package A and 60 Package B for maximum revenue of £3,600, clearing all available inventory.**