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

QUESTION: Are the demand figures in Table 4-3 (for example, 1000 for Specialty 1 in Donghai City) hard minimums that must be met exactly, or are they targets that can be exceeded or left short?

## Turn 1 - User Simulator

They are hard requirements. The demand figures in Table 4-3 must be met exactly. No more, no less.

## Turn 2 - Generic Agent

QUESTION: Is the total number of recruited personnel fixed at 9000 (the sum of the six types in Table 4-4), or is it a variable that can be adjusted?

## Turn 2 - User Simulator

The total number of recruited personnel is fixed at 9000, which is the sum of the six types in Table 4-4.

## Turn 3 - Generic Agent

QUESTION: Is the "8000 recruited personnel meet their preferred specialty" goal a hard constraint that must be satisfied, or is it a target to be maximized as part of a multi-objective optimization?

## Turn 3 - User Simulator

It is a target to be maximized as part of a multi-objective optimization. It is not a hard constraint.

## Turn 4 - Generic Agent

QUESTION: Is the "8000 recruited personnel meet their preferred city" goal also a target to be maximized as part of the multi-objective optimization, or is it a hard constraint?

## Turn 4 - User Simulator

It is a target to be maximized as part of the multi-objective optimization. It is not a hard constraint.

## Turn 5 - Generic Agent

QUESTION: Is the "minimum number of recruited personnel who cannot be assigned to their preferred city" a third objective to be minimized in the multi-objective optimization, or is it a derived metric that you want to report after solving the other two objectives?

## Turn 5 - User Simulator

It is a third objective to be minimized in the multi-objective optimization.

## Turn 6 - Generic Agent

QUESTION: How should the three objectives (maximize preferred specialty matches, maximize preferred city matches, minimize non-preferred city assignments) be combined into a single optimization problem, for example by assigning specific weights to each objective or by using a lexicographic priority order?

## Turn 6 - User Simulator

They should be combined using a lexicographic priority order. The priorities are in strict order: p1 (fully meet demand) is the highest priority, p2 (maximize preferred specialty matches) is second, and p3 (maximize preferred city matches / minimize non-preferred city assignments) is the lowest.

## Turn 7 - Generic Agent

QUESTION: In the lexicographic optimization, is the "fully meet demand" priority (p1) satisfied by the hard constraints that force the assignment totals to exactly match the demand figures in Table 4-3, or is it a separate objective level that needs to be explicitly optimized before moving to the specialty and city goals?

## Turn 7 - User Simulator

It is satisfied by the hard constraints that force the assignment totals to exactly match the demand figures in Table 4-3.

## Turn 8 - Generic Agent

QUESTION: Are the "Number of People" values in Table 4-4 (1500 for each type) hard upper limits on how many people of that type can be assigned, or are they exact quotas that must all be assigned?

## Turn 8 - User Simulator

They are hard upper limits. The total number of people assigned from each type cannot exceed the available number listed in Table 4-4.

## Turn 9 - Generic Agent

QUESTION: Since the total demand in Table 4-3 is 8500 and the total available personnel is 9000, are the 500 unassigned personnel allowed to remain unassigned, or must all 9000 personnel be assigned to some branch and specialty?

## Turn 9 - User Simulator

The 500 unassigned personnel are allowed to remain unassigned.

## Turn 10 - Generic Agent

QUESTION: For the lexicographic objective to maximize preferred specialty matches, does a person assigned to their preferred specialty count as a match even if they are assigned to a city that is not their preferred city?

## Turn 10 - User Simulator

Yes, a person assigned to their preferred specialty counts as a match for the preferred specialty objective, regardless of whether they are assigned to their preferred city.

## Turn 11 - Generic Agent

QUESTION: For the lexicographic objective to maximize preferred city matches, does a person assigned to their preferred city count as a match for the preferred city objective, regardless of whether they are assigned to their preferred specialty?

## Turn 11 - User Simulator

Yes, a person assigned to their preferred city counts as a match for the preferred city objective, regardless of whether they are assigned to their preferred specialty.

## Turn 12 - Generic Agent

QUESTION: Is the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective calculated only over the 8500 assigned personnel, or does it include the 500 unassigned personnel as well?

## Turn 12 - User Simulator

It is calculated only over the 8500 assigned personnel.

## Turn 13 - Generic Agent

QUESTION: Are the decision variables for assigning personnel to branches and specialties required to be integers, or can they be fractional values?

## Turn 13 - User Simulator

The decision variables must be integers.

## Turn 14 - Generic Agent

QUESTION: Are the decision variables for assigning personnel to branches and specialties required to be non-negative, meaning no negative assignments are allowed?

## Turn 14 - User Simulator

Yes, the decision variables must be non-negative.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Problem Type:** Multi-objective integer linear programming with lexicographic priorities.
2.  **Decision Variables:**
    *   Let $x_{t, c, s}$ be the number of personnel of type $t$ assigned to city $c$ and specialty $s$.
    *   Domain: Non-negative integers.
    *   Types $t \in \{1, 2, 3, 4, 5, 6\}$.
    *   Cities $c \in \{\text{Donghai}, \text{Nanjiang}\}$.
    *   Specialties $s \in \{1, 2, 3\}$.
3.  **Hard Constraints:**
    *   **Demand Satisfaction:** For each city $c$ and specialty $s$, the sum of assigned personnel must exactly equal the demand $D_{c,s}$ from Table 4-3.
        *   $\sum_{t} x_{t, c, s} = D_{c,s}$ for all $c, s$.
    *   **Availability Limits:** For each type $t$, the total number of assigned personnel cannot exceed the available number $A_t$ from Table 4-4.
        *   $\sum_{c, s} x_{t, c, s} \le A_t$ for all $t$.
    *   **Suitability:** Personnel can only be assigned to specialties listed in their "Suitable Specialty" set in Table 4-4.
        *   $x_{t, c, s} = 0$ if specialty $s$ is not in the suitable set for type $t$.
4.  **Objectives (Lexicographic Order):**
    *   **Priority 1 (Implicitly Satisfied):** The hard constraints ensure demand is met exactly.
    *   **Priority 2 (Maximize):** Maximize the number of assigned personnel who are assigned to their **Preferred Specialty**.
        *   A person of type $t$ assigned to specialty $s$ counts as a match if $s$ equals the "Preferred Specialty" for type $t$ in Table 4-4.
        *   This count is independent of the city assignment.
    *   **Priority 3 (Maximize/Minimize):** Maximize the number of assigned personnel who are assigned to their **Preferred City** (equivalently, minimize the number of assigned personnel *not* in their preferred city).
        *   A person of type $t$ assigned to city $c$ counts as a match if $c$ equals the "Preferred City" for type $t$ in Table 4-4.
        *   This count is independent of the specialty assignment.
        *   The metric is calculated only over the 8500 assigned personnel.
5.  **Data Summary:**
    *   **Total Personnel:** 9000 (1500 per type).
    *   **Total Demand:** 8500 (sum of Table 4-3).
    *   **Unassigned:** 500 personnel are allowed to remain unassigned.
    *   **Targets:** The user mentioned targets of 8000 for both preferred specialty and preferred city matches, but these are treated as soft goals to be maximized/minimized in the lexicographic optimization, not hard constraints.