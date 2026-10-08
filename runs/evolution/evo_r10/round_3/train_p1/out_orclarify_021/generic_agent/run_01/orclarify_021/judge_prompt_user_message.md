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

QUESTION: What is the objective of this plan — are you minimizing total cost, maximizing total tables, or something else (and if minimizing cost, is the 150-table minimum a hard requirement you must meet)?

## Turn 1 - User Simulator

The objective is to minimize the total cost of the order. The 150-table minimum is a hard requirement that must be met.

## Turn 2 - Generic Agent

QUESTION: Is the 600-table maximum a hard upper bound on the total number of tables ordered, or is it just a loose cap that the cost-minimizing solution would naturally stay under?

## Turn 2 - User Simulator

The 600-table maximum is a hard upper bound on the total number of tables ordered.

## Turn 3 - Generic Agent

QUESTION: Are there any per-supplier limits on how many orders you can place with each supplier (e.g., a maximum number of orders or a maximum number of tables from A, B, or C individually), or can you order any integer number of orders from each?

## Turn 3 - User Simulator

There are no per-supplier limits on the number of orders or tables. You can order any integer number of orders from each supplier, subject to the total table count staying between 150 and 600.

## Turn 4 - Generic Agent

QUESTION: Is there any requirement that you must order from all three suppliers (i.e., at least one order from each), or is it acceptable to order from only one or two of them?

## Turn 4 - User Simulator

It is acceptable to order from only one or two suppliers. There is no requirement to order from all three.

## Turn 5 - Generic Agent

QUESTION: Is there any other constraint or requirement I should know about — for example, a budget cap, a minimum number of tables from a specific supplier, or a requirement that the total number of tables be exactly some value — or is the problem fully described by: integer orders from each supplier, total tables between 150 and 600, and minimizing total cost?

## Turn 5 - User Simulator

There are two additional requirements:
1. If we order tables from Supplier A, we must also order at least 30 tables from Supplier B.
2. If we place an order with Supplier B, we must also place an order with Supplier C.

## Turn 6 - Generic Agent

QUESTION: For requirement 1, if you order from Supplier A, the "at least 30 tables from Supplier B" — does this mean the total tables from B must be at least 30 (which, since B comes in 15-table orders, means at least 2 orders from B), or does it mean at least 30 tables *in addition to* whatever B orders are already required by other rules?

## Turn 6 - User Simulator

It means the total tables from Supplier B must be at least 30.

## Turn 7 - Generic Agent

QUESTION: For requirement 2, "if we place an order with Supplier B, we must also place an order with Supplier C" — does this mean at least one order from C (i.e., at least 15 tables from C), or is there a specific minimum number of tables from C required?

## Turn 7 - User Simulator

It means at least one order from Supplier C, which is at least 15 tables.

## Turn 8 - Generic Agent

QUESTION: Are the two conditional rules one-way only as stated (i.e., ordering from B does NOT force ordering from A, and ordering from C does NOT force ordering from B), or are they two-way (i.e., if you order from B you must order from C, AND if you order from C you must order from B)?

## Turn 8 - User Simulator

The rules are one-way only as stated. Ordering from B does not force ordering from A, and ordering from C does not force ordering from B.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:**
- x_A, x_B, x_C: non-negative integers representing the number of orders placed with Suppliers A, B, and C respectively.

**Tables per order:**
- Supplier A: 20 tables per order
- Supplier B: 15 tables per order
- Supplier C: 15 tables per order

**Objective:**
- Minimize total cost = 120·(20·x_A) + 110·(15·x_B) + 100·(15·x_C) = 2400·x_A + 1650·x_B + 1500·x_C

**Constraints:**
1. Total tables: 150 ≤ 20·x_A + 15·x_B + 15·x_C ≤ 600
2. If x_A ≥ 1, then 15·x_B ≥ 30 (i.e., x_B ≥ 2)
3. If x_B ≥ 1, then x_C ≥ 1
4. x_A, x_B, x_C are non-negative integers
5. No per-supplier upper limits
6. No requirement to use all three suppliers
7. Both conditional rules are one-way only