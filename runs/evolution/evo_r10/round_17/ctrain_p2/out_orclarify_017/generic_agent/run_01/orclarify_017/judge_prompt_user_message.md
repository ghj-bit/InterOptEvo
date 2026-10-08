# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U11, U12, U13, U14, U16, U2, U3, U4, U5, U6, U7, U8, U9, U10
I need help planning a bombing mission to destroy enemy military targets. The mission is successful only if at least two of the four key parts are destroyed. The number of heavy bombs used cannot exceed 28, and the number of light bombs used cannot exceed 12. Total fuel consumption must not exceed 10,000 liters, and each bombing run is a round trip from the airport to the target and back.

The target has four key parts, numbered 1, 2, 3, 4.

| Key Part | Distance from Airport (km) | Probability of Destruction per Heavy Bomb | Probability of Destruction per Light Bomb |
|----------|----------------------------|------------------------------------------|------------------------------------------|
| 1        | 450                        | 0.03                                     | 0.08                                     |
| 2        | 480                        | 0.10                                     | 0.11                                     |
| 3        | 540                        | 0.05                                     | 0.12                                     |
| 4        | 600                        | 0.05                                     | 0.09                                     |

Heavy bombs available: 28.

Light bombs available: 12.

Total fuel available: 10,000 liters.

When carrying a heavy bomb, fuel efficiency is 2 km per liter.

When carrying a light bomb, fuel efficiency is 3 km per liter.

When the aircraft is empty (not carrying a bomb), fuel efficiency is 4 km per liter.

Each takeoff and landing combined consumes 100 liters of fuel per trip.

## Problem units
- U1 (context): I need help planning a bombing mission to destroy enemy military targets.
- U2 (data): The target has four key parts, numbered 1, 2, 3, 4.
- U3 (data): | Key Part | Distance from Airport (km) | Probability of Destruction per Heavy Bomb | Probability of Destruction per Light Bomb |
|----------|----------------------------|------------------------------------------|------------------------------------------|
| 1        | 450                        | 0.03                                     | 0.08                                     |
| 2        | 480                        | 0.10                                     | 0.11                                     |
| 3        | 540                        | 0.05                                     | 0.12                                     |
| 4        | 600                        | 0.05                                     | 0.09                                     |
- U4 (data): Heavy bombs available: 28.
- U5 (data): Light bombs available: 12.
- U6 (data): Total fuel available: 10,000 liters.
- U7 (data): When carrying a heavy bomb, fuel efficiency is 2 km per liter.
- U8 (data): When carrying a light bomb, fuel efficiency is 3 km per liter.
- U9 (data): When the aircraft is empty (not carrying a bomb), fuel efficiency is 4 km per liter.
- U10 (data): Each takeoff and landing combined consumes 100 liters of fuel per trip.
- U11 (constraint): The mission is successful only if at least two of the four key parts are destroyed.
- U12 (constraint): The number of heavy bombs used cannot exceed 28.
- U13 (constraint): The number of light bombs used cannot exceed 12.
- U14 (constraint): Total fuel consumption must not exceed 10,000 liters.
- U15 (constraint): Each aircraft can carry only one bomb per trip.
- U16 (constraint): Each bombing run is a round trip from the airport to the target and back.
- U17 (objective): Maximize the probability of success (destroying at least two key parts).

## Hidden slot scoring rules
## H1: missing_one_bomb_per_trip_constraint
- Severity: P1
- Severity reason: Without this constraint, the modeling agent may assume an aircraft can carry multiple bombs per trip, drastically altering the number of trips, fuel consumption calculations, and the overall model structure, leading to a materially incorrect formulation.
- Problem unit ID: U15
- Semantic hit rule: The agent's question must explicitly ask about the number of bombs an aircraft can carry per trip or the per‑trip carrying capacity.
- Reference acceptable questions:
  - Is there a limit on how many bombs a single aircraft can carry on a trip?
  - Can an aircraft carry more than one bomb per mission?
- Failure modes:
  - Assuming an unlimited number of bombs per aircraft per trip
  - Assuming all bombs can be dropped in a single trip

## H2: missing_objective_probability_maximization
- Severity: P0
- Severity reason: The objective is the core of the optimization problem; without it, the agent does not know what to maximize, making the problem ill‑posed and preventing any responsible modeling attempt.
- Problem unit ID: U17
- Semantic hit rule: The agent must ask about the objective or what is being maximized.
- Reference acceptable questions:
  - What exactly are we trying to optimize? Is it the probability of destroying at least two key parts?
  - What is the objective of the bombing plan?
- Failure modes:
  - Assuming a different objective like minimizing fuel or bombs used
  - Assuming all four parts must be destroyed


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed (with the bomb allocation chosen to achieve that), or is it to minimize the total fuel consumed subject to achieving a specified minimum probability of destroying at least two parts?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed, with the bomb allocation chosen to achieve that.

## Turn 2 - Generic Agent

