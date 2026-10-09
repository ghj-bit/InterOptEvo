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

QUESTION: What is the primary objective of this optimization—maximizing total revenue, maximizing profit (if costs are known), or simply finding any feasible combination of packages that meets the minimum sales and inventory constraints?

## Turn 1 - User Simulator

The primary objective is to maximize total revenue from selling packages A and B.

## Turn 2 - Generic Agent

QUESTION: Are the 200 shirts and 100 pairs of pants the only inventory available for these packages, or are there other items or constraints (like storage limits or production capacity) that could affect how many packages can be created?

## Turn 2 - User Simulator

The 200 shirts and 100 pairs of pants are the only inventory available for these packages. There are no other items or constraints like storage limits or production capacity affecting how many packages can be created.

## Turn 3 - Generic Agent

READY_TO_MODEL
I have confirmed the following understanding for the promotional package optimization:

**Objective:**
Maximize total revenue from selling Package A and Package B.

**Decision Variables:**
- Number of Package A units to sell (let's call this $A$)
- Number of Package B units to sell (let's call this $B$)

**Package Definitions:**
- **Package A:** Contains 1 shirt and 2 pairs of pants. Price: £30.
- **Package B:** Contains 3 shirts and 1 pair of pants. Price: £50.

**Constraints:**
1. **Shirt Inventory:** Total shirts used cannot exceed 200.
   - $1A + 3B \le 200$
2. **Pants Inventory:** Total pants used cannot exceed 100.
   - $2A + 1B \le 100$
3. **Minimum Sales for A:** At least 20 Package A units must be sold.
   - $A \ge 20$
4. **Minimum Sales for B:** At least 10 Package B units must be sold.
   - $B \ge 10$
5. **Non-negativity/Integrality:** $A$ and $B$ must be non-negative integers (since you can't sell partial packages).

**Revenue Function:**
Maximize $Z = 30A + 50B$