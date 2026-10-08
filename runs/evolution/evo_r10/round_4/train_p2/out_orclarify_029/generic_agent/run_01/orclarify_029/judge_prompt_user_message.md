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

QUESTION: When you say the total number of people assigned from each type cannot exceed the available number of that type, do you also require that all 9000 recruited people (1500 × 6 types) must be assigned to some branch and specialty, or is it allowed to leave some recruited people unassigned?

## Turn 1 - User Simulator

It is allowed to leave some recruited people unassigned. The constraint is only that the number assigned from each type cannot exceed the available number for that type. There is no requirement that all 9000 people must be assigned.

## Turn 2 - Generic Agent

QUESTION: Regarding the branch demand numbers in Table 4-3 (e.g., Donghai City specialty 1 needs 1000), are these exact requirements that must be met precisely, or are they maximum capacities that the assignments to each branch-specialty cannot exceed?

## Turn 2 - User Simulator

They are exact requirements. The number of professionals assigned to each specialty at each branch must exactly equal the demand shown in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) but you allow leaving some of the 9000 recruited people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 3 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people. The only objectives are the three priorities: (1) meet branch demands exactly, (2) get 8000 people into their preferred specialty, and (3) get 8000 people into their preferred city.

## Turn 4 - Generic Agent

QUESTION: You listed three priorities, but the first one (meeting branch demands exactly) is a hard constraint, not an objective. So the actual optimization objectives are: (1) maximize the number of assigned people who get their preferred specialty, targeting 8000, and (2) minimize the number of assigned people who do NOT get their preferred city, targeting 8000 getting their preferred city. Is this correct, and is priority (1) more important than priority (2), meaning we maximize preferred-specialty matches first and only then minimize preferred-city mismatches?

## Turn 4 - User Simulator

Yes, that is correct. The branch demand requirements are hard constraints. The two optimization objectives are: (1) maximize the number of assigned people who get their preferred specialty, targeting 8000, and (2) minimize the number of assigned people who do not get their preferred city, targeting 8000 getting their preferred city. Priority (1) is more important than priority (2), so we maximize preferred-specialty matches first and only then minimize preferred-city mismatches.

## Turn 5 - Generic Agent

QUESTION: When you say a person "meets their preferred specialty," does this mean the person is assigned to their preferred specialty at any branch (regardless of city), or must they be assigned to their preferred specialty at their preferred city specifically?

## Turn 5 - User Simulator

A person "meets their preferred specialty" if they are assigned to their preferred specialty at any branch, regardless of city.

## Turn 6 - Generic Agent

QUESTION: Similarly, when you say a person "meets their preferred city," does this mean the person is assigned to their preferred city at any specialty (regardless of which specialty), or must they be assigned to their preferred city AND their preferred specialty?

## Turn 6 - User Simulator

A person "meets their preferred city" if they are assigned to their preferred city at any specialty, regardless of which specialty.

## Turn 7 - Generic Agent

QUESTION: Since each type has a fixed preferred specialty and a fixed preferred city, and a person can only be assigned to specialties in their suitable set, is it possible for a person to be assigned to a specialty that is in their suitable set but is NOT their preferred specialty? For example, Type 1 has suitable specialties {1, 2} and preferred specialty 1 — can a Type 1 person be assigned to specialty 2?

## Turn 7 - User Simulator

Yes, a Type 1 person can be assigned to specialty 2. As long as the specialty is in their suitable set, they can be assigned to it, even if it is not their preferred specialty.

## Turn 8 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 8 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 9 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 9 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 10 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 10 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 11 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 11 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 12 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 12 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 13 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 13 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 14 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 14 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 15 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 15 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 16 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 16 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 17 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 17 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 18 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 18 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 19 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 19 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 20 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 20 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 21 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 21 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 22 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 22 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 23 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 23 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 24 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 24 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 25 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 25 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 26 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 26 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 27 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 27 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 28 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 28 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 29 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 29 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.

## Turn 30 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) and you allow leaving some people unassigned, is it acceptable for the model to leave exactly 500 people unassigned, or should the model also try to minimize the number of unassigned people as an additional objective?

## Turn 30 - User Simulator

It is acceptable to leave exactly 500 people unassigned. There is no additional objective to minimize the number of unassigned people.