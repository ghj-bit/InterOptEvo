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

QUESTION: When the aircraft carries a bomb, does it drop that bomb on the target and then return to the airport empty (so the outbound leg uses the loaded efficiency and the return leg uses the empty efficiency), or does it keep the bomb for the whole round trip?

## Turn 1 - User Simulator

The aircraft drops the bomb on the target and returns to the airport empty. So the outbound leg uses the loaded efficiency and the return leg uses the empty efficiency.

## Turn 2 - Generic Agent

QUESTION: For a bombing run that drops a heavy bomb, is the fuel for the round trip calculated as (distance out / 2 km per liter) + (distance back / 4 km per liter) + 100 liters for takeoff and landing, and similarly for a light bomb run using 3 km per liter outbound?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, or is there a different objective such as minimizing fuel or bomb usage subject to a minimum success probability?

## Turn 3 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 4 - Generic Agent

QUESTION: For each key part, is the probability that it is destroyed computed as 1 minus (1 minus the per-bomb probability) raised to the number of bombs dropped on that part, assuming each bomb's effect is independent?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: Can the number of heavy bombs and light bombs assigned to each key part be any non-negative integer, with no minimum or maximum per part other than the overall limits of 28 heavy and 12 light?

## Turn 5 - User Simulator

Yes, the number of heavy and light bombs assigned to each key part can be any non-negative integer, with no minimum or maximum per part other than the overall limits of 28 heavy and 12 light.

## Turn 6 - Generic Agent

QUESTION: Do the 28 heavy and 12 light bombs represent the total available for the whole mission (so unused bombs are simply left behind), or must all of them be used?

## Turn 6 - User Simulator

They represent the total available for the whole mission. Unused bombs are simply left behind.

## Turn 7 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard ceiling that must not be exceeded, with unused fuel simply left over?

## Turn 7 - User Simulator

Yes, the 10,000-liter fuel limit is a hard ceiling that must not be exceeded, with unused fuel simply left over.

## Turn 8 - Generic Agent

QUESTION: Does the 100-liter takeoff-and-landing fuel cost apply once per round trip (i.e., once per bomb dropped), regardless of bomb type?

## Turn 8 - User Simulator

Yes, the 100-liter takeoff-and-landing fuel cost applies once per round trip, regardless of bomb type.

## Turn 9 - Generic Agent

QUESTION: When computing the probability that at least two of the four key parts are destroyed, are the destruction events of the different key parts treated as independent of each other?

## Turn 9 - User Simulator

Yes, the destruction events of the different key parts are treated as independent of each other.

## Turn 10 - Generic Agent

QUESTION: Is the distance for each key part a one-way distance from the airport, so the round trip covers twice that distance (out and back)?

## Turn 10 - User Simulator

Yes, the distance for each key part is a one-way distance from the airport, so the round trip covers twice that distance.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how many times the aircraft can fly to the same key part (i.e., can it make multiple separate round trips to the same part, one bomb per trip)?

## Turn 11 - User Simulator

No, there is no limit on how many times the aircraft can fly to the same key part. It can make multiple separate round trips to the same part, one bomb per trip.

## Turn 12 - Generic Agent

QUESTION: Is the fuel efficiency for the outbound leg determined solely by the type of bomb being carried (2 km/L for heavy, 3 km/L for light), with no other factors affecting it?

## Turn 12 - User Simulator

Yes, the fuel efficiency for the outbound leg is determined solely by the type of bomb being carried: 2 km/L for heavy and 3 km/L for light.

## Turn 13 - Generic Agent

QUESTION: Is the fuel efficiency for the return leg always 4 km/L (empty), regardless of which key part was just bombed?

## Turn 13 - User Simulator

Yes, the fuel efficiency for the return leg is always 4 km/L (empty), regardless of which key part was just bombed.

## Turn 14 - Generic Agent

QUESTION: Are there any other constraints or considerations I should know about, such as a maximum number of total bombing runs, a minimum number of bombs per key part, or any other business rules?

## Turn 14 - User Simulator

No, there are no other constraints or considerations beyond what has already been discussed.

## Turn 15 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.
- **Decision variables:** For each key part i (i = 1, 2, 3, 4), let h_i = number of heavy bombs and l_i = number of light bombs assigned to part i. All are non-negative integers.
- **Destruction probability per part:** p_i = 1 − (1 − p_hi)^{h_i} · (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for part i.
- **Independence:** Destruction events across parts are independent, so the probability that at least 2 parts are destroyed is computed from the joint distribution of the four independent Bernoulli variables with probabilities p_1, p_2, p_3, p_4.
- **Bomb limits:** Σ h_i ≤ 28, Σ l_i ≤ 12. Unused bombs are left behind.
- **Fuel model per round trip to part i:**
  - Outbound (loaded): distance_i / efficiency_loaded (2 km/L for heavy, 3 km/L for light)
  - Return (empty): distance_i / 4 km/L
  - Takeoff + landing: 100 L
  - Total fuel for one heavy-bomb run to part i: 450/2 + 450/4 + 100 = 225 + 112.5 + 100 = 437.5 L (for part 1; analogous for others)
  - Total fuel for one light-bomb run to part i: distance_i/3 + distance_i/4 + 100
- **Fuel limit:** Total fuel across all runs ≤ 10,000 L. Unused fuel is left over.
- **No other constraints:** No per-part minimums, no cap on number of runs to a single part, no other business rules.