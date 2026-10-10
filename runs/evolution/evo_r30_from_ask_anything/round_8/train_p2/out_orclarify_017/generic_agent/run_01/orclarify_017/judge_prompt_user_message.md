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

QUESTION: Is the mission's objective to minimize the total fuel consumed while ensuring at least two of the four key parts are destroyed, or is it to maximize the probability of destroying at least two parts while staying within the fuel and bomb limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two of the four key parts, while staying within the fuel and bomb limits.

## Turn 2 - Generic Agent

QUESTION: When calculating the probability of destroying a specific key part, do you assume that the destruction events for each bomb dropped on that part are independent, so that the probability of at least one bomb destroying the part is calculated as 1 minus the product of the probabilities that each individual bomb fails to destroy it?

## Turn 2 - User Simulator

Yes, the destruction events for each bomb dropped on a specific key part are assumed to be independent.

## Turn 3 - Generic Agent

QUESTION: Are the destruction events for different key parts independent of each other, meaning the probability of destroying part 1 does not affect the probability of destroying part 2, part 3, or part 4?

## Turn 3 - User Simulator

Yes, the destruction events for different key parts are independent of each other.

## Turn 4 - Generic Agent

QUESTION: Does the fuel efficiency rate (2, 3, or 4 km per liter) apply to the entire round trip distance based on the heaviest bomb carried during that specific sortie, or does the fuel consumption change dynamically if the aircraft drops a bomb mid-flight and continues with a lighter load?

## Turn 4 - User Simulator

The fuel efficiency rate applies to the entire round trip distance based on the heaviest bomb carried during that specific sortie.

## Turn 5 - Generic Agent

QUESTION: Can a single aircraft sortie carry both heavy and light bombs simultaneously, or is each sortie restricted to carrying only one type of bomb (either heavy or light)?

## Turn 5 - User Simulator

Each sortie is restricted to carrying only one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: Does the 100-liter fuel consumption for takeoff and landing apply to each individual bomb dropped (i.e., one takeoff and one landing per bomb), or is it a fixed cost per mission regardless of how many bombs are dropped?

## Turn 6 - User Simulator

The 100-liter fuel consumption for takeoff and landing applies to each individual bomb dropped, meaning one takeoff and one landing per bomb.

## Turn 7 - Generic Agent

QUESTION: Is the total fuel consumption for a mission calculated as the sum of the fuel used for each individual bomb drop (including the distance-based fuel and the 100-liter takeoff/landing cost for that specific bomb), with no additional fuel required for repositioning or other operations?

## Turn 7 - User Simulator

Yes, the total fuel consumption for a mission is calculated as the sum of the fuel used for each individual bomb drop, including the distance-based fuel and the 100-liter takeoff/landing cost for that specific bomb, with no additional fuel required for repositioning or other operations.

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers?

## Turn 8 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 9 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated based on the total number of bombs (both heavy and light) dropped on that part, using the formula 1 - (1 - p_heavy)^(h_i) * (1 - p_light)^(l_i), where h_i and l_i are the counts of heavy and light bombs assigned to part i?

## Turn 9 - User Simulator

Yes, the probability of destroying a key part is calculated based on the total number of bombs (both heavy and light) dropped on that part, using the formula 1 - (1 - p_heavy)^(h_i) * (1 - p_light)^(l_i), where h_i and l_i are the counts of heavy and light bombs assigned to part i.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to part $i$ and $l_i$ be the number of light bombs assigned to part $i$, for $i = 1, 2, 3, 4$. All variables are non-negative integers.
3.  **Probability Model:**
    *   Destruction events are independent across bombs and across parts.
    *   The probability of destroying part $i$, denoted $P_i$, is $1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$.
    *   The objective is to maximize $P(\text{at least 2 parts destroyed}) = \sum_{S \subseteq \{1,2,3,4\}, |S| \ge 2} \left( \prod_{j \in S} P_j \prod_{k \notin S} (1 - P_k) \right)$.
4.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^4 h_i \le 28$.
    *   **Light Bomb Limit:** $\sum_{i=1}^4 l_i \le 12$.
    *   **Fuel Limit:** Total fuel $\le 10,000$ liters.
5.  **Fuel Calculation:**
    *   Each bomb drop is a separate sortie (one takeoff, one landing).
    *   Fuel for a heavy bomb on part $i$: $2 \times d_i + 100$ liters (where $d_i$ is the distance to part $i$).
    *   Fuel for a light bomb on part $i$: $3 \times d_i + 100$ liters.
    *   Total Fuel = $\sum_{i=1}^4 h_i (2 d_i + 100) + \sum_{i=1}^4 l_i (3 d_i + 100) \le 10,000$.
    *   Distances: $d_1=450, d_2=480, d_3=540, d_4=600$.
6.  **Probabilities:**
    *   Part 1: $p_{h,1}=0.03, p_{l,1}=0.08$
    *   Part 2: $p_{h,2}=0.10, p_{l,2}=0.11$
    *   Part 3: $p_{h,3}=0.05, p_{l,3}=0.12$
    *   Part 4: $p_{h,4}=0.05, p_{l,4}=0.09$