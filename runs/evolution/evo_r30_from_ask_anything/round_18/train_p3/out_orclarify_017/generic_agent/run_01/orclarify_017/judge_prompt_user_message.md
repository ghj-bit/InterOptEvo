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

QUESTION: Is the mission's objective to minimize the total number of bombs used (heavy plus light) subject to the constraint that the probability of destroying at least two of the four key parts is at least some threshold, or is the objective to maximize the probability of destroying at least two key parts subject to the bomb and fuel limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two key parts, subject to the bomb and fuel limits.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb on a bombing run, is the fuel efficiency of 2 km per liter applied to the entire round trip distance, or is it applied only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 2 - User Simulator

The 2 km per liter efficiency applies to the entire round trip distance.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a light bomb on a bombing run, is the fuel efficiency of 3 km per liter applied to the entire round trip distance, or is it applied only to the outbound leg while the return leg uses the empty-aircraft efficiency of 4 km per liter?

## Turn 3 - User Simulator

The 3 km per liter efficiency applies to the entire round trip distance.

## Turn 4 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost incurred once per round trip (i.e., one takeoff and one landing per bombing run), or is it incurred separately for the takeoff and for the landing, making it 200 liters per round trip?

## Turn 4 - User Simulator

The 100-liter cost is incurred once per round trip.

## Turn 5 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb on a bombing run to a specific key part, is the probability of destroying that key part calculated as 1 minus (1 minus 0.03) raised to the power of the number of heavy bombs dropped on that part, assuming each bomb's effect is independent?

## Turn 5 - User Simulator

Yes, the probability of destroying that key part is calculated as 1 minus (1 minus 0.03) raised to the power of the number of heavy bombs dropped on that part, assuming each bomb's effect is independent.

## Turn 6 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, so that the probability of destroying at least two parts is calculated by summing the probabilities of all combinations where at least two parts are destroyed?

## Turn 6 - User Simulator

Yes, the destruction events for the four key parts are independent of each other.

## Turn 7 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb simultaneously on a single bombing run, or is each bombing run restricted to carrying only one bomb (either heavy or light)?

## Turn 7 - User Simulator

Each bombing run is restricted to carrying only one bomb, either heavy or light.

## Turn 8 - Generic Agent

QUESTION: Can the aircraft make multiple separate bombing runs to the same key part, dropping one bomb per run, or is each key part limited to at most one bombing run?

## Turn 8 - User Simulator

The aircraft can make multiple separate bombing runs to the same key part, dropping one bomb per run.

## Turn 9 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers, meaning you cannot assign a fractional bomb to a target?

## Turn 9 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum number of bombs that can be dropped on any single key part, or is the only limit on bombs per part the total availability of 28 heavy and 12 light bombs?

## Turn 10 - User Simulator

The only limit on bombs per part is the total availability of 28 heavy and 12 light bombs.

## Turn 11 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as the round trip distance divided by the fuel efficiency (km per liter) plus the 100-liter takeoff and landing cost, or is there a different formula for total fuel per run?

## Turn 11 - User Simulator

Yes, the fuel consumption for a bombing run is calculated as the round trip distance divided by the fuel efficiency (km per liter) plus the 100-liter takeoff and landing cost.

## Turn 12 - Generic Agent

QUESTION: Are there any additional constraints or requirements for the mission that have not been mentioned yet, such as a minimum number of bombs that must be used, a limit on the total number of bombing runs, or any restrictions on which key parts can be targeted?

## Turn 12 - User Simulator

No, there are no additional constraints or requirements beyond those already mentioned.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the probability of destroying at least two of the four key parts.
2. **Decision Variables:** For each key part $i \in \{1, 2, 3, 4\}$, let $h_i$ be the number of heavy bombs and $l_i$ be the number of light bombs assigned to part $i$. All variables are non-negative integers.
3. **Probability Model:**
   - The probability of destroying part $i$ is $P_i = 1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs respectively.
   - The destruction events for the four parts are independent.
   - The mission success probability is the sum of probabilities of all combinations where at least two parts are destroyed.
4. **Constraints:**
   - **Heavy Bomb Limit:** $\sum_{i=1}^{4} h_i \le 28$.
   - **Light Bomb Limit:** $\sum_{i=1}^{4} l_i \le 12$.
   - **Fuel Limit:** Total fuel consumption $\le 10,000$ liters.
     - Fuel for a heavy bomb run to part $i$: $\frac{2 \times d_i}{2} + 100 = d_i + 100$ liters.
     - Fuel for a light bomb run to part $i$: $\frac{2 \times d_i}{3} + 100$ liters.
     - Total fuel: $\sum_{i=1}^{4} h_i (d_i + 100) + \sum_{i=1}^{4} l_i (\frac{2 d_i}{3} + 100) \le 10,000$.
5. **Data:**
   - Distances ($d_i$): Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.
   - Heavy bomb probabilities ($p_{h,i}$): Part 1: 0.03, Part 2: 0.10, Part 3: 0.05, Part 4: 0.05.
   - Light bomb probabilities ($p_{l,i}$): Part 1: 0.08, Part 2: 0.11, Part 3: 0.12, Part 4: 0.09.
6. **Operational Rules:**
   - Each bombing run carries exactly one bomb (heavy or light).
   - Multiple runs to the same part are allowed.
   - Fuel efficiency applies to the entire round trip distance.
   - Takeoff/landing cost is 100 liters per round trip.

**Assumptions:**
- None. All critical facts were confirmed by the user.