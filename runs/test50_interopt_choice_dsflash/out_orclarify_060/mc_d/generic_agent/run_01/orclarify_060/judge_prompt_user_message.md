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

```json
{
  "action": "ASK",
  "question": "What should the route plan primarily minimize?",
  "options": [
    {
      "id": "A",
      "text": "Minimize total travel distance between the visited locations."
    },
    {
      "id": "B",
      "text": "Minimize total travel time between the visited locations."
    },
    {
      "id": "C",
      "text": "Minimize the number of visits or stops made."
    }
  ],
  "allow_other": true
}
```

Question:
What should the route plan primarily minimize?

Options:
A. Minimize total travel distance between the visited locations.
B. Minimize total travel time between the visited locations.
C. Minimize the number of visits or stops made.
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
  "question": "Does the sales visit route need to start and end at a fixed home or base location?",
  "options": [
    {
      "id": "A",
      "text": "Yes, the route starts and ends at a fixed home/base location."
    },
    {
      "id": "B",
      "text": "No, the route is an open path that starts at one customer and ends at another."
    },
    {
      "id": "C",
      "text": "The route starts at a fixed base but does not need to return to it."
    }
  ],
  "allow_other": true
}
```

Question:
Does the sales visit route need to start and end at a fixed home or base location?

Options:
A. Yes, the route starts and ends at a fixed home/base location.
B. No, the route is an open path that starts at one customer and ends at another.
C. The route starts at a fixed base but does not need to return to it.
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
  "question": "Is the fixed home/base location one of the 7 listed locations, or is it a separate location not shown in the table?",
  "options": [
    {
      "id": "A",
      "text": "The base is one of the 7 listed locations."
    },
    {
      "id": "B",
      "text": "The base is a separate location not shown in the table."
    },
    {
      "id": "C",
      "text": "There is no fixed base; the route can start anywhere."
    }
  ],
  "allow_other": true
}
```

Question:
Is the fixed home/base location one of the 7 listed locations, or is it a separate location not shown in the table?

Options:
A. The base is one of the 7 listed locations.
B. The base is a separate location not shown in the table.
C. There is no fixed base; the route can start anywhere.
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
  "question": "Does the fixed base location also count as one of the 7 customers to be visited, or is it an additional stop?",
  "options": [
    {
      "id": "A",
      "text": "The base is one of the 7 customers and is visited as part of the route."
    },
    {
      "id": "B",
      "text": "The base is an additional stop separate from the 7 customers."
    },
    {
      "id": "C",
      "text": "The base is only a start/end point and is not counted as a customer visit."
    }
  ],
  "allow_other": true
}
```

Question:
Does the fixed base location also count as one of the 7 customers to be visited, or is it an additional stop?

Options:
A. The base is one of the 7 customers and is visited as part of the route.
B. The base is an additional stop separate from the 7 customers.
C. The base is only a start/end point and is not counted as a customer visit.
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
  "action": "ASK",
  "question": "Are there any scheduling constraints that affect when customers can be visited?",
  "options": [
    {
      "id": "A",
      "text": "No scheduling constraints; only total travel distance matters."
    },
    {
      "id": "B",
      "text": "Each customer has a specific time window during which they must be visited."
    },
    {
      "id": "C",
      "text": "There is a working-hour limit on the total route duration."
    }
  ],
  "allow_other": true
}
```

Question:
Are there any scheduling constraints that affect when customers can be visited?

Options:
A. No scheduling constraints; only total travel distance matters.
B. Each customer has a specific time window during which they must be visited.
C. There is a working-hour limit on the total route duration.
D. None of the above — I'd like to explain in my own words.

## Turn 5 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 6 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Must the route be a single closed loop that visits each location exactly once?",
  "options": [
    {
      "id": "A",
      "text": "Yes, a single closed loop visiting each location exactly once."
    },
    {
      "id": "B",
      "text": "No, locations may be revisited if it shortens the route."
    },
    {
      "id": "C",
      "text": "The route may pass through locations without counting them as visits."
    }
  ],
  "allow_other": true
}
```

Question:
Must the route be a single closed loop that visits each location exactly once?

Options:
A. Yes, a single closed loop visiting each location exactly once.
B. No, locations may be revisited if it shortens the route.
C. The route may pass through locations without counting them as visits.
D. None of the above — I'd like to explain in my own words.

## Turn 6 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 7 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "The goal is to minimize total travel distance for a single closed-loop sales visit route that starts and ends at a fixed base, where the base is one of the 7 listed customer locations and is visited as part of the route. Each of the 7 locations must be visited exactly once, with no scheduling constraints, time windows, or working-hour limits. The distance matrix provided is symmetric and gives the travel distance between each pair of locations. Remaining minor assumption: the distance matrix values are treated as the complete and correct travel distances between locations."
}
```

The goal is to minimize total travel distance for a single closed-loop sales visit route that starts and ends at a fixed base, where the base is one of the 7 listed customer locations and is visited as part of the route. Each of the 7 locations must be visited exactly once, with no scheduling constraints, time windows, or working-hour limits. The distance matrix provided is symmetric and gives the travel distance between each pair of locations. Remaining minor assumption: the distance matrix values are treated as the complete and correct travel distances between locations.