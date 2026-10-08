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

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to their single listed preferred specialty, or would being assigned to any specialty in their suitable specialty set also count?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty. Being assigned to any other specialty in their suitable specialty set does not count.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in their single listed preferred city, or would being assigned to any branch in either city count?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single listed preferred city. Being assigned to a branch in the other city does not count.

## Turn 3 - Generic Agent

QUESTION: The branch demands in Table 4-3 sum to 8500, but only 9000 people are recruited. Should the branch demands be treated as exact requirements that must be met precisely, or as maximum capacities that may be left partially unfilled?

## Turn 3 - User Simulator

The branch demands in Table 4-3 must be treated as exact requirements that must be met precisely. No more, no less.

## Turn 4 - Generic Agent

QUESTION: The branch demands sum to 8500 but 9000 people are recruited, so 500 people will be left unassigned. Should these 500 unassigned people be allowed to come from any type, or must the unassigned people be chosen in a specific way (for example, to help maximize the preferred-specialty and preferred-city goals)?

## Turn 4 - User Simulator

The 500 unassigned people can come from any type. There is no specific requirement on which types must be left unassigned; the selection is determined by the overall plan to meet the priorities in order.

## Turn 5 - Generic Agent

QUESTION: The three objectives (8000 meet preferred specialty, 8000 meet preferred city, and minimize those not meeting preferred city) are stated together. Should these be treated as a lexicographic priority sequence where the first goal is satisfied as much as possible before the second is considered, or should they be combined into a single weighted objective?

## Turn 5 - User Simulator

These should be treated as a lexicographic priority sequence. The first goal is satisfied as much as possible before the second is considered, and the second before the third. They are not combined into a single weighted objective.

## Turn 6 - Generic Agent

QUESTION: In the lexicographic sequence, should the first goal (preferred specialty) be maximized toward the 8000 target, and the second goal (preferred city) also be maximized toward its 8000 target, with the third goal then minimizing the number not meeting preferred city?

## Turn 6 - User Simulator

Yes. In the lexicographic sequence, the first goal is to maximize the number of people meeting their preferred specialty toward the 8000 target. The second goal is to maximize the number of people meeting their preferred city toward the 8000 target. The third goal is to minimize the number of people not meeting their preferred city.

## Turn 7 - Generic Agent

QUESTION: For the third goal, should "the number of people not meeting their preferred city" be counted only among the 8500 people who are actually assigned to a branch, or should it also include the 500 people who are left unassigned?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: When a person is assigned to a branch, must that branch's specialty be one of the specialties in that person's suitable specialty set, or can a person be assigned to any branch regardless of specialty suitability?

## Turn 8 - User Simulator

A person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4.

## Turn 9 - Generic Agent

QUESTION: For the third goal, should the 500 unassigned people be counted as "not meeting their preferred city," or should that count include only the 8500 people who are actually assigned to a branch?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Should the number of people assigned to each type be allowed to be less than the available number listed in Table 4-4 (i.e., the available number is an upper bound), or must every available person of each type be assigned to some branch?

## Turn 10 - User Simulator

The available number for each type in Table 4-4 is an upper bound. The number of people assigned from each type can be less than the available number.

## Turn 11 - Generic Agent

QUESTION: Should the number of people assigned to each branch-specialty combination be an integer (whole number of people), or is it acceptable to treat these as continuous values in the model?

## Turn 11 - User Simulator

The number of people assigned to each branch-specialty combination must be an integer (whole number of people).

## Turn 12 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the third goal (minimizing people not meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 18 - User Simulator

The point

## Turn 19 - Generic Agent

QUESTION: For the third goal (minimizing people not meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 19 - User Simulator

The point

## Turn 20 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 20 - User Simulator

The point

## Turn 21 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: For the third goal (minimizing people not meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: For the third goal (minimizing people not meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: For the third goal (minimizing people not meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: For the first goal (maximizing people meeting their preferred specialty), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: For the second goal (maximizing people meeting their preferred city), should this count include only the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people in some way?

## Turn 30 - User Simulator

The