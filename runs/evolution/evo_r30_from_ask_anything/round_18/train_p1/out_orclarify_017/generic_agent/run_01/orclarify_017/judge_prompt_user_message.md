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

QUESTION: Is the mission's objective to minimize total fuel consumption while ensuring at least two of the four key parts are destroyed, or is it to maximize the probability of destroying at least two parts subject to the fuel and bomb limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two of the four key parts, subject to the fuel and bomb limits.

## Turn 2 - Generic Agent

QUESTION: Are the probabilities of destruction for each key part independent across the different bombs dropped on that part, so that the probability a part survives is the product of the survival probabilities for each bomb assigned to it?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the fuel calculation, is the fuel consumed on the outbound leg determined by the bomb type carried on that leg, and is the fuel consumed on the return leg determined by the same bomb type or by the aircraft being empty?

## Turn 3 - User Simulator

The fuel consumed on the outbound leg is determined by the bomb type carried. The fuel consumed on the return leg is determined by the aircraft being empty.

## Turn 4 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as one minus the product of the survival probabilities for each bomb dropped on that part, assuming the destruction events for individual bombs are independent?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost incurred once per round trip (i.e., once per bombing run to a target), or is it incurred separately for each takeoff and each landing?

## Turn 5 - User Simulator

The 100-liter takeoff and landing fuel cost is incurred once per round trip.

## Turn 6 - Generic Agent

QUESTION: Can a single bombing run to a specific key part carry both heavy and light bombs simultaneously, or must each run carry only one type of bomb?

## Turn 6 - User Simulator

Each run must carry only one bomb.

## Turn 7 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as one minus the product of the survival probabilities for each bomb dropped on that part, assuming the destruction events for individual bombs are independent?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers, meaning you cannot assign a fractional number of bombs to a target?

## Turn 8 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 9 - Generic Agent

QUESTION: Is the total fuel consumption calculated as the sum of the fuel used for each individual bombing run, where each run's fuel is the distance to the target times the bomb type's fuel efficiency plus the 100-liter takeoff/landing cost?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is the fuel consumed on the outbound leg calculated by dividing the distance to the target by the fuel efficiency of the bomb type carried, and is the fuel consumed on the return leg calculated by dividing the distance by the empty aircraft fuel efficiency of 4 km per liter?

## Turn 10 - User Simulator

Yes, the fuel consumed on the outbound leg is calculated by dividing the distance to the target by the fuel efficiency of the bomb type carried, and the fuel consumed on the return leg is calculated by dividing the distance by the empty aircraft fuel efficiency of 4 km per liter.

## Turn 11 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as one minus the product of the survival probabilities for each bomb dropped on that part, assuming the destruction events for individual bombs are independent?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission planning that have not been mentioned yet, such as minimum or maximum numbers of bombs that must be dropped on each key part, or specific sequencing requirements for the bombing runs?

## Turn 12 - User Simulator

No, there are no additional constraints or requirements beyond those already mentioned.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$ ($i=1,2,3,4$) and $l_i$ be the number of light bombs assigned to key part $i$. All variables are non-negative integers.
3.  **Bomb Limits:**
    *   Total heavy bombs: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs: $\sum_{i=1}^{4} l_i \le 12$.
4.  **Fuel Constraints:**
    *   Total fuel consumption $\le 10,000$ liters.
    *   Each bomb dropped requires a separate round-trip run.
    *   For a heavy bomb run to part $i$ (distance $d_i$): Fuel = $\frac{d_i}{2} + \frac{d_i}{4} + 100$.
    *   For a light bomb run to part $i$ (distance $d_i$): Fuel = $\frac{d_i}{3} + \frac{d_i}{4} + 100$.
    *   Total Fuel = $\sum_{i=1}^{4} \left[ h_i \left( \frac{d_i}{2} + \frac{d_i}{4} + 100 \right) + l_i \left( \frac{d_i}{3} + \frac{d_i}{4} + 100 \right) \right] \le 10,000$.
5.  **Distances:** $d_1=450, d_2=480, d_3=540, d_4=600$ km.
6.  **Destruction Probabilities:**
    *   Heavy bomb destruction probabilities: $p_{h1}=0.03, p_{h2}=0.10, p_{h3}=0.05, p_{h4}=0.05$.
    *   Light bomb destruction probabilities: $p_{l1}=0.08, p_{l2}=0.11, p_{l3}=0.12, p_{l4}=0.09$.
7.  **Success Condition:** The mission is successful if at least two parts are destroyed. The objective function maximizes the probability of this event.

**Explicit Assumptions:**

1.  **Independence of Destruction Events:** It is assumed that the destruction of a key part by each individual bomb is an independent event. Therefore, the probability that part $i$ is destroyed is $1 - \prod_{j=1}^{h_i} (1-p_{hi}) \prod_{k=1}^{l_i} (1-p_{li})$. The probability that at least two parts are destroyed is calculated based on the joint distribution of the destruction statuses of the four parts, assuming independence between different parts.
2.  **Fuel Calculation Verification:** The fuel calculation formula derived from the user's confirmation is: Outbound Fuel = Distance / Efficiency, Return Fuel = Distance / 4, plus 100L fixed cost per run. This results in specific fuel costs per bomb type per target:
    *   Heavy to Part 1: $450/2 + 450/4 + 100 = 225 + 112.5 + 100 = 437.5$ L
    *   Heavy to Part 2: $480/2 + 480/4 + 100 = 240 + 120 + 100 = 460$ L
    *   Heavy to Part 3: $540/2 + 540/4 + 100 = 270 + 135 + 100 = 505$ L
    *   Heavy to Part 4: $600/2 + 600/4 + 100 = 300 + 150 + 100 = 550$ L
    *   Light to Part 1: $450/3 + 450/4 + 100 = 150 + 112.5 + 100 = 362.5$ L
    *   Light to Part 2: $480/3 + 480/4 + 100 = 160 + 120 + 100 = 380$ L
    *   Light to Part 3: $540/3 + 540/4 + 100 = 180 + 135 + 100 = 415$ L
    *   Light to Part 4: $600/3 + 600/4 + 100 = 200 + 150 + 100 = 450$ L