QUESTION: For a given key part, if I assign h heavy bombs and l light bombs to it, is the probability that the part is destroyed equal to 1 minus the product of (1 minus the per-bomb destruction probability) for each bomb assigned to that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: When the aircraft flies to a target and back, is the fuel consumed on the outbound leg calculated using the fuel efficiency of the bomb type being carried, and the fuel consumed on the return leg calculated using the empty-aircraft efficiency of 4 km per liter?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Does the 100-liter takeoff-and-landing fuel cost apply once per round trip (i.e., once per bombing run to a target), regardless of how many bombs are carried on that run?

## Turn 4 - User Simulator

Yes, the 100-liter takeoff-and-landing fuel cost applies once per round trip, regardless of how many bombs are carried on that run.

## Turn 5 - Generic Agent

QUESTION: Can a single bombing run to one target carry a mix of heavy and light bombs, or must each run carry only one bomb type (all heavy or all light)?

## Turn 5 - User Simulator

Each run can carry only one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many bombing runs (round trips) the aircraft can make in total, or is the only constraint on runs the 10,000-liter fuel budget?

## Turn 6 - User Simulator

The only constraint on the number of bombing runs is the 10,000-liter fuel budget.

## Turn 7 - Generic Agent

QUESTION: If the aircraft is assigned zero bombs to a particular key part, is that part simply not destroyed (probability of destruction = 0), with no other effect?

## Turn 7 - User Simulator

Yes, if zero bombs are assigned to a key part, its probability of destruction is 0.

## Turn 8 - Generic Agent

QUESTION: Is the fuel consumed by a bombing run to a target equal to (distance × 2) divided by the carried bomb type's efficiency, plus 100 liters for takeoff and landing — that is, for a heavy bomb to part 1: 900/2 + 100 = 550 liters, and for a light bomb to part 1: 900/3 + 100 = 400 liters?

## Turn 8 - User Simulator

No, that is not correct. The fuel consumed on the outbound leg is calculated using the carried bomb type's efficiency, and the fuel consumed on the return leg is calculated using the empty-aircraft efficiency of 4 km per liter.

## Turn 9 - Generic Agent

QUESTION: So for a heavy bomb to part 1, the fuel is 450/2 (outbound) + 450/4 (return) + 100 (takeoff/landing) = 225 + 112.5 + 100 = 437.5 liters, and for a light bomb to part 1 it is 450/3 + 450/4 + 100 = 150 + 112.5 + 100 = 362.5 liters — is that the correct formula?

## Turn 9 - User Simulator

Yes, that is the correct formula.

## Turn 10 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers (i.e., you can only assign whole bombs, and the total heavy bombs across all four parts cannot exceed 28 and total light bombs cannot exceed 12)?

## Turn 10 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers, and the total heavy bombs across all four parts cannot exceed 28 and total light bombs cannot exceed 12.

## Turn 11 - Generic Agent

QUESTION: Is it allowed to leave some of the available bombs unused (i.e., assign fewer than 28 heavy and/or fewer than 12 light bombs in total), as long as the fuel budget is not exceeded?

## Turn 11 - User Simulator

Yes, it is allowed to leave some of the available bombs unused, as long as the fuel budget is not exceeded.

## Turn 12 - Generic Agent

QUESTION: Is the probability that at least two of the four key parts are destroyed computed by summing over all pairs of parts (using the independence of the four parts' destruction events), i.e., the probability that the set of destroyed parts has size at least 2?

## Turn 12 - User Simulator

Yes, the probability that at least two of the four key parts are destroyed is computed by summing over all pairs of parts, using the independence of the four parts' destruction events.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize the probability that at least two of the four key parts are destroyed.

**Decision variables:** For each key part i (i = 1, 2, 3, 4), two non-negative integer variables:
- h_i = number of heavy bombs assigned to part i
- l_i = number of light bombs assigned to part i

**Destruction probability per part:** For part i, the probability of destruction is:
p_i = 1 − (1 − p_heavy_i)^(h_i) × (1 − p_light_i)^(l_i)

where p_heavy_i and p_light_i are the per-bomb destruction probabilities from the table. If h_i = l_i = 0, then p_i = 0.

**Objective function:** The probability that at least two parts are destroyed, computed by summing over all pairs (and higher-order terms) using independence of the four parts' destruction events:
P(at least 2 destroyed) = Σ_{i<j} p_i p_j (1−p_k)(1−p_l) + Σ_{i<j<k} p_i p_j p_k (1−p_l) + p_1 p_2 p_3 p_4
(summed over all combinations of 2, 3, and 4 parts).

**Constraints:**
1. Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
2. Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
3. Total fuel ≤ 10,000 liters, where fuel for each bomb assigned to part i is:
   - Heavy bomb to part i: d_i/2 + d_i/4 + 100 (outbound at 2 km/L, return at 4 km/L, plus 100 L takeoff/landing)
   - Light bomb to part i: d_i/3 + d_i/4 + 100 (outbound at 3 km/L, return at 4 km/L, plus 100 L takeoff/landing)
   
   Distances: d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600 km.

4. Each bombing run carries exactly one bomb (one heavy or one light) to one target.
5. Bombs may be left unused (constraints are ≤, not =).
6. All variables are non-negative integers.