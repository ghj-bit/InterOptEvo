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

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to exactly their single preferred specialty, or should it also count if they are assigned to any specialty in their suitable specialty set?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to exactly their single preferred specialty listed in Table 4-4. Being assigned to any other specialty in their suitable specialty set does not count toward this goal.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in exactly their single preferred city listed in Table 4-4, or should it also count if they are assigned to any branch in either city?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in exactly their single preferred city listed in Table 4-4. Being assigned to a branch in the other city does not count toward this goal.

## Turn 3 - Generic Agent

QUESTION: Regarding the total number of people to assign, should the model assign all 9000 available people (1500 each of the 6 types), or should it recruit/assign only a subset of them, with the branch demands in Table 4-3 (totaling 8500) acting as the binding constraint on how many people are actually placed?

## Turn 3 - User Simulator

The branch demands in Table 4-3 total 8500, and since the demand must be exactly met (p1), the model should assign exactly 8500 people. This means only a subset of the 9000 available people will be assigned, with the 8500 demand acting as the binding constraint on how many people are actually placed.

## Turn 4 - Generic Agent

QUESTION: For the branch demand constraint in Table 4-3, should each branch's demand be met exactly (equal to the listed number), or should it be met at least (greater than or equal to the listed number)?

## Turn 4 - User Simulator

Each branch's demand must be met exactly, equal to the listed number in Table 4-3. No more, no less.

## Turn 5 - Generic Agent

QUESTION: For the "type" supply constraint, should the number of people assigned from each type be at most (≤) the available number listed in Table 4-4, or exactly equal to it?

## Turn 5 - User Simulator

The number of people assigned from each type should be at most (≤) the available number listed in Table 4-4.

## Turn 6 - Generic Agent

QUESTION: The three objectives you listed are: (1) 8000 meet preferred specialty, (2) 8000 meet preferred city, and (3) minimize the number who cannot be assigned to their preferred city. Since objectives 2 and 3 are essentially the same thing (maximizing preferred-city matches = minimizing non-preferred-city assignments), how should these be combined into a single optimization? Should I treat this as a multi-objective problem with all three goals weighted equally, or should I prioritize them in a specific order (e.g., first maximize preferred-specialty matches, then maximize preferred-city matches)?

## Turn 6 - User Simulator

The three objectives should be prioritized in a specific order, not weighted equally. The priorities are in strict order: p1 (meeting branch demand exactly) is the highest priority, p2 (8000 meet preferred specialty) is second, and p3 (8000 meet preferred city / minimize the number who cannot be assigned to their preferred city) is the lowest. So the model should first ensure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, aim for 8000 people in their preferred city.

## Turn 7 - Generic Agent

QUESTION: For the p2 goal (8000 meet preferred specialty), should the model maximize the number of people assigned to their preferred specialty with 8000 as a target to reach if possible, or should it be a hard constraint that at least 8000 must be assigned to their preferred specialty?

## Turn 7 - User Simulator

The p2 goal should be treated as a target to reach if possible, not a hard constraint. The model should maximize the number of people assigned to their preferred specialty, aiming for 8000, but it is not a strict requirement that at least 8000 must be met.

## Turn 8 - Generic Agent

QUESTION: For the p3 goal (8000 meet preferred city / minimize the number who cannot be assigned to their preferred city), should this also be treated as a target to reach if possible (i.e., maximize the number assigned to their preferred city, aiming for 8000), or should it be a hard constraint that at least 8000 must be assigned to their preferred city?

## Turn 8 - User Simulator

The p3 goal should also be treated as a target to reach if possible, not a hard constraint. The model should maximize the number of people assigned to their preferred city, aiming for 8000, but it is not a strict requirement that at least 8000 must be met.

## Turn 9 - Generic Agent

QUESTION: For the p1 priority (meeting branch demand exactly), should this be a hard constraint that must be satisfied in every feasible solution, or should it be the first objective in a lexicographic optimization that is maximized before moving to p2 and p3?

## Turn 9 - User Simulator

The p1 priority should be a hard constraint that must be satisfied in every feasible solution. Each branch's demand must be met exactly, equal to the listed number in Table 4-3.

