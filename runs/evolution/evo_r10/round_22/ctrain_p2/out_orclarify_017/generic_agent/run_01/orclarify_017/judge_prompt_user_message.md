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

QUESTION: How should the mission's success be evaluated — is the goal to maximize the probability that at least two of the four key parts are destroyed (with the bomb allocation chosen to achieve that), or is there a different objective such as minimizing fuel or bombs used subject to a required success probability?

## Turn 1 - User Simulator

The goal is to maximize the probability that at least two of the four key parts are destroyed, with the bomb allocation chosen to achieve that.

## Turn 2 - Generic Agent

QUESTION: For the "at least two of the four key parts are destroyed" condition, should I treat the destruction of the four parts as independent events (so the probability of each part being destroyed depends only on the bombs assigned to that part, and the parts' outcomes don't affect each other)?

## Turn 2 - User Simulator

Yes, treat the destruction of the four parts as independent events.

## Turn 3 - Generic Agent

QUESTION: For a given key part, if I assign it h heavy bombs and l light bombs, should the probability that part is destroyed be computed as 1 minus (1 minus 0.03 to the h power) times (1 minus 0.08 to the l power) — that is, each bomb independently has its listed per-bomb probability of destroying that part, and the part is destroyed if any one of its assigned bombs succeeds?

## Turn 3 - User Simulator

No. The probability that a part is destroyed is not computed that way. The listed probabilities are per-bomb probabilities, but the part is destroyed if the cumulative effect of all assigned bombs results in destruction. The specific formula for combining multiple bombs on a single part still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: When the aircraft flies to a target and back, does it carry the bomb for the entire round trip (so the whole 2 times distance is flown at the bomb-carrying fuel efficiency), or does it drop the bomb at the target and return empty (so the outbound leg is at the bomb-carrying efficiency and the return leg is at the empty 4 km per liter efficiency)?

## Turn 4 - User Simulator

The aircraft drops the bomb at the target and returns empty. The outbound leg is flown at the bomb-carrying fuel efficiency, and the return leg is flown at the empty 4 km per liter efficiency.

## Turn 5 - Generic Agent

QUESTION: When the aircraft carries a bomb on the outbound leg, does it carry exactly one bomb per trip (one bomb dropped per round trip), or can it carry multiple bombs in a single trip and drop them all at the target?

## Turn 5 - User Simulator

The aircraft carries exactly one bomb per trip.

## Turn 6 - Generic Agent

QUESTION: For the takeoff and landing fuel cost of 100 liters per trip, does this apply to each round trip (one takeoff plus one landing), so a single round trip to a target and back costs 100 liters for takeoff and landing combined?

## Turn 6 - User Simulator

Yes, the 100 liters applies to each round trip, covering one takeoff and one landing combined.

## Turn 7 - Generic Agent

QUESTION: Can the aircraft visit multiple targets in a single sortie (e.g., drop a bomb at part 1, then fly on to part 2 and drop another bomb, then return to the airport), or must each round trip be dedicated to exactly one target?

## Turn 7 - User Simulator

Each round trip must be dedicated to exactly one target.

## Turn 8 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs hard upper limits that do not have to be fully used (i.e., the aircraft may use fewer than 28 heavy and fewer than 12 light bombs if that yields a higher success probability), or must all available bombs be dropped?

## Turn 8 - User Simulator

The 28 heavy bombs and 12 light bombs are hard upper limits. The aircraft may use fewer than 28 heavy and fewer than 12 light bombs if that yields a higher success probability.

## Turn 9 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound that the total fuel across all round trips must not exceed, with no requirement to use all of it?

## Turn 9 - User Simulator

Yes, the 10,000-liter fuel limit is a hard upper bound that the total fuel across all round trips must not exceed, with no requirement to use all of it.

## Turn 10 - Generic Agent

QUESTION: For the fuel calculation, when the aircraft carries a heavy bomb on the outbound leg, is the fuel for that leg computed as (distance in km) divided by 2 km per liter, and for a light bomb as (distance in km) divided by 3 km per liter, with the return leg always as (distance in km) divided by 4 km per liter, plus the 100-liter takeoff and landing cost per round trip?

