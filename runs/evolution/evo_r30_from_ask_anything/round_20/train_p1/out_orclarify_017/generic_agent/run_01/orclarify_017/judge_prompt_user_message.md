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

QUESTION: Are the numbers of heavy and light bombs assigned to each of the four key parts required to be non-negative integers?

## Turn 2 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 3 - Generic Agent

QUESTION: Is the probability that a specific key part is destroyed calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the total number of bombs assigned to that part, assuming each bomb's impact is independent?

## Turn 3 - User Simulator

Yes, the probability that a specific key part is destroyed is calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the total number of bombs assigned to that part, assuming each bomb's impact is independent.

## Turn 4 - Generic Agent

QUESTION: Are the destruction events for the four key parts assumed to be independent of each other when calculating the probability that at least two parts are destroyed?

## Turn 4 - User Simulator

Yes, the destruction events for the four key parts are assumed to be independent of each other.

## Turn 5 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run to a specific key part calculated as the sum of the fuel for the outbound leg (distance divided by the efficiency of the bomb type carried), the fuel for the return leg (distance divided by the empty efficiency of 4 km per liter), and the fixed 100 liters for takeoff and landing?

## Turn 5 - User Simulator

Yes, the fuel consumption for a bombing run to a specific key part is calculated as the sum of the fuel for the outbound leg (distance divided by the efficiency of the bomb type carried), the fuel for the return leg (distance divided by the empty efficiency of 4 km per liter), and the fixed 100 liters for takeoff and landing.

## Turn 6 - Generic Agent

QUESTION: Is the total fuel consumption for the mission calculated as the sum of the fuel consumed by each individual bombing run, where each run carries exactly one bomb to one specific key part?

## Turn 6 - User Simulator

Yes, the total fuel consumption for the mission is calculated as the sum of the fuel consumed by each individual bombing run, where each run carries exactly one bomb to one specific key part.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements for the mission, such as a minimum number of bombs that must be used, a limit on the total number of bombing runs, or a requirement that every key part must receive at least one bomb?

## Turn 7 - User Simulator

No, there are no other constraints or requirements. The only constraints are:
- At least two of the four key parts must be destroyed.
- Heavy bombs used cannot exceed 28.
- Light bombs used cannot exceed 12.
- Total fuel consumption must not exceed 10,000 liters.
- Each aircraft can carry only one bomb per trip.
- Each bombing run is a round trip from the airport to the target and back.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:**
    *   $h_i$: Number of heavy bombs assigned to key part $i$ (for $i=1, 2, 3, 4$).
    *   $l_i$: Number of light bombs assigned to key part $i$ (for $i=1, 2, 3, 4$).
    *   Domain: All variables are non-negative integers.
3.  **Probability Model:**
    *   The probability that key part $i$ is destroyed is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs, respectively.
    *   The destruction events for the four key parts are independent.
    *   The objective function is the sum of the probabilities of all combinations where at least two parts are destroyed.
4.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^{4} h_i \le 28$.
    *   **Light Bomb Limit:** $\sum_{i=1}^{4} l_i \le 12$.
    *   **Fuel Limit:** Total fuel consumption $\le 10,000$ liters.
5.  **Fuel Calculation:**
    *   Each bombing run carries exactly one bomb.
    *   Fuel for a heavy bomb run to part $i$: $100 + \frac{d_i}{2} + \frac{d_i}{4}$ liters.
    *   Fuel for a light bomb run to part $i$: $100 + \frac{d_i}{3} + \frac{d_i}{4}$ liters.
    *   Total fuel is the sum of fuel for all individual runs.
    *   Distances $d_i$: Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.
6.  **Per-Bomb Destruction Probabilities:**
    *   Part 1: Heavy 0.03, Light 0.08
    *   Part 2: Heavy 0.10, Light 0.11
    *   Part 3: Heavy 0.05, Light 0.12
    *   Part 4: Heavy 0.05, Light 0.09