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

QUESTION: For the two goals of "8000 meet preferred specialty" and "8000 meet preferred city", should the model maximize the number of people meeting each goal (i.e., treat 8000 as a target to be approached as closely as possible, penalizing both shortfalls and excesses), or should it only require at least 8000 to meet each goal (i.e., treat 8000 as a lower bound that must be satisfied)?

## Turn 1 - User Simulator

Treat 8000 as a target to be approached as closely as possible, penalizing both shortfalls and excesses.

## Turn 2 - Generic Agent

QUESTION: The third objective is to "determine the minimum number of recruited personnel who cannot be assigned to their preferred city" — should this be a separate minimization objective (i.e., minimize the number of people assigned to a city different from their preferred city), or is it simply a reported output computed from the final assignment (i.e., total 9000 minus the number who got their preferred city)?

## Turn 2 - User Simulator

It is a separate minimization objective.

## Turn 3 - Generic Agent

QUESTION: Since there are now three objectives (approach 8000 for preferred specialty, approach 8000 for preferred city, and minimize the number not in preferred city), how should they be combined — should I use a weighted sum with specific weights you provide, or use lexicographic (priority-ordered) optimization where one objective is optimized first, then the next, and so on?

## Turn 3 - User Simulator

Use lexicographic (priority-ordered) optimization.

## Turn 4 - Generic Agent

QUESTION: In the lexicographic ordering, what is the priority sequence of the three objectives — is it (1) approach 8000 for preferred specialty, (2) approach 8000 for preferred city, (3) minimize number not in preferred city, or a different order?

## Turn 4 - User Simulator

The priority sequence is: (1) approach 8000 for preferred specialty, (2) approach 8000 for preferred city, (3) minimize number not in preferred city.

## Turn 5 - Generic Agent

QUESTION: Regarding the branch demand numbers in Table 4-3 (e.g., Donghai City specialty 1 needs 1000), should these be treated as exact requirements that must be met precisely, or as upper bounds (maximum capacity) that the assignment cannot exceed?

## Turn 5 - User Simulator

They should be treated as exact requirements that must be met precisely.

## Turn 6 - Generic Agent

QUESTION: Regarding the "Number of People" column in Table 4-4 (1500 for each of the 6 types, totaling 9000), should all 9000 people be assigned (i.e., the total supply must be fully utilized), or is it possible that some people remain unassigned?

## Turn 6 - User Simulator

All 9000 people must be assigned.

## Turn 7 - Generic Agent

QUESTION: For the "approach 8000" goals, the deviation is measured as |actual − 8000|. Since the total is 9000 and each person has exactly one preferred specialty and one preferred city, the maximum possible count for either goal is 9000. Should the penalty for exceeding 8000 (i.e., having more than 8000 meet the goal) be the same magnitude as the penalty for falling short of 8000, or should exceeding 8000 be penalized less (or not at all)?

## Turn 7 - User Simulator

The penalty for exceeding 8000 should be the same magnitude as the penalty for falling short of 8000.

## Turn 8 - Generic Agent

QUESTION: For the lexicographic optimization, when I fix the first objective (approach 8000 for preferred specialty) at its optimal value and then optimize the second objective (approach 8000 for preferred city), should I constrain the first objective to be exactly at its optimal value, or should I allow it to be within some tolerance of the optimal value?

## Turn 8 - User Simulator

Constrain the first objective to be exactly at its optimal value.

## Turn 9 - Generic Agent

QUESTION: For the "approach 8000 for preferred specialty" objective, the count of people meeting their preferred specialty is the sum over all 6 types of people assigned to their preferred specialty. Since each type has a fixed preferred specialty (e.g., Type 1 prefers specialty 1), and a person can only be assigned to a specialty in their suitable set, is it possible that a type's preferred specialty is NOT in their suitable specialty set (which would make it impossible for that type to ever meet their preferred specialty)? Looking at the table, all types' preferred specialties appear to be in their suitable sets — can I confirm this is correct and there are no additional restrictions?

## Turn 9 - User Simulator

