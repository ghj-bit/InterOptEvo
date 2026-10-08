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

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed (with the bomb allocation chosen to achieve that), or is it to minimize the total fuel consumed subject to the requirement that the probability of destroying at least two parts is at least some target level?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed, with the bomb allocation chosen to achieve that.

## Turn 2 - Generic Agent

QUESTION: For the fuel calculation, is the fuel consumed on the outbound leg (airport to target) based on the efficiency of the bomb being carried, and the fuel on the return leg (target back to airport) based on the empty-aircraft efficiency of 4 km per liter?

## Turn 2 - User Simulator

Yes, that is correct. The outbound leg fuel is based on the efficiency of the bomb being carried, and the return leg fuel is based on the empty-aircraft efficiency of 4 km per liter.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop that single bomb and return empty, meaning each bombing run uses exactly one bomb (either one heavy or one light) and the fuel for that run is (distance / bomb-efficiency) + (distance / 4) + 100 liters?

## Turn 3 - User Simulator

Yes, that is correct. Each bombing run uses exactly one bomb, the aircraft drops it and returns empty, and the fuel for that run is (distance / bomb-efficiency) + (distance / 4) + 100 liters.

## Turn 4 - Generic Agent

QUESTION: For the probability of destroying a key part, if multiple bombs are dropped on the same part, is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability), i.e., assuming independent attempts?

## Turn 4 - User Simulator

Yes, that is correct. The probability that a key part is destroyed is computed as 1 minus the product of (1 minus each bomb's individual destruction probability), assuming independent attempts.

## Turn 5 - Generic Agent

QUESTION: Are the destruction events of the four key parts independent of each other, so that the probability of at least two parts being destroyed is computed by combining the individual part-destruction probabilities assuming independence across parts?

## Turn 5 - User Simulator

Yes, the destruction events of the four key parts are independent of each other.

## Turn 6 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs allocated to each part required to be non-negative integers (you can only drop whole bombs), and is it allowed to drop zero bombs on a given part?

## Turn 6 - User Simulator

Yes, the numbers of heavy and light bombs allocated to each part must be non-negative integers, and it is allowed to drop zero bombs on a given part.

## Turn 7 - Generic Agent

QUESTION: Is it acceptable for the total number of bombs actually dropped to be less than the available 28 heavy and 12 light (i.e., the 28 and 12 are upper bounds, not requirements to use all of them)?

## Turn 7 - User Simulator

Yes, the 28 heavy and 12 light bombs are upper bounds, not requirements to use all of them.

## Turn 8 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound on the sum of fuel across all bombing runs (so the total fuel of all runs combined must not exceed 10,000), rather than a per-run limit?

## Turn 8 - User Simulator

Yes, the 10,000-liter fuel limit is a hard upper bound on the sum of fuel across all bombing runs.

## Turn 9 - Generic Agent

QUESTION: Is there any requirement that the aircraft must return to the airport after each run (so every run is a complete round trip as described), or could a run end without returning?

## Turn 9 - User Simulator

Yes, every run is a complete round trip from the airport to the target and back.

## Turn 10 - Generic Agent

QUESTION: Is there any additional constraint on the total number of bombing runs (e.g., a maximum number of sorties), or is the only limit on the number of runs the fuel and bomb availability?

## Turn 10 - User Simulator

There is no additional constraint on the total number of bombing runs. The only limits are the fuel and bomb availability.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize the probability that at least two of the four key parts are destroyed.

**Decision variables:** For each key part i (i = 1, 2, 3, 4), two non-negative integer variables:
- h_i = number of heavy bombs dropped on part i
- l_i = number of light bombs dropped on part i

**Part destruction probabilities (independent attempts within a part):**
- p_i = 1 − (1 − p_h_i)^(h_i) × (1 − p_l_i)^(l_i), where p_h_i and p_l_i are the per-bomb destruction probabilities for part i.
- Part 1: p_h = 0.03, p_l = 0.08
- Part 2: p_h = 0.10, p_l = 0.11
- Part 3: p_h = 0.05, p_l = 0.12
- Part 4: p_h = 0.05, p_l = 0.09

**Objective value:** The four parts are destroyed independently. The probability that at least two parts are destroyed is computed by summing over all subsets of parts of size ≥ 2 the product of the destruction probabilities of the parts in the subset and the survival probabilities of the parts not in the subset.

**Constraints:**
1. Heavy bomb availability: h_1 + h_2 + h_3 + h_4 ≤ 28
2. Light bomb availability: l_1 + l_2 + l_3 + l_4 ≤ 12
3. Fuel: The total fuel across all runs ≤ 10,000 liters. Each run to part i carrying a heavy bomb consumes (d_i / 2) + (d_i / 4) + 100 liters; each run carrying a light bomb consumes (d_i / 3) + (d_i / 4) + 100 liters. Distances: d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600 km.
   - Fuel per heavy-bomb run to part i: d_i/2 + d_i/4 + 100
   - Fuel per light-bomb run to part i: d_i/3 + d_i/4 + 100
   - Total fuel = Σ_i [h_i × (d_i/2 + d_i/4 + 100) + l_i × (d_i/3 + d_i/4 + 100)] ≤ 10,000
4. All variables are non-negative integers.
5. No other constraints (no minimum or maximum number of runs; bombs are upper bounds, not requirements to use all).