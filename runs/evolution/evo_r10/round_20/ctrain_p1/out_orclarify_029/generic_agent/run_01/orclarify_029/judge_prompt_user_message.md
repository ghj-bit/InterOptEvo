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

QUESTION: For the two 8000-person goals (preferred specialty and preferred city), should the model treat them as soft goals to be maximized as much as possible (i.e., maximize the number of people who get their preferred specialty and the number who get their preferred city, with 8000 as an aspirational target), or as hard constraints that must be met exactly (i.e., require at least 8000 people to get their preferred specialty and at least 8000 to get their preferred city, even if that forces other trade-offs)?

## Turn 1 - User Simulator

They are soft goals. We want to maximize the number of people who get their preferred specialty and the number who get their preferred city, with 8000 as the aspirational target for each. They are not hard constraints that must be met exactly.

## Turn 2 - Generic Agent

QUESTION: The total demand across all branches and specialties is 8500, but the total number of recruited personnel is 9000. Should the model require that all 8500 demand slots be filled exactly (i.e., each branch-specialty demand is met exactly), or is it acceptable to leave some demand slots unfilled (i.e., demand is an upper bound on how many can be assigned to each branch-specialty)?

## Turn 2 - User Simulator

The model must require that all 8500 demand slots be filled exactly. Each branch-specialty demand must be met exactly as shown in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Since there are 9000 recruited personnel but only 8500 demand slots, 500 people will not be assigned to any branch. Should these 500 unassigned people be treated as a leftover group that simply exists (with no cost or penalty in the objective), or should the model also try to minimize the number of unassigned people (i.e., maximize the number assigned to some branch-specialty)?

## Turn 3 - User Simulator

The 500 unassigned people are simply a leftover group that exists. There is no cost or penalty in the objective for them, and the model does not need to minimize their number. The priority is to fill the 8500 demand slots exactly, and the remaining 500 are just not assigned.

## Turn 4 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person be counted as meeting their preferred specialty only if they are assigned to their preferred specialty in their preferred city (i.e., both city and specialty match), or should they be counted as meeting their preferred specialty as long as they are assigned to their preferred specialty in any city (regardless of which city)?

## Turn 4 - User Simulator

A person is counted as meeting their preferred specialty as long as they are assigned to their preferred specialty in any city, regardless of which city. The city does not need to match for this goal.

## Turn 5 - Generic Agent

QUESTION: For the "preferred city" goal, should a person be counted as meeting their preferred city only if they are assigned to their preferred city in their preferred specialty (i.e., both city and specialty match), or should they be counted as meeting their preferred city as long as they are assigned to any specialty in their preferred city (regardless of which specialty)?

## Turn 5 - User Simulator

A person is counted as meeting their preferred city as long as they are assigned to any specialty in their preferred city, regardless of which specialty. The specialty does not need to match for this goal.

## Turn 6 - Generic Agent

QUESTION: The objective mentions three things: (1) maximize the number who get their preferred specialty, (2) maximize the number who get their preferred city, and (3) determine the minimum number who cannot be assigned to their preferred city. Since goals (1) and (2) are soft goals to be maximized, and (3) is essentially the complement of (2) (i.e., 9000 minus the number who get their preferred city), should the model treat this as a single multi-objective problem that simultaneously maximizes both preferred-specialty count and preferred-city count (requiring a trade-off or weighting between them), or should it be a lexicographic/priority problem where one goal takes precedence over the other?

## Turn 6 - User Simulator

It should be a lexicographic/priority problem. The priorities are in strict order: first, fully meet all demand (p1); second, maximize the number of people who get their preferred specialty (p2); and third, maximize the number of people who get their preferred city (p3). So we first make sure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, we aim for 8000 people in their preferred city.

## Turn 7 - Generic Agent

QUESTION: Since the total number of recruited personnel is 9000 and the total demand is 8500, exactly 500 people will be unassigned. For the "preferred city" goal, should the 500 unassigned people be counted as NOT meeting their preferred city (i.e., they are part of the "cannot be assigned to preferred city" count), or should the preferred-city goal only consider the 8500 assigned people (i.e., unassigned people are excluded from both the numerator and denominator of the preferred-city metric)?

## Turn 7 - User Simulator

The 500 unassigned people should be counted as NOT meeting their preferred city. They are part of the "cannot be assigned to preferred city" count.

## Turn 8 - Generic Agent

QUESTION: For the "preferred specialty" goal, should the 500 unassigned people also be counted as NOT meeting their preferred specialty (i.e., they are part of the "cannot be assigned to preferred specialty" count), or should the preferred-specialty goal only consider the 8500 assigned people (i.e., unassigned people are excluded from the preferred-specialty metric)?

## Turn 8 - User Simulator

The 500 unassigned people should be counted as NOT meeting their preferred specialty. They are part of the "cannot be assigned to preferred specialty" count.

## Turn 9 - Generic Agent

QUESTION: The problem states that "a person can only be assigned to a specialty that is listed in their suitable specialty set." Does this mean that a person of a given type can only be assigned to a branch-specialty combination where the specialty is in their suitable set, regardless of which city the branch is in? For example, Type 1 people (suitable specialties: 1, 2) can be assigned to Specialty 1 or 2 in either Donghai or Nanjiang, but cannot be assigned to Specialty 3 in either city. Is that correct?

## Turn 9 - User Simulator

Yes, that is correct. A person of a given type can only be assigned to a branch-specialty combination where the specialty is in their suitable set, regardless of which city the branch is in. For example, Type 1 people (suitable specialties: 1, 2) can be assigned to Specialty 1 or 2 in either Donghai or Nanjiang, but cannot be assigned to Specialty 3 in either city.

