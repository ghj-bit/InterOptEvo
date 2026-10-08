## Turn 1 - Generic Agent

QUESTION: When a marshaling station is not used at all (zero flow through it), is its fixed cost f_k still incurred, or is it charged only when the station is actually used?

## Turn 1 - User Simulator

The fixed cost f_k is charged only when the station is actually used. If there is zero flow through a marshaling station, its fixed cost is not incurred.

## Turn 2 - Generic Agent

QUESTION: Is the demand at each demand point j required to be met exactly (total received equals b_j), or is it allowed to be under-met (total received at most b_j)?

## Turn 2 - User Simulator

The demand at each demand point j must be met exactly. The total quantity received at each demand point must equal its demand b_j.

## Turn 3 - Generic Agent

QUESTION: Is the objective to minimize the total cost, where total cost equals the sum of all unit transportation costs (production-to-station plus station-to-demand) plus the fixed costs of the stations that are used?

## Turn 3 - User Simulator

Yes, the objective is to minimize the total cost, which includes both the unit transportation costs (from production points to marshaling stations and from marshaling stations to demand points) and the fixed costs of the marshaling stations that are actually used.

## Turn 4 - Generic Agent

QUESTION: Can a production point ship directly to a demand point without going through a marshaling station, or is it mandatory that every unit of shipment passes through exactly one marshaling station?

## Turn 4 - User Simulator

It is mandatory that every unit of shipment passes through exactly one marshaling station. Production points cannot ship directly to demand points.

## Turn 5 - Generic Agent

QUESTION: Is the transshipment capacity q_k of a marshaling station a limit on the total quantity flowing through it (i.e., the sum of all incoming shipments from production points, which must equal the sum of all outgoing shipments to demand points)?

## Turn 5 - User Simulator

Yes, the transshipment capacity q_k is a limit on the total quantity flowing through the marshaling station. The total quantity transshipped through station k (which is the sum of all incoming shipments from production points, equal to the sum of all outgoing shipments to demand points) must not exceed q_k.

## Turn 6 - Generic Agent

QUESTION: Is the production output a_i a limit on the total quantity shipped out from production point i (i.e., the sum of all shipments from i to all marshaling stations must not exceed a_i), or must production point i ship out exactly a_i units?

## Turn 6 - User Simulator

The production output a_i is a limit on the total quantity shipped out from production point i. The sum of all shipments from production point i to all marshaling stations must not exceed a_i. It is not required to ship out exactly a_i units.

## Turn 7 - Generic Agent

QUESTION: Is there any restriction on how much a single production point can ship to a single marshaling station, or is the only limit on the production-to-station flow the production point's total output a_i and the station's total capacity q_k?

## Turn 7 - User Simulator

The only limits on the production-to-station flow are the production point's total output a_i and the station's total capacity q_k. There is no separate restriction on how much a single production point can ship to a single marshaling station.

## Turn 8 - Generic Agent

QUESTION: Is there any restriction on how much a single marshaling station can ship to a single demand point, or is the only limit on the station-to-demand flow the station's total capacity q_k and the demand point's exact demand b_j?

## Turn 8 - User Simulator

The only limits on the station-to-demand flow are the station's total capacity q_k and the demand point's exact demand b_j. There is no separate restriction on how much a single marshaling station can ship to a single demand point.

## Turn 9 - Generic Agent

QUESTION: Are the shipment quantities allowed to be any non-negative real numbers (continuous), or must they be whole numbers (integers)?

## Turn 9 - User Simulator

The shipment quantities are allowed to be any non-negative real numbers (continuous). They do not have to be whole numbers.

## Turn 10 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments must be split only among stations that are "opened" (i.e., used), or can a production point send a positive amount to a station even if that station's fixed cost is not being charged?

## Turn 10 - User Simulator

A production point can only send a positive amount to a station if that station is "opened" (i.e., used). If a station is not used, no shipments can flow through it, and its fixed cost is not charged.

## Turn 11 - Generic Agent

QUESTION: Is there any requirement that a marshaling station must be "opened" (incurring its fixed cost) before it can send shipments to demand points, or can a station send shipments to demand points without being opened?

## Turn 11 - User Simulator

A marshaling station must be "opened" (incurring its fixed cost) before it can send shipments to demand points. A station cannot send shipments to demand points without being opened.

## Turn 12 - Generic Agent

QUESTION: Is there any requirement that a station must receive shipments from at least one production point before it can be considered "opened" and send shipments to demand points, or can a station be opened and send shipments to demand points even if it receives zero shipments from production points?

## Turn 12 - User Simulator

A station must receive shipments from at least one production point before it can be considered "opened" and send shipments to demand points. A station cannot be opened and send shipments to demand points if it receives zero shipments from production points.

## Turn 13 - Generic Agent

QUESTION: Is there any requirement that a station must send shipments to at least one demand point before it can be considered "opened," or can a station be opened (incurring its fixed cost) and receive shipments from production points even if it sends zero shipments to demand points?

## Turn 13 - User Simulator

A station must send shipments to at least one demand point before it can be considered "opened." A station cannot be opened (incurring its fixed cost) and receive shipments from production points if it sends zero shipments to demand points.

