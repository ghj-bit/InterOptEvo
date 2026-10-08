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

QUESTION: When the aircraft carries a bomb, does it deliver that single bomb to one key part and then return to the airport (one bomb per round trip), or can it carry multiple bombs on one trip and drop them across several key parts before returning?

## Turn 1 - User Simulator

It delivers that single bomb to one key part and then returns to the airport. Each aircraft can carry only one bomb per trip.

## Turn 2 - Generic Agent

QUESTION: For a round trip to a key part at distance d km, is the fuel consumed equal to (d × 2) liters for the outbound leg with the bomb plus (d × 4) liters for the empty return leg, plus the 100-liter takeoff/landing charge — i.e., 6d + 100 liters for a heavy-bomb trip and 7d + 100 liters for a light-bomb trip?

## Turn 2 - User Simulator

That is not correct.

Fuel consumption depends on the distance traveled and the fuel efficiency for that leg.

For a round trip to a key part at distance d km:
- Outbound leg (carrying a bomb): distance is d km.
- Return leg (empty): distance is d km.
- Takeoff and landing: 100 liters per trip.

The fuel for the outbound leg is d divided by the fuel efficiency when carrying that bomb type.
The fuel for the return leg is d divided by the fuel efficiency when empty.

So, for a heavy-bomb trip:
- Outbound fuel: d / 2 liters
- Return fuel: d / 4 liters
- Takeoff/landing: 100 liters
- Total: d/2 + d/4 + 100 liters

For a light-bomb trip:
- Outbound fuel: d / 3 liters
- Return fuel: d / 4 liters
- Takeoff/landing: 100 liters
- Total: d/3 + d/4 + 100 liters

## Turn 3 - Generic Agent

QUESTION: The probabilities given (e.g., 0.03 per heavy bomb on part 1) — are these independent per-bomb destruction chances, so that dropping k bombs on a part gives a destruction probability of 1 − (1 − p)^k?

## Turn 3 - User Simulator

Yes, the probabilities are independent per-bomb destruction chances. Dropping k bombs on a part gives a destruction probability of 1 − (1 − p)^k.

## Turn 4 - Generic Agent

QUESTION: Is the mission's objective to minimize the total fuel consumed (or equivalently the number of bombing trips) subject to the constraint that the probability of destroying at least two of the four key parts is at least some required level, or is the objective to maximize the probability of destroying at least two key parts subject to the fuel, heavy-bomb, and light-bomb limits?

## Turn 4 - User Simulator

The objective is to maximize the probability of destroying at least two key parts subject to the fuel, heavy-bomb, and light-bomb limits.

## Turn 5 - Generic Agent

QUESTION: When you say "the probability of destroying at least two key parts," do you mean the probability that at least two of the four parts are each destroyed (i.e., the joint probability over the four parts' destruction events), or something else?

## Turn 5 - User Simulator

Yes, it means the probability that at least two of the four parts are each destroyed.

## Turn 6 - Generic Agent

QUESTION: Are the destruction events of the four key parts independent of each other (so the joint probability is computed by multiplying the individual parts' destruction probabilities), or is there any dependence between them?

## Turn 6 - User Simulator

The destruction events of the four key parts are independent of each other.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy bombs and light bombs allocated to each key part required to be non-negative integers (you can only drop whole bombs), and is there any limit on how many bombs can be dropped on a single key part?

## Turn 7 - User Simulator

Yes, the numbers of heavy bombs and light bombs allocated to each key part must be non-negative integers. There is no specific limit on how many bombs can be dropped on a single key part, other than the total limits of 28 heavy bombs and 12 light bombs.

## Turn 8 - Generic Agent

QUESTION: Is there any requirement that all 28 heavy bombs and 12 light bombs must be used, or is it acceptable to use fewer than the available totals as long as the fuel and bomb limits are respected?

## Turn 8 - User Simulator

It is acceptable to use fewer than the available totals. The limits are maximums, not requirements to use all of them.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize the probability that at least two of the four key parts are each destroyed, subject to resource limits.

- **Decision variables:** For each key part i (i = 1..4), choose non-negative integers h_i (heavy bombs) and l_i (light bombs) to drop on that part. There is no per-part cap beyond the global totals.

- **Destruction probability per part:** Independent per-bomb chances, so part i is destroyed with probability p_i = 1 − (1 − pH_i)^{h_i} · (1 − pL_i)^{l_i}, where pH_i and pL_i are the per-bomb probabilities from the table.

- **Objective:** The four parts' destruction events are mutually independent, so the objective is the joint probability that at least two of the four parts are destroyed (sum over all subsets of size ≥ 2 of the product of the chosen parts' destruction probabilities and the survival probabilities of the rest).

- **Resource constraints (all maximums, not requirements to use everything):**
  - Heavy bombs: Σ h_i ≤ 28
  - Light bombs: Σ l_i ≤ 12
  - Fuel: Σ over parts of [h_i·(d_i/2 + d_i/4 + 100) + l_i·(d_i/3 + d_i/4 + 100)] ≤ 10,000 liters, where d_i is the distance to part i.

- **Trip structure:** Each bomb is delivered on its own round trip (one bomb per trip): outbound leg carrying the bomb at the bomb-type efficiency (heavy 2 km/L, light 3 km/L), return leg empty at 4 km/L, plus a 100-liter takeoff/landing charge per trip.

- **Distances:** part 1 = 450 km, part 2 = 480 km, part 3 = 540 km, part 4 = 600 km.

- **Per-bomb destruction probabilities:**
  - Part 1: heavy 0.03, light 0.08
  - Part 2: heavy 0.10, light 0.11
  - Part 3: heavy 0.05, light 0.12
  - Part 4: heavy 0.05, light 0.09

- **Integrality:** All bomb counts are non-negative integers.

I will now formulate and solve this model.