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

QUESTION: Is the mission's success criterion that at least two of the four key parts are destroyed (i.e., the mission is a binary success/failure based on that count), or is the objective to maximize the probability that at least two parts are destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: When the aircraft flies to a target and back, is the fuel efficiency for the entire round trip determined by the heaviest bomb carried on that trip (so a trip carrying both a heavy and a light bomb uses the heavy-bomb rate of 2 km/liter for the whole round trip), or is the fuel computed separately for each bomb's portion of the flight?

## Turn 2 - User Simulator

Each aircraft can only carry one bomb per trip.

## Turn 3 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel charge applied once per round trip (i.e., one 100-liter charge for the whole out-and-back trip), or is it charged separately for the takeoff and for the landing (i.e., 200 liters per round trip)?

## Turn 3 - User Simulator

The 100-liter charge is applied once per round trip.

## Turn 4 - Generic Agent

QUESTION: For a given key part, if you drop multiple bombs on it, is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent per-bomb attempts — or is there some other way the probabilities combine?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: When the aircraft flies to a target and back, is the fuel efficiency for the entire round trip determined by the bomb carried on that trip (so a trip carrying a heavy bomb uses 2 km/liter for the whole round trip, and a trip carrying a light bomb uses 3 km/liter for the whole round trip), or is the fuel computed separately for the outbound and return legs?

## Turn 5 - User Simulator

The fuel efficiency for the entire round trip is determined by the bomb carried on that trip. A trip carrying a heavy bomb uses 2 km/liter for the whole round trip, and a trip carrying a light bomb uses 3 km/liter for the whole round trip.

## Turn 6 - Generic Agent

QUESTION: Can the aircraft make multiple trips to the same key part (dropping one bomb per trip), or is each key part visited at most once during the mission?

## Turn 6 - User Simulator

The aircraft can make multiple trips to the same key part, dropping one bomb per trip.

## Turn 7 - Generic Agent

QUESTION: Is the probability that a key part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent per-bomb attempts — or is there some other way the probabilities combine?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the destruction probabilities for the four key parts independent of each other (i.e., the destruction of one part does not affect the probability of destroying another part)?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the total number of bombs dropped (heavy plus light) constrained by the 28 heavy and 12 light availability limits only, or is there also a limit on the total number of trips the aircraft can make?

## Turn 9 - User Simulator

The total number of bombs dropped is constrained only by the 28 heavy and 12 light availability limits.

## Turn 10 - Generic Agent

QUESTION: Is the fuel constraint a single shared pool of 10,000 liters for the entire mission (all trips combined), or does each trip have its own separate fuel budget?

## Turn 10 - User Simulator

The fuel constraint is a single shared pool of 10,000 liters for the entire mission.

## Turn 11 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever fly a trip, or does every trip always carry exactly one bomb?

## Turn 11 - User Simulator

Every trip always carries exactly one bomb.

## Turn 12 - Generic Agent

QUESTION: Is the number of heavy bombs dropped on each key part required to be a whole number (integer), or can it be a fractional value?

## Turn 12 - User Simulator

The number of heavy bombs dropped on each key part must be a whole number (integer).

## Turn 13 - Generic Agent

QUESTION: Is the number of light bombs dropped on each key part also required to be a whole number (integer)?

## Turn 13 - User Simulator

Yes, the number of light bombs dropped on each key part must be a whole number (integer).

## Turn 14 - Generic Agent

QUESTION: Is there a maximum number of bombs (heavy plus light combined) that can be dropped on a single key part, or is the only limit the total availability of 28 heavy and 12 light bombs?

## Turn 14 - User Simulator

The only limit is the total availability of 28 heavy and 12 light bombs.

## Turn 15 - Generic Agent

QUESTION: Is the fuel consumption for a trip to a key part calculated as (2 × distance / fuel efficiency) + 100, where distance is the one-way distance from the airport to that key part?

## Turn 15 - User Simulator

Yes, the fuel consumption for a trip to a key part is calculated as (2 × distance / fuel efficiency) + 100, where distance is the one-way distance from the airport to that key part.

## Turn 16 - Generic Agent

QUESTION: Is the probability that a key part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent per-bomb attempts — or is there some other way the probabilities combine?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is the probability that a key part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., independent per-bomb attempts — or is there some other way the probabilities combine?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
- **Decision variables:** For each key part i (i = 1, 2, 3, 4), choose non-negative integers h_i (heavy bombs) and l_i (light bombs) to drop on that part.
- **Bomb availability:** Sum of h_i ≤ 28; sum of l_i ≤ 12.
- **Fuel:** Single shared pool of 10,000 liters. Each trip carries exactly one bomb. Fuel for a trip to part i with a heavy bomb = (2 × d_i / 2) + 100; with a light bomb = (2 × d_i / 3) + 100, where d_i is the one-way distance. Total fuel across all trips ≤ 10,000.
- **Distances:** Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.
- **Destruction probabilities per bomb:** As given in the table (heavy: 0.03, 0.10, 0.05, 0.05; light: 0.08, 0.11, 0.12, 0.09).
- **Deferred (internal confirmation pending):** The exact formula for combining multiple bombs' destruction probabilities on the same part (assumed independent per-bomb attempts: P_destroyed = 1 − ∏(1 − p_j)), and whether the four parts' destruction events are mutually independent.
- **No per-part cap** on the number of bombs; the only limits are total heavy (28) and total light (12) availability.
- **Every trip carries exactly one bomb**; no empty trips.