Yes, that is correct. All types' preferred specialties are in their suitable specialty sets, and there are no additional restrictions.

## Turn 10 - Generic Agent

QUESTION: For the "approach 8000 for preferred city" objective, the count of people meeting their preferred city is the sum over all 6 types of people assigned to their preferred city. Since each person is assigned to exactly one branch (city + specialty), a person meets their preferred city if and only if they are assigned to any specialty in their preferred city. Is this correct — i.e., the city goal is satisfied regardless of which specialty within that city they are assigned to?

## Turn 10 - User Simulator

Yes, that is correct. A person meets their preferred city if they are assigned to any specialty in that city.

## Turn 11 - Generic Agent

QUESTION: For the third objective (minimize the number not in preferred city), this is equivalent to 9000 minus the number who got their preferred city. Since the second objective already optimizes the number who got their preferred city (approaching 8000), and the third objective minimizes the complement, are these two objectives perfectly aligned (i.e., maximizing preferred-city count is the same as minimizing non-preferred-city count), or is there a subtle difference I should be aware of?

## Turn 11 - User Simulator

They are perfectly aligned. Maximizing the preferred-city count is the same as minimizing the non-preferred-city count.

## Turn 12 - Generic Agent

QUESTION: Since the second objective (approach 8000 for preferred city) and the third objective (minimize number not in preferred city) are perfectly aligned, does the lexicographic optimization effectively reduce to two stages — (1) approach 8000 for preferred specialty, then (2) approach 8000 for preferred city (which simultaneously minimizes the number not in preferred city) — or do you still want me to explicitly model and report the third objective as a separate step even though it is redundant?

## Turn 12 - User Simulator

You should still explicitly model and report the third objective as a separate step, even though it is redundant.

## Turn 13 - Generic Agent

QUESTION: For the decision variables, should I model this as assigning individual people (i.e., 9000 binary variables), or is it sufficient to model the number of people of each type assigned to each city-specialty combination (i.e., 6 types × 6 city-specialty combinations = 36 continuous or integer variables), since people within the same type are indistinguishable?

## Turn 13 - User Simulator

It is sufficient to model the number of people of each type assigned to each city-specialty combination (i.e., 6 types × 6 city-specialty combinations = 36 continuous or integer variables).

## Turn 14 - Generic Agent

QUESTION: Should the 36 decision variables (number of type-t people assigned to city-specialty combination) be constrained to be integers, or can they be continuous (since the numbers are large and the optimal solution will naturally be integral due to the problem structure)?

## Turn 14 - User Simulator

They can be continuous.

## Turn 15 - Generic Agent

QUESTION: For the suitability constraint, a person of type t can only be assigned to a specialty in their suitable set. Does this mean that for a given type t, the variable x[t, city, specialty] must be zero for any specialty NOT in type t's suitable set, regardless of which city it is in? For example, Type 6 (suitable specialty: 3 only) can only be assigned to specialty 3 in either Donghai or Nanjiang, and must have zero assigned to specialties 1 and 2 in both cities?

## Turn 15 - User Simulator

Yes, that is correct.

## Turn 16 - Generic Agent

QUESTION: For the demand constraints in Table 4-3, the demand for each city-specialty combination (e.g., Donghai City specialty 1 = 1000) must be met exactly. Does this mean the sum of x[t, city, specialty] over all 6 types t must equal the demand for that city-specialty combination?

## Turn 16 - User Simulator

Yes, that is correct.

## Turn 17 - Generic Agent

QUESTION: For the supply constraint, the total number of type-t people assigned across all city-specialty combinations must equal 1500 for each type t (since all 9000 must be assigned and each type has exactly 1500 people). Is this correct — i.e., the sum of x[t, city, specialty] over all 6 city-specialty combinations equals 1500 for each type t?

## Turn 17 - User Simulator

Yes, that is correct.

## Turn 18 - Generic Agent

