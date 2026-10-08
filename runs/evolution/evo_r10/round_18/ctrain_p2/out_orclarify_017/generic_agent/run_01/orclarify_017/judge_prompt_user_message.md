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

QUESTION: For each key part, is the destruction probability per bomb independent across bombs (so that dropping multiple bombs on the same part compounds the destruction probability), and is the mission objective to maximize the probability that at least two of the four parts are destroyed?

## Turn 1 - User Simulator

Yes, the destruction probability per bomb is independent across bombs, so dropping multiple bombs on the same part compounds the destruction probability. And yes, the mission objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as the sum of fuel for the outbound leg (carrying the bomb), the return leg (empty), plus the 100-liter takeoff/landing cost?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: Can a single aircraft carry both a heavy bomb and a light bomb on the same trip, or does each trip carry exactly one bomb (either heavy or light)?

## Turn 3 - User Simulator

Each trip carries exactly one bomb, either heavy or light.

## Turn 4 - Generic Agent

QUESTION: Can the same key part be bombed multiple times (i.e., can multiple bombs be dropped on the same part across different trips)?

## Turn 4 - User Simulator

Yes, the same key part can be bombed multiple times.

## Turn 5 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used (28 and 12) hard upper bounds that we may use fewer of, or must we use exactly all 28 heavy and all 12 light bombs?

## Turn 5 - User Simulator

They are hard upper bounds; we may use fewer than 28 heavy bombs and fewer than 12 light bombs.

## Turn 6 - Generic Agent

QUESTION: Is the fuel constraint a single shared pool of 10,000 liters across all trips combined, or is it a per-trip limit?

## Turn 6 - User Simulator

It is a single shared pool of 10,000 liters across all trips combined.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total number of trips (sorties) the aircraft can make, or is the only constraint on trips the shared 10,000-liter fuel pool?

## Turn 7 - User Simulator

The only constraint on trips is the shared 10,000-liter fuel pool.

## Turn 8 - Generic Agent

QUESTION: For the fuel calculation, is the distance used for each leg the one-way distance from the airport to the target (so a round trip to part 1 is 450 km out + 450 km back), or is the listed distance already the round-trip distance?

## Turn 8 - User Simulator

The listed distance is the one-way distance from the airport to the target.

## Turn 9 - Generic Agent

QUESTION: When computing the probability that a part is destroyed, is it simply 1 minus the product of (1 minus p) over all bombs dropped on that part, where p is the per-bomb probability for that bomb type?

## Turn 9 - User Simulator

Yes, that is correct.

## Turn 10 - Generic Agent

QUESTION: Is the aircraft's fuel efficiency on the outbound leg determined by the bomb it is carrying (2 km/L for heavy, 3 km/L for light), and on the return leg it is always 4 km/L since it is empty?

## Turn 10 - User Simulator

Yes, that is correct.

## Turn 11 - Generic Agent

QUESTION: Are the numbers of heavy bombs dropped on each part and light bombs dropped on each part required to be non-negative integers?

## Turn 11 - User Simulator

Yes, the numbers of heavy and light bombs dropped on each part must be non-negative integers.

## Turn 12 - Generic Agent

QUESTION: Is the 100-liter takeoff/landing cost incurred once per trip (i.e., once per bomb dropped), regardless of which part is targeted?

## Turn 12 - User Simulator

Yes, the 100-liter takeoff/landing cost is incurred once per trip, regardless of which part is targeted.

## Turn 13 - Generic Agent

QUESTION: Is there any minimum number of parts that must be bombed, or can we choose to bomb only a subset of the four parts (e.g., concentrate all bombs on just two parts)?

## Turn 13 - User Simulator

There is no minimum number of parts that must be bombed. We can choose to bomb only a subset of the four parts.

## Turn 14 - Generic Agent

QUESTION: Is the objective strictly to maximize the probability that at least two of the four parts are destroyed, with no secondary objective (such as minimizing fuel used or number of trips) in case of ties?

## Turn 14 - User Simulator

Yes, the objective is strictly to maximize the probability that at least two of the four parts are destroyed, with no secondary objective.

## Turn 15 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:** For each key part i (i = 1,2,3,4), let h_i = number of heavy bombs dropped on part i, and l_i = number of light bombs dropped on part i. All are non-negative integers.

**Objective:** Maximize the probability that at least 2 of the 4 parts are destroyed.

**Destruction probability per part:** For part i, the probability it is destroyed is:
p_i = 1 − (1 − 0.03·h_i contribution) ... more precisely, p_i = 1 − ∏ over all bombs dropped on part i of (1 − p_bomb), where p_bomb is 0.03/0.05/0.05/0.05 for heavy and 0.08/0.11/0.12/0.09 for light on parts 1–4 respectively. Since bombs of the same type on the same part are independent: p_i = 1 − (1 − p_h_i)^{h_i} · (1 − p_l_i)^{l_i}.

**Probability of mission success (≥2 parts destroyed):** Sum over all subsets S of {1,2,3,4} with |S| ≥ 2 of [∏_{i∈S} p_i · ∏_{j∉S} (1 − p_j)].

**Constraints:**
1. Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
2. Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
3. Total fuel ≤ 10,000 liters, where fuel for a trip to part i carrying a heavy bomb = (d_i / 2) + (d_i / 4) + 100, and fuel for a trip to part i carrying a light bomb = (d_i / 3) + (d_i / 4) + 100, with d_i being the one-way distance (450, 480, 540, 600 km for parts 1–4). Total fuel = Σ_i [h_i · (d_i/2 + d_i/4 + 100) + l_i · (d_i/3 + d_i/4 + 100)].
4. Each trip carries exactly one bomb (already reflected in the per-bomb fuel accounting).
5. No minimum number of parts must be bombed.
6. No secondary objective.