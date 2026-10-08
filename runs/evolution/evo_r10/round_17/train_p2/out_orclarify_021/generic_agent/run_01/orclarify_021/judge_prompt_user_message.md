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

QUESTION: What is the objective of this plan — are you minimizing total cost, maximizing total tables, or something else (e.g., meeting a target number of tables at minimum cost)?

## Turn 1 - User Simulator

We want to minimize the total cost of the order for the dining tables.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum or maximum limits on how many orders can be placed with each individual supplier (A, B, and C), or is the only limit the total table count between 150 and 600?

## Turn 2 - User Simulator

The only limit is the total table count between 150 and 600.

## Turn 3 - Generic Agent

QUESTION: Is there any requirement that at least one order must be placed with each of the three suppliers, or is it acceptable to place zero orders with one or more of them?

## Turn 3 - User Simulator

It is acceptable to place zero orders with one or more of them.

## Turn 4 - Generic Agent

QUESTION: Is there any other cost or constraint I should account for — such as a fixed setup/transport fee per supplier used, a maximum budget, or a requirement to hit an exact table count — or is the model simply: choose non-negative integer orders from A, B, C, total tables between 150 and 600, minimize total cost?

## Turn 4 - User Simulator

There are two additional constraints:

1. If we decide to order from Supplier A, we must also order at least 30 tables from Supplier B.
2. If we place an order with Supplier B, we must also place an order with Supplier C.

## Turn 5 - Generic Agent

QUESTION: For constraint 1, if we order from Supplier A, does "at least 30 tables from Supplier B" mean at least 2 orders from B (since each B order is 15 tables), and does this requirement apply only when we place at least one order with A?

## Turn 5 - User Simulator

Yes, "at least 30 tables from Supplier B" means at least 2 orders from B, and this requirement applies only when we place at least one order with A.

## Turn 6 - Generic Agent

QUESTION: For constraint 2, does "if we place an order with Supplier B, we must also place an order with Supplier C" mean that placing at least one order with B requires at least one order with C (with no minimum number of C orders specified)?

## Turn 6 - User Simulator

Yes, placing at least one order with B requires at least one order with C, with no minimum number of C orders specified.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:**
- x_A, x_B, x_C = number of orders placed with Suppliers A, B, C respectively
- All are non-negative integers (0, 1, 2, ...)

**Objective:**
- Minimize total cost = 120·(20·x_A) + 110·(15·x_B) + 100·(15·x_C)
- i.e., minimize 2400·x_A + 1650·x_B + 1500·x_C

**Constraints:**
1. Total tables: 150 ≤ 20·x_A + 15·x_B + 15·x_C ≤ 600
2. If x_A ≥ 1, then x_B ≥ 2 (i.e., at least 30 tables from B)
3. If x_B ≥ 1, then x_C ≥ 1 (i.e., at least one order from C)
4. No per-supplier minimum or maximum beyond the above; zero orders with any supplier are allowed.

**No other costs, budgets, or exact-target requirements.**