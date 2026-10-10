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

QUESTION: When the aircraft carries a heavy bomb, is the fuel efficiency of 2 km per liter applied to the entire round trip (both the outbound leg to the target and the return leg to the airport), or does the efficiency change depending on whether the bomb has been dropped?

## Turn 2 - User Simulator

The fuel efficiency of 2 km per liter applies to the entire round trip when carrying a heavy bomb.

## Turn 3 - Generic Agent

QUESTION: Does the 100-liter takeoff and landing fuel consumption apply once per round trip (i.e., once for the takeoff at the start and once for the landing at the end), or is it 100 liters for takeoff plus 100 liters for landing, totaling 200 liters per round trip?

## Turn 3 - User Simulator

The 100 liters is the combined total for takeoff and landing per round trip.

## Turn 4 - Generic Agent

QUESTION: When the aircraft carries a light bomb, is the fuel efficiency of 3 km per liter applied to the entire round trip (both the outbound leg to the target and the return leg to the airport), or does the efficiency change depending on whether the bomb has been dropped?

## Turn 4 - User Simulator

The fuel efficiency of 3 km per liter applies to the entire round trip when carrying a light bomb.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb simultaneously on a single round trip, or is each round trip limited to carrying only one bomb (either heavy or light)?

## Turn 5 - User Simulator

Each round trip is limited to carrying only one bomb, either heavy or light.

## Turn 6 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), is the fuel efficiency of 4 km per liter applied to the entire round trip, or is this efficiency only relevant for a specific leg of the journey?

## Turn 6 - User Simulator

The fuel efficiency of 4 km per liter applies to the entire round trip when the aircraft is empty.

## Turn 7 - Generic Agent

QUESTION: Are the probabilities of destruction for each key part independent across different bombing runs, meaning that the probability of a part being destroyed by a second bomb is calculated independently of whether it was already hit by a previous bomb?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Assuming the destruction events are independent, is the probability that a key part is destroyed by multiple bombs calculated using the formula 1 minus the product of (1 minus individual probabilities) for each bomb, or is there a different cumulative probability rule applied?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each of the four key parts required to be integers, or can they be fractional values in the optimization model?

## Turn 9 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be integers.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum limit on the total number of bombing runs (round trips) the aircraft can perform, or is the only constraint on the number of runs derived from the fuel and bomb availability limits?

## Turn 10 - User Simulator

There is no separate maximum limit on the total number of bombing runs. The only constraints on the number of runs are derived from the fuel and bomb availability limits.

## Turn 11 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission, such as minimum numbers of bombs that must be used, specific sequencing rules for the bombing runs, or restrictions on which targets can be attacked in a single mission?

## Turn 11 - User Simulator

No, there are no additional constraints or requirements beyond those already specified.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:**
    *   Let $h_i$ be the number of heavy bombs assigned to key part $i$ (for $i = 1, 2, 3, 4$).
    *   Let $l_i$ be the number of light bombs assigned to key part $i$ (for $i = 1, 2, 3, 4$).
    *   All variables $h_i$ and $l_i$ are non-negative integers.
3.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^{4} h_i \le 28$.
    *   **Light Bomb Limit:** $\sum_{i=1}^{4} l_i \le 12$.
    *   **Fuel Limit:** Total fuel consumption $\le 10,000$ liters.
        *   Fuel for a heavy bomb run to part $i$: $2 \times (2 \times \text{Distance}_i) + 100$ liters. (Note: Efficiency is 2 km/L, so Fuel = Distance / Efficiency. Round trip distance is $2 \times \text{Distance}_i$. So Fuel = $(2 \times \text{Distance}_i) / 2 + 100 = \text{Distance}_i + 100$).
        *   Fuel for a light bomb run to part $i$: $(2 \times \text{Distance}_i) / 3 + 100$ liters.
        *   Total Fuel = $\sum_{i=1}^{4} [ h_i (\text{Distance}_i + 100) + l_i (\frac{2 \times \text{Distance}_i}{3} + 100) ] \le 10,000$.
4.  **Probability Calculation (Assumed):**
    *   **Assumption:** Destruction events are independent.
    *   **Assumption:** The probability that key part $i$ is destroyed given $h_i$ heavy bombs and $l_i$ light bombs is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb probabilities from the table.
    *   **Assumption:** The probability that at least two parts are destroyed is calculated by summing the probabilities of all combinations of two or more parts being destroyed, assuming independence between the destruction of different parts.
5.  **Other Rules:**
    *   Each round trip carries exactly one bomb (heavy or light).
    *   No separate limit on the total number of runs.
    *   No other constraints or sequencing rules.

**Explicit Assumptions:**
*   Independence of destruction events for a single part across multiple bombs.
*   Independence of destruction events across different parts.
*   The standard cumulative probability formula $1 - \prod(1-p)$ is used for calculating the probability of a part being destroyed by multiple bombs.