## Turn 10 - Generic Agent

QUESTION: The problem mentions "the total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4." Since each type has exactly 1500 people available, and the total demand is 8500 (less than 9000 total available), should the model allow that some people of a given type may be left unassigned (i.e., the number assigned from each type is ≤ 1500), or must all 1500 people of each type be assigned to some branch-specialty (i.e., the number assigned from each type is exactly 1500)?

## Turn 10 - User Simulator

The model should allow that some people of a given type may be left unassigned. The number assigned from each type is ≤ 1500, not exactly 1500.

## Turn 11 - Generic Agent

QUESTION: For the lexicographic objective, the first priority is to "fully meet all demand." Since the total demand is 8500 and total available personnel is 9000, this is always feasible. Should the first priority simply be a hard constraint (i.e., all demand slots must be filled exactly, as you already confirmed), or should it be treated as a lexicographic objective level that is optimized before the other two goals (which would be redundant given it's always feasible)?

## Turn 11 - User Simulator

The first priority should simply be a hard constraint. All demand slots must be filled exactly as shown in Table 4-3. It does not need to be treated as a lexicographic objective level, since it is always feasible and must be met regardless.

## Turn 12 - Generic Agent

QUESTION: For the lexicographic objective, the second priority is to maximize the number of people who get their preferred specialty, and the third priority is to maximize the number who get their preferred city. Should the model report both the maximum preferred-specialty count and the maximum preferred-city count (achieving the best possible preferred-city count among all solutions that already achieve the maximum preferred-specialty count), or should it only report the maximum preferred-city count (with the preferred-specialty count being whatever it ends up being as a byproduct)?

## Turn 12 - User Simulator

The model should report both the maximum preferred-specialty count and the maximum preferred-city count. The preferred-city count should be the best possible among all solutions that already achieve the maximum preferred-specialty count.

## Turn 13 - Generic Agent

QUESTION: The problem asks to "determine the minimum number of recruited personnel who cannot be assigned to their preferred city." Since you confirmed that unassigned people count as NOT meeting their preferred city, this minimum number would be 9000 minus the maximum preferred-city count. Should the model explicitly report this minimum number as a separate output, or is it sufficient to report the maximum preferred-city count and let the reader compute the difference?

## Turn 13 - User Simulator

The model should explicitly report this minimum number as a separate output.

## Turn 14 - Generic Agent

QUESTION: For the decision variables, should the number of people of each type assigned to each branch-specialty combination be required to be integer (i.e., you cannot assign 0.5 of a person), or can they be treated as continuous (which would be fine in practice given the large numbers, but is a modeling choice)?

## Turn 14 - User Simulator

The number of people of each type assigned to each branch-specialty combination should be required to be integer.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or business rules I should be aware of that are not already captured in the tables and our discussion so far? For example, are there any restrictions on how many people of a given type can be assigned to a specific city, or any other hidden rules?

## Turn 15 - User Simulator

No, there are no other constraints or business rules beyond what is already captured in the tables and our discussion so far.

## Turn 16 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision Variables:**
- x[t, c, s] = number of people of type t assigned to city c, specialty s (integer, ≥ 0)
- for t ∈ {1,...,6}, c ∈ {Donghai, Nanjiang}, s ∈ {1, 2, 3}

**Hard Constraints:**
1. **Demand met exactly:** For each (city, specialty) pair, the sum of x[t, c, s] over all types t equals the demand in Table 4-3.
2. **Type availability:** For each type t, the sum of x[t, c, s] over all cities c and specialties s is ≤ 1500.
3. **Suitable specialty:** x[t, c, s] = 0 if specialty s is not in the suitable specialty set of type t (per Table 4-4).

**Lexicographic Objective (two levels, since demand is a hard constraint):**
- **Priority 1 (P2):** Maximize the total number of people assigned to their preferred specialty (in any city). A person of type t is counted if assigned to specialty = preferred_specialty[t]. The 500 unassigned people count as NOT meeting this goal.
- **Priority 2 (P3):** Subject to achieving the maximum from Priority 1, maximize the total number of people assigned to their preferred city (in any specialty). A person of type t is counted if assigned to city = preferred_city[t]. The 500 unassigned people count as NOT meeting this goal.

**Outputs to Report:**
1. The maximum number of people who get their preferred specialty (target: 8000).
2. The maximum number of people who get their preferred city (target: 8000), among all solutions achieving the maximum preferred-specialty count.
3. The minimum number of recruited personnel who cannot be assigned to their preferred city (= 9000 − maximum preferred-city count).
4. The full assignment plan (values of x[t, c, s]).

**Key Parameters (from tables):**
- Demand: Donghai-S1=1000, Donghai-S2=2000, Donghai-S3=1500, Nanjiang-S1=2000, Nanjiang-S2=1000, Nanjiang-S3=1000 (total 8500).
- Type data (count, suitable specialties, preferred specialty, preferred city):
  - Type 1: 1500, {1,2}, pref spec 1, pref city Donghai
  - Type 2: 1500, {2,3}, pref spec 2, pref city Donghai
  - Type 3: 1500, {1,3}, pref spec 1, pref city Nanjiang
  - Type 4: 1500, {1,3}, pref spec 3, pref city Nanjiang
  - Type 5: 1500, {2,3}, pref spec 3, pref city Donghai
  - Type 6: 1500, {3}, pref spec 3, pref city Nanjiang

**Notes:**
- Total available = 9000, total demand = 8500, so exactly 500 people will be unassigned.
- Unassigned people count as NOT meeting either preferred-specialty or preferred-city goals.
- All decision variables are integer.
- No other constraints or business rules apply.