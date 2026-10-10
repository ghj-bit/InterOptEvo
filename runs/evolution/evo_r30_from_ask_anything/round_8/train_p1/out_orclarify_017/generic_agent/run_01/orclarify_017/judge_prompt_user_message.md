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

QUESTION: Is the mission's objective to minimize the total number of bombs used (heavy plus light) subject to the constraint that the probability of destroying at least two of the four key parts is at least some specified threshold, or is the objective to maximize the probability of destroying at least two key parts subject to the bomb and fuel limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two key parts, subject to the bomb and fuel limits.

## Turn 2 - Generic Agent

QUESTION: For the fuel calculation, is the fuel consumed on the outbound leg determined by the bomb type carried during that leg, and is the fuel consumed on the return leg always calculated using the empty-aircraft efficiency of 4 km per liter since the bomb is dropped at the target?

## Turn 2 - User Simulator

Yes, the fuel consumed on the outbound leg is determined by the bomb type carried, and the fuel consumed on the return leg is calculated using the empty-aircraft efficiency of 4 km per liter.

## Turn 3 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs of that type assigned to that part, assuming each bomb's impact is independent?

## Turn 3 - User Simulator

Yes, the probability of destroying a key part is calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs of that type assigned to that part, assuming each bomb's impact is independent.

## Turn 4 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, so that the probability of destroying at least two parts is calculated by summing the probabilities of all combinations where two or more parts are destroyed?

## Turn 4 - User Simulator

Yes, the destruction events for the four key parts are independent of each other.

## Turn 5 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost incurred once per round trip to a specific target part, regardless of whether the aircraft carries a heavy bomb, a light bomb, or both types of bombs on that trip?

## Turn 5 - User Simulator

Yes, the 100-liter takeoff and landing fuel cost is incurred once per round trip to a specific target part, regardless of the bomb type carried.

## Turn 6 - Generic Agent

QUESTION: Can the aircraft carry both heavy and light bombs simultaneously on a single trip to a target part, or must each trip be dedicated to carrying only one type of bomb?

## Turn 6 - User Simulator

Each trip must be dedicated to carrying only one type of bomb.

## Turn 7 - Generic Agent

QUESTION: If the aircraft makes multiple trips to the same target part, is the fuel efficiency for the outbound leg of each trip determined by the specific bomb type carried on that particular trip?

## Turn 7 - User Simulator

Yes, the fuel efficiency for the outbound leg of each trip is determined by the specific bomb type carried on that particular trip.

## Turn 8 - Generic Agent

QUESTION: Is the number of bombs of each type assigned to each key part required to be a non-negative integer?

## Turn 8 - User Simulator

Yes, the number of bombs of each type assigned to each key part must be a non-negative integer.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability of destroying at least two of the four key parts.
2.  **Decision Variables:** Let $h_{i}$ and $l_{i}$ be the number of heavy and light bombs assigned to key part $i$ (where $i \in \{1, 2, 3, 4\}$). These variables must be non-negative integers.
3.  **Probability Calculation:**
    *   The probability of destroying key part $i$ is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs, respectively.
    *   The destruction events for the four parts are independent.
    *   The objective function is the sum of the probabilities of all mutually exclusive events where exactly 2, 3, or 4 parts are destroyed.
4.  **Constraints:**
    *   **Bomb Limits:** $\sum_{i=1}^{4} h_i \le 28$ and $\sum_{i=1}^{4} l_i \le 12$.
    *   **Fuel Limit:** Total fuel consumption $\le 10,000$ liters.
5.  **Fuel Calculation:**
    *   Each trip is a round trip to a specific target part.
    *   Trips are dedicated to one bomb type (heavy or light).
    *   Outbound fuel consumption = $\frac{\text{Distance}}{\text{Efficiency}}$, where Efficiency is 2 km/L for heavy bombs and 3 km/L for light bombs.
    *   Return fuel consumption = $\frac{\text{Distance}}{4}$ km/L (empty aircraft efficiency).
    *   Takeoff/landing overhead = 100 liters per round trip.
    *   Total fuel for $h_i$ heavy bombs to part $i$ is $h_i \times (\frac{d_i}{2} + \frac{d_i}{4} + 100)$.
    *   Total fuel for $l_i$ light bombs to part $i$ is $l_i \times (\frac{d_i}{3} + \frac{d_i}{4} + 100)$.
    *   Total Fuel = $\sum_{i=1}^{4} [ h_i (\frac{d_i}{2} + \frac{d_i}{4} + 100) + l_i (\frac{d_i}{3} + \frac{d_i}{4} + 100) ] \le 10,000$.
6.  **Distances:** $d_1=450, d_2=480, d_3=540, d_4=600$ km.
7.  **Probabilities:**
    *   Part 1: $p_{h,1}=0.03, p_{l,1}=0.08$
    *   Part 2: $p_{h,2}=0.10, p_{l,2}=0.11$
    *   Part 3: $p_{h,3}=0.05, p_{l,3}=0.12$
    *   Part 4: $p_{h,4}=0.05, p_{l,4}=0.09$

**Open Assumptions:**
None. All formulation-critical facts have been confirmed.