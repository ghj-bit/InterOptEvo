# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U2, U3, U4
I need help planning the distribution of coal from two coal yards to three residential areas, and the total coal supplied to each residential area must meet its monthly demand.

Three residential areas require 55 tons, 75 tons, and 50 tons of coal per month, respectively.

Coal yard A receives no less than 80 tons of coal per month; coal yard B receives no less than 100 tons of coal per month.

Distances (in km):
|               | Residential Area 1 | Residential Area 2 | Residential Area 3 |
|---------------|--------------------|--------------------|--------------------|
| Coal Yard A   | 10                 | 5                  | 6                  |
| Coal Yard B   | 4                  | 8                  | 15                 |

## Problem units
- U1 (context): I need help planning the distribution of coal from two coal yards to three residential areas.
- U2 (data): Three residential areas require 55 tons, 75 tons, and 50 tons of coal per month, respectively.
- U3 (data): Coal yard A receives no less than 80 tons of coal per month; coal yard B receives no less than 100 tons of coal per month.
- U4 (data): Distances (in km):
|               | Residential Area 1 | Residential Area 2 | Residential Area 3 |
|---------------|--------------------|--------------------|--------------------|
| Coal Yard A   | 10                 | 5                  | 6                  |
| Coal Yard B   | 4                  | 8                  | 15                 |
- U5 (objective): Minimize the ton-kilometers of transportation.
- U6 (constraint): The amount of coal distributed from each coal yard must not exceed the amount of coal it receives per month.
- U7 (constraint): The total coal supplied to each residential area must meet its monthly demand.

## Hidden slot scoring rules
## H1: unknown_objective
- Severity: P0
- Severity reason: Without the objective, the optimization problem is undefined; a responsible modeling agent cannot determine what to minimize, making model formulation impossible.
- Problem unit ID: U5
- Semantic hit rule: The agent’s question must inquire about the optimization goal, specifically asking what metric to minimize (e.g., total ton-kilometers, total cost, or total weighted distance).
- Reference acceptable questions:
  - What is the objective we are trying to minimize?
  - Should we minimize total ton-kilometers traveled?
- Failure modes:
  - Assuming the goal is to minimize total unweighted distance traveled (ignoring tonnage).
  - Assuming the goal is to minimize total cost based on some implicit rate.

## H2: undisclosed_distribution_limit
- Severity: P1
- Severity reason: Without this constraint, the model could either assume unbounded supply or fix supplies at the given minimal amounts, but the precise condition that distribution cannot exceed what each yard actually receives is a key business rule that may change the feasible region and optimal solution.
- Problem unit ID: U6
- Semantic hit rule: The agent’s question must explicitly ask about the upper bound on outgoing coal from each yard, or whether the distribution amount can exceed the amount the yard receives.
- Reference acceptable questions:
  - Is there a limit on how much coal each yard can send out?
  - Can a coal yard distribute more coal than it receives?
- Failure modes:
  - Assuming the yards can supply any amount without limit.
  - Assuming the supply at each yard is exactly 80 and 100 tons with no dependence on the actual received quantity.


# Full Transcript

## Turn 1 - Generic Agent

```json
{
  "action": "ASK",
  "question": "What should the distribution plan primarily aim to achieve?",
  "options": [
    {
      "id": "A",
      "text": "Minimize total transport distance or ton-kilometers."
    },
    {
      "id": "B",
      "text": "Minimize total transport cost based on distance and quantity."
    },
    {
      "id": "C",
      "text": "Just find any feasible plan that satisfies all demands and yard minimums."
    }
  ],
  "allow_other": true
}
```

Question:
What should the distribution plan primarily aim to achieve?

Options:
A. Minimize total transport distance or ton-kilometers.
B. Minimize total transport cost based on distance and quantity.
C. Just find any feasible plan that satisfies all demands and yard minimums.
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
  "question": "How should the coal received by each yard be treated in the plan?",
  "options": [
    {
      "id": "A",
      "text": "The amounts received by the yards are fixed inputs already decided outside this plan."
    },
    {
      "id": "B",
      "text": "The amounts received by the yards are decisions to be chosen as part of this plan."
    },
    {
      "id": "C",
      "text": "The amounts received are fixed at the stated minimums, with no extra coal available."
    }
  ],
  "allow_other": true
}
```

Question:
How should the coal received by each yard be treated in the plan?

Options:
A. The amounts received by the yards are fixed inputs already decided outside this plan.
B. The amounts received by the yards are decisions to be chosen as part of this plan.
C. The amounts received are fixed at the stated minimums, with no extra coal available.
D. None of the above — I'd like to explain in my own words.

## Turn 2 - User Simulator

```json
{
  "choice": "D",
  "comment": "The yards receive no less than the stated amounts, so the received amounts are not fixed at exactly those minimums; a yard could receive more, and its total deliveries are capped by whatever it actually receives."
}
```

Business user response: none of the offered options match. The yards receive no less than the stated amounts, so the received amounts are not fixed at exactly those minimums; a yard could receive more, and its total deliveries are capped by whatever it actually receives.

## Turn 3 - Generic Agent

```json
{
  "action": "ASK",
  "question": "How should the total amount of coal received across both yards relate to the total residential demand?",
  "options": [
    {
      "id": "A",
      "text": "Total received coal must exactly equal total residential demand."
    },
    {
      "id": "B",
      "text": "Total received coal may exceed total residential demand, with excess left unused."
    },
    {
      "id": "C",
      "text": "Total received coal is fixed at the stated minimums regardless of demand."
    }
  ],
  "allow_other": true
}
```

Question:
How should the total amount of coal received across both yards relate to the total residential demand?

Options:
A. Total received coal must exactly equal total residential demand.
B. Total received coal may exceed total residential demand, with excess left unused.
C. Total received coal is fixed at the stated minimums regardless of demand.
D. None of the above — I'd like to explain in my own words.