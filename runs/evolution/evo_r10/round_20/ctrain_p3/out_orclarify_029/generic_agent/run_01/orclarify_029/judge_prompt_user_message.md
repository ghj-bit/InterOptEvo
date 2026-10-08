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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city", should the model treat these as hard requirements that must be exactly satisfied, or as targets to be achieved as closely as possible (i.e., maximize the number meeting each goal, subject to the 8000 target)?

## Turn 1 - User Simulator

Treat them as targets to be achieved as closely as possible. The goal is to maximize the number of people meeting each preference, with 8000 as the target level. They are not hard requirements that must be exactly satisfied.

## Turn 2 - Generic Agent

QUESTION: The total demand across all branches and specialties is 8500, but the total number of recruited personnel is 9000. Should the model require that all 8500 demand slots be filled exactly (i.e., every branch-specialty demand is met), or is it acceptable to leave some demand slots unfilled?

## Turn 2 - User Simulator

The model must require that all 8500 demand slots be filled exactly. Every branch-specialty demand in Table 4-3 must be met with no more and no less than the specified numbers.

## Turn 3 - Generic Agent

QUESTION: Since there are 9000 recruited people but only 8500 demand slots, 500 people will be left unassigned. Should the model explicitly track and report these 500 unassigned people, or is it sufficient to simply allow up to 500 people to go unassigned without any further constraint or objective on them?

## Turn 3 - User Simulator

It is sufficient to simply allow up to 500 people to go unassigned without any further constraint or objective on them. The model does not need to explicitly track or report these 500 unassigned people.

## Turn 4 - Generic Agent

QUESTION: The objective mentions "determine the minimum number of recruited personnel who cannot be assigned to their preferred city." Should this be a separate minimization objective (i.e., minimize the number of assigned people whose city differs from their preferred city), or is it simply a reported quantity computed from the final assignment (i.e., the number of assigned people not in their preferred city, given the other objectives are optimized)?

## Turn 4 - User Simulator

It is a separate minimization objective. The model should minimize the number of assigned people whose city differs from their preferred city, as the third priority (p3), after fully meeting demand (p1) and maximizing the number meeting their preferred specialty (p2).

## Turn 5 - Generic Agent

QUESTION: You mentioned p1 (fully meet demand), p2 (maximize preferred specialty), and p3 (minimize non-preferred city). Where does the "maximize preferred city" goal (target 8000) fit in the priority hierarchy? Is it also p2 (same level as preferred specialty), or is it a separate priority level, or is it simply implied by p3 (minimizing non-preferred city)?

## Turn 5 - User Simulator

The "maximize preferred city" goal (target 8000) is simply implied by p3 (minimizing non-preferred city). It is not a separate priority level. The three priorities are: p1 (fully meet demand), p2 (maximize preferred specialty, target 8000), and p3 (minimize non-preferred city, which is equivalent to maximizing preferred city, target 8000).

## Turn 6 - Generic Agent

