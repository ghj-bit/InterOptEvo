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

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to their single listed preferred specialty (e.g., a Type 1 person only counts if assigned to specialty 1), or should any specialty in their suitable set count as meeting the goal?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty. For example, a Type 1 person only counts if assigned to specialty 1.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in their single listed preferred city (e.g., a Type 3 person only counts if assigned to Nanjiang), or should any city count?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single listed preferred city. For example, a Type 3 person only counts if assigned to Nanjiang.

## Turn 3 - Generic Agent

QUESTION: Regarding the branch demand numbers in Table 4-3 (e.g., Donghai specialty 1 = 1000), are these exact requirements that must be met precisely, or are they maximum capacities that may be under-filled?

## Turn 3 - User Simulator

These are exact requirements that must be met precisely. No more, no less.

## Turn 4 - Generic Agent

QUESTION: Since the total branch demand is 8500 but only 9000 people are available, 500 people will be left unassigned. Is it acceptable for some people to be left unassigned (i.e., not placed in any branch), or must all 9000 people be assigned to some branch?

## Turn 4 - User Simulator

It is acceptable for some people to be left unassigned. The constraint is that the total number of people assigned from each type cannot exceed the available number of that type, so not all 9000 need to be placed in a branch.

## Turn 5 - Generic Agent

QUESTION: The problem states three objectives: (1) 8000 meet preferred specialty, (2) 8000 meet preferred city, and (3) minimize the number who cannot be assigned to their preferred city. Are objectives (1) and (2) hard constraints that must be satisfied (i.e., at least 8000 must meet each), or are they soft goals to be maximized as much as possible?

## Turn 5 - User Simulator

They are soft goals to be maximized as much as possible, in strict priority order: first fully meet all branch demand (p1), then try to get 8000 people into their preferred specialty (p2), and finally aim for 8000 people in their preferred city (p3).

## Turn 6 - Generic Agent

QUESTION: In the lexicographic priority order you described, is "minimizing the number of people who cannot be assigned to their preferred city" the same as priority level p3 (i.e., maximizing the number who DO get their preferred city, with target 8000), or is it a separate, lower-priority objective that comes after p3?

## Turn 6 - User Simulator

It is the same as priority level p3. Minimizing the number who cannot be assigned to their preferred city is equivalent to maximizing the number who do get their preferred city, with the target of 8000.

## Turn 7 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), should a person who is left unassigned (not placed in any branch) be counted as NOT meeting their preferred specialty, or should unassigned people be excluded from the count entirely?

## Turn 7 - User Simulator

An unassigned person is counted as NOT meeting their preferred specialty.

## Turn 8 - Generic Agent

QUESTION: For the "preferred city" goal (p3), should a person who is left unassigned (not placed in any branch) be counted as NOT meeting their preferred city, or should unassigned people be excluded from the count entirely?

## Turn 8 - User Simulator

An unassigned person is counted as NOT meeting their preferred city.

## Turn 9 - Generic Agent

QUESTION: When you say "first fully meet all branch demand (p1)," does this mean the branch demand constraints are hard constraints that must always be satisfied (i.e., the model is infeasible if they can't be met), or is p1 a soft goal to be maximized (i.e., fill as much demand as possible, but allow under-filling if necessary)?

## Turn 9 - User Simulator

The branch demand constraints are hard constraints that must always be satisfied. The model is infeasible if they cannot be met.

## Turn 10 - Generic Agent

QUESTION: For the "preferred specialty" goal (p2), is the target of 8000 a hard lower bound (i.e., the model must achieve at least 8000 people in their preferred specialty, and if infeasible the model fails), or is it a soft target to be maximized (i.e., get as close to 8000 as possible, but fewer is acceptable)?

## Turn 10 - User Simulator

It is a soft target to be maximized. Get as close to 8000 as possible, but fewer is acceptable.

## Turn 11 - Generic Agent

QUESTION: For the "preferred city" goal (p3), is the target of 8000 also a soft target to be maximized (get as close to 8000 as possible, but fewer is acceptable), consistent with how you described p2?

## Turn 11 - User Simulator

Yes, the target of 8000 for the preferred city goal (p3) is also a soft target to be maximized. Get as close to 8000 as possible, but fewer is acceptable.

## Turn 12 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision variables:**
- x[t, c, s] = number of people of type t assigned to city c (Donghai or Nanjiang) in specialty s, for t = 1..6, c ∈ {Donghai, Nanjiang}, s ∈ {1, 2, 3}. These are non-negative integers.

**Hard constraints:**
1. **Branch demand (exact):** For each city c and specialty s, the sum of x[t, c, s] over all types t must equal the demand in Table 4-3 (Donghai: 1000, 2000, 1500; Nanjiang: 2000, 1000, 1000).
2. **Type availability (upper bound):** For each type t, the sum of x[t, c, s] over all cities c and specialties s must be ≤ the available number (1500 for each type).
3. **Suitable specialty:** x[t, c, s] = 0 if specialty s is not in type t's suitable specialty set (Table 4-4).

**Lexicographic objective (minimize in order):**
- **p1:** (Implicitly satisfied by hard constraints — all branch demand is met exactly.)
- **p2:** Minimize the number of people NOT in their preferred specialty. Equivalently, maximize the count of assigned people who are in their single listed preferred specialty. Target: 8000 (soft, maximize). An unassigned person counts as NOT meeting preferred specialty.
- **p3:** Minimize the number of people NOT in their preferred city. Equivalently, maximize the count of assigned people who are in their single listed preferred city. Target: 8000 (soft, maximize). An unassigned person counts as NOT meeting preferred city.

**Key facts confirmed:**
- 9000 people total (6 types × 1500), 8500 branch demand, so 500 will be unassigned.
- Unassigned people are allowed and count against both soft goals.
- Both soft goals are maximized (not hard lower bounds).
- The lexicographic order is: p2 first, then p3.