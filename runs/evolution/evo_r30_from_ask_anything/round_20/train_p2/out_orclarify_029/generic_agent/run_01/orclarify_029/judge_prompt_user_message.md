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

QUESTION: Is the total number of recruited personnel fixed at 9000 (the sum of the six types in Table 4-4), or is it a variable that can differ from that sum?

## Turn 1 - User Simulator

The total number of recruited personnel is fixed at 9000, which is the sum of the six types in Table 4-4.

## Turn 2 - Generic Agent

QUESTION: Are the demand figures in Table 4-3 hard constraints that must be met exactly, or are they targets that can be exceeded or underfilled?

## Turn 2 - User Simulator

The demand figures in Table 4-3 are hard constraints that must be met exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: Is the "8000 recruited personnel meet their preferred specialty" goal a hard constraint that must be satisfied exactly, or is it a soft target to be maximized in the objective function?

## Turn 3 - User Simulator

It is a soft target to be maximized in the objective function.

## Turn 4 - Generic Agent

QUESTION: Is the "8000 recruited personnel meet their preferred city" goal a hard constraint that must be satisfied exactly, or is it a soft target to be maximized in the objective function?

## Turn 4 - User Simulator

It is a soft target to be maximized in the objective function.

## Turn 5 - Generic Agent

QUESTION: Is the "minimum number of recruited personnel who cannot be assigned to their preferred city" a separate objective to be minimized, or is it simply the residual (9000 minus the number who do get their preferred city) that follows from maximizing the preferred-city goal?

## Turn 5 - User Simulator

It is simply the residual (9000 minus the number who do get their preferred city) that follows from maximizing the preferred-city goal.

## Turn 6 - Generic Agent

QUESTION: Are the two soft targets (preferred specialty and preferred city) to be optimized simultaneously in a single objective function, or is one prioritized over the other in a lexicographic or weighted manner?

## Turn 6 - User Simulator

They are prioritized in a lexicographic manner. The preferred specialty target is second priority, and the preferred city target is third priority.

## Turn 7 - Generic Agent

QUESTION: What is the first-priority objective in the lexicographic ordering, since you have identified preferred specialty as second priority and preferred city as third priority?

## Turn 7 - User Simulator

The first-priority objective is to fully meet the demand, meaning exactly the numbers shown in Table 4-3.

## Turn 8 - Generic Agent

QUESTION: Is the assignment of individuals to specific branches and specialties required to be an integer (whole number of people) decision, or can fractional assignments be allowed in the model?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Should the model treat the number of people assigned from each type to each branch-specialty combination as a non-negative continuous variable, or as a non-negative integer variable?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are there any additional constraints or rules beyond those already stated, such as minimum assignment requirements per branch, exclusivity rules between specialties, or other dependencies that should be included in the model?

## Turn 10 - User Simulator

No, there are no additional constraints or rules beyond those already stated.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Total Personnel:** Fixed at 9000 (sum of six types in Table 4-4). [Confirmed]
2. **Demand Constraints:** The demand figures in Table 4-3 are hard constraints that must be met exactly. [Confirmed]
3. **Preferred Specialty Target:** A soft target to be maximized, with a goal of 8000 personnel meeting their preferred specialty. [Confirmed]
4. **Preferred City Target:** A soft target to be maximized, with a goal of 8000 personnel meeting their preferred city. [Confirmed]
5. **Residual Metric:** The number of personnel who cannot be assigned to their preferred city is simply 9000 minus the number who do get their preferred city. [Confirmed]
6. **Lexicographic Prioritization:** 
   - First priority: Fully meet the demand (exactly as in Table 4-3). [Confirmed]
   - Second priority: Maximize the number of personnel meeting their preferred specialty (target 8000). [Confirmed]
   - Third priority: Maximize the number of personnel meeting their preferred city (target 8000). [Confirmed]
7. **Additional Constraints:** None beyond those already stated. [Confirmed]

**Open Assumptions:**

1. **Variable Domain:** The number of people assigned from each type to each branch-specialty combination is assumed to be a non-negative continuous variable, as the integrality requirement was not confirmed. [Assumed]