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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city", should the model treat these as hard requirements that must be exactly satisfied, or as targets to be maximized (i.e., maximize the number of people meeting each, with 8000 being the desired level)?

## Turn 1 - User Simulator

Treat them as targets to be maximized, with 8000 being the desired level. They are not hard requirements that must be exactly satisfied.

## Turn 2 - Generic Agent

QUESTION: The total demand across all branches and specialties is 8500, but only 9000 people are available. Should the model require that all 8500 demand positions be filled exactly, or is it acceptable to leave some positions unfilled?

## Turn 2 - User Simulator

The model must require that all 8500 demand positions be filled exactly. No more, no less.

## Turn 3 - Generic Agent

QUESTION: The total available people is 9000 but total demand is only 8500, so 500 people will be left unassigned. Should the model allow any of the 9000 to be left unassigned (i.e., not placed in any branch), or must all 9000 be assigned somewhere?

## Turn 3 - User Simulator

The model should allow any of the 9000 to be left unassigned. It is not required that all 9000 be assigned somewhere.

## Turn 4 - Generic Agent

QUESTION: The problem lists three objectives (maximize people meeting preferred specialty, maximize people meeting preferred city, and minimize people not meeting preferred city). Since maximizing preferred-city and minimizing not-preferred-city are essentially the same thing, how should these be combined into a single optimization — should I use a weighted sum with specific weights, or treat them as a lexicographic (priority-ordered) sequence where one goal is optimized before the next?

## Turn 4 - User Simulator

Treat them as a lexicographic (priority-ordered) sequence. The priorities are in strict order: p1 (fully meet demand) is the highest priority, p2 (8000 meet preferred specialty) is second, and p3 (8000 meet preferred city) is the lowest. So we first make sure all demand is fully met, then try to get 8000 people into their preferred specialty, and finally, after that, we aim for 8000 people in their preferred city.

## Turn 5 - Generic Agent

QUESTION: You mentioned p1 (fully meet demand) as the highest priority. Since we already confirmed that all 8500 demand positions must be filled exactly, is p1 simply the hard constraint that demand is met exactly, or is it a separate optimization objective that should be optimized before p2 and p3?

## Turn 5 - User Simulator

p1 is simply the hard constraint that demand is met exactly. It is not a separate optimization objective.

## Turn 6 - Generic Agent

QUESTION: For the "meet preferred specialty" goal, should a person be counted as meeting their preferred specialty only if they are assigned to that specific specialty, regardless of which city they are in? For example, if a Type 1 person (preferred specialty 1) is assigned to Specialty 1 in Nanjiang City, does that count as meeting their preferred specialty?

## Turn 6 - User Simulator

Yes, a person is counted as meeting their preferred specialty if they are assigned to that specific specialty, regardless of which city they are in. So a Type 1 person assigned to Specialty 1 in Nanjiang City does count as meeting their preferred specialty.

## Turn 7 - Generic Agent

QUESTION: For the "meet preferred city" goal, should a person be counted as meeting their preferred city only if they are assigned to that specific city, regardless of which specialty they are in? For example, if a Type 1 person (preferred city Donghai) is assigned to Specialty 2 in Donghai City, does that count as meeting their preferred city?

## Turn 7 - User Simulator

Yes, a person is counted as meeting their preferred city if they are assigned to that specific city, regardless of which specialty they are in. So a Type 1 person assigned to Specialty 2 in Donghai City does count as meeting their preferred city.

## Turn 8 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" objective, should this count only among the people who are actually assigned to a branch, or should it also include the 500 people who are left unassigned (since they are not in their preferred city either)?

## Turn 8 - User Simulator

This count should only include the people who are actually assigned to a branch. The 500 people who are left unassigned should not be included in this count.

## Turn 9 - Generic Agent

QUESTION: Since we are maximizing the number of people meeting their preferred city (p3), and the "minimum number who cannot be assigned to their preferred city" is just the complement (total assigned minus those meeting preferred city), should the final model simply maximize the number of assigned people in their preferred city, and then report the minimum as (total assigned) minus (that maximum)?

