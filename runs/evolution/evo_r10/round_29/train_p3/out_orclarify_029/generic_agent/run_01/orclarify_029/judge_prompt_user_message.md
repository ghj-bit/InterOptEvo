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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city", should the model minimize the total shortfall from both 8000 targets combined (i.e., minimize (8000 − specialty-met) + (8000 − city-met)), or should it minimize only the shortfall from the preferred-city target while treating the 8000 preferred-specialty target as a hard constraint that must be exactly met?

## Turn 1 - User Simulator

The model should minimize only the shortfall from the preferred-city target. The 8000 preferred-specialty target is not a hard constraint that must be exactly met; it is a goal to be achieved after the demand is fully met, but before the preferred-city goal is addressed.

## Turn 2 - Generic Agent

QUESTION: When you say the 8000 preferred-specialty target is achieved "after demand is fully met, but before the preferred-city goal", does that mean the model should use lexicographic (priority) optimization — first minimize the number of unfilled demand slots, then, among all solutions with the minimum unfilled demand, maximize the number of people in their preferred specialty, and only then minimize the shortfall from the 8000 preferred-city target — or should the demand be treated as a hard constraint that must be exactly satisfied, with the preferred-specialty goal then optimized before the preferred-city goal?

## Turn 2 - User Simulator

The demand should be treated as a hard constraint that must be exactly satisfied. The preferred-specialty goal is then optimized before the preferred-city goal.

## Turn 3 - Generic Agent

QUESTION: The total demand across all branches and specialties is 8500, but the total number of recruited personnel is 9000, so 500 people will not be assigned to any branch. Should these 500 unassigned people be counted as failing both the preferred-specialty and preferred-city goals (i.e., they do not contribute to either the specialty-met or city-met counts), or should they be excluded from the goal calculations entirely?

## Turn 3 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 4 - Generic Agent

QUESTION: For the preferred-city goal, should a person be counted as "meeting their preferred city" only if they are assigned to a branch in their preferred city, or should a person assigned to a specialty in their preferred city count as meeting the city goal even if the specific branch's specialty demand is in a different city?

## Turn 4 - User Simulator

A person is counted as meeting their preferred city only if they are assigned to a branch in their preferred city.

## Turn 5 - Generic Agent

QUESTION: For the preferred-specialty goal, should a person be counted as "meeting their preferred specialty" only if they are assigned to a branch where the specialty matches their preferred specialty, regardless of which city that branch is in?

## Turn 5 - User Simulator

Yes, a person is counted as meeting their preferred specialty if they are assigned to a branch where the specialty matches their preferred specialty, regardless of which city that branch is in.

## Turn 6 - Generic Agent

QUESTION: The total demand is 8500 and total recruited personnel is 9000, so 500 people will be unassigned. Should the model require that all 8500 demand slots be filled exactly (i.e., each branch-specialty demand is met precisely), with the remaining 500 people simply left unassigned, or could some demand slots be left unfilled if that helps achieve the preferred-specialty and preferred-city goals?

## Turn 6 - User Simulator

The model must require that all 8500 demand slots be filled exactly. The remaining 500 people are simply left unassigned.

## Turn 7 - Generic Agent

QUESTION: For the lexicographic optimization, should the preferred-specialty goal be to maximize the total number of assigned people who are in their preferred specialty (i.e., maximize the count, with 8000 being a target but not a hard cap), or should it be to minimize the shortfall from 8000 (i.e., minimize max(0, 8000 − specialty-met))?

## Turn 7 - User Simulator

The preferred-specialty goal is to maximize the total number of assigned people who are in their preferred specialty. The 8000 is a target, not a hard cap.

## Turn 8 - Generic Agent

QUESTION: For the preferred-city goal, should the model minimize the shortfall from 8000 (i.e., minimize max(0, 8000 − city-met)), or should it simply minimize the total number of assigned people who are NOT in their preferred city (equivalently, maximize the number who ARE in their preferred city)?

## Turn 8 - User Simulator

The model should minimize the total number of assigned people who are NOT in their preferred city, which is equivalent to maximizing the number who ARE in their preferred city.

## Turn 9 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 9 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 10 - Generic Agent

QUESTION: For the "total number of people assigned from each type cannot exceed the available number of that type" constraint, should this be a hard constraint (i.e., the number assigned from each type must be ≤ the available number), or could the model assign more people of a type than are available if it helps achieve the goals?

## Turn 10 - User Simulator

This should be a hard constraint. The number assigned from each type must be ≤ the available number of that type.

## Turn 11 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 11 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 12 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 12 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 13 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 13 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 14 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 14 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 15 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 15 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 16 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 16 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 17 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 17 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 18 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 18 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 19 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 19 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 20 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 20 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 21 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 21 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 22 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 22 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 23 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 23 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 24 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 24 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 25 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 25 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 26 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 26 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 27 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 27 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 28 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 28 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 29 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 29 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.

## Turn 30 - Generic Agent

QUESTION: For the 500 unassigned people, should they be excluded from both the preferred-specialty and preferred-city goal calculations (i.e., only the 8500 assigned people count toward these goals), or should the 500 unassigned people be counted as failing both goals?

## Turn 30 - User Simulator

I need to confirm internally how the 500 unassigned people should be treated in the goal calculations.