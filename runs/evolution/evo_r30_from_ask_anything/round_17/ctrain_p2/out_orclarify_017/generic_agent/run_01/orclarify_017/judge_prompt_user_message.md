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

QUESTION: When you say "each bombing run is a round trip from the airport to the target and back," does each run carry exactly one bomb (either one heavy or one light), or can a single run carry multiple bombs?

## Turn 2 - User Simulator

Each run carries exactly one bomb, either one heavy or one light.

## Turn 3 - Generic Agent

QUESTION: For a single bombing run carrying one bomb to a specific key part, is the fuel consumed calculated as the round-trip distance (2 × distance to that part) divided by the fuel efficiency for that bomb type, plus the 100-liter takeoff/landing cost?

## Turn 3 - User Simulator

Yes.

## Turn 4 - Generic Agent

QUESTION: When multiple bombs are dropped on the same key part, is the probability that the part is destroyed calculated as 1 minus the product of (1 minus the per-bomb probability) for each bomb dropped on that part, assuming independent destruction events?

## Turn 4 - User Simulator

Yes.

## Turn 5 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each of the four key parts required to be non-negative integers?

## Turn 5 - User Simulator

Yes.

## Turn 6 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs hard upper limits on total usage, meaning you can use fewer than the full available supply if that yields a higher probability of success?

## Turn 6 - User Simulator

Yes, they are hard upper limits. You can use fewer than the full available supply if that yields a higher probability of success.

## Turn 7 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound on total fuel consumed across all bombing runs, meaning you can use less fuel if that yields a higher probability of success?

## Turn 7 - User Simulator

Yes, the 10,000-liter fuel limit is a hard upper bound. You can use less fuel if that yields a higher probability of success.

## Turn 8 - Generic Agent

QUESTION: Are there any additional requirements or constraints on the mission that are not already stated in the brief, such as a minimum number of bombs that must be dropped on any particular key part, a requirement that all four parts must receive at least one bomb, or any other operational rules?

## Turn 8 - User Simulator

No, there are no additional requirements or constraints beyond those already stated.

## Turn 9 - Generic Agent

QUESTION: Is the 100-liter takeoff and landing fuel cost applied once per bombing run (i.e., once per round trip), or is it applied separately for the takeoff and for the landing?

## Turn 9 - User Simulator

It is applied once per bombing run (once per round trip).

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the probability that at least two of the four key parts are destroyed. (Confirmed)

2. **Decision Variables:** For each key part i (i = 1, 2, 3, 4), let h_i be the number of heavy bombs and l_i be the number of light bombs assigned to that part. (Confirmed)

3. **Variable Domain:** All h_i and l_i are non-negative integers. (Confirmed)

4. **Destruction Probability per Part:** For key part i, the probability of destruction is 1 − (1 − p_hi)^{h_i} × (1 − p_li)^{l_i}, where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs respectively, assuming independent events. (Confirmed)

5. **Success Condition:** The mission succeeds if at least two of the four parts are destroyed. The overall success probability is computed from the joint distribution of the four part-destruction events. (Confirmed)

6. **Bomb Constraints:**
   - Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28 (hard upper bound) (Confirmed)
   - Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12 (hard upper bound) (Confirmed)

7. **Fuel Constraint:** Total fuel consumed across all bombing runs ≤ 10,000 liters (hard upper bound). (Confirmed)

8. **Fuel per Run:** Each run carries exactly one bomb to one key part. Fuel for a run to key part i with a heavy bomb = (2 × d_i / 2) + 100 = d_i + 100 liters. Fuel for a run to key part i with a light bomb = (2 × d_i / 3) + 100 liters. The 100-liter takeoff/landing cost is applied once per round trip. (Confirmed)

9. **Distances:** d_1 = 450 km, d_2 = 480 km, d_3 = 540 km, d_4 = 600 km. (Confirmed)

10. **Per-Bomb Destruction Probabilities:**
    - Part 1: heavy 0.03, light 0.08
    - Part 2: heavy 0.10, light 0.11
    - Part 3: heavy 0.05, light 0.12
    - Part 4: heavy 0.05, light 0.09
    (Confirmed)

11. **No Additional Constraints:** No minimum bombs per part, no requirement to hit all parts, no other operational rules. (Confirmed)

**Open Assumptions:** None. All formulation-critical facts are confirmed.