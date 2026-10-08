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

QUESTION: For each key part, is the probability of destruction per bomb independent across bombs (so that dropping multiple bombs on the same part compounds the destruction probability), or does each part require a fixed number of bombs to be destroyed?

## Turn 1 - User Simulator

The probability of destruction per bomb is independent across bombs. Dropping multiple bombs on the same key part compounds the destruction probability.

## Turn 2 - Generic Agent

QUESTION: Is the mission objective to maximize the probability that at least two of the four key parts are destroyed, or is there a different objective (such as minimizing fuel or bomb usage subject to a minimum success probability)?

## Turn 2 - User Simulator

The mission objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 3 - Generic Agent

QUESTION: Does each bomb dropped on a key part require a separate bombing run (one round trip per bomb), or can the aircraft carry multiple bombs in a single run and drop them all on the same target?

## Turn 3 - User Simulator

Each bomb dropped on a key part requires a separate bombing run. The aircraft can carry only one bomb per trip.

## Turn 4 - Generic Agent

QUESTION: For a bombing run carrying a heavy bomb, is the fuel efficiency of 2 km per liter applied to the entire round trip (both the outbound leg to the target and the return leg to the airport), or does the efficiency differ between the outbound and return legs?

## Turn 4 - User Simulator

The fuel efficiency of 2 km per liter is applied to the entire round trip for a bombing run carrying a heavy bomb.

## Turn 5 - Generic Agent

QUESTION: For a bombing run carrying a light bomb, is the fuel efficiency of 3 km per liter applied to the entire round trip (both the outbound leg to the target and the return leg to the airport), or does the efficiency differ between the outbound and return legs?

## Turn 5 - User Simulator

The fuel efficiency of 3 km per liter is applied to the entire round trip for a bombing run carrying a light bomb.

## Turn 6 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing fuel cost charged once per round trip (i.e., once per bombing run), or is it charged separately for the takeoff and for the landing?

## Turn 6 - User Simulator

The 100-liter takeoff-and-landing fuel cost is charged once per round trip (once per bombing run).

## Turn 7 - Generic Agent

QUESTION: Can the aircraft drop a heavy bomb on one key part and a light bomb on a different key part within the same mission, or must all bombs dropped in a mission be of the same type?

## Turn 7 - User Simulator

The aircraft can drop a heavy bomb on one key part and a light bomb on a different key part within the same mission. There is no requirement that all bombs dropped in a mission be of the same type.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many times the aircraft can fly to the same key part, or can it make unlimited bombing runs to the same target as long as the total bomb and fuel constraints are satisfied?

## Turn 8 - User Simulator

There is no limit on how many times the aircraft can fly to the same key part. It can make unlimited bombing runs to the same target as long as the total bomb and fuel constraints are satisfied.

## Turn 9 - Generic Agent

QUESTION: When computing the fuel for a bombing run to a key part, is the distance used the one-way distance from the airport to that key part (so the round trip distance is twice that value), or is the distance in the table already the round-trip distance?

## Turn 9 - User Simulator

The distance in the table is the one-way distance from the airport to that key part. The round trip distance is twice that value.

## Turn 10 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used required to be integers (you can only use whole bombs), or can they be treated as continuous variables in the model?

## Turn 10 - User Simulator

The numbers of heavy and light bombs used must be integers. You can only use whole bombs.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint on the total number of bombing runs (flights) the aircraft can make, or is the only limit on runs the fuel and bomb availability?

## Turn 11 - User Simulator

There is no specific constraint on the total number of bombing runs. The only limits on runs are the fuel and bomb availability.

## Turn 12 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), is the 4 km per liter fuel efficiency relevant to this mission, or is it simply unused information since every run carries exactly one bomb?

## Turn 12 - User Simulator

The 4 km per liter fuel efficiency is unused information for this mission, since every run carries exactly one bomb.

## Turn 13 - Generic Agent

QUESTION: Is the fuel consumption for a bombing run calculated as (round-trip distance / fuel efficiency) + 100 liters, where the 100 liters is added on top of the distance-based fuel, or is the 100 liters included within the distance-based calculation?

## Turn 13 - User Simulator

The fuel consumption for a bombing run is calculated as (round-trip distance / fuel efficiency) + 100 liters. The 100 liters is added on top of the distance-based fuel.

