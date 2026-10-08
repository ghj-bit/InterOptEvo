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

QUESTION: When the aircraft carries a bomb to a target and drops it, does it return to the airport empty (using the 4 km/liter empty efficiency on the way back), or does it return still carrying the bomb (using the bomb's efficiency for the whole round trip)?

## Turn 1 - User Simulator

It returns to the airport empty. The aircraft carries the bomb out to the target, drops it, and then flies back with no bomb, so the return leg uses the empty efficiency of 4 km per liter.

## Turn 2 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel charge applied once per round trip (i.e., once per bomb dropped), or is it charged separately for the takeoff and for the landing?

## Turn 2 - User Simulator

It is applied once per round trip, meaning once per bomb dropped.

## Turn 3 - Generic Agent

QUESTION: Is the mission objective to minimize total fuel consumption subject to the constraint that at least two of the four key parts are destroyed, or is it to maximize the probability that at least two parts are destroyed subject to the fuel and bomb limits?

## Turn 3 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed, subject to the fuel and bomb limits.

## Turn 4 - Generic Agent

QUESTION: For a key part that receives multiple bombs, is the probability that it is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability), assuming independent attempts?

## Turn 4 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: When a key part receives multiple bombs, is the probability that it is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability), assuming independent attempts?

## Turn 5 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run to a target at distance d computed as (d divided by the outbound efficiency) plus (d divided by 4) plus 100 liters, where the outbound efficiency is 2 km/liter for a heavy bomb or 3 km/liter for a light bomb?

## Turn 6 - User Simulator

Yes.

## Turn 7 - Generic Agent

QUESTION: Can the aircraft carry multiple bombs on a single trip to a target, or does each trip carry exactly one bomb to exactly one target?

## Turn 7 - User Simulator

Each trip carries exactly one bomb to exactly one target.

## Turn 8 - Generic Agent

QUESTION: Are the destruction probabilities for each bomb independent of each other, so that a part hit by multiple bombs has a destruction probability of 1 minus the product of (1 minus each bomb's probability)?

## Turn 8 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: If a key part is hit by both a heavy bomb and a light bomb, do their destruction probabilities combine as 1 minus (1 minus the heavy probability) times (1 minus the light probability), treating the two bombs as independent attempts?

## Turn 9 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the numbers 28 heavy bombs and 12 light bombs hard upper limits on how many can be used, or are they the exact total quantities that must all be deployed?

## Turn 10 - User Simulator

They are hard upper limits on how many can be used.

## Turn 11 - Generic Agent

QUESTION: If a key part is hit by two bombs, is the probability that the part is destroyed equal to 1 minus (1 minus the first bomb's probability) times (1 minus the second bomb's probability), treating the two hits as independent?

## Turn 11 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: When computing the probability that a key part is destroyed after being hit by several bombs, should I treat each bomb's hit as an independent attempt and combine them as 1 minus the product of (1 minus each bomb's probability)?

## Turn 12 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is the "at least two of the four key parts are destroyed" success condition evaluated using the expected (probabilistic) destruction of each part, meaning the mission's success probability is the probability that at least two parts are actually destroyed given the bomb allocation?

## Turn 13 - User Simulator

Yes.

## Turn 14 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 14 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 15 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 16 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 17 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 18 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 19 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 20 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 21 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 22 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 23 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 24 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 25 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 26 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 27 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 28 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 29 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), treating each bomb as an independent attempt?

## Turn 30 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.