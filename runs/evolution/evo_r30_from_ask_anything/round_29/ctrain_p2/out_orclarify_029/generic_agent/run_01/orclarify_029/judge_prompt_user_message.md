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

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the six types in Table 4-4), or is it a different fixed number?

## Turn 1 - User Simulator

The total number of recruited personnel is exactly 9000, which is the sum of the six types in Table 4-4 (6 types × 1500 people each).

## Turn 2 - Generic Agent

QUESTION: Are the demand figures in Table 4-3 hard constraints that must be met exactly, or are they targets that can be exceeded or underfilled?

## Turn 2 - User Simulator

The demand figures in Table 4-3 are hard constraints that must be met exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: For the "preferred specialty" goal, does a person count as meeting this goal only if they are assigned to their single listed preferred specialty, or does it also count if they are assigned to any specialty in their suitable specialty set?

## Turn 3 - User Simulator

A person counts as meeting the preferred specialty goal only if they are assigned to their single listed preferred specialty.

## Turn 4 - Generic Agent

QUESTION: For the "preferred city" goal, does a person count as meeting this goal only if they are assigned to their single listed preferred city, or is there any other condition?

## Turn 4 - User Simulator

A person counts as meeting the preferred city goal only if they are assigned to their single listed preferred city.

## Turn 5 - Generic Agent

QUESTION: Is the objective to minimize the number of people not assigned to their preferred city, or is it a multi-objective problem that also tries to maximize the number of people assigned to their preferred specialty?

## Turn 5 - User Simulator

It is a multi-objective problem with strict priority order:

1. **p1 (highest):** Fully meet the demand in Table 4-3 exactly.
2. **p2:** Achieve 8000 recruited personnel meeting their preferred specialty.
3. **p3 (lowest):** Achieve 8000 recruited personnel meeting their preferred city, which is equivalent to minimizing the number of people not assigned to their preferred city.

So yes, it does try to maximize the number of people assigned to their preferred specialty, but only after the demand is fully met, and the preferred-city goal comes after that.

## Turn 6 - Generic Agent

QUESTION: Are the decision variables for assigning people to branches and specialties required to be integers, or can they be fractional?

## Turn 6 - User Simulator

The decision variables must be integers, since we are assigning whole people to branches and specialties.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or rules for the assignment plan besides the demand requirements, the suitable specialty restrictions, and the type availability limits?

## Turn 7 - User Simulator

No, there are no other constraints or rules beyond:

1. The demand in Table 4-3 must be met exactly.
2. A person can only be assigned to a specialty listed in their suitable specialty set.
3. The total number of people assigned from each type cannot exceed the available number of that type.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Total Personnel:** Exactly 9,000 recruited professionals (6 types × 1,500 each). *(Confirmed)*
2. **Decision Variables:** Integer variables representing the number of people of each type assigned to each (City, Specialty) combination. *(Confirmed)*
3. **Hard Constraints (Priority p1):**
   - The demand for each (City, Specialty) pair in Table 4-3 must be met exactly. *(Confirmed)*
   - A person of a given type can only be assigned to a specialty listed in that type's "Suitable Specialty" set in Table 4-4. *(Confirmed)*
   - The total number of people assigned from each type cannot exceed 1,500 (the available number for that type). *(Confirmed)*
4. **Multi-Objective Structure (Lexicographic Priority):**
   - **Priority p1:** Satisfy all hard constraints above. *(Confirmed)*
   - **Priority p2:** Maximize the number of people assigned to their single listed "Preferred Specialty" from Table 4-4, with a target of 8,000. *(Confirmed)*
   - **Priority p3:** Maximize the number of people assigned to their single listed "Preferred City" from Table 4-4, with a target of 8,000 (equivalently, minimize the number of people not assigned to their preferred city). *(Confirmed)*
5. **Goal Definitions:**
   - A person meets the "Preferred Specialty" goal only if assigned to their specific single preferred specialty. *(Confirmed)*
   - A person meets the "Preferred City" goal only if assigned to their specific single preferred city. *(Confirmed)*
6. **No Other Constraints:** There are no additional rules, exclusivity requirements, or secondary constraints beyond those listed. *(Confirmed)*

**Assumptions:**
- None. All formulation-critical facts were confirmed by the user.