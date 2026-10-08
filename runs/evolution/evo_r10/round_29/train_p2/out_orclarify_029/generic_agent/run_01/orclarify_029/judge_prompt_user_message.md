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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city," should the model minimize the total shortfall from both 8000 targets combined (i.e., minimize (8000 − specialty-met) + (8000 − city-met)), or should it minimize only the shortfall from the preferred-city target while treating the 8000 preferred-specialty target as a hard constraint that must be met exactly?

## Turn 1 - User Simulator

No, it should not minimize the combined shortfall, and it should not treat the 8000 preferred-specialty target as a hard constraint.

The two goals are separate objectives with different priorities. The 8000 preferred-specialty target is the second priority (p2), and the 8000 preferred-city target is the third priority (p3). The model should first minimize the shortfall from the 8000 preferred-specialty target. Only after that shortfall is minimized should it minimize the shortfall from the 8000 preferred-city target.

## Turn 2 - Generic Agent

QUESTION: You mentioned priorities p2 and p3 for the two goals — is there a first-priority (p1) objective that should be optimized before the preferred-specialty shortfall, such as minimizing the number of branch specialty demands that cannot be fully met, or is the preferred-specialty shortfall actually the top-priority objective?

## Turn 2 - User Simulator

There is a first-priority (p1) objective. The model must first fully meet the branch specialty demands exactly as shown in Table 4-3. No more, no less. Only after ensuring all demands are fully met should the model minimize the shortfall from the 8000 preferred-specialty target.

## Turn 3 - Generic Agent

QUESTION: The total demand in Table 4-3 is 8500, but the total number of recruited personnel is 9000, so 500 people will be left unassigned — is that the intended treatment, i.e., the model assigns exactly the demanded number to each branch specialty and the remaining 500 recruited personnel are simply not placed anywhere?

## Turn 3 - User Simulator

Yes, that is the intended treatment. The model assigns exactly the demanded number to each branch specialty as shown in Table 4-3, and the remaining 500 recruited personnel are simply not placed anywhere.

## Turn 4 - Generic Agent

QUESTION: For the preferred-city goal, should a person who is not assigned to any branch (one of the 500 unplaced) be counted as NOT meeting their preferred city, i.e., do the 8000 city-met people have to come from the 8500 actually assigned, or can unassigned people be treated as meeting their preferred city?

## Turn 4 - User Simulator

The 8000 city-met people have to come from the 8500 actually assigned. Unassigned people are not counted as meeting their preferred city.

## Turn 5 - Generic Agent

QUESTION: For the preferred-specialty goal, should a person who is assigned to a branch but to a specialty that is not their preferred one be counted as NOT meeting their preferred specialty, and should the 8000 specialty-met people also have to come from the 8500 actually assigned (with the 500 unassigned not counted)?

## Turn 5 - User Simulator

Yes. A person assigned to a specialty that is not their preferred one is counted as NOT meeting their preferred specialty. The 8000 specialty-met people must come from the 8500 actually assigned, and the 500 unassigned are not counted.

## Turn 6 - Generic Agent

QUESTION: The original request also asks to "determine the minimum number of recruited personnel who cannot be assigned to their preferred city" — should this number be reported as the final value of the p3 objective (i.e., 9000 minus the number of assigned people who got their preferred city, which would include the 500 unassigned), or as 8500 minus the number of assigned people who got their preferred city (counting only the assigned)?

## Turn 6 - User Simulator

The number should be reported as 9000 minus the number of assigned people who got their preferred city. This includes the 500 unassigned people in the count of those who cannot be assigned to their preferred city.

## Turn 7 - Generic Agent

QUESTION: For the p2 objective (minimizing the shortfall from 8000 preferred-specialty), should the shortfall be computed as max(0, 8000 − specialty-met), so that if more than 8000 assigned people happen to get their preferred specialty, the shortfall is zero and no penalty is applied for exceeding 8000?

## Turn 7 - User Simulator

Yes, the shortfall should be computed as max(0, 8000 − specialty-met). If more than 8000 assigned people get their preferred specialty, the shortfall is zero and no penalty is applied for exceeding 8000.

## Turn 8 - Generic Agent

QUESTION: For the p3 objective (minimizing the shortfall from 8000 preferred-city), should the shortfall likewise be computed as max(0, 8000 − city-met), so that if more than 8000 assigned people get their preferred city, the shortfall is zero and no penalty is applied for exceeding 8000?

## Turn 8 - User Simulator

Yes, the shortfall should be computed as max(0, 8000 − city-met). If more than 8000 assigned people get their preferred city, the shortfall is zero and no penalty is applied for exceeding 8000.

## Turn 9 - Generic Agent

QUESTION: Regarding the type supply constraint — the total number of people assigned from each type (across both cities and all specialties) cannot exceed the available number of that type (1500 each) — should this be a hard constraint (≤ 1500, never violated), or can some of a type's people be left unassigned as long as the assigned count does not exceed 1500?

## Turn 9 - User Simulator

It is a hard constraint: the total number of people assigned from each type cannot exceed 1500. Some of a type's people can be left unassigned as long as the assigned count does not exceed 1500.

