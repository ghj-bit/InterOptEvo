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

QUESTION: When the aircraft carries a bomb to a target and drops it, does it return to the airport carrying that same bomb (so the entire round trip uses the "carrying a bomb" fuel efficiency), or does it return empty (so the outbound leg uses the carrying efficiency and the return leg uses the empty 4 km/liter efficiency)?

## Turn 1 - User Simulator

It returns empty. The outbound leg uses the carrying-bomb fuel efficiency, and the return leg uses the empty 4 km/liter efficiency.

## Turn 2 - Generic Agent

QUESTION: Does each bombing run carry exactly one bomb (one heavy or one light) to one target, or can a single run carry multiple bombs (e.g., several heavy bombs at once) to a target?

## Turn 2 - User Simulator

Each bombing run carries exactly one bomb (one heavy or one light) to one target.

## Turn 3 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel cost charged once per round trip (i.e., once per bombing run, covering both the takeoff and the landing), or is it charged separately for the takeoff and again for the landing?

## Turn 3 - User Simulator

The 100-liter cost is charged once per round trip, covering both the takeoff and the landing.

## Turn 4 - Generic Agent

QUESTION: Is the mission's objective to minimize total fuel consumption subject to the constraint that at least two of the four key parts are destroyed, or is it to maximize the probability that at least two parts are destroyed subject to the fuel and bomb limits?

## Turn 4 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed, subject to the fuel and bomb limits.

## Turn 5 - Generic Agent

QUESTION: For a given key part that receives multiple bombs, is the probability that the part is destroyed computed as 1 minus the product of (1 minus each bomb's individual destruction probability) — i.e., assuming each bomb's attempt is independent — or is there some other rule (for example, a cap, or diminishing returns) for combining multiple bombs on the same part?

## Turn 5 - User Simulator

The probability that a part is destroyed is computed as 1 minus the product of (1 minus each bomb's individual destruction probability), assuming each bomb's attempt is independent.

## Turn 6 - Generic Agent

QUESTION: Are the destruction outcomes of the four key parts independent of each other (so the probability that at least two are destroyed is computed by combining the four parts' individual destruction probabilities assuming independence), or is there any dependence between parts?

## Turn 6 - User Simulator

The destruction outcomes of the four key parts are independent of each other.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers (you can only assign whole bombs), or can they be treated as continuous values?

## Turn 7 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 8 - Generic Agent

QUESTION: Is the total fuel consumption the sum of the fuel used by all bombing runs (each run's fuel = outbound carrying leg + return empty leg + 100 liters), and must this sum be at most 10,000 liters?

## Turn 8 - User Simulator

Yes, the total fuel consumption is the sum of the fuel used by all bombing runs, and this sum must be at most 10,000 liters.

## Turn 9 - Generic Agent

QUESTION: For the fuel calculation, is the distance for a bombing run to a target simply twice the one-way distance from the airport to that target (outbound one-way distance at carrying efficiency plus return one-way distance at empty efficiency), with no additional distance or detour?

## Turn 9 - User Simulator

Yes, the distance for a bombing run to a target is simply twice the one-way distance from the airport to that target, with no additional distance or detour.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how many bombing runs can be made to the same key part (i.e., can you send multiple runs, each carrying one bomb, to the same part), or is each key part limited to at most one bombing run?

## Turn 10 - User Simulator

There is no limit on how many bombing runs can be made to the same key part.

## Turn 11 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs the total available across the entire mission (so the sum of heavy bombs assigned to all four parts must be at most 28, and the sum of light bombs assigned to all four parts must be at most 12), or are these limits per key part?

## Turn 11 - User Simulator

The 28 heavy bombs and 12 light bombs are the total available across the entire mission.

## Turn 12 - Generic Agent

QUESTION: If a key part receives zero bombs, is its probability of destruction simply 0 (i.e., it is not destroyed), and does the "at least two parts destroyed" condition count only parts that actually received at least one bomb?

## Turn 12 - User Simulator

Yes, if a key part receives zero bombs, its probability of destruction is 0. The "at least two parts destroyed" condition counts only parts that actually received at least one bomb.

## Turn 13 - Generic Agent

QUESTION: Is the fuel efficiency for the outbound leg determined solely by the type of bomb carried (heavy = 2 km/liter, light = 3 km/liter), regardless of the target, and is the return leg always at the empty efficiency of 4 km/liter?

## Turn 13 - User Simulator

Yes, the fuel efficiency for the outbound leg is determined solely by the type of bomb carried (heavy = 2 km/liter, light = 3 km/liter), and the return leg is always at the empty efficiency of 4 km/liter.

## Turn 14 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing cost the same for every bombing run regardless of the target's distance and the bomb type, or does it vary by target or bomb type?

## Turn 14 - User Simulator

The 100-liter takeoff-and-landing cost is the same for every bombing run, regardless of the target's distance and the bomb type.

## Turn 15 - Generic Agent

QUESTION: Is the probability that at least two of the four key parts are destroyed computed by summing over all pairs (and larger combinations) of parts, using the independence of parts, i.e., P(at least 2 destroyed) = 1 - P(0 destroyed) - P(exactly 1 destroyed), where each part's destruction probability is 1 minus the product of (1 minus each bomb's probability) for all bombs assigned to that part?

## Turn 15 - User Simulator

Yes, the probability that at least two of the four key parts are destroyed is computed as 1 - P(0 destroyed) - P(exactly 1 destroyed), using the independence of parts, where each part's destruction probability is 1 minus the product of (1 minus each bomb's probability) for all bombs assigned to that part.

## Turn 16 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Maximize the probability that at least two of four key parts are destroyed, subject to bomb and fuel limits.

**Decision variables:** For each key part i (i = 1, 2, 3, 4), let h_i = number of heavy bombs assigned (non-negative integer) and l_i = number of light bombs assigned (non-negative integer).

**Parameters:**
- Distances (one-way, km): d = [450, 480, 540, 600]
- Heavy bomb destruction probabilities: p_h = [0.03, 0.10, 0.05, 0.05]
- Light bomb destruction probabilities: p_l = [0.08, 0.11, 0.12, 0.09]
- Heavy bomb limit: sum(h_i) ≤ 28
- Light bomb limit: sum(l_i) ≤ 12
- Fuel limit: total ≤ 10,000 liters

**Fuel per run:**
- Heavy bomb to part i: (d_i / 2) + (d_i / 4) + 100 = 0.75·d_i + 100
- Light bomb to part i: (d_i / 3) + (d_i / 4) + 100 = (7/12)·d_i + 100

**Fuel constraint:** sum over all parts of [h_i·(0.75·d_i + 100) + l_i·((7/12)·d_i + 100)] ≤ 10,000

**Destruction probability for part i:**
- If h_i + l_i = 0: P_i = 0
- Otherwise: P_i = 1 - (1 - p_h[i])^h_i · (1 - p_l[i])^l_i

**Objective:** Maximize P(at least 2 parts destroyed) = 1 - P(0 destroyed) - P(exactly 1 destroyed), where parts are independent.

**Each run carries exactly one bomb to one target; no limit on runs per part; 100L takeoff/landing cost is per round trip.**