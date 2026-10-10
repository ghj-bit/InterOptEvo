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

QUESTION: For the two goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city, are these intended as hard constraints that must be exactly satisfied, or as soft targets to be maximized as much as possible within the model?

## Turn 1 - User Simulator

They are soft targets to be maximized as much as possible within the model, not hard constraints that must be exactly satisfied.

## Turn 2 - Generic Agent

QUESTION: For the third objective of determining the minimum number of recruited personnel who cannot be assigned to their preferred city, is this a separate minimization goal to be optimized alongside the two maximization goals, or is it simply a descriptive output you want to read off after the other two goals are optimized?

## Turn 2 - User Simulator

It is a separate minimization goal to be optimized alongside the two maximization goals.

## Turn 3 - Generic Agent

QUESTION: For the branch demand figures in Table 4-3 (for example, 1000 for Specialty 1 in Donghai City), are these exact requirements that must be met precisely, or are they maximum capacities that the assigned personnel can fill up to but not exceed?

## Turn 3 - User Simulator

They are exact requirements that must be met precisely.

## Turn 4 - Generic Agent

QUESTION: For the "Number of People" figures in Table 4-4 (1500 for each of the 6 types), are these exact numbers that must all be assigned, or are they maximum available pools from which the model can choose to assign fewer?

## Turn 4 - User Simulator

They are maximum available pools from which the model can choose to assign fewer.

## Turn 5 - Generic Agent

QUESTION: Are the 8000-person targets for preferred specialty and preferred city calculated over all 9000 recruited personnel, or only over the subset of personnel who are actually assigned to a branch?

## Turn 5 - User Simulator

The 8000-person targets are calculated over all 9000 recruited personnel.

## Turn 6 - Generic Agent

QUESTION: For the "Suitable Specialty" column in Table 4-4, is the restriction that a person can only be assigned to a specialty listed in their suitable set a hard constraint that must always be satisfied, or is it a soft preference that can be violated if needed?

## Turn 6 - User Simulator

It is a hard constraint that must always be satisfied.

## Turn 7 - Generic Agent

QUESTION: For the three objectives (maximize preferred-specialty matches, maximize preferred-city matches, minimize non-preferred-city assignments), should the model treat them as a single combined objective with equal weights, or should they be optimized in a specific priority order where one goal is fully satisfied before the next is considered?

## Turn 7 - User Simulator

They should be optimized in a specific priority order where one goal is fully satisfied before the next is considered.

## Turn 8 - Generic Agent

QUESTION: In the priority order, which of the three goals is the highest priority: maximizing preferred-specialty matches, maximizing preferred-city matches, or minimizing non-preferred-city assignments?

## Turn 8 - User Simulator

Maximizing preferred-specialty matches is the highest priority.

## Turn 9 - Generic Agent

QUESTION: After maximizing preferred-specialty matches is fully satisfied, which goal is the second priority: maximizing preferred-city matches or minimizing non-preferred-city assignments?

## Turn 9 - User Simulator

Maximizing preferred-city matches is the second priority.

## Turn 10 - Generic Agent

QUESTION: For the decision variables, should the model track assignments at the level of individual people, or is it sufficient to track the number of people assigned from each type to each city-specialty combination?

## Turn 10 - User Simulator

It is sufficient to track the number of people assigned from each type to each city-specialty combination.

## Turn 11 - Generic Agent

QUESTION: For the decision variables tracking the number of people assigned from each type to each city-specialty combination, should these variables be restricted to integer values, or can they take continuous values?

## Turn 11 - User Simulator

They should be restricted to integer values.

## Turn 12 - Generic Agent

QUESTION: Are there any additional requirements or constraints beyond the suitable-specialty restriction, the branch demand equalities, and the type availability limits that the model must satisfy?

## Turn 12 - User Simulator

No, there are no additional requirements or constraints beyond the suitable-specialty restriction, the branch demand equalities, and the type availability limits.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Decision Variables:** Integer variables representing the number of people assigned from each of the 6 types to each city-specialty combination (2 cities × 3 specialties = 6 combinations per type, 36 variables total). Confirmed.

2. **Variable Domain:** Non-negative integers. Confirmed.

3. **Hard Constraints:**
   - **Suitable Specialty:** A person of a given type can only be assigned to a specialty listed in their "Suitable Specialty" set from Table 4-4. Confirmed.
   - **Branch Demand:** The total number of people assigned to each city-specialty combination must exactly equal the demand in Table 4-3 (e.g., exactly 1000 to Specialty 1 in Donghai City). Confirmed.
   - **Type Availability:** The total number of people assigned from each type across all city-specialty combinations cannot exceed 1500 (the "Number of People" in Table 4-4). Confirmed.

4. **Objective (Lexicographic Priority Order):**
   - **Priority 1 (Maximize):** The number of assigned personnel who are placed in their preferred specialty (target 8000, soft). Confirmed.
   - **Priority 2 (Maximize):** The number of assigned personnel who are placed in their preferred city (target 8000, soft). Confirmed.
   - **Priority 3 (Minimize):** The number of assigned personnel who are NOT placed in their preferred city. Confirmed.

5. **Scope of Objectives:** The 8000-person targets and the minimization goal are calculated over all 9000 recruited personnel (i.e., all assigned personnel, since the model assigns from the available pools). Confirmed.

6. **No Additional Constraints:** No other restrictions exist beyond those listed above. Confirmed.

**Open Assumptions:** None. All formulation-critical facts are confirmed.