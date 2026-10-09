# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U5, U9, U12, U2, U3, U6, U8
I need help planning the weekly production of two products, X and Y, to maximize profit. Total machine time used per week must not exceed 40 hours, total craftsman time used per week must not exceed 35 hours, and at least 10 batches of product X must be produced each week.

| Item | Machine Time (minutes) | Craftsman Time (minutes) |
| :---: | :---: | :---: |
| X | 13 | 20 |
| Y | 19 | 29 |

Machine time available per week: 40 hours. Craftsman time available per week: 35 hours.

Cost of machine time: £10 per hour. Cost of craftsman time: £2 per hour.

Revenue for product X: £20 per batch. Revenue for product Y: £30 per batch.

## Problem units
- U1 (context): I need help planning the weekly production of two products, X and Y.
- U2 (data): | Item | Machine Time (minutes) | Craftsman Time (minutes) |
| :---: | :---: | :---: |
| X | 13 | 20 |
| Y | 19 | 29 |
- U3 (data): Machine time available per week: 40 hours. Craftsman time available per week: 35 hours.
- U4 (constraint): Total machine time used per week must not exceed 40 hours.
- U5 (constraint): Total craftsman time used per week must not exceed 35 hours.
- U6 (data): Cost of machine time: £10 per hour. Cost of craftsman time: £2 per hour.
- U7 (assumption): Idle time for machines and craftsmen incurs no cost.
- U8 (data): Revenue for product X: £20 per batch. Revenue for product Y: £30 per batch.
- U9 (constraint): At least 10 batches of product X must be produced each week.
- U10 (assumption): Production batches may be fractional.
- U11 (assumption): All produced batches are sold.
- U12 (objective): Maximize profit.

## Hidden slot scoring rules
## H1: idle_time_no_cost
- Severity: P2
- Severity reason: Without this clarification, the agent might incorrectly assume idle time incurs a cost, adding an unnecessary term to the objective or overcomplicating the model. Clarifying that idle time costs nothing keeps the profit calculation simple and correct.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must inquire about whether idle (unused) time for machines or craftsmen incurs a cost.
- Reference acceptable questions:
  - Do we pay for unused machine or craftsman time?
  - Is there any cost for idle time?
- Failure modes:
  - Assuming idle time incurs a cost and subtracting it from profit
  - Assuming unused capacity is paid for

## H2: fractional_batches_allowed
- Severity: P2
- Severity reason: Batch divisibility determines whether the problem is linear or mixed-integer. Without it, the agent might unnecessarily impose integer constraints. The omission still allows a coherent model, but clarifying the allowance of fractional batches ensures a pure LP formulation as intended.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must ask about whether the production quantities can be fractional or must be integer.
- Reference acceptable questions:
  - Can we produce fractional batches?
  - Do the batch numbers have to be whole numbers?
- Failure modes:
  - Assuming batches must be integer, leading to a mixed-integer linear programming model
  - Adding integrality constraints unnecessarily

## H3: all_batches_sold
- Severity: P2
- Severity reason: The assumption that all produced batches are sold directly affects revenue calculation and whether demand constraints exist. Without this, the agent might incorrectly add demand limits or inventory considerations, making the model more complex than intended. Clarifying keeps the model focused on pure production‑profit maximization.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask whether all produced batches are guaranteed to be sold, or if there is a demand constraint.
- Reference acceptable questions:
  - Are all the batches we produce actually sold?
  - Is there any limit on how many batches we can sell?
- Failure modes:
  - Assuming a demand cap on product X or Y, thereby adding unnecessary constraints
  - Introducing inventory or backorder variables


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the objective to maximize weekly profit, where profit equals total revenue from batches of X and Y minus the cost of the machine and craftsman time actually used that week?

## Turn 1 - User Simulator

Yes, that is correct.

## Turn 2 - Generic Agent

QUESTION: Are the machine and craftsman time costs charged only on the time actually used by production, or are they fixed weekly charges for the full 40 and 35 hours regardless of usage?

## Turn 2 - User Simulator

The costs are charged only on the time actually used by production.

## Turn 3 - Generic Agent

QUESTION: Is there any upper limit on how many batches of product Y can be produced per week, or can Y be produced in any non-negative quantity?

## Turn 3 - User Simulator

There is no upper limit on product Y. It can be produced in any non-negative quantity, subject to the machine and craftsman time constraints.

## Turn 4 - Generic Agent

QUESTION: Must the number of batches of X and Y be whole numbers, or can they be fractional?

## Turn 4 - User Simulator

Fractional batches are allowed.

## Turn 5 - Generic Agent

QUESTION: Is the "at least 10 batches of X" a hard requirement that must always hold, or can it be relaxed (e.g., with a penalty) if the time constraints make it infeasible?

## Turn 5 - User Simulator

It is a hard requirement. At least 10 batches of product X must be produced each week.

## Turn 6 - Generic Agent

QUESTION: Are the 40 machine hours and 35 craftsman hours the only resource limits, or are there any other constraints (e.g., demand caps, minimum production of Y, or other resources) I should include?

## Turn 6 - User Simulator

The 40 machine hours and 35 craftsman hours are the only resource limits. There are no other constraints such as demand caps or minimum production of Y.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** x = batches of product X per week, y = batches of product Y per week. Both are continuous (fractional allowed), non-negative.
- **Objective:** Maximize weekly profit = total revenue − cost of time actually used.
  - Revenue: £20 per batch of X, £30 per batch of Y.
  - Machine time cost: £10 per hour used; craftsman time cost: £2 per hour used (charged only on time actually used, not on the full available hours).
- **Constraints:**
  - Machine time: 13 minutes per batch of X + 19 minutes per batch of Y ≤ 40 hours (2400 minutes) per week.
  - Craftsman time: 20 minutes per batch of X + 29 minutes per batch of Y ≤ 35 hours (2100 minutes) per week.
  - Minimum X: x ≥ 10 (hard requirement).
  - No upper limit on Y; no other constraints (no demand caps, no minimum Y, no other resources).

I will now formulate the linear program.