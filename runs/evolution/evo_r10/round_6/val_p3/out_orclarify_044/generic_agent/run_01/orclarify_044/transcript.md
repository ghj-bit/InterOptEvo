## Turn 1 - Generic Agent

QUESTION: Should the fixed cost f_k be incurred only if marshaling station k is actually used (i.e., some positive quantity is transshipped through it), and should the model be allowed to leave a station unused to save its fixed cost?

## Turn 1 - User Simulator

Yes. The fixed cost f_k is incurred only if marshaling station k is actually used (i.e., some positive quantity is transshipped through it). The model is allowed to leave a station unused to save its fixed cost.

## Turn 2 - Generic Agent

QUESTION: Is the objective to minimize the total cost, where total cost equals the sum of variable transportation costs (production-to-station plus station-to-demand) plus the fixed costs of the stations that are used?

## Turn 2 - User Simulator

Yes. The objective is to minimize the total cost, which includes both the variable transportation costs (production-to-station plus station-to-demand) and the fixed costs of the stations that are used.

## Turn 3 - Generic Agent

QUESTION: Must the total quantity delivered to each demand point j be exactly equal to its demand b_j, or is it acceptable to deliver less than b_j (i.e., demand is a minimum that must be met, or a target that may be unmet)?

## Turn 3 - User Simulator

The total quantity delivered to each demand point j must be exactly equal to its demand b_j.

## Turn 4 - Generic Agent

QUESTION: Is the total quantity shipped from each production point i allowed to be strictly less than its output a_i (i.e., a_i is an upper bound and unused production is simply left at the source), or must each production point ship exactly a_i?

## Turn 4 - User Simulator

The total quantity shipped from each production point i is allowed to be strictly less than its output a_i. The output a_i is an upper bound, and unused production is simply left at the source.

## Turn 5 - Generic Agent

QUESTION: Is the transshipment capacity q_k an upper bound on the total quantity passing through station k (i.e., the sum of all inflows to k equals the sum of all outflows from k, and that common total must not exceed q_k), or is q_k a limit on inflow only with outflow allowed to differ?

## Turn 5 - User Simulator

The transshipment capacity q_k is an upper bound on the total quantity passing through station k. The sum of all inflows to k equals the sum of all outflows from k, and that common total must not exceed q_k.

## Turn 6 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the fixed cost, is a station considered "used" (and thus charged f_k) if any positive amount is transshipped through it, and is there any minimum quantity that must pass through a station once it is opened?

## Turn 7 - User Simulator

A station is considered "used" (and thus charged f_k) if any positive amount is transshipped through it. There is no minimum quantity that must pass through a station once it is opened.

## Turn 8 - Generic Agent

QUESTION: Can a production point ship directly to a demand point without going through a marshaling station, or must every unit of material pass through exactly one marshaling station before reaching a demand point?

## Turn 8 - User Simulator

Every unit of material must pass through exactly one marshaling station before reaching a demand point.

## Turn 9 - Generic Agent

QUESTION: Can a single production point split its shipment across both marshaling stations (e.g., some of point 1's output goes to station 1 and some to station 2), or must each production point send all of its shipped quantity to a single station?

## Turn 9 - User Simulator

A single production point can split its shipment across both marshaling stations.

## Turn 10 - Generic Agent

QUESTION: Can a single marshaling station send its transshipped quantity to both demand points (i.e., split its outflow across demand points), or must each station send all of its outflow to a single demand point?

## Turn 10 - User Simulator

A single marshaling station can send its transshipped quantity to both demand points.

## Turn 11 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there any additional cost or penalty associated with production that is not shipped (i.e., left unused at the production point), or is unused production simply free with no cost impact?

## Turn 12 - User Simulator

Unused production is simply free with no cost impact.

## Turn 13 - Generic Agent

QUESTION: Are there any restrictions on which production points can ship to which marshaling stations, or which stations can ship to which demand points (e.g., are all i-to-k and k-to-j routes available), or are all routes fully available as shown in the cost tables?

## Turn 13 - User Simulator

All routes are fully available as shown in the cost tables.

## Turn 14 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is there any limit on how many times a unit of material can be transshipped, or does each unit pass through exactly one marshaling station (one transshipment) before reaching its demand point?

## Turn 15 - User Simulator

Each unit passes through exactly one marshaling station (one transshipment) before reaching its demand point.

## Turn 16 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is there any restriction that a production point's shipment to a station must be zero if that station is not opened (i.e., no fixed cost paid), or could a production point ship to a station without paying its fixed cost?

## Turn 17 - User Simulator

A production point's shipment to a station must be zero if that station is not opened (i.e., no fixed cost paid).

## Turn 18 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there any restriction on whether a demand point can receive material from both marshaling stations, or must each demand point receive all of its material from a single station?

## Turn 19 - User Simulator

A demand point can receive material from both marshaling stations.

## Turn 20 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any restriction that a station's outflow to a demand point must be zero if that station is not opened (i.e., no fixed cost paid), or could a station send material to a demand point without paying its fixed cost?

## Turn 21 - User Simulator

A station's outflow to a demand point must be zero if that station is not opened (i.e., no fixed cost paid).

## Turn 22 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is there any restriction on whether a production point can ship to a station that is not opened, or is the only restriction that no material can pass through an unopened station (both inflow and outflow must be zero)?

## Turn 23 - User Simulator

The only restriction is that no material can pass through an unopened station (both inflow and outflow must be zero).

## Turn 24 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any restriction on whether a demand point can receive material from a station that is not opened, or is the only restriction that no material can pass through an unopened station (both inflow and outflow must be zero)?

## Turn 25 - User Simulator

The only restriction is that no material can pass through an unopened station (both inflow and outflow must be zero).

## Turn 26 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there any restriction on whether a production point can ship to a station that is not opened, or is the only restriction that no material can pass through an unopened station (both inflow and outflow must be zero)?

## Turn 27 - User Simulator

The only restriction is that no material can pass through an unopened station (both inflow and outflow must be zero).

## Turn 28 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there any restriction on whether a demand point can receive material from a station that is not opened, or is the only restriction that no material can pass through an unopened station (both inflow and outflow must be zero)?

## Turn 29 - User Simulator

The only restriction is that no material can pass through an unopened station (both inflow and outflow must be zero).

## Turn 30 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole units (integers)?

## Turn 30 - User Simulator

The point still needs internal confirmation.