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

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, or is there a different optimization goal such as minimizing fuel used or maximizing the expected number of parts destroyed?

## Turn 1 - User Simulator

The mission objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each of the four key parts required to be non-negative integers, or can they be fractional values in the model?

## Turn 2 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 3 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus the product of (1 minus the per-bomb destruction probability) for each bomb assigned to that part, assuming independent bomb impacts?

## Turn 3 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus the product of (1 minus the per-bomb destruction probability) for each bomb assigned to that part, assuming independent bomb impacts?

## Turn 4 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run to a key part calculated as the sum of the fuel for the outbound leg carrying the bomb, the fuel for the return leg with the aircraft empty, plus the 100-liter takeoff and landing cost?

## Turn 5 - User Simulator

Yes.

## Turn 6 - Generic Agent

QUESTION: Is the total fuel consumption for the mission the sum of the fuel consumed by each individual bombing run to each key part?

## Turn 6 - User Simulator

Yes.

## Turn 7 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs the total available for the entire mission, meaning the sum of heavy bombs assigned to all four key parts cannot exceed 28 and the sum of light bombs assigned to all four key parts cannot exceed 12?

## Turn 7 - User Simulator

Yes.

## Turn 8 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus the product of (1 minus the per-bomb destruction probability) for each bomb assigned to that part, assuming independent bomb impacts?

## Turn 8 - User Simulator

The available business facts do not determine the answer. The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission, such as a minimum number of bombs that must be assigned to each key part, a requirement that certain key parts must be targeted, or any other operational restrictions not yet mentioned?

## Turn 9 - User Simulator

No, there are no additional constraints or requirements beyond those already mentioned.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$ ($i=1,2,3,4$), and $l_i$ be the number of light bombs assigned to key part $i$.
3.  **Variable Domain:** $h_i$ and $l_i$ are non-negative integers.
4.  **Bomb Constraints:**
    *   Total heavy bombs: $\sum_{i=1}^{4} h_i \le 28$.
    *   Total light bombs: $\sum_{i=1}^{4} l_i \le 12$.
5.  **Fuel Constraints:**
    *   Total fuel available: 10,000 liters.
    *   Fuel per run to part $i$ (round trip):
        *   Outbound (carrying bomb): Distance $d_i$ / Efficiency.
        *   Return (empty): Distance $d_i$ / 4 km/L.
        *   Takeoff/Landing: 100 liters.
        *   *Note:* The prompt specifies efficiency depends on the bomb type carried. Since a single run carries one bomb type (implied by "when carrying a heavy bomb... when carrying a light bomb"), a run to part $i$ using a heavy bomb consumes $d_i/2 + d_i/4 + 100$ liters. A run using a light bomb consumes $d_i/3 + d_i/4 + 100$ liters.
    *   Total fuel constraint: $\sum_{i=1}^{4} [ h_i \cdot (d_i/2 + d_i/4 + 100) + l_i \cdot (d_i/3 + d_i/4 + 100) ] \le 10,000$.
6.  **Distances:** $d_1=450, d_2=480, d_3=540, d_4=600$ km.
7.  **Destruction Probabilities (per bomb):**
    *   Part 1: Heavy 0.03, Light 0.08
    *   Part 2: Heavy 0.10, Light 0.11
    *   Part 3: Heavy 0.05, Light 0.12
    *   Part 4: Heavy 0.05, Light 0.09
8.  **Success Condition:** At least 2 of the 4 parts are destroyed.

**Assumptions:**
1.  **Independence of Bomb Impacts:** The probability that a specific key part $i$ is destroyed is calculated as $P_i = 1 - \prod_{j=1}^{h_i} (1 - p_{h,i}) \cdot \prod_{k=1}^{l_i} (1 - p_{l,i})$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$. This assumes each bomb's impact is an independent event.
2.  **Independence Across Parts:** The destruction of one key part is independent of the destruction of another key part. Therefore, the probability that a specific set of parts $S$ is destroyed is the product of their individual destruction probabilities.
3.  **Single Bomb per Run:** Each bombing run carries exactly one bomb (either heavy or light). The fuel calculation assumes the aircraft flies out with one bomb, drops it, and returns empty. It does not assume the aircraft can carry multiple bombs in a single run to the same target, which would change the fuel efficiency profile for the outbound leg. Given the discrete nature of "number of bombs" and the specific fuel efficiencies provided for "carrying a heavy bomb" vs "carrying a light bomb", this is the standard interpretation for such problems. If multiple bombs could be carried, the efficiency would likely be different or unspecified.
4.  **Fuel Efficiency Application:** The fuel efficiency applies to the distance traveled. The outbound leg uses the efficiency corresponding to the bomb type carried. The return leg uses the empty efficiency (4 km/L). The 100L takeoff/landing cost is added per trip.