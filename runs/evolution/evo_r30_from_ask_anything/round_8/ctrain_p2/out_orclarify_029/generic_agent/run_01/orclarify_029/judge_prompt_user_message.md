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

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the six types in Table 4-4), or is it a different fixed total that I should use for the assignment plan?

## Turn 1 - User Simulator

The total number of recruited personnel is exactly 9000, which is the sum of the six types in Table 4-4 (6 types × 1500 people each).

## Turn 2 - Generic Agent

QUESTION: For the branch demand figures in Table 4-3, are they hard ceilings that must not be exceeded, or are they exact targets that must be met precisely?

## Turn 2 - User Simulator

They are exact targets that must be met precisely. No more, no less.

## Turn 3 - Generic Agent

QUESTION: For the "total number of people assigned from each type cannot exceed the available number" rule, is the available number for each type (1500) a hard ceiling that can be left partially unassigned, or must all 1500 people of each type be assigned to some branch and specialty?

## Turn 3 - User Simulator

The available number for each type (1500) is a hard ceiling that can be left partially unassigned.

## Turn 4 - Generic Agent

QUESTION: Since the branch demands in Table 4-3 sum to exactly 9000 and the total available personnel is 9000, does the plan require that all 9000 recruited personnel be assigned to a branch and specialty, or is it acceptable for some personnel to remain unassigned?

## Turn 4 - User Simulator

The plan requires that all 9000 recruited personnel be assigned to a branch and specialty.

## Turn 5 - Generic Agent

QUESTION: For the goal of having 8000 personnel meet their preferred specialty, is 8000 a minimum target that must be met or exceeded, or is it an exact target that must be met precisely?

## Turn 5 - User Simulator

8000 is a minimum target that must be met or exceeded.

## Turn 6 - Generic Agent

QUESTION: For the goal of having 8000 personnel meet their preferred city, is 8000 a minimum target that must be met or exceeded, or is it an exact target that must be met precisely?

## Turn 6 - User Simulator

8000 is a minimum target that must be met or exceeded.

## Turn 7 - Generic Agent

QUESTION: Is the objective to minimize the number of personnel who do not meet their preferred city, subject to the constraint that at least 8000 meet their preferred specialty, or is the objective to minimize the number who do not meet their preferred specialty, subject to the constraint that at least 8000 meet their preferred city?

## Turn 7 - User Simulator

The objective is to minimize the number of personnel who do not meet their preferred city, subject to the constraint that at least 8000 meet their preferred specialty.

## Turn 8 - Generic Agent

QUESTION: When a person is assigned to a specialty that is in their suitable specialty set but is not their preferred specialty, does that person count as "meeting their preferred specialty" for the 8000 minimum target, or do they only count if assigned to their exact preferred specialty?

## Turn 8 - User Simulator

They only count if assigned to their exact preferred specialty.

## Turn 9 - Generic Agent

QUESTION: When a person is assigned to a city that is not their preferred city, does that person count as "meeting their preferred city" for the 8000 minimum target, or do they only count if assigned to their exact preferred city?

## Turn 9 - User Simulator

They only count if assigned to their exact preferred city.

## Turn 10 - Generic Agent

QUESTION: Is the constraint that at least 8000 personnel meet their preferred city a hard requirement that must be satisfied, or is it a soft goal that is only used to define the objective function?

## Turn 10 - User Simulator

It is a soft goal that is only used to define the objective function.

## Turn 11 - Generic Agent

QUESTION: Is the constraint that at least 8000 personnel meet their preferred specialty a hard requirement that must be satisfied, or is it a soft goal that is only used to define the objective function?

## Turn 11 - User Simulator

It is a hard requirement that must be satisfied.

## Turn 12 - Generic Agent

QUESTION: For the assignment decision, is the number of people assigned from each type to each branch-specialty combination required to be an integer, or can it be a continuous value?

## Turn 12 - User Simulator

The number of people assigned from each type to each branch-specialty combination is required to be an integer.

## Turn 13 - Generic Agent

QUESTION: Are the assignment variables required to be non-negative, meaning no negative number of people can be assigned to any branch-specialty combination?

## Turn 13 - User Simulator

Yes, the assignment variables are required to be non-negative.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Total Personnel:** 9000 recruited personnel (6 types × 1500 each). [Confirmed]
2.  **Assignment Requirement:** All 9000 personnel must be assigned to a branch and specialty. [Confirmed]
3.  **Branch Demands:** The demands in Table 4-3 are exact targets that must be met precisely. [Confirmed]
4.  **Type Availability:** The available number for each type (1500) is a hard ceiling. [Confirmed]
5.  **Suitable Specialty Constraint:** A person can only be assigned to a specialty listed in their suitable specialty set (Table 4-4). [Confirmed]
6.  **Preferred Specialty Goal:** At least 8000 personnel must be assigned to their exact preferred specialty. This is a hard constraint. [Confirmed]
7.  **Preferred City Goal:** The goal of 8000 personnel meeting their preferred city is a soft goal used to define the objective function. [Confirmed]
8.  **Objective Function:** Minimize the number of personnel who do not meet their preferred city. [Confirmed]
9.  **Counting Rules:**
    *   "Meeting preferred specialty" means being assigned to the exact specialty listed in the "Preferred Specialty" column of Table 4-4. [Confirmed]
    *   "Meeting preferred city" means being assigned to the exact city listed in the "Preferred City" column of Table 4-4. [Confirmed]
10. **Variable Domain:** Assignment variables (number of people from each type to each branch-specialty) are non-negative integers. [Confirmed]

**Open Assumptions:**
*   None. All formulation-critical facts have been confirmed.