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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is it to minimize the total fuel consumed while ensuring that probability is at least some specific threshold?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: Are the decision variables the number of heavy bombs and light bombs assigned to each of the four key parts, with the constraint that the total number of heavy bombs used across all parts does not exceed 28 and the total number of light bombs used across all parts does not exceed 12?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs of that type assigned to that part, assuming each bomb's impact is independent?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run to a specific key part calculated as the sum of the fuel for the outbound leg (distance divided by the fuel efficiency of the bomb type carried) plus the fuel for the return leg (distance divided by the fuel efficiency when empty) plus the fixed 100 liters for takeoff and landing?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: Is the total fuel consumption for the mission calculated as the sum of the fuel consumption for each individual bombing run, where each run corresponds to one bomb dropped on one key part?

## Turn 5 - User Simulator

Yes, that is correct.

## Turn 6 - Generic Agent

QUESTION: Are the number of heavy bombs and light bombs assigned to each key part required to be non-negative integers?

## Turn 6 - User Simulator

Yes, they must be non-negative integers.

## Turn 7 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission, such as a minimum number of bombs that must be dropped on each key part, a limit on the number of bombing runs per key part, or any other operational restrictions?

## Turn 7 - User Simulator

No, there are no additional constraints or requirements beyond those already specified.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$ and $l_i$ be the number of light bombs assigned to key part $i$, for $i = 1, 2, 3, 4$.
3.  **Variable Domain:** $h_i$ and $l_i$ are non-negative integers for all $i$.
4.  **Destruction Probability:** The probability that key part $i$ is destroyed is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$, respectively.
5.  **Success Condition:** The mission is successful if the sum of the indicators for destroyed parts is at least 2. The objective is to maximize the probability of this event.
6.  **Bomb Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs: $\sum_{i=1}^{4} l_i \le 12$.
7.  **Fuel Constraints:**
    *   Total fuel consumption $\le 10,000$ liters.
    *   Fuel for a run to part $i$ with a heavy bomb: $2 \times d_i$ (outbound) + $0.25 \times d_i$ (return, since 4 km/L) + 100 (takeoff/landing). Note: Efficiency is km/L, so Fuel = Distance / Efficiency.
        *   Outbound (Heavy): $d_i / 2$ liters.
        *   Return (Empty): $d_i / 4$ liters.
        *   Fixed: 100 liters.
        *   Total per heavy run to $i$: $d_i/2 + d_i/4 + 100 = 0.75 d_i + 100$.
    *   Fuel for a run to part $i$ with a light bomb:
        *   Outbound (Light): $d_i / 3$ liters.
        *   Return (Empty): $d_i / 4$ liters.
        *   Fixed: 100 liters.
        *   Total per light run to $i$: $d_i/3 + d_i/4 + 100 = (7/12) d_i + 100$.
    *   Total Fuel: $\sum_{i=1}^{4} [h_i (0.75 d_i + 100) + l_i ((7/12) d_i + 100)] \le 10,000$.
8.  **Distances:** $d_1=450, d_2=480, d_3=540, d_4=600$ km.
9.  **Probabilities:**
    *   Part 1: $p_{h,1}=0.03, p_{l,1}=0.08$
    *   Part 2: $p_{h,2}=0.10, p_{l,2}=0.11$
    *   Part 3: $p_{h,3}=0.05, p_{l,3}=0.12$
    *   Part 4: $p_{h,4}=0.05, p_{l,4}=0.09$
10. **Assumptions:**
    *   Each bomb drop requires a separate round-trip flight.
    *   The aircraft returns to the airport after each bomb drop.
    *   The probability of destruction for each part is independent of the others.
    *   The "at least two" condition applies to the final state of the four parts after all bombs are dropped.