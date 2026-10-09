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


# Atomic Question Map

Q1 (turn 1): Should the £10 per hour machine time and £2 per hour craftsman time costs be subtracted from revenue based on the minutes each batch uses, or are they fixed weekly costs that do not change with production quantities?
Q2 (turn 2): Should the weekly production quantities of X and Y be whole batches (integers), or can fractional batches be produced?
Q3 (turn 3): Is the minimum of 10 batches of product X a hard requirement that must always be met, or a soft target that can be violated if it improves profit?
Q4 (turn 4): Should the £10 per hour machine cost and £2 per hour craftsman cost be converted to per-minute costs by dividing by 60 before multiplying by the minutes each batch uses?
Q5 (turn 5): Are the 40 machine hours and 35 craftsman hours separate weekly limits, or do they together represent one combined total time limit?
Q6 (turn 6): Are there any maximum or minimum weekly production limits for product Y, such as demand caps or required minimum batches?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Should the £10 per hour machine time and £2 per hour craftsman time costs be subtracted from revenue based on the minutes each batch uses, or are they fixed weekly costs that do not change with production quantities?

## Turn 1 - User Simulator

They should be subtracted from revenue based on the time each batch actually uses. They are not fixed weekly costs.

## Turn 2 - Generic Agent

QUESTION: Should the weekly production quantities of X and Y be whole batches (integers), or can fractional batches be produced?

## Turn 2 - User Simulator

Fractional batches are allowed. The weekly plan can involve fractional batches when appropriate.

## Turn 3 - Generic Agent

QUESTION: Is the minimum of 10 batches of product X a hard requirement that must always be met, or a soft target that can be violated if it improves profit?

## Turn 3 - User Simulator

It's a hard requirement. At least 10 batches of product X must be produced each week.

## Turn 4 - Generic Agent

QUESTION: Should the £10 per hour machine cost and £2 per hour craftsman cost be converted to per-minute costs by dividing by 60 before multiplying by the minutes each batch uses?

## Turn 4 - User Simulator

Yes. Since the time per batch is given in minutes and the costs are per hour, convert the hourly costs to per-minute costs before applying them to the minutes each batch uses.

## Turn 5 - Generic Agent

QUESTION: Are the 40 machine hours and 35 craftsman hours separate weekly limits, or do they together represent one combined total time limit?

## Turn 5 - User Simulator

They are separate weekly limits. Machine time must not exceed 40 hours, and craftsman time must not exceed 35 hours.

## Turn 6 - Generic Agent

QUESTION: Are there any maximum or minimum weekly production limits for product Y, such as demand caps or required minimum batches?

## Turn 6 - User Simulator

No. There are no maximum or minimum weekly production limits for product Y.

## Turn 7 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.900

Confidence rationale: The objective, cost basis, unit conversion, variable domains, capacity constraints, and the X minimum are all confirmed. The only remaining gap is nonnegativity of production quantities, which is a standard implicit feasibility requirement for production planning and does not require business clarification.

Summary: Maximize weekly profit for products X and Y, where profit equals revenue minus machine and craftsman time costs based on minutes actually used per batch. Revenue is £20 per batch of X and £30 per batch of Y. Machine time cost is £10 per hour and craftsman time cost is £2 per hour, converted to per-minute rates. Each batch of X uses 13 machine minutes and 20 craftsman minutes; each batch of Y uses 19 machine minutes and 29 craftsman minutes. Machine time is limited to 40 hours per week and craftsman time to 35 hours per week, as separate hard constraints. At least 10 batches of X must be produced weekly as a hard requirement. Fractional batches are allowed. There are no minimum or maximum production limits for Y. Production quantities are nonnegative.