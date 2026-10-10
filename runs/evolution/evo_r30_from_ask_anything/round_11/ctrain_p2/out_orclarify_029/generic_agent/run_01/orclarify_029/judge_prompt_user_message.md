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

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the six types in Table 4-4), or is it a different fixed number that I should use as the total pool to be assigned?

## Turn 1 - User Simulator

The total number of recruited personnel is exactly 9000, which is the sum of the six types in Table 4-4 (6 types × 1500 people each).

## Turn 2 - Generic Agent

QUESTION: For the demand figures in Table 4-3 (e.g., 1000 for Donghai City Specialty 1), are these hard ceilings that the number of people assigned to that branch-specialty combination cannot exceed, or are they exact targets that must be met precisely?

## Turn 2 - User Simulator

They are exact targets that must be met precisely. The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: For the "Number of People" figures in Table 4-4 (1500 for each type), are these hard ceilings that the number of people assigned from each type cannot exceed, or are they exact totals that must all be assigned?

## Turn 3 - User Simulator

They are hard ceilings. The total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4.

## Turn 4 - Generic Agent

QUESTION: Since the demand in Table 4-3 sums to exactly 9000 and the available personnel also sum to 9000, does every one of the 9000 recruited personnel have to be assigned to a branch-specialty position, or is it permissible to leave some personnel unassigned?

## Turn 4 - User Simulator

Every one of the 9000 recruited personnel has to be assigned to a branch-specialty position. Since the demand in Table 4-3 sums to exactly 9000 and must be met precisely, and the available personnel also sum to 9000, all personnel must be assigned.

## Turn 5 - Generic Agent

QUESTION: For the "suitable specialty" restriction in Table 4-4, is it a hard constraint that a person of a given type can only be assigned to a specialty listed in their suitable specialty set, or is it a soft preference that can be violated if needed?

## Turn 5 - User Simulator

It is a hard constraint. A person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4.

## Turn 6 - Generic Agent

QUESTION: For the preferred-specialty goal of 8000, is the target that at least 8000 of the 9000 assigned personnel are placed in their preferred specialty, or is it that exactly 8000 are placed in their preferred specialty?

## Turn 6 - User Simulator

The target is that at least 8000 of the 9000 assigned personnel are placed in their preferred specialty.

## Turn 7 - Generic Agent

QUESTION: For the preferred-city goal of 8000, is the target that at least 8000 of the 9000 assigned personnel are placed in their preferred city, or is it that exactly 8000 are placed in their preferred city?

## Turn 7 - User Simulator

The target is that at least 8000 of the 9000 assigned personnel are placed in their preferred city.

## Turn 8 - Generic Agent

QUESTION: Is the "minimum number of recruited personnel who cannot be assigned to their preferred city" the primary objective to be minimized, with the two 8000 targets treated as hard constraints that must be satisfied, or are the 8000 targets soft goals to be maximized while the minimum non-preferred-city count is the objective?

## Turn 8 - User Simulator

The 8000 targets are soft goals to be maximized, and the minimum non-preferred-city count is the objective to be minimized. The priorities are in strict order: first, fully meet all demand (p1); second, try to get 8000 people into their preferred specialty (p2); and third, after that, aim for 8000 people in their preferred city (p3).

## Turn 9 - Generic Agent

QUESTION: In the third priority level, is the goal to maximize the number of people in their preferred city (equivalently, minimize the number not in their preferred city) as a single objective, or is there a separate explicit target of 8000 that must be reached before any further optimization?

## Turn 9 - User Simulator

The goal is to maximize the number of people in their preferred city (equivalently, minimize the number not in their preferred city) as a single objective. The 8000 figure is the target for that goal, but it is not a hard threshold that must be reached before any further optimization; it is the aspiration level for the soft goal at priority p3.

## Turn 10 - Generic Agent

QUESTION: For the second priority level, is the goal to maximize the number of people in their preferred specialty as a single objective, or is there a separate explicit target of 8000 that must be reached before any further optimization?

## Turn 10 - User Simulator

The goal is to maximize the number of people in their preferred specialty as a single objective. The 8000 figure is the target for that goal, but it is not a hard threshold that must be reached before any further optimization; it is the aspiration level for the soft goal at priority p2.

## Turn 11 - Generic Agent

QUESTION: Are there any additional requirements or constraints beyond those already discussed, such as minimum staffing levels per branch, balance requirements across cities, or any other rules that should be included in the model?

## Turn 11 - User Simulator

No, there are no additional requirements or constraints beyond those already discussed. The model should include:

1. Exact demand fulfillment per branch-specialty (Table 4-3).
2. Suitable specialty restriction per type (Table 4-4).
3. Type availability ceiling (Table 4-4).
4. Priority p2: maximize preferred-specialty matches (target 8000).
5. Priority p3: maximize preferred-city matches (target 8000).

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Total personnel:** Exactly 9000 (6 types × 1500 each). All 9000 must be assigned. *(Confirmed)*

2. **Demand (Table 4-3):** The number assigned to each branch-specialty combination must exactly equal the stated demand. Total demand = 9000. *(Confirmed)*

3. **Suitable specialty restriction:** A person of a given type can only be assigned to a specialty listed in their suitable specialty set. This is a hard constraint. *(Confirmed)*

4. **Type availability ceiling:** The number assigned from each type cannot exceed 1500. *(Confirmed)*

5. **Priority structure (preemptive multi-objective):**
   - **P1 (highest):** Fully meet all demand exactly (this is effectively a hard constraint given the totals match). *(Confirmed)*
   - **P2:** Maximize the number of personnel placed in their preferred specialty (aspiration: 8000). *(Confirmed)*
   - **P3:** Maximize the number of personnel placed in their preferred city (aspiration: 8000). *(Confirmed)*

6. **No additional constraints** beyond those listed above. *(Confirmed)*

**Decision Variables:**
- Let $x_{t,c,s}$ = number of people of type $t$ assigned to city $c$ (Donghai or Nanjiang) in specialty $s$ (1, 2, or 3).

**Constraints:**
- For each city $c$ and specialty $s$: $\sum_t x_{t,c,s} = \text{Demand}(c,s)$ (exact demand fulfillment).
- For each type $t$: $\sum_{c,s} x_{t,c,s} \leq 1500$ (availability ceiling).
- $x_{t,c,s} = 0$ if specialty $s$ is not in the suitable specialty set of type $t$.
- $x_{t,c,s} \geq 0$ for all $t, c, s$.

**Objective (preemptive):**
- **P1:** Satisfied by the equality constraints (demand sums to 9000 = total personnel, so all are assigned).
- **P2:** Maximize $\sum_{t,c,s} x_{t,c,s} \cdot \mathbb{1}[s = \text{PreferredSpecialty}(t)]$.
- **P3:** Maximize $\sum_{t,c,s} x_{t,c,s} \cdot \mathbb{1}[c = \text{PreferredCity}(t)]$.

**Open Assumptions:** None. All formulation-critical facts are confirmed.