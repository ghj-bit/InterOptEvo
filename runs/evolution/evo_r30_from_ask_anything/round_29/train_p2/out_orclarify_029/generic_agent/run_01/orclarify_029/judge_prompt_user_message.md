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

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the 1500 people in each of the 6 types), or is 8000 the total number of people to be assigned?

## Turn 1 - User Simulator

The total number of recruited personnel is 9000, which is the sum of the 1500 people in each of the 6 types. The 8000 figure is the target number for the preferred-specialty and preferred-city goals, not the total headcount.

## Turn 2 - Generic Agent

QUESTION: Are the branch demand figures in Table 4-3 (e.g., 1000 for Specialty 1 in Donghai) hard ceilings that must not be exceeded, or are they exact targets that must be met precisely?

## Turn 2 - User Simulator

They are exact targets that must be met precisely. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Is the "total number of people assigned from each type cannot exceed the available number" constraint a hard ceiling (meaning you can assign fewer than 1500 from a type if needed), or is it an exact equality (meaning all 1500 people from each type must be assigned)?

## Turn 3 - User Simulator

It is a hard ceiling. You can assign fewer than 1500 from a type if needed, but you cannot assign more than the available number listed in Table 4-4.

## Turn 4 - Generic Agent

QUESTION: Since the total demand across all branches is 8500 but the total available personnel is 9000, are the 500 unassigned people simply left out of the plan, or is there a penalty or cost associated with leaving someone unassigned?

## Turn 4 - User Simulator

The 500 unassigned people are simply left out of the plan. There is no penalty or cost associated with leaving someone unassigned.

## Turn 5 - Generic Agent

QUESTION: Is the objective to minimize the number of assigned personnel who do not get their preferred city, or is it to minimize the number of all 9000 recruited personnel who do not get their preferred city (including the 500 unassigned)?

## Turn 5 - User Simulator

The objective is to minimize the number of assigned personnel who do not get their preferred city. The 500 unassigned people are not included in this count.

## Turn 6 - Generic Agent

QUESTION: Are the goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city hard constraints that must be satisfied, or are they soft targets that are used to define the objective function?

## Turn 6 - User Simulator

They are soft targets used to define the objective function. They are not hard constraints that must be satisfied.

## Turn 7 - Generic Agent

QUESTION: Is the objective function a single weighted sum that combines the penalty for not meeting the preferred-specialty target and the penalty for not meeting the preferred-city target, or is it a lexicographic objective where one goal takes strict priority over the other?

## Turn 7 - User Simulator

It is a lexicographic objective. The goals are handled in strict priority order: first, fully meet the demand (p1); second, try to get 8000 people into their preferred specialty (p2); and third, after that, aim for 8000 people in their preferred city (p3).

## Turn 8 - Generic Agent

QUESTION: In the lexicographic objective, is the second priority (p2) to maximize the number of assigned personnel who get their preferred specialty, or is it to minimize the shortfall from the target of 8000?

## Turn 8 - User Simulator

It is to minimize the shortfall from the target of 8000.

## Turn 9 - Generic Agent

QUESTION: In the lexicographic objective, is the third priority (p3) to minimize the shortfall from the target of 8000 for preferred city, or is it to minimize the total number of assigned personnel who do not get their preferred city?

## Turn 9 - User Simulator

It is to minimize the total number of assigned personnel who do not get their preferred city.

## Turn 10 - Generic Agent

QUESTION: Are the decision variables continuous (allowing fractional people) or integer (requiring whole numbers of people)?

## Turn 10 - User Simulator

The decision variables are integer, requiring whole numbers of people.

## Turn 11 - Generic Agent

QUESTION: Are there any additional constraints or rules, such as minimum assignment requirements per branch or specialty, that are not listed in the tables?

## Turn 11 - User Simulator

No, there are no additional constraints or rules beyond what is listed in the tables and the constraints we have discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Total Personnel:** 9000 total recruited personnel (6 types × 1500 each).
2.  **Assignment Capacity:** The total demand across all branches is 8500 (1000+2000+1500+2000+1000+1000). Therefore, exactly 500 people will remain unassigned.
3.  **Decision Variables:** Integer variables representing the number of people from each type assigned to each (City, Specialty) combination.
4.  **Hard Constraints:**
    *   **Demand Satisfaction:** The number of people assigned to each specific (City, Specialty) branch must exactly equal the demand listed in Table 4-3.
    *   **Type Availability:** The total number of people assigned from each type (1-6) cannot exceed 1500.
    *   **Suitability:** A person can only be assigned to a specialty listed in their "Suitable Specialty" set in Table 4-4.
5.  **Objective Function (Lexicographic):**
    *   **Priority 1 (P1):** Satisfy all branch demands exactly (this is effectively a feasibility constraint given the hard constraints above, but listed as the first priority in the user's description).
    *   **Priority 2 (P2):** Minimize the shortfall from the target of 8000 assigned personnel who get their preferred specialty. (i.e., Maximize the number of assigned personnel who get their preferred specialty, up to a target of 8000).
    *   **Priority 3 (P3):** Minimize the total number of assigned personnel who do *not* get their preferred city.
6.  **Unassigned Personnel:** The 500 unassigned people are not counted in the objective function metrics for preferred specialty or preferred city.
7.  **No Other Constraints:** No minimums, exclusivity rules, or other hidden constraints exist.