## Turn 1 - Generic Agent

QUESTION: Is the mission's success criterion "at least two of the four key parts are destroyed" a hard requirement that must be satisfied (i.e., the plan is only valid if this holds), or is it an objective to maximize the probability of achieving?

## Turn 1 - User Simulator

It is an objective to maximize the probability of achieving. The plan is not required to guarantee that at least two key parts are destroyed; rather, we want to maximize the probability that at least two of the four key parts are destroyed.

## Turn 2 - Generic Agent

QUESTION: When the aircraft flies to a target and back, does it carry the bomb for the entire round trip (outbound and return), or does it drop the bomb at the target and return empty?

## Turn 2 - User Simulator

The aircraft drops the bomb at the target and returns empty.

## Turn 3 - Generic Agent

QUESTION: Does the aircraft make one trip per bomb (i.e., each trip carries exactly one bomb to a target), or can it carry multiple bombs in a single trip and drop them at one or more targets?

## Turn 3 - User Simulator

Each trip carries exactly one bomb to a target.

## Turn 4 - Generic Agent

QUESTION: Can the aircraft visit multiple targets in a single trip (e.g., drop a bomb at target 1, then fly to target 2 and drop another bomb), or does each trip go to exactly one target and return to the airport?

## Turn 4 - User Simulator

Each trip goes to exactly one target and returns to the airport.

## Turn 5 - Generic Agent

QUESTION: For the fuel calculation, is the fuel efficiency (2 km/L for heavy, 3 km/L for light, 4 km/L for empty) applied to the total distance flown, or is it applied per leg (outbound vs. return)?

## Turn 5 - User Simulator

It is applied per leg. The outbound leg uses the efficiency for the bomb being carried, and the return leg uses the empty efficiency.

## Turn 6 - Generic Agent

QUESTION: Is the 100-liter takeoff/landing fuel cost charged once per round trip (i.e., one takeoff and one landing), or is it charged separately for the takeoff and for the landing (i.e., 100 liters for takeoff plus 100 liters for landing)?

## Turn 6 - User Simulator

It is charged once per round trip, meaning 100 liters total for the combined takeoff and landing.

## Turn 7 - Generic Agent

