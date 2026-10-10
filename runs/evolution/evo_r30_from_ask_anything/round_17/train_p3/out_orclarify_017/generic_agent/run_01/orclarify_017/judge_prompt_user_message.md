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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is it to guarantee (with certainty) that at least two parts are destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed. It is not to guarantee destruction with certainty.

## Turn 2 - Generic Agent

QUESTION: For each key part, is the probability of destruction calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs of that type assigned to that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is the correct calculation method.

## Turn 3 - Generic Agent

QUESTION: Can a single aircraft carry both a heavy bomb and a light bomb simultaneously on one bombing run, or must each run carry exactly one bomb of one type?

## Turn 3 - User Simulator

Each run must carry exactly one bomb of one type.

## Turn 4 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as the sum of the fuel for the outbound leg (carrying the bomb), the fuel for the return leg (empty), plus the 100 liters for takeoff and landing?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers?

## Turn 5 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 6 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission planning that are not mentioned in the brief, such as minimum bomb counts per target, restrictions on which bomb types can be used on specific targets, or other operational limitations?

## Turn 6 - User Simulator

No, there are no additional constraints or requirements beyond those already mentioned.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed. (Confirmed)
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to part $i$, and $l_i$ be the number of light bombs assigned to part $i$, for $i \in \{1, 2, 3, 4\}$. (Confirmed)
3.  **Variable Domain:** $h_i$ and $l_i$ are non-negative integers. (Confirmed)
4.  **Destruction Probability:** The probability that part $i$ is destroyed is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$, respectively. (Confirmed)
5.  **Success Condition:** The mission is successful if the sum of the indicators for destroyed parts is at least 2. The objective function maximizes the probability of this event occurring. (Confirmed)
6.  **Bomb Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^4 h_i \le 28$. (Confirmed)
    *   Total light bombs: $\sum_{i=1}^4 l_i \le 12$. (Confirmed)
7.  **Fuel Constraints:**
    *   Total fuel available: 10,000 liters.
    *   Fuel consumption per run depends on the bomb type and distance.
    *   For a heavy bomb run to part $i$ (distance $d_i$):
        *   Outbound (carrying heavy): $d_i / 2$ liters.
        *   Return (empty): $d_i / 4$ liters.
        *   Takeoff/Landing: 100 liters.
        *   Total per heavy run to part $i$: $d_i/2 + d_i/4 + 100 = 0.75 d_i + 100$.
    *   For a light bomb run to part $i$ (distance $d_i$):
        *   Outbound (carrying light): $d_i / 3$ liters.
        *   Return (empty): $d_i / 4$ liters.
        *   Takeoff/Landing: 100 liters.
        *   Total per light run to part $i$: $d_i/3 + d_i/4 + 100 = \frac{7}{12} d_i + 100$.
    *   Total fuel constraint: $\sum_{i=1}^4 h_i (0.75 d_i + 100) + \sum_{i=1}^4 l_i (\frac{7}{12} d_i + 100) \le 10,000$. (Confirmed)
8.  **Run Structure:** Each run carries exactly one bomb of one type. (Confirmed)
9.  **No Other Constraints:** There are no minimum bomb counts, exclusivity rules, or other operational limitations. (Confirmed)

**Distances:**
*   $d_1 = 450$ km
*   $d_2 = 480$ km
*   $d_3 = 540$ km
*   $d_4 = 600$ km

**Per-bomb Destruction Probabilities:**
*   Part 1: Heavy 0.03, Light 0.08
*   Part 2: Heavy 0.10, Light 0.11
*   Part 3: Heavy 0.05, Light 0.12
*   Part 4: Heavy 0.05, Light 0.09