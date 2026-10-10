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

QUESTION: When the aircraft flies to a target carrying a bomb, does it drop that single bomb on the target and then return to the airport, meaning each bombing run uses exactly one bomb?

## Turn 2 - User Simulator

Yes, each bombing run uses exactly one bomb. The aircraft carries one bomb, drops it on the target, and returns to the airport.

## Turn 3 - Generic Agent

QUESTION: For a bombing run to a specific key part, is the fuel consumed calculated as the round-trip distance (2 times the distance to that part) multiplied by the fuel efficiency rate for the bomb type being carried, plus the 100-liter takeoff and landing cost?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Are the probabilities of destruction for each key part independent of each other, meaning the destruction of one part does not affect the probability of destroying another part?

## Turn 4 - User Simulator

I need to confirm this internally.

## Turn 5 - Generic Agent

QUESTION: If the independence of destruction probabilities across key parts is not confirmed, should I assume that the probability of destroying each key part is independent of the others, or is there a known dependency structure I should account for?

## Turn 5 - User Simulator

I need to confirm this internally.

## Turn 6 - Generic Agent

QUESTION: Should I assume that the probability of destroying each key part is independent of the others, or is there a known dependency structure I should account for?

## Turn 6 - User Simulator

I need to confirm this internally.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be integers, or can they be fractional values in the optimization model?

## Turn 7 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be integers.

## Turn 8 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing cost incurred once per round trip to a target, or is it incurred separately for each takeoff and each landing?

## Turn 8 - User Simulator

The 100-liter cost is incurred once per round trip.

## Turn 9 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs total limits for the entire mission, or are they limits per key part?

## Turn 9 - User Simulator

The 28 heavy bombs and 12 light bombs are total limits for the entire mission.

## Turn 10 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a total limit for the entire mission across all bombing runs, or is it a limit per individual bombing run?

## Turn 10 - User Simulator

The 10,000-liter fuel limit is a total limit for the entire mission across all bombing runs.

## Turn 11 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission, such as a minimum number of bombs that must be used, a requirement to visit all four key parts, or any restrictions on the order in which targets are visited?

## Turn 11 - User Simulator

No, there are no additional constraints or requirements beyond those already specified.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$, and $l_i$ be the number of light bombs assigned to key part $i$, for $i = 1, 2, 3, 4$.
3.  **Variable Domain:** $h_i$ and $l_i$ are non-negative integers.
4.  **Bomb Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs: $\sum_{i=1}^{4} l_i \le 12$.
5.  **Fuel Constraints:**
    *   Total fuel consumption $\le 10,000$ liters.
    *   Fuel for a run to part $i$ with a heavy bomb: $2 \times d_i \times (1/2) + 100 = d_i + 100$ liters (since efficiency is 2 km/L, fuel = distance / efficiency). Wait, efficiency is km per liter. So fuel = distance / efficiency.
        *   Heavy bomb run to part $i$: Distance is $2 \times d_i$ (round trip). Efficiency is 2 km/L. Fuel = $(2 \times d_i) / 2 = d_i$ liters for flight + 100 liters for takeoff/landing. Total = $d_i + 100$ liters.
        *   Light bomb run to part $i$: Distance is $2 \times d_i$. Efficiency is 3 km/L. Fuel = $(2 \times d_i) / 3$ liters for flight + 100 liters for takeoff/landing. Total = $\frac{2 d_i}{3} + 100$ liters.
    *   Total Fuel: $\sum_{i=1}^{4} h_i (d_i + 100) + \sum_{i=1}^{4} l_i (\frac{2 d_i}{3} + 100) \le 10,000$.
6.  **Probability Model:**
    *   Let $p_{hi}$ be the probability of destroying part $i$ with one heavy bomb, and $p_{li}$ be the probability with one light bomb.
    *   The probability that part $i$ is *not* destroyed by $h_i$ heavy bombs and $l_i$ light bombs is $(1 - p_{hi})^{h_i} (1 - p_{li})^{l_i}$.
    *   The probability that part $i$ *is* destroyed is $P_i = 1 - (1 - p_{hi})^{h_i} (1 - p_{li})^{l_i}$.
7.  **Success Condition:** The mission is successful if at least two parts are destroyed. The objective is to maximize the probability of this event.

**Assumptions:**
1.  **Independence:** It is assumed that the destruction of each key part is independent of the destruction of the other key parts. (This was not confirmed by the user, but is a standard assumption in such models unless dependencies are specified. The user declined to confirm or deny dependencies, so this is flagged as an assumption.)
2.  **Fuel Efficiency Application:** It is assumed that the fuel efficiency rates (2 km/L for heavy, 3 km/L for light) apply to the entire round-trip distance when carrying the respective bomb type. The 100-liter takeoff/landing cost is added per round trip.
3.  **No Empty Runs:** It is assumed that no "empty" runs (runs without a bomb) are performed, as they would consume fuel without contributing to the objective. The brief mentions empty-run efficiency, but since each run must drop a bomb to be a "bombing run," and the objective is destruction, empty runs are suboptimal and excluded.

**Model Formulation:**
Maximize $P(\text{at least 2 parts destroyed})$
Subject to:
$\sum_{i=1}^{4} h_i \le 28$
$\sum_{i=1}^{4} l_i \le 12$
$\sum_{i=1}^{4} h_i (d_i + 100) + \sum_{i=1}^{4} l_i (\frac{2 d_i}{3} + 100) \le 10,000$
$h_i, l_i \in \mathbb{Z}_{\ge 0}$ for $i=1,2,3,4$

Where $d = [450, 480, 540, 600]$.
$p_h = [0.03, 0.10, 0.05, 0.05]$.
$p_l = [0.08, 0.11, 0.12, 0.09]$.

The objective function is the sum of probabilities of all combinations where at least two parts are destroyed, calculated using the independence assumption.