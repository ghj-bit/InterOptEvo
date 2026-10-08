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

QUESTION: For the mission to count as successful, must at least two of the four key parts be destroyed by the end of the entire mission (i.e., across all bombing runs combined), or must each individual bombing run destroy at least two parts?

## Turn 1 - User Simulator

The mission is successful if at least two of the four key parts are destroyed by the end of the entire mission, across all bombing runs combined.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop the entire bomb load on that target in a single run, or can it drop only part of its load and return with the rest?

## Turn 2 - User Simulator

The aircraft drops the entire bomb load on that target in a single run.

## Turn 3 - Generic Agent

QUESTION: Can the aircraft carry a mix of heavy and light bombs in a single run (e.g., 2 heavy + 1 light), or must each run carry only one type of bomb?

## Turn 3 - User Simulator

Each run must carry only one bomb.

## Turn 4 - Generic Agent

QUESTION: How many bombs can the aircraft carry in a single run — is it exactly one bomb per run (so each run delivers exactly one bomb to one target), or can it carry multiple bombs of the same type per run?

## Turn 4 - User Simulator

The aircraft can carry exactly one bomb per run.

## Turn 5 - Generic Agent

QUESTION: For the fuel calculation of a run to a target at distance d km, is the fuel consumed equal to (2d / efficiency) + 100 liters, where the 100 liters covers the takeoff and landing for that trip?

## Turn 5 - User Simulator

Yes, the fuel consumed for a run to a target at distance d km is (2d / efficiency) + 100 liters, where the 100 liters covers the takeoff and landing for that trip.

## Turn 6 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb, is the fuel efficiency 2 km per liter for the entire round trip (both outbound and return legs), or is it 2 km per liter only on the outbound leg and 4 km per liter (empty) on the return leg?

## Turn 6 - User Simulator

The fuel efficiency is 2 km per liter for the entire round trip (both outbound and return legs) when carrying a heavy bomb.

## Turn 7 - Generic Agent

QUESTION: Is the probability of destroying a key part independent of the number of bombs dropped on it, so that the probability of destruction after dropping h heavy bombs and l light bombs on part i is 1 - (1-p_hi)^h * (1-p_li)^l?

## Turn 7 - User Simulator

Yes, the probability of destroying a key part is independent of the number of bombs dropped on it, so that the probability of destruction after dropping h heavy bombs and l light bombs on part i is 1 - (1-p_hi)^h * (1-p_li)^l.

## Turn 8 - Generic Agent

QUESTION: Is the objective to maximize the probability that at least two of the four key parts are destroyed by the end of the mission?

## Turn 8 - User Simulator

Yes, the objective is to maximize the probability that at least two of the four key parts are destroyed by the end of the mission.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements I should be aware of, such as a maximum number of runs, a minimum number of runs, or any restrictions on which targets can be bombed?

## Turn 9 - User Simulator

No, there are no other constraints or requirements beyond those already stated.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed by the end of the mission.
- **Decision variables:** For each key part i (1–4), the number of heavy bombs h_i and light bombs l_i dropped on it.
- **Constraints:**
  - Total heavy bombs: Σ h_i ≤ 28
  - Total light bombs: Σ l_i ≤ 12
  - Total fuel: Σ over all runs of [(2·d_i / efficiency) + 100] ≤ 10,000 liters
    - Heavy bomb run to part i: (2·d_i / 2) + 100 = d_i + 100 liters
    - Light bomb run to part i: (2·d_i / 3) + 100 liters
  - Each run carries exactly one bomb (heavy or light) to exactly one target.
- **Destruction probability:** For part i, P(destroyed) = 1 − (1−p_hi)^{h_i} · (1−p_li)^{l_i}, with independent bomb effects.
- **Success condition:** At least 2 of the 4 parts destroyed (across all runs combined).
- **No other constraints** (no max/min runs, no target restrictions).