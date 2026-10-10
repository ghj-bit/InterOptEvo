# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U7, U8, U9, U10, U2, U3, U4
I need help creating a personnel arrangement plan for Jieli Company to assign recruited professionals to branches in Donghai City and Nanjiang City, where a person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4, and the total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4. The objectives are to have 8000 recruited personnel meet their preferred specialty, have 8000 meet their preferred city, and determine the minimum number of recruited personnel who cannot be assigned to their preferred city.

Table 4-3
| Branch Location | Specialty | Demand |
|-----------------|-----------|--------|
| Donghai City    | 1         | 1000   |
| Donghai City    | 2         | 2000   |
| Donghai City    | 3         | 1500   |
| Nanjiang City   | 1         | 2000   |
| Nanjiang City   | 2         | 1000   |
| Nanjiang City   | 3         | 1000   |

Table 4-4

| Type | Number of People | Suitable Specialty | Preferred Specialty | Preferred City |
|------|------------------|--------------------|---------------------|----------------|
| 1    | 1500             | 1,2                | 1                   | Donghai        |
| 2    | 1500             | 2,3                | 2                   | Donghai        |
| 3    | 1500             | 1,3                | 1                   | Nanjiang       |
| 4    | 1500             | 1,3                | 3                   | Nanjiang       |
| 5    | 1500             | 2,3                | 3                   | Donghai        |
| 6    | 1500             | 3                  | 3                   | Nanjiang       |

The target number for each of the preferred-specialty and preferred-city goals is 8000 recruited personnel.

## Problem units
- U1 (context): I need help creating a personnel arrangement plan for Jieli Company to assign recruited professionals to branches in Donghai City and Nanjiang City.
- U2 (data): Table 4-3
| Branch Location | Specialty | Demand |
|-----------------|-----------|--------|
| Donghai City    | 1         | 1000   |
| Donghai City    | 2         | 2000   |
| Donghai City    | 3         | 1500   |
| Nanjiang City   | 1         | 2000   |
| Nanjiang City   | 2         | 1000   |
| Nanjiang City   | 3         | 1000   |
- U3 (data): Table 4-4

| Type | Number of People | Suitable Specialty | Preferred Specialty | Preferred City |
|------|------------------|--------------------|---------------------|----------------|
| 1    | 1500             | 1,2                | 1                   | Donghai        |
| 2    | 1500             | 2,3                | 2                   | Donghai        |
| 3    | 1500             | 1,3                | 1                   | Nanjiang       |
| 4    | 1500             | 1,3                | 3                   | Nanjiang       |
| 5    | 1500             | 2,3                | 3                   | Donghai        |
| 6    | 1500             | 3                  | 3                   | Nanjiang       |
- U4 (data): The target number for each of the preferred-specialty and preferred-city goals is 8000 recruited personnel.
- U5 (constraint): The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3 (p1).
- U6 (constraint): A person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4.
- U7 (constraint): The total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4.
- U8 (objective): Achieve that 8000 recruited personnel meet their preferred specialty.
- U9 (objective): Achieve that 8000 recruited personnel meet their preferred city.
- U10 (objective): Determine the minimum number of recruited personnel who cannot be assigned to their preferred city.
- U11 (assumption): The company considers the three priorities in the order p1, p2, p3, with p1 being the highest priority and p3 the lowest.

## Hidden slot scoring rules
## H1: exact_demand_equality
- Severity: P1
- Severity reason: Without knowing that the demand must be met exactly (not just a lower bound), the model would use inequality constraints, changing the feasible set and the degree to which p2 and p3 can be achieved. This leads to a materially different solution than the intended problem.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must ask whether the demand fulfillment condition for p1 is an exact equality (assign exactly the demand numbers) or a lower bound (at least the demand).
- Reference acceptable questions:
  - For the demand requirement p1, does that mean we must assign exactly the number in Table 4‑3 to each specialty and branch, or is it acceptable to assign more than the demand if needed?
  - Is p1 an exact equality constraint, or is it a minimum to be met (i.e., at least the demand)?
- Failure modes:
  - Agent silently assumes the demand is a lower bound (>=) and allows over‑assignment, which changes the feasible set and the optimal achievement of p2/p3.

## H2: priority_order_lexicographic
- Severity: P0
- Severity reason: The entire multi‑objective formulation depends on the priority structure. Without knowing that the priorities are lexicographic (p1 before p2 before p3), a modeling agent cannot correctly specify the goal programming model. The problem would be ill‑posed.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must explicitly ask whether the priorities follow a lexicographic (preemptive) order, with p1 highest and p3 lowest, and that the goals are solved in that sequence.
- Reference acceptable questions:
  - How are the priorities structured? Is it a strict lexicographic order where p1 must be satisfied first, then p2, and finally p3?
  - Are we using preemptive goal programming, meaning we first fully satisfy p1, then try to achieve p2 as much as possible, and only after that try to achieve p3?
- Failure modes:
  - Agent treats all three goals as equally weighted and uses a weighted‑sum objective, ignoring the preemptive priority structure.
  - Agent assumes the three goals can be traded off simultaneously without a strict order, leading to a fundamentally different model.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the 6 types in Table 4-4), or is it a different fixed number?

## Turn 1 - User Simulator

The total number of recruited personnel is exactly 9000, which is the sum of the 6 types in Table 4-4.

## Turn 2 - Generic Agent