## Turn 14 - Generic Agent

QUESTION: Is there any requirement that a production point must ship to at least one station, or can a production point ship zero total units (i.e., not participate at all) as long as its shipments do not exceed a_i?

## Turn 14 - User Simulator

A production point can ship zero total units (i.e., not participate at all) as long as its shipments do not exceed a_i. There is no requirement that a production point must ship to at least one station.

## Turn 15 - Generic Agent

QUESTION: Is there any requirement that a demand point must receive shipments from at least one station, or can a demand point receive zero total units (i.e., not be served) as long as its total received equals b_j?

## Turn 15 - User Simulator

A demand point must receive shipments from at least one station. Since the total received at each demand point must equal its demand b_j, and b_j is positive, a demand point cannot receive zero total units.

## Turn 16 - Generic Agent

QUESTION: Is there any requirement that a station's incoming flow from production points must exactly equal its outgoing flow to demand points (i.e., no storage or loss at the station), or can a station receive more than it sends out (storing the excess) or send out more than it receives?

## Turn 16 - User Simulator

A station's incoming flow from production points must exactly equal its outgoing flow to demand points. There is no storage or loss at the station.

## Turn 17 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a particular station must be zero if that station is not opened, or is the only restriction that a station cannot be opened (incurring fixed cost) unless it receives shipments from at least one production point and sends shipments to at least one demand point?

## Turn 17 - User Simulator

A production point's shipments to a particular station must be zero if that station is not opened.

## Turn 18 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a particular demand point must be zero if that station is not opened, or is the only restriction that a station cannot be opened (incurring fixed cost) unless it receives shipments from at least one production point and sends shipments to at least one demand point?

## Turn 18 - User Simulator

A station's shipments to a particular demand point must be zero if that station is not opened.

## Turn 19 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a station must be zero if that production point ships zero total units, or can a production point ship zero total units while still having positive shipments to some stations (which would be offset by negative shipments to other stations)?

## Turn 19 - User Simulator

A production point's shipments to a station must be zero if that production point ships zero total units. Shipments cannot be negative, so a production point cannot have positive shipments to some stations offset by negative shipments to others.

## Turn 20 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a demand point must be zero if that station sends zero total units to all demand points, or can a station send zero total units while still having positive shipments to some demand points (which would be offset by negative shipments to other demand points)?

## Turn 20 - User Simulator

A station's shipments to a demand point must be zero if that station sends zero total units to all demand points. Shipments cannot be negative, so a station cannot have positive shipments to some demand points offset by negative shipments to others.

## Turn 21 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a station must be zero if that station sends zero total units to all demand points, or can a production point ship positive units to a station that sends zero total units to all demand points?

## Turn 21 - User Simulator

A production point's shipments to a station must be zero if that station sends zero total units to all demand points.

## Turn 22 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a demand point must be zero if that station receives zero total units from all production points, or can a station send positive units to a demand point while receiving zero total units from all production points?

## Turn 22 - User Simulator

A station's shipments to a demand point must be zero if that station receives zero total units from all production points.

## Turn 23 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a station must be zero if that production point ships zero total units to all stations, or can a production point ship positive units to a station while shipping zero total units to all stations?

## Turn 23 - User Simulator

A production point's shipments to a station must be zero if that production point ships zero total units to all stations.

## Turn 24 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a demand point must be zero if that demand point receives zero total units from all stations, or can a station send positive units to a demand point while that demand point receives zero total units from all stations?

## Turn 24 - User Simulator

A station's shipments to a demand point must be zero if that demand point receives zero total units from all stations.

## Turn 25 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a station must be zero if that station is not opened, or can a production point ship positive units to a station that is not opened?

## Turn 25 - User Simulator

A production point's shipments to a station must be zero if that station is not opened.

## Turn 26 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a demand point must be zero if that station is not opened, or can a station send positive units to a demand point while the station is not opened?

## Turn 26 - User Simulator

A station's shipments to a demand point must be zero if that station is not opened.

## Turn 27 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a station must be zero if that production point ships zero total units to all stations, or can a production point ship positive units to a station while shipping zero total units to all stations?

## Turn 27 - User Simulator

A production point's shipments to a station must be zero if that production point ships zero total units to all stations.

## Turn 28 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a demand point must be zero if that station sends zero total units to all demand points, or can a station send positive units to a demand point while sending zero total units to all demand points?

## Turn 28 - User Simulator

A station's shipments to a demand point must be zero if that station sends zero total units to all demand points.

## Turn 29 - Generic Agent

QUESTION: Is there any requirement that a production point's shipments to a station must be zero if that station receives zero total units from all production points, or can a production point ship positive units to a station that receives zero total units from all production points?

## Turn 29 - User Simulator

A production point's shipments to a station must be zero if that station receives zero total units from all production points.

## Turn 30 - Generic Agent

QUESTION: Is there any requirement that a station's shipments to a demand point must be zero if that station sends zero total units to all demand points, or can a station send positive units to a demand point while sending zero total units to all demand points?

## Turn 30 - User Simulator

A station's shipments to a demand point must be zero if that station sends zero total units to all demand points.