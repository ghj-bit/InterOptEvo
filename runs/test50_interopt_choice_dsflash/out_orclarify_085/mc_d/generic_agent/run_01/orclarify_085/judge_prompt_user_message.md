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

```json
{
  "action": "ASK",
  "question": "How should profit be calculated for each product?",
  "options": [
    {
      "id": "A",
      "text": "Profit is revenue minus the machine and craftsman time costs incurred for the batches produced."
    },
    {
      "id": "B",
      "text": "Profit is revenue only; machine and craftsman time costs are not deducted."
    },
    {
      "id": "C",
      "text": "Profit is revenue minus a fixed weekly cost for machine and craftsman time, regardless of usage."
    }
  ],
  "allow_other": true
}
```

Question:
How should profit be calculated for each product?

Options:
A. Profit is revenue minus the machine and craftsman time costs incurred for the batches produced.
B. Profit is revenue only; machine and craftsman time costs are not deducted.
C. Profit is revenue minus a fixed weekly cost for machine and craftsman time, regardless of usage.
D. None of the above — I'd like to explain in my own words.

## Turn 1 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 2 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Are there any upper bounds, demand limits, or minimum production requirements for product Y?",
  "options": [
    {
      "id": "A",
      "text": "There is no upper bound or minimum requirement for product Y; it can be produced in any non-negative amount."
    },
    {
      "id": "B",
      "text": "There is a maximum demand limit for product Y that cannot be exceeded."
    },
    {
      "id": "C",
      "text": "There is a minimum production requirement for product Y that must be met."
    }
  ],
  "allow_other": true
}
```

Question:
Are there any upper bounds, demand limits, or minimum production requirements for product Y?

Options:
A. There is no upper bound or minimum requirement for product Y; it can be produced in any non-negative amount.
B. There is a maximum demand limit for product Y that cannot be exceeded.
C. There is a minimum production requirement for product Y that must be met.
D. None of the above — I'd like to explain in my own words.

## Turn 2 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 3 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Are machine and craftsman time costs charged only for time actually used, or for the full available weekly capacity?",
  "options": [
    {
      "id": "A",
      "text": "Costs are charged only for time actually used in production."
    },
    {
      "id": "B",
      "text": "Costs are charged for the full available weekly capacity regardless of usage."
    },
    {
      "id": "C",
      "text": "Costs are charged for time actually used, but unused time is also charged at a reduced rate."
    }
  ],
  "allow_other": true
}
```

Question:
Are machine and craftsman time costs charged only for time actually used, or for the full available weekly capacity?

Options:
A. Costs are charged only for time actually used in production.
B. Costs are charged for the full available weekly capacity regardless of usage.
C. Costs are charged for time actually used, but unused time is also charged at a reduced rate.
D. None of the above — I'd like to explain in my own words.

## Turn 3 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 4 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Are there any other business constraints that should be considered, such as storage limits, budget limits, or labor availability?",
  "options": [
    {
      "id": "A",
      "text": "No other constraints apply; only machine time, craftsman time, and the minimum for X matter."
    },
    {
      "id": "B",
      "text": "There is a storage limit on total batches that can be held per week."
    },
    {
      "id": "C",
      "text": "There is a budget limit on total weekly production spending."
    }
  ],
  "allow_other": true
}
```

Question:
Are there any other business constraints that should be considered, such as storage limits, budget limits, or labor availability?

Options:
A. No other constraints apply; only machine time, craftsman time, and the minimum for X matter.
B. There is a storage limit on total batches that can be held per week.
C. There is a budget limit on total weekly production spending.
D. None of the above — I'd like to explain in my own words.

## Turn 4 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 5 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "The goal is to maximize weekly profit from producing products X and Y. Profit for each product equals its revenue minus the machine and craftsman time costs actually incurred for the batches produced. Machine time is limited to 40 hours per week and craftsman time to 35 hours per week. At least 10 batches of X must be produced weekly. There are no upper bounds or minimum requirements for Y, no storage or budget limits, and no other constraints. Time costs are charged only for time actually used. The only remaining minor assumption is that production quantities are continuous (fractional batches allowed), which does not change the business structure."
}
```

The goal is to maximize weekly profit from producing products X and Y. Profit for each product equals its revenue minus the machine and craftsman time costs actually incurred for the batches produced. Machine time is limited to 40 hours per week and craftsman time to 35 hours per week. At least 10 batches of X must be produced weekly. There are no upper bounds or minimum requirements for Y, no storage or budget limits, and no other constraints. Time costs are charged only for time actually used. The only remaining minor assumption is that production quantities are continuous (fractional batches allowed), which does not change the business structure.