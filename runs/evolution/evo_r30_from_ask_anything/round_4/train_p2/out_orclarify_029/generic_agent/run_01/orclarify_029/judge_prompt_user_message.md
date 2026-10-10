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

QUESTION: For the two goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city, are these targets to be treated as hard constraints that must be exactly satisfied, or as soft goals to be maximized as much as possible within the feasible assignments?

## Turn 1 - User Simulator

They are soft goals to be maximized as much as possible within the feasible assignments.

## Turn 2 - Generic Agent

QUESTION: For the third objective of determining the minimum number of recruited personnel who cannot be assigned to their preferred city, is this a separate optimization problem to be solved after maximizing the two soft goals, or should it be part of a single multi-objective model where all three objectives are considered simultaneously?

## Turn 2 - User Simulator

It should be part of a single multi-objective model where all three objectives are considered simultaneously.

## Turn 3 - Generic Agent

QUESTION: In the single multi-objective model, how should the three objectives be combined: should I use a weighted sum with specific weights you provide, a lexicographic priority order where one objective is optimized before the next, or should I present the Pareto frontier of trade-offs among the three objectives?

## Turn 3 - User Simulator

Use a lexicographic priority order where one objective is optimized before the next.

## Turn 4 - Generic Agent

QUESTION: In the lexicographic priority order, which of the three objectives should be optimized first: maximizing the number of personnel who meet their preferred specialty, maximizing the number who meet their preferred city, or minimizing the number who cannot be assigned to their preferred city?

## Turn 4 - User Simulator

Maximizing the number of personnel who meet their preferred specialty should be optimized first.

## Turn 5 - Generic Agent

QUESTION: After maximizing the number of personnel who meet their preferred specialty, which objective should be optimized second: maximizing the number who meet their preferred city, or minimizing the number who cannot be assigned to their preferred city?

## Turn 5 - User Simulator

Maximizing the number who meet their preferred city should be optimized second.

## Turn 6 - Generic Agent

QUESTION: For the branch demand figures in Table 4-3, should each branch-specialty demand be treated as a hard constraint that must be met exactly, or as a soft target that can be underfilled or overfilled if necessary to satisfy the other objectives?

## Turn 6 - User Simulator

Each branch-specialty demand should be treated as a hard constraint that must be met exactly.

## Turn 7 - Generic Agent

QUESTION: For the "Number of People" column in Table 4-4, should the total number of people assigned from each type be exactly equal to the listed number, or should it be at most that number (allowing some people of a type to remain unassigned)?

## Turn 7 - User Simulator

It should be at most that number, allowing some people of a type to remain unassigned.

## Turn 8 - Generic Agent

QUESTION: When a person is assigned to a specialty that is not their preferred specialty, does that person still count toward the branch demand for that specialty, or are only people assigned to their preferred specialty counted toward demand?

## Turn 8 - User Simulator

That person still counts toward the branch demand for that specialty.

## Turn 9 - Generic Agent

QUESTION: For the "suitable specialty" constraint, if a person is assigned to a specialty that is in their suitable specialty set but is not their preferred specialty, are they considered to have "met their preferred specialty" for the first objective, or does "meeting preferred specialty" strictly mean being assigned to the exact specialty listed in the "Preferred Specialty" column?

## Turn 9 - User Simulator

"Meeting preferred specialty" strictly means being assigned to the exact specialty listed in the "Preferred Specialty" column.

## Turn 10 - Generic Agent

QUESTION: For the "meeting preferred city" objective, does a person count as meeting their preferred city only if they are assigned to a branch in the city listed in the "Preferred City" column, regardless of which specialty they are assigned to within that city?

## Turn 10 - User Simulator

Yes, a person counts as meeting their preferred city only if they are assigned to a branch in the city listed in the "Preferred City" column, regardless of which specialty they are assigned to within that city.

## Turn 11 - Generic Agent

QUESTION: For the third objective of minimizing the number of recruited personnel who cannot be assigned to their preferred city, does this count include only people who are actually assigned to a branch but in a non-preferred city, or does it also include people who remain unassigned (i.e., not assigned to any branch)?

## Turn 11 - User Simulator

It includes only people who are actually assigned to a branch but in a non-preferred city.

## Turn 12 - Generic Agent

QUESTION: For the decision variables representing the number of people of each type assigned to each branch-specialty combination, should these variables be required to be integers, or can they be treated as continuous values?

## Turn 12 - User Simulator

They should be required to be integers.

## Turn 13 - Generic Agent

QUESTION: Are there any upper bounds on the number of people that can be assigned to a specific branch-specialty combination beyond the total demand for that combination, or is the only limit the total demand for that branch-specialty pair?

## Turn 13 - User Simulator

The only limit is the total demand for that branch-specialty pair.

## Turn 14 - Generic Agent

QUESTION: For the "at most" constraint on the number of people assigned from each type, should the sum of people assigned from a type across all branch-specialty combinations be less than or equal to the listed number, or should it be strictly less than the listed number?

## Turn 14 - User Simulator

It should be less than or equal to the listed number.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Decision Variables:** Integer variables representing the number of people of each type (1–6) assigned to each branch-specialty combination (Donghai/Nanjiang × Specialty 1/2/3). Total of 6 types × 6 branch-specialty combinations = 36 variables.

2. **Hard Constraints:**
   - **Branch Demand:** Each branch-specialty demand in Table 4-3 must be met exactly.
     - Donghai Specialty 1: 1000
     - Donghai Specialty 2: 2000
     - Donghai Specialty 3: 1500
     - Nanjiang Specialty 1: 2000
     - Nanjiang Specialty 2: 1000
     - Nanjiang Specialty 3: 1000
   - **Suitable Specialty:** A person of a given type can only be assigned to a specialty in their suitable specialty set (Table 4-4).
   - **Type Availability:** The total number of people assigned from each type across all branch-specialty combinations must be ≤ the listed number in Table 4-4 (1500 for each type).

3. **Objectives (Lexicographic Priority Order):**
   - **Priority 1:** Maximize the number of people assigned to their exact preferred specialty (as listed in Table 4-4).
   - **Priority 2:** Maximize the number of people assigned to a branch in their preferred city (as listed in Table 4-4).
   - **Priority 3:** Minimize the number of people who are assigned to a branch but in a non-preferred city.

4. **Interpretation Clarifications:**
   - "Meeting preferred specialty" strictly means being assigned to the exact specialty in the "Preferred Specialty" column.
   - "Meeting preferred city" means being assigned to any branch in the preferred city, regardless of specialty.
   - The third objective counts only people who are assigned to a branch but in a non-preferred city; unassigned people are not counted.
   - People assigned to a non-preferred specialty still count toward branch demand.

5. **No Additional Bounds:** No upper bounds on individual branch-specialty assignments beyond the total demand for that combination.