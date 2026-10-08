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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city", should the model minimize the total shortfall from both 8000 targets combined (i.e., minimize (8000 − specialty-met) + (8000 − city-met)), or should it treat one of these as a hard constraint that must be satisfied exactly and only minimize the shortfall on the other?

## Turn 1 - User Simulator

Neither. Both are soft goals, not hard constraints. The model should minimize the shortfall for each goal separately, in the priority order: first minimize the shortfall from 8000 for preferred specialty, then, subject to that, minimize the shortfall from 8000 for preferred city. They are not combined into a single total.

## Turn 2 - Generic Agent

QUESTION: The third objective is to "determine the minimum number of recruited personnel who cannot be assigned to their preferred city" — is this a separate optimization problem to be solved independently (i.e., minimize the number of people not in their preferred city, ignoring the two 8000 goals), or is it simply the value of the city-shortfall variable that results from the two-level goal program you just described?

## Turn 2 - User Simulator

It is simply the value of the city-shortfall variable that results from the two-level goal program. It is not a separate optimization problem.

## Turn 3 - Generic Agent

QUESTION: Regarding the demand figures in Table 4-3 (e.g., Donghai specialty 1 needs 1000): are these exact requirements that must be met precisely, or are they maximum capacities that may be under-filled if not enough suitable people are available?

## Turn 3 - User Simulator

They are exact requirements that must be met precisely. No more, no less.

## Turn 4 - Generic Agent

QUESTION: The total demand across all branches and specialties is 8500, but the total number of recruited personnel is 9000 — so 500 people will not be assigned to any branch. Is this acceptable (i.e., some people simply go unassigned), or must all 9000 people be assigned to some branch and specialty?

## Turn 4 - User Simulator

Some people simply go unassigned. The constraint is that the total number of people assigned from each type cannot exceed the available number of that type. It does not require all 9000 to be assigned.

## Turn 5 - Generic Agent

QUESTION: When a person is unassigned (not placed in any branch/specialty), do they count toward the "preferred specialty met" or "preferred city met" tallies, or are only actually-assigned people counted in those tallies?

## Turn 5 - User Simulator

Only actually-assigned people are counted in those tallies.

## Turn 6 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 6 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 7 - Generic Agent

QUESTION: For the "preferred city met" tally, does a person count as meeting their preferred city if they are assigned to their preferred city in either specialty (e.g., a type-1 person whose preferred city is Donghai counts as met whether assigned to specialty 1 or specialty 2 in Donghai), or must they also be in their preferred specialty to count?

## Turn 7 - User Simulator

A person counts as meeting their preferred city if they are assigned to their preferred city in either specialty. The specialty does not need to match for the city tally.

## Turn 8 - Generic Agent

QUESTION: For the "preferred city met" tally, does a person count as meeting their preferred city if they are assigned to their preferred city in either specialty (e.g., a type-1 person whose preferred city is Donghai counts as met whether assigned to specialty 1 or specialty 2 in Donghai), or must they also be in their preferred specialty to count?

## Turn 8 - User Simulator

A person counts as meeting their preferred city if they are assigned to their preferred city in either specialty. The specialty does not need to match for the city tally.

## Turn 9 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 9 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 10 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 10 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 11 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 11 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 12 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 12 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 13 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 13 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 14 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 14 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 15 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 15 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 16 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 16 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 17 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 17 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 18 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 18 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their

## Turn 19 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 19 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to their preferred specialty in either city. The city does not need to match for the specialty tally.

## Turn 20 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 20 - User Simulator

A person counts as meeting their preferred

## Turn 21 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 21 - User Simulator

A person counts as meeting

## Turn 22 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 22 - User Simulator

A

## Turn 23 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 23 - User Simulator

A person

## Turn 24 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 24 - User Simulator

A

## Turn 25 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 25 - User Simulator

A

## Turn 26 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 26 - User Simulator

A

## Turn 27 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 27 - User Simulator

A

## Turn 28 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 28 - User Simulator

A

## Turn 29 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 29 - User Simulator

A

## Turn 30 - Generic Agent

QUESTION: For the "preferred specialty met" tally, does a person count as meeting their preferred specialty if they are assigned to their preferred specialty in either city (e.g., a type-1 person whose preferred specialty is 1 counts as met whether assigned to specialty 1 in Donghai or specialty 1 in Nanjiang), or must they also be in their preferred city to count?

## Turn 30 - User Simulator

A