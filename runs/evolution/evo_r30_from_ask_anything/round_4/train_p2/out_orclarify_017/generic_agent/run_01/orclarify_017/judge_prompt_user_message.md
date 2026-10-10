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

QUESTION: Is the mission's objective to minimize the total number of bombs used (heavy plus light) while ensuring at least two key parts are destroyed, or is it to maximize the probability that at least two key parts are destroyed subject to the resource limits?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two key parts are destroyed, subject to the resource limits.

## Turn 2 - Generic Agent

QUESTION: When calculating the probability that a specific key part is destroyed, do you assume that the destruction events for each bomb dropped on that part are independent, so that the probability of the part surviving is the product of the survival probabilities for each individual bomb?

## Turn 2 - User Simulator

Yes, the destruction events for each bomb dropped on a specific key part are assumed to be independent.

## Turn 3 - Generic Agent

QUESTION: When the aircraft travels from the airport to a target and back, does it carry the bomb for the entire round trip (consuming fuel at the loaded efficiency rate for both legs), or does it drop the bomb at the target and return empty (consuming fuel at the loaded rate for the outbound leg and the empty rate for the return leg)?

## Turn 3 - User Simulator

The aircraft drops the bomb at the target and returns empty. It consumes fuel at the loaded efficiency rate for the outbound leg and the empty efficiency rate for the return leg.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb simultaneously on a single trip to a target, or is it limited to carrying only one bomb (either heavy or light) per trip?

## Turn 4 - User Simulator

The aircraft is limited to carrying only one bomb per trip.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft visit multiple different key parts in a single sortie (e.g., drop a bomb on Part 1, then fly to Part 2 and drop another bomb, then return to the airport), or must each trip be dedicated to exactly one key part?

## Turn 5 - User Simulator

Each trip must be dedicated to exactly one key part.

## Turn 6 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers, meaning you cannot assign a fractional bomb to a target?

## Turn 6 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 7 - Generic Agent

QUESTION: Is the 100-liter fuel consumption for takeoff and landing applied once per round trip (i.e., 100 liters total for the takeoff at the start and the landing at the end of the mission to that target), or is it applied separately for each takeoff and each landing (i.e., 100 liters for takeoff plus 100 liters for landing, totaling 200 liters per round trip)?

## Turn 7 - User Simulator

The 100 liters is applied once per round trip, meaning 100 liters total for the takeoff and landing combined.

## Turn 8 - Generic Agent

QUESTION: When calculating the fuel consumption for a trip to a specific key part, is the distance used for the fuel calculation the one-way distance from the airport to that part (which is then doubled for the round trip distance), or is there a different distance metric provided for the round trip?

## Turn 8 - User Simulator

The distance used is the one-way distance from the airport to that part, which is doubled for the round trip distance.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective**: Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables**: Let $h_i$ be the number of heavy bombs assigned to part $i$, and $l_i$ be the number of light bombs assigned to part $i$, for $i \in \{1, 2, 3, 4\}$. All variables are non-negative integers.
3.  **Probability Model**:
    *   Destruction events for individual bombs on a specific part are independent.
    *   The probability that part $i$ is destroyed is $1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$, respectively.
    *   The overall objective is to maximize the probability that the sum of indicators for destroyed parts is $\ge 2$.
4.  **Resource Constraints**:
    *   **Heavy Bombs**: $\sum_{i=1}^4 h_i \le 28$.
    *   **Light Bombs**: $\sum_{i=1}^4 l_i \le 12$.
    *   **Fuel**: Total fuel consumption $\le 10,000$ liters.
5.  **Fuel Calculation**:
    *   Each trip is dedicated to exactly one key part.
    *   The aircraft carries one bomb (heavy or light) on the outbound leg and returns empty.
    *   Outbound fuel = $\frac{\text{Distance}_i}{\text{Efficiency}_{\text{loaded}}}$.
    *   Return fuel = $\frac{\text{Distance}_i}{\text{Efficiency}_{\text{empty}}}$.
    *   Takeoff/Landing fuel = 100 liters per round trip.
    *   Total fuel for one trip to part $i$ with a heavy bomb = $\frac{d_i}{2} + \frac{d_i}{4} + 100$.
    *   Total fuel for one trip to part $i$ with a light bomb = $\frac{d_i}{3} + \frac{d_i}{4} + 100$.
    *   Total fuel constraint: $\sum_{i=1}^4 \left( h_i \left(\frac{d_i}{2} + \frac{d_i}{4} + 100\right) + l_i \left(\frac{d_i}{3} + \frac{d_i}{4} + 100\right) \right) \le 10,000$.
6.  **Distances**:
    *   $d_1 = 450$ km
    *   $d_2 = 480$ km
    *   $d_3 = 540$ km
    *   $d_4 = 600$ km
7.  **Probabilities**:
    *   Part 1: $p_{h,1}=0.03, p_{l,1}=0.08$
    *   Part 2: $p_{h,2}=0.10, p_{l,2}=0.11$
    *   Part 3: $p_{h,3}=0.05, p_{l,3}=0.12$
    *   Part 4: $p_{h,4}=0.05, p_{l,4}=0.09$