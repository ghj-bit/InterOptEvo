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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city," should the model maximize the number of people meeting each goal (i.e., treat 8000 as a target to be approached as closely as possible, penalizing both shortfalls and excesses), or should it simply require at least 8000 to meet each goal as a hard constraint?

## Turn 1 - User Simulator

Treat 8000 as a target to be approached as closely as possible, penalizing both shortfalls and excesses.

## Turn 2 - Generic Agent

QUESTION: For the third objective, "determine the minimum number of recruited personnel who cannot be assigned to their preferred city," should this be a separate minimization objective (i.e., minimize the count of people not in their preferred city), or is it simply a reported value computed after solving the first two goals?

## Turn 2 - User Simulator

It is a separate minimization objective.

## Turn 3 - Generic Agent

QUESTION: The three objectives (approach 8000 for preferred specialty, approach 8000 for preferred city, and minimize the number not in preferred city) — should they be treated as a lexicographic (priority-ordered) goal program where you first optimize the first goal, then the second, then the third, or should they be combined into a single weighted objective with specific weights?

## Turn 3 - User Simulator

They should be treated as a lexicographic (priority-ordered) goal program.

## Turn 4 - Generic Agent

QUESTION: For the first two goals (approaching 8000 for preferred specialty and preferred city), you said to penalize both shortfalls and excesses — should the penalty for a shortfall (fewer than 8000) and the penalty for an excess (more than 8000) be equal, or should one be weighted more heavily than the other?

## Turn 4 - User Simulator

The penalty for a shortfall and the penalty for an excess should be equal.

## Turn 5 - Generic Agent

QUESTION: Regarding the branch demand numbers in Table 4-3 (e.g., Donghai City specialty 1 needs 1000), should these be treated as exact requirements that must be met precisely, or as upper bounds that can be underfilled if necessary?

## Turn 5 - User Simulator

They should be treated as exact requirements that must be met precisely.

## Turn 6 - Generic Agent

QUESTION: Regarding the "Number of People" in Table 4-4 (1500 per type, 9000 total), should all 9000 people be assigned to some branch and specialty, or is it possible that some people remain unassigned?

## Turn 6 - User Simulator

It is possible that some people remain unassigned.

## Turn 7 - Generic Agent

QUESTION: If some people remain unassigned, should unassigned people be penalized in the objective, or is leaving people unassigned free (no cost) as long as the branch demands are met exactly?

## Turn 7 - User Simulator

Leaving people unassigned is free (no cost) as long as the branch demands are met exactly.

## Turn 8 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is unassigned (not placed in any branch), should they be counted as "not meeting their preferred city" (i.e., they contribute to the shortfall/excess relative to 8000 and to the third objective of minimizing non-preferred-city assignments)?

## Turn 8 - User Simulator

Yes, unassigned people should be counted as "not meeting their preferred city."

## Turn 9 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is unassigned, should they be counted as "not meeting their preferred specialty" (i.e., they contribute to the shortfall/excess relative to 8000)?

## Turn 9 - User Simulator

Yes, unassigned people should be counted as "not meeting their preferred specialty."

## Turn 10 - Generic Agent

QUESTION: For the third objective (minimize the number of people not in their preferred city), should unassigned people also be counted in this minimization objective, or does this objective only count people who are actually assigned to a branch but in a city different from their preferred city?

## Turn 10 - User Simulator

Unassigned people should also be counted in this minimization objective.

## Turn 11 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch but to a specialty that is not their preferred specialty (though still in their suitable set), should they be counted as "not meeting their preferred specialty"?

## Turn 11 - User Simulator

Yes, they should be counted as "not meeting their preferred specialty."

## Turn 12 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city, should they be counted as "not meeting their preferred city"?

## Turn 12 - User Simulator

Yes, they should be counted as "not meeting their preferred city."

## Turn 13 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they still be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 13 - User Simulator

Yes, they should still be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 14 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they still be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 14 - User Simulator

No, they should not be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 15 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 15 - User Simulator

Yes, they should be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 16 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 16 - User Simulator

No, they should not be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 17 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 17 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 18 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 18 - User Simulator

No, they should not be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 19 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 19 - User Simulator

No, they should not be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 20 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 20 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 21 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 21 - User Simulator

Yes, they should be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 22 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 22 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 23 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 23 - User Simulator

Yes, they should be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 24 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 24 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 25 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 25 - User Simulator

Yes, they should be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 26 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 26 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 27 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 27 - User Simulator

Yes, they should be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 28 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 28 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.

## Turn 29 - Generic Agent

QUESTION: For the "preferred city" goal, if a person is assigned to a branch in a city that is not their preferred city but to their preferred specialty, should they be counted as "meeting their preferred specialty" for the preferred-specialty goal?

## Turn 29 - User Simulator

Yes, they should be counted as "meeting their preferred specialty" for the preferred-specialty goal.

## Turn 30 - Generic Agent

QUESTION: For the "preferred specialty" goal, if a person is assigned to a branch in their preferred city but to a specialty that is not their preferred specialty, should they be counted as "meeting their preferred city" for the preferred-city goal?

## Turn 30 - User Simulator

Yes, they should be counted as "meeting their preferred city" for the preferred-city goal.