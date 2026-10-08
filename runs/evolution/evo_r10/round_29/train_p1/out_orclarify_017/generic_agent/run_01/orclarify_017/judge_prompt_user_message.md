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

QUESTION: For the mission to count as successful, do the two destroyed key parts have to be destroyed by the same aircraft in a single sortie, or is it enough that across the whole mission (possibly multiple sorties) at least two of the four parts end up destroyed?

## Turn 1 - User Simulator

It is enough that across the whole mission, at least two of the four key parts end up destroyed. They do not have to be destroyed by the same aircraft in a single sortie.

## Turn 2 - Generic Agent

QUESTION: When an aircraft carries a bomb to a target, does it drop that bomb on exactly one key part and then return empty, or can it carry multiple bombs in one sortie and drop them on different key parts before returning?

## Turn 2 - User Simulator

The aircraft drops that bomb on exactly one key part and then returns empty. It cannot carry multiple bombs in one sortie.

## Turn 3 - Generic Agent

QUESTION: For a sortie to a key part at distance d, is the fuel consumed equal to (d / 2) liters for the outbound leg carrying the bomb plus (d / 4) liters for the empty return leg, plus the 100-liter takeoff-and-landing charge?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: The destruction probabilities are given per bomb — for example, a heavy bomb on part 1 destroys it with probability 0.03. If multiple bombs are dropped on the same part, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual probability), i.e., independent trials?

## Turn 4 - User Simulator

Yes, the probability that the part is destroyed is equal to 1 minus the product of (1 minus each bomb's individual probability).

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits?

## Turn 5 - User Simulator

Yes, the objective is to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits.

## Turn 6 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs hard upper bounds that may be left unused, or must all available bombs be dropped?

## Turn 6 - User Simulator

They are hard upper bounds that may be left unused.

## Turn 7 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a single shared pool for the whole mission (all sorties combined), rather than a per-sortie or per-aircraft limit?

## Turn 7 - User Simulator

Yes, the 10,000-liter fuel limit is a single shared pool for the whole mission.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on the number of sorties (aircraft trips) that can be made, or is the only constraint on sorties the shared 10,000-liter fuel pool?

## Turn 8 - User Simulator

The only constraint on sorties is the shared 10,000-liter fuel pool.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how many bombs can be dropped on a single key part, or can any number of bombs be concentrated on one part as long as the total bomb and fuel limits are respected?

## Turn 9 - User Simulator

There is no limit on how many bombs can be dropped on a single key part, as long as the total bomb and fuel limits are respected.

## Turn 10 - Generic Agent

QUESTION: When computing the probability that at least two parts are destroyed, are the destruction events of the four key parts treated as independent of each other?

## Turn 10 - User Simulator

Yes, the destruction events of the four key parts are treated as independent of each other.

## Turn 11 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing charge applied once per sortie (i.e., once per round trip to a target), not once per leg?

## Turn 11 - User Simulator

Yes, the 100-liter takeoff-and-landing charge is applied once per sortie.

## Turn 12 - Generic Agent

QUESTION: Since each sortie carries exactly one bomb and drops it on exactly one key part, is the decision simply how many heavy bombs and how many light bombs to assign to each of the four parts (with the fuel cost determined by those assignments), or is there any additional decision such as choosing which aircraft or sortie order?

## Turn 12 - User Simulator

The decision is simply how many heavy bombs and how many light bombs to assign to each of the four parts. There is no additional decision such as choosing which aircraft or sortie order.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize the probability that at least 2 of the 4 key parts are destroyed.
- **Decision variables:** For each key part i (i = 1..4), choose non-negative integers h_i (heavy bombs) and l_i (light bombs) to drop on it.
- **Success rule:** Mission succeeds if at least 2 of the 4 parts are destroyed (across the whole mission, not per sortie).
- **Destruction probability per part:** Part i is destroyed with probability 1 − (1 − 0.03·indicator... ) — specifically, 1 − ∏ over all bombs on part i of (1 − p), where p = 0.03/0.10/0.05/0.05 for heavy and 0.08/0.11/0.12/0.09 for light, per part. Multiple bombs on the same part are independent trials.
- **Independence:** Destruction events across the four parts are independent.
- **Bomb limits (hard upper bounds, may be unused):** Σ_i h_i ≤ 28, Σ_i l_i ≤ 12.
- **Fuel:** Single shared pool of 10,000 L for the whole mission. Each sortie carries exactly one bomb, drops it on one part, and returns empty. Fuel per sortie to part i at distance d_i:
  - Heavy bomb: d_i/2 (outbound) + d_i/4 (return) + 100 L
  - Light bomb: d_i/3 (outbound) + d_i/4 (return) + 100 L
  - Total fuel = Σ_i [ h_i·(d_i/2 + d_i/4 + 100) + l_i·(d_i/3 + d_i/4 + 100) ] ≤ 10,000.
- **No limit** on sorties beyond the fuel pool; no limit on bombs per part; no per-sortie or per-aircraft fuel limit; no sortie-order or aircraft-choice decision.
- **Distances:** d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600 km.

I will now formulate and solve the model.