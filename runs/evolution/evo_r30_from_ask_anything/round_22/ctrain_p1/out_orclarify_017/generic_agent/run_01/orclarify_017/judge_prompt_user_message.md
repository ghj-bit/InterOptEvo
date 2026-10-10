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

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers?

## Turn 2 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 3 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs assigned to that part, assuming independent attempts?

## Turn 3 - User Simulator

Yes, the probability of destroying a key part is calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs assigned to that part, assuming independent attempts.

## Turn 4 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as the sum of the fuel for the outbound leg (carrying the bomb), the fuel for the return leg (empty), and the fixed 100 liters for takeoff and landing?

## Turn 4 - User Simulator

Yes, the fuel consumption for a bombing run is calculated as the sum of the fuel for the outbound leg (carrying the bomb), the fuel for the return leg (empty), and the fixed 100 liters for takeoff and landing.

## Turn 5 - Generic Agent

QUESTION: Is the total fuel consumption constraint applied to the sum of fuel used across all individual bombing runs, where each run corresponds to one bomb dropped on one specific key part?

## Turn 5 - User Simulator

Yes, the total fuel consumption constraint is applied to the sum of fuel used across all individual bombing runs, where each run corresponds to one bomb dropped on one specific key part.

## Turn 6 - Generic Agent

QUESTION: Are the four key parts assumed to be destroyed independently of one another, such that the probability of the mission success is calculated by summing the probabilities of all combinations where at least two parts are destroyed?

## Turn 6 - User Simulator

Yes, the four key parts are assumed to be destroyed independently of one another, such that the probability of mission success is calculated by summing the probabilities of all combinations where at least two parts are destroyed.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$, and $l_i$ be the number of light bombs assigned to key part $i$, for $i = 1, 2, 3, 4$.
3.  **Variable Domain:** $h_i$ and $l_i$ are non-negative integers.
4.  **Probability Model:**
    *   The probability of destroying key part $i$ is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$, respectively.
    *   The destruction of the four key parts is independent.
    *   The mission success probability is the sum of the probabilities of all subsets of $\{1, 2, 3, 4\}$ with size at least 2.
5.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^{4} h_i \le 28$.
    *   **Light Bomb Limit:** $\sum_{i=1}^{4} l_i \le 12$.
    *   **Fuel Limit:** The total fuel consumption across all bombing runs must not exceed 10,000 liters.
6.  **Fuel Calculation:**
    *   Each bomb dropped corresponds to one round-trip bombing run.
    *   For a heavy bomb on part $i$ (distance $d_i$ km):
        *   Outbound fuel: $d_i / 2$ liters (efficiency 2 km/L).
        *   Return fuel: $d_i / 4$ liters (efficiency 4 km/L, empty).
        *   Takeoff/Landing: 100 liters.
        *   Total per heavy bomb run on part $i$: $0.75 d_i + 100$ liters.
    *   For a light bomb on part $i$ (distance $d_i$ km):
        *   Outbound fuel: $d_i / 3$ liters (efficiency 3 km/L).
        *   Return fuel: $d_i / 4$ liters (efficiency 4 km/L, empty).
        *   Takeoff/Landing: 100 liters.
        *   Total per light bomb run on part $i$: $(1/3 + 1/4) d_i + 100 = \frac{7}{12} d_i + 100$ liters.
    *   Total Fuel Constraint: $\sum_{i=1}^{4} h_i (0.75 d_i + 100) + \sum_{i=1}^{4} l_i (\frac{7}{12} d_i + 100) \le 10,000$.

**Data:**
*   Distances ($d_i$): $d_1=450, d_2=480, d_3=540, d_4=600$.
*   Heavy Bomb Probabilities ($p_{h,i}$): $p_{h,1}=0.03, p_{h,2}=0.10, p_{h,3}=0.05, p_{h,4}=0.05$.
*   Light Bomb Probabilities ($p_{l,i}$): $p_{l,1}=0.08, p_{l,2}=0.11, p_{l,3}=0.12, p_{l,4}=0.09$.

**Assumptions:**
*   None. All critical facts were confirmed by the user.