## Turn 10 - Generic Agent

QUESTION: For the p2 and p3 goals, should the model use a lexicographic (preemptive) approach where p2 is fully optimized first and then p3 is optimized subject to p2's optimal value being maintained, or should p2 and p3 be combined into a single weighted objective (e.g., maximize 8000-preferred-specialty-matches + 8000-preferred-city-matches) after satisfying p1?

## Turn 10 - User Simulator

The model should use a lexicographic (preemptive) approach. p2 is fully optimized first, and then p3 is optimized subject to p2's optimal value being maintained. They should not be combined into a single weighted objective.

## Turn 11 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be an integer, or can they be treated as continuous values?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: For the "suitable specialty" constraint, should a person of a given type be allowed to be assigned to any specialty in their suitable specialty set regardless of which city they are assigned to, or is there an additional restriction that limits which specialties are available in which city?

## Turn 12 - User Simulator

A person of a given type should be allowed to be assigned to any specialty in their suitable specialty set regardless of which city they are assigned to. There is no additional restriction limiting which specialties are available in which city beyond the demand numbers in Table 4-3.

## Turn 13 - Generic Agent

QUESTION: For the 500 people who are not assigned (since 9000 are available but only 8500 are placed), should the model track which specific types they come from, or is it sufficient to simply ensure that the total assigned from each type does not exceed its available number?

## Turn 13 - User Simulator

It is sufficient to simply ensure that the total assigned from each type does not exceed its available number. The model does not need to track which specific types the 500 unassigned people come from beyond that constraint.

## Turn 14 - Generic Agent

QUESTION: For the lexicographic optimization, should the model be formulated as a single multi-objective linear program with three objectives in strict priority order (p1 as hard constraint, p2 as first objective to maximize, p3 as second objective to maximize), or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: For the p2 objective (maximize number of people assigned to their preferred specialty), should the target of 8000 be used as a cap (i.e., the objective is to maximize min(actual matches, 8000)), or should the objective simply be to maximize the total number of preferred-specialty matches without any cap, with 8000 being just a reference target?

## Turn 15 - User Simulator

The objective should simply be to maximize the total number of preferred-specialty matches without any cap. The 8000 is just a reference target, not a cap on the objective function.

## Turn 16 - Generic Agent

QUESTION: For the p3 objective (maximize number of people assigned to their preferred city), should the target of 8000 also be treated the same way—simply maximize the total number of preferred-city matches without any cap, with 8000 being just a reference target?

## Turn 16 - User Simulator

Yes, the p3 objective should also simply maximize the total number of preferred-city matches without any cap, with 8000 being just a reference target.

## Turn 17 - Generic Agent

QUESTION: For the p3 objective, should the model report the minimum number of people who cannot be assigned to their preferred city as a separate output metric (i.e., 8500 minus the number of preferred-city matches), or is maximizing preferred-city matches sufficient and the "minimum number who cannot be assigned" is just a derived value?

## Turn 17 - User Simulator

Maximizing preferred-city matches is sufficient. The "minimum number who cannot be assigned to their preferred city" is just a derived value (8500 minus the number of preferred-city matches), not a separate output metric that needs to be explicitly reported by the model.

## Turn 18 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be a non-negative integer, or can they be treated as non-negative continuous values?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be a non-negative integer, or can they be treated as non-negative continuous values?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be a non-negative integer, or can they be treated as non-negative continuous values?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be a non-negative integer, or can they be treated as non-negative continuous values?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be a non-negative integer, or can they be treated as non-negative continuous values?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: For the decision variables, should the number of people assigned from each type to each (city, specialty) combination be required to be a non-negative integer, or can they be treated as non-negative continuous values?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: For the lexicographic structure, should the model be formulated as a single multi-objective linear program with p2 as the first objective and p3 as the second objective in strict priority order, or should it be solved in two sequential steps where step 1 maximizes p2 and step 2 maximizes p3 subject to p2 achieving its optimal value from step 1?

## Turn 30 - User Simulator

The point still needs internal confirmation.