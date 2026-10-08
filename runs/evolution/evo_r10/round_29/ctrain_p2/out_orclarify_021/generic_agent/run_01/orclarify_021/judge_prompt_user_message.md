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

QUESTION: What is the goal of this plan — minimize the total cost of the tables ordered, or is there another objective (such as meeting a specific target number of tables, or balancing orders across suppliers)?

## Turn 1 - User Simulator

The goal is to minimize the total cost of the tables ordered.

## Turn 2 - Generic Agent

QUESTION: Are there any limits on how many orders can be placed with each supplier (for example, a maximum number of orders per supplier, or a requirement to use at least one of each supplier)?

## Turn 2 - User Simulator

No, there are no limits on the number of orders per supplier, and there is no requirement to use at least one of each supplier.

## Turn 3 - Generic Agent

QUESTION: The total number of tables must be at least 150 and no more than 600 — should the model treat 150 as a hard minimum that must be met (i.e., order at least 150 tables), or is 150 just a lower bound that the total happens to fall above?

## Turn 3 - User Simulator

150 is a hard minimum that must be met.

## Turn 4 - Generic Agent

QUESTION: Since each order comes in a fixed bundle (20, 15, or 15 tables), the total number of tables will be a specific sum of those bundles — is it acceptable for the total to exceed 150 (for example, 165 tables) as long as it is at least 150 and at most 600, or must the total be exactly 150?

## Turn 4 - User Simulator

It is acceptable for the total to exceed 150, as long as it is at least 150 and at most 600.

## Turn 5 - Generic Agent

QUESTION: Is there any other cost or constraint I should account for besides the per-table cost (for example, a fixed cost per order, a shipping fee, or a budget cap on total spending)?

## Turn 5 - User Simulator

No, there are no other costs or constraints besides the per-table cost.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** Number of orders placed with each supplier — A, B, C — each a non-negative integer.
- **Tables per order:** Supplier A = 20 tables, Supplier B = 15 tables, Supplier C = 15 tables.
- **Total tables:** 20·A + 15·B + 15·C, which must be at least 150 (hard minimum) and at most 600.
- **Objective:** Minimize total cost = 120·(20·A) + 110·(15·B) + 100·(15·C), i.e., minimize the per-table cost times the number of tables from each supplier.
- **No other constraints:** No per-supplier order limits, no requirement to use all three suppliers, no fixed per-order cost, no budget cap.

The model is a small integer linear program: minimize 2400·A + 1650·B + 1500·C subject to 150 ≤ 20·A + 15·B + 15·C ≤ 600, with A, B, C non-negative integers.