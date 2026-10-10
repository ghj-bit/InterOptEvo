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

QUESTION: Is the objective to minimize the total number of bombing runs (or total fuel consumed) subject to the constraint that the probability of destroying at least two of the four key parts is at least some threshold, or is the objective to maximize the probability of destroying at least two key parts subject to the bomb and fuel limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two key parts, subject to the bomb and fuel limits.

## Turn 2 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs of that type assigned to that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is the correct calculation method.

## Turn 3 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, so that the probability of destroying at least two parts is computed by summing the probabilities of all combinations of two or more parts being destroyed?

## Turn 3 - User Simulator

Yes, the destruction events for the four key parts are independent of each other.

## Turn 4 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run to a specific key part calculated as the round-trip distance to that part multiplied by the fuel efficiency corresponding to the bomb type carried, plus the 100-liter takeoff and landing cost?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

QUESTION: When the aircraft flies to a key part carrying a heavy bomb, is the fuel efficiency for the entire round trip (both outbound and return) 2 km per liter, or is the return leg calculated at the empty-aircraft efficiency of 4 km per liter?

## Turn 5 - User Simulator

The fuel efficiency for the entire round trip is 2 km per liter when carrying a heavy bomb.

## Turn 6 - Generic Agent

QUESTION: Can a single bombing run carry both a heavy bomb and a light bomb to the same key part, or is each run limited to carrying exactly one bomb of one type?

## Turn 6 - User Simulator

Each run is limited to carrying exactly one bomb of one type.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers?

## Turn 7 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 8 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing cost incurred once per bombing run, regardless of which key part is targeted?

## Turn 8 - User Simulator

Yes, the 100-liter takeoff and landing cost is incurred once per bombing run, regardless of which key part is targeted.

## Turn 9 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be assigned to each key part, or is it permissible to assign zero bombs to a key part?

## Turn 9 - User Simulator

It is permissible to assign zero bombs to a key part.

## Turn 10 - Generic Agent

QUESTION: Is the total fuel consumption constraint a hard ceiling of 10,000 liters, meaning the sum of fuel used across all bombing runs must be less than or equal to 10,000 liters?

## Turn 10 - User Simulator

Yes, the total fuel consumption must not exceed 10,000 liters.

## Turn 11 - Generic Agent

QUESTION: Are the heavy bomb limit of 28 and the light bomb limit of 12 hard ceilings, meaning the total number of heavy bombs used across all key parts must be less than or equal to 28, and the total number of light bombs used across all key parts must be less than or equal to 12?

## Turn 11 - User Simulator

Yes, the total number of heavy bombs used must be less than or equal to 28, and the total number of light bombs used must be less than or equal to 12.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the probability that at least two of the four key parts are destroyed. (Confirmed)

2. **Decision Variables:** For each key part $i \in \{1, 2, 3, 4\}$, let $h_i$ be the number of heavy bombs assigned and $l_i$ be the number of light bombs assigned. (Confirmed)

3. **Variable Domain:** All $h_i$ and $l_i$ are non-negative integers. (Confirmed)

4. **Probability Calculation:**
   - The probability that key part $i$ is destroyed is $1 - (1 - p_{h,i})^{h_i} (1 - p_{l,i})^{l_i}$, where $p_{h,i}$ and $p_{l,i}$ are the per-bomb destruction probabilities for heavy and light bombs on part $i$, respectively. (Confirmed)
   - The destruction events for the four key parts are independent. (Confirmed)
   - The objective value is the sum of probabilities of all combinations of 2, 3, or 4 parts being destroyed. (Confirmed)

5. **Constraints:**
   - **Heavy Bomb Limit:** $\sum_{i=1}^{4} h_i \leq 28$. (Confirmed)
   - **Light Bomb Limit:** $\sum_{i=1}^{4} l_i \leq 12$. (Confirmed)
   - **Fuel Limit:** Total fuel consumption $\leq 10,000$ liters. (Confirmed)
   - **Fuel Calculation per Run:**
     - A run to part $i$ carrying a heavy bomb consumes $\frac{2 \times d_i}{2} + 100 = d_i + 100$ liters, where $d_i$ is the distance to part $i$. (Confirmed)
     - A run to part $i$ carrying a light bomb consumes $\frac{2 \times d_i}{3} + 100$ liters. (Confirmed)
     - The fuel efficiency applies to the entire round trip. (Confirmed)
     - The 100-liter takeoff/landing cost is incurred once per run. (Confirmed)
   - **Run Structure:** Each run carries exactly one bomb of one type to one key part. (Confirmed)
   - **Zero Assignment:** It is permissible to assign zero bombs to any key part. (Confirmed)

6. **Data:**
   - Distances: $d_1=450, d_2=480, d_3=540, d_4=600$ km. (Confirmed)
   - Heavy bomb probabilities: $p_{h,1}=0.03, p_{h,2}=0.10, p_{h,3}=0.05, p_{h,4}=0.05$. (Confirmed)
   - Light bomb probabilities: $p_{l,1}=0.08, p_{l,2}=0.11, p_{l,3}=0.12, p_{l,4}=0.09$. (Confirmed)
   - Fuel efficiencies: Heavy=2 km/L, Light=3 km/L, Empty=4 km/L. (Confirmed)
   - Takeoff/landing cost: 100 L per run. (Confirmed)

**Open Assumptions:** None. All formulation-critical facts have been confirmed.