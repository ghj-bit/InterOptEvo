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

QUESTION: Is the mission's goal to maximize the probability that at least two of the four key parts are destroyed, or is there a different objective such as minimizing fuel used or maximizing the expected number of parts destroyed?

## Turn 1 - User Simulator

The goal is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: When you say the number of heavy bombs used cannot exceed 28, does that mean the total number of heavy bombs allocated across all four targets must be 28 or fewer, or is 28 the total number of heavy bombs physically available to the mission?

## Turn 2 - User Simulator

28 is the total number of heavy bombs physically available to the mission.

## Turn 3 - Generic Agent

QUESTION: Is 12 the total number of light bombs physically available to the mission, meaning the total light bombs allocated across all four targets must be 12 or fewer?

## Turn 3 - User Simulator

Yes, 12 is the total number of light bombs physically available to the mission.

## Turn 4 - Generic Agent

QUESTION: For the fuel calculation, is the fuel consumed for a bombing run calculated as (distance to target × 2 for the round trip) divided by the fuel efficiency of the bomb being carried, plus the 100 liters for takeoff and landing?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: When an aircraft carries a heavy bomb to a target, does it use the heavy bomb fuel efficiency (2 km/liter) for the entire round trip, or does it use the empty aircraft efficiency (4 km/liter) for the return leg after dropping the bomb?

## Turn 5 - User Simulator

It uses the heavy bomb fuel efficiency (2 km/liter) for the entire round trip.

## Turn 6 - Generic Agent

QUESTION: Does the 100 liters for takeoff and landing apply once per aircraft sortie (one takeoff and one landing), or does it apply separately to the takeoff and to the landing?

## Turn 6 - User Simulator

It applies once per aircraft sortie, covering both the takeoff and the landing combined.

## Turn 7 - Generic Agent

QUESTION: Can a single aircraft sortie carry both a heavy bomb and a light bomb to the same target, or is each sortie limited to carrying only one bomb?

## Turn 7 - User Simulator

Each sortie is limited to carrying only one bomb.

## Turn 8 - Generic Agent

QUESTION: When calculating the probability that a key part is destroyed, do you assume that the destruction events from each bomb are independent, so that the probability of destruction from multiple bombs is calculated as 1 minus the product of the probabilities of each bomb failing to destroy it?

## Turn 8 - User Simulator

Yes, the destruction events from each bomb are assumed to be independent.

## Turn 9 - Generic Agent

QUESTION: Are the destruction events for different key parts independent of each other, meaning the probability that at least two parts are destroyed is calculated by considering all combinations of parts being destroyed or not, with each part's destruction probability being independent of the others?

## Turn 9 - User Simulator

Yes, the destruction events for different key parts are independent of each other.

## Turn 10 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers, meaning you cannot assign a fraction of a bomb to a target?

## Turn 10 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on the number of sorties an aircraft can make, or can the aircraft make as many sorties as needed as long as the total fuel consumption does not exceed 10,000 liters?

## Turn 11 - User Simulator

There is no limit on the number of sorties an aircraft can make, as long as the total fuel consumption does not exceed 10,000 liters.

## Turn 12 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard constraint that must not be exceeded, or is it a target that can be exceeded if it leads to a higher probability of mission success?

## Turn 12 - User Simulator

It is a hard constraint that must not be exceeded.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$, and $l_i$ be the number of light bombs assigned to key part $i$, for $i = 1, 2, 3, 4$. All variables are non-negative integers.
3.  **Resource Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs: $\sum_{i=1}^{4} l_i \le 12$.
    *   Total fuel: $\sum_{i=1}^{4} [ (h_i \times \text{Fuel}_{heavy, i}) + (l_i \times \text{Fuel}_{light, i}) ] \le 10,000$ liters.
4.  **Fuel Calculation per Bomb:**
    *   Each bomb requires one sortie (round trip).
    *   Fuel for a heavy bomb to target $i$: $(2 \times \text{Distance}_i) / 2 + 100$ liters.
    *   Fuel for a light bomb to target $i$: $(2 \times \text{Distance}_i) / 3 + 100$ liters.
    *   Distances: $d_1=450, d_2=480, d_3=540, d_4=600$ km.
    *   Specific fuel costs:
        *   Heavy to 1: $450 + 100 = 550$ L
        *   Heavy to 2: $480 + 100 = 580$ L
        *   Heavy to 3: $540 + 100 = 640$ L
        *   Heavy to 4: $600 + 100 = 700$ L
        *   Light to 1: $300 + 100 = 400$ L
        *   Light to 2: $320 + 100 = 420$ L
        *   Light to 3: $360 + 100 = 460$ L
        *   Light to 4: $400 + 100 = 500$ L
5.  **Probability Model:**
    *   Probability that part $i$ is destroyed: $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$.
    *   Destruction probabilities per bomb:
        *   Part 1: $p_{h,1}=0.03, p_{l,1}=0.08$
        *   Part 2: $p_{h,2}=0.10, p_{l,2}=0.11$
        *   Part 3: $p_{h,3}=0.05, p_{l,3}=0.12$
        *   Part 4: $p_{h,4}=0.05, p_{l,4}=0.09$
    *   Events are independent across parts and across bombs.
    *   Mission Success Probability: Sum of probabilities of all subsets of parts of size 2, 3, or 4 being destroyed.