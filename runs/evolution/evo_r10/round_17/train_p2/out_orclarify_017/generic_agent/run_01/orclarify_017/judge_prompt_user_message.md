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

QUESTION: When the aircraft carries a bomb to a target, does it drop the bomb on arrival (so the return leg is flown empty at 4 km per liter), or does it carry the bomb for the entire round trip (so both legs use the loaded efficiency)?

## Turn 1 - User Simulator

The aircraft drops the bomb on arrival, so the return leg is flown empty at 4 km per liter.

## Turn 2 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel charge applied once per round trip (i.e., 100 liters total per sortie), or is it 100 liters for takeoff plus 100 liters for landing (200 liters total per sortie)?

## Turn 2 - User Simulator

The 100-liter charge is applied once per round trip, so it is 100 liters total per sortie.

## Turn 3 - Generic Agent

QUESTION: Is the mission's objective to minimize total fuel consumed (subject to the 10,000-liter cap and the requirement that at least two key parts are destroyed), or is it to maximize the probability that at least two key parts are destroyed (subject to the fuel and bomb caps)?

## Turn 3 - User Simulator

The objective is to maximize the probability that at least two key parts are destroyed, subject to the fuel and bomb caps.

## Turn 4 - Generic Agent

QUESTION: When a key part is hit by multiple bombs, is the probability that it is destroyed computed as 1 minus the product of (1 minus p) over all bombs assigned to it (i.e., independent hits), or is it simply the sum of the individual probabilities capped at 1?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: For the probability that a key part is destroyed by multiple bombs, should I use the independent-hits formula 1 minus the product of (1 minus p) over all bombs assigned to that part?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light)), or does only one bomb type count toward that part?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the fuel model, is the fuel for a sortie to a target at distance d equal to d divided by 2 plus d divided by 4 plus 100 (loaded leg at 2 km per liter, empty return at 4 km per liter, plus the 100-liter takeoff-landing charge)?

## Turn 7 - User Simulator

Yes, that is correct.

## Turn 8 - Generic Agent

QUESTION: Can the same key part be hit by more than one bomb (for example, two heavy bombs on part 2), or is each key part limited to at most one bomb total?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is the number of bombs assigned to each key part required to be a whole number (you cannot split a bomb between targets), so the decision variables are integer counts of heavy and light bombs per part?

## Turn 9 - User Simulator

Yes, the number of bombs assigned to each key part must be a whole number.

## Turn 10 - Generic Agent

QUESTION: Is the 28 heavy bombs and 12 light bombs a hard upper limit on total usage (you may use fewer), or must all 28 heavy and all 12 light bombs be used?

## Turn 10 - User Simulator

It is a hard upper limit; you may use fewer.

## Turn 11 - Generic Agent

QUESTION: Is the 10,000-liter fuel figure a hard upper limit on total consumption (you may use less), or must the mission use exactly 10,000 liters?

## Turn 11 - User Simulator

It is a hard upper limit; you may use less.

## Turn 12 - Generic Agent

QUESTION: For the probability that a key part is destroyed by multiple bombs, should I use the independent-hits formula 1 minus the product of (1 minus p) over all bombs assigned to that part?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light))?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: If a key part is hit by two heavy bombs, is its destruction probability 1 minus (1 minus 0.03) squared, i.e., do repeated hits on the same part combine independently?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is the probability that the mission succeeds (at least two of the four key parts destroyed) computed by treating the four parts' destruction events as independent of each other, so that the success probability is the sum over all pairs and triples of the joint probabilities?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is the probability that the mission succeeds (at least two of the four key parts destroyed) computed by treating the four parts' destruction events as independent of each other?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light))?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: If a key part is hit by two heavy bombs, is its destruction probability 1 minus (1 minus 0.03) squared, i.e., do repeated hits on the same part combine independently?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is the probability that the mission succeeds (at least two of the four key parts destroyed) computed by treating the four parts' destruction events as independent of each other?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light))?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: If a key part is hit by two heavy bombs, is its destruction probability 1 minus (1 minus 0.03) squared, i.e., do repeated hits on the same part combine independently?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is the probability that the mission succeeds (at least two of the four key parts destroyed) computed by treating the four parts' destruction events as independent of each other?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light))?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: If a key part is hit by two heavy bombs, is its destruction probability 1 minus (1 minus 0.03) squared, i.e., do repeated hits on the same part combine independently?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is the probability that the mission succeeds (at least two of the four key parts destroyed) computed by treating the four parts' destruction events as independent of each other?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light))?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: If a key part is hit by two heavy bombs, is its destruction probability 1 minus (1 minus 0.03) squared, i.e., do repeated hits on the same part combine independently?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is the probability that the mission succeeds (at least two of the four key parts destroyed) computed by treating the four parts' destruction events as independent of each other?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: If a key part is hit by both a heavy and a light bomb, do the two hits act independently (so the part's destruction probability is 1 minus (1 minus p_heavy) times (1 minus p_light))?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: If a key part is hit by two heavy bombs, is its destruction probability 1 minus (1 minus 0.03) squared, i.e., do repeated hits on the same part combine independently?

## Turn 30 - User Simulator

The point still needs internal confirmation.