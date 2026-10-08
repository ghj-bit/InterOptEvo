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

QUESTION: When you say "the total number of people assigned from each type cannot exceed the available number of that type," do you mean each type's 1500 people must all be assigned (so the total assigned is exactly 9000, which exceeds the 8500 total branch demand), or may some recruited people be left unassigned (so the total assigned is at most 9000 and must fit within the 8500 branch demand)?

## Turn 1 - User Simulator

Some recruited people may be left unassigned. The total assigned is at most 9000 and must fit within the 8500 branch demand.

## Turn 2 - Generic Agent

QUESTION: For the branch demand numbers in Table 4-3 (e.g., Donghai specialty 1 = 1000), are these exact requirements that must be met precisely, or are they maximum capacities that may be underfilled?

## Turn 2 - User Simulator

They are exact requirements that must be met precisely.

## Turn 3 - Generic Agent

QUESTION: Since the branch demands must be met exactly (totaling 8500) but up to 9000 people may be assigned, does "assigned" mean a person is counted as assigned only if they fill one of the 8500 branch positions, so that at least 500 of the 9000 recruited people are necessarily left unassigned?

## Turn 3 - User Simulator

Yes, "assigned" means a person fills one of the 8500 branch positions, so at least 500 of the 9000 recruited people are necessarily left unassigned.

## Turn 4 - Generic Agent

QUESTION: For the "preferred specialty" goal, is a person counted as meeting their preferred specialty only if they are assigned to a branch position in that specialty, or does a person also count as meeting it if they are assigned to their preferred specialty in either city (i.e., the city does not matter for this goal)?

## Turn 4 - User Simulator

A person counts as meeting their preferred specialty if they are assigned to a branch position in that specialty, regardless of which city it is in.

## Turn 5 - Generic Agent

QUESTION: For the "preferred city" goal, is a person counted as meeting their preferred city only if they are assigned to a branch position in that city, regardless of which specialty they are assigned to?

## Turn 5 - User Simulator

Yes, a person counts as meeting their preferred city if they are assigned to a branch position in that city, regardless of which specialty they are assigned to.

## Turn 6 - Generic Agent

QUESTION: You listed three objectives: (1) 8000 meet preferred specialty, (2) 8000 meet preferred city, and (3) minimize the number who cannot be assigned to their preferred city. Are (1) and (2) hard constraints that must be satisfied (i.e., at least 8000 must meet each), with (3) as the objective to minimize, or are all three goals to be balanced in a multi-objective sense?

## Turn 6 - User Simulator

They are not hard constraints. All three goals are to be balanced in a multi-objective sense, with priorities in strict order: first meet all branch demand exactly, then try to get 8000 people into their preferred specialty, and finally aim for 8000 people in their preferred city.

## Turn 7 - Generic Agent

QUESTION: You said the priorities are in strict order: first meet all branch demand exactly, then try to get 8000 into preferred specialty, and finally aim for 8000 in preferred city. Since meeting branch demand exactly (8500 positions) is always feasible, is the actual optimization a lexicographic one where you first maximize the number of people in their preferred specialty (up to 8000), and only among solutions achieving that maximum do you then maximize the number in their preferred city (up to 8000)?

## Turn 7 - User Simulator

Yes, it is a lexicographic optimization: first maximize the number of people in their preferred specialty (up to 8000), and only among solutions achieving that maximum, maximize the number in their preferred city (up to 8000).

## Turn 8 - Generic Agent

QUESTION: For the "preferred city" goal, is a person who is left unassigned (does not fill any of the 8500 branch positions) counted as "not meeting their preferred city," or are unassigned people simply excluded from the preferred-city count?

## Turn 8 - User Simulator

Unassigned people are simply excluded from the preferred-city count.

## Turn 9 - Generic Agent

QUESTION: For the "preferred specialty" goal, are unassigned people also simply excluded from the preferred-specialty count (i.e., only assigned people are counted toward the 8000 preferred-specialty target)?

## Turn 9 - User Simulator

Yes, unassigned people are simply excluded from the preferred-specialty count.

## Turn 10 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, is this count taken over all 9000 recruited people (so unassigned people are counted as "cannot be assigned to their preferred city"), or only over the 8500 assigned people?

## Turn 10 - User Simulator

This count is taken over all 9000 recruited people, so unassigned people are counted as "cannot be assigned to their preferred city."

## Turn 11 - Generic Agent

QUESTION: You mentioned three goals in strict priority order: (1) meet branch demand exactly, (2) maximize preferred-specialty matches up to 8000, (3) maximize preferred-city matches up to 8000. Is the "minimum number who cannot be assigned to their preferred city" (counted over all 9000) a separate fourth objective with its own priority level, or is it simply the reported outcome (9000 minus the preferred-city matches) that you want displayed after solving the lexicographic problem?

## Turn 11 - User Simulator

It is simply the reported outcome (9000 minus the preferred-city matches) that you want displayed after solving the lexicographic problem.

## Turn 12 - Generic Agent

