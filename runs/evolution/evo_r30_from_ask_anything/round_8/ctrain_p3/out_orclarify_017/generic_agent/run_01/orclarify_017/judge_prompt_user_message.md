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

QUESTION: When the aircraft flies to a target carrying a bomb, does the fuel efficiency for the entire round trip depend on whether it is carrying a heavy or light bomb for both the outbound and return legs, or does it use the empty-aircraft efficiency for the return leg since the bomb is dropped at the target?

## Turn 2 - User Simulator

The fuel efficiency for the entire round trip depends on the bomb type carried for both the outbound and return legs.

## Turn 3 - Generic Agent

QUESTION: Can the aircraft make multiple separate trips to the same key part, dropping one bomb per trip, or is it limited to a single trip per key part where it can drop multiple bombs at once?

## Turn 3 - User Simulator

The aircraft can make multiple separate trips to the same key part, dropping one bomb per trip.

## Turn 4 - Generic Agent

QUESTION: Does the probability of destruction for a key part depend on the total number of bombs dropped on it, calculated as 1 minus the product of (1 minus individual probabilities) for each bomb, or is there a different rule for how multiple bombs combine their effects on the same part?

## Turn 4 - User Simulator

The probability of destruction for a key part depends on the total number of bombs dropped on it, calculated as 1 minus the product of (1 minus individual probabilities) for each bomb.

## Turn 5 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers, or can they be fractional values in the optimization model?

## Turn 5 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 6 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost incurred once per round trip to a target, regardless of how many bombs are dropped during that trip, or is it incurred for each individual bomb dropped?

## Turn 6 - User Simulator

The 100-liter takeoff and landing fuel cost is incurred once per round trip to a target.

## Turn 7 - Generic Agent

QUESTION: When calculating the fuel consumption for a round trip to a specific key part, is the distance used the one-way distance from the airport to that part multiplied by 2, or is there a different distance metric for the round trip?

## Turn 7 - User Simulator

The distance used is the one-way distance from the airport to that part multiplied by 2.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs and $l_i$ be the number of light bombs assigned to key part $i$ (for $i=1,2,3,4$). These variables are non-negative integers.
3.  **Bomb Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs: $\sum_{i=1}^{4} l_i \le 12$.
4.  **Fuel Constraints:**
    *   Total fuel consumption $\le 10,000$ liters.
    *   Fuel consumption is calculated per trip. Each trip is a round trip to a specific key part $i$.
    *   The aircraft makes one trip per bomb dropped (since it drops one bomb per trip).
    *   For a trip to part $i$ carrying a heavy bomb:
        *   Distance = $2 \times d_i$ (where $d_i$ is the one-way distance).
        *   Fuel for flight = $(2 \times d_i) / 2$ liters (efficiency 2 km/L).
        *   Takeoff/Landing cost = 100 liters.
        *   Total fuel per heavy bomb trip to $i$ = $d_i + 100$.
    *   For a trip to part $i$ carrying a light bomb:
        *   Distance = $2 \times d_i$.
        *   Fuel for flight = $(2 \times d_i) / 3$ liters (efficiency 3 km/L).
        *   Takeoff/Landing cost = 100 liters.
        *   Total fuel per light bomb trip to $i$ = $(2/3)d_i + 100$.
    *   Total Fuel = $\sum_{i=1}^{4} [ h_i(d_i + 100) + l_i(\frac{2}{3}d_i + 100) ] \le 10,000$.
5.  **Probability Calculation:**
    *   The destruction events for each key part are independent.
    *   The probability that part $i$ is destroyed, $P_i$, is calculated based on the number of heavy ($h_i$) and light ($l_i$) bombs assigned to it.
    *   $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for part $i$.
    *   The objective is to maximize $P(\text{at least 2 parts destroyed}) = 1 - P(\text{0 parts destroyed}) - P(\text{exactly 1 part destroyed})$.
    *   $P(\text{0 parts destroyed}) = \prod_{i=1}^{4} (1 - P_i)$.
    *   $P(\text{exactly 1 part destroyed}) = \sum_{j=1}^{4} P_j \prod_{k \neq j} (1 - P_k)$.

**Assumptions:**
*   None. All critical formulation details were confirmed by the user.