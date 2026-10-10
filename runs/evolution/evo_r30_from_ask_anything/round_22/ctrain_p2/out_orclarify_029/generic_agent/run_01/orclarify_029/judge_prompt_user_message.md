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

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the 1500 people in each of the six types in Table 4-4), or is there a different total pool size that I should use for the assignment plan?

## Turn 1 - User Simulator

The total number of recruited personnel is exactly 9000, which is the sum of the 1500 people in each of the six types listed in Table 4-4.

## Turn 2 - Generic Agent

QUESTION: Are the demand figures in Table 4-3 (e.g., 1000 for Specialty 1 in Donghai City) hard constraints that must be met exactly, or are they targets that can be exceeded or underfilled?

## Turn 2 - User Simulator

The demand figures in Table 4-3 are hard constraints that must be met exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: For the two goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city, are these targets to be maximized (i.e., you want as many as possible to meet them, with 8000 being a minimum threshold), or are they exact equality constraints that must be satisfied precisely?

## Turn 3 - User Simulator

These are targets to be maximized. You want as many as possible to meet their preferred specialty and preferred city, with 8000 being the goal for each.

## Turn 4 - Generic Agent

QUESTION: Is the third objective, "determine the minimum number of recruited personnel who cannot be assigned to their preferred city," a separate optimization problem to be solved after the first two goals are met, or is it simply a derived metric calculated from the final assignment plan?

## Turn 4 - User Simulator

It is a separate optimization objective. The priorities are in strict order: first, fully meet all demand (p1); second, maximize the number of personnel meeting their preferred specialty (p2); and third, minimize the number of personnel who cannot be assigned to their preferred city (p3).

## Turn 5 - Generic Agent

QUESTION: Are the 8000-person targets for preferred specialty and preferred city hard lower-bound constraints that must be satisfied in the final solution, or are they soft goals that are maximized subject to the priority hierarchy where demand fulfillment is the absolute top priority?

## Turn 5 - User Simulator

They are soft goals that are maximized subject to the priority hierarchy. Demand fulfillment is the absolute top priority.

## Turn 6 - Generic Agent

QUESTION: When a person is assigned to a specialty, must they be assigned to exactly one specialty and one city, or is it possible for a person to be assigned to multiple specialties or cities?

## Turn 6 - User Simulator

Each person must be assigned to exactly one specialty and one city.

## Turn 7 - Generic Agent

QUESTION: Are the decision variables for the number of people of each type assigned to each city-specialty combination required to be integers, or can they be treated as continuous values?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Should the number of people of each type assigned to each city-specialty combination be treated as integer values, or is it acceptable to treat them as continuous values for the purpose of this planning model?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the "Number of People" values in Table 4-4 (1500 for each type) hard upper limits on how many people of that type can be assigned, or are they exact equality constraints meaning all 1500 people of each type must be assigned?

## Turn 9 - User Simulator

They are hard upper limits. The total number of people assigned from each type cannot exceed the available number of that type as listed in Table 4-4.

## Turn 10 - Generic Agent

QUESTION: Is it possible that not all 9000 recruited personnel will be assigned to a position, or must every single one of the 9000 people be assigned to exactly one city-specialty combination?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is it possible that some of the 9000 recruited personnel will remain unassigned, or must every single one of the 9000 people be assigned to exactly one city-specialty combination?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are the demand figures in Table 4-3 (totaling 8500) hard constraints that must be met exactly, or are they maximum capacities that can be underfilled if not enough suitable personnel are available?

## Turn 12 - User Simulator

The demand figures in Table 4-3 are hard constraints that must be met exactly.

## Turn 13 - Generic Agent

QUESTION: Since the total demand in Table 4-3 is 8500 and the total available personnel is 9000, are the 500 unassigned personnel considered "not meeting their preferred city" for the purpose of the third objective, or are they excluded from that count?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the third objective of minimizing the number of personnel who cannot be assigned to their preferred city, does this count include only those personnel who are assigned to a position but in a city different from their preference, or does it also include the 500 personnel who remain unassigned?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: For the third objective of minimizing the number of personnel who cannot be assigned to their preferred city, does this count include only those personnel who are assigned to a position but in a city different from their preference, or does it also include the 500 personnel who remain unassigned?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the third objective of minimizing the number of personnel who cannot be assigned to their preferred city, does this count include only those personnel who are assigned to a position but in a city different from their preference, or does it also include the 500 personnel who remain unassigned?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Total Personnel:** There are exactly 9,000 recruited personnel, divided into 6 types, with 1,500 people in each type (Confirmed).
2.  **Demand Constraints:** The demand figures in Table 4-3 (totaling 8,500 positions) are hard constraints that must be met exactly (Confirmed).
3.  **Supply Constraints:** The number of people assigned from each type cannot exceed the available number of that type (1,500 per type) (Confirmed).
4.  **Assignment Rule:** Each assigned person must be assigned to exactly one specialty and one city (Confirmed).
5.  **Suitability Constraint:** A person can only be assigned to a specialty listed in their "Suitable Specialty" set in Table 4-4 (Confirmed).
6.  **Objective Hierarchy:** The problem is a lexicographic optimization with the following strict priorities:
    *   **Priority 1:** Fully meet all demand (8,500 positions filled exactly) (Confirmed).
    *   **Priority 2:** Maximize the number of personnel meeting their preferred specialty (Target: 8,000, but treated as a soft goal to be maximized) (Confirmed).
    *   **Priority 3:** Minimize the number of personnel who cannot be assigned to their preferred city (Confirmed).
7.  **Unassigned Personnel:** Since total supply (9,000) exceeds total demand (8,500), 500 personnel will remain unassigned (Derived from Confirmed facts).

**Explicit Assumptions:**

1.  **Integrality:** The number of people assigned to each city-specialty combination is assumed to be an integer, as personnel are discrete units (Assumed due to lack of confirmation).
2.  **Scope of "Not Meeting Preferred City":** The third objective (minimizing personnel not in preferred city) is assumed to apply **only** to the 8,500 personnel who are actually assigned to positions. The 500 unassigned personnel are excluded from this specific penalty count (Assumed due to lack of confirmation).
3.  **Non-negativity:** All assignment variables are non-negative (Standard assumption).