## Turn 10 - Generic Agent

QUESTION: For the p1 objective of fully meeting branch specialty demands exactly — since total demand (8500) is less than total supply (9000), "exactly" is achievable as an equality constraint. Should I implement the demand satisfaction as a hard equality constraint (each branch specialty gets exactly its Table 4-3 demand), rather than as a lexicographic objective to be minimized?

## Turn 10 - User Simulator

Yes, implement the demand satisfaction as a hard equality constraint. Each branch specialty must get exactly its Table 4-3 demand.

## Turn 11 - Generic Agent

QUESTION: For the lexicographic optimization, should the model be solved as a single lexicographic multi-objective program (p1 demand equality as hard constraint, then minimize specialty shortfall, then minimize city shortfall in that priority order), or should it be solved in stages — first solve to minimize the specialty shortfall, fix that shortfall value as a constraint, then re-solve to minimize the city shortfall?

## Turn 11 - User Simulator

Either approach is acceptable. The model can be solved as a single lexicographic multi-objective program or in stages. The key requirement is that the priorities are respected in strict order: first ensure all demand is fully met, then minimize the specialty shortfall, and finally minimize the city shortfall.

## Turn 12 - Generic Agent

QUESTION: For the specialty-met count, a person "meets their preferred specialty" only if they are assigned to a branch whose specialty equals their preferred specialty — for example, a Type 1 person (preferred specialty 1) assigned to Donghai City specialty 1 counts as meeting, but the same person assigned to Nanjiang City specialty 1 also counts as meeting (since the specialty matches, regardless of city). Is that correct, i.e., the specialty-met condition depends only on the specialty matching, not on the city?

## Turn 12 - User Simulator

Yes, that is correct. The specialty-met condition depends only on the specialty matching, not on the city.

## Turn 13 - Generic Agent

QUESTION: For the city-met count, a person "meets their preferred city" only if they are assigned to a branch in their preferred city — for example, a Type 1 person (preferred city Donghai) assigned to any specialty in Donghai City counts as meeting, regardless of whether the specialty matches their preference. Is that correct, i.e., the city-met condition depends only on the city matching, not on the specialty?

## Turn 13 - User Simulator

Yes, that is correct. The city-met condition depends only on the city matching, not on the specialty.

## Turn 14 - Generic Agent

QUESTION: Regarding the suitable-specialty constraint — a person can only be assigned to a specialty listed in their suitable specialty set (e.g., Type 6 can only be assigned to specialty 3) — should this be a hard constraint that is never violated, meaning a Type 6 person can only be placed in a specialty-3 branch (in either city) or left unassigned?

## Turn 14 - User Simulator

Yes, this is a hard constraint that is never violated. A Type 6 person can only be placed in a specialty-3 branch (in either city) or left unassigned.

## Turn 15 - Generic Agent

QUESTION: Is there any additional constraint or business rule I have not yet covered — for example, a limit on how many people from a single type can be assigned to a particular branch specialty, or a requirement that each branch specialty's demand be met by a mix of types — or are the constraints I have confirmed (demand equality, type supply cap, suitable-specialty eligibility, and the lexicographic objectives) the complete set?

## Turn 15 - User Simulator

The constraints I have confirmed (demand equality, type supply cap, suitable-specialty eligibility, and the lexicographic objectives) are the complete set. There are no additional constraints or business rules.

## Turn 16 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:** x[t, c, s] = number of type-t people assigned to city c, specialty s, for t = 1..6, c ∈ {Donghai, Nanjiang}, s ∈ {1, 2, 3}.

**Hard constraints:**
1. **Demand equality:** For each (city, specialty) pair, the sum of x[t, c, s] over all types t equals exactly the Table 4-3 demand (Donghai: 1000/2000/1500; Nanjiang: 2000/1000/1000). Total assigned = 8500.
2. **Type supply cap:** For each type t, the sum of x[t, c, s] over all cities and specialties ≤ 1500.
3. **Suitable-specialty eligibility:** x[t, c, s] = 0 if specialty s is not in type t's suitable specialty set (Type 1: {1,2}; Type 2: {2,3}; Type 3: {1,3}; Type 4: {1,3}; Type 5: {2,3}; Type 6: {3}).
4. **Non-negativity:** x[t, c, s] ≥ 0.

**Lexicographic objectives (strict priority order):**
- **p1:** Satisfied by the hard demand-equality constraint (all 8500 demand met exactly).
- **p2:** Minimize specialty shortfall = max(0, 8000 − specialty_met), where specialty_met = sum of x[t, c, s] over all (t, c, s) where s equals type t's preferred specialty.
- **p3:** Minimize city shortfall = max(0, 8000 − city_met), where city_met = sum of x[t, c, s] over all (t, c, s) where c equals type t's preferred city.

**Reporting:** The final answer for "minimum number of recruited personnel who cannot be assigned to their preferred city" is 9000 − city_met (includes the 500 unassigned).

**Unassigned treatment:** The 500 unassigned people are not counted toward either specialty-met or city-met.