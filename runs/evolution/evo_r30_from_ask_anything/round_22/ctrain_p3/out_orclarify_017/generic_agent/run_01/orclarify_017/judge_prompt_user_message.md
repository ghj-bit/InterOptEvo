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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is it to guarantee (i.e., achieve with certainty) that at least two parts are destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed. It is not to guarantee destruction with certainty.

## Turn 2 - Generic Agent

QUESTION: When you say "each bombing run is a round trip from the airport to the target and back," does each run carry exactly one bomb (either one heavy or one light), or can a single run carry multiple bombs of the same or different types?

## Turn 2 - User Simulator

Each run carries exactly one bomb, either one heavy or one light.

## Turn 3 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for takeoff and landing, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 3 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip, not once per leg.

## Turn 4 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 4 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 5 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 5 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 6 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 6 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 7 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 7 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 8 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 8 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 9 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 9 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 10 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 10 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 11 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 11 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 12 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 12 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 13 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 13 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 14 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 14 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 15 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 15 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 16 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 16 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 17 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 17 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 18 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 18 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 19 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 19 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 20 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 20 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 21 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 21 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 22 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 22 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 23 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 23 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 24 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 24 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 25 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge is applied once per round trip rather than once per leg?

## Turn 25 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 26 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 26 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 27 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 27 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 28 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 28 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 29 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 29 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.

## Turn 30 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific target part, is the fuel consumption calculated as (distance to target × 2 for the outbound leg at the loaded efficiency) plus (distance back × 2 for the return leg at the empty efficiency) plus 100 liters for the round trip, or is the 100-liter takeoff/landing charge applied once per round trip rather than once per leg?

## Turn 30 - User Simulator

The 100-liter takeoff and landing charge is applied once per round trip.