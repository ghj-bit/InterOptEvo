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

QUESTION: Is the mission objective to minimize the total fuel consumed while ensuring at least two of the four key parts are destroyed, or is it to maximize the probability of destroying at least two parts subject to the fuel and bomb limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two of the four key parts, subject to the fuel and bomb limits.

## Turn 2 - Generic Agent

QUESTION: When calculating the probability that a specific key part is destroyed, do you assume that the destruction events for each bomb dropped on that part are independent, so that the probability of the part surviving is the product of the survival probabilities of all bombs assigned to it?

## Turn 2 - User Simulator

Yes, the destruction events for each bomb dropped on a specific key part are assumed to be independent.

## Turn 3 - Generic Agent

QUESTION: Does the aircraft have to return to the airport after each individual bomb drop, or can it carry multiple bombs on a single sortie to drop them at different targets before returning?

## Turn 3 - User Simulator

The aircraft must return to the airport after each individual bomb drop. Each aircraft can carry only one bomb per trip.

## Turn 4 - Generic Agent

QUESTION: Is the fuel consumption for a trip calculated by multiplying the total round-trip distance by the fuel efficiency rate corresponding to the specific bomb carried on that trip, plus the fixed 100 liters for takeoff and landing?

## Turn 4 - User Simulator

Yes, the fuel consumption for a trip is calculated by multiplying the total round-trip distance by the fuel efficiency rate corresponding to the specific bomb carried on that trip, plus the fixed 100 liters for takeoff and landing.

## Turn 5 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each of the four key parts required to be non-negative integers?

## Turn 5 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each of the four key parts must be non-negative integers.

## Turn 6 - Generic Agent

QUESTION: Is the total fuel consumption constraint a hard limit that must not be exceeded, meaning the sum of fuel used for all trips must be less than or equal to 10,000 liters?

## Turn 6 - User Simulator

Yes, the total fuel consumption is a hard limit that must not be exceeded. The sum of fuel used for all trips must be less than or equal to 10,000 liters.

## Turn 7 - Generic Agent

QUESTION: Are the limits of 28 heavy bombs and 12 light bombs hard constraints that must not be exceeded, meaning the total number of heavy bombs used across all targets must be less than or equal to 28 and the total number of light bombs used must be less than or equal to 12?

## Turn 7 - User Simulator

Yes, the limits of 28 heavy bombs and 12 light bombs are hard constraints. The total number of heavy bombs used across all targets must be less than or equal to 28, and the total number of light bombs used must be less than or equal to 12.

## Turn 8 - Generic Agent

QUESTION: Is the "at least two of the four key parts are destroyed" condition a hard requirement for the mission to be considered successful, or is it merely a target that contributes to the probability objective?

## Turn 8 - User Simulator

The condition that at least two of the four key parts are destroyed is the definition of mission success. The objective is to maximize the probability that this condition is met.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to part $i$, and $l_i$ be the number of light bombs assigned to part $i$, for $i = 1, 2, 3, 4$. All variables are non-negative integers.
3.  **Probability Model:**
    *   Destruction events for individual bombs on a specific part are independent.
    *   Let $p_{hi}$ be the probability a heavy bomb destroys part $i$ (given in table).
    *   Let $p_{li}$ be the probability a light bomb destroys part $i$ (given in table).
    *   Probability part $i$ is destroyed: $P_i = 1 - (1 - p_{hi})^{h_i} (1 - p_{li})^{l_i}$.
    *   The objective is to maximize $P(\text{at least 2 parts destroyed}) = \sum_{S \subseteq \{1,2,3,4\}, |S| \ge 2} \left( \prod_{i \in S} P_i \prod_{j \notin S} (1 - P_j) \right)$.
4.  **Constraints:**
    *   **Heavy Bomb Limit:** $\sum_{i=1}^4 h_i \le 28$.
    *   **Light Bomb Limit:** $\sum_{i=1}^4 l_i \le 12$.
    *   **Fuel Limit:** Total fuel $\le 10,000$ liters.
5.  **Fuel Calculation:**
    *   Each bomb drop is a separate round trip.
    *   The aircraft carries only one bomb per trip.
    *   Fuel for a heavy bomb trip to part $i$: $2 \times \text{Distance}_i + 100$ liters (since efficiency is 2 km/liter, fuel = distance / efficiency? No, "2 km per liter" means 1 liter per 2 km, so fuel = distance / 2. Wait, let's re-read carefully: "fuel efficiency is 2 km per liter". This means 1 liter allows 2 km. So fuel = distance / 2. Let's verify standard interpretation. Usually "efficiency" in km/l means distance per fuel. So Fuel = Distance / Efficiency.
    *   Let's check the numbers. Distance 450 km. Efficiency 2 km/l. Fuel = 450 / 2 = 225 liters. Plus 100 for takeoff/landing. Total 325 liters.
    *   Distance 600 km. Efficiency 3 km/l (light). Fuel = 600 / 3 = 200 liters. Plus 100. Total 300 liters.
    *   This seems reasonable.
    *   Total Fuel = $\sum_{i=1}^4 [ h_i \times (\frac{2 \times D_i}{2} + 100) + l_i \times (\frac{2 \times D_i}{3} + 100) ] \le 10,000$.
    *   Simplifying:
        *   Heavy trip fuel to part $i$: $D_i + 100$.
        *   Light trip fuel to part $i$: $\frac{2 D_i}{3} + 100$.
    *   Constraint: $\sum_{i=1}^4 h_i (D_i + 100) + \sum_{i=1}^4 l_i (\frac{2 D_i}{3} + 100) \le 10,000$.

**Assumptions:**
*   None. All critical formulation details were confirmed by the user.