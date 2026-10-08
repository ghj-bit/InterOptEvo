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

QUESTION: Is the goal to minimize the total cost of the tables ordered, subject to the total being between 150 and 600 tables?

## Turn 1 - User Simulator

Yes, the goal is to minimize the total cost of the tables ordered, subject to the total number of tables being at least 150 and no more than 600.

## Turn 2 - Generic Agent

QUESTION: Are there any limits on how many orders can be placed with each supplier (for example, a maximum number of orders per supplier), or can I place any non-negative integer number of orders with each of the three suppliers?

## Turn 2 - User Simulator

There are no specific maximum limits on the number of orders per supplier. You can place any non-negative integer number of orders with each of the three suppliers, subject to the total table count constraints and the conditional requirements.

## Turn 3 - Generic Agent

QUESTION: You mentioned "conditional requirements" — could you describe what those conditional requirements are, since the original brief only listed the total table count range and the per-supplier order sizes?

## Turn 3 - User Simulator

Yes, there are two conditional requirements:

1. If we order tables from Supplier A, we must also order at least 30 tables from Supplier B.
2. If we place an order with Supplier B, we must also place an order with Supplier C.

## Turn 4 - Generic Agent

QUESTION: For requirement 1, if we order from Supplier A, does "at least 30 tables from Supplier B" mean the total tables from B must be at least 30 (i.e., at least 2 orders of B, since each B order is 15 tables), or does it mean at least 30 tables beyond what would otherwise be ordered from B?

## Turn 4 - User Simulator

It means the total tables from Supplier B must be at least 30.

## Turn 5 - Generic Agent

QUESTION: For requirement 2, "if we place an order with Supplier B, we must also place an order with Supplier C" — does this mean that whenever we order any tables from B (i.e., at least 1 order of B), we must place at least 1 order with C, and does the reverse also hold (i.e., if we order from C, must we also order from B)?

## Turn 5 - User Simulator

Yes, whenever we order any tables from Supplier B (at least 1 order), we must place at least 1 order with Supplier C. The reverse does not hold; we can order from Supplier C without ordering from Supplier B.

## Turn 6 - Generic Agent

QUESTION: Just to confirm the boundary: the total number of tables must be at least 150 and at most 600, inclusive of both 150 and 600 — is that correct?

## Turn 6 - User Simulator

Yes, the total number of tables must be at least 150 and at most 600, inclusive of both 150 and 600.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:**
- x_A, x_B, x_C = number of orders placed with Suppliers A, B, C respectively. Each is a non-negative integer.

**Tables per order:**
- Supplier A: 20 tables per order
- Supplier B: 15 tables per order
- Supplier C: 15 tables per order

**Objective:**
- Minimize total cost = 120·(20·x_A) + 110·(15·x_B) + 100·(15·x_C)
  - i.e., minimize 2400·x_A + 1650·x_B + 1500·x_C

**Constraints:**
1. Total tables: 150 ≤ 20·x_A + 15·x_B + 15·x_C ≤ 600
2. Conditional 1: If x_A ≥ 1, then 15·x_B ≥ 30 (i.e., x_B ≥ 2)
3. Conditional 2: If x_B ≥ 1, then x_C ≥ 1 (one-way only; ordering from C does not require ordering from B)
4. x_A, x_B, x_C ∈ ℤ₊ (non-negative integers)

**No other limits** on the number of orders per supplier.