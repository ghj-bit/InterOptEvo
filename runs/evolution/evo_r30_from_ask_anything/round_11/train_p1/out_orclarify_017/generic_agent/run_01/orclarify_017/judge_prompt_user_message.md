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

QUESTION: Is the mission's objective to minimize total fuel consumption while ensuring at least two of the four key parts are destroyed, or is it to maximize the probability of destroying at least two key parts subject to the fuel and bomb limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two of the four key parts, subject to the fuel and bomb limits.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb, is the fuel efficiency of 2 km per liter applied to the entire round trip (both the outbound leg to the target and the return leg to the airport), or does the efficiency change depending on whether the bomb is still on board during the return leg?

## Turn 2 - User Simulator

The 2 km per liter efficiency applies to the entire round trip when carrying a heavy bomb.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a light bomb, is the fuel efficiency of 3 km per liter applied to the entire round trip (both the outbound leg to the target and the return leg to the airport), or does the efficiency change depending on whether the bomb is still on board during the return leg?

## Turn 3 - User Simulator

The 3 km per liter efficiency applies to the entire round trip when carrying a light bomb.

## Turn 4 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), is the fuel efficiency of 4 km per liter applied to the entire round trip, or is this efficiency only relevant for a specific leg of the trip?

## Turn 4 - User Simulator

The 4 km per liter efficiency applies to the entire round trip when the aircraft is empty.

## Turn 5 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel consumption a fixed cost per round trip regardless of the distance to the target, or does it vary based on the specific target being bombed?

## Turn 5 - User Simulator

The 100-liter takeoff and landing fuel consumption is a fixed cost per round trip, regardless of the distance to the target.

## Turn 6 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb to a target, is the total fuel consumption for that round trip calculated as (2 * distance / 2) + 100, or is there a different formula that accounts for the distance and efficiency in a different way?

## Turn 6 - User Simulator

The total fuel consumption for that round trip is calculated as (2 * distance / 2) + 100.

## Turn 7 - Generic Agent

QUESTION: When the aircraft carries a light bomb to a target, is the total fuel consumption for that round trip calculated as (2 * distance / 3) + 100, or is there a different formula that accounts for the distance and efficiency in a different way?

## Turn 7 - User Simulator

The total fuel consumption for that round trip is calculated as (2 * distance / 3) + 100.

## Turn 8 - Generic Agent

QUESTION: When the aircraft is empty and makes a round trip, is the total fuel consumption calculated as (2 * distance / 4) + 100, or is there a different formula that accounts for the distance and efficiency in a different way?

## Turn 8 - User Simulator

The total fuel consumption for that round trip is calculated as (2 * distance / 4) + 100.

## Turn 9 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb on the same round trip to a target, or is it limited to carrying only one bomb per trip?

## Turn 9 - User Simulator

The aircraft is limited to carrying only one bomb per trip.

## Turn 10 - Generic Agent

QUESTION: When calculating the probability of destroying a specific key part, are the effects of multiple bombs dropped on that part independent of each other, or is there a different statistical model for how multiple bombs combine to destroy the part?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: If the effects of multiple bombs on a key part are not independent, what specific statistical model or formula should be used to calculate the combined probability of destruction when multiple bombs are dropped on the same part?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are the destruction events for the four different key parts independent of each other, or is there a dependency between the destruction of one part and the destruction of another part?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Can the aircraft make multiple separate round trips to the same key part, dropping one bomb per trip, or is each key part limited to being visited only once during the mission?

## Turn 13 - User Simulator

The aircraft can make multiple separate round trips to the same key part, dropping one bomb per trip.

## Turn 14 - Generic Agent

QUESTION: Is the total fuel consumption constraint of 10,000 liters applied to the sum of fuel used across all round trips made during the mission, or is it applied per individual round trip?

## Turn 14 - User Simulator

The total fuel consumption constraint of 10,000 liters is applied to the sum of fuel used across all round trips made during the mission.

## Turn 15 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used in the mission required to be integers, or can they be fractional values?

## Turn 15 - User Simulator

The numbers of heavy and light bombs used in the mission must be integers.

## Turn 16 - Generic Agent

QUESTION: Is there a limit on the total number of round trips the aircraft can make during the mission, or is the only constraint on the number of trips the fuel and bomb availability?

## Turn 16 - User Simulator

The only constraints on the number of trips are the fuel and bomb availability.

## Turn 17 - Generic Agent

QUESTION: Are there any other constraints or requirements for the mission that have not been mentioned, such as minimum or maximum numbers of bombs that must be dropped on each key part, or specific sequencing requirements for the bombing runs?

## Turn 17 - User Simulator

No, there are no other constraints or requirements for the mission beyond those already mentioned.

## Turn 18 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:**
    *   $H_i$: Number of heavy bombs dropped on key part $i$ (integer, non-negative).
    *   $L_i$: Number of light bombs dropped on key part $i$ (integer, non-negative).
    *   Indices $i \in \{1, 2, 3, 4\}$.
3.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^{4} H_i \le 28$.
    *   **Light Bomb Limit:** $\sum_{i=1}^{4} L_i \le 12$.
    *   **Fuel Limit:** Total fuel consumption across all trips $\le 10,000$ liters.
4.  **Fuel Consumption Model:**
    *   Each bomb drop corresponds to one round trip.
    *   The aircraft carries only one bomb per trip.
    *   Fuel for a heavy bomb trip to part $i$: $(2 \times d_i / 2) + 100 = d_i + 100$ liters.
    *   Fuel for a light bomb trip to part $i$: $(2 \times d_i / 3) + 100$ liters.
    *   Distances ($d_i$): Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.
    *   Total Fuel Constraint: $\sum_{i=1}^{4} [H_i(d_i + 100) + L_i(\frac{2d_i}{3} + 100)] \le 10,000$.
5.  **Probability Model:**
    *   **Assumption 1 (Independence of Bombs on Same Part):** The destruction events for individual bombs dropped on the same key part are independent. The probability that part $i$ is destroyed given $H_i$ heavy and $L_i$ light bombs is $1 - (1 - p_{H,i})^{H_i} (1 - p_{L,i})^{L_i}$, where $p_{H,i}$ and $p_{L,i}$ are the per-bomb destruction probabilities.
    *   **Assumption 2 (Independence Across Parts):** The destruction events for different key parts are independent. The probability that at least two parts are destroyed is calculated based on the joint distribution of the four independent part-destruction events.
6.  **Data:**
    *   $p_{H,1}=0.03, p_{L,1}=0.08$
    *   $p_{H,2}=0.10, p_{L,2}=0.11$
    *   $p_{H,3}=0.05, p_{L,3}=0.12$
    *   $p_{H,4}=0.05, p_{L,4}=0.09$

**Open Assumptions:**
*   The statistical independence of bomb effects on the same target and across different targets was not explicitly confirmed by the user but is the standard interpretation for this type of problem. If these assumptions are incorrect, the probability calculation will need to be adjusted.