QUESTION: Are the demand figures in Table 4-3 (e.g., 1000 for Donghai Specialty 1) hard requirements that must be met exactly, or are they maximum capacities that can be under-filled?

## Turn 2 - User Simulator

The demand figures in Table 4-3 are hard requirements that must be met exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: For the "preferred specialty" goal, does a person count as meeting it only if they are assigned to their single listed preferred specialty, or does it also count if they are assigned to any specialty in their suitable specialty set?

## Turn 3 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty.

## Turn 4 - Generic Agent

QUESTION: For the "preferred city" goal, does a person count as meeting it only if they are assigned to a branch in their single listed preferred city, or is there any other condition?

## Turn 4 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single listed preferred city.

## Turn 5 - Generic Agent

QUESTION: Are the "8000 meet preferred specialty" and "8000 meet preferred city" targets hard minimum requirements that must be satisfied, or are they soft goals to be maximized as much as possible?

## Turn 5 - User Simulator

They are soft goals to be maximized as much as possible.

## Turn 6 - Generic Agent

QUESTION: Is the primary objective to minimize the number of people not assigned to their preferred city, with the 8000-person targets for preferred specialty and preferred city treated as secondary goals to be maximized only after that minimum is achieved?

## Turn 6 - User Simulator

No, that is not the correct order. The priorities are in strict order: p1 (fully meeting the demand in Table 4-3) is the highest priority, p2 (8000 people meeting their preferred specialty) is second, and p3 (8000 people meeting their preferred city) is the lowest. So we first make sure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, we aim for 8000 people in their preferred city.

## Turn 7 - Generic Agent

QUESTION: Since the demand in Table 4-3 sums to 8500 but there are 9000 people, are the 500 unassigned people simply left out of the plan, or must they be assigned to some branch even if it exceeds the demand?

## Turn 7 - User Simulator

The 500 unassigned people are simply left out of the plan. The demand in Table 4-3 must be met exactly, so no more than 8500 people are assigned to branches.

## Turn 8 - Generic Agent

QUESTION: For the p2 goal of 8000 people meeting their preferred specialty, is this a target to be maximized (i.e., get as close to 8000 as possible), or is it a hard constraint that at least 8000 must be assigned to their preferred specialty?

## Turn 8 - User Simulator

It is a target to be maximized, meaning we aim to get as close to 8000 as possible.

## Turn 9 - Generic Agent

QUESTION: For the p3 goal of 8000 people meeting their preferred city, is this also a target to be maximized (i.e., get as close to 8000 as possible), or is it a hard constraint that at least 8000 must be assigned to their preferred city?

## Turn 9 - User Simulator

It is a target to be maximized, meaning we aim to get as close to 8000 as possible.

## Turn 10 - Generic Agent

QUESTION: Is the "minimum number of recruited personnel who cannot be assigned to their preferred city" simply the total number of assigned people (8500) minus the number who are assigned to their preferred city, or does it include the 500 unassigned people in that count?

## Turn 10 - User Simulator

It is simply the total number of assigned people (8500) minus the number who are assigned to their preferred city. The 500 unassigned people are not included in that count.

## Turn 11 - Generic Agent

QUESTION: Are the decision variables for assigning people to branches continuous (allowing fractional people) or must they be integer values?

## Turn 11 - User Simulator

The decision variables must be integer values.

## Turn 12 - Generic Agent

QUESTION: Are there any additional constraints or rules not mentioned in the brief, such as limits on how many people of a specific type can be assigned to a single branch, or any other restrictions on the assignment?

## Turn 12 - User Simulator

No, there are no additional constraints or rules beyond those already mentioned.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Total Personnel:** 9000 recruited professionals, divided into 6 types (1500 each).
2.  **Assignment Capacity:** Only 8500 people can be assigned to branches (sum of demands in Table 4-3). The remaining 500 are unassigned and excluded from all counts and objectives.
3.  **Decision Variables:** Integer variables representing the number of people of each type assigned to each (City, Specialty) combination.
4.  **Hard Constraints (Priority p1):**
    *   **Demand Satisfaction:** The total number of people assigned to each specific (City, Specialty) pair must exactly equal the demand listed in Table 4-3.
    *   **Type Availability:** The total number of people assigned from each type (across all cities and specialties) cannot exceed 1500.
    *   **Suitability:** A person of a given type can only be assigned to a specialty listed in their "Suitable Specialty" set in Table 4-4.
5.  **Soft Goals (Maximization):**
    *   **Priority p2:** Maximize the number of assigned people who are placed in their "Preferred Specialty" (as listed in Table 4-4). The target is 8000, but the goal is to maximize this count subject to p1.
    *   **Priority p3:** Maximize the number of assigned people who are placed in their "Preferred City" (as listed in Table 4-4). The target is 8000, but the goal is to maximize this count subject to p1 and p2.
6.  **Objective Function:** This is a lexicographic optimization problem.
    *   First, satisfy all hard constraints (p1).
    *   Second, maximize the count of people in their preferred specialty (p2).
    *   Third, among all solutions that maximize p2, maximize the count of people in their preferred city (p3).
7.  **Final Output Metric:** The "minimum number of recruited personnel who cannot be assigned to their preferred city" is calculated as $8500 - (\text{Number of assigned people in their preferred city})$. This is derived from the optimal solution of the lexicographic problem.

**Assumptions:**
*   None. All critical facts were confirmed by the user.