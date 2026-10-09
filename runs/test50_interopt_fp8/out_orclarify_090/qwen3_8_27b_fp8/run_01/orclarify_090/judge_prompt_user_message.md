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


# Atomic Question Map

Q1 (turn 1): What is the primary goal of this optimization: maximizing total revenue, minimizing the amount of leftover inventory, or something else?
Q2 (turn 2): Are the minimum sales requirements of 20 Package A and 10 Package B hard constraints that must be strictly met, or are they soft targets that can be missed if doing so leads to higher total revenue?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the primary goal of this optimization: maximizing total revenue, minimizing the amount of leftover inventory, or something else?

## Turn 1 - User Simulator

The primary goal is to maximize total revenue from selling the packages.

## Turn 2 - Generic Agent

QUESTION: Are the minimum sales requirements of 20 Package A and 10 Package B hard constraints that must be strictly met, or are they soft targets that can be missed if doing so leads to higher total revenue?

## Turn 2 - User Simulator

They are hard constraints that must be strictly met.

## Turn 3 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 1.000

Confidence rationale: The request is fully specified. The decision variables are the number of Package A and Package B sold. The objective is to maximize total revenue (30*A + 50*B). The constraints are clearly defined: resource limits (shirts <= 200, pants <= 100), hard minimum sales (A >= 20, B >= 10), and non-negativity/integer domains (implied by the nature of packages). No silent assumptions are required.

Summary: Maximize revenue from selling Package A (£30, 1 shirt, 2 pants) and Package B (£50, 3 shirts, 1 pant) subject to inventory limits (200 shirts, 100 pants) and minimum sales requirements (at least 20 A, at least 10 B).