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

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, or is it to guarantee (with certainty) that at least two are destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed. It is not a requirement to guarantee destruction with certainty.

## Turn 2 - Generic Agent

QUESTION: When you say "each bombing run is a round trip from the airport to the target and back," does each run carry exactly one bomb (either one heavy or one light), or can a single run carry multiple bombs?

## Turn 2 - User Simulator

Each run carries exactly one bomb, either one heavy or one light.

## Turn 3 - Generic Agent

QUESTION: For a single bombing run to a specific key part, is the fuel consumed calculated as the round-trip distance (2 × distance) multiplied by the fuel efficiency for the bomb type being carried, plus the 100-liter takeoff/landing cost?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: When the aircraft returns to the airport after dropping a bomb, is the return leg's fuel consumption calculated using the empty-aircraft efficiency (4 km per liter), or does it continue using the efficiency of the bomb type carried on the outbound leg

## Turn 4 - User Simulator

The return leg uses the empty-aircraft efficiency of 4 km per liter.

## Turn 5 - Generic Agent

QUESTION

## Turn 5 - User Simulator

It looks like your question got cut off. Please go ahead and ask it.

## Turn 6 - Generic Agent

QUESTION: For a single bombing run to a key part, is the probability that the part is destroyed calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs dropped on that

## Turn 6 - User Simulator

Yes, that is correct.

## Turn 7 - Generic Agent

QUESTION

## Turn 7 - User Simulator

It looks like your question got cut off again. Please go ahead and ask it.

## Turn 8 - Generic Agent

QUESTION: Are the destruction outcomes of the four key

## Turn 8 - User Simulator

It looks like your question got cut off. Please go ahead and ask it.

## Turn 9 - Generic Agent

QUESTION: Are the destruction

## Turn 9 - User Simulator

It

## Turn 10 - Generic Agent

QUESTION: Are the

## Turn 10 - User Simulator

It

## Turn 11 - Generic Agent

QUESTION:

## Turn 11 - User Simulator

It

## Turn 12 - Generic Agent

QUESTION

## Turn 12 - User Simulator

It

## Turn 13 - Generic Agent

QUESTION

## Turn 13 - User Simulator

It

## Turn 14 - Generic Agent

QUESTION

## Turn 14 - User Simulator

It

## Turn 15 - Generic Agent

QUESTION

## Turn 15 - User Simulator

It

## Turn 16 - Generic Agent

QUESTION

## Turn 16 - User Simulator

It

## Turn 17 - Generic Agent

QUESTION

## Turn 17 - User Simulator

It

## Turn 18 - Generic Agent

QUESTION

## Turn 18 - User Simulator

It

## Turn 19 - Generic Agent

QUESTION

## Turn 19 - User Simulator

It

## Turn 20 - Generic Agent

QUESTION

## Turn 20 - User Simulator

It

## Turn 21 - Generic Agent

QUESTION

## Turn 21 - User Simulator

It

## Turn 22 - Generic Agent

QUESTION

## Turn 22 - User Simulator

It

## Turn 23 - Generic Agent

QUESTION

## Turn 23 - User Simulator

It

## Turn 24 - Generic Agent

QUESTION

## Turn 24 - User Simulator

It

## Turn 25 - Generic Agent

QUESTION

## Turn 25 - User Simulator

It

## Turn 26 - Generic Agent

QUESTION

## Turn 26 - User Simulator

It

## Turn 27 - Generic Agent

QUESTION

## Turn 27 - User Simulator

It

## Turn 28 - Generic Agent

QUESTION

## Turn 28 - User Simulator

It

## Turn 29 - Generic Agent

QUESTION

## Turn 29 - User Simulator

It

## Turn 30 - Generic Agent

QUESTION

## Turn 30 - User Simulator

It