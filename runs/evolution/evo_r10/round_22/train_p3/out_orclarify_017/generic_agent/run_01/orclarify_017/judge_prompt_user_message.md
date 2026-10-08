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

QUESTION: Does the mission objective require maximizing the probability that at least two of the four key parts are destroyed, or is there a different objective (such as minimizing fuel used or maximizing expected number of parts destroyed)?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop that bomb on that target and then return to the airport empty, meaning each bomb requires its own separate round-trip flight?

## Turn 2 - User Simulator

Yes, each bomb requires its own separate round-trip flight.

## Turn 3 - Generic Agent

QUESTION: For a single round-trip flight carrying one bomb to a target at distance d km, is the fuel consumed equal to (d / efficiency_with_bomb) + (d / efficiency_empty) + 100, i.e., the outbound leg uses the bomb-carrying efficiency, the return leg uses the empty efficiency, and the 100-liter takeoff/landing charge is added once per trip?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Are the destruction events for the four key parts independent of each other, so that the probability at least two are destroyed is computed from the individual per-part destruction probabilities assuming independence?

## Turn 4 - User Simulator

I need to confirm that point internally.

## Turn 5 - Generic Agent

QUESTION: For a given key part, if you assign it multiple bombs, is the probability that the part is destroyed equal to 1 minus the product of (1 minus each bomb's individual destruction probability), i.e., the individual bomb hits are independent?

## Turn 5 - User Simulator

I need to confirm that point internally.

## Turn 6 - Generic Agent

QUESTION: Can a single key part be assigned both heavy and light bombs, or is each key part assigned only one bomb type?

## Turn 6 - User Simulator

A single key part can be assigned both heavy and light bombs.

## Turn 7 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs hard upper bounds that you may use fewer of, or must all of them be used?

## Turn 7 - User Simulator

They are hard upper bounds; you may use fewer.

## Turn 8 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound that must not be exceeded, with no requirement to use all of it?

## Turn 8 - User Simulator

Yes, it is a hard upper bound that must not be exceeded, with no requirement to use all of it.

## Turn 9 - Generic Agent

QUESTION: Are the numbers of bombs assigned to each key part required to be whole numbers (you cannot split a bomb), which I would assume yes?

## Turn 9 - User Simulator

Yes, the numbers of bombs assigned to each key part must be whole numbers.

## Turn 10 - Generic Agent

QUESTION: Regarding the independence of destruction events, which I asked about twice and you deferred: should I proceed assuming that all bomb hits are mutually independent (both across different key parts and across multiple bombs on the same part), so that each part's destruction probability is 1 minus the product of (1 minus each assigned bomb's probability)?

## Turn 10 - User Simulator

I need to confirm that point internally.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how many bombs can be assigned to a single key part, other than the total bomb and fuel constraints?

## Turn 11 - User Simulator

No, there is no limit on how many bombs can be assigned to a single key part, other than the total bomb and fuel constraints.

## Turn 12 - Generic Agent

QUESTION: For the fuel calculation, is the 100-liter takeoff/landing charge applied once per round-trip flight (i.e., once per bomb dropped), not once per leg?

## Turn 12 - User Simulator

Yes, the 100-liter takeoff/landing charge is applied once per round-trip flight.

## Turn 13 - Generic Agent

QUESTION: If a key part receives zero bombs, is its destruction probability simply zero, and it counts as not destroyed for the "at least two destroyed" success condition?

## Turn 13 - User Simulator

Yes, if a key part receives zero bombs, its destruction probability is zero, and it counts as not destroyed for the success condition.

## Turn 14 - Generic Agent

QUESTION: Is the success condition "at least two of the four key parts are destroyed" evaluated based on the expected/average outcome (i.e., we maximize the probability of this event), rather than requiring it to be guaranteed with certainty?

## Turn 14 - User Simulator

Yes, the success condition is evaluated probabilistically; we maximize the probability that at least two of the four key parts are destroyed.

## Turn 15 - Generic Agent

QUESTION: Regarding the independence assumption, which you have deferred three times: should I proceed with the standard assumption that all bomb hits are mutually independent (across parts and across bombs on the same part), so each part's destruction probability is 1 minus the product of (1 minus each assigned bomb's probability), and the four parts' destruction events are also independent of each other?

## Turn 15 - User Simulator

I need to confirm that point internally.

## Turn 16 - Generic Agent

QUESTION: Is there any other constraint or business rule I have not yet covered that would affect the model, such as a minimum number of bombs per part, a maximum number of flights, or a requirement to visit parts in a specific order?

## Turn 16 - User Simulator

No, there are no other constraints or business rules beyond those already covered.

## Turn 17 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize the probability that at least two of the four key parts are destroyed.

**Decision variables:** For each key part i (i = 1, 2, 3, 4), let h_i = number of heavy bombs assigned (non-negative integer) and l_i = number of light bombs assigned (non-negative integer).

**Constraints:**
- Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
- Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
- Total fuel ≤ 10,000 liters
- All variables are non-negative integers

**Fuel per bomb:**
- Each bomb requires one round-trip flight.
- Heavy bomb to part i at distance d_i: fuel = d_i/2 + d_i/4 + 100 = 0.75·d_i + 100
- Light bomb to part i at distance d_i: fuel = d_i/3 + d_i/4 + 100 = (7/12)·d_i + 100
- Total fuel = Σ_i [h_i·(0.75·d_i + 100) + l_i·((7/12)·d_i + 100)] ≤ 10,000

**Distances:** d_1 = 450, d_2 = 480, d_3 = 540, d_4 = 600 km.

**Destruction probabilities (per bomb):**
- Part 1: heavy 0.03, light 0.08
- Part 2: heavy 0.10, light 0.11
- Part 3: heavy 0.05, light 0.12
- Part 4: heavy 0.05, light 0.09

**Probability model (assumed independence, pending client confirmation):**
- Part i destruction probability: p_i = 1 − (1 − p_h_i)^{h_i} · (1 − p_l_i)^{l_i}
- Probability at least two parts destroyed: sum over all pairs, triples, and the quadruple of the joint probabilities, computed under mutual independence of the four parts' destruction events.

**Notes:**
- A part with zero bombs has destruction probability 0.
- No per-part cap on bombs beyond the global constraints.
- Bomb counts are integers; fractional bombs not allowed.
- The independence assumption was deferred by the client four times; I will proceed with it as the standard modeling assumption and flag it in the final solution.