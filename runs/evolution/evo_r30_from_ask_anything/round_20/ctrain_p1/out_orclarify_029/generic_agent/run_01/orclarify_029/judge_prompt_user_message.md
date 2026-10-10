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

QUESTION: Should the total number of recruited personnel be fixed at exactly 9000 (the sum of the six types in Table 4-4), or is the total number of people to be assigned a decision variable that can be less than 9000?

## Turn 1 - User Simulator

The total number of people to be assigned is a decision variable that can be less than 9000. The constraint is that the number assigned from each type cannot exceed the available number for that type, not that all available people must be assigned.

## Turn 2 - Generic Agent

QUESTION: Are the demand figures in Table 4-3 (e.g., 1000 for Specialty 1 in Donghai) hard upper limits that the number of people assigned to each branch-specialty combination cannot exceed, or are they targets that should be met exactly?

## Turn 2 - User Simulator

They are targets that should be met exactly. The number of professionals assigned to each specialty at each branch must exactly equal the demand given in Table 4-3. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Is the objective to minimize the number of recruited personnel who cannot be assigned to their preferred city, or is it to maximize the number who can be assigned to their preferred city?

## Turn 3 - User Simulator

The objective is to minimize the number of recruited personnel who cannot be assigned to their preferred city.

## Turn 4 - Generic Agent

QUESTION: Are the two goals of having 8000 personnel meet their preferred specialty and 8000 meet their preferred city hard constraints that must be satisfied, or are they soft targets that the model should try to achieve but may not fully meet?

## Turn 4 - User Simulator

They are soft targets that the model should try to achieve but may not fully meet.

## Turn 5 - Generic Agent

QUESTION: Since the 8000-person targets for preferred specialty and preferred city are soft, how should the model handle them: should it minimize the shortfall from 8000 for each target, or should it simply report the achieved numbers as secondary outputs while the primary objective remains minimizing the number of people not in their preferred city?

## Turn 5 - User Simulator

The model should minimize the shortfall from 8000 for each target. The priorities are in strict order: first, fully meet all demand (p1); second, try to get 8000 people into their preferred specialty (p2); and third, after that, aim for 8000 people in their preferred city (p3).

## Turn 6 - Generic Agent

QUESTION: Are the 8000-person targets for preferred specialty and preferred city applied to the total number of people actually assigned (which can be less than 9000), or are they applied to the full pool of 9000 available people regardless of how many are assigned?

## Turn 6 - User Simulator

The 8000-person targets are applied to the total number of people actually assigned.

## Turn 7 - Generic Agent

QUESTION: When a person is assigned to a specialty that is in their suitable set but is not their preferred specialty, does that count as a shortfall against the 8000 preferred-specialty target?

## Turn 7 - User Simulator

Yes, that counts as a shortfall against the 8000 preferred-specialty target.

## Turn 8 - Generic Agent

QUESTION: When a person is assigned to a city that is not their preferred city, does that count as a shortfall against the 8000 preferred-city target?

## Turn 8 - User Simulator

Yes, that counts as a shortfall against the 8000 preferred-city target.

## Turn 9 - Generic Agent

QUESTION: Are the decision variables for the number of people assigned from each type to each branch-specialty combination required to be integers, or can they be continuous values?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the decision variables for the number of people assigned from each type to each branch-specialty combination required to be non-negative, meaning no negative assignments are allowed?

## Turn 10 - User Simulator

Yes, the decision variables must be non-negative. No negative assignments are allowed.

## Turn 11 - Generic Agent

QUESTION: Are there any additional constraints or rules beyond those already discussed, such as minimum assignment requirements per type, exclusivity rules between branches, or other conditions that must be satisfied?

## Turn 11 - User Simulator

No, there are no additional constraints or rules beyond those already discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Decision Variables:** Let x_{t,c,s} = number of people of type t assigned to city c, specialty s. These are non-negative (confirmed). Integrality is an open assumption (see below).

2. **Types and Availability:** Six types, each with 1500 available people (Table 4-4). The number assigned from each type cannot exceed 1500 (confirmed). The total assigned is a decision variable and can be less than 9000 (confirmed).

3. **Suitable Specialty Constraint:** A person of type t can only be assigned to a specialty listed in their suitable specialty set from Table 4-4 (confirmed).

4. **Demand Constraints (Hard, Priority 1):** The number of people assigned to each branch-specialty combination must exactly equal the demand in Table 4-3 (confirmed). This means:
   - Donghai, Specialty 1: exactly 1000
   - Donghai, Specialty 2: exactly 2000
   - Donghai, Specialty 3: exactly 1500
   - Nanjiang, Specialty 1: exactly 2000
   - Nanjiang, Specialty 2: exactly 1000
   - Nanjiang, Specialty 3: exactly 1000
   Total demand = 8500, so exactly 8500 people will be assigned.

5. **Preferred Specialty Target (Soft, Priority 2):** Minimize the shortfall from 8000 people being assigned to their preferred specialty. A person counts toward the 8000 only if assigned to their preferred specialty (confirmed). Applied to the 8500 actually assigned (confirmed).

6. **Preferred City Target (Soft, Priority 3):** Minimize the shortfall from 8000 people being assigned to their preferred city. A person counts toward the 8000 only if assigned to their preferred city (confirmed). Applied to the 8500 actually assigned (confirmed).

7. **Objective Structure:** Lexicographic (preemptive) multi-objective optimization with strict priority order:
   - P1: Meet all demand exactly (hard constraint)
   - P2: Minimize shortfall from 8000 for preferred specialty
   - P3: Minimize shortfall from 8000 for preferred city

8. **No Additional Constraints:** No minimum assignment per type, no exclusivity rules, no other conditions (confirmed).

**Open Assumptions:**
- **Integrality:** The decision variables are assumed to be integers (whole people), as the context involves assigning individual professionals. This was not explicitly confirmed by the client.