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

QUESTION: For the "preferred specialty" goal, should a person count as meeting it only if they are assigned to their single listed preferred specialty, or should any assignment within their suitable specialty set count as meeting it?

## Turn 1 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty.

## Turn 2 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting it only if they are assigned to a branch in their single listed preferred city, or should any assignment in either city count as meeting it?

## Turn 2 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to a branch in their single listed preferred city.

## Turn 3 - Generic Agent

QUESTION: For the branch demand numbers in Table 4-3, should each branch's demand be treated as an exact requirement that must be met exactly, or as a maximum that must not be exceeded?

## Turn 3 - User Simulator

Each branch's demand must be met exactly. No more, no less.

## Turn 4 - Generic Agent

QUESTION: The total branch demand is 8500 but the total available personnel is 9000, so 500 people will be left unassigned; should these 500 unassigned people be treated as simply not placed anywhere (with no penalty or cost attached to them)?

## Turn 4 - User Simulator

Yes, the 500 unassigned people are simply not placed anywhere, with no penalty or cost attached to them.

## Turn 5 - Generic Agent

QUESTION: For the "preferred specialty" goal with a target of 8000, should the number of people meeting their preferred specialty be treated as a target to be achieved as closely as possible (i.e., at least 8000 if feasible, or as close to 8000 as possible), or is it simply a quantity to be reported alongside the minimum unmet preferred-city count?

## Turn 5 - User Simulator

The number of people meeting their preferred specialty is a target to be achieved as closely as possible, specifically aiming for at least 8000 if feasible.

## Turn 6 - Generic Agent

QUESTION: For the "preferred city" goal with a target of 8000, should the number of people meeting their preferred city be treated as a target to be achieved as closely as possible (i.e., at least 8000 if feasible), or is it simply a quantity to be reported alongside the minimum unmet preferred-city count?

## Turn 6 - User Simulator

The number of people meeting their preferred city is a target to be achieved as closely as possible, specifically aiming for at least 8000 if feasible.

## Turn 7 - Generic Agent

QUESTION: If both the preferred-specialty target (at least 8000) and the preferred-city target (at least 8000) cannot be met simultaneously, which goal should take priority in the optimization?

## Turn 7 - User Simulator

The preferred-specialty goal takes priority over the preferred-city goal. We first try to get 8000 people into their preferred specialty, and then, after that, we aim for 8000 people in their preferred city.

## Turn 8 - Generic Agent

QUESTION: When we minimize the number of people not in their preferred city, should this minimization be applied only among the 8500 people who are actually assigned to a branch, or should it also count the 500 unassigned people as "not in their preferred city"?

## Turn 8 - User Simulator

The minimization should be applied only among the 8500 people who are actually assigned to a branch. The 500 unassigned people are not counted as "not in their preferred city."

## Turn 9 - Generic Agent

QUESTION: When we aim for at least 8000 people meeting their preferred specialty, should this count be taken only among the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people?

## Turn 9 - User Simulator

This count should be taken only among the 8500 people who are actually assigned to a branch.

## Turn 10 - Generic Agent

QUESTION: When we aim for at least 8000 people meeting their preferred city, should this count be taken only among the 8500 people who are actually assigned to a branch, or should it also consider the 500 unassigned people?

## Turn 10 - User Simulator

This count should be taken only among the 8500 people who are actually assigned to a branch.

## Turn 11 - Generic Agent

QUESTION: For the "at least 8000" preferred-specialty target, should the model treat 8000 as a hard lower bound that must be satisfied (i.e., the solution is infeasible if fewer than 8000 can be placed in their preferred specialty), or as a soft target to be maximized up to 8000 (i.e., if fewer than 8000 is achievable, the model should still produce the best feasible solution)?

## Turn 11 - User Simulator

It is a soft target to be maximized up to 8000. If fewer than 8000 is achievable, the model should still produce the best feasible solution.

## Turn 12 - Generic Agent

QUESTION: For the "at least 8000" preferred-city target, should the model treat 8000 as a hard lower bound that must be satisfied (i.e., the solution is infeasible if fewer than 8000 can be placed in their preferred city), or as a soft target to be maximized up to 8000 (i.e., if fewer than 8000 is achievable, the model should still produce the best feasible solution)?

## Turn 12 - User Simulator

It is a soft target to be maximized up to 8000. If fewer than 8000 is achievable, the model should still produce the best feasible solution.

## Turn 13 - Generic Agent

QUESTION: Since the preferred-specialty target is maximized first and the preferred-city target is maximized second, should the model maximize the preferred-city count only among solutions that already achieve the maximum possible preferred-specialty count (i.e., a strict lexicographic hierarchy), or should it combine both into a single weighted objective?

## Turn 13 - User Simulator

It should be a strict lexicographic hierarchy. The model should maximize the preferred-city count only among solutions that already achieve the maximum possible preferred-specialty count.

