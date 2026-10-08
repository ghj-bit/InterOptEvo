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

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, or is it to guarantee (with certainty) that at least two parts are destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed. It is not a guarantee of certainty.

## Turn 2 - Generic Agent

QUESTION: For a given key part, if I assign multiple bombs to it, is the probability that the part is destroyed calculated as 1 minus the product of (1 minus the per-bomb probability) for each bomb assigned to that part?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: When the aircraft flies to a target and back, does it carry the bomb on the outbound leg and return empty on the inbound leg, so that fuel for one bombing run to a part at distance d is (d / 2) + (d / 4) + 100 liters?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Can a single aircraft carry both a heavy bomb and a light bomb on the same trip, or does each trip carry exactly one bomb (either heavy or light)?

## Turn 4 - User Simulator

Each trip carries exactly one bomb, either heavy or light.

## Turn 5 - Generic Agent

QUESTION: Can the same key part be bombed multiple times (i.e., receive more than one bomb across multiple trips), or is each key part bombed at most once?

## Turn 5 - User Simulator

A key part can be bombed multiple times.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many times a single key part can be bombed, other than the overall limits on total heavy bombs (28), total light bombs (12), and total fuel (10,000 liters)?

## Turn 6 - User Simulator

No, there is no specific limit on how many times a single key part can be bombed, other than the overall limits on total heavy bombs, total light bombs, and total fuel.

## Turn 7 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs the total available for the entire mission (i.e., the sum of heavy bombs used across all trips cannot exceed 28, and the sum of light bombs used across all trips cannot exceed 12)?

## Turn 7 - User Simulator

Yes, the 28 heavy bombs and 12 light bombs are the total available for the entire mission.

## Turn 8 - Generic Agent

QUESTION: Is the probability that each key part is destroyed independent of the destruction probabilities of the other key parts?

## Turn 8 - User Simulator

Yes, the probability that each key part is destroyed is independent of the destruction probabilities of the other key parts.

## Turn 9 - Generic Agent

QUESTION: Is the fuel consumption for the takeoff and landing (100 liters per trip) a fixed cost per trip regardless of which target is being bombed, or does it vary by target?

## Turn 9 - User Simulator

It is a fixed cost of 100 liters per trip, regardless of which target is being bombed.

## Turn 10 - Generic Agent

QUESTION: Is the fuel efficiency (2 km/liter for heavy, 3 km/liter for light, 4 km/liter for empty) applied to the total distance flown, or is it applied per leg (outbound and inbound separately)?

## Turn 10 - User Simulator

It is applied per leg (outbound and inbound separately).

## Turn 11 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing cost incurred once per trip (i.e., once per round trip to a target), or is it incurred twice per trip (once for takeoff and once for landing)?

## Turn 11 - User Simulator

It is incurred once per trip (once per round trip to a target).

## Turn 12 - Generic Agent

QUESTION: Is the fuel consumption for the outbound leg calculated as distance divided by the fuel efficiency of the bomb being carried (e.g., 450 km / 2 km/liter = 225 liters for a heavy bomb to part 1), and the inbound leg as distance divided by 4 km/liter (e.g., 450 km / 4 km/liter = 112.5 liters), plus the 100-liter takeoff/landing cost?

## Turn 12 - User Simulator

Yes, that is correct.

## Turn 13 - Generic Agent

QUESTION: Is the probability of destruction for a key part calculated using only the bombs assigned to that specific part, or do bombs assigned to other parts also contribute to the destruction probability of that part?

## Turn 13 - User Simulator

The probability of destruction for a key part is calculated using only the bombs assigned to that specific part.

## Turn 14 - Generic Agent

QUESTION: Is the total fuel consumption the sum of fuel used across all trips, and must this sum not exceed 10,000 liters?

## Turn 14 - User Simulator

Yes, the total fuel consumption is the sum of fuel used across all trips, and this sum must not exceed 10,000 liters.

## Turn 15 - Generic Agent

QUESTION: Is the number of trips (bombing runs) unlimited, as long as the total heavy bombs used do not exceed 28, total light bombs used do not exceed 12, and total fuel does not exceed 10,000 liters?

## Turn 15 - User Simulator

Yes, the number of trips is unlimited, as long as the total heavy bombs used do not exceed 28, total light bombs used do not exceed 12, and total fuel does not exceed 10,000 liters.

## Turn 16 - Generic Agent

