# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U7, U2
I need help planning a route for a traveling salesman to visit multiple cities, with the goal to minimize the total distance, given that he must return to the original starting city.

| City |    1    |    2    |    3    |    4    |
| ---- | ------ | ------ | ------ | ------ |
| 1    | 0    | 10   | 20   | 12   |
| 2    | 10   | 0    | 5    | 10   |
| 3    | 20   | 5    | 0    | 8    |
| 4    | 15   | 12   | 8    | 0    |

## Problem units
- U1 (context): I need help planning a route for a traveling salesman to visit multiple cities.
- U2 (data): | City |    1    |    2    |    3    |    4    |
| ---- | ------ | ------ | ------ | ------ |
| 1    | 0    | 10   | 20   | 12   |
| 2    | 10   | 0    | 5    | 10   |
| 3    | 20   | 5    | 0    | 8    |
| 4    | 15   | 12   | 8    | 0    |
- U3 (objective): Minimize the total distance.
- U4 (constraint): The traveling salesman departs from a certain city.
- U5 (constraint): He must visit two other cities to sell merchandise.
- U6 (constraint): He must visit each city exactly once.
- U7 (constraint): He must return to the original starting city.

## Hidden slot scoring rules
## H1: missing_starting_city
- Severity: P1
- Severity reason: Without knowing the specific starting city, the modeling agent cannot determine the exact route, even though the optimal tour distance is independent of starting point in a symmetric TSP. However, the problem explicitly asks for a route, so the starting city is important to specify.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must ask for the identity of the starting city or whether the starting city is given.
- Reference acceptable questions:
  - Which city does the salesman start from?
  - Is the starting city specified?
- Failure modes:
  - Assuming the starting city is city 1 by default
  - Assuming the starting city can be chosen arbitrarily

## H2: number_of_cities_to_visit
- Severity: P0
- Severity reason: The phrase 'visit two other cities' directly conflicts with the requirement to 'visit each city exactly once' when there are four cities. Without clarification, the constraint set is contradictory, making a valid model impossible.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must address the discrepancy between 'two other cities' and 'each city exactly once' or ask for the total number of cities to be visited.
- Reference acceptable questions:
  - Does the salesman need to visit all four cities exactly once, or only two other cities besides the starting city?
  - The problem mentions visiting two other cities but also visiting each city exactly once; could you clarify how many cities he actually visits?
- Failure modes:
  - Assuming only three cities are involved (start + two selling cities), ignoring other cities
  - Assuming all four cities must be visited despite the mention of only two selling cities, rewriting the problem
  - Supplying a model that is internally inconsistent

## H3: visit_each_city_exactly_once
- Severity: P2
- Severity reason: The requirement that each city is visited exactly once is a standard TSP constraint. While it is essential, the typical interpretation is clear and unlikely to be misunderstood, so clarifying it is not critical for a coherent model.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must ask for clarification on whether the starting city counts as visited twice or whether the 'exactly once' applies strictly to all cities excluding the final return.
- Reference acceptable questions:
  - Does 'each city exactly once' include the starting city, meaning we cannot visit it again until the return?
  - When you say 'visit each city exactly once', does that refer to the entire journey including the start and end?
- Failure modes:
  - Assuming the starting city can be visited twice during the tour, leading to an incorrect interpretation
  - Modeling without considering that each city must appear exactly once in the tour sequence (except the return)


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the distance matrix symmetric (i.e., the distance from city i to city j equals the distance from city j to city i), or should I treat it as directed/asymmetric?

## Turn 1 - User Simulator

The distance matrix is not symmetric. For example, the distance from city 1 to city 4 is 12, but the distance from city 4 to city 1 is 15. You should treat it as directed/asymmetric.

## Turn 2 - Generic Agent

QUESTION: Is the salesman's starting city fixed (for example, city 1), or can the route start from any city?

## Turn 2 - User Simulator

The starting city is not fixed to a specific city like city 1. The problem states he departs from "a certain city," but does not specify which one.

## Turn 3 - Generic Agent

QUESTION: Since the starting city is not fixed, should the objective be to find the minimum-cost directed Hamiltonian cycle over all possible starting cities (i.e., the best closed tour regardless of where it starts)?

## Turn 3 - User Simulator

Yes, the goal is to find the best closed tour regardless of where it starts.

## Turn 4 - Generic Agent

QUESTION: Are there any constraints on the route beyond visiting each city exactly once and returning to the start, such as time windows, maximum route length, or forbidden city pairs?

## Turn 4 - User Simulator

No, there are no additional constraints beyond visiting each city exactly once and returning to the starting city.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:
- Problem: Asymmetric (directed) Traveling Salesman Problem (ATSP) with 4 cities.
- Objective: Minimize total route distance.
- Decision: Find a directed Hamiltonian cycle (closed tour) that visits each of the 4 cities exactly once and returns to the starting city.
- Starting city: Not fixed — the best closed tour is sought regardless of which city it starts from (equivalently, the best directed cycle over all 4 cities).
- Distance matrix (directed, row = from, column = to):
  - 1→2: 10, 1→3: 20, 1→4: 12
  - 2→1: 10, 2→3: 5, 2→4: 10
  - 3→1: 20, 3→2: 5, 3→4: 8
  - 4→1: 15, 4→2: 12, 4→3: 8
- Constraints: Each city visited exactly once; route is a single closed cycle; no time windows, no max length, no forbidden pairs.
- Note: Since the tour is a closed cycle, the choice of "starting city" does not change the set of feasible tours or the objective value — the optimal directed cycle is the same regardless of where it is read from.