## Turn 10 - User Simulator

Yes, that is correct.

## Turn 11 - Generic Agent

QUESTION: Are the bomb counts assigned to each key part required to be non-negative integers (you can only assign whole bombs, and you cannot assign a fraction of a bomb to a part)?

## Turn 11 - User Simulator

Yes, the bomb counts assigned to each key part must be non-negative integers.

## Turn 12 - Generic Agent

QUESTION: Is there any restriction on how many bombs of each type can be assigned to a single key part (for example, a maximum number of heavy or light bombs per part), or can any number of bombs be concentrated on one part as long as the overall totals stay within the 28 heavy and 12 light limits?

## Turn 12 - User Simulator

There is no restriction on how many bombs of each type can be assigned to a single key part. Any number of bombs can be concentrated on one part as long as the overall totals stay within the 28 heavy and 12 light limits.

## Turn 13 - Generic Agent

QUESTION: Regarding the formula for combining multiple bombs on a single part, you mentioned it still needs internal confirmation. Could you clarify the exact formula now — for example, is it 1 minus (1 minus p) to the power of the total number of bombs, where p is the per-bomb probability, treating all bombs on that part as independent attempts?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: When the aircraft flies to a target and back, is the fuel for the outbound leg calculated using the distance from the airport to that specific target (e.g., 450 km for part 1), or is there a single fixed distance used for all targets?

## Turn 14 - User Simulator

The fuel for the outbound leg is calculated using the distance from the airport to that specific target.

## Turn 15 - Generic Agent

QUESTION: If a key part receives zero bombs of both types, is its probability of being destroyed exactly zero?

## Turn 15 - User Simulator

Yes, if a key part receives zero bombs of both types, its probability of being destroyed is exactly zero.

## Turn 16 - Generic Agent

QUESTION: For the "at least two of the four key parts are destroyed" success condition, should I compute the overall success probability by summing over all combinations of two or more parts being destroyed, using the independence assumption you confirmed earlier?

## Turn 16 - User Simulator

Yes, compute the overall success probability by summing over all combinations of two or more parts being destroyed, using the independence assumption.

## Turn 17 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the probability that at least two of the four key parts are destroyed.

**Decision variables:** For each key part i (i = 1, 2, 3, 4), assign h_i heavy bombs and l_i light bombs, where h_i and l_i are non-negative integers.

**Constraints:**
- Total heavy bombs: h_1 + h_2 + h_3 + h_4 ≤ 28
- Total light bombs: l_1 + l_2 + l_3 + l_4 ≤ 12
- Total fuel ≤ 10,000 liters

**Fuel per round trip to part i (one bomb dropped):**
- Outbound leg: distance_i / efficiency (heavy: 2 km/L, light: 3 km/L)
- Return leg: distance_i / 4 (empty, 4 km/L)
- Takeoff + landing: 100 liters
- Total fuel for one heavy-bomb trip to part i: (distance_i / 2) + (distance_i / 4) + 100
- Total fuel for one light-bomb trip to part i: (distance_i / 3) + (distance_i / 4) + 100

**Distances:** Part 1: 450 km, Part 2: 480 km, Part 3: 540 km, Part 4: 600 km.

**Per-bomb destruction probabilities:**
| Part | Heavy | Light |
|------|-------|-------|
| 1    | 0.03  | 0.08  |
| 2    | 0.10  | 0.11  |
| 3    | 0.05  | 0.12  |
| 4    | 0.05  | 0.09  |

**Part destruction probability:** The exact formula for combining multiple bombs on a single part is pending internal confirmation. The part is destroyed if the cumulative effect of all assigned bombs results in destruction. If a part receives zero bombs, its destruction probability is exactly zero.

**Success probability:** Computed by summing over all combinations of two or more parts being destroyed, treating the four parts' destruction events as independent.

**Other confirmed facts:**
- One bomb per trip; each round trip is dedicated to exactly one target.
- The aircraft drops the bomb at the target and returns empty.
- No per-part cap on bomb counts.
- Bomb and fuel limits are upper bounds (not all need to be used).