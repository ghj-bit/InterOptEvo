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

QUESTION: Is the objective to minimize the total number of bombing runs (or total fuel consumed) subject to the constraint that the probability of destroying at least two of the four key parts is at least some target level, or is the objective to maximize the probability of destroying at least two key parts subject to the resource limits?

## Turn 1 - User Simulator

The objective is to maximize the probability of destroying at least two key parts, subject to the resource limits.

## Turn 2 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs assigned to that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is the correct calculation method.

## Turn 3 - Generic Agent

QUESTION: Is the probability of destroying at least two key parts calculated as the sum over all pairs of key parts of the probability that both are destroyed, minus the probability that three or more are destroyed (i.e., using the inclusion-exclusion principle for at least two successes), or is there a different method you prefer for combining the individual part destruction probabilities?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as the distance to the target multiplied by the fuel efficiency factor for the bomb type being carried, plus 100 liters for takeoff and landing, or is the 100 liters a separate fixed cost added to the round-trip distance fuel?

## Turn 4 - User Simulator

The 100 liters is a separate fixed cost added to the round-trip distance fuel.

## Turn 5 - Generic Agent

QUESTION: Is the fuel efficiency for a bombing run determined by the type of bomb being carried during the entire round trip, meaning if you carry a heavy bomb the entire round trip uses 2 km per liter, or does the fuel efficiency change depending on whether the aircraft is carrying or not carrying the bomb during different segments of the trip?

## Turn 5 - User Simulator

The fuel efficiency is determined by the type of bomb being carried during the entire round trip.

## Turn 6 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as (2 × distance to target) / fuel efficiency + 100 liters, where the distance is doubled for the round trip, or is it calculated as (distance to target) / fuel efficiency + 100 liters, where the distance is not doubled?

## Turn 6 - User Simulator

The fuel consumption is calculated as (2 × distance to target) / fuel efficiency + 100 liters, where the distance is doubled for the round trip.

## Turn 7 - Generic Agent

QUESTION: Can a single bombing run carry both a heavy bomb and a light bomb simultaneously, or is each bombing run limited to carrying only one bomb of a single type?

## Turn 7 - User Simulator

Each bombing run is limited to carrying only one bomb of a single type.

## Turn 8 - Generic Agent

QUESTION: Are the decision variables the number of heavy bombs assigned to each of the four key parts and the number of light bombs assigned to each of the four key parts, with the constraint that the total heavy bombs used does not exceed 28 and the total light bombs used does not exceed 12?

## Turn 8 - User Simulator

Yes, the decision variables are the number of heavy bombs assigned to each of the four key parts and the number of light bombs assigned to each of the four key parts, with the constraint that the total heavy bombs used does not exceed 28 and the total light bombs used does not exceed 12.

## Turn 9 - Generic Agent

QUESTION: Are the number of heavy bombs and light bombs assigned to each key part required to be non-negative integers, or can they be fractional values?

## Turn 9 - User Simulator

They must be non-negative integers.

## Turn 10 - Generic Agent

QUESTION: Is the fuel constraint a single total constraint where the sum of fuel consumed by all bombing runs (heavy and light, across all four key parts) must not exceed 10,000 liters, or is there a separate fuel limit for heavy bomb runs and light bomb runs?

## Turn 10 - User Simulator

It is a single total constraint where the sum of fuel consumed by all bombing runs (heavy and light, across all four key parts) must not exceed 10,000 liters.

## Turn 11 - Generic Agent

QUESTION: Are there any additional constraints or requirements not mentioned in the brief, such as minimum bomb counts per key part, restrictions on which bomb types can be used on specific key parts, or dependencies between the bombing assignments to different key parts?

## Turn 11 - User Simulator

No, there are no additional constraints or requirements beyond those mentioned in the brief.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the probability of destroying at least two of the four key parts.
2. **Decision Variables:** Non-negative integers representing the number of heavy bombs assigned to each of the four key parts (h1, h2, h3, h4) and the number of light bombs assigned to each of the four key part (l1, l2, l3, l4).
3. **Probability Calculation:** The probability of destroying key part i is 1 - (1 - p_hi)^(h_i) - (1 - p_li)^(l_i) + (1 - p_hi)^(h_i) * (1 - p_li)^(l_i), where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs respectively.
4. **Success Probability:** The probability of destroying at least two key parts is calculated using the inclusion-exclusion principle over all pairs of key parts.
5. **Bomb Constraints:**
   - Total heavy bombs used (h1 + h2 + h3 + h4) ≤ 28
   - Total light bombs used (l1 + l2 + l3 + l4) ≤ 12
6. **Fuel Constraint:** The total fuel consumed by all bombing runs must not exceed 10,000 liters.
7. **Fuel Calculation per Run:** For a bombing run to key part i carrying a heavy bomb: (2 × distance_i) / 2 + 100 liters. For a light bomb: (2 × distance_i) / 3 + 100 liters.
8. **Run Structure:** Each bombing run carries exactly one bomb of a single type (heavy or light) to one key part.
9. **Distances:** Key part 1: 450 km, Key part 2: 480 km, Key part 3: 540 km, Key part 4: 600 km.
10. **Per-Bomb Destruction Probabilities:**
    - Key part 1: Heavy 0.03, Light 0.08
    - Key part 2: Heavy 0.10, Light 0.11
    - Key part 3: Heavy 0.05, Light 0.12
    - Key part 4: Heavy 0.05, Light 0.09

**Open Assumptions:**
- The exact method for combining individual part destruction probabilities into the "at least two" success probability will use the standard inclusion-exclusion principle for at least two successes out of four independent events.