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

QUESTION: Is the total number of recruited personnel exactly 9000 (the sum of the six types in Table 4-4), or is 9000 a maximum pool from which a smaller number may be selected for assignment?

## Turn 1 - User Simulator

The total number of recruited personnel is exactly 9000. All 9000 people (the sum of the six types in Table 4-4) must be assigned to the branches.

## Turn 2 - Generic Agent

QUESTION: For the demand figures in Table 4-3 (e.g., 1000 for Specialty 1 in Donghai), are these exact requirements that must be met precisely, or are they maximum capacities that can be filled up to but not exceeded?

## Turn 2 - User Simulator

They are exact requirements. The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Regarding the two goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city, are these hard constraints that must be satisfied exactly, or are they soft targets where falling short is allowed and penalized in the objective function?

## Turn 3 - User Simulator

They are soft targets. Falling short is allowed, and the shortfall is penalized in the objective function.

## Turn 4 - Generic Agent

QUESTION: For the third objective of minimizing the number of recruited personnel who cannot be assigned to their preferred city, is this a separate minimization goal that is optimized simultaneously with the two soft-target penalties, or is it the primary objective with the two 8000-person targets treated as secondary constraints?

## Turn 4 - User Simulator

The three priorities are in strict order: p1 (meeting demand exactly) is the highest priority, p2 (8000 people in their preferred specialty) is second, and p3 (8000 people in their preferred city) is the lowest. So we first make sure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, we aim for 8000 people in their preferred city.

## Turn 5 - Generic Agent

QUESTION: In the lexicographic objective, is the third priority (p3) to minimize the number of personnel NOT in their preferred city, or to maximize the number of personnel IN their preferred city (i.e., get as close to 8000 as possible)?

## Turn 5 - User Simulator

The third priority (p3) is to minimize the number of personnel NOT in their preferred city.

## Turn 6 - Generic Agent

QUESTION: For the second priority (p2), is the goal to maximize the number of personnel assigned to their preferred specialty (i.e., get as close to 8000 as possible), or is it to minimize the number of personnel NOT in their preferred specialty?

## Turn 6 - User Simulator

The goal for the second priority (p2) is to maximize the number of personnel assigned to their preferred specialty, i.e., get as close to 8000 as possible.

## Turn 7 - Generic Agent

QUESTION: For the first priority (p1), since the demand figures in Table 4-3 are exact requirements, is p1 simply the feasibility condition that all branch-specialty demands are met exactly, or is there an additional penalty term in the objective for any deviation from those exact demand values?

## Turn 7 - User Simulator

p1 is simply the feasibility condition that all branch-specialty demands are met exactly. There is no additional penalty term in the objective for any deviation from those exact demand values.

## Turn 8 - Generic Agent

QUESTION: Are the decision variables (the number of people of each type assigned to each branch-specialty combination) required to be integers, or can they be treated as continuous values?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: For the decision variables representing the number of people of each type assigned to each branch-specialty combination, should they be constrained to be non-negative integers, or is it acceptable for them to be non-negative continuous values?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are there any additional constraints or rules beyond those already stated, such as minimum assignment requirements per type, exclusivity rules between branches, or other conditions that must be satisfied?

## Turn 10 - User Simulator

No, there are no additional constraints or rules beyond those already stated.

## Turn 11 - Generic Agent

QUESTION: For the "suitable specialty" restriction in Table 4-4, does this mean that a person of a given type can ONLY be assigned to specialties listed in their suitable specialty set, making any assignment to a non-listed specialty infeasible?

## Turn 11 - User Simulator

Yes, a person can only be assigned to a specialty that is listed in their suitable specialty set according to Table 4-4. Any assignment to a non-listed specialty is infeasible.

## Turn 12 - Generic Agent

QUESTION: For the "preferred city" column in Table 4-4, does this mean that a person of a given type can be assigned to either city (Donghai or Nanjiang) as long as the specialty is in their suitable set, and the preferred city is only used to determine whether they are "in their preferred city" for the p3 objective?

## Turn 12 - User Simulator

Yes, a person of a given type can be assigned to either city (Donghai or Nanjiang) as long as the specialty is in their suitable set. The preferred city is only used to determine whether they are "in their preferred city" for the p3 objective.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Total personnel:** Exactly 9000 people (sum of six types in Table 4-4), all must be assigned. *(Confirmed)*

2. **Decision variables:** Let x_{t,c,s} = number of people of type t assigned to city c (Donghai or Nanjiang) in specialty s. *(Confirmed)*

3. **Variable domain:** Non-negative (integrality pending internal confirmation — flagged as assumption: treat as non-negative continuous for now, but integer constraints can be added if confirmed). *(Assumed: non-negative continuous; integrality unconfirmed)*

4. **Feasibility constraints (p1 – hard):**
   - For each city c and specialty s: sum over all types t of x_{t,c,s} = Demand(c,s) from Table 4-3. *(Confirmed)*
   - For each type t: sum over all cities c and specialties s of x_{t,c,s} = Number of People of type t from Table 4-4. *(Confirmed)*
   - x_{t,c,s} = 0 if specialty s is not in the suitable specialty set of type t. *(Confirmed)*

5. **Lexicographic objective (strict priority order):**
   - **p1 (highest):** Feasibility — all demand and supply constraints satisfied exactly. No penalty term; purely a feasibility condition. *(Confirmed)*
   - **p2 (second):** Maximize the number of personnel assigned to their preferred specialty (target 8000). This is a soft target; shortfall is allowed. *(Confirmed)*
   - **p3 (lowest):** Minimize the number of personnel NOT assigned to their preferred city (equivalently, maximize those in their preferred city, target 8000). This is a soft target; shortfall is allowed. *(Confirmed)*

6. **Preferred specialty mapping (from Table 4-4):**
   - Type 1 → Specialty 1
   - Type 2 → Specialty 2
   - Type 3 → Specialty 1
   - Type 4 → Specialty 3
   - Type 5 → Specialty 3
   - Type 6 → Specialty 3 *(Confirmed)*

7. **Preferred city mapping (from Table 4-4):**
   - Type 1 → Donghai
   - Type 2 → Donghai
   - Type 3 → Nanjiang
   - Type 4 → Nanjiang
   - Type 5 → Donghai
   - Type 6 → Nanjiang *(Confirmed)*

8. **No additional constraints** beyond those stated. *(Confirmed)*

**Open Assumptions:**
- **Integrality:** Decision variables are assumed non-negative continuous. If integer constraints are required, they can be added without changing the model structure. *(Flagged – pending internal confirmation)*