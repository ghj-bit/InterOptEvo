## Turn 1 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop the bomb on arrival (so the return leg is flown empty at 4 km/L), or does it carry the bomb for the entire round trip (outbound and return both at the loaded efficiency)?

## Turn 1 - User Simulator

The aircraft drops the bomb on arrival, so the return leg is flown empty at 4 km per liter.

## Turn 2 - Generic Agent

QUESTION: Does the 100-liter takeoff-and-landing fuel cost apply once per round trip (i.e., one takeoff plus one landing per mission to a target), or once per leg (so a round trip to one target costs 200 liters)?

## Turn 2 - User Simulator

The 100-liter takeoff-and-landing fuel cost applies once per round trip.

## Turn 3 - Generic Agent

QUESTION: Does the aircraft fly one bomb per sortie (one takeoff, one bomb dropped, one landing), or can it carry multiple bombs in a single sortie and drop them at one or more targets before returning?

## Turn 3 - User Simulator

The aircraft flies one bomb per sortie.

## Turn 4 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, is the fuel efficiency for the entire outbound leg determined by the type of bomb being carried (heavy = 2 km/L, light = 3 km/L), regardless of how many bombs of that type are being carried?

## Turn 4 - User Simulator

Yes, the fuel efficiency for the outbound leg is determined by the type of bomb being carried: heavy = 2 km/L, light = 3 km/L.

## Turn 5 - Generic Agent

QUESTION: Is the probability of destroying a key part calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs dropped on that part, assuming independent bomb impacts?

## Turn 5 - User Simulator

Yes, the probability of destroying a key part is calculated as 1 minus (1 minus the per-bomb probability) raised to the power of the number of bombs dropped on that part, assuming independent bomb impacts.

## Turn 6 - Generic Agent

QUESTION: Is the mission success criterion that the expected number of destroyed key parts is at least 2, or that the probability of destroying at least 2 key parts is at least some threshold (and if the latter, what is that threshold)?

## Turn 6 - User Simulator

The mission success criterion is that the probability of destroying at least 2 key parts is maximized. There is no specific threshold; the goal is to maximize that probability.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs assigned to each key part required to be non-negative integers (you can only drop whole bombs), or can they be treated as continuous variables?

## Turn 7 - User Simulator

The numbers of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 8 - Generic Agent

QUESTION: Is the total fuel consumption the sum of fuel used by all sorties (each bomb dropped requires its own sortie with its own fuel cost), or is there a single aircraft that flies sequentially and the 10,000-liter limit applies to the cumulative fuel across all sorties?

## Turn 8 - User Simulator

The 10,000-liter limit applies to the cumulative fuel across all sorties.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint on the total number of sorties (takeoffs/landings), or is the only limit on sorties the fuel and bomb availability?

## Turn 9 - User Simulator

There is no separate constraint on the total number of sorties. The only limits are fuel availability and bomb availability.

## Turn 10 - Generic Agent

QUESTION: Can a key part receive both heavy and light bombs in the same mission, or must each key part be assigned only one type of bomb?

## Turn 10 - User Simulator

A key part can receive both heavy and light bombs in the same mission.

## Turn 11 - Generic Agent

QUESTION: Is there any minimum number of bombs that must be dropped on each key part, or can a key part receive zero bombs (i.e., be left untouched)?

## Turn 11 - User Simulator

A key part can receive zero bombs.

## Turn 12 - Generic Agent

QUESTION: Is the objective to maximize the probability of destroying at least 2 of the 4 key parts, or is there a secondary objective (such as minimizing fuel used or maximizing expected number of parts destroyed) that should be considered if multiple solutions achieve the same maximum probability?

## Turn 12 - User Simulator

The objective is to maximize the probability of destroying at least 2 of the 4 key parts. There is no secondary objective.

## Turn 13 - Generic Agent

QUESTION: When calculating fuel for a sortie to a target, is the distance used the one-way distance from the airport to that target (so round-trip distance is twice that), or is there a different distance convention?

## Turn 13 - User Simulator

