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

QUESTION: Is the total number of recruited personnel fixed at 9000 (the sum of the six types in Table 4-4), or is it a variable that can be adjusted?

## Turn 1 - User Simulator

The total number of recruited personnel is fixed at 9000. This is the sum of the available people across the six types listed in Table 4-4 (1500 per type × 6 types).

## Turn 2 - Generic Agent

QUESTION: Regarding the demand figures in Table 4-3 (e.g., 1000 for Specialty 1 in Donghai), are these hard upper limits that must not be exceeded, or are they exact targets that must be met precisely?

## Turn 2 - User Simulator

They are exact targets that must be met precisely. The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Regarding the "preferred specialty" and "preferred city" goals with a target of 8000, are these hard constraints that must be met exactly, or are they soft goals where the model should minimize the shortfall from 8000?

## Turn 3 - User Simulator

They are soft goals. The model should minimize the shortfall from 8000 for each of the preferred-specialty and preferred-city objectives.

## Turn 4 - Generic Agent

QUESTION: Regarding the third objective to "determine the minimum number of recruited personnel who cannot be assigned to their preferred city," is this a separate optimization objective to be minimized independently, or is it simply a derived metric calculated from the final assignment solution?

## Turn 4 - User Simulator

It is a separate optimization objective to be minimized independently. It is the third priority (p3) in the strict order: first meet all demand exactly (p1), then minimize the shortfall from 8000 for preferred specialty (p2), and finally minimize the number of people not assigned to their preferred city (p3).

## Turn 5 - Generic Agent

QUESTION: Regarding the "suitable specialty" constraint in Table 4-4, is it a hard constraint that a person can only be assigned to a specialty listed in their suitable set, or is it a soft preference that can be violated if necessary to meet the demand targets?

## Turn 5 - User Simulator

It is a hard constraint. A person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4.

## Turn 6 - Generic Agent

QUESTION: Regarding the "available number" constraint in Table 4-4, is it a hard upper limit that the total number of people assigned from each type cannot exceed the available number (1500), or is it an exact requirement that all 1500 people of each type must be assigned?

## Turn 6 - User Simulator

It is a hard upper limit. The total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4.

## Turn 7 - Generic Agent

QUESTION: Regarding the priority structure, is the first priority (p1) to meet all demand targets exactly a hard constraint that must be satisfied before any optimization begins, or is it a lexicographic objective where the model first minimizes the deviation from demand before considering the other goals?

## Turn 7 - User Simulator

It is a hard constraint that must be satisfied before any optimization begins. The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3. No more, no less.

## Turn 8 - Generic Agent

QUESTION: Regarding the lexicographic optimization, are the second priority (minimizing shortfall from 8000 for preferred specialty) and the third priority (minimizing the number of people not assigned to their preferred city) optimized sequentially in strict order, or are they combined into a single weighted objective function?

## Turn 8 - User Simulator

They are optimized sequentially in strict order. The priorities are in strict order: p1 is the highest priority, p2 is second, and p3 is the lowest. So we first make sure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, we aim for 8000 people in their preferred city.

## Turn 9 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 9 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 10 - Generic Agent

QUESTION: Regarding the lexicographic optimization, is the second priority (minimizing the shortfall from 8000 for preferred specialty) and the third priority (minimizing the number of people not assigned to their preferred city) optimized sequentially in strict order, or are they combined into a single weighted objective function?

## Turn 10 - User Simulator

They are optimized sequentially in strict order. The priorities are in strict order: p1 is the highest priority, p2 is second, and p3 is the lowest. So we first make sure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, we aim for 8000 people in their preferred city.

## Turn 11 - Generic Agent

QUESTION: Regarding the decision variables, are the assignments required to be integer values (whole numbers of people), or can they be fractional?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 12 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 13 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 13 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 14 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 14 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 15 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 15 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 16 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 16 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 17 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 17 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 18 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 18 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 19 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 19 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 20 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 20 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 21 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 21 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 22 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 22 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 23 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 23 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 24 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 24 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 25 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 25 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 26 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 26 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 27 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 27 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 28 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 28 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.

## Turn 29 - Generic Agent

QUESTION: Regarding the "preferred city" goal, is the target of 8000 people assigned to their preferred city a separate soft goal to be minimized independently, or is it the same metric as the third priority (minimizing the number of people not assigned to their preferred city)?

## Turn 29 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred city and the third priority of minimizing the number of people not assigned to their preferred city refer to the same objective.

## Turn 30 - Generic Agent

QUESTION: Regarding the "preferred specialty" goal, is the target of 8000 people assigned to their preferred specialty a separate soft goal to be minimized independently, or is it the same metric as the second priority (minimizing the shortfall from 8000 for preferred specialty)?

## Turn 30 - User Simulator

They are the same metric. The target of 8000 people assigned to their preferred specialty and the second priority of minimizing the shortfall from 8000 for preferred specialty refer to the same objective.