QUESTION: For the "approach 8000 for preferred specialty" objective, the count of people meeting their preferred specialty is the sum over all types t of x[t, city, preferred_specialty(t)] summed over both cities. For example, Type 1 prefers specialty 1, so the contribution is x[1, Donghai, 1] + x[1, Nanjiang, 1]. Is this correct — i.e., a person meets their preferred specialty if they are assigned to that specialty in either city?

## Turn 18 - User Simulator

Yes, that is correct.

## Turn 19 - Generic Agent

QUESTION: For the "approach 8000 for preferred city" objective, the count of people meeting their preferred city is the sum over all types t of x[t, preferred_city(t), specialty] summed over all specialties in that city. For example, Type 1 prefers Donghai, so the contribution is x[1, Donghai, 1] + x[1, Donghai, 2] (since Type 1's suitable specialties are 1 and 2). Is this correct?

## Turn 19 - User Simulator

Yes, that is correct.

## Turn 20 - Generic Agent

QUESTION: For the lexicographic optimization, when I fix the first objective (deviation from 8000 for preferred specialty) at its optimal value, I need to express this as a constraint. The deviation is |count_preferred_specialty − 8000|. Should I fix this as a single equality constraint (count_preferred_specialty = 8000 + d* or count_preferred_specialty = 8000 − d*, where d* is the optimal deviation), or should I allow both the positive and negative deviations to be fixed at their optimal values simultaneously?

## Turn 20 - User Simulator

Fix it as a single equality constraint: count_preferred_specialty = 8000 + d* or count_preferred_specialty = 8000 − d*, where d* is the optimal deviation.

## Turn 21 - Generic Agent

QUESTION: For the second stage of the lexicographic optimization, when I fix the second objective (deviation from 8000 for preferred city) at its optimal value, should I similarly fix it as a single equality constraint (count_preferred_city = 8000 + d2* or count_preferred_city = 8000 − d2*), and then in the third stage minimize the number not in preferred city (which equals 9000 − count_preferred_city)?

## Turn 21 - User Simulator

Yes, that is correct.

## Turn 22 - Generic Agent

QUESTION: For the non-negativity of the decision variables, should I explicitly state that all x[t, city, specialty] ≥ 0, or is this implied by the context of counting people?

## Turn 22 - User Simulator

You should explicitly state that all x[t, city, specialty] ≥ 0.

## Turn 23 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision Variables:**
- x[t, city, specialty] ≥ 0 (continuous) for t = 1..6, city ∈ {Donghai, Nanjiang}, specialty ∈ {1, 2, 3} — 36 variables total.
- x[t, city, specialty] = 0 if specialty is not in type t's suitable specialty set.

**Constraints:**
1. **Supply:** For each type t, sum over all 6 city-specialty combinations of x[t, city, specialty] = 1500.
2. **Demand:** For each city-specialty combination, sum over all 6 types of x[t, city, specialty] = the demand in Table 4-3 (Donghai: 1000, 2000, 1500; Nanjiang: 2000, 1000, 1000).
3. **Suitability:** x[t, city, specialty] = 0 if specialty ∉ suitable set of type t.

**Objectives (lexicographic, 3 stages):**

- **Stage 1:** Minimize |count_preferred_specialty − 8000|, where count_preferred_specialty = Σ_t Σ_city x[t, city, preferred_specialty(t)].
- **Stage 2:** Subject to count_preferred_specialty = 8000 ± d* (fixed at Stage 1 optimal), minimize |count_preferred_city − 8000|, where count_preferred_city = Σ_t Σ_specialty x[t, preferred_city(t), specialty].
- **Stage 3:** Subject to count_preferred_city = 8000 ± d2* (fixed at Stage 2 optimal), minimize (9000 − count_preferred_city) — explicitly modeled and reported as a separate step.

**Key confirmed facts:**
- All 9000 people must be assigned.
- Demands are exact equalities.
- A person meets preferred specialty if assigned to that specialty in either city.
- A person meets preferred city if assigned to any specialty in that city.
- Penalty for exceeding 8000 equals penalty for falling short.
- Variables are continuous, non-negative.
- Each lexicographic stage fixes the prior objective at its exact optimal value.