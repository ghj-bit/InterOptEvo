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


# Atomic Question Map

Q1 (turn 1): Does the sales visit route need to start and end at a specific depot or home base, or can it start and end at any of the 7 customer locations?
Q2 (turn 2): Should the route be planned to minimize total travel distance, or is there another objective such as minimizing travel time or cost?
Q3 (turn 3): Must the route visit all 7 customers exactly once, or can some customers be skipped or visited more than once?
Q4 (turn 4): Are the travel distances symmetric, meaning the distance from location A to location B is the same as from B to A?
Q5 (turn 4): Can you provide the missing distances for all pairs?
Q6 (turn 5): If the missing distances cannot be confirmed as symmetric, should the route be planned using only the provided one-directional distances as if they were symmetric, or should planning wait until the missing pairs are confirmed?
Q7 (turn 6): Can you provide the missing distances for all pairs?
Q8 (turn 6): Confirm whether the distance from location A to location B equals the distance from location B to location A?
Q9 (turn 7): Since the missing distances and symmetry cannot be confirmed now, should I pause the modeling effort until your internal team provides the complete distance data?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Does the sales visit route need to start and end at a specific depot or home base, or can it start and end at any of the 7 customer locations?

## Turn 1 - User Simulator

It needs to start and end at location 1.

## Turn 2 - Generic Agent

QUESTION: Should the route be planned to minimize total travel distance, or is there another objective such as minimizing travel time or cost?

## Turn 2 - User Simulator

It should be planned to minimize total travel distance.

## Turn 3 - Generic Agent

QUESTION: Must the route visit all 7 customers exactly once, or can some customers be skipped or visited more than once?

## Turn 3 - User Simulator

All 7 customers must be visited, each at their own location.

## Turn 4 - Generic Agent

QUESTION: Are the travel distances symmetric, meaning the distance from location A to location B is the same as from B to A, and can you provide the missing distances for all pairs?

## Turn 4 - User Simulator

I don’t have confirmation on whether the distances are symmetric. The table you have is the distance information I can provide; the missing pairs still need internal confirmation.

## Turn 5 - Generic Agent

QUESTION: If the missing distances cannot be confirmed as symmetric, should the route be planned using only the provided one-directional distances as if they were symmetric, or should planning wait until the missing pairs are confirmed?

## Turn 5 - User Simulator

Planning should wait until the missing pairs are confirmed.

## Turn 6 - Generic Agent

QUESTION: Can you provide the missing distances for all pairs and confirm whether the distance from location A to location B equals the distance from location B to location A?

## Turn 6 - User Simulator

I can’t provide the missing distances, and I can’t confirm that the distance from A to B equals the distance from B to A. That still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the missing distances and symmetry cannot be confirmed now, should I pause the modeling effort until your internal team provides the complete distance data?

## Turn 7 - User Simulator

Yes, please pause the modeling effort until the complete distance data is provided.

## Turn 8 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.000

Confidence rationale: The modeling effort has been explicitly paused by the user until the missing pairwise distances and symmetry status are confirmed internally. The distance matrix is incomplete and symmetry is unconfirmed, so the objective (total travel distance) cannot be evaluated and no unique route optimization formulation can be built at this time.

Summary: The problem is a sales visit routing problem: start and end at location 1, visit all 7 customers exactly once at their own locations, and minimize total travel distance. However, the provided distance matrix is incomplete and symmetry is unconfirmed. Per the user's instruction, modeling is paused until the complete distance data and symmetry confirmation are provided.