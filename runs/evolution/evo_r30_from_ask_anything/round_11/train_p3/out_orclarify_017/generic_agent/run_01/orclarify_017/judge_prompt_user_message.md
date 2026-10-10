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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is there a different goal such as minimizing fuel used or maximizing the expected number of parts destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: For each key part, is the probability of destruction calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs assigned to that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is the correct calculation method.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb on a bombing run, is the fuel efficiency of 2 km per liter applied to the entire round trip distance (out and back), or is it applied only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 3 - User Simulator

The fuel efficiency of 2 km per liter is applied to the entire round trip distance (out and back) when carrying a heavy bomb.

## Turn 4 - Generic Agent

QUESTION: When the aircraft carries a light bomb on a bombing run, is the fuel efficiency of 3 km per liter applied to the entire round trip distance (out and back), or is it applied only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 4 - User Simulator

The fuel efficiency of 3 km per liter is applied to the entire round trip distance (out and back) when carrying a light bomb.

## Turn 5 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel consumption applied once per round trip (i.e., once per bombing run), or is it applied separately for the takeoff and for the landing?

## Turn 5 - User Simulator

The 100-liter fuel consumption is applied once per round trip (i.e., once per bombing run).

## Turn 6 - Generic Agent

QUESTION: Can a single bombing run carry both a heavy bomb and a light bomb simultaneously, or is each bombing run limited to carrying exactly one bomb (either heavy or light)?

## Turn 6 - User Simulator

Each bombing run is limited to carrying exactly one bomb, either heavy or light.

## Turn 7 - Generic Agent

QUESTION: Can the aircraft make multiple separate bombing runs to the same key part, or is each key part visited at most once during the mission?

## Turn 7 - User Simulator

The aircraft can make multiple separate bombing runs to the same key part.

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers, or can they be fractional values?

## Turn 8 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 9 - Generic Agent

QUESTION: Is there any additional requirement or constraint not yet mentioned, such as a minimum number of bombs that must be used, a requirement to visit all four key parts, or a limit on the total number of bombing runs?

## Turn 9 - User Simulator

No, there are no additional requirements or constraints beyond those already mentioned.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the probability that at least two of the four key parts are destroyed. (Confirmed)
2. **Decision Variables:** Let $h_i$ be the number of heavy bombs assigned to key part $i$ (for $i = 1, 2, 3, 4$), and $l_i$ be the number of light bombs assigned to key part $i$. (Confirmed)
3. **Variable Domain:** All $h_i$ and $l_i$ are non-negative integers. (Confirmed)
4. **Probability Calculation:** The probability that key part $i$ is destroyed is $1 - (1 - p_{hi})^{h_i} (1 - p_{li})^{l_i}$, where $p_{hi}$ and $p_{li}$ are the per-bomb destruction probabilities for heavy and light bombs respectively. (Confirmed)
5. **Success Condition:** The mission is successful if at least two of the four key parts are destroyed. The objective is to maximize the probability of this event. (Confirmed)
6. **Bomb Constraints:**
   - Total heavy bombs used: $\sum_{i=1}^{4} h_i \le 28$. (Confirmed)
   - Total light bombs used: $\sum_{i=1}^{4} l_i \le 12$. (Confirmed)
7. **Fuel Constraints:**
   - Total fuel consumption must not exceed 10,000 liters. (Confirmed)
   - Each bombing run is a round trip from the airport to the target and back. (Confirmed)
   - Each bombing run carries exactly one bomb (either heavy or light). (Confirmed)
   - Fuel efficiency for a heavy bomb run: 2 km per liter for the entire round trip. (Confirmed)
   - Fuel efficiency for a light bomb run: 3 km per liter for the entire round trip. (Confirmed)
   - Fuel efficiency for an empty aircraft: 4 km per liter. (Confirmed, but not directly used in the model since every run carries a bomb).
   - Takeoff and landing fuel consumption: 100 liters per round trip. (Confirmed)
8. **Multiple Runs to Same Part:** The aircraft can make multiple separate bombing runs to the same key part. (Confirmed)
9. **No Additional Constraints:** There are no other requirements or constraints. (Confirmed)

**Model Formulation:**

Let $d_i$ be the distance from the airport to key part $i$ (km).
- $d_1 = 450$, $d_2 = 480$, $d_3 = 540$, $d_4 = 600$.

For a heavy bomb run to part $i$:
- Round trip distance: $2d_i$ km.
- Fuel for travel: $2d_i / 2 = d_i$ liters.
- Fuel for takeoff/landing: 100 liters.
- Total fuel per heavy bomb run to part $i$: $d_i + 100$ liters.

For a light bomb run to part $i$:
- Round trip distance: $2d_i$ km.
- Fuel for travel: $2d_i / 3$ liters.
- Fuel for takeoff/landing: 100 liters.
- Total fuel per light bomb run to part $i$: $2d_i / 3 + 100$ liters.

**Fuel Constraint:**
$$ \sum_{i=1}^{4} h_i (d_i + 100) + \sum_{i=1}^{4} l_i \left(\frac{2d_i}{3} + 100\right) \le 10000 $$

**Objective Function:**
Maximize $P(\text{at least 2 parts destroyed})$, where the probability that part $i$ is destroyed is:
$$ P_i = 1 - (1 - p_{hi})^{h_i} (1 - p_{li})^{l_i} $$

The probability that at least two parts are destroyed is:
$$ \sum_{i<j} P_i P_j (1 - P_k) (1 - P_l) + \sum_{i} P_i \prod_{j \neq i} P_j $$
(where the sums are over all combinations of parts).

This is a nonlinear integer programming problem.