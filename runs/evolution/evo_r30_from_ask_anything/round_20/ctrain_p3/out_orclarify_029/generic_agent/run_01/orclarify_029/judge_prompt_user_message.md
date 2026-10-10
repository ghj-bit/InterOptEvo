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

QUESTION: For each branch-location and specialty combination in Table 4-3, is the listed demand a hard requirement that must be met exactly, or is it a maximum ceiling that the assigned number can be less than?

## Turn 2 - User Simulator

The demand for each branch-location and specialty combination in Table 4-3 is a hard requirement that must be met exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Is the "Number of People" for each type in Table 4-4 a hard requirement that all 1500 people of that type must be assigned, or is it a maximum ceiling that allows assigning fewer than 1500 of that type?

## Turn 3 - User Simulator

The "Number of People" for each type in Table 4-4 is a maximum ceiling. The total number of people assigned from each type cannot exceed the available number listed, but it is not required to assign all 1500 of that type.

## Turn 4 - Generic Agent

QUESTION: Since the total demand in Table 4-3 is 8500 but the total available personnel is 9000, are the 500 unassigned people simply left unassigned with no penalty, or is there a cost or constraint associated with not assigning someone?

## Turn 4 - User Simulator

The 500 unassigned people are simply left unassigned with no penalty or additional constraint associated with not assigning them.

## Turn 5 - Generic Agent

QUESTION: Are the two goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city treated as hard constraints that must be satisfied exactly, or are they soft targets where the model should minimize the shortfall from 8000 for each?

## Turn 5 - User Simulator

They are soft targets. The model should minimize the shortfall from 8000 for each goal, in the order of priority: first fully meet the demand (p1), then try to get 8000 people into their preferred specialty (p2), and finally aim for 8000 people in their preferred city (p3).

## Turn 6 - Generic Agent

QUESTION: Is the third objective, "determine the minimum number of recruited personnel who cannot be assigned to their preferred city," a separate optimization problem to be solved independently, or is it simply the value of the preferred-city shortfall variable that results from solving the lexicographic model you described?

## Turn 6 - User Simulator

It is simply the value of the preferred-city shortfall variable that results from solving the lexicographic model. It is not a separate optimization problem.

## Turn 7 - Generic Agent

QUESTION: When counting the 8000 target for preferred specialty, does a person who is assigned to their preferred specialty but in a city different from their preferred city count toward the 8000 preferred-specialty target?

## Turn 7 - User Simulator

Yes, a person who is assigned to their preferred specialty but in a city different from their preferred city counts toward the 8000 preferred-specialty target.

## Turn 8 - Generic Agent

QUESTION: When counting the 8000 target for preferred city, does a person who is assigned to their preferred city but in a specialty different from their preferred specialty count toward the 8000 preferred-city target?

## Turn 8 - User Simulator

Yes, a person who is assigned to their preferred city but in a specialty different from their preferred specialty counts toward the 8000 preferred-city target.

## Turn 9 - Generic Agent

QUESTION: Are the decision variables for the number of people of each type assigned to each branch-location and specialty combination required to be integers, or can they be treated as continuous values?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the decision variables for the number of people of each type assigned to each branch-location and specialty combination required to be integers, or can they be treated as continuous values?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any additional constraints or requirements beyond those already discussed, such as minimum staffing levels per branch, exclusivity rules between specialties, or other operational limits that I should include in the model?

## Turn 11 - User Simulator

No, there are no additional constraints or requirements beyond those already discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Total Personnel Pool:** Exactly 9000 people, composed of 6 types with 1500 people each (Confirmed).
2. **Assignment Granularity:** People are assigned to specific (City, Specialty) combinations. A person of a given type can only be assigned to a specialty listed in their "Suitable Specialty" set in Table 4-4 (Confirmed).
3. **Supply Constraint:** The number of people assigned from each type cannot exceed 1500. It is not required to assign all 1500; up to 500 total people may remain unassigned with no penalty (Confirmed).
4. **Demand Constraint:** The demand for each (City, Specialty) combination in Table 4-3 is a hard requirement that must be met exactly. Total demand is 8500, so exactly 8500 people will be assigned, and 500 will be unassigned (Confirmed).
5. **Objective Structure:** This is a lexicographic (preemptive) multi-objective optimization problem with the following priority order:
   - **Priority 1 (P1):** Meet all demand requirements exactly (hard constraint, but listed as top priority for clarity).
   - **Priority 2 (P2):** Minimize the shortfall from 8000 people being assigned to their preferred specialty. A person counts toward this target if they are assigned to their preferred specialty, regardless of city (Confirmed).
   - **Priority 3 (P3):** Minimize the shortfall from 8000 people being assigned to their preferred city. A person counts toward this target if they are assigned to their preferred city, regardless of specialty (Confirmed).
6. **Output Metric:** The "minimum number of recruited personnel who cannot be assigned to their preferred city" is simply the value of the P3 shortfall variable resulting from the lexicographic solution (Confirmed).
7. **No Additional Constraints:** There are no other operational limits, minimum staffing rules, or exclusivity constraints beyond those specified (Confirmed).

**Open Assumptions:**

1. **Integrality:** It is assumed that the decision variables (number of people of each type assigned to each city-specialty combination) are integers. This is a standard assumption for personnel assignment problems, but it was not explicitly confirmed by the client. If continuous values are acceptable, the model remains valid but may yield fractional assignments which would need rounding in practice.