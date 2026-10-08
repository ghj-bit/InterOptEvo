## Turn 1 - Generic Agent

QUESTION: When you say the mission is successful only if at least two of the four key parts are destroyed, do you want the model to maximize the probability of achieving that success, or to guarantee (with certainty) that at least two parts are destroyed?

## Turn 1 - User Simulator

We want the model to maximize the probability of achieving that success. We are not asking for a guaranteed destruction of at least two parts.

## Turn 2 - Generic Agent

QUESTION: For the probability of a key part being destroyed, should I treat each bomb's destruction probability as independent (so a part hit by multiple bombs has destruction probability 1 minus the product of the per-bomb survival probabilities), or should I use some other rule for combining multiple bombs on the same part?

## Turn 2 - User Simulator

The available business facts do not specify the rule for combining multiple bombs on the same part. This point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the fuel constraint, is the 10,000-liter limit a total across the entire mission (all bombing runs combined), or is it a per-aircraft/per-run limit?

## Turn 3 - User Simulator

The 10,000-liter limit is a total across the entire mission (all bombing runs combined).

## Turn 4 - Generic Agent

QUESTION: For a bombing run to a target at distance d km, is the fuel consumed equal to (2d divided by the fuel efficiency while carrying the bomb) plus the 100-liter takeoff-and-landing cost, where the aircraft carries the bomb the entire round trip?

## Turn 4 - User Simulator

The available business facts do not specify whether the aircraft carries the bomb the entire round trip or only one way. This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Can a single aircraft carry both a heavy bomb and a light bomb on the same bombing run, or does each run carry exactly one bomb (either heavy or light)?

## Turn 5 - User Simulator

Each run carries exactly one bomb (either heavy or light).

## Turn 6 - Generic Agent

QUESTION: Can the same key part be bombed by both heavy and light bombs (i.e., can I split bombs of both types across the four parts), or must each part receive only one bomb type?

## Turn 6 - User Simulator

The available business facts do not specify whether a key part can receive both heavy and light bombs. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are the numbers of heavy and light bombs used (28 and 12) maximum limits I can choose to use fewer of, or must I use exactly all 28 heavy and all 12 light bombs?

## Turn 7 - User Simulator

They are maximum limits. I can choose to use fewer than 28 heavy bombs and fewer than 12 light bombs.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on the number of bombing runs (takeoffs/landings) the aircraft can make, other than the fuel and bomb availability constraints?

## Turn 8 - User Simulator

The available business facts do not specify a limit on the number of bombing runs other than the fuel and bomb availability constraints. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever fly a leg in this mission, or is the empty-aircraft fuel efficiency of 4 km per liter simply unused because every run carries exactly one bomb the whole way?

## Turn 9 - User Simulator

The available business facts do not specify whether the aircraft ever flies a leg while empty. This point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: For the 100-liter takeoff-and-landing cost, is it charged once per bombing run (i.e., once per round trip), or once per takeoff and once per landing separately?

## Turn 10 - User Simulator

It is charged once per bombing run (i.e., once per round trip).

## Turn 11 - Generic Agent

QUESTION: For the fuel consumed on a bombing run to a part at distance d km, should I compute it as (2d divided by the fuel efficiency while carrying that bomb) plus the 100-liter takeoff-and-landing cost, with the bomb carried the entire round trip?

## Turn 11 - User Simulator

The available business facts do not specify whether the bomb is carried the entire round trip or only one way. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: For the probability of a key part being destroyed, should I treat each bomb's destruction probability as independent, so a part hit by multiple bombs has destruction probability equal to 1 minus the product of the per-bomb survival probabilities?

## Turn 12 - User Simulator

The available business facts do not specify the rule for combining multiple bombs on the same part. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Can a single key part receive bombs of both types (for example, some heavy and some light bombs on part 3), or must each part be assigned only one bomb type?

## Turn 13 - User Simulator

The available business facts do not specify whether a key part can receive bombs of both types. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any limit on the number of bombing runs the aircraft can make, other than the fuel and bomb availability constraints?

## Turn 14 - User Simulator

The available business facts do not specify a limit on the number of bombing runs other than the fuel and bomb availability constraints. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever fly a leg in this mission, or is the empty-aircraft fuel efficiency of 4 km per liter simply unused because every run carries exactly one bomb the whole way?

