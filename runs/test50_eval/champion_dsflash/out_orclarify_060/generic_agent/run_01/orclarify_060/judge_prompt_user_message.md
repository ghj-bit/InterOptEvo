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

QUESTION: Does the route need to start and end at a specific home base (depot), or is it a pure tour among the 7 customers with no fixed start/end?

## Turn 1 - User Simulator

The route must start and end at location 1.

## Turn 2 - Generic Agent

QUESTION: Should the route visit each of the 7 customers exactly once (a Hamiltonian cycle), or may some customers be skipped?

## Turn 2 - User Simulator

The route must visit all 7 customers.

## Turn 3 - Generic Agent

QUESTION: Is the goal to minimize total travel distance, or is there another objective (e.g., minimize time, or balance the route)?

## Turn 3 - User Simulator

The goal is to minimize the total travel distance.

## Turn 4 - Generic Agent

QUESTION: The distance matrix is given only for the upper triangle (rows 1–6). Should I treat the matrix as symmetric, i.e., the distance from i to j equals the distance from j to i?

## Turn 4 - User Simulator

I need to confirm internally whether the distance matrix is symmetric.

## Turn 5 - Generic Agent

QUESTION: For the missing entries in the lower triangle, if the matrix turns out not to be symmetric, do you have the reverse-direction distances available, or should I assume symmetry as the only option?

## Turn 5 - User Simulator

I need to confirm internally whether the reverse-direction distances are available.

## Turn 6 - Generic Agent

QUESTION: Should the route be a single continuous loop (one vehicle, one closed tour), or could it involve multiple vehicles/routes?

## Turn 6 - User Simulator

The route is a single continuous loop with one vehicle.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:
- 7 customers at 7 distinct locations, all must be visited exactly once.
- Route is a single closed tour (one vehicle, one continuous loop) that starts and ends at location 1.
- Objective: minimize total travel distance.
- Distance matrix: only the upper triangle (rows 1–6) is provided. Symmetry is unconfirmed (client is checking internally); reverse-direction distances are also unconfirmed. I will model with the symmetric assumption, using the given entries for both directions, and note this as the key assumption to revisit if the client's internal confirmation contradicts it.

Model: a Traveling Salesman Problem (TSP) on nodes {1,...,7} with node 1 as the fixed depot/start-end, minimizing the sum of arc distances over a Hamiltonian cycle, using the provided distances symmetrically.