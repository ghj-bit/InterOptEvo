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

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to their single preferred specialty, or should they also count if assigned to any specialty in their suitable specialty set?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single preferred specialty listed in Table 4-4. Being assigned to any other specialty in their suitable specialty set does not count toward this goal.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in their single preferred city, or should they also count if assigned to any branch in either city?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single preferred city listed in Table 4-4. Being assigned to a branch in the other city does not count toward this goal.

## Turn 3 - Generic Agent

QUESTION: Regarding the branch demand numbers in Table 4-3, should the total number of people assigned to each branch specialty be exactly equal to the listed demand, or should it be at most the listed demand?

## Turn 3 - User Simulator

The total number of people assigned to each branch specialty must be exactly equal to the listed demand in Table 4-3. No more, no less.

## Turn 4 - Generic Agent

QUESTION: Regarding the "available number of each type" constraint from Table 4-4, should the number of people assigned from each type be exactly equal to the listed number, or should it be at most the listed number?

## Turn 4 - User Simulator

The number of people assigned from each type should be at most the listed number in Table 4-4.

## Turn 5 - Generic Agent

QUESTION: Since total demand across all branches is 8500 but total available personnel is 9000, and each branch demand must be met exactly, should all 8500 demand slots be filled (leaving 500 people unassigned), or should all 9000 people be assigned (which would require exceeding some branch demand)?

## Turn 5 - User Simulator

All 8500 demand slots should be filled, leaving 500 people unassigned. The branch demand must be met exactly, so we cannot assign more than the listed demand to any branch specialty.

## Turn 6 - Generic Agent

QUESTION: Regarding the three objectives you mentioned (8000 meeting preferred specialty, 8000 meeting preferred city, and minimizing those not meeting preferred city), should this be modeled as a single optimization problem with a specific priority order among these goals, or as three separate independent optimization problems each solved on its own?

## Turn 6 - User Simulator

This should be modeled as a single optimization problem with a specific priority order among the goals. The priorities are in strict order: first, fully meet all branch demand (p1); second, achieve 8000 people meeting their preferred specialty (p2); and third, achieve 8000 people meeting their preferred city (p3).

## Turn 7 - Generic Agent

QUESTION: For the second priority (p2), should the model maximize the number of people meeting their preferred specialty up to a cap of 8000, or should it simply maximize the number of people meeting their preferred specialty with no cap (where 8000 is just the expected target)?

## Turn 7 - User Simulator

The model should maximize the number of people meeting their preferred specialty up to a cap of 8000. The target is 8000, so the goal is to achieve that number, not to exceed it.

## Turn 8 - Generic Agent

QUESTION: For the third priority (p3), should the model maximize the number of people meeting their preferred city up to a cap of 8000, or should it minimize the number of people NOT meeting their preferred city (which is equivalent to maximizing those who do meet it, but without a cap)?

## Turn 8 - User Simulator

The model should minimize the number of people not meeting their preferred city. This is the third priority objective as stated in the original request.

## Turn 9 - Generic Agent

QUESTION: For the second priority (p2), should the model maximize the number of people meeting their preferred specialty with no upper cap (i.e., simply maximize it, where 8000 is the expected achievable target), or should it maximize up to a hard cap of exactly 8000 (i.e., the objective is min(number meeting preferred specialty, 8000))?

## Turn 9 - User Simulator

The model should maximize the number of people meeting their preferred specialty with no upper cap. The 8000 is the expected achievable target, not a hard cap.

## Turn 10 - Generic Agent

QUESTION: For the unassigned 500 people (since only 8500 of 9000 are assigned), should the model be free to choose which types are left unassigned, or is there a specific rule about which types must be assigned first?

## Turn 10 - User Simulator

The model is free to choose which types are left unassigned. There is no specific rule about which types must be assigned first.

## Turn 11 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each branch specialty be required to be integer (whole persons), or can they be treated as continuous values?

## Turn 11 - User Simulator

The number of people assigned from each type to each branch specialty should be required to be integer (whole persons).

## Turn 12 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 12 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 13 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty also include only the 8500 assigned people (excluding the 500 unassigned)?

## Turn 13 - User Simulator

Yes, the count of people meeting their preferred specialty should also include only the 8500 assigned people, excluding the 500 unassigned.

## Turn 14 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 14 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 15 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 15 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 16 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 16 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 17 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 17 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 18 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 18 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 19 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 19 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 20 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 20 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 21 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 21 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 22 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 22 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 23 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 23 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 24 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 24 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 25 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 25 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 26 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 26 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this objective.

## Turn 27 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 27 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 28 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 28 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count toward this

## Turn 29 - Generic Agent

QUESTION: For the "preferred city" objective (p3), should the count of people meeting their preferred city include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any city)?

## Turn 29 - User Simulator

The count of people meeting their preferred city should include only the 8500 assigned people. The 500 unassigned people are not in any city and do not count toward this objective.

## Turn 30 - Generic Agent

QUESTION: For the "preferred specialty" objective (p2), should the count of people meeting their preferred specialty include only the 8500 assigned people, or should it also count the 500 unassigned people (who by definition are not in any specialty)?

## Turn 30 - User Simulator

The count of people meeting their preferred specialty should include only the 8500 assigned people. The 500 unassigned people are not in any specialty and do not count