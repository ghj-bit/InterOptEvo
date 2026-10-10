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

QUESTION: For each key part, is the probability of destruction calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs assigned to that part, assuming each bomb's effect is independent?

## Turn 2 - User Simulator

Yes, that is correct.

## Turn 3 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated by summing the fuel for the outbound leg (carrying the bomb), the return leg (empty), and the takeoff/landing cost, where the outbound fuel equals the distance divided by the efficiency for the bomb type carried?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft make multiple separate trips to the same key part, or is each key part visited at most once during the mission?

## Turn 4 - User Simulator

The aircraft can make multiple separate trips to the same key part.

## Turn 5 - Generic Agent

QUESTION: When the aircraft makes a trip to a key part, does it carry exactly one bomb (either heavy or light) per trip, or can it carry multiple bombs of the same or different types on a single trip?

## Turn 5 - User Simulator

The aircraft carries exactly one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: Are the number of heavy bombs assigned to each key part and the number of light bombs assigned to each key part required to be non-negative integers?

## Turn 6 - User Simulator

Yes, the number of heavy bombs and light bombs assigned to each key part must be non-negative integers.

## Turn 7 - Generic Agent

QUESTION: Is the total fuel consumption constraint a hard ceiling that must not be exceeded, meaning the sum of fuel for all trips plus all takeoff/landing costs must be less than or equal to 10,000 liters?

## Turn 7 - User Simulator

Yes, the total fuel consumption must not exceed 10,000 liters.

## Turn 8 - Generic Agent

QUESTION: Are the bomb availability limits (28 heavy, 12 light) hard ceilings on the total number of bombs used across all key parts, meaning the sum of heavy bombs assigned to all parts must be at most 28 and the sum of light bombs assigned to all parts must be at most 12?

## Turn 8 - User Simulator

Yes, the total number of heavy bombs used across all key parts must be at most 28, and the total number of light bombs used across all key parts must be at most 12.

## Turn 9 - Generic Agent

QUESTION: Is the probability of destroying at least two key parts calculated as the sum over all pairs of key parts of the probability that both parts in the pair are destroyed, minus the sum over all triples of the probability that all three parts in the triple are destroyed, plus the probability that all four parts are destroyed, using the inclusion-exclusion principle?

## Turn 9 - User Simulator

Yes, that is correct.

## Turn 10 - Generic Agent

QUESTION: Is the takeoff and landing fuel cost of 100 liters applied once per trip (i.e., once per round trip to a key part), or is it applied separately for the takeoff and for the landing?

## Turn 10 - User Simulator

The 100 liters is applied once per trip (once per round trip to a key part).

## Turn 11 - Generic Agent

QUESTION: Is the fuel efficiency for the outbound leg determined solely by the type of bomb carried (2 km/liter for heavy, 3 km/liter for light), regardless of the number of bombs or other payload?

## Turn 11 - User Simulator

Yes, the fuel efficiency for the outbound leg is determined solely by the type of bomb carried: 2 km/liter for heavy and 3 km/liter for light.

## Turn 12 - Generic Agent

QUESTION: Is the fuel efficiency for the return leg always 4 km/liter (empty aircraft), regardless of which key part was visited or what bomb was carried on the outbound leg?

## Turn 12 - User Simulator

Yes, the fuel efficiency for the return leg is always 4 km/liter.

## Turn 13 - Generic Agent

QUESTION: Are there any additional constraints or requirements beyond the bomb limits, fuel limit, and the objective of maximizing the probability of destroying at least two key parts?

## Turn 13 - User Simulator

No, there are no additional constraints or requirements beyond the bomb limits, fuel limit, and the objective of maximizing the probability of destroying at least two key parts.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the probability of destroying at least two of the four key parts. (Confirmed)

2. **Decision Variables:** For each key part i (i = 1, 2, 3, 4), let h_i be the number of heavy bombs assigned and l_i be the number of light bombs assigned. All h_i and l_i are non-negative integers. (Confirmed)

3. **Probability Model:** The probability that key part i is destroyed is 1 - (1 - p_hi)^(h_i) * (1 - p_li)^(l_i), where p_hi and p_li are the per-bomb destruction probabilities for heavy and light bombs respectively. The probability of destroying at least two parts is computed via inclusion-exclusion over all pairs, triples, and the quadruple of parts. (Confirmed)

4. **Bomb Constraints:**
   - Sum of h_i over all i ≤ 28 (hard ceiling). (Confirmed)
   - Sum of l_i over all i ≤ 12 (hard ceiling). (Confirmed)

5. **Fuel Model:** Each trip to key part i (one bomb per trip) consumes:
   - Outbound: distance_i / efficiency_outbound, where efficiency is 2 km/liter for heavy bombs and 3 km/liter for light bombs.
   - Return: distance_i / 4 km/liter (empty aircraft).
   - Takeoff/landing: 100 liters per trip.
   - Total fuel for a heavy-bomb trip to part i: distance_i/2 + distance_i/4 + 100.
   - Total fuel for a light-bomb trip to part i: distance_i/3 + distance_i/4 + 100.

6. **Fuel Constraint:** The sum of fuel consumed over all trips (h_i trips with heavy bombs and l_i trips with light bombs for each part i) must be ≤ 10,000 liters. (Confirmed)

7. **Trip Structure:** Each bomb is delivered on a separate round trip. The aircraft can make multiple trips to the same key part. (Confirmed)

8. **No Additional Constraints:** No other requirements exist beyond those listed. (Confirmed)

**Open Assumptions:** None. All formulation-critical facts have been confirmed.