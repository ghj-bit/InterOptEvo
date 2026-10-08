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

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to their single listed preferred specialty, or does being assigned to any specialty in their suitable specialty set count as meeting the goal?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty. Being assigned to any other specialty in their suitable specialty set does not count.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in their single listed preferred city, or does being assigned to any branch in either city count as meeting the goal?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single listed preferred city. Being assigned to a branch in the other city does not count.

## Turn 3 - Generic Agent

QUESTION: For the branch demand figures in Table 4-3, should each branch's demand be treated as an exact requirement that must be met precisely, or as a maximum that must not be exceeded?

## Turn 3 - User Simulator

Each branch's demand in Table 4-3 must be met precisely. No more, no less.

## Turn 4 - Generic Agent

QUESTION: For the "available number of each type" in Table 4-4, should the number of people assigned from each type be treated as a maximum that must not be exceeded, or as an exact requirement that must be met precisely?

## Turn 4 - User Simulator

The number of people assigned from each type must not exceed the available number listed in Table 4-4. It is a maximum, not an exact requirement.

## Turn 5 - Generic Agent

QUESTION: The total branch demand is 8500 but the total available personnel is 9000, so 500 people will be unassigned. Should unassigned people be allowed (i.e., not every recruited person must be placed in a branch), or must all 9000 be assigned?

## Turn 5 - User Simulator

Unassigned people are allowed. Not every recruited person must be placed in a branch.

## Turn 6 - Generic Agent

QUESTION: The three stated objectives (8000 meeting preferred specialty, 8000 meeting preferred city, and minimizing the number not meeting preferred city) cannot all be satisfied simultaneously in a single optimization. How should these be combined into one model — for example, minimize the number not meeting preferred city as the primary objective while treating the two 8000 goals as constraints, or use some other priority or weighting scheme?

## Turn 6 - User Simulator

The three objectives should be treated as strict priorities in the order p1, p2, p3. First, fully meet all branch demand (p1). Second, try to get 8000 people into their preferred specialty (p2). Third, after that, aim for 8000 people in their preferred city (p3). This is a lexicographic priority scheme, not a single weighted objective.

## Turn 7 - Generic Agent

QUESTION: In the lexicographic scheme, is "fully meet all branch demand" (p1) a hard feasibility requirement that must be satisfied before any optimization begins, or is it the first objective level to be optimized?

## Turn 7 - User Simulator

"Fully meet all branch demand" (p1) is the first objective level to be optimized. It is not a hard feasibility requirement that must be satisfied before any optimization begins; it is the highest-priority objective in the lexicographic scheme.

## Turn 8 - Generic Agent

QUESTION: For the p2 objective (preferred specialty), should the model maximize the number of people assigned to their preferred specialty up to a cap of 8000, or should it simply maximize the number with no cap, treating 8000 as a target that may or may not be reached?

## Turn 8 - User Simulator

The model should maximize the number of people assigned to their preferred specialty with no cap. The figure of 8000 is a target that may or may not be reached; it is not a hard upper limit on the objective.

## Turn 9 - Generic Agent

QUESTION: For the p3 objective (preferred city), should the model minimize the number of assigned people who are NOT in their preferred city, or should it maximize the number of assigned people who ARE in their preferred city?

## Turn 9 - User Simulator

The model should minimize the number of assigned people who are NOT in their preferred city.

## Turn 10 - Generic Agent

QUESTION: When counting "assigned people who are not in their preferred city" for the p3 objective, should unassigned people (those not placed in any branch) be included in that count, or should only people who are actually assigned to a branch be considered?

## Turn 10 - User Simulator

Only people who are actually assigned to a branch should be considered. Unassigned people are not included in the count for the p3 objective.

## Turn 11 - Generic Agent

QUESTION: For the p1 objective (fully meet all branch demand), should the model maximize the total number of branch demand units satisfied, or should it minimize the total shortfall across all branches?

## Turn 11 - User Simulator

The model should maximize the total number of branch demand units satisfied.

## Turn 12 - Generic Agent

