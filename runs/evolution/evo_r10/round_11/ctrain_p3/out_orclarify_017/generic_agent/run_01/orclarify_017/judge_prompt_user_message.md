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

QUESTION: Is the mission's success criterion "at least two of the four key parts are destroyed" a hard requirement that the plan must guarantee (i.e., the model must ensure at least two parts are destroyed with certainty), or is it a probabilistic objective where we maximize the probability that at least two parts are destroyed?

## Turn 1 - User Simulator

It is a probabilistic objective. We want to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: For the probability that a key part is destroyed, should I compute it as 1 minus the product of (1 minus the per-bomb probability) over all bombs of each type dropped on that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is the correct approach.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop that single bomb on one key part and then return empty, meaning each bombing run uses exactly one bomb and the fuel for the outbound leg is computed at the loaded efficiency while the return leg is at the empty efficiency?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: For a bombing run to a key part at distance D, is the fuel consumed equal to (D divided by the loaded efficiency) plus (D divided by the empty efficiency) plus 100 liters for the takeoff and landing?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft drop multiple bombs on the same key part during the mission, and is there any limit on how many bombs can be assigned to a single key part?

## Turn 5 - User Simulator

Yes, the aircraft can drop multiple bombs on the same key part. There is no limit on how many bombs can be assigned to a single key part, other than the total available bombs and fuel constraints.

## Turn 6 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers?

## Turn 6 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 7 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost incurred once per bombing run (i.e., once per bomb dropped), or once per mission regardless of how many runs are made?

## Turn 7 - User Simulator

It is incurred once per bombing run, meaning once per bomb dropped.

## Turn 8 - Generic Agent

QUESTION: If the aircraft is assigned zero bombs to a key part, is that key part's probability of destruction simply zero?

## Turn 8 - User Simulator

Yes, if zero bombs are assigned to a key part, its probability of destruction is zero.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as a minimum number of bombs that must be used, a requirement to use all available bombs, or any other operational restrictions?

## Turn 9 - User Simulator

No, there are no other constraints or considerations. You do not need to use all available bombs, and there is no minimum number of bombs that must be used.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
- **Decision variables:** For each key part i (i = 1, 2, 3, 4), let h_i = number of heavy bombs and l_i = number of light bombs assigned to part i. All are non-negative integers.
- **Probability model:** The probability that part i is destroyed is p_i = 1 − (1 − p_hi)^{h_i} · (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs on part i respectively. If h_i = l_i = 0, then p_i = 0.
- **Success probability:** The probability that at least two of the four parts are destroyed is computed from the individual p_i values assuming independence across parts.
- **Bomb constraints:**
  - Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
  - Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
- **Fuel constraint:** Total fuel ≤ 10,000 liters. Each bombing run to part i at distance D_i consumes:
  - Outbound (loaded): D_i / (2 if heavy, 3 if light) liters
  - Return (empty): D_i / 4 liters
  - Takeoff/landing: 100 liters
  - Total per run: D_i / (loaded efficiency) + D_i / 4 + 100
  - Total fuel = sum over all bombs of the per-run fuel cost.
- **Distances:** Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.
- **Per-bomb destruction probabilities:**
  - Part 1: heavy 0.03, light 0.08
  - Part 2: heavy 0.10, light 0.11
  - Part 3: heavy 0.05, light 0.12
  - Part 4: heavy 0.05, light 0.09
- **No other constraints:** No minimum bomb usage, no requirement to use all bombs, no per-part limits beyond global bomb and fuel limits.