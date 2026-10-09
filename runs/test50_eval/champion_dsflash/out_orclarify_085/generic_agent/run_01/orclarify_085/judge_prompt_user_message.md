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

QUESTION: Should the machine and craftsman time costs be treated as costs incurred per hour actually used (so profit = revenue − time costs), or are they fixed weekly costs that do not depend on usage?

## Turn 1 - User Simulator

They are costs incurred per hour actually used. You only pay for the time you actually use, so profit is revenue minus the time costs for the hours consumed.

## Turn 2 - Generic Agent

QUESTION: For the "at least 10 batches of X" requirement, is that a hard minimum that must always be met, or a target that can be violated at some penalty?

## Turn 2 - User Simulator

It is a hard minimum that must always be met.

## Turn 3 - Generic Agent

QUESTION: Are the batch quantities of X and Y required to be whole numbers (integer batches), or can they be fractional?

## Turn 3 - User Simulator

Fractional batches are allowed. The weekly plan can involve fractional batches when appropriate.

## Turn 4 - Generic Agent

QUESTION: Is there any upper limit on how many batches of X or Y can be produced per week (for example, a maximum demand or sales cap), or can you produce as many as the time constraints allow?

## Turn 4 - User Simulator

There is no upper limit on batches of X or Y. You can produce as many as the time constraints allow, and all produced batches will be sold.

## Turn 5 - Generic Agent

QUESTION: Should the machine and craftsman time be measured in the same units as the table (minutes per batch) with the weekly limits converted to minutes, or is there any other unit convention I should follow?

## Turn 5 - User Simulator

Use the table's units: minutes per batch. Convert the weekly limits to minutes (40 hours = 2400 minutes for machine time, 35 hours = 2100 minutes for craftsman time).

## Turn 6 - Generic Agent

QUESTION: For the profit calculation, should the time costs be computed on the total hours consumed (converting total minutes used to hours), i.e. profit = 20X + 30Y − 10·(machine minutes used/60) − 2·(craftsman minutes used/60)?

## Turn 6 - User Simulator

Yes, that is correct. Profit = 20X + 30Y − 10·(machine minutes used/60) − 2·(craftsman minutes used/60).

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** X = batches of product X per week, Y = batches of product Y per week. Both continuous (fractional allowed), both ≥ 0.
- **Objective:** Maximize profit = 20X + 30Y − 10·(machine minutes used / 60) − 2·(craftsman minutes used / 60), where machine minutes used = 13X + 19Y and craftsman minutes used = 20X + 29Y. Time costs are incurred only on time actually used.
- **Constraints:**
  - Machine time: 13X + 19Y ≤ 2400 minutes (40 hours).
  - Craftsman time: 20X + 29Y ≤ 2100 minutes (35 hours).
  - Minimum production: X ≥ 10 (hard minimum).
  - No upper limits on X or Y; all produced batches are sold.
- **Units:** minutes per batch as given; weekly limits converted to minutes.

This is a linear program with two continuous variables, a linear objective, and linear constraints. I will formulate and solve it accordingly.