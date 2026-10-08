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

QUESTION: When the aircraft carries a bomb to a target, does it drop the bomb on arrival (so the return leg is flown empty at 4 km/L), or does it carry the bomb for the entire round trip (so both legs use the bomb's fuel efficiency)?

## Turn 1 - User Simulator

The aircraft drops the bomb on arrival, so the return leg is flown empty at 4 km per liter.

## Turn 2 - Generic Agent

QUESTION: The mission is successful if at least two of the four key parts are destroyed — is the objective to minimize total fuel used (or total bombs used) subject to the constraint that at least two parts are destroyed, or is the objective to maximize the probability that at least two parts are destroyed subject to the fuel and bomb limits?

## Turn 2 - User Simulator

The objective is to maximize the probability that at least two parts are destroyed, subject to the fuel and bomb limits.

## Turn 3 - Generic Agent

QUESTION: For a given key part, if you drop multiple bombs on it, is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent trials — or is there some other rule (for example, only the first bomb counts, or probabilities are simply added and capped at 1)?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: When the aircraft flies to a target carrying a bomb, does it carry exactly one bomb per trip (one bomb dropped per round trip), or can it carry multiple bombs on a single trip and drop them all at the target?

## Turn 4 - User Simulator

The aircraft carries exactly one bomb per trip.

## Turn 5 - Generic Agent

QUESTION: For a given key part, if you drop multiple bombs on it, is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent trials — or is there some other rule (for example, only the first bomb counts, or probabilities are simply added and capped at 1)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: The 100-liter takeoff-and-landing charge is per round trip (one takeoff plus one landing), correct — so a single round trip to a target costs 100 liters for takeoff/landing plus the fuel for the outbound leg (carrying the bomb) and the return leg (empty)?

## Turn 6 - User Simulator

Yes, that is correct.

## Turn 7 - Generic Agent

QUESTION: If the aircraft makes multiple trips to the same key part (dropping one bomb per trip), is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent trials — or is there some other rule (for example, only the first bomb counts, or probabilities are simply added and capped at 1)?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs hard upper bounds on how many may be used (i.e., you may use fewer, and any unused bombs simply stay on the ground), or must all of them be used?

## Turn 8 - User Simulator

They are hard upper bounds. You may use fewer, and any unused bombs simply stay on the ground.

## Turn 9 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound on total fuel consumed across all trips (you may use less), or must the aircraft use exactly 10,000 liters?

## Turn 9 - User Simulator

It is a hard upper bound. You may use less, and any unused fuel simply remains.

## Turn 10 - Generic Agent

QUESTION: When the aircraft flies to a target carrying a bomb, is the fuel for the outbound leg computed as (distance divided by the bomb's fuel efficiency) — for example, 450 km carrying a heavy bomb at 2 km/L uses 225 liters — and the return leg as (distance divided by 4 km/L), plus the 100-liter takeoff/landing charge, for a total of 225 + 112.5 + 100 = 437.5 liters for that trip?

## Turn 10 - User Simulator

Yes, that calculation is correct.

## Turn 11 - Generic Agent

QUESTION: If the aircraft makes multiple trips to the same key part (dropping one bomb per trip), is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent trials — or is there some other rule (for example, only the first bomb counts, or probabilities are simply added and capped at 1)?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Since the destruction-probability rule for multiple bombs on the same part is still pending internal confirmation, may I proceed with the standard independent-trials assumption — that the probability a part is destroyed equals 1 minus the product of (1 minus each dropped bomb's individual probability) — and flag it clearly in the final model so it can be swapped if the confirmed rule differs?

## Turn 12 - User Simulator

Yes, you may proceed with the standard independent-trials assumption and flag it clearly in the final model.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed, subject to all resource limits.

**Decision variables:** For each key part i (i = 1..4), choose how many heavy bombs h_i and light bombs l_i to drop on it (non-negative integers). Each bomb dropped corresponds to exactly one round trip (one bomb per trip).

**Destruction probability (flagged assumption — pending internal confirmation):** Independent trials. Probability part i is destroyed = 1 − ∏(1 − p), where p runs over the individual destruction probabilities of all bombs dropped on part i (heavy: 0.03/0.10/0.05/0.05 for parts 1–4; light: 0.08/0.11/0.12/0.09 for parts 1–4).

**Objective value:** Sum over all subsets S of parts with |S| ≥ 2 of [∏_{i∈S} P_i · ∏_{j∉S} (1 − P_j)], where P_i is the destruction probability of part i.

**Fuel per trip:** Outbound leg = distance / bomb efficiency (heavy: 2 km/L, light: 3 km/L); return leg = distance / 4 km/L (empty); plus 100 L takeoff/landing per round trip. Example confirmed: part 1 with a heavy bomb = 450/2 + 450/4 + 100 = 437.5 L.

**Constraints:**
- Total heavy bombs used ≤ 28 (hard upper bound; unused bombs stay on the ground).
- Total light bombs used ≤ 12 (hard upper bound; unused bombs stay on the ground).
- Total fuel consumed across all trips ≤ 10,000 L (hard upper bound; unused fuel remains).

**Distances (km):** Part 1 = 450, Part 2 = 480, Part 3 = 540, Part 4 = 600.