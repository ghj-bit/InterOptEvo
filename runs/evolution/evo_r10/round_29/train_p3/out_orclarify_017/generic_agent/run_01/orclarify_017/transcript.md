## Turn 1 - Generic Agent

QUESTION: When the aircraft carries a bomb to a target, does it drop the bomb on arrival (so the return leg is flown empty at 4 km/L), or does it carry the bomb for the entire round trip (so both legs use the bomb's fuel efficiency)?

## Turn 1 - User Simulator

The aircraft drops the bomb on arrival, so the return leg is flown empty at 4 km per liter.

## Turn 2 - Generic Agent

QUESTION: Does the 100-liter takeoff-and-landing fuel cost apply once per round trip (i.e., one takeoff plus one landing per sortie), or is it charged separately for each takeoff and each landing?

## Turn 2 - User Simulator

The 100-liter cost applies once per round trip, covering one takeoff and one landing per sortie.

## Turn 3 - Generic Agent

QUESTION: The mission is successful if at least two of the four key parts are destroyed — is the objective to maximize the probability of achieving that success, or is it to guarantee (with certainty) that at least two parts are destroyed?

## Turn 3 - User Simulator

The objective is to maximize the probability of achieving that success.

## Turn 4 - Generic Agent

QUESTION: Are the destruction events for each key part independent of one another, so that the probability a part survives equals the product of the survival probabilities of all bombs dropped on it?

## Turn 4 - User Simulator

Yes, the destruction events for each key part are independent of one another.

## Turn 5 - Generic Agent

QUESTION: Can the aircraft carry both a heavy and a light bomb on the same sortie, or does each sortie carry exactly one bomb (either heavy or light)?

## Turn 5 - User Simulator

Each sortie carries exactly one bomb, either heavy or light.

## Turn 6 - Generic Agent

QUESTION: Can the aircraft make multiple sorties to the same key part (dropping several bombs on one part across separate round trips), or is each key part visited at most once?

## Turn 6 - User Simulator

The aircraft can make multiple sorties to the same key part, dropping several bombs on one part across separate round trips.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total number of sorties (round trips) the aircraft can make, or is the only constraint on sorties the fuel budget?

## Turn 7 - User Simulator

The only constraint on sorties is the fuel budget.

## Turn 8 - Generic Agent

QUESTION: For the fuel calculation, is the distance flown in a sortie simply twice the one-way distance to the target (out and back along the same route), with no additional distance for maneuvering or loitering?

## Turn 8 - User Simulator

Yes, the distance flown in a sortie is simply twice the one-way distance to the target, with no additional distance for maneuvering or loitering.

## Turn 9 - Generic Agent

QUESTION: When computing the probability that a key part is destroyed by multiple bombs, is it correct to use 1 minus the product of (1 minus each bomb's destruction probability) for all bombs dropped on that part?

## Turn 9 - User Simulator

Yes, that is correct.

## Turn 10 - Generic Agent

QUESTION: Are the 28 heavy and 12 light bombs hard upper bounds (you may use fewer), or must all of them be used?

## Turn 10 - User Simulator

They are hard upper bounds; you may use fewer.

## Turn 11 - Generic Agent

QUESTION: Is the 10,000-liter fuel a hard upper bound (you may use less), and is there any minimum fuel reserve that must remain after the mission?

## Turn 11 - User Simulator

The 10,000-liter fuel is a hard upper bound, and there is no minimum fuel reserve that must remain after the mission.

## Turn 12 - Generic Agent

QUESTION: Can the number of bombs dropped on a key part be zero (i.e., is it allowed to skip a key part entirely and not drop any bombs on it)?

## Turn 12 - User Simulator

Yes, it is allowed to skip a key part entirely and not drop any bombs on it.

## Turn 13 - Generic Agent

QUESTION: Is there any requirement that the aircraft must return to the airport after each sortie (i.e., every sortie is a complete round trip that ends back at the airport), or could it end the mission away from the airport?

## Turn 13 - User Simulator

Every sortie is a complete round trip that ends back at the airport.

## Turn 14 - Generic Agent

QUESTION: Is the probability of success computed as the sum over all subsets of key parts of size at least two, of the probability that exactly that subset is destroyed (with the rest surviving)?

## Turn 14 - User Simulator

Yes, the probability of success is computed as the sum over all subsets of key parts of size at least two, of the probability that exactly that subset is destroyed (with the rest surviving).

## Turn 15 - Generic Agent

QUESTION: Is there any limit on how many bombs of the same type can be dropped on a single key part in total (e.g., all 28 heavy bombs on one part), or is the only limit the overall bomb and fuel budgets?

## Turn 15 - User Simulator

The only limits are the overall bomb and fuel budgets.

## Turn 16 - Generic Agent

QUESTION: When the aircraft flies the outbound leg carrying a bomb, is the fuel efficiency for that entire outbound leg determined solely by the bomb type carried (2 km/L for heavy, 3 km/L for light), regardless of the target's distance?

## Turn 16 - User Simulator

Yes, the fuel efficiency for the outbound leg is determined solely by the bomb type carried: 2 km/L for heavy, 3 km/L for light.

## Turn 17 - Generic Agent

QUESTION: Is the 100-liter takeoff-and-landing cost added on top of the fuel consumed for the distance flown (outbound plus return), so total fuel per sortie equals distance-based fuel plus 100 liters?

## Turn 17 - User Simulator

Yes, the 100-liter takeoff-and-landing cost is added on top of the fuel consumed for the distance flown, so total fuel per sortie equals distance-based fuel plus 100 liters.

## Turn 18 - Generic Agent

QUESTION: Is the fuel consumed for a sortie to key part i with a heavy bomb equal to (450×2)/2 + (450×2)/4 + 100, i.e., outbound distance divided by 2 km/L plus return distance divided by 4 km/L plus 100 liters?

## Turn 18 - User Simulator

Yes, that is correct.

## Turn 19 - Generic Agent

QUESTION: Is the fuel consumed for a sortie to key part i with a light bomb equal to (distance×2)/3 + (distance×2)/4 + 100, i.e., outbound distance divided by 3 km/L plus return distance divided by 4 km/L plus 100 liters?

## Turn 19 - User Simulator

Yes, that is correct.

## Turn 20 - Generic Agent

QUESTION: Are the decision variables (number of heavy and light bombs assigned to each key part) required to be non-negative integers?

## Turn 20 - User Simulator

Yes, the number of heavy and light bombs assigned to each key part must be non-negative integers.

## Turn 21 - Generic Agent

QUESTION: Is there any requirement that at least one bomb must be dropped in total (i.e., the mission cannot consist of zero sorties)?

## Turn 21 - User Simulator

No, there is no requirement that at least one bomb must be dropped in total.

## Turn 22 - Generic Agent

QUESTION: Is the probability of destruction per bomb independent of how many other bombs are dropped on the same key part (i.e., each bomb's probability is fixed regardless of the total number of bombs on that part)?

## Turn 22 - User Simulator

Yes, each bomb's probability of destruction is fixed regardless of the total number of bombs dropped on that key part.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint on the total number of sorties (round trips) the aircraft can make, or is the only constraint on sorties the fuel budget?

## Turn 23 - User Simulator

The only constraint on sorties is the fuel budget.

## Turn 24 - Generic Agent

QUESTION: Is the probability of success the sum over all subsets of key parts of size at least two, of the probability that exactly that subset is destroyed (with the rest surviving), where each part's destruction probability is computed from the bombs assigned to it?

## Turn 24 - User Simulator

Yes, that is correct.

## Turn 25 - Generic Agent

QUESTION: Is there any requirement that the aircraft must use at least one heavy bomb and at least one light bomb, or can it use only one type of bomb?

## Turn 25 - User Simulator

There is no requirement to use both types; the aircraft can use only one type of bomb.

## Turn 26 - Generic Agent

QUESTION: Is the fuel consumed for a sortie to key part i with a heavy bomb equal to (distance to i)×2/2 + (distance to i)×2/4 + 100, i.e., outbound distance divided by 2 km/L plus return distance divided by 4 km/L plus 100 liters?

## Turn 26 - User Simulator

Yes, that is correct.

## Turn 27 - Generic Agent

QUESTION: Is the fuel consumed for a sortie to key part i with a light bomb equal to (distance to i)×2/3 + (distance to i)×2/4 + 100, i.e., outbound distance divided by 3 km/L plus return distance divided by 4 km/L plus 100 liters?

## Turn 27 - User Simulator

Yes, that is correct.

## Turn 28 - Generic Agent

QUESTION: Is the probability that key part i is destroyed equal to 1 minus the product of (1 minus p) for each bomb dropped on part i, where p is the destruction probability of that bomb type on that part?

## Turn 28 - User Simulator

Yes, that is correct.

## Turn 29 - Generic Agent

QUESTION: Is the probability of mission success equal to the sum over all subsets of key parts of size at least two, of the probability that exactly that subset is destroyed (with the rest surviving)?

## Turn 29 - User Simulator

Yes, that is correct.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the total number of sorties (round trips) must not exceed some maximum, or is the only constraint on sorties the fuel budget?

## Turn 30 - User Simulator

The only constraint on sorties is the fuel budget.