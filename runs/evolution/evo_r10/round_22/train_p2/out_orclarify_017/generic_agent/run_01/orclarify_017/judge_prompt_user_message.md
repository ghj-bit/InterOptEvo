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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits?

## Turn 1 - User Simulator

Yes, that is correct.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb, is the fuel efficiency of 2 km per liter applied to the entire round trip (outbound and return), or only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 2 - User Simulator

The 2 km per liter efficiency applies to the entire round trip when carrying a heavy bomb.

## Turn 3 - Generic Agent

QUESTION: For a bombing run to a given key part, is the fuel consumed equal to (2 × distance / efficiency) + 100 liters, where the 100 liters is the fixed takeoff-and-landing cost per trip?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Are the destruction probabilities for the individual bombs within a single key part independent of each other, so that the probability a part is destroyed after n bombs is 1 minus the product of (1 minus p) over all bombs assigned to it?

## Turn 4 - User Simulator

Yes, the destruction probabilities for individual bombs within a single key part are independent.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft make multiple separate trips to the same key part (dropping one bomb per trip), or must all bombs assigned to a part be dropped in a single trip?

## Turn 5 - User Simulator

The aircraft can make multiple separate trips to the same key part, dropping one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb on the same trip, or is each trip limited to carrying exactly one bomb (either heavy or light)?

## Turn 6 - User Simulator

Each trip is limited to carrying exactly one bomb, either heavy or light.

## Turn 7 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs hard upper limits on the total number used across all trips, meaning the aircraft may use fewer than the full available stock?

## Turn 7 - User Simulator

Yes, the 28 heavy bombs and 12 light bombs are hard upper limits on the total number used across all trips. The aircraft may use fewer than the full available stock.

## Turn 8 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound on total fuel consumed across all trips, with no requirement to use all of it?

## Turn 8 - User Simulator

Yes, the 10,000-liter fuel limit is a hard upper bound on total fuel consumed across all trips, with no requirement to use all of it.

## Turn 9 - Generic Agent

QUESTION: When computing the probability that at least two of the four key parts are destroyed, are the destruction events of the four key parts independent of each other?

## Turn 9 - User Simulator

Yes, the destruction events of the four key parts are independent of each other.

## Turn 10 - Generic Agent

QUESTION: Is the number of bombs assigned to each key part required to be a non-negative integer (i.e., you cannot assign a fractional bomb)?

## Turn 10 - User Simulator

Yes, the number of bombs assigned to each key part must be a non-negative integer.

## Turn 11 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be dropped on each key part, or can a key part receive zero bombs (and thus have zero probability of being destroyed)?

## Turn 11 - User Simulator

A key part can receive zero bombs, and in that case it has zero probability of being destroyed.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on the total number of trips the aircraft can make, or is the only constraint on trips the total fuel consumption not exceeding 10,000 liters?

## Turn 12 - User Simulator

There is no separate limit on the total number of trips. The only constraint on trips is that the total fuel consumption must not exceed 10,000 liters.

## Turn 13 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel cost incurred once per trip regardless of which key part is targeted, or does it vary by target?

## Turn 13 - User Simulator

The 100-liter takeoff-and-landing fuel cost is incurred once per trip regardless of which key part is targeted.

## Turn 14 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever need to fly to a target, or is the empty-aircraft efficiency of 4 km per liter only relevant if there were a return leg without a bomb (which cannot happen since each trip carries exactly one bomb)?

## Turn 14 - User Simulator

The empty-aircraft efficiency of 4 km per liter is not relevant for this mission, since each trip carries exactly one bomb and the bomb-carrying efficiency applies to the entire round trip.

## Turn 15 - Generic Agent

QUESTION: Is the objective to maximize the probability that at least two of the four key parts are destroyed, or is there a secondary objective (such as minimizing fuel used or minimizing the number of bombs used) that should be optimized after maximizing that probability?

## Turn 15 - User Simulator

The objective is solely to maximize the probability that at least two of the four key parts are destroyed. There is no secondary objective.

## Turn 16 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.
- **Decision variables:** For each key part i (i = 1,2,3,4), let h_i = number of heavy bombs assigned (non-negative integer) and l_i = number of light bombs assigned (non-negative integer).
- **Destruction probability per part:** Part i is destroyed with probability 1 − ∏_{j=1}^{h_i}(1 − p_h(i)) × ∏_{j=1}^{l_i}(1 − p_l(i)), where p_h(i) and p_l(i) are the per-bomb destruction probabilities from the table. If h_i = l_i = 0, the probability is 0.
- **Independence:** Destruction events across the four parts are independent; within a part, individual bomb effects are independent.
- **Success probability:** P(at least 2 of 4 parts destroyed) = sum over all subsets S of {1,2,3,4} with |S| ≥ 2 of [∏_{i∈S} q_i × ∏_{j∉S}(1 − q_j)], where q_i is the destruction probability of part i.
- **Bomb constraints:**
  - ∑ h_i ≤ 28
  - ∑ l_i ≤ 12
- **Fuel constraint:** Each trip to part i carrying a heavy bomb consumes (2 × d_i / 2) + 100 = d_i + 100 liters. Each trip to part i carrying a light bomb consumes (2 × d_i / 3) + 100 liters. Total fuel ≤ 10,000 liters.
  - Part 1 (d=450): heavy trip = 550 L, light trip = 400 L
  - Part 2 (d=480): heavy trip = 580 L, light trip = 420 L
  - Part 3 (d=540): heavy trip = 640 L, light trip = 460 L
  - Part 4 (d=600): heavy trip = 700 L, light trip = 500 L
- **No other constraints:** No minimum bombs per part, no limit on number of trips, no secondary objective.