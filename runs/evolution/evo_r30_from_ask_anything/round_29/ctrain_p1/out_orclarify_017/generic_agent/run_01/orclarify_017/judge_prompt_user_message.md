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

QUESTION: Is the mission's objective to maximize the probability that at least two of the four key parts are destroyed, or is there a different goal such as minimizing fuel used or maximizing the expected number of parts destroyed?

## Turn 1 - User Simulator

The objective is to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: When the aircraft carries a heavy bomb, does it carry exactly one heavy bomb per trip, or can it carry multiple heavy bombs on a single trip?

## Turn 2 - User Simulator

The aircraft carries exactly one heavy bomb per trip.

## Turn 3 - Generic Agent

QUESTION: When the aircraft carries a light bomb, does it carry exactly one light bomb per trip, or can it carry multiple light bombs on a single trip?

## Turn 3 - User Simulator

The aircraft carries exactly one light bomb per trip.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft carry one heavy bomb and one light bomb together on a single trip, or must each trip carry only one bomb of a single type?

## Turn 4 - User Simulator

Each trip carries only one bomb of a single type.

## Turn 5 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it still fly a round trip to the target and back, or does it only fly empty legs between targets or back to the airport?

## Turn 5 - User Simulator

The aircraft only flies empty legs between targets or back to the airport.

## Turn 6 - Generic Agent

QUESTION: Does the aircraft start at the airport before the first bombing run?

## Turn 6 - User Simulator

Yes, the aircraft starts at the airport before the first bombing run.

## Turn 7 - Generic Agent

QUESTION: After the final bombing run, does the aircraft need to return to the airport, or can it end the mission at the last target?

## Turn 7 - User Simulator

The aircraft must return to the airport after the final bombing run.

## Turn 8 - Generic Agent

QUESTION: When the aircraft flies an empty leg between two different targets, is the fuel efficiency 4 km per liter for the entire distance between those two targets?

## Turn 8 - User Simulator

Yes, the fuel efficiency is 4 km per liter for the entire distance between those two targets.

## Turn 9 - Generic Agent

QUESTION: When the aircraft flies an empty leg from a target back to the airport, is the fuel efficiency 4 km per liter for the entire distance?

## Turn 9 - User Simulator

Yes, the fuel efficiency is 4 km per liter for the entire distance.

## Turn 10 - Generic Agent

QUESTION: When the aircraft flies a bombing run from the airport to a target and back, is the fuel efficiency 2 km per liter (for heavy) or 3 km per liter (for light) for the entire round trip distance?

## Turn 10 - User Simulator

Yes, the fuel efficiency is 2 km per liter for the entire round trip distance when carrying a heavy bomb, and 3 km per liter for the entire round trip distance when carrying a light bomb.

## Turn 11 - Generic Agent

QUESTION: Does the 100-liter takeoff and landing fuel consumption apply to every trip, including empty legs between targets?

## Turn 11 - User Simulator

No, the 100-liter takeoff and landing fuel consumption applies only to trips that start and end at the airport.

## Turn 12 - Generic Agent

QUESTION: Does the 100-liter takeoff and landing fuel consumption apply to the final return trip from the last target back to the airport?

## Turn 12 - User Simulator

Yes, the 100-liter takeoff and landing fuel consumption applies to the final return trip from the last target back to the airport.

## Turn 13 - Generic Agent

QUESTION: When the aircraft flies a bombing run from the airport to a target and back to the airport, does the 100-liter takeoff and landing fuel consumption apply to that trip?

## Turn 13 - User Simulator

Yes, the 100-liter takeoff and landing fuel consumption applies to that trip.

## Turn 14 - Generic Agent

QUESTION: Are the destruction probabilities for each bomb independent of each other, meaning the probability of destroying a part with multiple bombs is calculated as 1 minus the product of the survival probabilities for each bomb?

## Turn 14 - User Simulator

Yes, the destruction probabilities for each bomb are independent of each other.

## Turn 15 - Generic Agent

QUESTION: Can the same key part be targeted by multiple bombs, or must each bomb be assigned to a different key part?

## Turn 15 - User Simulator

The same key part can be targeted by multiple bombs.

## Turn 16 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used integer values, or can they be fractional?

## Turn 16 - User Simulator

The numbers of heavy and light bombs used are integer values.

## Turn 17 - Generic Agent

QUESTION: Is there a limit on the total number of trips the aircraft can make, or is the only limit on trips the fuel constraint?

## Turn 17 - User Simulator