## Turn 14 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs the total available for the entire mission (i.e., you can use at most 28 heavy and at most 12 light across all runs), or are these per-run limits?

## Turn 14 - User Simulator

The 28 heavy bombs and 12 light bombs are the total available for the entire mission. You can use at most 28 heavy and at most 12 light across all runs.

## Turn 15 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit the total fuel available for the entire mission (across all bombing runs), or is it a per-run limit?

## Turn 15 - User Simulator

The 10,000-liter fuel limit is the total fuel available for the entire mission, across all bombing runs.

## Turn 16 - Generic Agent

QUESTION: When computing the probability that a key part is destroyed, is it simply 1 minus the product of (1 minus the per-bomb probability) for each bomb dropped on that part, assuming all bombs are independent?

## Turn 16 - User Simulator

Yes, the probability that a key part is destroyed is 1 minus the product of (1 minus the per-bomb probability) for each bomb dropped on that part, assuming all bombs are independent.

## Turn 17 - Generic Agent

QUESTION: When computing the probability that at least two of the four key parts are destroyed, are the destruction events for different key parts independent of each other?

## Turn 17 - User Simulator

Yes, the destruction events for different key parts are independent of each other.

## Turn 18 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be dropped on each key part, or can a key part receive zero bombs (and thus have zero probability of being destroyed)?

## Turn 18 - User Simulator

There is no minimum number of bombs that must be dropped on each key part. A key part can receive zero bombs, in which case it has zero probability of being destroyed.

## Turn 19 - Generic Agent

QUESTION: Are there any other constraints or considerations I should be aware of, such as a maximum number of bombs that can be dropped on a single key part, or any other operational restrictions?

## Turn 19 - User Simulator

No, there are no other constraints or considerations. There is no maximum number of bombs that can be dropped on a single key part, and there are no other operational restrictions beyond the bomb availability, fuel limit, and the requirement that each run carries one bomb.

## Turn 20 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize the probability that at least 2 of the 4 key parts are destroyed.

**Decision Variables:**
- For each key part *i* (i = 1, 2, 3, 4):
  - *h_i* = number of heavy bombs dropped on part *i* (non-negative integer)
  - *l_i* = number of light bombs dropped on part *i* (non-negative integer)

**Parameters:**
| Key Part | One-way Distance (km) | P(destruction per heavy) | P(destruction per light) |
|----------|----------------------|--------------------------|--------------------------|
| 1        | 450                  | 0.03                     | 0.08                     |
| 2        | 480                  | 0.10                     | 0.11                     |
| 3        | 540                  | 0.05                     | 0.12                     |
| 4        | 600                  | 0.05                     | 0.09                     |

**Destruction Probability per Part:**
- P(part *i* destroyed) = 1 − (1 − 0.03)^{h_i} × (1 − 0.08)^{l_i} for part 1, and analogously for parts 2–4 with their respective probabilities.

**Success Probability (objective):**
- P(at least 2 parts destroyed) = sum over all subsets S of {1,2,3,4} with |S| ≥ 2 of [∏_{i∈S} p_i × ∏_{j∉S} (1 − p_j)], where p_i is the destruction probability of part i.

**Constraints:**
1. **Heavy bomb limit:** Σ_i h_i ≤ 28
2. **Light bomb limit:** Σ_i l_i ≤ 12
3. **Fuel limit:** Σ_i [h_i × (2 × d_i / 2 + 100) + l_i × (2 × d_i / 3 + 100)] ≤ 10,000
   - where d_i is the one-way distance to part i, so round-trip distance is 2 × d_i.
   - Heavy bomb run fuel: (2 × d_i / 2) + 100 = d_i + 100 liters
   - Light bomb run fuel: (2 × d_i / 3) + 100 liters
4. **Integrality:** All h_i and l_i are non-negative integers.

**Key Assumptions Confirmed:**
- Each bomb requires a separate bombing run (one bomb per trip).
- Destruction probabilities are independent across bombs on the same part and across different parts.
- No minimum or maximum bombs per part.
- No limit on number of runs beyond fuel and bomb availability.
- The 4 km/L empty-aircraft efficiency is irrelevant.
- Fuel = (round-trip distance / efficiency) + 100 L per run.