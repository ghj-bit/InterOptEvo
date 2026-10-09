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

QUESTION: Must the weekly quantities of products X and Y be whole batches, or may fractional batches be produced?

## Turn 1 - User Simulator

Fractional batches are allowed. The weekly plan can involve fractional batches when appropriate.

## Turn 2 - Generic Agent

QUESTION: Are there any upper limits on the weekly demand for products X or Y?

## Turn 2 - User Simulator

There are no upper limits on the weekly demand for products X or Y. All batches we produce will be sold.

## Turn 3 - Generic Agent

READY_TO_MODEL

Confirmed understanding: Choose nonnegative weekly quantities of products X and Y, with fractional batches allowed. All production can be sold, so there are no demand limits. The objective is to maximize profit after variable machine and craftsman costs.

Let:

- `x` = batches of X
- `y` = batches of Y

Profit per batch:

- X: `£20 - (13/60 × £10) - (20/60 × £2) = £17.1667`
- Y: `£30 - (19/60 × £10) - (29/60 × £2) = £25.8667`

Constraints:

- Machine time: `13x + 19y ≤ 2,400` minutes
- Craftsman time: `20x + 29y ≤ 2,100` minutes
- Minimum X production: `x ≥ 10`
- `x, y ≥ 0`

Because product Y generates more profit per craftsman minute, and craftsman time is the binding resource, the optimal plan produces the minimum required amount of X and uses the remaining craftsman capacity for Y:

- `x = 10`
- `y = (2,100 - 20×10) / 29 = 65.5172`

**Optimal weekly production plan**

| Product | Batches |
|---|---:|
| X | 10 |
| Y | 65.517 |

Resource usage:

- Machine time: `1,374.83` minutes = `22.91` hours of 40
- Craftsman time: `2,100` minutes = `35` hours of 35

Financial result:

- Revenue: approximately `£2,165.52`
- Machine cost: approximately `£229.14`
- Craftsman cost: `£70.00`
- **Maximum weekly profit: approximately £1,866.38**

The machine-time limit has unused capacity; craftsman time is fully utilized.