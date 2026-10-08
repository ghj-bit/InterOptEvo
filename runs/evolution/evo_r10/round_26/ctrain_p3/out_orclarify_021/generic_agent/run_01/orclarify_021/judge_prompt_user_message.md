# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U2, U3
I need help planning an order of dining tables from three suppliers. The number of orders placed with each supplier must be an integer, and the total number of tables ordered must be at least 150 and no more than 600.

Cost per dining table: Supplier A $120, Supplier B $110, Supplier C $100.

Each order from Supplier A includes 20 tables; each order from Supplier B includes 15 tables; each order from Supplier C includes 15 tables.

## Problem units
- U1 (context): I need help planning an order of dining tables from three suppliers.
- U2 (data): Cost per dining table: Supplier A $120, Supplier B $110, Supplier C $100.
- U3 (data): Each order from Supplier A includes 20 tables; each order from Supplier B includes 15 tables; each order from Supplier C includes 15 tables.
- U4 (objective): Minimize the total cost of the order.
- U5 (constraint): The number of orders placed with each supplier must be an integer.
- U6 (constraint): The total number of tables ordered must be at least 150.
- U7 (constraint): The total number of tables ordered must be no more than 600.
- U8 (constraint): If the restaurant decides to order tables from Supplier A, it must also order at least 30 tables from Supplier B.
- U9 (constraint): If the restaurant decides to order tables from Supplier B, it must also order tables from Supplier C.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without an explicit objective, the optimization problem is ill-posed. The modeling agent cannot formulate a meaningful model because there is no goal to optimize, making the problem essentially undefined.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must ask about the objective or goal of the optimization, such as whether to minimize cost, maximize something else, or achieve a specific target.
- Reference acceptable questions:
  - What are we trying to optimize? Should we minimize total cost or something else?
  - Is the goal to reduce the overall cost of the table order?
- Failure modes:
  - Silently assuming the objective is to minimize the number of tables ordered.
  - Assuming the objective is to minimize the number of orders placed.

## H2: A_requires_min_B_tables
- Severity: P1
- Severity reason: This is a material business rule that links orders from Supplier A to a minimum quantity from Supplier B. Without it, the model is still coherent but the feasible region and optimal solution will likely be significantly different, missing a key constraint of the real problem.
- Problem unit ID: U8
- Semantic hit rule: The agent's question must reference the conditional constraint linking an order from Supplier A to a minimum number of tables from Supplier B.
- Reference acceptable questions:
  - If we order from Supplier A, do we have to order a certain number of tables from Supplier B?
  - Is there any requirement that ordering from A forces us to order some minimum amount from B?
- Failure modes:
  - Silently ignoring the link and treating orders from A and B as independent.
  - Assuming that ordering from A carries no obligation to order from B.

## H3: B_requires_C_order
- Severity: P1
- Severity reason: This conditional rule fundamentally affects the feasible ordering patterns. Omitting it produces a model that is structurally valid but fails to capture a real business restriction, likely yielding a solution that would be invalid in practice.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must explicitly ask about the requirement that any order from Supplier B implies an order from Supplier C.
- Reference acceptable questions:
  - If we place an order with Supplier B, do we also have to place an order with Supplier C?
  - Does ordering from B automatically require ordering from C as well?
- Failure modes:
  - Silently assuming that orders from Supplier B and C are entirely independent.
  - Treating Supplier B and C as completely interchangeable without any linked obligation.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the goal of this plan — are we minimizing the total cost of the tables ordered?

## Turn 1 - User Simulator

Yes, the goal is to minimize the total cost of the tables ordered.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum limits on how many orders (or tables) can be placed with each individual supplier, or can we order any non-negative integer number of orders from each of A, B, and C?

## Turn 2 - User Simulator

There are no minimum or maximum limits on the number of orders placed with each individual supplier. We can order any non-negative integer number of orders from each of A, B, and C.

## Turn 3 - Generic Agent

QUESTION: The total number of tables must be at least 150 and at most 600 — is the 600-table upper bound a hard limit we must respect, or is it just a rough guideline we can exceed if it helps?

## Turn 3 - User Simulator

The 600-table upper bound is a hard limit we must respect.

## Turn 4 - Generic Agent

QUESTION: Since we're minimizing cost and Supplier C is cheapest, the model would naturally push toward the 600-table maximum — is that intended (i.e., we want as many tables as possible up to 600), or is there a reason we might want to stop at fewer than 600 tables?

## Turn 4 - User Simulator

The 600-table upper bound is a hard limit, but it is not a target. We want to order as few tables as possible while still meeting the minimum of 150, because our goal is to minimize total cost.

## Turn 5 - Generic Agent

QUESTION: To confirm the lower bound: is the 150-table minimum a hard requirement that must be met (i.e., we cannot order fewer than 150 tables in total)?

## Turn 5 - User Simulator

Yes, the 150-table minimum is a hard requirement.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Non-negative integer number of orders placed with each supplier:
  - `x_A` = number of orders from Supplier A (each order = 20 tables)
  - `x_B` = number of orders from Supplier B (each order = 15 tables)
  - `x_C` = number of orders from Supplier C (each order = 15 tables)

- **Objective:** Minimize total cost = 120·(20·x_A) + 110·(15·x_B) + 100·(15·x_C) = 2400·x_A + 1650·x_B + 1500·x_C.

- **Constraints:**
  - Total tables: 20·x_A + 15·x_B + 15·x_C ≥ 150 (hard minimum)
  - Total tables: 20·x_A + 15·x_B + 15·x_C ≤ 600 (hard maximum, not a target)
  - x_A, x_B, x_C are non-negative integers.
  - No per-supplier minimum or maximum limits.

- **Note:** Since we minimize cost and the minimum of 150 tables is a hard requirement, the optimum will sit at the smallest feasible total table count that is at least 150 (and the 600 cap will not bind).