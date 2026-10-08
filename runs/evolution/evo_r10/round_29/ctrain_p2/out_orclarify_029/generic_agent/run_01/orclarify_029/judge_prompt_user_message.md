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

QUESTION: For the two goals of "8000 personnel meet their preferred specialty" and "8000 meet their preferred city," should the model minimize the total shortfall from both 8000 targets combined (i.e., minimize (8000 − specialty-met) + (8000 − city-met)), or should it minimize only the shortfall on the preferred-city goal while treating the 8000 preferred-specialty target as a hard constraint that must be met exactly?

## Turn 1 - User Simulator

No, it should not minimize the combined shortfall, and it should not treat the 8000 preferred-specialty target as a hard constraint.

The two goals are separate objectives with different priorities. The 8000 preferred-specialty target is a goal to be achieved at the second priority level, and the 8000 preferred-city target is a goal to be achieved at the third priority level. The model should first satisfy the demand exactly, then maximize the number of people meeting their preferred specialty (aiming for 8000), and then, subject to the previous levels being satisfied, maximize the number of people meeting their preferred city (aiming for 8000).

## Turn 2 - Generic Agent

QUESTION: You mentioned the model should "first satisfy the demand exactly" as the top priority — does this mean the branch demands in Table 4-3 (e.g., 1000 for Donghai specialty 1, 2000 for Donghai specialty 2, etc.) must be met exactly as equality constraints, or should they be treated as upper bounds (demand not exceeded) with the priority-1 objective being to maximize total filled demand?

## Turn 2 - User Simulator

The branch demands in Table 4-3 must be met exactly as equality constraints. The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: The total demand across all branches is 8500 (1000+2000+1500+2000+1000+1000), but the total number of recruited personnel is 9000 (6 types × 1500). Since demand must be met exactly, 500 people will be left unassigned — is that acceptable, and should those 500 simply be excluded from the model (i.e., the model only assigns exactly 8500 people and the remaining 500 are not counted toward any goal)?

## Turn 3 - User Simulator

Yes, that is acceptable. The model only assigns exactly 8500 people to meet the demand, and the remaining 500 are not counted toward any goal.

## Turn 4 - Generic Agent

QUESTION: For the "preferred specialty" goal, a person meets their preferred specialty if they are assigned to the specialty listed in the "Preferred Specialty" column of Table 4-4, regardless of which city they are assigned to — is that correct, or does a person only count as meeting their preferred specialty if they are assigned to both their preferred specialty AND their preferred city?

## Turn 4 - User Simulator

A person meets their preferred specialty if they are assigned to the specialty listed in the "Preferred Specialty" column of Table 4-4, regardless of which city they are assigned to.

## Turn 5 - Generic Agent

QUESTION: For the "preferred city" goal, a person meets their preferred city if they are assigned to the city listed in the "Preferred City" column of Table 4-4, regardless of which specialty they are assigned to — is that correct, or does a person only count as meeting their preferred city if they are assigned to both their preferred city AND their preferred specialty?

## Turn 5 - User Simulator

A person meets their preferred city if they are assigned to the city listed in the "Preferred City" column of Table 4-4, regardless of which specialty they are assigned to.

## Turn 6 - Generic Agent

QUESTION: The "Suitable Specialty" column in Table 4-4 restricts which specialties a person can be assigned to, but does it also restrict which city they can be assigned to — for example, can a Type 1 person (suitable specialties 1,2; preferred city Donghai) be assigned to specialty 1 in Nanjiang City, or must they only be assigned to their preferred city?

## Turn 6 - User Simulator

The "Suitable Specialty" column only restricts which specialties a person can be assigned to. It does not restrict which city they can be assigned to. A Type 1 person can be assigned to specialty 1 in Nanjiang City, as long as specialty 1 is in their suitable specialty set.

## Turn 7 - Generic Agent

QUESTION: The "Number of People" column in Table 4-4 (1500 per type) represents the total available supply of each type — is this an upper bound (at most 1500 of each type can be assigned), or must exactly 1500 of each type be assigned (meaning all 9000 must be placed, which would conflict with the 8500 demand)?

## Turn 7 - User Simulator

This is an upper bound. At most 1500 of each type can be assigned.

## Turn 8 - Generic Agent

QUESTION: The problem statement mentions "determine the minimum number of recruited personnel who cannot be assigned to their preferred city" — is this a separate reporting quantity that the model should compute as a result (i.e., 9000 minus the number who get their preferred city, or 8500 assigned minus the number who get their preferred city), or is it actually the primary objective that the model should minimize directly?

## Turn 8 - User Simulator

It is a separate reporting quantity that the model should compute as a result. It is not the primary objective that the model should minimize directly.

## Turn 9 - Generic Agent

