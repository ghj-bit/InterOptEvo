# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U2, U3
I need help planning a sales visit route and must visit 7 customers at 7 different locations.

7 customers at 7 different locations.

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | - | 86 | 49 | 57 | 31 | 69 | 50 |
| 2 |  | - | 68 | 79 | 93 | 24 | 5 |
| 3 |  |  | - | 16 | 7 | 72 | 67 |
| 4 |  |  |  | - | 90 | 69 | 1 |
| 5 |  |  |  |  | - | 86 | 59 |
| 6 |  |  |  |  |  | - | 81 |

## Problem units
- U1 (context): I need help planning a sales visit route.
- U2 (data): 7 customers at 7 different locations.
- U3 (data): |  | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | - | 86 | 49 | 57 | 31 | 69 | 50 |
| 2 |  | - | 68 | 79 | 93 | 24 | 5 |
| 3 |  |  | - | 16 | 7 | 72 | 67 |
| 4 |  |  |  | - | 90 | 69 | 1 |
| 5 |  |  |  |  | - | 86 | 59 |
| 6 |  |  |  |  |  | - | 81 |
- U4 (constraint): Must visit 7 customers at 7 different locations.
- U5 (constraint): Starting and ending at location 1.
- U6 (objective): Minimize the travel distance.

## Hidden slot scoring rules
## H1: start_end_location
- Severity: P2
- Severity reason: Without this information, the agent can still formulate a correct TSP model for minimizing total travel distance, but they might not output the tour starting at location 1 as intended. The missing constraint is a reporting detail that does not affect the core optimization result.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must inquire about the requirement for the tour to start and end at location 1, or generally ask if there is a specified depot location.
- Reference acceptable questions:
  - Does the tour have to start and end at a specific location?
  - Is location 1 the starting and ending point?
- Failure modes:
  - Assuming the tour can start and end at any location, and not specifying the start node constraint.

## H2: objective_minimize_distance
- Severity: P0
- Severity reason: Without an objective, the mathematical program cannot be formulated, as there is no criterion to optimize. The problem would be unclear and the agent would have to guess the objective, which is a critical missing piece that makes modeling impossible.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must ask about the optimization objective, specifically whether the goal is to minimize total distance or something else.
- Reference acceptable questions:
  - What is the objective? Are we minimizing total distance, time, or cost?
  - Do we want to minimize the total travel distance?
- Failure modes:
  - Assuming without clarification that the objective is to minimize distance, when it could be minimize time or cost.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the table showing travel times or distances from customer \(i\) to customer \(j\), and should the route start and end at a specified location?

## Turn 1 - User Simulator

The table shows travel distances. The route must start and end at location 1.

## Turn 2 - Generic Agent

QUESTION: Should the blank lower-triangle entries be treated as equal to the corresponding upper-triangle distances, meaning travel distance is the same in both directions?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Until internal confirmation is available, should I assume the distances are symmetric in both directions?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Do you want a provisional route based on the symmetry assumption while the distance directionality is being confirmed?

## Turn 4 - User Simulator

Yes, please provide a provisional route based on the symmetry assumption while the distance directionality is being confirmed.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding: You need a provisional round trip visiting locations 1 through 7 exactly once, starting and ending at location 1. Because directionality is still awaiting confirmation, I am treating each listed distance as symmetric.

A shortest provisional route is:

**1 → 5 → 3 → 4 → 7 → 2 → 6 → 1**

Distance:

`1–5: 31`  
`5–3: 7`  
`3–4: 16`  
`4–7: 1`  
`7–2: 5`  
`2–6: 24`  
`6–1: 69`

**Total distance: 153 units**

The reverse route, **1 → 6 → 2 → 7 → 4 → 3 → 5 → 1**, has the same total under the symmetry assumption. This route should be treated as provisional until the directional distances are confirmed.