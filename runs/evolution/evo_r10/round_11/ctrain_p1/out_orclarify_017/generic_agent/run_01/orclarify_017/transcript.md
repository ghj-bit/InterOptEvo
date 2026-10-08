## Turn 1 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop that bomb on arrival (so the return leg is flown empty at 4 km/liter), or does it carry the bomb for the entire round trip (so both legs use the bomb's fuel efficiency)?

## Turn 1 - User Simulator

The aircraft drops the bomb on arrival, so the return leg is flown empty at 4 km per liter.

## Turn 2 - Generic Agent

QUESTION: For a bombing run to a key part, is the fuel consumed equal to (distance × 2 / bomb-efficiency) + (distance / 4) + 100 liters — i.e., the 100-liter takeoff/landing charge is added once per round trip — or is the 100 liters charged separately for the takeoff and for the landing (200 liters per round trip)?

## Turn 2 - User Simulator

The 100-liter takeoff/landing charge is added once per round trip.

## Turn 3 - Generic Agent

QUESTION: The mission is successful only if at least two of the four key parts are destroyed — is the objective to maximize the probability of achieving that success, or is it to minimize the total fuel consumed (or total bombs used) subject to the probability of success being at least some threshold?

## Turn 3 - User Simulator

The objective is to maximize the probability of achieving that success.

## Turn 4 - Generic Agent

QUESTION: Are the destruction probabilities for the four key parts independent of each other, so that the probability of a given set of parts being destroyed is the product of their individual destruction probabilities?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: For a single key part, if you drop multiple bombs on it, is the probability that the part is destroyed equal to 1 minus (1 minus the per-bomb probability) raised to the number of bombs dropped on that part — i.e., each bomb independently has a chance to destroy it?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Can a single aircraft carry both a heavy bomb and a light bomb on the same round trip, or does each round trip carry exactly one bomb (either one heavy or one light)?

## Turn 6 - User Simulator

Each round trip carries exactly one bomb (either one heavy or one light).

## Turn 7 - Generic Agent

QUESTION: Can the same key part be bombed by both heavy and light bombs (i.e., split the bombs assigned to a part between the two types), or must all bombs assigned to a given part be of a single type?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the heavy and light bomb counts (28 and 12) hard upper limits that you may use fewer of, or must you use exactly all 28 heavy and all 12 light bombs?

## Turn 8 - User Simulator

They are hard upper limits; you may use fewer of each.

## Turn 9 - Generic Agent

QUESTION: Is the 10,000-liter fuel limit a hard upper bound that you may use less than, or must the plan use exactly 10,000 liters?

## Turn 9 - User Simulator

It is a hard upper bound; you may use less than 10,000 liters.

## Turn 10 - Generic Agent

QUESTION: If a key part receives zero bombs, is its probability of being destroyed exactly zero (i.e., it cannot be destroyed by any other means)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: When computing the probability that a key part is destroyed, should I treat each bomb's chance to destroy it as independent and additive in the sense that P(destroyed) = 1 - (1 - p)^n for n bombs of that type, or should I use a different combination rule?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: If a key part receives both heavy and light bombs, should the probability of its destruction be computed by combining the heavy-bomb contribution and the light-bomb contribution as independent (i.e., 1 - (1 - p_heavy_destroyed)(1 - p_light_destroyed)), or should only one bomb type be allowed per part?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is the probability that a key part is destroyed, given it receives n bombs, computed as 1 minus (1 minus the per-bomb probability) to the power n, treating each bomb's effect as independent?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the fuel calculation, is the round-trip fuel for a heavy bomb to a part at distance d equal to (2d / 2) + (2d / 4) + 100, and for a light bomb equal to (2d / 3) + (2d / 4) + 100, where the first term is the outbound leg carrying the bomb and the second term is the return leg empty?

## Turn 14 - User Simulator

Yes, that is correct.

## Turn 15 - Generic Agent

QUESTION: When a key part receives multiple bombs, is the probability that the part is destroyed equal to 1 minus (1 minus the per-bomb probability) raised to the total number of bombs dropped on that part, treating each bomb's effect as independent?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: If a key part receives both heavy and light bombs, should the destruction probability be computed by first computing the heavy-bomb contribution as 1-(1-p_h)^n_h and the light-bomb contribution as 1-(1-p_l)^n_l, then combining them as 1 - (1 - P_h)(1 - P_l), treating the two bomb types' effects as independent?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Are the destruction outcomes of the four key parts independent of one another, so that the probability of any particular combination of parts being destroyed is the product of the individual parts' destruction probabilities?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: If a key part receives zero bombs, is its probability of being destroyed exactly zero?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is the probability that a key part is destroyed, given it receives n bombs of a single type, equal to 1 minus (1 minus the per-bomb probability) to the power n?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Should the model allow assigning both heavy and light bombs to the same key part, or must each key part receive bombs of only one type?

## Turn 30 - User Simulator

The point still needs internal