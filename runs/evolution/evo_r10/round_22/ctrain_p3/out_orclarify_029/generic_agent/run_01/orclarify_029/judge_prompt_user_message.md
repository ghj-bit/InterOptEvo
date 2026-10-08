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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city", should the model minimize the total shortfall from both 8000 targets combined (i.e., minimize (8000 − specialty-met) + (8000 − city-met)), or should it treat these as hard constraints that must be satisfied exactly, with the minimum number of people not in their preferred city reported only as a result?

## Turn 1 - User Simulator

These are not hard constraints. They are goals to be achieved in priority order.

First, we fully meet the demand (p1). Then, we try to get 8000 people into their preferred specialty (p2). Finally, after that, we aim for 8000 people in their preferred city (p3).

So, the model should minimize the shortfall for the preferred specialty goal first. Then, subject to that, it should minimize the shortfall for the preferred city goal. The minimum number of people not in their preferred city is the result of this final step.

## Turn 2 - Generic Agent

QUESTION: When you say "fully meet the demand" as the top priority, does that mean the demand numbers in Table 4-3 (e.g., 1000 for Donghai Specialty 1) must be met exactly, or can a branch-specialty cell receive more people than its listed demand as long as the total assigned from each type does not exceed its available number?

## Turn 2 - User Simulator

The demand numbers in Table 4-3 must be met exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: The total demand across all branch-specialty cells is 8500, but the total available personnel is 9000, so 500 people will be left unassigned. Is that correct — i.e., exactly 8500 people get assigned to a branch-specialty cell and the remaining 500 are simply not placed anywhere?

## Turn 3 - User Simulator

Yes, that is correct. Exactly 8500 people get assigned to a branch-specialty cell, and the remaining 500 are simply not placed anywhere.

## Turn 4 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person count as meeting their preferred specialty only if they are assigned to that specialty in their preferred city, or does it count as long as they are assigned to their preferred specialty in either city (e.g., a Type 1 person whose preferred specialty is 1 and preferred city is Donghai would count toward the specialty goal even if assigned to Specialty 1 in Nanjiang)?

## Turn 4 - User Simulator

I need to confirm this internally. The original request does not specify whether the preferred specialty goal requires the person to be in their preferred city as well.

## Turn 5 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting their preferred city only if they are assigned to a branch in that city, regardless of which specialty they are placed in, or must they also be in their preferred specialty to count?

## Turn 5 - User Simulator

I need to confirm this internally. The original request does not specify whether the preferred city goal requires the person to also be in their preferred specialty.

## Turn 6 - Generic Agent

QUESTION: Since the demand cells must be met exactly and each person can only go to a specialty in their suitable set, is it possible that some demand cell cannot be fully staffed because not enough people with that specialty in their suitable set are available? If so, should the model treat the demand as a hard constraint (which would make the problem infeasible) or should it allow a shortfall in demand as a last-resort option?

## Turn 6 - User Simulator

The demand must be met exactly. It is a hard constraint. If the problem turns out to be infeasible, that is a problem with the data, not with the model structure. We do not allow a shortfall in demand.

## Turn 7 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person count as meeting their preferred specialty only if they are assigned to that specialty in their preferred city, or does it count as long as they are assigned to their preferred specialty in either city (e.g., a Type 1 person whose preferred specialty is 1 and preferred city is Donghai would count toward the specialty goal even if assigned to Specialty 1 in Nanjiang)?

## Turn 7 - User Simulator

A person counts as meeting their preferred specialty as long as they are assigned to that specialty in either city. The city does not need to match for the specialty goal.

## Turn 8 - Generic Agent

QUESTION: For the "preferred city" goal, should a person count as meeting their preferred city only if they are assigned to a branch in that city, regardless of which specialty they are placed in, or must they also be in their preferred specialty to count?

## Turn 8 - User Simulator

A person counts as meeting their preferred city as long as they are assigned to a branch in that city, regardless of which specialty they are placed in.

## Turn 9 - Generic Agent

QUESTION: For the 500 unassigned people, should the model decide which types are left unassigned in a way that helps achieve the preferred-specialty and preferred-city goals (i.e., the model chooses who gets left out), or is there a fixed rule about which types are left unassigned?

## Turn 9 - User Simulator

The model should decide which types are left unassigned in a way that helps achieve the preferred-specialty and preferred-city goals. There is no fixed rule about which types are left out.

## Turn 10 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision variables:** For each type t (1–6) and each branch-specialty cell (city c, specialty s), let x[t][c][s] = number of type-t people assigned to specialty s in city c. Also let u[t] = number of type-t people left unassigned.

**Hard constraints:**
1. **Demand met exactly:** For each (city, specialty) cell, the sum of x[t][c][s] over all types t equals the demand in Table 4-3.
2. **Type availability:** For each type t, the sum of x[t][c][s] over all c and s, plus u[t], equals the available number (1500) from Table 4-4.
3. **Suitable specialty:** x[t][c][s] > 0 only if specialty s is in type t's suitable specialty set.
4. **Non-negativity:** All variables ≥ 0.

**Goal achievement definitions:**
- A person meets their **preferred specialty** if they are assigned to their preferred specialty in *either* city (city does not matter for this goal).
- A person meets their **preferred city** if they are assigned to a branch in their preferred city, regardless of which specialty they are placed in.

**Lexicographic (priority-ordered) objective:**
- **P1 (hard, already enforced):** Demand met exactly.
- **P2:** Minimize the shortfall from 8000 people meeting their preferred specialty, i.e., minimize (8000 − total assigned to preferred specialty).
- **P3:** Subject to P2 being optimal, minimize the shortfall from 8000 people meeting their preferred city, i.e., minimize (8000 − total assigned to preferred city).

**Output of interest:** The minimum number of recruited personnel who cannot be assigned to their preferred city (i.e., 8000 minus the P3-optimal value, or equivalently the total number of assigned people not in their preferred city).

**Unassigned people:** The model freely decides which types are left unassigned (500 total) to best serve the P2 and P3 goals.