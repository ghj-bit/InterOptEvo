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

The objective is to maximize the probability that at least two of the four key parts are destroyed. It is not a guarantee of certainty.

## Turn 2 - Generic Agent

QUESTION: When calculating the probability that a specific key part is destroyed, do you assume that the destruction events from individual bombs are independent, meaning the probability of the part surviving all assigned bombs is the product of the survival probabilities for each bomb?

## Turn 2 - User Simulator

Yes, the destruction events from individual bombs are assumed to be independent.

## Turn 3 - Generic Agent

QUESTION: When calculating the fuel consumption for a bombing run to a specific target, do you assume the aircraft carries the same type of bomb for the entire round trip (outbound and return), or does the fuel efficiency change on the return leg because the bomb is no longer being carried?

## Turn 3 - User Simulator

The fuel efficiency changes on the return leg because the bomb is no longer being carried.

## Turn 4 - Generic Agent

QUESTION: When calculating the fuel consumption for the outbound leg of a bombing run, do you assume the aircraft carries the bomb for the entire distance from the airport to the target, or is there a specific drop-off point where the bomb is released and the aircraft becomes empty for the remainder of the outbound leg?

## Turn 4 - User Simulator

The aircraft carries the bomb for the entire distance from the airport to the target.

## Turn 5 - Generic Agent

QUESTION: Does the 100-liter takeoff and landing fuel consumption apply to each individual bomb drop (i.e., one takeoff and one landing per bomb), or does it apply to the entire mission as a single takeoff and landing event regardless of how many bombs are dropped?

## Turn 5 - User Simulator

The 100-liter takeoff and landing fuel consumption applies to each individual bomb drop, meaning one takeoff and one landing per bomb.

## Turn 6 - Generic Agent

QUESTION: When calculating the fuel consumption for the return leg of a bombing run, do you assume the aircraft is empty (not carrying any bomb) for the entire distance from the target back to the airport?

## Turn 6 - User Simulator

Yes, the aircraft is empty for the entire distance from the target back to the airport.

## Turn 7 - Generic Agent

QUESTION: Can the aircraft carry both heavy and light bombs simultaneously on a single bombing run, or is each run dedicated to dropping only one type of bomb?

## Turn 7 - User Simulator

Each run is dedicated to dropping only one type of bomb.

## Turn 8 - Generic Agent

QUESTION: Can the aircraft drop multiple bombs of the same type on a single bombing run to the same target, or is each run limited to dropping exactly one bomb?

## Turn 8 - User Simulator

Each run is limited to dropping exactly one bomb.

## Turn 9 - Generic Agent

QUESTION: Can the aircraft visit multiple different targets in a single mission, or is each mission dedicated to a single target?

## Turn 9 - User Simulator

Each mission is dedicated to a single target.

## Turn 10 - Generic Agent

QUESTION: Is the total fuel consumption constraint of 10,000 liters applied to the sum of fuel used across all individual bombing runs in the mission, or is it a per-run limit?

## Turn 10 - User Simulator

The 10,000-liter fuel constraint is applied to the sum of fuel used across all individual bombing runs in the mission.

## Turn 11 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs the total number available for the entire mission, or are they the number available per individual bombing run?

## Turn 11 - User Simulator

The 28 heavy bombs and 12 light bombs are the total number available for the entire mission.

## Turn 12 - Generic Agent

QUESTION: Is the probability of destruction for a key part calculated based on the total number of bombs of each type assigned to that specific part, regardless of which specific runs they were dropped in?

## Turn 12 - User Simulator

Yes, the probability of destruction for a key part is calculated based on the total number of bombs of each type assigned to that specific part.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** The number of heavy bombs ($H_i$) and light bombs ($L_i$) assigned to each of the four key parts ($i=1,2,3,4$).
3.  **Independence:** Destruction events for individual bombs are independent. The probability that part $i$ is destroyed is $1 - (1-p_{H,i})^{H_i}(1-p_{L,i})^{L_i}$, where $p_{H,i}$ and $p_{L,i}$ are the per-bomb destruction probabilities for heavy and light bombs, respectively.
4.  **Bomb Constraints:**
    *   Total heavy bombs used $\le 28$.
    *   Total light bombs used $\le 12$.
    *   $H_i, L_i$ are non-negative integers.
5.  **Fuel Constraints:**
    *   Total fuel consumption across all runs $\le 10,000$ liters.
    *   Each bomb drop corresponds to one round-trip run.
    *   **Outbound Leg:** Aircraft carries the bomb for the full distance $d_i$ to target $i$.
        *   Fuel for heavy bomb run outbound: $d_i / 2$ liters.
        *   Fuel for light bomb run outbound: $d_i / 3$ liters.
    *   **Return Leg:** Aircraft is empty for the full distance $d_i$ back to airport.
        *   Fuel for return leg (both types): $d_i / 4$ liters.
    *   **Takeoff/Landing:** 100 liters per run (applies to both heavy and light bomb runs).
    *   **Total Fuel per Heavy Bomb to Target $i$:** $d_i/2 + d_i/4 + 100 = 0.75 d_i + 100$.
    *   **Total Fuel per Light Bomb to Target $i$:** $d_i/3 + d_i/4 + 100 = (7/12) d_i + 100$.
6.  **Target Distances:**
    *   Part 1: 450 km
    *   Part 2: 480 km
    *   Part 3: 540 km
    *   Part 4: 600 km
7.  **Destruction Probabilities:**
    *   Part 1: Heavy 0.03, Light 0.08
    *   Part 2: Heavy 0.10, Light 0.11
    *   Part 3: Heavy 0.05, Light 0.12
    *   Part 4: Heavy 0.05, Light 0.09
8.  **Mission Structure:** Each run drops exactly one bomb at one target. The mission consists of a series of such runs. The total fuel is the sum of fuel for all runs.