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

QUESTION: Are the demand values in Table 4-3 (e.g., 1000 for Specialty 1 in Donghai) hard minimums that must be met exactly, or are they targets that the assignment plan should satisfy as closely as possible?

## Turn 1 - User Simulator

They are hard requirements. The assignment plan must meet the demand values in Table 4-3 exactly—no more, no less.

## Turn 2 - Generic Agent

QUESTION: Is the total number of recruited personnel fixed at 9000 (the sum of the six types in Table 4-4), and must every one of these 9000 people be assigned to a branch and specialty?

## Turn 2 - User Simulator

The total number of recruited personnel is 9000, which is the sum of the six types in Table 4-4. However, the available business facts do not explicitly state whether every one of these 9000 people must be assigned to a branch and specialty. This point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Since the total demand in Table 4-3 is 8500 and the total supply is 9000, are the 500 unassigned people simply left unassigned, or must they be assigned to some branch and specialty even if it exceeds the demand?

## Turn 3 - User Simulator

The 500 unassigned people are simply left unassigned. The demand values in Table 4-3 must be met exactly, so no one can be assigned to a branch and specialty if it would exceed the demand.

## Turn 4 - Generic Agent

QUESTION: Regarding the objective to have 8000 personnel meet their preferred specialty, is this a hard constraint that must be satisfied, or is it a target to be maximized as part of a multi-objective optimization?

## Turn 4 - User Simulator

It is a target to be maximized as part of a multi-objective optimization. It is not a hard constraint.

## Turn 5 - Generic Agent

QUESTION: Regarding the objective to have 8000 personnel meet their preferred city, is this also a target to be maximized as part of the multi-objective optimization, or is it a hard constraint?

## Turn 5 - User Simulator

It is a target to be maximized as part of the multi-objective optimization, not a hard constraint.

## Turn 6 - Generic Agent

QUESTION: Regarding the third objective to determine the minimum number of recruited personnel who cannot be assigned to their preferred city, is this a separate minimization objective to be optimized alongside the two maximization targets, or is it simply a metric to be reported after solving the first two objectives

## Turn 6 - User Simulator

It is a separate minimization objective to be optimized alongside the two maximization targets.

## Turn 7 - Generic Agent

QUESTION: How should the three objectives (maximize preferred specialty matches, maximize preferred city matches, minimize non-preferred city assignments) be combined into a single optimization problem, for example by assigning specific weights to each objective or by using a lexicographic priority order

## Turn 7 - User Simulator

The three objectives should be combined using a lexicographic priority order. The priorities are in strict order: p1 (meeting demand exactly) is the highest priority, p2 (maximizing preferred specialty matches) is second, and p3 (maximizing preferred city matches / minimizing non-preferred city assignments) is the lowest.

## Turn 8 - Generic Agent

QUESTION: In the lexicographic priority order, is "meeting demand exactly" (p1) treated as a hard constraint that must be satisfied before optimizing the other objectives, or is it a soft objective with a penalty

## Turn 8 - User Simulator

"Meeting demand exactly" (p1) is treated as a hard constraint that must be satisfied before optimizing the other objectives.

## Turn 9 - Generic Agent

QUESTION: Are the "Number of People" values in Table 4-4 (1500 for each type) hard upper limits on how many people of that type can be assigned, or are they exact quotas that must all be assigned

## Turn 9 - User Simulator

They are hard upper limits on how many people of that type can be assigned.

## Turn 10 - Generic Agent

QUESTION: Are the "Suitable Specialty" sets in Table 4-4 hard constraints that restrict which specialties a person of a given type can be assigned to

## Turn 10 - User Simulator

Yes, the "Suitable Specialty" sets in Table 4-4 are hard constraints that restrict which specialties a person of a given type can be assigned to.

## Turn 11 - Generic Agent

QUESTION: Are the "Preferred City" values in Table 4-3 hard constraints that restrict which city a person of a given type can be assigned to

## Turn 11 - User Simulator

No, the "Preferred City" values in Table 4-4 are not hard constraints. They are used to define the objective of maximizing the number of personnel assigned to their preferred city.

## Turn 12 - Generic Agent

QUESTION: Are the "Preferred Specialty" values in Table 4-4 hard constraints that restrict which specialty a person of a given type can be assigned to

## Turn 12 - User Simulator

No, the "Preferred Specialty" values in Table 4-4 are not hard constraints. They are used to define the objective of maximizing the number of personnel assigned to their preferred specialty.

## Turn 13 - Generic Agent

QUESTION: Are there any additional requirements or constraints not mentioned in the brief, such as minimum staffing levels per branch, diversity requirements, or dependencies between different types

## Turn 13 - User Simulator

There are no additional requirements or constraints beyond those already mentioned.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Problem Type:** Multi-objective assignment problem with lexicographic priorities.
2.  **Decision Variables:** The number of people of each type (1-6) assigned to each branch (Donghai, Nanjiang) and specialty (1-3).
3.  **Hard Constraints (Priority 1):**
    *   **Demand Satisfaction:** The total number of people assigned to each (Branch, Specialty) pair must exactly match the demand in Table 4-3.
        *   Donghai-S1: 1000
        *   Donghai-S2: 2000
        *   Donghai-S3: 1500
        *   Nanjiang-S1: 2000
        *   Nanjiang-S2: 1000
        *   Nanjiang-S3: 1000
    *   **Supply Limits:** The total number of people assigned from each type (1-6) cannot exceed 1500.
    *   **Suitability:** A person of a given type can only be assigned to a specialty listed in their "Suitable Specialty" set in Table 4-4.
    *   **Non-negativity:** Assignment variables must be non-negative.
4.  **Objectives (Lexicographic Order):**
    *   **Priority 2 (Maximize):** The total number of personnel assigned to their "Preferred Specialty" as listed in Table 4-4.
    *   **Priority 3 (Maximize/Minimize):** The total number of personnel assigned to their "Preferred City" as listed in Table 4-4. (Equivalently, minimize the number of personnel *not* assigned to their preferred city).
5.  **Data:**
    *   **Table 4-3 (Demand):**
        *   Donghai: S1=1000, S2=2000, S3=1500
        *   Nanjiang: S1=2000, S2=1000, S3=1000
    *   **Table 4-4 (Supply & Preferences):**
        *   Type 1: Supply=1500, Suitable={1,2}, PrefSpec=1, PrefCity=Donghai
        *   Type 2: Supply=1500, Suitable={2,3}, PrefSpec=2, PrefCity=Donghai
        *   Type 3: Supply=1500, Suitable={1,3}, PrefSpec=1, PrefCity=Nanjiang
        *   Type 4: Supply=1500, Suitable={1,3}, PrefSpec=3, PrefCity=Nanjiang
        *   Type 5: Supply=1500, Suitable={2,3}, PrefSpec=3, PrefCity=Donghai
        *   Type 6: Supply=1500, Suitable={3}, PrefSpec=3, PrefCity=Nanjiang
6.  **Assumptions:**
    *   The total supply (9000) exceeds total demand (8500), so 500 people will remain unassigned. This is handled by the supply constraints being inequalities ($\le$) rather than equalities.
    *   The "Preferred City" and "Preferred Specialty" are only used for the objective functions, not as hard constraints.
    *   There are no other hidden constraints or requirements.