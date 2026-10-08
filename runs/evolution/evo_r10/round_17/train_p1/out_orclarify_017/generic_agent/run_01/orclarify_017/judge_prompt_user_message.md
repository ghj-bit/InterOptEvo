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

QUESTION: For a bombing run to a target at distance d km, is the fuel consumed equal to (d / 2) liters for the outbound leg carrying the bomb, plus (d / 4) liters for the empty return leg, plus 100 liters for the takeoff-and-landing overhead — i.e., 1.5d + 100 for a heavy bomb and 1.333d + 100 for a light bomb?

## Turn 1 - User Simulator

No, that is not correct.

The fuel consumption for a bombing run to a target at distance *d* km is calculated as follows:

1.  **Outbound leg (carrying bomb):** The aircraft travels distance *d* with a fuel efficiency of 2 km/liter (heavy) or 3 km/liter (light).
    *   Heavy bomb fuel: *d* / 2 liters
    *   Light bomb fuel: *d* / 3 liters
2.  **Return leg (empty):** The aircraft travels distance *d* with a fuel efficiency of 4 km/liter.
    *   Empty return fuel: *d* / 4 liters
3.  **Takeoff and landing overhead:** 100 liters per trip.

Therefore, the total fuel consumption is:
*   **Heavy bomb:** (*d* / 2) + (*d* / 4) + 100 = **0.75d + 100** liters
*   **Light bomb:** (*d* / 3) + (*d* / 4) + 100 = **0.5833d + 100** liters

Your proposed formula of 1.5d + 100 for heavy bombs and 1.333d + 100 for light bombs is incorrect.

## Turn 2 - Generic Agent

QUESTION: When the aircraft drops a bomb on a key part, does that part's destruction probability depend only on the total number of bombs dropped on it (with each bomb acting independently), so that the probability the part survives after h heavy and l light bombs is (1-p_h)^h × (1-p_l)^l?

## Turn 2 - User Simulator

Yes, that is correct. The destruction probability for a key part depends only on the total number of heavy and light bombs dropped on it, with each bomb acting independently. The probability that the part survives after *h* heavy bombs and *l* light bombs is (1 - p_h)^h × (1 - p_l)^l, where p_h is the probability of destruction per heavy bomb and p_l is the probability of destruction per light bomb for that specific key part.

## Turn 3 - Generic Agent

QUESTION: Is the mission's success probability the probability that at least two of the four key parts are destroyed, where the destruction of different key parts is independent of each other?

## Turn 3 - User Simulator

Yes, the mission's success probability is the probability that at least two of the four key parts are destroyed, and the destruction of different key parts is independent of each other.

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits?

## Turn 4 - User Simulator

Yes, the objective is to maximize the probability that at least two of the four key parts are destroyed, subject to the bomb and fuel limits.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft make multiple separate trips to the same key part (dropping one bomb per trip), or must all bombs for a given part be delivered in a single trip?

## Turn 5 - User Simulator

The aircraft can make multiple separate trips to the same key part, dropping one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: Is each trip limited to carrying exactly one bomb (either one heavy or one light), so that a trip to part i costs 0.75d_i + 100 if it carries a heavy bomb and 0.5833d_i + 100 if it carries a light bomb?

## Turn 6 - User Simulator

Yes, each trip is limited to carrying exactly one bomb (either one heavy or one light). A trip to part *i* costs 0.75d_i + 100 liters if it carries a heavy bomb and 0.5833d_i + 100 liters if it carries a light bomb.

## Turn 7 - Generic Agent

QUESTION: Are the 28 heavy and 12 light bombs hard upper bounds (you may use fewer), and is the 10,000-liter fuel limit also a hard upper bound (you may use less fuel)?

## Turn 7 - User Simulator

Yes, the 28 heavy and 12 light bombs are hard upper bounds (you may use fewer), and the 10,000-liter fuel limit is also a hard upper bound (you may use less fuel).

## Turn 8 - Generic Agent

QUESTION: Is it allowed to drop zero bombs on a key part (leaving it untouched), and is it allowed to use fewer than all available bombs overall?

## Turn 8 - User Simulator

Yes, it is allowed to drop zero bombs on a key part, and it is allowed to use fewer than all available bombs overall.

## Turn 9 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each part required to be non-negative integers (you cannot drop a fraction of a bomb)?

## Turn 9 - User Simulator

Yes, the numbers of heavy and light bombs assigned to each part must be non-negative integers.

## Turn 10 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing overhead charged once per trip (i.e., once per bomb dropped), so that dropping h heavy and l light bombs on part i incurs (h + l) × 100 liters of overhead in total?

## Turn 10 - User Simulator

Yes, the 100-liter takeoff-and-landing overhead is charged once per trip (i.e., once per bomb dropped), so that dropping *h* heavy and *l* light bombs on part *i* incurs (*h* + *l*) × 100 liters of overhead in total.

## Turn 11 - Generic Agent

QUESTION: Is the fuel consumed by a trip to part i carrying a heavy bomb exactly 0.75 × d_i + 100 liters, and carrying a light bomb exactly (5/6) × d_i + 100 liters, where d_i is the one-way distance to part i?

## Turn 11 - User Simulator

Yes, the fuel consumed by a trip to part *i* carrying a heavy bomb is exactly 0.75 × d_i + 100 liters, and carrying a light bomb is exactly (5/6) × d_i + 100 liters, where d_i is the one-way distance to part *i*.

## Turn 12 - Generic Agent

QUESTION: Is the success probability computed by summing over all subsets of key parts of size 2, 3, or 4, using the product of each part's destruction probability (for parts in the subset) and survival probability (for parts not in the subset), given the independence of parts?

## Turn 12 - User Simulator

Yes, the success probability is computed by summing over all subsets of key parts of size 2, 3, or 4, using the product of each part's destruction probability (for parts in the subset) and survival probability (for parts not in the subset), given the independence of parts.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Decision variables:** For each key part i ∈ {1,2,3,4}, two non-negative integer variables: h_i = number of heavy bombs dropped on part i, and l_i = number of light bombs dropped on part i.

**Objective:** Maximize the probability that at least two of the four key parts are destroyed.

**Destruction probability per part:** Part i is destroyed with probability
p_i(h_i, l_i) = 1 − (1 − p_h_i)^{h_i} × (1 − p_l_i)^{l_i},
where p_h_i and p_l_i are the per-bomb destruction probabilities for part i (from the table). Destruction of different parts is independent.

**Success probability:** Sum over all subsets S of {1,2,3,4} with |S| ≥ 2 of [∏_{i∈S} p_i × ∏_{i∉S} (1 − p_i)].

**Constraints:**
- Heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28.
- Light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12.
- Fuel: Σ_i [h_i × (0.75 d_i + 100) + l_i × ((5/6) d_i + 100)] ≤ 10,000, where d = (450, 480, 540, 600) km.
- All h_i, l_i are non-negative integers.

**Per-trip fuel:** Each bomb dropped requires one round-trip trip; a heavy-bomb trip to part i costs 0.75 d_i + 100 liters, a light-bomb trip costs (5/6) d_i + 100 liters. The 100-liter overhead is per trip (per bomb).

**Data:**
| Part | d (km) | p_h | p_l |
|------|--------|-----|-----|
| 1 | 450 | 0.03 | 0.08 |
| 2 | 480 | 0.10 | 0.11 |
| 3 | 540 | 0.05 | 0.12 |
| 4 | 600 | 0.05 | 0.09 |

All limits are hard upper bounds; using fewer bombs or less fuel is allowed; zero bombs on a part is allowed.