QUESTION: For the "suitable specialty" restriction, is it correct that a person of a given type can only be assigned to a branch position whose specialty is in that type's suitable specialty set (e.g., type 6 can only be assigned to specialty 3 positions in either city), and there is no other restriction on which city a person can be assigned to?

## Turn 12 - User Simulator

Yes, a person of a given type can only be assigned to a branch position whose specialty is in that type's suitable specialty set, and there is no other restriction on which city a person can be assigned to.

## Turn 13 - Generic Agent

QUESTION: Since the branch demands must be met exactly (8500 positions) and each type has 1500 people (9000 total), with each person assigned to at most one position, is it correct that the model should allow any number from 0 up to 1500 of each type to be assigned (with the rest unassigned), subject to the suitable-specialty restriction and the exact branch demands?

## Turn 13 - User Simulator

Yes, the model should allow any number from 0 up to 1500 of each type to be assigned, with the rest unassigned, subject to the suitable-specialty restriction and the exact branch demands.

## Turn 14 - Generic Agent

QUESTION: For the lexicographic objective, when you say "maximize the number of people in their preferred specialty (up to 8000)," is the first-level objective to maximize the total count of assigned people who are in their preferred specialty (with 8000 being just the target/ceiling for reporting), or is it to maximize the count but capped at 8000 (i.e., once you reach 8000, additional preferred-specialty matches give no extra benefit)?

## Turn 14 - User Simulator

It is to maximize the count but capped at 8000, meaning once you reach 8000, additional preferred-specialty matches give no extra benefit.

## Turn 15 - Generic Agent

QUESTION: For the second-level objective (preferred city), is it also capped at 8000 in the same way, meaning once you reach 8000 assigned people in their preferred city, additional preferred-city matches give no extra benefit?

## Turn 15 - User Simulator

Yes, it is also capped at 8000, meaning once you reach 8000 assigned people in their preferred city, additional preferred-city matches give no extra benefit.

## Turn 16 - Generic Agent

QUESTION: For the "preferred specialty" count, is a person counted as matching their preferred specialty if they are assigned to a branch position in that specialty, even if that position is in a city different from their preferred city? (For example, a type-1 person whose preferred specialty is 1 and preferred city is Donghai would count as a preferred-specialty match if assigned to specialty 1 in Nanjiang.)

## Turn 16 - User Simulator

Yes, a person is counted as matching their preferred specialty if they are assigned to a branch position in that specialty, even if that position is in a city different from their preferred city.

## Turn 17 - Generic Agent

QUESTION: For the "preferred city" count, is a person counted as matching their preferred city if they are assigned to a branch position in that city, even if that position is in a specialty different from their preferred specialty? (For example, a type-1 person whose preferred specialty is 1 and preferred city is Donghai would count as a preferred-city match if assigned to specialty 2 in Donghai.)

## Turn 17 - User Simulator

Yes, a person is counted as matching their preferred city if they are assigned to a branch position in that city, even if that position is in a specialty different from their preferred specialty.

## Turn 18 - Generic Agent

QUESTION: Are the decision variables (number of people of each type assigned to each city-specialty position) required to be integers, or can they be treated as continuous values?

## Turn 18 - User Simulator

They must be integers.

## Turn 19 - Generic Agent

QUESTION: For the lexicographic optimization, is the first-level objective to maximize the number of assigned people in their preferred specialty (capped at 8000), and the second-level objective to maximize the number of assigned people in their preferred city (capped at 8000), with no other objectives or constraints beyond the exact branch demands, suitable-specialty restrictions, and type availability limits?

## Turn 19 - User Simulator

Yes, that is correct.

## Turn 20 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision variables:** Integer variables x[t, c, s] = number of people of type t assigned to city c, specialty s, for t = 1..6, c ∈ {Donghai, Nanjiang}, s ∈ {1, 2, 3}.

**Constraints:**
1. **Suitable specialty:** x[t, c, s] = 0 if specialty s is not in type t's suitable specialty set (per Table 4-4).
2. **Type availability:** For each type t, the sum of x[t, c, s] over all cities and specialties ≤ 1500.
3. **Exact branch demand:** For each city c and specialty s, the sum of x[t, c, s] over all types t = the demand in Table 4-3 (totaling 8500).

**Lexicographic objective (strict priority order):**
- **Level 1:** Maximize the number of assigned people in their preferred specialty, capped at 8000. A person of type t counts as a preferred-specialty match if assigned to a position in specialty = t's preferred specialty (regardless of city).
- **Level 2:** Among solutions achieving the Level 1 maximum, maximize the number of assigned people in their preferred city, capped at 8000. A person of type t counts as a preferred-city match if assigned to a position in city = t's preferred city (regardless of specialty).

**Reported outcome:** After solving, report the minimum number of recruited personnel who cannot be assigned to their preferred city = 9000 − (preferred-city matches).

**Key clarifications confirmed:**
- Unassigned people are excluded from both the preferred-specialty and preferred-city counts.
- The "cannot be assigned to preferred city" count includes unassigned people (hence 9000 minus matches).
- At least 500 people will be unassigned (9000 recruited, 8500 positions).
- All variables are non-negative integers.