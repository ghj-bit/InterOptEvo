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

QUESTION: When you say the mission is successful only if at least two of the four key parts are destroyed, do you mean the objective is to maximize the probability that at least two parts are destroyed (with the bomb allocation chosen to make that probability as high as possible), or is there a different objective such as maximizing the expected number of parts destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: For the fuel calculation, is the fuel consumed on the outbound leg (airport to target) determined by the bomb the aircraft is carrying at that moment, and the fuel on the return leg (target back to airport) determined by whether the bomb was dropped — i.e., if the aircraft carries a heavy bomb out and drops it, it returns empty at 4 km per liter, or is the entire round trip charged at the efficiency of the bomb carried for that run?

## Turn 2 - User Simulator

The fuel on the outbound leg is determined by the bomb carried, and the fuel on the return leg is determined by whether the bomb was dropped. If the aircraft carries a heavy bomb out and drops it, it returns empty at 4 km per liter.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target and drops it, is the bomb always dropped (i.e., every bomb carried to a target is used on that target), or can the aircraft carry a bomb to a target and choose not to drop it, returning with the bomb still on board?

## Turn 3 - User Simulator

Every bomb carried to a target is dropped on that target.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft make multiple bombing runs to the same key part (dropping more than one bomb on a single part across separate trips), or is each key part visited at most once with at most one bomb dropped on it?

## Turn 4 - User Simulator

The aircraft can make multiple bombing runs to the same key part, dropping more than one bomb on a single part across separate trips.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb on the same trip (dropping one or both on the same or different targets in a single sortie), or does each trip carry exactly one bomb?

## Turn 5 - User Simulator

Each trip carries exactly one bomb.

## Turn 6 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb to a target and drops it, the return leg is empty at 4 km per liter — but does the 100-liter takeoff-and-landing charge apply once per trip (covering both the takeoff and the landing), or is it 100 liters for takeoff plus 100 liters for landing (200 liters total per trip)?

## Turn 6 - User Simulator

The 100-liter charge applies once per trip, covering both the takeoff and the landing.

## Turn 7 - Generic Agent

QUESTION: The probability of destruction per bomb (e.g., 0.03 for a heavy bomb on part 1) — when multiple bombs are dropped on the same part, is the probability that the part is destroyed calculated as 1 minus the product of (1 minus p) for each bomb dropped on it, assuming independent destruction attempts?

## Turn 7 - User Simulator

Yes, the probability that the part is destroyed is calculated as 1 minus the product of (1 minus p) for each bomb dropped on it, assuming independent destruction attempts.

## Turn 8 - Generic Agent

QUESTION: Are the destruction outcomes of the four key parts independent of each other (so the probability that at least two are destroyed is computed from the individual part destruction probabilities assuming independence across parts)?

## Turn 8 - User Simulator

Yes, the destruction outcomes of the four key parts are independent of each other.

## Turn 9 - Generic Agent

QUESTION: Is the fuel constraint a hard limit (the total fuel consumed across all trips must not exceed 10,000 liters, and the mission is infeasible if it would exceed that), or is there a penalty for exceeding it?

## Turn 9 - User Simulator

The fuel constraint is a hard limit. The total fuel consumed across all trips must not exceed 10,000 liters, and the mission is infeasible if it would exceed that.

## Turn 10 - Generic Agent

QUESTION: Are the heavy bomb limit (28) and light bomb limit (12) hard upper bounds on the total number of bombs that can be dropped across all trips, meaning you can use at most 28 heavy bombs and at most 12 light bombs in total?

## Turn 10 - User Simulator

Yes, the heavy bomb limit (28) and light bomb limit (12) are hard upper bounds on the total number of bombs that can be dropped across all trips.

## Turn 11 - Generic Agent

QUESTION: Is there a minimum number of bombs that must be dropped, or can the aircraft choose to drop zero bombs (i.e., is it allowed to use fewer than all available bombs)?

## Turn 11 - User Simulator

There is no minimum number of bombs that must be dropped. The aircraft can choose to use fewer than all available bombs.

## Turn 12 - Generic Agent

QUESTION: When the aircraft carries a light bomb to a target and drops it, the return leg is empty at 4 km per liter — is this the same rule as for heavy bombs (return empty at 4 km per liter regardless of bomb type)?

## Turn 12 - User Simulator

Yes, the return leg is empty at 4 km per liter regardless of bomb type.

## Turn 13 - Generic Agent

QUESTION: Is the distance from the airport to each target a one-way distance, so the round trip distance for a target at 450 km is 900 km total (450 km out + 450 km back)?

## Turn 13 - User Simulator

Yes, the distance from the airport to each target is a one-way distance, so the round trip distance for a target at 450 km is 900 km total.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.

**Decision variables:** For each key part i (i = 1, 2, 3, 4), decide how many heavy bombs (h_i) and how many light bombs (l_i) to drop on it. All are non-negative integers.

**Part destruction probabilities:**
- Part i is destroyed with probability 1 − (1 − p_hi)^{h_i} × (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs on part i.
- Destruction outcomes across parts are independent.

**Constraints:**
1. Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
2. Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
3. Total fuel ≤ 10,000 liters (hard limit)

**Fuel per trip:**
- Each trip carries exactly one bomb to one target and drops it.
- Outbound leg: distance d_i at efficiency depending on bomb type (heavy: 2 km/L, light: 3 km/L).
- Return leg: distance d_i at 4 km/L (empty).
- Takeoff + landing: 100 liters per trip.
- Fuel for one heavy-bomb trip to part i: d_i/2 + d_i/4 + 100
- Fuel for one light-bomb trip to part i: d_i/3 + d_i/4 + 100

**Distances (one-way):** Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.

**Per-bomb destruction probabilities:**
| Part | Heavy (p_hi) | Light (p_li) |
|------|-------------|-------------|
| 1    | 0.03        | 0.08        |
| 2    | 0.10        | 0.11        |
| 3    | 0.05        | 0.12        |
| 4    | 0.05        | 0.09        |

**Success condition:** At least 2 of the 4 parts destroyed (probability computed from independent part destruction probabilities).

**No minimum bomb usage** — the aircraft may use fewer than all available bombs.