## Turn 14 - Generic Agent

QUESTION: Within the lexicographic hierarchy, after maximizing the preferred-specialty count and then the preferred-city count, should the final objective be to minimize the number of assigned people not in their preferred city, or is the preferred-city count itself the final objective (with the minimum unmet count simply reported as 8500 minus that count)?

## Turn 14 - User Simulator

The preferred-city count itself is the final objective. The minimum unmet count is simply reported as 8500 minus that count.

## Turn 15 - Generic Agent

QUESTION: When a person is assigned to a branch, should they be assigned to exactly one specialty at that branch (i.e., each person goes to exactly one city-specialty combination), or could a person be split across multiple specialties or branches?

## Turn 15 - User Simulator

Each person is assigned to exactly one specialty at one branch. A person cannot be split across multiple specialties or branches.

## Turn 16 - Generic Agent

QUESTION: Since people of the same type are identical in their suitable specialties, preferred specialty, and preferred city, should the model treat people of each type as indistinguishable (i.e., use aggregate flow variables per type-branch combination), or should each individual person be tracked separately?

## Turn 16 - User Simulator

The model should treat people of each type as indistinguishable, using aggregate flow variables per type-branch combination.

## Turn 17 - Generic Agent

QUESTION: For the "suitable specialty" constraint, should a person of a given type be allowed to be assigned to any branch (in either city) as long as the branch's specialty is in their suitable specialty set, or is there an additional restriction that limits which cities a person can be assigned to?

## Turn 17 - User Simulator

A person of a given type can be assigned to any branch in either city, as long as the branch's specialty is in their suitable specialty set. There is no additional restriction limiting which cities a person can be assigned to.

## Turn 18 - Generic Agent

QUESTION: When we maximize the preferred-specialty count, should a person assigned to their preferred specialty in either city count toward this goal, or should they only count if they are in their preferred specialty AND their preferred city?

## Turn 18 - User Simulator

A person assigned to their preferred specialty in either city counts toward the preferred-specialty goal.

## Turn 19 - Generic Agent

QUESTION: When we maximize the preferred-city count, should a person assigned to their preferred city in any specialty (within their suitable set) count toward this goal, or should they only count if they are in their preferred city AND their preferred specialty?

## Turn 19 - User Simulator

A person assigned to their preferred city in any specialty (within their suitable set) counts toward the preferred-city goal.

## Turn 20 - Generic Agent

QUESTION: For the lexicographic hierarchy, should the model first maximize the total number of assigned people in their preferred specialty (across all types), and then, subject to that maximum being achieved, maximize the total number of assigned people in their preferred city (across all types)?

## Turn 20 - User Simulator

Yes, the model should first maximize the total number of assigned people in their preferred specialty (across all types), and then, subject to that maximum being achieved, maximize the total number of assigned people in their preferred city (across all types).

## Turn 21 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Decision Variables:**
- Let x[t][c][s] = number of people of type t assigned to city c, specialty s (aggregate, indistinguishable people within a type).
- t ∈ {1,2,3,4,5,6}, c ∈ {Donghai, Nanjiang}, s ∈ {1,2,3}.
- x[t][c][s] ≥ 0 and integer.

**Constraints:**
1. **Suitable specialty:** x[t][c][s] > 0 only if specialty s is in type t's suitable specialty set (from Table 4-4).
2. **Type supply:** For each type t, the total assigned across all cities and specialties ≤ the number of people of type t (1500 each). The 500 unassigned people are simply not placed; no penalty.
3. **Branch demand (exact):** For each city c and specialty s, the sum of x[t][c][s] over all types t equals the demand in Table 4-3 exactly.
4. **One assignment per person:** Each person is assigned to exactly one (city, specialty) combination (enforced by the type supply constraint being an upper bound and the demand being exact).

**Objective (Lexicographic, two levels):**
- **Level 1 (primary):** Maximize the total number of assigned people in their preferred specialty. A person of type t counts if assigned to specialty = type t's preferred specialty, in either city.
- **Level 2 (secondary, subject to Level 1 being at its maximum):** Maximize the total number of assigned people in their preferred city. A person of type t counts if assigned to city = type t's preferred city, in any specialty within their suitable set.

**Reporting:**
- The minimum number of assigned people not in their preferred city = 8500 − (maximum preferred-city count).
- The 500 unassigned people are not counted in any of the above metrics.

**Key clarifications confirmed:**
- Preferred specialty goal: soft target, maximize up to 8000 (but the true maximum is what the model finds).
- Preferred city goal: soft target, maximize up to 8000 (but the true maximum is what the model finds).
- Strict lexicographic hierarchy: Level 2 is optimized only among solutions achieving the Level 1 maximum.
- Counts are taken only among the 8500 assigned people.
- No additional city restrictions beyond the suitable specialty set.
- People of the same type are indistinguishable (aggregate variables).