The only limit on trips is the fuel constraint.

## Turn 18 - Generic Agent

QUESTION: Can the aircraft visit the same target multiple times during the mission, or must each target be visited at most once?

## Turn 18 - User Simulator

The aircraft can visit the same target multiple times during the mission.

## Turn 19 - Generic Agent

QUESTION: Are there any other constraints or requirements for the mission that have not been mentioned yet?

## Turn 19 - User Simulator

No, there are no other constraints or requirements for the mission.

## Turn 20 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the probability that at least two of the four key parts are destroyed.
2.  **Decision Variables:**
    *   The sequence of bombing runs (which target is hit, with which bomb type).
    *   The number of heavy bombs used ($H$) and light bombs used ($L$).
    *   The path of the aircraft (sequence of targets visited).
3.  **Variable Domains:**
    *   $H$ and $L$ are non-negative integers.
    *   The sequence of targets is a finite sequence of indices from $\{1, 2, 3, 4\}$.
4.  **Constraints:**
    *   **Bomb Limits:** $H \le 28$, $L \le 12$.
    *   **Fuel Limit:** Total fuel consumption $\le 10,000$ liters.
    *   **Trip Structure:**
        *   The aircraft starts at the airport.
        *   Each bombing run consists of flying from the current location to a target, dropping one bomb, and then either flying to the next target (empty leg) or returning to the airport (empty leg).
        *   The aircraft must return to the airport after the final bombing run.
        *   Each trip carries exactly one bomb (either heavy or light).
        *   The aircraft can visit the same target multiple times.
5.  **Fuel Consumption Rules:**
    *   **Bombing Run (Airport to Target and back to Airport):**
        *   Distance: $2 \times d_i$ (where $d_i$ is the distance to target $i$).
        *   Efficiency: 2 km/L for heavy bombs, 3 km/L for light bombs.
        *   Fuel for distance: $(2 \times d_i) / \text{efficiency}$.
        *   Takeoff/Landing: +100 liters.
    *   **Empty Leg (Between Targets or Target to Airport):**
        *   Distance: Distance between the two locations.
        *   Efficiency: 4 km/L.
        *   Fuel for distance: $\text{distance} / 4$.
        *   Takeoff/Landing: +100 liters **only** if the leg ends at the airport (i.e., the final return trip). No takeoff/landing fuel is consumed for legs between targets.
    *   *Note on Interpretation:* The user confirmed that the 100L takeoff/landing cost applies to trips that start and end at the airport. This includes the initial bombing run (Airport -> Target -> Airport) and the final return (Target -> Airport). It does not apply to legs between targets.
6.  **Probability Model:**
    *   Destruction probabilities are independent.
    *   If a target $i$ is hit by $h_i$ heavy bombs and $l_i$ light bombs, the probability of destruction is $1 - (1-p_{h,i})^{h_i} (1-p_{l,i})^{l_i}$.
    *   The events of destruction for different targets are independent.
    *   The mission is successful if at least two targets are destroyed.
7.  **Data:**
    *   Target 1: $d=450$ km, $p_h=0.03$, $p_l=0.08$.
    *   Target 2: $d=480$ km, $p_h=0.10$, $p_l=0.11$.
    *   Target 3: $d=540$ km, $p_h=0.05$, $p_l=0.12$.
    *   Target 4: $d=600$ km, $p_h=0.05$, $p_l=0.09$.
    *   Heavy bombs available: 28.
    *   Light bombs available: 12.
    *   Total fuel available: 10,000 liters.

**Assumptions:**
*   The distance between two targets $i$ and $j$ for an empty leg is calculated as $|d_i - d_j|$ (assuming they are on the same radial line from the airport). This is a standard assumption for such problems unless a map is provided. If the targets are not collinear with the airport, the distance would be different. Given the data format (single distance per target), collinearity is the only computable interpretation.
*   The "round trip" description in the prompt for bombing runs is interpreted as the path Airport -> Target -> Airport. The user confirmed that the 100L cost applies to this.
*   The user confirmed that the 100L cost applies to the final return trip. It is assumed that if the aircraft returns to the airport mid-mission (e.g., to refuel or just as a routing choice), that leg also incurs the 100L cost. However, since the objective is to maximize probability under a fuel constraint, and refueling is not mentioned as a possibility (only a total fuel limit), the aircraft likely does not return to the airport mid-mission unless it is the final return. The model will allow any sequence, but the fuel cost rules are strictly applied as defined.