QUESTION: For the reporting quantity "minimum number of recruited personnel who cannot be assigned to their preferred city," should this be computed over all 9000 recruited personnel (including the 500 unassigned), or only over the 8500 who are actually assigned to a branch?

## Turn 9 - User Simulator

It should be computed over all 9000 recruited personnel, including the 500 unassigned.

## Turn 10 - Generic Agent

QUESTION: For the lexicographic priority structure, the priority-2 objective is to maximize the number of assigned people meeting their preferred specialty (targeting 8000), and priority-3 is to maximize the number meeting their preferred city (targeting 8000) — should these be hard-capped at 8000 (i.e., once 8000 is reached, no further improvement is sought), or should the model simply maximize the count without any cap, with 8000 being just a reference target?

## Turn 10 - User Simulator

The model should simply maximize the count without any cap. The 8000 is just a reference target.

## Turn 11 - Generic Agent

QUESTION: Since the model is lexicographic (priority 1: meet demand exactly, priority 2: maximize preferred-specialty count, priority 3: maximize preferred-city count), and demand is met exactly in priority 1, does priority 2 mean: among all assignments that meet demand exactly, maximize the number of people whose assigned specialty equals their preferred specialty — and then priority 3 means: among all assignments that meet demand exactly AND achieve the maximum preferred-specialty count, maximize the number of people whose assigned city equals their preferred city?

## Turn 11 - User Simulator

Yes, that is correct. Priority 2 means: among all assignments that meet demand exactly, maximize the number of people whose assigned specialty equals their preferred specialty. Priority 3 means: among all assignments that meet demand exactly AND achieve the maximum preferred-specialty count, maximize the number of people whose assigned city equals their preferred city.

## Turn 12 - Generic Agent

QUESTION: For the decision variables, should the model track assignments at the level of (type, city, specialty) — i.e., how many people of each type are assigned to each city-specialty combination — or is there any additional granularity needed, such as distinguishing between people who get their preferred specialty versus those who don't within the same type-city-specialty cell?

## Turn 12 - User Simulator

The model should track assignments at the level of (type, city, specialty). No additional granularity is needed.

## Turn 13 - Generic Agent

QUESTION: I have confirmed all the key structural elements. Let me verify one final point: the "preferred specialty" and "preferred city" goals only count among the 8500 assigned people (since the 500 unassigned are not counted toward any goal), but the reporting quantity "number who cannot be assigned to their preferred city" counts over all 9000 — is that distinction correct, meaning the 500 unassigned are automatically counted as "not assigned to their preferred city" in the reporting quantity?

## Turn 13 - User Simulator

Yes, that distinction is correct. The "preferred specialty" and "preferred city" goals only count among the 8500 assigned people. The reporting quantity "number who cannot be assigned to their preferred city" counts over all 9000, meaning the 500 unassigned are automatically counted as "not assigned to their preferred city" in the reporting quantity.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision Variables:**
- x[t, c, s] = number of people of type t assigned to city c, specialty s, where t ∈ {1,...,6}, c ∈ {Donghai, Nanjiang}, s ∈ {1, 2, 3}.

**Constraints:**
1. **Demand (equality):** For each (city, specialty) pair, the sum over all types of x[t, c, s] must exactly equal the demand in Table 4-3 (total 8500).
2. **Supply (upper bound):** For each type t, the sum over all (c, s) of x[t, c, s] ≤ 1500.
3. **Suitable specialty:** x[t, c, s] = 0 if specialty s is not in the suitable specialty set of type t (per Table 4-4).
4. **Non-negativity and integrality:** x[t, c, s] ≥ 0 and integer.

**Lexicographic Objective (3 priority levels):**
- **Priority 1:** Satisfied by the equality constraints (demand met exactly).
- **Priority 2:** Maximize the number of assigned people whose assigned specialty equals their preferred specialty (from Table 4-4). This counts only among the 8500 assigned.
- **Priority 3:** Subject to achieving the maximum priority-2 value, maximize the number of assigned people whose assigned city equals their preferred city (from Table 4-4). This also counts only among the 8500 assigned.

**Reporting Quantity (not an objective):**
- Minimum number of recruited personnel who cannot be assigned to their preferred city = 9000 − (number of the 8500 assigned who get their preferred city). The 500 unassigned are automatically counted as not getting their preferred city.

**Key clarifications confirmed:**
- Suitable specialty restricts only the specialty, not the city.
- Preferred specialty is met if assigned to that specialty regardless of city.
- Preferred city is met if assigned to that city regardless of specialty.
- The 8000 targets are reference values only; the model simply maximizes the counts.
- 500 people will be unassigned (9000 supply − 8500 demand) and are excluded from the goals but included in the reporting quantity.