QUESTION: Are the destruction probabilities for each bomb independent, so that the probability a key part is destroyed after receiving multiple bombs is 1 minus the product of (1 minus each bomb's probability)?

## Turn 7 - User Simulator

Yes, the destruction probabilities for each bomb are independent.

## Turn 8 - Generic Agent

QUESTION: Can the same key part receive both heavy and light bombs (i.e., can we split bomb types across the four parts), or must each part receive only one type of bomb?

## Turn 8 - User Simulator

The same key part can receive both heavy and light bombs.

## Turn 9 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each target required to be integers (i.e., you can only assign whole bombs), or can they be fractional in the optimization?

## Turn 9 - User Simulator

The numbers of heavy and light bombs assigned to each target must be integers.

## Turn 10 - Generic Agent

QUESTION: Is there a limit on how many bombs can be dropped on a single key part, or can all 28 heavy and 12 light bombs be concentrated on one part?

## Turn 10 - User Simulator

There is no limit on how many bombs can be dropped on a single key part.

## Turn 11 - Generic Agent

QUESTION: Is the fuel constraint a single shared pool of 10,000 liters for all trips combined, or is there a separate fuel limit per trip?

## Turn 11 - User Simulator

It is a single shared pool of 10,000 liters for all trips combined.

## Turn 12 - Generic Agent

QUESTION: Is the objective to maximize the probability that at least two of the four key parts are destroyed, where the probability of each part being destroyed depends on the number and type of bombs assigned to it, and the overall probability is computed by summing over all combinations of at least two parts being destroyed?

## Turn 12 - User Simulator

Yes, that is correct.

## Turn 13 - Generic Agent

QUESTION: Are the 28 heavy bombs and 12 light bombs the total available for the entire mission (i.e., you can use up to 28 heavy and up to 12 light across all targets), or are these per-target limits?

## Turn 13 - User Simulator

They are the total available for the entire mission.

## Turn 14 - Generic Agent

QUESTION: Is there any requirement that the aircraft must use all available bombs, or can it choose to use fewer than 28 heavy and/or fewer than 12 light bombs if that leads to a higher probability?

## Turn 14 - User Simulator

The aircraft can choose to use fewer than 28 heavy and/or fewer than 12 light bombs.

## Turn 15 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be used, or can the aircraft choose to use zero bombs if that somehow maximizes the probability?

## Turn 15 - User Simulator

There is no minimum number of bombs that must be used.

## Turn 16 - Generic Agent

QUESTION: Is the fuel efficiency for the outbound leg determined by the type of bomb being carried (2 km/L for heavy, 3 km/L for light), regardless of the target's distance, and the return leg always uses 4 km/L (empty)?

## Turn 16 - User Simulator

Yes, that is correct.

## Turn 17 - Generic Agent

QUESTION: Is the 100-liter takeoff/landing cost the same regardless of the target's distance or the type of bomb carried?

## Turn 17 - User Simulator

Yes, the 100-liter takeoff/landing cost is the same regardless of the target's distance or the type of bomb carried.

## Turn 18 - Generic Agent

QUESTION: Is the fuel consumption for the outbound leg calculated as (distance to target) divided by (fuel efficiency for the bomb type), and the return leg as (distance to target) divided by 4, plus the 100-liter takeoff/landing cost?

## Turn 18 - User Simulator

Yes, that is correct.

## Turn 19 - Generic Agent

QUESTION: Is the probability that a key part is destroyed calculated as 1 minus the product of (1 minus the probability of each individual bomb destroying it), where each bomb's probability is the value from the table for that part and bomb type?

## Turn 19 - User Simulator

Yes, that is correct.

## Turn 20 - Generic Agent

QUESTION: Is the overall objective to maximize the probability that at least two of the four key parts are destroyed, where this probability is computed by summing over all subsets of at least two parts the product of their individual destruction probabilities and the survival probabilities of the remaining parts?

## Turn 20 - User Simulator

Yes, that is correct.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint on the number of trips the aircraft can make, or is the only limit on trips the fuel and bomb availability?

## Turn 21 - User Simulator

The only limits on trips are the fuel and bomb availability.

## Turn 22 - Generic Agent

QUESTION: Is the fuel consumption for a trip to target i with a heavy bomb equal to (distance_i / 2) + (distance_i / 4) + 100, and for a light bomb equal to (distance_i / 3) + (distance_i / 4) + 100?

## Turn 22 - User Simulator

Yes, that is correct.

## Turn 23 - Generic Agent

QUESTION: Is the total fuel consumption the sum of the fuel for each individual trip, and this sum must not exceed 10,000 liters?

## Turn 23 - User Simulator

Yes, that is correct.

## Turn 24 - Generic Agent

QUESTION: Is the total number of heavy bombs used across all targets at most 28, and the total number of light bombs used across all targets at most 12?

## Turn 24 - User Simulator

Yes, that is correct.

## Turn 25 - Generic Agent

QUESTION: Is the decision variable for each target the number of heavy bombs and the number of light bombs assigned to that target, with the constraint that the sum of heavy bombs across all targets is at most 28 and the sum of light bombs across all targets is at most 12?

## Turn 25 - User Simulator

Yes, that is correct.

## Turn 26 - Generic Agent

QUESTION: Is the fuel constraint the sum over all targets of (heavy_bombs_i * fuel_per_heavy_trip_i + light_bombs_i * fuel_per_light_trip_i) at most 10,000, where fuel_per_heavy_trip_i = distance_i/2 + distance_i/4 + 100 and fuel_per_light_trip_i = distance_i/3 + distance_i/4 + 100?

## Turn 26 - User Simulator

Yes, that is correct.

## Turn 27 - Generic Agent

QUESTION: Is the probability that key part i is destroyed equal to 1 minus (1 minus p_heavy_i) raised to the power of heavy_bombs_i, times (1 minus p_light_i) raised to the power of light_bombs_i, where p_heavy_i and p_light_i are the per-bomb destruction probabilities from the table?

## Turn 27 - User Simulator

Yes, that is correct.

## Turn 28 - Generic Agent

QUESTION: Is the overall objective to maximize the probability that at least two of the four key parts are destroyed, where this probability is computed as 1 minus the probability that zero parts are destroyed minus the probability that exactly one part is destroyed?

## Turn 28 - User Simulator

Yes, that is correct.

## Turn 29 - Generic Agent

QUESTION: Is the probability that exactly one part is destroyed equal to the sum over each part i of (probability part i is destroyed times the product of the probabilities that all other parts are not destroyed)?

## Turn 29 - User Simulator

Yes, that is correct.

## Turn 30 - Generic Agent

QUESTION: Is the probability that zero parts are destroyed equal to the product over all four parts of the probability that each part is not destroyed?

## Turn 30 - User Simulator

Yes, that is correct.