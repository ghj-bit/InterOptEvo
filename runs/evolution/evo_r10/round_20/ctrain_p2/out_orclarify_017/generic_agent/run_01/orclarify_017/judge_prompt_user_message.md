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

QUESTION: For each key part, is the probability that it is destroyed after dropping a set of bombs equal to 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., the bombs act as independent attempts on that part — or is it some other rule (for example, the probabilities add, or the part is destroyed only if a single bomb hits it)?

## Turn 1 - User Simulator

The bombs act as independent attempts on that part. The probability that a key part is destroyed after dropping a set of bombs is equal to 1 minus the product of (1 minus each bomb's individual destruction probability).

## Turn 2 - Generic Agent

QUESTION: When the aircraft flies to a target and back, is the fuel consumed on the outbound leg calculated with the efficiency of the bomb it is carrying, and the fuel consumed on the return leg calculated with the empty-aircraft efficiency (4 km per liter), or is the same efficiency used for both legs?

## Turn 2 - User Simulator

The fuel consumed on the outbound leg is calculated with the efficiency of the bomb it is carrying, and the fuel consumed on the return leg is calculated with the empty-aircraft efficiency (4 km per liter).

## Turn 3 - Generic Agent

QUESTION: Does the 100-liter takeoff-and-landing fuel cost apply once per round trip (i.e., once per bomb dropped, since each bomb requires its own round trip), or is it charged differently?

## Turn 3 - User Simulator

The 100-liter takeoff-and-landing fuel cost applies once per round trip.

## Turn 4 - Generic Agent

QUESTION: Can a single aircraft carry multiple bombs on one round trip and drop them all at the same target, or does each bomb require its own separate round trip (one bomb per trip)?

## Turn 4 - User Simulator

Each bomb requires its own separate round trip. Each aircraft can carry only one bomb per trip.

## Turn 5 - Generic Agent

QUESTION: Is the fuel constraint a single shared pool of 10,000 liters total across all bombing runs (all targets combined), or is there a separate fuel budget per target?

## Turn 5 - User Simulator

The fuel constraint is a single shared pool of 10,000 liters total across all bombing runs.

## Turn 6 - Generic Agent

QUESTION: Are the heavy-bomb limit (28) and light-bomb limit (12) total caps across all four targets combined, or is there a separate cap per target?

## Turn 6 - User Simulator

The heavy-bomb limit (28) and light-bomb limit (12) are total caps across all four targets combined.

## Turn 7 - Generic Agent

QUESTION: Is the objective to minimize total fuel consumption subject to the constraint that the probability of destroying at least two of the four key parts is at least some threshold, or is the objective to maximize the probability of destroying at least two of the four key parts subject to the fuel and bomb limits?

## Turn 7 - User Simulator

The objective is to maximize the probability of destroying at least two of the four key parts, subject to the fuel and bomb limits.

## Turn 8 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be integers (you can only drop whole bombs), or can they be treated as continuous values in the model?

## Turn 8 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be integers.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how many bombs can be dropped on a single key part, or can all 28 heavy and 12 light bombs be concentrated on one part if that is optimal?

## Turn 9 - User Simulator

There is no limit on how many bombs can be dropped on a single key part, other than the total caps of 28 heavy and 12 light bombs.

## Turn 10 - Generic Agent

QUESTION: For the fuel calculation, is the distance used the one-way distance from the airport to the target (so the round trip is 2 × that distance), or is the distance in the table already the round-trip distance?

## Turn 10 - User Simulator

The distance in the table is the one-way distance from the airport to the target. The round trip is 2 × that distance.

## Turn 11 - Generic Agent

QUESTION: When computing fuel for a round trip carrying a heavy bomb, is the outbound leg fuel = (one-way distance) / 2, and the return leg fuel = (one-way distance) / 4, plus the 100-liter takeoff/landing cost? In other words, for a heavy bomb to target 1 (450 km one-way), the fuel would be 450/2 + 450/4 + 100 = 225 + 112.5 + 100 = 437.5 liters?

## Turn 11 - User Simulator

Yes, that is correct. For a heavy bomb to target 1, the fuel would be 450/2 + 450/4 + 100 = 437.5 liters.

## Turn 12 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be dropped (i.e., must the mission use at least one bomb), or is it acceptable to drop zero bombs if that happens to be optimal?

## Turn 12 - User Simulator

It is acceptable to drop zero bombs if that happens to be optimal.

## Turn 13 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as a maximum number of bombing runs, a time limit, or a requirement that each key part must receive at least one bomb?

## Turn 13 - User Simulator

No, there are no other constraints or considerations.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Decision variables:**
- For each key part *i* (i = 1, 2, 3, 4), let *h_i* = number of heavy bombs dropped on part *i*, and *l_i* = number of light bombs dropped on part *i*.
- All *h_i* and *l_i* are non-negative integers.

**Objective:**
- Maximize the probability that at least 2 of the 4 key parts are destroyed.

**Destruction probability per part:**
- Part *i* is destroyed with probability *p_i* = 1 − (1 − 0.03·h_i + …) — more precisely, *p_i* = 1 − (1 − p_h_i)^{h_i} · (1 − p_l_i)^{l_i}, where *p_h_i* and *p_l_i* are the per-bomb destruction probabilities for heavy and light bombs on part *i* respectively.
- The four parts are destroyed independently.
- The probability that at least 2 of 4 parts are destroyed is computed from the joint distribution of the four independent Bernoulli outcomes.

**Constraints:**
1. Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
2. Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
3. Total fuel ≤ 10,000 liters, where fuel for each bomb is:
   - Heavy bomb to part *i*: (d_i / 2) + (d_i / 4) + 100 = (3·d_i / 4) + 100
   - Light bomb to part *i*: (d_i / 3) + (d_i / 4) + 100 = (7·d_i / 12) + 100
   - where d_i is the one-way distance to part *i* (450, 480, 540, 600 km respectively).
4. No per-part minimum or maximum bomb count beyond the global caps.
5. Zero bombs is a feasible (if suboptimal) solution.

**Distances (one-way, km):** Part 1: 450, Part 2: 480, Part 3: 540, Part 4: 600.

**Per-bomb destruction probabilities:**
| Part | Heavy | Light |
|------|-------|-------|
| 1    | 0.03  | 0.08  |
| 2    | 0.10  | 0.11  |
| 3    | 0.05  | 0.12  |
| 4    | 0.05  | 0.09  |