QUESTION: Is the probability that at least two of the four key parts are destroyed calculated as 1 minus the probability that zero or one parts are destroyed, where the probability that a specific part is destroyed depends only on the bombs assigned to that part?

## Turn 16 - User Simulator

Yes, that is correct.

## Turn 17 - Generic Agent

QUESTION: Is the decision variable for each key part the number of heavy bombs and the number of light bombs assigned to that part, with the constraint that the total heavy bombs across all parts do not exceed 28 and the total light bombs across all parts do not exceed 12?

## Turn 17 - User Simulator

Yes, that is correct.

## Turn 18 - Generic Agent

QUESTION: Is the fuel consumption for a trip to a specific key part determined solely by the distance to that part and the type of bomb carried, independent of how many bombs are assigned to that part?

## Turn 18 - User Simulator

Yes, the fuel consumption for a trip to a specific key part is determined solely by the distance to that part and the type of bomb carried, independent of how many bombs are assigned to that part.

## Turn 19 - Generic Agent

QUESTION: Is the total fuel consumption calculated as the sum over all trips, where each trip's fuel is determined by the distance to the target and the type of bomb carried on that trip?

## Turn 19 - User Simulator

Yes, that is correct.

## Turn 20 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs of that type assigned to that part, summed over both heavy and light bombs?

## Turn 20 - User Simulator

No, that is not quite right. The probability that a key part is destroyed is calculated as 1 minus the product of (1 minus the per-bomb probability) for each individual bomb assigned to that part, regardless of whether the bomb is heavy or light.

## Turn 21 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus the product over all bombs assigned to that part of (1 minus the per-bomb probability for that specific bomb type), where the per-bomb probability depends on whether the bomb is heavy or light?

## Turn 21 - User Simulator

Yes, that is correct.

## Turn 22 - Generic Agent

QUESTION: Is the total fuel consumption calculated as the sum over all key parts of (number of heavy bombs assigned to that part times the fuel per heavy bomb trip to that part) plus (number of light bombs assigned to that part times the fuel per light bomb trip to that part)?

## Turn 22 - User Simulator

Yes, that is correct.

## Turn 23 - Generic Agent

QUESTION: Is the fuel per heavy bomb trip to a key part at distance d calculated as (d / 2) + (d / 4) + 100 liters, and the fuel per light bomb trip to a key part at distance d calculated as (d / 3) + (d / 4) + 100 liters?

## Turn 23 - User Simulator

Yes, that is correct.

## Turn 24 - Generic Agent

QUESTION: Is the objective to maximize the probability that at least two of the four key parts are destroyed, where this probability is calculated as 1 minus the probability that zero parts are destroyed minus the probability that exactly one part is destroyed?

## Turn 24 - User Simulator

Yes, that is correct.

## Turn 25 - Generic Agent

QUESTION: Is the probability that zero parts are destroyed calculated as the product over all four parts of (1 minus the probability that that part is destroyed)?

## Turn 25 - User Simulator

Yes, that is correct.

## Turn 26 - Generic Agent

QUESTION: Is the probability that exactly one part is destroyed calculated as the sum over all four parts of (the probability that that specific part is destroyed times the product over the other three parts of (1 minus the probability that those parts are destroyed))?

## Turn 26 - User Simulator

Yes, that is correct.

## Turn 27 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus the product over all bombs assigned to that part of (1 minus the per-bomb probability for that bomb type), where the per-bomb probability for a heavy bomb to part i is given in the table and the per-bomb probability for a light bomb to part i is also given in the table?

## Turn 27 - User Simulator

Yes, that is correct.

## Turn 28 - Generic Agent

QUESTION: Is the total number of heavy bombs used across all four key parts constrained to be less than or equal to 28, and the total number of light bombs used across all four key parts constrained to be less than or equal to 12?

## Turn 28 - User Simulator

Yes, that is correct.

## Turn 29 - Generic Agent

QUESTION: Is the total fuel consumption constrained to be less than or equal to 10,000 liters, where the total fuel consumption is the sum over all four key parts of (number of heavy bombs assigned to that part times the fuel per heavy bomb trip to that part) plus (number of light bombs assigned to that part times the fuel per light bomb trip to that part)?

## Turn 29 - User Simulator

Yes, that is correct.

## Turn 30 - Generic Agent

QUESTION: Are the number of heavy bombs and light bombs assigned to each key part required to be non-negative integers?

## Turn 30 - User Simulator

Yes, the number of heavy bombs and light bombs assigned to each key part must be non-negative integers.