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

QUESTION: The distance matrix is not symmetric — for example, city 1 to city 4 is 12 but city 4 to city 1 is 15. Should the route be planned as a directed tour (respecting the direction of each leg), or should the two directions be treated as the same distance?

## Turn 1 - User Simulator

The route should be planned as a directed tour, respecting the direction of each leg. The distances are not the same in both directions, so the specific direction of travel matters for the total distance.

## Turn 2 - Generic Agent

QUESTION: Should the salesman visit every one of the four cities exactly once before returning to the start, or is it acceptable to skip some cities?

## Turn 2 - User Simulator

The salesman must visit every one of the four cities exactly once before returning to the start. Skipping cities is not acceptable.

## Turn 3 - Generic Agent

QUESTION: Is the starting city fixed (for example, city 1), or may the tour start from any city?

## Turn 3 - User Simulator

The starting city is not fixed to a specific city like city 1. The problem states he departs from "a certain city," but does not specify which one.

## Turn 4 - Generic Agent

QUESTION: Since the start city is not fixed, should the model choose the starting city that yields the shortest total tour, or should it be told a specific start city to use?

## Turn 4 - User Simulator

The model should choose the starting city that yields the shortest total tour.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Problem type:** Directed Traveling Salesman Problem (asymmetric TSP), because the distance matrix is not symmetric (e.g., 1→4 = 12 but 4→1 = 15), so leg direction matters.
- **Coverage:** The salesman must visit all four cities exactly once and return to the start — a complete Hamiltonian cycle, no skipping.
- **Start city:** Not fixed; the model is free to choose whichever starting city yields the shortest total tour.
- **Objective:** Minimize total travel distance of the closed directed tour.

**Model formulation:**

Sets: cities \(i, j \in \{1,2,3,4\}\).

Parameters: directed distance \(d_{ij}\) from the matrix (with \(d_{ii}=0\)).

Decision variables:
- \(x_{ij} \in \{0,1\}\): 1 if the tour travels directly from city \(i\) to city \(j\), else 0.
- \(u_i\): continuous ordering/position variable for subtour elimination (MTZ), \(i \in \{1,2,3,4\}\).

Objective:
\[
\min \sum_{i}\sum_{j \neq i} d_{ij}\, x_{ij}
\]

Constraints:
1. Each city has exactly one outgoing leg: \(\sum_{j \neq i} x_{ij} = 1 \quad \forall i\)
2. Each city has exactly one incoming leg: \(\sum_{i \neq j} x_{ij} = 1 \quad \forall j\)
3. Subtour elimination (MTZ): \(u_i - u_j + n\, x_{ij} \le n-1\) for \(i \neq j\), with \(n=4\), and \(u_i\) bounded (e.g., \(1 \le u_i \le n\)).
4. Binary and continuous domains as above.

Because the start city is free, no city is pinned as the origin; the cycle is chosen endogenously by the optimization.