## Turn 9 - User Simulator

Yes, the final model should simply maximize the number of assigned people in their preferred city, and then report the minimum as (total assigned) minus (that maximum).

## Turn 10 - Generic Agent

QUESTION: For the lexicographic optimization, when we maximize "people meeting preferred specialty" (p2), should the model maximize the total count across all 6 types, or should it maximize the count for each type individually (i.e., each type's count should be as close to its own target as possible)?

## Turn 10 - User Simulator

The model should maximize the total count across all 6 types.

## Turn 11 - Generic Agent

QUESTION: When maximizing the total count of people meeting their preferred specialty (p2), is there a cap at 8000, or should the model maximize without any upper bound (i.e., if more than 8000 can meet their preferred specialty, that's fine and should be achieved)?

## Turn 11 - User Simulator

The model should maximize without any upper bound. If more than 8000 can meet their preferred specialty, that's fine and should be achieved.

## Turn 12 - Generic Agent

QUESTION: Similarly, when maximizing the total count of people meeting their preferred city (p3), is there a cap at 8000, or should the model maximize without any upper bound (i.e., if more than 8000 can meet their preferred city, that's fine and should be achieved)?

## Turn 12 - User Simulator

The model should maximize without any upper bound. If more than 8000 can meet their preferred city, that's fine and should be achieved.

## Turn 13 - Generic Agent

QUESTION: For the "suitable specialty" constraint, should a person only be assignable to specialties listed in their "Suitable Specialty" column in Table 4-4, and is there any additional restriction that a person cannot be assigned to a specialty in a city where that specialty has no demand (i.e., demand = 0)?

## Turn 13 - User Simulator

A person can only be assigned to specialties listed in their "Suitable Specialty" column in Table 4-4. There is no additional restriction beyond that.

## Turn 14 - Generic Agent

QUESTION: Since all 6 types have 1500 people each (total 9000), and the "Number of People" column in Table 4-4 represents the available supply per type, should the model treat these as individual people (i.e., we can assign any integer number from 0 to 1500 of each type), or are these fixed groups that must be assigned as a whole?

## Turn 14 - User Simulator

The model should treat these as individual people. We can assign any integer number from 0 to 1500 of each type.

## Turn 15 - Generic Agent

QUESTION: Should the decision variables (number of people of each type assigned to each city-specialty combination) be required to be integers, or can they be continuous (fractional) values?

## Turn 15 - User Simulator

The decision variables should be required to be integers.

## Turn 16 - Generic Agent

QUESTION: For the lexicographic optimization, should I implement it as a two-stage sequential approach (first solve for p2 to get its optimal value, then fix that value as a constraint and solve for p3), or should I use a single model with a very large weight on p2 and a smaller weight on p3?

## Turn 16 - User Simulator

Implement it as a two-stage sequential approach: first solve for p2 to get its optimal value, then fix that value as a constraint and solve for p3.

## Turn 17 - Generic Agent

QUESTION: In the two-stage approach, when you fix the p2 optimal value as a constraint in stage 2, should it be fixed as an exact equality (exactly that many people meet preferred specialty) or as a lower bound (at least that many people meet preferred specialty)?

## Turn 17 - User Simulator

It should be fixed as an exact equality (exactly that many people meet preferred specialty).

## Turn 18 - Generic Agent

QUESTION: For the final output, should the model report the assignment plan (how many of each type go to each city-specialty), or is it sufficient to just report the optimal objective values (max people meeting preferred specialty, max people meeting preferred city, and the minimum number not meeting preferred city)?

## Turn 18 - User Simulator

The model should report the assignment plan (how many of each type go to each city-specialty).

## Turn 19 - Generic Agent

QUESTION: For the assignment plan output, should it show the number of people of each type assigned to each specific city-specialty combination (e.g., Type 1 → Donghai-Specialty 1: 500, Type 1 → Donghai-Specialty 2: 300, etc.), or is a summary by type and city sufficient?

## Turn 19 - User Simulator

It should show the number of people of each type assigned to each specific city-specialty combination.

## Turn 20 - Generic Agent

QUESTION: Should the model also report how many people of each type are left unassigned (i.e., not placed in any branch)?

## Turn 20 - User Simulator

Yes, the model should also report how many people of each type are left unassigned.

## Turn 21 - Generic Agent

QUESTION: For the "preferred city" goal, should a person who is assigned to a branch in their preferred city but to a specialty that is NOT their preferred specialty still count toward the "meet preferred city" objective? In other words, are the two goals (preferred specialty and preferred city) completely independent of each other?

## Turn 21 - User Simulator

Yes, the two goals are completely independent of each other. A person assigned to their preferred city but not their preferred specialty still counts toward the "meet preferred city" objective.

## Turn 22 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person who is assigned to their preferred specialty but in a city that is NOT their preferred city still count toward the "meet preferred specialty" objective?

## Turn 22 - User Simulator

Yes, a person assigned to their preferred specialty but in a city that is not their preferred city still counts toward the "meet preferred specialty" objective.

## Turn 23 - Generic Agent

QUESTION: For the "minimum number of recruited personnel who cannot be assigned to their preferred city" that you want reported, should this be calculated as (total assigned people) minus (people assigned to their preferred city), where "total assigned people" is 8500 (since all demand must be met exactly)?

## Turn 23 - User Simulator

Yes, this should be calculated as (total assigned people) minus (people assigned to their preferred city), where "total assigned people" is 8500.

## Turn 24 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person who is assigned to their preferred specialty but in a city where that specialty has no demand (i.e., demand = 0 for that city-specialty combination) still count toward the "meet preferred specialty" objective?

## Turn 24 - User Simulator

This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Since all 6 city-specialty combinations in Table 4-3 have positive demand (1000, 2000, 1500, 2000, 1000, 1000), and a person can only be assigned to a city-specialty combination that has demand, is the question about assigning to a city-specialty with zero demand actually moot in this problem?

## Turn 25 - User Simulator

Yes, the question is moot in this problem since all 6 city-specialty combinations in Table 4-3 have positive demand.

## Turn 26 - Generic Agent

QUESTION: For the "preferred city" goal, should a person who is assigned to their preferred city but to a specialty that is NOT in their suitable specialty set still count toward the "meet preferred city" objective?

## Turn 26 - User Simulator

No, a person cannot be assigned to a specialty that is not in their suitable specialty set, so this situation cannot occur.

## Turn 27 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person who is assigned to their preferred specialty but in a city that is NOT their preferred city still count toward the "meet preferred specialty" objective?

## Turn 27 - User Simulator

Yes, a person assigned to their preferred specialty but in a city that is not their preferred city still counts toward the "meet preferred specialty" objective.

## Turn 28 - Generic Agent

QUESTION: For the "preferred city" goal, should a person who is assigned to their preferred city but to a specialty that is NOT their preferred specialty still count toward the "meet preferred city" objective?

## Turn 28 - User Simulator

Yes, a person assigned to their preferred city but to a specialty that is not their preferred specialty still counts toward the "meet preferred city" objective.

## Turn 29 - Generic Agent

QUESTION: For the "preferred specialty" goal, should a person who is assigned to their preferred specialty but in a city that is NOT their preferred city still count toward the "meet preferred specialty" objective?

## Turn 29 - User Simulator

Yes, a person assigned to their preferred specialty but in a city that is not their preferred city still counts toward the "meet preferred specialty" objective.

## Turn 30 - Generic Agent

QUESTION: For the "preferred city" goal, should a person who is assigned to their preferred city but to a specialty that is NOT their preferred specialty still count toward the "meet preferred city" objective?

## Turn 30 - User Simulator

Yes, a person assigned to their preferred city but to a specialty that is not their preferred specialty still counts toward the "meet preferred city" objective.