QUESTION: For p2 (maximize preferred specialty), should the model maximize the total number of assigned people who get their preferred specialty, or should it maximize the number up to the target of 8000 (i.e., cap the objective at 8000 so that once 8000 is reached, further improvements don't matter)?

## Turn 6 - User Simulator

The model should maximize the total number of assigned people who get their preferred specialty, with 8000 as the target level. It is not capped at 8000; the goal is to achieve as many as possible, aiming for the 8000 target.

## Turn 7 - Generic Agent

QUESTION: For p3 (minimize non-preferred city), should the model minimize the total number of assigned people who are NOT in their preferred city (i.e., minimize the count of people in the wrong city), or should it maximize the total number of assigned people who ARE in their preferred city?

## Turn 7 - User Simulator

The model should minimize the total number of assigned people who are NOT in their preferred city.

## Turn 8 - Generic Agent

QUESTION: For the "suitable specialty" constraint, if a person of a given type is assigned to a branch in a city, they must be assigned to a specialty that is in their suitable specialty set. Does this mean that a person of type 1 (suitable specialties 1,2) can be assigned to either specialty 1 or specialty 2 in either Donghai or Nanjiang, as long as that specialty is in their suitable set?

## Turn 8 - User Simulator

Yes, that is correct. A person of type 1 can be assigned to either specialty 1 or specialty 2 in either Donghai or Nanjiang, as long as that specialty is in their suitable set.

## Turn 9 - Generic Agent

QUESTION: For the "total number of people assigned from each type cannot exceed the available number of that type" constraint, should this be a strict upper bound (assigned ≤ available) or an equality (assigned = available)? In other words, can some people of a given type be left unassigned, or must all people of each type be assigned?

## Turn 9 - User Simulator

It should be a strict upper bound (assigned ≤ available). Some people of a given type can be left unassigned.

## Turn 10 - Generic Agent

QUESTION: For the decision variables, should the number of people of each type assigned to each branch-specialty combination be an integer, or can it be treated as a continuous variable (since the numbers are large, integrality may not matter in practice)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, should it count only people who are actually assigned (to a branch-specialty slot), or should it also include people who are unassigned but whose preferred specialty matches some demand?

## Turn 11 - User Simulator

It should count only people who are actually assigned to a branch-specialty slot.

## Turn 12 - Generic Agent

QUESTION: For the "preferred city" count in p3, should it count only people who are actually assigned to a branch in a city, or should it also include unassigned people?

## Turn 12 - User Simulator

It should count only people who are actually assigned to a branch in a city.

## Turn 13 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Nanjiang City (not their preferred city), do they still count toward the "preferred specialty" goal?

## Turn 13 - User Simulator

Yes, they still count toward the "preferred specialty" goal.

## Turn 14 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to specialty 2 (not their preferred specialty) in Donghai City, do they still count toward the "preferred city" goal?

## Turn 14 - User Simulator

Yes, they still count toward the "preferred city" goal.

## Turn 15 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Donghai City, they count toward the preferred specialty goal. But if a person of type 2 (preferred specialty 2) is assigned to specialty 2 in Donghai City, they also count. Is the preferred specialty goal simply the sum over all types of (number of people of that type assigned to their preferred specialty, regardless of city)?

## Turn 15 - User Simulator

Yes, the preferred specialty goal is simply the sum over all types of the number of people of that type assigned to their preferred specialty, regardless of city.

## Turn 16 - Generic Agent

QUESTION: For the "preferred city" count in p3, is the preferred city goal simply the sum over all types of the number of people of that type assigned to their preferred city, regardless of specialty?

## Turn 16 - User Simulator

Yes, the preferred city goal is simply the sum over all types of the number of people of that type assigned to their preferred city, regardless of specialty.

## Turn 17 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1, they count. But what if a person of type 3 (preferred specialty 1) is also assigned to specialty 1? Do they also count toward the preferred specialty goal, even though they are a different type?

## Turn 17 - User Simulator

Yes, they also count toward the preferred specialty goal.

## Turn 18 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to Donghai, they count. But what if a person of type 2 (preferred city Donghai) is also assigned to Donghai? Do they also count toward the preferred city goal, even though they are a different type?

## Turn 18 - User Simulator

Yes, they also count toward the preferred city goal.

## Turn 19 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1, they count. But what if a person of type 1 is assigned to specialty 2 (which is in their suitable set but not their preferred specialty)? Do they NOT count toward the preferred specialty goal?

## Turn 19 - User Simulator

Yes, they do NOT count toward the preferred specialty goal.

## Turn 20 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to Nanjiang, do they NOT count toward the preferred city goal?

## Turn 20 - User Simulator

Yes, they do NOT count toward the preferred city goal.

## Turn 21 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 1 in Nanjiang? Do they still count toward the preferred specialty goal?

## Turn 21 - User Simulator

Yes, they still count toward the preferred specialty goal.

## Turn 22 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 2 in Donghai? Do they still count toward the preferred city goal?

## Turn 22 - User Simulator

Yes, they still count toward the preferred city goal.

## Turn 23 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 1 in Nanjiang? Do they still count toward the preferred specialty goal?

## Turn 23 - User Simulator

Yes, they still count toward the preferred specialty goal.

## Turn 24 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 2 in Donghai? Do they still count toward the preferred city goal?

## Turn 24 - User Simulator

Yes, they still count toward the preferred city goal.

## Turn 25 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 1 in Nanjiang? Do they still count toward the preferred specialty goal?

## Turn 25 - User Simulator

Yes, they still count toward the preferred specialty goal.

## Turn 26 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 2 in Donghai? Do they still count toward the preferred city goal?

## Turn 26 - User Simulator

Yes, they still count toward the preferred city goal.

## Turn 27 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 1 in Nanjiang? Do they still count toward the preferred specialty goal?

## Turn 27 - User Simulator

Yes, they still count toward the preferred specialty goal.

## Turn 28 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 2 in Donghai? Do they still count toward the preferred city goal?

## Turn 28 - User Simulator

Yes, they still count toward the preferred city goal.

## Turn 29 - Generic Agent

QUESTION: For the "preferred specialty" count in p2, if a person of type 1 (preferred specialty 1) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 1 in Nanjiang? Do they still count toward the preferred specialty goal?

## Turn 29 - User Simulator

Yes, they still count toward the preferred specialty goal.

## Turn 30 - Generic Agent

QUESTION: For the "preferred city" count in p3, if a person of type 1 (preferred city Donghai) is assigned to specialty 1 in Donghai, they count. But what if a person of type 1 is assigned to specialty 2 in Donghai? Do they still count toward the preferred city goal?

## Turn 30 - User Simulator

Yes, they still count toward the preferred city goal.