The distance used is the one-way distance from the airport to that target, so the round-trip distance is twice that.

## Turn 14 - Generic Agent

QUESTION: Is the fuel consumption for a sortie calculated as (outbound distance divided by loaded efficiency) plus (return distance divided by empty efficiency) plus 100 liters, where outbound and return distances are both equal to the one-way distance to the target?

## Turn 14 - User Simulator

Yes, the fuel consumption for a sortie is calculated as (outbound distance divided by loaded efficiency) plus (return distance divided by empty efficiency) plus 100 liters, where outbound and return distances are both equal to the one-way distance to the target.

## Turn 15 - Generic Agent

QUESTION: Are the probabilities of destruction for different key parts independent of each other (i.e., the destruction of one part does not affect the probability of destroying another part)?

## Turn 15 - User Simulator

Yes, the probabilities of destruction for different key parts are independent of each other.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that the total number of bombs dropped (heavy plus light) must be at least some minimum, or can the solution use fewer than all available bombs?

## Turn 16 - User Simulator

There is no minimum number of bombs that must be dropped. The solution can use fewer than all available bombs.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the aircraft must return to the airport after each sortie, or could it potentially end the mission at a target?

## Turn 17 - User Simulator

The aircraft must return to the airport after each sortie.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint on the order in which sorties are flown, or can sorties to different targets be flown in any sequence?

## Turn 18 - User Simulator

There is no constraint on the order in which sorties are flown.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the aircraft must be able to carry the bomb type it is assigned (e.g., can the same aircraft carry both heavy and light bombs, or are there separate aircraft for each bomb type)?

## Turn 19 - User Simulator

There is no constraint that the aircraft must be able to carry only one type of bomb. The same aircraft can carry both heavy and light bombs.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the total number of sorties must be feasible given the aircraft's operational limits (such as maximum flight time or maximum number of sorties per day), or is the only constraint the fuel and bomb availability?

## Turn 20 - User Simulator

There is no constraint on the total number of sorties beyond fuel and bomb availability.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the aircraft must have a minimum amount of fuel remaining after each sortie, or can it use all available fuel across all sorties with no reserve requirement?

## Turn 21 - User Simulator

There is no minimum fuel reserve requirement. The aircraft can use all available fuel across all sorties.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the total fuel used across all sorties must be strictly less than 10,000 liters, or can it be exactly 10,000 liters?

## Turn 22 - User Simulator

The total fuel used across all sorties can be exactly 10,000 liters.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the number of heavy bombs used must be strictly less than 28, or can it be exactly 28?

## Turn 23 - User Simulator

The number of heavy bombs used can be exactly 28.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the number of light bombs used must be strictly less than 12, or can it be exactly 12?

## Turn 24 - User Simulator

The number of light bombs used can be exactly 12.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the aircraft must drop all bombs it carries in a single sortie, or can it carry a bomb and choose not to drop it (i.e., return with the bomb still on board)?

## Turn 25 - User Simulator

The aircraft must drop the bomb it carries in a single sortie.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the aircraft must drop the bomb on the specific target it is assigned to, or can it drop the bomb on any target along the way?

## Turn 26 - User Simulator

The aircraft must drop the bomb on the specific target it is assigned to.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the aircraft must fly directly to the assigned target, or can it fly to multiple targets in a single sortie (dropping one bomb at each)?

## Turn 27 - User Simulator

The aircraft must fly directly to the assigned target.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the aircraft must return to the airport immediately after dropping the bomb, or can it loiter or fly to another location before returning?

## Turn 28 - User Simulator

The aircraft must return to the airport immediately after dropping the bomb.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the aircraft must have a minimum speed or maximum speed during flight, or is the fuel efficiency the only factor determining fuel consumption?

## Turn 29 - User Simulator

There is no constraint on minimum or maximum speed. The fuel efficiency is the only factor determining fuel consumption.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the aircraft must complete all sorties within a specific time window, or is there no time limit on the mission?

## Turn 30 - User Simulator

There is no time limit on the mission.