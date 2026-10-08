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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city," should the model minimize the total shortfall (i.e., minimize the sum of the number of people not meeting their preferred specialty plus the number not meeting their preferred city), or should it minimize the shortfall for preferred city only (as the third objective states), or should it minimize the shortfall for preferred specialty only?

## Turn 1 - User Simulator

The model should minimize the shortfall for preferred city only.

The two goals of "8000 meet preferred specialty" and "8000 meet preferred city" are separate objectives with different priorities. The third objective specifically asks to determine the minimum number of recruited personnel who cannot be assigned to their preferred city. Therefore, the model minimizes the shortfall for preferred city only, not the sum of both shortfalls, and not the shortfall for preferred specialty only.

## Turn 2 - Generic Agent

QUESTION: The branch demands in Table 4-3 sum to 8500, but the total number of recruited personnel is 9000 (6 types × 1500). Should the model treat the branch demands as exact requirements that must be met exactly (leaving 500 people unassigned), or as upper bounds that may be underfilled, or should all 9000 people be assigned even if that means exceeding some branch demands?

## Turn 2 - User Simulator

The branch demands should be treated as exact requirements that must be met exactly, leaving 500 people unassigned.

## Turn 3 - Generic Agent

QUESTION: For the 500 people who cannot be assigned to any branch, should the model be free to choose which people are left unassigned (i.e., the unassigned set is a decision), or is there a rule about which types or people must be left out?

## Turn 3 - User Simulator

The model is free to choose which people are left unassigned. There is no rule specifying which types or people must be left out.

## Turn 4 - Generic Agent

QUESTION: When counting whether a person "meets their preferred city," should only people who are actually assigned to a branch count (i.e., the 500 unassigned people are excluded from the preferred-city shortfall calculation), or should unassigned people also count as not meeting their preferred city?

## Turn 4 - User Simulator

Only people who are actually assigned to a branch count. The 500 unassigned people are excluded from the preferred-city shortfall calculation.

## Turn 5 - Generic Agent

QUESTION: The problem mentions a goal of 8000 people meeting their preferred specialty, but the objective is only to minimize the preferred-city shortfall. Should the model also track or report the number of people meeting their preferred specialty as a secondary output, or is the preferred-specialty goal purely informational and not part of the model at all?

## Turn 5 - User Simulator

The preferred-specialty goal is part of the model. It is the second priority (p2), after meeting all branch demands exactly (p1) and before minimizing the preferred-city shortfall (p3). The model should first ensure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally minimize the number of people not in their preferred city.

## Turn 6 - Generic Agent

QUESTION: For the preferred-specialty goal (p2), should the model minimize the number of assigned people who do NOT get their preferred specialty (i.e., maximize the number who do, targeting 8000), or should it be a hard constraint that exactly 8000 assigned people must get their preferred specialty?

## Turn 6 - User Simulator

The model should minimize the number of assigned people who do NOT get their preferred specialty, targeting 8000. It is not a hard constraint that exactly 8000 assigned people must get their preferred specialty.

## Turn 7 - Generic Agent

QUESTION: For the preferred-city shortfall (p3), should the 500 unassigned people be counted as NOT meeting their preferred city (i.e., they add to the shortfall), or should they be excluded from the preferred-city shortfall calculation entirely?

## Turn 7 - User Simulator

The 500 unassigned people should be excluded from the preferred-city shortfall calculation entirely.

## Turn 8 - Generic Agent

QUESTION: For the preferred-specialty shortfall (p2), should the 500 unassigned people also be excluded from the preferred-specialty shortfall calculation, meaning only the 8500 assigned people count toward the 8000 target?

## Turn 8 - User Simulator

Yes, the 500 unassigned people should also be excluded from the preferred-specialty shortfall calculation. Only the 8500 assigned people count toward the 8000 target.

## Turn 9 - Generic Agent

QUESTION: For the "type" constraint, should the total number of people assigned (across all branches and specialties) from each type be at most 1500 (the available number), or should it be exactly 1500?

## Turn 9 - User Simulator

The total number of people assigned from each type should be at most 1500.

## Turn 10 - Generic Agent

QUESTION: When a person of a given type is assigned to a branch, they must be assigned to a specialty that is in their suitable specialty set. Should the model also require that the specialty assigned to a person at a branch matches the branch's specialty (i.e., a person assigned to Donghai City specialty 2 must be counted toward the Donghai City specialty 2 demand of 2000)?

## Turn 10 - User Simulator

Yes, a person assigned to a branch must be assigned to a specific specialty at that branch, and that assignment counts toward that branch's specialty demand. For example, a person assigned to Donghai City specialty 2 counts toward the Donghai City specialty 2 demand of 2000.

## Turn 11 - Generic Agent

QUESTION: For the preferred-city shortfall (p3), should the model minimize the number of assigned people whose assigned city is NOT their preferred city, or should it minimize the number of assigned people whose assigned city IS their preferred city (i.e., maximize the number who get their preferred city, targeting 8000)?

## Turn 11 - User Simulator

The model should minimize the number of assigned people whose assigned city is NOT their preferred city.

## Turn 12 - Generic Agent

QUESTION: For the preferred-specialty shortfall (p2), should the model minimize the number of assigned people whose assigned specialty is NOT their preferred specialty, or should it maximize the number of assigned people whose assigned specialty IS their preferred specialty (targeting 8000)?

## Turn 12 - User Simulator

The model should minimize the number of assigned people whose assigned specialty is NOT their preferred specialty.

## Turn 13 - Generic Agent

QUESTION: Are there any additional constraints or business rules I should be aware of, such as minimum staffing requirements per branch-specialty, or any other restrictions on how people can be distributed across branches?

## Turn 13 - User Simulator

No, there are no additional constraints or business rules beyond those already discussed. The only constraints are:

1. Branch demands must be met exactly (p1).
2. A person can only be assigned to a specialty in their suitable specialty set.
3. The total number of people assigned from each type cannot exceed 1500.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision Variables:**
- x[t, c, s] = number of people of type t assigned to city c, specialty s (for all valid combinations where specialty s is in type t's suitable specialty set)
- u[t] = number of people of type t left unassigned

**Parameters:**
- 6 types, each with 1500 available people
- 2 cities (Donghai, Nanjiang) × 3 specialties = 6 branch-specialty cells with exact demands (total 8500)
- Each type has a suitable specialty set, a preferred specialty, and a preferred city

**Constraints:**
1. **Branch demand (exact):** For each city c and specialty s, the sum of x[t, c, s] over all types t equals the demand for (c, s).
2. **Suitable specialty:** x[t, c, s] = 0 if specialty s is not in type t's suitable specialty set.
3. **Type availability:** For each type t, the sum of x[t, c, s] over all c and s, plus u[t], equals 1500 (i.e., assigned + unassigned = available).
4. **Non-negativity:** All variables ≥ 0.

**Objective (lexicographic, 3 priorities):**
- **p1:** Meet all branch demands exactly (handled as hard constraints).
- **p2:** Minimize the number of assigned people whose assigned specialty is NOT their preferred specialty. (Only the 8500 assigned people count; the 500 unassigned are excluded.)
- **p3:** Minimize the number of assigned people whose assigned city is NOT their preferred city. (Only the 8500 assigned people count; the 500 unassigned are excluded.)

**Output:** The minimum number of recruited personnel who cannot be assigned to their preferred city (the p3 objective value), along with the full assignment plan.