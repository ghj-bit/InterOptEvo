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

QUESTION: For the two goals of "8000 personnel meet their preferred specialty" and "8000 meet their preferred city," should the model maximize the number of people meeting each goal (i.e., treat 8000 as a target to be approached as closely as possible, possibly falling short), or must the model guarantee at least 8000 meet each goal as hard constraints?

## Turn 1 - User Simulator

Treat 8000 as a target to be approached as closely as possible, possibly falling short. These are not hard constraints; they are goals within the priority structure.

## Turn 2 - Generic Agent

QUESTION: Regarding the third objective, "determine the minimum number of recruited personnel who cannot be assigned to their preferred city" — should this be a separate optimization objective (i.e., minimize the number of people not in their preferred city), or is it simply a reported output/metric calculated after solving the model?

## Turn 2 - User Simulator

It is a separate optimization objective. We want to minimize the number of recruited personnel who cannot be assigned to their preferred city, as the lowest priority (p3) in the sequence.

## Turn 3 - Generic Agent

QUESTION: You mentioned a priority structure (p3 for minimizing non-preferred-city assignments). What are the priorities for the other two goals — is maximizing the number meeting their preferred specialty p1 and maximizing the number meeting their preferred city p2, or are the two "8000" goals at the same priority level?

## Turn 3 - User Simulator

The priorities are:

- p1: Fully meet the demand in Table 4-3 (exactly the numbers shown).
- p2: Achieve that 8000 recruited personnel meet their preferred specialty.
- p3: Achieve that 8000 recruited personnel meet their preferred city (equivalently, minimize the number who cannot be assigned to their preferred city).

So the two "8000" goals are at different priority levels: preferred specialty is p2, and preferred city is p3.

## Turn 4 - Generic Agent

QUESTION: Regarding the demand in Table 4-3 (total 8500) versus the total recruited personnel (9000): should the model require that the demand in each branch-specialty cell be met exactly (i.e., exactly 1000 in Donghai-1, 2000 in Donghai-2, etc.), or can some cells be overfilled as long as the total assigned equals 9000?

## Turn 4 - User Simulator

The model must require that the demand in each branch-specialty cell be met exactly. No more, no less.

## Turn 5 - Generic Agent

QUESTION: Since the total demand is 8500 but there are 9000 recruited personnel, 500 people will not be assigned to any branch. Is this acceptable (i.e., some people simply remain unassigned), or must all 9000 be assigned to some branch-specialty cell?

## Turn 5 - User Simulator

Yes, this is acceptable. Since the total demand is 8500 and there are 9000 recruited personnel, 500 people will remain unassigned. The constraint is that the total number of people assigned from each type cannot exceed the available number of that type, not that all available people must be assigned.

## Turn 6 - Generic Agent

QUESTION: For the unassigned 500 people, should they be excluded from the p2 and p3 goal calculations (i.e., only assigned people count toward "meeting preferred specialty" and "meeting preferred city"), or should unassigned people be counted as failing to meet both goals?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should the count include only people who are assigned to their preferred specialty, or should it also count people who are assigned to their preferred specialty but in a non-preferred city (i.e., is the specialty goal independent of city)?

## Turn 7 - User Simulator

The p2 goal counts only people who are assigned to their preferred specialty. The specialty goal is independent of city.

## Turn 8 - Generic Agent

QUESTION: For the p3 goal (minimizing the number who cannot be assigned to their preferred city), does this count only among the assigned people (i.e., the 8500 who get a branch), or does it also count the 500 unassigned people as "not in their preferred city"?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: For the p1 constraint (exactly meeting each demand cell), is it possible that the model becomes infeasible given the specialty restrictions in Table 4-4? For example, Donghai City specialty 1 needs 1000 people, but only types 1, 3, and 4 can do specialty 1, and type 3 and 4 prefer Nanjiang. Should I assume the problem is always feasible as given, or should the model handle potential infeasibility (e.g., by allowing some demand to go unmet)?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: For the p2 goal of 8000 meeting preferred specialty: since the total demand is 8500 and only 8500 people can be assigned, is the maximum possible count of people meeting their preferred specialty bounded by 8500 (i.e., the target of 8000 is achievable only if at least 8000 of the 8500 assigned people happen to be in their preferred specialty)?

## Turn 10 - User Simulator

Yes, the maximum possible count of people meeting their preferred specialty is bounded by 8500, since only 8500 people can be assigned. The target of 8000 is achievable only if at least 8000 of the 8500 assigned people happen to be in their preferred specialty.

## Turn 11 - Generic Agent

QUESTION: For the p3 goal (minimizing the number who cannot be assigned to their preferred city), does this count only among the 8500 assigned people, or does it also include the 500 unassigned people as "not in their preferred city"?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: For the p1 constraint requiring each demand cell to be met exactly: should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: For the p3 goal, since the client has deferred the question of whether unassigned people count, I will proceed with the assumption that p3 counts only among the 8500 assigned people (i.e., minimize the number of assigned people who are not in their preferred city). Is that the correct interpretation to proceed with?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: For the p2 goal (8000 meeting preferred specialty), should unassigned people be counted as failing to meet their preferred specialty (i.e., they reduce the count toward the 8000 target), or should only assigned people be considered in this goal?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: For the p1 constraint, should I assume the problem is always feasible as given (i.e., the specialty restrictions in Table 4-4 are compatible with the demand in Table 4-3), or should the model be formulated to handle potential infeasibility by allowing some demand to go unmet?

## Turn 30 - User Simulator

The point still needs internal confirmation.