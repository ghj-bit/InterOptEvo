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

QUESTION: For the mission to count as successful, do the two destroyed key parts have to be destroyed by bombs actually dropped on them (i.e., you choose how many heavy and light bombs to drop on each of the four parts), or is there any other way a part could be counted as destroyed?

## Turn 1 - User Simulator

The two destroyed key parts must be destroyed by bombs actually dropped on them. You choose how many heavy and light bombs to drop on each of the four parts, and a part is counted as destroyed based on the probability of destruction from those specific bombs.

## Turn 2 - Generic Agent

QUESTION: When you drop multiple bombs on the same key part, is the probability that the part is destroyed calculated as 1 minus the product of (1 minus each bomb's individual probability), assuming the bombs act independently?

## Turn 2 - User Simulator

Yes, that is correct. The probability that a key part is destroyed is calculated as 1 minus the product of (1 minus each bomb's individual probability), assuming the bombs act independently.

## Turn 3 - Generic Agent

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is it to find any feasible bomb allocation that guarantees (or makes most likely) at least two parts destroyed?

## Turn 3 - User Simulator

The mission's objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 4 - Generic Agent

QUESTION: For fuel consumption, is the fuel used for a bombing run calculated as (distance to target times 2 for the round trip) divided by the fuel efficiency of the bomb being carried, plus the 100 liters for takeoff and landing?

## Turn 4 - User Simulator

Yes, that is correct. The fuel used for a bombing run is calculated as (distance to target times 2 for the round trip) divided by the fuel efficiency of the bomb being carried, plus the 100 liters for takeoff and landing.

## Turn 5 - Generic Agent

QUESTION: When the aircraft flies back to the airport after dropping a bomb, is it considered empty (using 4 km per liter efficiency) for the return leg, or does it still use the efficiency of the bomb it carried on the way out for the entire round trip?

## Turn 5 - User Simulator

The aircraft uses the efficiency of the bomb it carried on the way out for the entire round trip.

## Turn 6 - Generic Agent

QUESTION: Can the aircraft make multiple separate trips to the same target (e.g., fly to target 1, drop a bomb, return, then fly to target 2, drop a bomb, return), or must all bombs be dropped in a single trip?

## Turn 6 - User Simulator

The aircraft can make multiple separate trips to the same target. Each bombing run is a separate round trip from the airport to the target and back.

## Turn 7 - Generic Agent

QUESTION: Is there a limit on the number of separate trips the aircraft can make, or is the only constraint on trips the total fuel available (10,000 liters)?

## Turn 7 - User Simulator

The only constraint on trips is the total fuel available (10,000 liters).

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs dropped on each target required to be non-negative integers (you can't drop half a bomb), or can they be treated as continuous values in the optimization?

## Turn 8 - User Simulator

The numbers of heavy and light bombs dropped on each target must be non-negative integers.

## Turn 9 - Generic Agent

QUESTION: Is the 28 heavy bombs and 12 light bombs the total available for the entire mission (across all targets), or is that the maximum that can be carried on a single trip?

## Turn 9 - User Simulator

The 28 heavy bombs and 12 light bombs are the total available for the entire mission across all targets.

## Turn 10 - Generic Agent

QUESTION: Can the aircraft carry both heavy and light bombs on the same trip, or must each trip carry only one type of bomb?

## Turn 10 - User Simulator

Each trip can carry only one bomb.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint on the order in which the aircraft visits the four targets, or can it visit them in any order it chooses?

## Turn 11 - User Simulator

There is no constraint on the order in which the aircraft visits the four targets. It can visit them in any order it chooses.

## Turn 12 - Generic Agent

QUESTION: If the aircraft drops a bomb on a target and that target is not destroyed, can the aircraft make another trip to the same target to drop more bombs on it?

## Turn 12 - User Simulator

Yes, the aircraft can make another trip to the same target to drop more bombs on it.

## Turn 13 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated based on all bombs dropped on that part across all trips, or is it calculated per trip and then combined somehow?

## Turn 13 - User Simulator

The probability of destroying a key part is calculated based on all bombs dropped on that part across all trips.

## Turn 14 - Generic Agent

QUESTION: When calculating the probability that at least two of the four key parts are destroyed, do we assume the destruction events for different key parts are independent of each other?

## Turn 14 - User Simulator

Yes, the destruction events for different key parts are assumed to be independent of each other.

## Turn 15 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision Variables:**
- For each of the 4 key parts (targets), choose non-negative integers: the number of heavy bombs and the number of light bombs to drop on that part.

**Objective:**
- Maximize the probability that at least 2 of the 4 key parts are destroyed.

**Probability Model:**
- For each key part, the probability of destruction is 1 minus the product of (1 minus each bomb's individual probability), assuming independence among bombs on the same part.
- The destruction events across different key parts are independent.
- The overall success probability is computed by summing over all combinations of at least 2 parts being destroyed.

**Constraints:**
1. Total heavy bombs used across all 4 parts ≤ 28.
2. Total light bombs used across all 4 parts ≤ 12.
3. Total fuel consumption ≤ 10,000 liters.

**Fuel Model:**
- Each bomb dropped requires one separate round-trip flight.
- For a heavy bomb dropped on a target at distance d km: fuel = (2d / 2) + 100 = d + 100 liters.
- For a light bomb dropped on a target at distance d km: fuel = (2d / 3) + 100 liters.
- The aircraft uses the efficiency of the bomb carried for the entire round trip.
- Each trip carries exactly one bomb.
- There is no limit on the number of trips other than the fuel constraint.

**Target Data:**
| Part | Distance (km) | P(destruction | heavy) | P(destruction | light) |
|------|--------------|--------------------------|--------------------------|
| 1    | 450          | 0.03                     | 0.08                     |
| 2    | 480          | 0.10                     | 0.11                     |
| 3    | 540          | 0.05                     | 0.12                     |
| 4    | 600          | 0.05                     | 0.09                     |

**Key Structural Notes:**
- The problem is a mixed-integer nonlinear optimization (integer variables with a nonlinear probability objective).
- The order of visiting targets does not matter.
- Multiple trips to the same target are allowed.
- All bombs are allocated across the 4 targets; unused bombs are simply not deployed.