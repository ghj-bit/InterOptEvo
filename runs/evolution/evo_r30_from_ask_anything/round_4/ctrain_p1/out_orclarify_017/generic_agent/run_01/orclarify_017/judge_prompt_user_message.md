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

QUESTION: Is the mission's success criterion that at least two of the four key parts must be destroyed with a probability of at least 50%, or is it a deterministic requirement that at least two parts must be destroyed with certainty

## Turn 1 - User Simulator

The success criterion is that at least two of the four key parts are destroyed. We want to maximize the probability of achieving this outcome. It is not a deterministic requirement that two parts must be destroyed with certainty, nor is there a fixed 50% probability threshold.

## Turn 2 - Generic Agent

QUESTION: Are the destruction probabilities for each key part independent of the destruction probabilities for the other key

## Turn 2 - User Simulator

The destruction probabilities for each key part are independent of the destruction probabilities for the other key parts.

## Turn 3 - Generic Agent

QUESTION: Does the probability of destruction for a specific key part depend on the total number of bombs of each type assigned to that part

## Turn 3 - User Simulator

Yes, the probability of destruction for a specific key part depends on the total number of heavy bombs and light bombs assigned to that part.

## Turn 4 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated as 1 minus the product of (1 minus the individual bomb probability) for every heavy and light bomb assigned

## Turn 4 - User Simulator

Yes, the probability of destroying a key part is calculated as 1 minus the product of (1 minus the individual bomb probability) for every heavy and light bomb assigned to that part.

## Turn 5 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as the sum of the fuel for the outbound leg, the fuel for the return leg

## Turn 5 - User Simulator

Yes, the fuel consumption for a bombing run is calculated as the sum of the fuel for the outbound leg and the fuel for the return leg.

## Turn 6 - Generic Agent

QUESTION: When calculating the fuel for the outbound leg of a bombing run to a specific key part, is the fuel efficiency determined by the type of bomb being

## Turn 6 - User Simulator

Yes, the fuel efficiency for the outbound leg is determined by the type of bomb being carried.

## Turn 7 - Generic Agent

QUESTION: Is the fuel efficiency for the return leg of a bombing

## Turn 7 - User Simulator

Yes, the fuel efficiency for the return leg is determined by the aircraft being empty, which is 4 km per liter.

## Turn 8 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel

## Turn 8 - User Simulator

Yes, the 100-liter takeoff and landing fuel consumption is included in the total fuel consumption for each bombing run.

## Turn 9 - Generic Agent

QUESTION: Can a single bombing run carry multiple bombs

## Turn 9 - User Simulator

No, each aircraft can carry only one bomb per trip.

## Turn 10 - Generic Agent

QUESTION: Is the total number of bombing

## Turn 10 - User Simulator

The total number of bombing runs is not fixed; it is determined by the number of heavy and light bombs used, since each run carries exactly one bomb.

## Turn 11 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run to a specific key part calculated as (distance to that key part divided by the fuel

## Turn 11 - User Simulator

Yes, the fuel consumption for a bombing run to a specific key part is calculated as the distance to that key part divided by the fuel efficiency for the outbound leg, plus the distance to that key part divided by the fuel efficiency for the return leg, plus 100 liters for takeoff and landing.

## Turn 12 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key

## Turn 12 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part are the decision variables to be determined.

## Turn 13 - Generic Agent

QUESTION: Are the decision variables for the number of heavy and light

## Turn 13 - User Simulator

Yes, the decision variables are the number of heavy bombs and the number of light bombs assigned to each of the four key parts.

## Turn 14 - Generic Agent

QUESTION: Are the decision variables for the number of heavy

## Turn 14 - User Simulator

Yes, the decision variables are the number of heavy bombs and the number of light bombs assigned to each of the four key parts.

## Turn 15 - Generic Agent

QUESTION: Are the decision variables for the number of

## Turn 15 - User Simulator

Yes, the decision variables are the number of heavy bombs and the number of light bombs assigned to each of the four key parts.

## Turn 16 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$ and $l_i$ be the number of light bombs assigned to key part $i$, for $i = 1, 2, 3, 4$.
3.  **Variable Domains:** $h_i$ and $l_i$ are non-negative integers.
4.  **Destruction Probability:** The probability $p_i$ that key part $i$ is destroyed is calculated as:
    $$ p_i = 1 - \prod_{j=1}^{h_i} (1 - p_{H,i}) \prod_{k=1}^{l_i} (1 - p_{L,i}) $$
    where $p_{H,i}$ and $p_{L,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$, respectively. If $h_i=0$ or $l_i=0$, the respective product is 1.
5.  **Success Condition:** The mission is successful if at least two of the four events $\{ \text{Part } i \text{ is destroyed} \}$ occur. Since the destruction events are independent, the probability of success is the sum of the probabilities of all combinations where exactly 2, 3, or 4 parts are destroyed.
6.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^{4} h_i \le 28$
    *   **Light Bomb Limit:** $\sum_{i=1}^{4} l_i \le 12$
    *   **Fuel Limit:** Total fuel consumption $\le 10,000$ liters.
7.  **Fuel Calculation:**
    *   Each bomb requires one bombing run.
    *   A bombing run to key part $i$ carrying a heavy bomb consumes:
        $$ F_{H,i} = \frac{d_i}{2} + \frac{d_i}{4} + 100 $$
    *   A bombing run to key part $i$ carrying a light bomb consumes:
        $$ F_{L,i} = \frac{d_i}{3} + \frac{d_i}{4} + 100 $$
    *   Total Fuel: $\sum_{i=1}^{4} (h_i \cdot F_{H,i} + l_i \cdot F_{L,i}) \le 10,000$
    *   Distances $d_i$: $d_1=450, d_2=480, d_3=540, d_4=600$ km.
8.  **Independence:** The destruction of each key part is independent of the others.
9.  **Run Structure:** Each run carries exactly one bomb. The outbound leg fuel efficiency depends on the bomb type (2 km/L for heavy, 3 km/L for light). The return leg fuel efficiency is always 4 km/L (empty aircraft). Takeoff/landing adds 100 liters per run.