## Turn 15 - User Simulator

The available business facts do not specify whether the aircraft ever flies a leg while empty. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the fuel consumed on a bombing run to a part at distance d km, should I compute it as (2d divided by the fuel efficiency while carrying that bomb) plus the 100-liter takeoff-and-landing cost, with the bomb carried the entire round trip?

## Turn 16 - User Simulator

The available business facts do not specify whether the bomb is carried the entire round trip or only one way. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: For the probability of a key part being destroyed, should I treat each bomb's destruction probability as independent, so a part hit by multiple bombs has destruction probability equal to 1 minus the product of the per-bomb survival probabilities?

## Turn 17 - User Simulator

The available business facts do not specify the rule for combining multiple bombs on the same part. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Can a single key part receive bombs of both types (for example, some heavy and some light bombs on part 3), or must each part be assigned only one bomb type?

## Turn 18 - User Simulator

The available business facts do not specify whether a key part can receive bombs of both types. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there any limit on the number of bombing runs the aircraft can make, other than the fuel and bomb availability constraints?

## Turn 19 - User Simulator

The available business facts do not specify a limit on the number of bombing runs other than the fuel and bomb availability constraints. This point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever fly a leg in this mission, or is the empty-aircraft fuel efficiency of 4 km per liter simply unused because every run carries exactly one bomb the whole way?

## Turn 20 - User Simulator

The available business facts do not specify whether the aircraft ever flies a leg while empty. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: For the fuel consumed on a bombing run to a part at distance d km, should I compute it as (2d divided by the fuel efficiency while carrying that bomb) plus the 100-liter takeoff-and-landing cost, with the bomb carried the entire round trip?

## Turn 21 - User Simulator

The available business facts do not specify whether the bomb is carried the entire round trip or only one way. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: For the probability of a key part being destroyed, should I treat each bomb's destruction probability as independent, so a part hit by multiple bombs has destruction probability equal to 1 minus the product of the per-bomb survival probabilities?

## Turn 22 - User Simulator

The available business facts do not specify the rule for combining multiple bombs on the same part. This point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Can a single key part receive bombs of both types (for example, some heavy and some light bombs on part 3), or must each part be assigned only one bomb type?

## Turn 23 - User Simulator

The available business facts do not specify whether a key part can receive bombs of both types. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any limit on the number of bombing runs the aircraft can make, other than the fuel and bomb availability constraints?

## Turn 24 - User Simulator

The available business facts do not specify a limit on the number of bombing runs other than the fuel and bomb availability constraints. This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever fly a leg in this mission, or is the empty-aircraft fuel efficiency of 4 km per liter simply unused because every run carries exactly one bomb the whole way?

## Turn 25 - User Simulator

The available business facts do not specify whether the aircraft ever flies a leg while empty. This point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: For the fuel consumed on a bombing run to a part at distance d km, should I compute it as (2d divided by the fuel efficiency while carrying that bomb) plus the 100-liter takeoff-and-landing cost, with the bomb carried the entire round trip?

## Turn 26 - User Simulator

The available business facts do not specify whether the bomb is carried the entire round trip or only one way. This point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: For the probability of a key part being destroyed, should I treat each bomb's destruction probability as independent, so a part hit by multiple bombs has destruction probability equal to 1 minus the product of the per-bomb survival probabilities?

## Turn 27 - User Simulator

The available business facts do not specify the rule for combining multiple bombs on the same part. This point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Can a single key part receive bombs of both types (for example, some heavy and some light bombs on part 3), or must each part be assigned only one bomb type?

## Turn 28 - User Simulator

The available business facts do not specify whether a key part can receive bombs of both types. This point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there any limit on the number of bombing runs the aircraft can make, other than the fuel and bomb availability constraints?

## Turn 29 - User Simulator

The available business facts do not specify a limit on the number of bombing runs other than the fuel and bomb availability constraints. This point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: When the aircraft is empty (not carrying a bomb), does it ever fly a leg in this mission, or is the empty-aircraft fuel efficiency of 4 km per liter simply unused because every run carries exactly one bomb the whole way?

## Turn 30 - User Simulator

The available business facts do not specify whether the aircraft ever flies a leg while empty. This point still needs internal confirmation.