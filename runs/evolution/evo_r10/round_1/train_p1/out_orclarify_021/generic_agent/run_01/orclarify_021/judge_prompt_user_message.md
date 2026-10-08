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

QUESTION: What is the objective of this plan — minimize total cost, maximize total tables, or something else (e.g., meet a specific target number of tables at minimum cost)?

## Turn 1 - User Simulator

The objective is to minimize the total cost of the order.

## Turn 2 - Generic Agent

QUESTION: Are there any per-supplier limits on how many orders (or total tables) can be placed with each supplier, or can we order any non-negative integer number of orders from each?

## Turn 2 - User Simulator

There are no per-supplier limits on the number of orders or total tables. We can order any non-negative integer number of orders from each supplier.

## Turn 3 - Generic Agent

QUESTION: The total tables must be between 150 and 600 — is the lower bound a hard minimum (we must order at least 150 tables), or is it just a range within which any total is acceptable?

## Turn 3 - User Simulator

The lower bound is a hard minimum. We must order at least 150 tables.

## Turn 4 - Generic Agent

QUESTION: Since we minimize cost and must order at least 150 tables, the natural solution is to order exactly 150 tables (the cheapest feasible total). Is it acceptable to order exactly 150 tables, or must the total be strictly greater than 150?

## Turn 4 - User Simulator

It is acceptable to order exactly 150 tables.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Non-negative integer number of orders placed with each supplier: `x_A` (Supplier A), `x_B` (Supplier B), `x_C` (Supplier C).
- **Tables per order:** Supplier A: 20 tables/order; Supplier B: 15 tables/order; Supplier C: 15 tables/order.
- **Total tables:** `20·x_A + 15·x_B + 15·x_C`, which must satisfy `150 ≤ total ≤ 600`. The lower bound is a hard minimum; exactly 150 is acceptable.
- **Cost per table:** Supplier A: $120; Supplier B: $110; Supplier C: $100.
- **Objective:** Minimize total cost = `120·(20·x_A) + 110·(15·x_B) + 100·(15·x_C)`.
- **Constraints:**
  - `20·x_A + 15·x_B + 15·x_C ≥ 150`
  - `20·x_A + 15·x_B + 15·x_C ≤ 600`
  - `x_A, x_B, x_C` are non-negative integers.
- **No per-supplier limits** on orders or tables.

Note: Since cost is proportional to tables and Supplier C is cheapest per table, the optimum will order exactly 150 tables, all from Supplier C (10 orders of 15), for a total cost of $15,000. The upper bound of 600 is non-binding at the optimum.