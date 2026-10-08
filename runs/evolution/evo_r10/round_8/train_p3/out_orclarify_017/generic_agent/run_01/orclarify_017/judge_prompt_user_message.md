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

QUESTION: When you say the mission is successful only if at least two of the four key parts are destroyed, do you want the model to maximize the probability of achieving that success (i.e., maximize the probability that at least two parts are destroyed), or is there a different objective you have in mind?

## Turn 1 - User Simulator

Yes, the objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: For the fuel calculation, is the fuel consumed on the outbound leg (airport to target) based on the fuel efficiency of the bomb being carried, and the fuel consumed on the return leg (target to airport) based on the empty-aircraft efficiency of 4 km per liter?

## Turn 2 - User Simulator

Yes, that is correct. The outbound leg uses the fuel efficiency of the bomb being carried, and the return leg uses the empty-aircraft efficiency of 4 km per liter.

## Turn 3 - Generic Agent

QUESTION: For the probability of destroying a key part, if you assign multiple bombs to the same part, is the destruction probability calculated as 1 minus the product of (1 minus each bomb's individual probability), assuming independent destruction attempts?

## Turn 3 - User Simulator

Yes, that is correct. The destruction probability for a key part is calculated as 1 minus the product of (1 minus each bomb's individual probability), assuming independent destruction attempts.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft carry both a heavy bomb and a light bomb on the same bombing run, or does each run carry exactly one bomb (either heavy or light)?

## Turn 4 - User Simulator

Each run carries exactly one bomb, either heavy or light.

## Turn 5 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost incurred once per bombing run (i.e., once per round trip), or is it incurred separately for the takeoff and for the landing?

## Turn 5 - User Simulator

The 100-liter cost is incurred once per bombing run, meaning once per round trip.

## Turn 6 - Generic Agent

QUESTION: Can the same key part be bombed multiple times (i.e., can you assign more than one bombing run to the same part), or is each part bombed at most once?

## Turn 6 - User Simulator

Yes, the same key part can be bombed multiple times.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the number of bombing runs the aircraft can make, other than the bomb and fuel constraints?

## Turn 7 - User Simulator

No, there is no limit on the number of bombing runs other than the bomb and fuel constraints.

## Turn 8 - Generic Agent

QUESTION: When you say "the number of heavy bombs used cannot exceed 28" and "the number of light bombs used cannot exceed 12," does this mean the total number of heavy bombs assigned across all parts cannot exceed 28, and similarly for light bombs?

## Turn 8 - User Simulator

Yes, the total number of heavy bombs assigned across all parts cannot exceed 28, and the total number of light bombs assigned across all parts cannot exceed 12.

## Turn 9 - Generic Agent

QUESTION: Is the fuel constraint a single total across all bombing runs (i.e., the sum of fuel consumed by all runs must not exceed 10,000 liters), or is there a per-run fuel limit as well?

## Turn 9 - User Simulator

The fuel constraint is a single total across all bombing runs. The sum of fuel consumed by all runs must not exceed 10,000 liters.

## Turn 10 - Generic Agent

QUESTION: Are the decision variables (number of heavy bombs and light bombs assigned to each part) required to be non-negative integers, or can they be fractional?

## Turn 10 - User Simulator

The number of heavy bombs and light bombs assigned to each part must be non-negative integers.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint that the aircraft must return to the airport after each bombing run, or can it perform multiple bombing runs in a single sortie (e.g., bomb one part, then fly to another part, then return)?

## Turn 11 - User Simulator

Each bombing run is a round trip from the airport to the target and back. The aircraft must return to the airport after each bombing run.

## Turn 12 - Generic Agent

QUESTION: If a part receives both heavy and light bombs, is the destruction probability calculated by combining all bombs (heavy and light) together using the same independent formula, i.e., 1 minus the product of (1 minus each bomb's individual probability) across all bombs assigned to that part?

## Turn 12 - User Simulator

Yes, the destruction probability is calculated by combining all bombs (heavy and light) together using the same independent formula: 1 minus the product of (1 minus each bomb's individual probability) across all bombs assigned to that part.

## Turn 13 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.

**Decision Variables:**
- For each part i (i = 1, 2, 3, 4): h_i = number of heavy bombs assigned (non-negative integer), l_i = number of light bombs assigned (non-negative integer).

**Destruction Probability per Part:**
- p_i = 1 − ∏(1 − 0.03)^{h_i} × ∏(1 − 0.08)^{l_i} for part 1, and similarly for parts 2, 3, 4 using their respective probabilities.
- More generally: p_i = 1 − (1 − p_hi)^{h_i} × (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs on part i.

**Success Probability (Objective):**
- P(success) = probability that at least 2 of the 4 parts are destroyed, computed from the joint distribution of the 4 independent destruction events.

**Constraints:**
1. Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
2. Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
3. Total fuel: sum over all runs of (outbound fuel + return fuel + 100 L takeoff/landing) ≤ 10,000 L
   - Outbound fuel for a heavy bomb to part i: d_i / 2 liters (where d_i is the distance in km)
   - Outbound fuel for a light bomb to part i: d_i / 3 liters
   - Return fuel (empty): d_i / 4 liters
   - So fuel per heavy-bomb run to part i: d_i/2 + d_i/4 + 100
   - Fuel per light-bomb run to part i: d_i/3 + d_i/4 + 100
4. All variables are non-negative integers.

**Distances:** Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.

**Per-bomb destruction probabilities:**
| Part | Heavy | Light |
|------|-------|-------|
| 1    | 0.03  | 0.08  |
| 2    | 0.10  | 0.11  |
| 3    | 0.05  | 0.12  |
| 4    | 0.05  | 0.09  |

**Key structural notes:**
- Each bombing run carries exactly one bomb (heavy or light) and is a round trip.
- The same part can be bombed multiple times.
- No limit on number of runs beyond bomb and fuel constraints.
- Fuel is a single aggregate constraint across all runs.