QUESTION: For the p1 objective, should the total number of branch demand units satisfied be counted as the sum of people assigned to each branch (capped at each branch's demand), or simply as the total number of people assigned to any branch regardless of whether it exceeds that branch's demand?

## Turn 12 - User Simulator

The total number of branch demand units satisfied should be counted as the sum of people assigned to each branch, capped at each branch's demand.

## Turn 13 - Generic Agent

QUESTION: Since branch demand must be met precisely (no more, no less) as stated earlier, and p1 maximizes demand units satisfied, should the branch demand constraints be hard equality constraints (assignment to each branch equals its demand exactly), or should they be soft constraints where exceeding demand is allowed but not rewarded in p1?

## Turn 13 - User Simulator

The branch demand constraints should be hard equality constraints. The assignment to each branch must equal its demand exactly.

## Turn 14 - Generic Agent

QUESTION: For the p2 objective (maximize people in preferred specialty), should this count include only people who are assigned to a branch, or should it also include unassigned people (who trivially are not in any specialty)?

## Turn 14 - User Simulator

Only people who are assigned to a branch should be counted for the p2 objective.

## Turn 15 - Generic Agent

QUESTION: For the p2 objective, should the count of people in their preferred specialty be limited to those assigned to a branch in any city, or should it additionally require that the person is assigned to a branch in their preferred city as well?

## Turn 15 - User Simulator

The count for the p2 objective should include only people assigned to a branch in any city. It does not require that the person is also in their preferred city.

## Turn 16 - Generic Agent

QUESTION: For the p3 objective (minimize assigned people not in preferred city), should the count include all assigned people regardless of whether they are in their preferred specialty, or only those who are also in their preferred specialty?

## Turn 16 - User Simulator

The count for the p3 objective should include all assigned people regardless of whether they are in their preferred specialty.

## Turn 17 - Generic Agent

QUESTION: For the decision variables, should the number of people of each type assigned to each branch (city, specialty) be required to be integer-valued, or can they be continuous (fractional) values?

## Turn 17 - User Simulator

The number of people of each type assigned to each branch must be integer-valued.

## Turn 18 - Generic Agent

QUESTION: For the p1 objective, since branch demand is a hard equality constraint (each branch must be filled exactly), the total demand satisfied is always 8500. Does p1 then become trivially satisfied, or is there a scenario where p1 could be infeasible and the model should handle that case?

## Turn 18 - User Simulator

Since branch demand is a hard equality constraint, p1 is trivially satisfied whenever a feasible solution exists. If the constraints make the problem infeasible, the model should report that no feasible assignment exists.

## Turn 19 - Generic Agent

QUESTION: For the p2 objective (maximize people in preferred specialty), should the model also track and report the number of people who meet their preferred city goal (p3 target of 8000), or is p3 solely the minimization of people not in their preferred city?

## Turn 19 - User Simulator

P3 is solely the minimization of the number of assigned people not in their preferred city. The model does not need to separately track or report the number meeting the 8000 target as a distinct output; that target is implicit in the minimization objective.

## Turn 20 - Generic Agent

QUESTION: For the p2 objective, should the model maximize the number of assigned people in their preferred specialty, or should it maximize the number of assigned people in their preferred specialty minus a penalty for each person not in their preferred city?

## Turn 20 - User Simulator

The model should maximize the number of assigned people in their preferred specialty. There is no penalty for being out of preferred city in the p2 objective.

## Turn 21 - Generic Agent

QUESTION: For the p3 objective, should the model minimize the number of assigned people not in their preferred city, or should it minimize the number of assigned people not in their preferred city minus a penalty for each person not in their preferred specialty?

## Turn 21 - User Simulator

The model should minimize the number of assigned people not in their preferred city. There is no penalty for being out of preferred specialty in the p3 objective.

## Turn 22 - Generic Agent

QUESTION: For the p2 objective, should the model maximize the number of assigned people in their preferred specialty, or should it maximize the number of assigned people in their preferred specialty subject to the constraint that at least 8000 people are in their preferred specialty?

## Turn 22 - User Simulator

The model should maximize the number of assigned people in their preferred specialty. There is no constraint requiring at least 8000 people to be in their preferred specialty.

## Turn 23 - Generic Agent

QUESTION: For the p3 objective, should the model minimize the number of assigned people not in their preferred city, or should it minimize the number of assigned people not in their preferred city subject to the constraint that at least 8000 people are in their preferred city?

## Turn 23 - User Simulator

The model should minimize the number of assigned people not in their preferred city. There is no constraint requiring at least 8000 people to be in their preferred city.

## Turn 24 - Generic Agent

QUESTION: For the p2 objective, should the model maximize the number of assigned people in their preferred specialty, or should it maximize the number of assigned people in their preferred specialty subject to the constraint that the number of assigned people in their preferred city is at least 8000?

## Turn 24 - User Simulator

The model should maximize the number of assigned people in their preferred specialty. There is no constraint requiring the number of assigned people in their preferred city to be at least 8000.

## Turn 25 - Generic Agent

QUESTION: For the p3 objective, should the model minimize the number of assigned people not in their preferred city, or should it minimize the number of assigned people not in their preferred city subject to the constraint that the number of assigned people in their preferred specialty is at least 8000?

## Turn 25 - User Simulator

The model should minimize the number of assigned people not in their preferred city. There is no constraint requiring the number of assigned people in their preferred specialty to be at least 8000.

## Turn 26 - Generic Agent

QUESTION: For the p2 objective, should the model maximize the number of assigned people in their preferred specialty, or should it maximize the number of assigned people in their preferred specialty subject to the constraint that the number of assigned people not in their preferred city is at most 500?

## Turn 26 - User Simulator

The model should maximize the number of assigned people in their preferred specialty. There is no constraint requiring the number of assigned people not in their preferred city to be at most 500.

## Turn 27 - Generic Agent

QUESTION: For the p3 objective, should the model minimize the number of assigned people not in their preferred city, or should it minimize the number of assigned people not in their preferred city subject to the constraint that the number of assigned people in their preferred specialty is at most 8000?

## Turn 27 - User Simulator

The model should minimize the number of assigned people not in their preferred city. There is no constraint requiring the number of assigned people in their preferred specialty to be at most 8000.

## Turn 28 - Generic Agent

QUESTION: For the p2 objective, should the model maximize the number of assigned people in their preferred specialty, or should it maximize the number of assigned people in their preferred specialty subject to the constraint that the number of assigned people not in their preferred city is at most 500?

## Turn 28 - User Simulator

The model should maximize the number of assigned people in their preferred specialty. There is no constraint requiring the number of assigned people not in their preferred city to be at most 500.

## Turn 29 - Generic Agent

QUESTION: For the p3 objective, should the model minimize the number of assigned people not in their preferred city, or should it minimize the number of assigned people not in their preferred city subject to the constraint that the number of assigned people in their preferred specialty is at most 8000?

## Turn 29 - User Simulator

The model should minimize the number of assigned people not in their preferred city. There is no constraint requiring the number of assigned people in their preferred specialty to be at most 8000.

## Turn 30 - Generic Agent

QUESTION: For the p2 objective, should the model maximize the number of assigned people in their preferred specialty, or should it maximize the number of assigned people in their preferred specialty subject to the constraint that the number of assigned people not in their preferred city is at most 500?

## Turn 30 - User Simulator

The model should maximize the number of assigned people in their preferred specialty. There is no constraint requiring the number of assigned people not in their preferred city to be at most 500.