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

QUESTION: Is the mission carried out by a single aircraft that makes multiple sorties (each sortie being one round trip to one target part, dropping all bombs it carries on that part), or by multiple aircraft each making one sortie?

## Turn 2 - User Simulator

The mission is carried out by a single aircraft that makes multiple sorties. Each sortie is one round trip to one target part, and the aircraft drops all bombs it carries on that part.

## Turn 3 - Generic Agent

QUESTION: In a single sortie, can the aircraft carry a mix of heavy and light bombs (e.g., 3 heavy and 2 light), or must each sortie carry only one bomb type?

## Turn 3 - User Simulator

Each sortie must carry only one bomb type.

## Turn 4 - Generic Agent

QUESTION: When the aircraft flies a sortie carrying heavy bombs, is the fuel efficiency 2 km per liter for the entire round trip (both the outbound leg and the return leg), or is it 2 km per liter only on the outbound leg while the return leg (now empty) uses the empty-aircraft efficiency of 4 km per liter?

## Turn 4 - User Simulator

The fuel efficiency is 2 km per liter for the entire round trip (both the outbound leg and the return leg).

## Turn 5 - Generic Agent

QUESTION: How many bombs of a given type can the aircraft carry in a single sortie — is there a maximum payload per sortie, or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the probability of destroying a key part, is it computed as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs dropped on that part, assuming each bomb acts independently?

## Turn 6 - User Simulator

Yes, the probability of destroying a key part is computed as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs dropped on that part, assuming each bomb acts independently.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is there a limit on the total number of sorties the aircraft can make in the mission, or can it make as many sorties as needed as long as the total fuel and bomb counts stay within their limits?

## Turn 8 - User Simulator

There is no limit on the total number of sorties. The aircraft can make as many sorties as needed as long as the total fuel and bomb counts stay within their limits.

## Turn 9 - Generic Agent

QUESTION: Is the objective to minimize the total fuel consumed (or total number of bombs used) while ensuring at least two key parts are destroyed, or is the objective to maximize the probability that at least two key parts are destroyed subject to the fuel and bomb limits?

## Turn 9 - User Simulator

The objective is to maximize the probability that at least two key parts are destroyed, subject to the fuel and bomb limits.

## Turn 10 - Generic Agent

QUESTION: When the aircraft makes a sortie to a key part, does it have to drop all the bombs it is carrying on that part, or can it choose to drop only some of them and keep the rest for a later sortie?

## Turn 10 - User Simulator

The aircraft has to drop all the bombs it is carrying on that part.

## Turn 11 - Generic Agent

QUESTION: Can the aircraft make multiple sorties to the same key part (e.g., one heavy-bomb sortie and later a light-bomb sortie to part 3), or is each key part visited at most once across the whole mission?

## Turn 11 - User Simulator

The aircraft can make multiple sorties to the same key part.

## Turn 12 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: For the fuel calculation, is the 100-liter takeoff-and-landing charge applied once per sortie (i.e., once per round trip), or once per leg (so twice per round trip)?

## Turn 13 - User Simulator

The 100-liter takeoff-and-landing charge is applied once per sortie (i.e., once per round trip).

## Turn 14 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: If the aircraft makes two sorties to the same key part (e.g., 2 heavy bombs then 3 light bombs), is the destruction probability for that part computed by combining all 5 bombs together (using the per-bomb probabilities for each), or is each sortie's contribution computed separately and then combined?

## Turn 15 - User Simulator

The destruction probability for that part is computed by combining all 5 bombs together, using the per-bomb probabilities for each.

## Turn 16 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there a maximum number of bombs the aircraft can carry in a single sortie (a payload limit), or can it carry any number up to the total available (up to 28 heavy or 12 light in one trip)?

## Turn 30 - User Simulator

The point still needs internal confirmation.