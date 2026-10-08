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

QUESTION: When you say the mission is successful only if at least two of the four key parts are destroyed, do you want the model to maximize the probability of achieving that outcome, or is there a different objective (e.g., minimize fuel or bombs used subject to a required success probability)?

## Turn 1 - User Simulator

We want to maximize the probability of mission success, which means destroying at least two of the four key parts.

## Turn 2 - Generic Agent

QUESTION: For each key part, is the destruction probability from multiple bombs calculated as 1 minus (1 minus p) to the power of the number of bombs, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: When the aircraft flies to a target carrying a bomb, does it drop the bomb on arrival and then return to the airport empty, or does it carry the bomb for the entire round trip?

## Turn 3 - User Simulator

The aircraft drops the bomb on arrival and returns to the airport empty.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft carry both a heavy and a light bomb on the same trip, or is each trip limited to carrying exactly one bomb (either heavy or light)?

## Turn 4 - User Simulator

Each trip is limited to carrying exactly one bomb, either heavy or light.

## Turn 5 - Generic Agent

QUESTION: Does the 100-liter takeoff-and-landing fuel cost apply once per round trip (i.e., one takeoff plus one landing), or is it charged separately for the takeoff and for the landing?

## Turn 5 - User Simulator

The 100-liter cost applies once per round trip, covering one takeoff and one landing combined.

## Turn 6 - Generic Agent

QUESTION: Can the aircraft make multiple trips to the same key part (dropping one bomb per trip), or is each key part visited at most once?

## Turn 6 - User Simulator

The aircraft can make multiple trips to the same key part, dropping one bomb per trip.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used required to be integers (i.e., you can only use whole bombs), or can they be treated as continuous quantities in the model?

## Turn 7 - User Simulator

The numbers of heavy and light bombs used must be integers.

## Turn 8 - Generic Agent

QUESTION: The brief says heavy bombs "cannot exceed 28" and light bombs "cannot exceed 12" — do you want the model to be allowed to use fewer than all available bombs (i.e., these are upper bounds, not requirements to use them all)?

## Turn 8 - User Simulator

Yes, these are upper bounds. The model is allowed to use fewer than all available bombs.

## Turn 9 - Generic Agent

QUESTION: For the fuel constraint, is the 10,000-liter limit a hard cap on total fuel consumed across all trips, or is it the amount of fuel the aircraft can carry per trip (requiring refueling between trips)?

## Turn 9 - User Simulator

The 10,000-liter limit is a hard cap on total fuel consumed across all trips.

## Turn 10 - Generic Agent

QUESTION: When computing the probability that a key part is destroyed, do you assume the destruction events from different bombs on the same part are independent of each other?

## Turn 10 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are the destruction outcomes of different key parts independent of each other (i.e., destroying part 1 does not affect the probability of destroying part 2)?

## Turn 11 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: For the fuel calculation on a trip to a key part at distance D km, is the fuel consumed equal to (D divided by the outbound fuel efficiency) plus (D divided by the return fuel efficiency) plus 100 liters?

## Turn 12 - User Simulator

Yes, the fuel consumed for a trip to a key part at distance D km is equal to (D divided by the outbound fuel efficiency) plus (D divided by the return fuel efficiency) plus 100 liters.

## Turn 13 - Generic Agent

QUESTION: If the model decides not to drop any bomb on a particular key part, is that part's destruction probability simply zero (i.e., it cannot be destroyed by any other means)?

## Turn 13 - User Simulator

Yes, if no bomb is dropped on a particular key part, its destruction probability is zero.

## Turn 14 - Generic Agent

QUESTION: Is there any limit on the total number of trips the aircraft can make, or is the only constraint on trips the total fuel cap of 10,000 liters?

## Turn 14 - User Simulator

The only constraint on trips is the total fuel cap of 10,000 liters.

## Turn 15 - Generic Agent

QUESTION: Since the independence assumptions (both within a part and across parts) are still pending internal confirmation, would you like me to proceed with the standard assumption that all bomb effects are mutually independent, or should I wait for that confirmation before finalizing the model?

## Turn 15 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 16 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.
- **Decision variables:** For each key part i (i = 1,2,3,4), let h_i = number of heavy bombs dropped on part i (integer ≥ 0) and l_i = number of light bombs dropped on part i (integer ≥ 0).
- **Bomb constraints:**
  - Σ h_i ≤ 28 (heavy bombs)
  - Σ l_i ≤ 12 (light bombs)
- **Trip structure:** Each bomb dropped requires one round trip. The aircraft carries exactly one bomb outbound (at the corresponding fuel efficiency), drops it, and returns empty (at 4 km/L).
- **Fuel per trip to part i:** (D_i / efficiency_out) + (D_i / 4) + 100, where efficiency_out is 2 km/L for heavy and 3 km/L for light.
  - Heavy trip to part i: D_i/2 + D_i/4 + 100
  - Light trip to part i: D_i/3 + D_i/4 + 100
- **Fuel constraint:** Total fuel across all trips ≤ 10,000 liters.
- **Destruction probability per part:** P_i = 1 − (1 − p_hi)^{h_i} × (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for part i. (Independence of bomb effects within a part is assumed as the standard model; this is pending internal confirmation.)
- **Mission success probability:** P(success) = P(at least 2 of the 4 parts are destroyed), computed from the individual part destruction probabilities. (Independence across parts is assumed; this is also pending internal confirmation.)
- **No bomb on a part → destruction probability = 0.**
- **No limit on number of trips** beyond the fuel cap.
- **Bombs are integers; upper bounds are not requirements to use all.**