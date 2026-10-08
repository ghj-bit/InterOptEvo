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

QUESTION: When you say the total number of people assigned from each type cannot exceed the available number of that type, do you mean each type's 1500 people must all be assigned (i.e., exactly 1500 of each type are placed, totaling 9000), or may some of the 1500 of a type be left unassigned (i.e., at most 1500 of each type, with the total assigned possibly below 9000)?

## Turn 1 - User Simulator

It is at most 1500 of each type. Some of the 1500 of a type may be left unassigned, so the total assigned can be below 9000.

## Turn 2 - Generic Agent

QUESTION: For the branch demand numbers in Table 4-3 (e.g., Donghai City specialty 1 = 1000), are these exact requirements that must be met precisely, or are they maximum capacities that may be under-filled?

## Turn 2 - User Simulator

They are exact requirements that must be met precisely.

## Turn 3 - Generic Agent

QUESTION: You mention three objectives (8000 meet preferred specialty, 8000 meet preferred city, and the minimum number who cannot be assigned to their preferred city). Is this a goal-programming problem where you want to simultaneously achieve the 8000 preferred-specialty target and the 8000 preferred-city target (minimizing the shortfall from each), or is the primary objective simply to minimize the number of people not assigned to their preferred city while treating the 8000 preferred-specialty figure as a separate reporting metric?

## Turn 3 - User Simulator

It is a goal-programming problem with strict priorities: first meet all branch demand exactly, then achieve 8000 people in their preferred specialty, and finally achieve 8000 people in their preferred city. The minimum number not assigned to their preferred city is the result of the third priority.

## Turn 4 - Generic Agent

QUESTION: In the goal-programming priorities, when you say "achieve 8000 people in their preferred specialty" as the second priority, do you mean to maximize the number of assigned people who get their preferred specialty (with 8000 being the target to reach), or to minimize the shortfall below 8000 (i.e., penalize only if fewer than 8000 get their preferred specialty, but not penalize if more than 8000 do)?

## Turn 4 - User Simulator

Minimize the shortfall below 8000. If more than 8000 get their preferred specialty, that is not penalized.

## Turn 5 - Generic Agent

QUESTION: Similarly for the third priority (preferred city), do you mean to minimize the shortfall below 8000 people getting their preferred city (i.e., penalize only if fewer than 8000 get their preferred city, but not penalize if more than 8000 do)?

## Turn 5 - User Simulator

Yes, minimize the shortfall below 8000. If more than 8000 get their preferred city, that is not penalized.

## Turn 6 - Generic Agent

QUESTION: Since the branch demands in Table 4-3 sum to exactly 8500 (1000+2000+1500+2000+1000+1000), and you confirmed these must be met exactly, does that mean exactly 8500 people will be assigned in total (one per demand slot), making the "at most 1500 per type" constraint the only upper bound on how many of each type are used?

## Turn 6 - User Simulator

Yes, exactly 8500 people will be assigned in total, and the "at most 1500 per type" constraint is the only upper bound on how many of each type are used.

## Turn 7 - Generic Agent

QUESTION: For the "preferred specialty" goal, a person "meets their preferred specialty" if they are assigned to the specialty listed in their Preferred Specialty column (e.g., Type 1 people meet it if assigned to specialty 1), regardless of which city they are placed in — is that correct?

## Turn 7 - User Simulator

Yes, that is correct. A person meets their preferred specialty if they are assigned to the specialty listed in their Preferred Specialty column, regardless of which city they are placed in.

## Turn 8 - Generic Agent

QUESTION: For the "preferred city" goal, a person "meets their preferred city" if they are assigned to the city listed in their Preferred City column (e.g., Type 1 people meet it if assigned to Donghai), regardless of which specialty they are placed in — is that correct?

## Turn 8 - User Simulator

Yes, that is correct. A person meets their preferred city if they are assigned to the city listed in their Preferred City column, regardless of which specialty they are placed in.

## Turn 9 - Generic Agent

QUESTION: You mentioned the "minimum number of recruited personnel who cannot be assigned to their preferred city" as one of the objectives. Is this simply the complement of the third-priority goal (i.e., 8500 minus the number who get their preferred city), or is it a separate, distinct quantity that could differ from that complement?

## Turn 9 - User Simulator

It is simply the complement of the third-priority goal: 8500 minus the number who get their preferred city.

## Turn 10 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision variables:**
- x[t, c, s] = number of people of type t assigned to city c, specialty s, where t ∈ {1,...,6}, c ∈ {Donghai, Nanjiang}, s ∈ {1,2,3}.
- A person of type t can only be assigned to a specialty in their Suitable Specialty set (from Table 4-4).

**Constraints:**
1. **Branch demand (exact):** For each (city, specialty) pair in Table 4-3, the sum of x[t, c, s] over all types t equals the stated demand exactly (total = 8500).
2. **Type availability (upper bound):** For each type t, the sum of x[t, c, s] over all cities and specialties ≤ 1500.
3. **Non-negativity:** x[t, c, s] ≥ 0 (continuous; no integrality requirement stated).

**Goal-programming objective (strict lexicographic priorities):**
- **Priority 1:** Meet all branch demands exactly (handled as hard constraints above).
- **Priority 2:** Minimize the shortfall below 8000 in the number of assigned people who get their preferred specialty. A person of type t gets their preferred specialty if assigned to the specialty in their Preferred Specialty column (regardless of city). Shortfall = max(0, 8000 − (number getting preferred specialty)).
- **Priority 3:** Minimize the shortfall below 8000 in the number of assigned people who get their preferred city. A person of type t gets their preferred city if assigned to the city in their Preferred City column (regardless of specialty). Shortfall = max(0, 8000 − (number getting preferred city)).

**Reported result:** The minimum number of people not assigned to their preferred city = 8500 − (number getting preferred city), which is the outcome of Priority 3.