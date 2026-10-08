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

QUESTION: For each key part, is the destruction probability per bomb independent across bombs (so that dropping multiple bombs on the same part multiplies their survival probabilities), and does a part count as "destroyed" if it is hit by at least one bomb that succeeds?

## Turn 1 - User Simulator

Yes. The destruction probability per bomb is independent across bombs, so dropping multiple bombs on the same part multiplies their survival probabilities. A part counts as "destroyed" if it is hit by at least one bomb that succeeds.

## Turn 2 - Generic Agent

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits?

## Turn 2 - User Simulator

Yes, the mission objective is to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits.

## Turn 3 - Generic Agent

QUESTION: When the aircraft flies a bombing run to a target, does it carry all of its bombs for that run and drop them all at that target, or can it carry a mix of heavy and light bombs on a single run?

## Turn 3 - User Simulator

The aircraft can carry only one bomb per trip.

## Turn 4 - Generic Agent

QUESTION: On a trip to a target, the aircraft flies out carrying the bomb and returns empty. So the fuel for one trip to a target at distance d is: (d / efficiency_with_bomb) + (d / 4) + 100, where efficiency_with_bomb is 2 for heavy and 3 for light. Is that the correct fuel calculation per trip?

## Turn 4 - User Simulator

Yes, that is the correct fuel calculation per trip.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft make multiple trips to the same target (dropping one bomb per trip), or is each target visited at most once?

## Turn 5 - User Simulator

The aircraft can make multiple trips to the same target, dropping one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used (up to 28 and 12 respectively) and the total fuel (up to 10,000 liters) hard upper bounds that must not be exceeded, with no requirement to use all of them?

## Turn 6 - User Simulator

Yes, the numbers of heavy and light bombs used (up to 28 and 12 respectively) and the total fuel (up to 10,000 liters) are hard upper bounds that must not be exceeded, with no requirement to use all of them.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total number of trips the aircraft can make, or is the only constraint on trips the total fuel budget of 10,000 liters?

## Turn 7 - User Simulator

The only constraint on trips is the total fuel budget of 10,000 liters.

## Turn 8 - Generic Agent

QUESTION: Can the aircraft carry a heavy bomb on one trip and a light bomb on another trip to the same target, i.e., can both bomb types be used against the same key part?

## Turn 8 - User Simulator

Yes, both bomb types can be used against the same key part.

## Turn 9 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be dropped, or can the aircraft choose to drop zero bombs on a given key part (leaving it untouched)?

## Turn 9 - User Simulator

There is no minimum number of bombs that must be dropped. The aircraft can choose to drop zero bombs on a given key part.

## Turn 10 - Generic Agent

QUESTION: Is the probability of destroying a key part computed as 1 minus the product of the survival probabilities of all bombs dropped on it, where survival probability for a heavy bomb is (1 - 0.03) for part 1, (1 - 0.10) for part 2, etc., and similarly for light bombs?

## Turn 10 - User Simulator

Yes, the probability of destroying a key part is computed as 1 minus the product of the survival probabilities of all bombs dropped on it.

## Turn 11 - Generic Agent

QUESTION: Is the mission success probability computed as the probability that at least two of the four key parts are destroyed, where each part's destruction is an independent event given the bombs assigned to it?

## Turn 11 - User Simulator

Yes, the mission success probability is computed as the probability that at least two of the four key parts are destroyed, where each part's destruction is an independent event given the bombs assigned to it.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.

- **Decision variables:** For each key part i (i = 1, 2, 3, 4), let h_i = number of heavy bombs dropped on part i, and l_i = number of light bombs dropped on part i. All are non-negative integers.

- **Destruction probability per part:** Part i is destroyed with probability p_i = 1 − ∏(survival of each bomb), where survival of a heavy bomb on part i is (1 − p_heavy_i) and of a light bomb is (1 − p_light_i). Specifically:
  - Part 1: p_heavy = 0.03, p_light = 0.08
  - Part 2: p_heavy = 0.10, p_light = 0.11
  - Part 3: p_heavy = 0.05, p_light = 0.12
  - Part 4: p_heavy = 0.05, p_light = 0.09

- **Mission success probability:** P(at least 2 parts destroyed) = sum over all subsets S of parts with |S| ≥ 2 of [∏_{i∈S} p_i × ∏_{j∉S} (1 − p_j)].

- **Constraints:**
  - Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
  - Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
  - Total fuel ≤ 10,000 liters, where fuel for one trip to part i with a heavy bomb is (d_i / 2) + (d_i / 4) + 100, and with a light bomb is (d_i / 3) + (d_i / 4) + 100. Distances: d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600 km.
  - No minimum bombs per part; zero is allowed.
  - Multiple trips to the same part are allowed; one bomb per trip.
  - Both bomb types can be used on the same part.
  - All bomb and fuel limits are hard upper bounds; no requirement to use all.