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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is it to guarantee (i.e., achieve with certainty) that at least two parts are destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed. It is not to guarantee destruction with certainty.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb, is the fuel efficiency of 2 km per liter applied to the entire round trip (both outbound and return legs), or does the aircraft use 2 km per liter only on the outbound leg and 4 km per liter on the return leg when it is empty?

## Turn 2 - User Simulator

The fuel efficiency of 2 km per liter applies to the entire round trip when carrying a heavy bomb.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a light bomb, is the fuel efficiency of 3 km per liter applied to the entire round trip (both outbound and return legs), or does the aircraft use 3 km per liter only on the outbound leg and 4 km per liter on the return leg when it is empty?

## Turn 3 - User Simulator

The fuel efficiency of 3 km per liter applies to the entire round trip when carrying a light bomb.

## Turn 4 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel consumption applied once per round trip (i.e., once per bombing run), or is it applied separately to the takeoff and to the landing, making it 200 liters per round trip?

## Turn 4 - User Simulator

The 100-liter fuel consumption is applied once per round trip.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb simultaneously on a single bombing run, or is each bombing run limited to carrying exactly one bomb (either heavy or light)?

## Turn 5 - User Simulator

Each bombing run is limited to carrying exactly one bomb, either heavy or light.

## Turn 6 - Generic Agent

QUESTION: When multiple bombs are dropped on the same key part, is the probability that the part is destroyed calculated as 1 minus the product of the probabilities that each individual bomb fails to destroy it, assuming independent events

## Turn 6 - User Simulator

Yes, the probability that a key part is destroyed when multiple bombs are dropped on it is calculated as 1 minus the product of the probabilities that each individual bomb fails to destroy it, assuming independent events.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative

## Turn 7 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative.

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part

## Turn 8 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 9 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission that

## Turn 9 - User Simulator

No, there are no additional constraints or requirements beyond those already specified.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$ (for $i=1,2,3,4$), and $l_i$ be the number of light bombs assigned to key part $i$.
3.  **Variable Domain:** All $h_i$ and $l_i$ are non-negative integers.
4.  **Resource Constraints:**
    *   Total heavy bombs used: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs used: $\sum_{i=1}^{4} l_i \le 12$.
    *   Total fuel consumption: $\sum_{i=1}^{4} (h_i \cdot F_{heavy, i} + l_i \cdot F_{light, i}) \le 10,000$ liters.
5.  **Fuel Calculation per Bombing Run:**
    *   Each bombing run is a round trip from the airport to the target and back.
    *   Each run carries exactly one bomb (either heavy or light).
    *   **Heavy Bomb Run to Part $i$:**
        *   Distance: $2 \times d_i$ km (round trip).
        *   Efficiency: 2 km/liter for the entire round trip.
        *   Fuel for flight: $(2 \times d_i) / 2 = d_i$ liters.
        *   Takeoff/Landing: 100 liters.
        *   Total Fuel $F_{heavy, i} = d_i + 100$ liters.
    *   **Light Bomb Run to Part $i$:**
        *   Distance: $2 \times d_i$ km (round trip).
        *   Efficiency: 3 km/liter for the entire round trip.
        *   Fuel for flight: $(2 \times d_i) / 3$ liters.
        *   Takeoff/Landing: 100 liters.
        *   Total Fuel $F_{light, i} = \frac{2 d_i}{3} + 100$ liters.
6.  **Probability Model:**
    *   Destruction of each key part is independent of the others.
    *   For a specific key part $i$, the probability of destruction $P_i$ is calculated based on the bombs assigned to it.
    *   Let $p_{h,i}$ be the probability a single heavy bomb destroys part $i$, and $p_{l,i}$ be the probability a single light bomb destroys part $i$.
    *   The probability that part $i$ is *not* destroyed by one heavy bomb is $(1 - p_{h,i})$.
    *   The probability that part $i$ is *not* destroyed by one light bomb is $(1 - p_{l,i})$.
    *   The probability that part $i$ is destroyed given $h_i$ heavy and $l_i$ light bombs is:
        $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$.
    *   The objective is to maximize $P(\text{at least 2 parts destroyed}) = 1 - P(\text{0 parts destroyed}) - P(\text{exactly 1 part destroyed})$.
    *   $P(\text{0 parts destroyed}) = \prod_{i=1}^{4} (1 - P_i)$.
    *   $P(\text{exactly 1 part destroyed}) = \sum_{j=1}^{4} \left[ P_j \prod_{k \neq j} (1 - P_k) \right]$.

**Data Values:**
*   $d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600$.
*   $p_{h,1}=0.03, p_{h,2}=0.10, p_{h,3}=0.05, p_{h,4}=0.05$.
*   $p_{l,1}=0.08, p_{l,2}=0.11, p_{l,3}=0.12, p_{l,4}=0.09$.
*   $F_{heavy,1} = 450 + 100 = 550$ L.
*   $F_{heavy,2} = 480 + 100 = 580$ L.
*   $F_{heavy,3} = 540 + 100 = 640$ L.
*   $F_{heavy,4} = 600 + 100 = 700$ L.
*   $F_{light,1} = \frac{900}{3} + 100 = 300 + 100 = 400$ L.
*   $F_{light,2} = \frac{960}{3} + 100 = 320 + 100 = 420$ L.
*   $F_{light,3} = \frac{1080}{3} + 100 = 360 + 100 = 460$ L.
*   $F_{light,4} = \frac{1200}{3} + 100 = 400 + 100 = 500$ L.

**Assumptions:**
*   None. All critical facts were confirmed by the user.