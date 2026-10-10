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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is there a different goal such as minimizing fuel or bomb usage subject to a minimum success probability?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: For a given key part, if you assign multiple bombs to it, is the probability that the part is destroyed calculated as 1 minus the probability that none of the assigned bombs destroy it, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, the probability that a key part is destroyed is calculated as 1 minus the probability that none of the assigned bombs destroy it, assuming each bomb's effect is independent.

## Turn 3 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, so that the probability of at least two parts being destroyed is calculated by summing the probabilities of all combinations where two or more parts are destroyed?

## Turn 3 - User Simulator

Yes, the destruction events for the four key parts are independent of each other.

## Turn 4 - Generic Agent

QUESTION: When calculating fuel consumption for a bombing run to a specific key part, is the fuel used for the outbound leg determined by the bomb type carried to that target, and the fuel used for the return leg determined by the empty-aircraft efficiency, or is the entire round trip calculated using a single efficiency rate?

## Turn 4 - User Simulator

The fuel used for the outbound leg is determined by the bomb type carried to that target, and the fuel used for the return leg is determined by the empty-aircraft efficiency.

## Turn 5 - Generic Agent

QUESTION: Does the 100-liter takeoff and landing fuel consumption apply once per round trip (i.e., once per bombing run to a target), or does it apply separately to the takeoff and to the landing, making it 200 liters per round trip?

## Turn 5 - User Simulator

The 100-liter takeoff and landing fuel consumption applies once per round trip.

## Turn 6 - Generic Agent

QUESTION: Can a single aircraft make multiple bombing runs to the same key part in one mission, or is each key part visited at most once?

## Turn 6 - User Simulator

A single aircraft can make multiple bombing runs to the same key part in one mission.

## Turn 7 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb simultaneously on a single bombing run, or is each run limited to carrying only one bomb?

## Turn 7 - User Simulator

Each run is limited to carrying only one bomb.

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers?

## Turn 8 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$, and $l_i$ be the number of light bombs assigned to key part $i$, for $i = 1, 2, 3, 4$.
3.  **Variable Domain:** $h_i$ and $l_i$ are non-negative integers.
4.  **Destruction Probability:** For key part $i$, the probability of destruction $P_i$ is calculated as:
    $$P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$$
    where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs, respectively.
5.  **Independence:** The destruction events for the four key parts are independent. The objective function is the sum of probabilities of all combinations where at least two parts are destroyed.
6.  **Bomb Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^4 h_i \le 28$
    *   Total light bombs: $\sum_{i=1}^4 l_i \le 12$
7.  **Fuel Constraints:**
    *   Total fuel available: 10,000 liters.
    *   Fuel consumption per run to key part $i$:
        *   Outbound leg (carrying heavy bomb): $2 \times \text{Distance}_i$ km / (2 km/L) = $\text{Distance}_i$ liters.
        *   Outbound leg (carrying light bomb): $2 \times \text{Distance}_i$ km / (3 km/L) = $\frac{2}{3} \text{Distance}_i$ liters.
        *   Return leg (empty): $2 \times \text{Distance}_i$ km / (4 km/L) = $\frac{1}{2} \text{Distance}_i$ liters.
        *   Takeoff/Landing: 100 liters per round trip.
    *   Total fuel constraint:
        $$\sum_{i=1}^4 \left[ h_i \left( \text{Distance}_i + \frac{1}{2} \text{Distance}_i + 100 \right) + l_i \left( \frac{2}{3} \text{Distance}_i + \frac{1}{2} \text{Distance}_i + 100 \right) \right] \le 10,000$$
        Simplifying the fuel per bomb type per part $i$:
        *   Heavy bomb run fuel: $1.5 \times \text{Distance}_i + 100$
        *   Light bomb run fuel: $\frac{7}{6} \times \text{Distance}_i + 100$

**Assumptions:**
*   None. All critical formulation details were confirmed by the user.