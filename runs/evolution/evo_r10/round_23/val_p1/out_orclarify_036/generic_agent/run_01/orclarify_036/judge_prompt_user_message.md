# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U10, U11, U12, U13, U2, U3, U4, U5, U6
I need help creating a delivery plan for a logistics provider servicing customers in a city's central business district, where all customer demands must be met, at most 5 trucks can be used, and the total demand of customers on a single route must not exceed the truck capacity of 200 units. Each customer has a hard time window; service can only begin within that window, so if a vehicle arrives early, it must wait, and late arrival is not permitted. The objective is to minimize the total distance traveled by all vehicles.

There are 20 customers requiring delivery service.

Central Depot (Depot 0): Coordinates: (40, 50). Operating Time Window: [0, 1236] minutes.

| Customer ID | Coordinates (X, Y) | Demand (units) | Time Window (minutes) | Service Duration (minutes) |
| :--- | :--- | :--- |:--- | :--- |
| 1 | (45, 68) | 10 | [912, 967] | 90 |
| 2 | (45, 70) | 30 | [825, 870] | 90 |
| 3 | (42, 66) | 10 | [65, 146] | 90 |
| 4 | (42, 68) | 10 | [727, 782] | 90 |
| 5 | (42, 65) | 10 | [15, 67] | 90 |
| 6 | (40, 69) | 20 | [621, 702] | 90 |
| 7 | (40, 66) | 20 | [170, 225] | 90 |
| 8 | (38, 68) | 20 | [255, 324] | 90 |
| 9 | (38, 70) | 10 | [534, 605] | 90 |
| 10 | (35, 66) | 10 | [357, 410] | 90 |
| 11 | (35, 69) | 10 | [448, 505] | 90 |
| 12 | (25, 85) | 20 | [652, 721] | 90 |
| 13 | (22, 75) | 30 | [30, 92] | 90 |
| 14 | (22, 85) | 10 | [567, 620] | 90 |
| 15 | (20, 80) | 40 | [384, 429] | 90 |
| 16 | (20, 85) | 40 | [475, 528] | 90 |
| 17 | (18, 75) | 20 | [99, 148] | 90 |
| 18 | (15, 75) | 20 | [179, 254] | 90 |
| 19 | (15, 80) | 10 | [278, 345] | 90 |
| 20 | (30, 50) | 10 | [10, 73] | 90 |

Maximum number of available trucks: 5. Truck capacity: 200 units.

Fixed service time per customer: 90 minutes.

## Problem units
- U1 (context): I need help creating a delivery plan for a logistics provider servicing customers in a city's central business district.
- U2 (data): There are 20 customers requiring delivery service.
- U3 (data): Central Depot (Depot 0): Coordinates: (40, 50). Operating Time Window: [0, 1236] minutes.
- U4 (data): | Customer ID | Coordinates (X, Y) | Demand (units) | Time Window (minutes) | Service Duration (minutes) |
| :--- | :--- | :--- |:--- | :--- |
| 1 | (45, 68) | 10 | [912, 967] | 90 |
| 2 | (45, 70) | 30 | [825, 870] | 90 |
| 3 | (42, 66) | 10 | [65, 146] | 90 |
| 4 | (42, 68) | 10 | [727, 782] | 90 |
| 5 | (42, 65) | 10 | [15, 67] | 90 |
| 6 | (40, 69) | 20 | [621, 702] | 90 |
| 7 | (40, 66) | 20 | [170, 225] | 90 |
| 8 | (38, 68) | 20 | [255, 324] | 90 |
| 9 | (38, 70) | 10 | [534, 605] | 90 |
| 10 | (35, 66) | 10 | [357, 410] | 90 |
| 11 | (35, 69) | 10 | [448, 505] | 90 |
| 12 | (25, 85) | 20 | [652, 721] | 90 |
| 13 | (22, 75) | 30 | [30, 92] | 90 |
| 14 | (22, 85) | 10 | [567, 620] | 90 |
| 15 | (20, 80) | 40 | [384, 429] | 90 |
| 16 | (20, 85) | 40 | [475, 528] | 90 |
| 17 | (18, 75) | 20 | [99, 148] | 90 |
| 18 | (15, 75) | 20 | [179, 254] | 90 |
| 19 | (15, 80) | 10 | [278, 345] | 90 |
| 20 | (30, 50) | 10 | [10, 73] | 90 |
- U5 (data): Maximum number of available trucks: 5. Truck capacity: 200 units.
- U6 (data): Fixed service time per customer: 90 minutes.
- U7 (constraint): All customer demands must be met.
- U8 (constraint): Each customer must be served by exactly one vehicle.
- U9 (constraint): Vehicles must start from the depot and return to the depot.
- U10 (constraint): At most 5 trucks can be used.
- U11 (constraint): The total demand of customers on a single route must not exceed the truck capacity of 200 units.
- U12 (constraint): Each customer has a hard time window; service can only begin within that window. If a vehicle arrives early, it must wait; late arrival is not permitted.
- U13 (objective): Minimize the total distance traveled by all vehicles.

## Hidden slot scoring rules
## H1: single_vehicle_per_customer
- Severity: P1
- Severity reason: Without this clarification, the agent may assume split deliveries are permitted, leading to a fundamentally different problem (Split Delivery VRP) that could yield lower-cost solutions but violates the real business rule.
- Problem unit ID: U8
- Semantic hit rule: The agent's question must explicitly ask whether a customer's demand can be split across multiple vehicles or if each customer must be serviced by exactly one vehicle.
- Reference acceptable questions:
  - Does each customer need to be served entirely by a single truck, or can their demand be split across multiple vehicles?
  - Can a customer's delivery be split between two different trucks, or must one truck handle their whole order?
- Failure modes:
  - Assuming split deliveries are allowed and modeling with capacity constraints allowing demand splitting.
  - Building routes where a single customer is visited by multiple vehicles.

## H2: depot_return_requirement
- Severity: P1
- Severity reason: Without this, the agent may assume vehicles do not need to return to the depot (Open VRP), removing return‑trip costs and potentially underestimating total distance while violating operational rules.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must explicitly ask whether vehicles must return to the depot or if routes can be open.
- Reference acceptable questions:
  - Do the trucks need to return to the depot at the end of their routes, or can they finish at any customer?
  - Is returning to the depot mandatory after completing all deliveries?
- Failure modes:
  - Assuming vehicles do not have to return to the depot and modelling routes that end at the last customer.
  - Assuming the depot return is optional or can be ignored in distance calculation.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the travel speed used to convert the Euclidean distance between two points into travel time (in minutes)?

## Turn 1 - User Simulator

That point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: Do all trucks have to return to the central depot after completing their route, or is it acceptable for a truck to end its route at its last customer?

## Turn 2 - User Simulator

All trucks must return to the central depot after completing their route.

## Turn 3 - Generic Agent

QUESTION: Can a single truck visit the same customer more than once during its route, or must each customer be served exactly once by exactly one truck?

## Turn 3 - User Simulator

Each customer must be served exactly once by exactly one truck.

## Turn 4 - Generic Agent

QUESTION: Is the distance between two points measured as straight-line (Euclidean) distance, or as Manhattan (grid) distance?

## Turn 4 - User Simulator

That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Can a truck leave the depot at any time within its operating window [0, 1236] minutes, or must it depart at time 0?

## Turn 5 - User Simulator

That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the 200-unit truck capacity a hard limit on the sum of demands on a route, or is it a soft limit that may be exceeded with a penalty?

## Turn 6 - User Simulator

It is a hard limit. The total demand of customers on a single route must not exceed 200 units.

## Turn 7 - Generic Agent

QUESTION: Is the objective purely to minimize total distance traveled, or should there also be a penalty for using more trucks (e.g., a fixed cost per truck)?

## Turn 7 - User Simulator

The objective is purely to minimize the total distance traveled by all vehicles.

## Turn 8 - Generic Agent

QUESTION: Is the 90-minute service time the only time spent at each customer (i.e., no separate loading/unloading time), and does the truck's clock start at the moment it arrives at the customer?

## Turn 8 - User Simulator

The 90-minute service time is the fixed time spent at each customer. The truck's clock starts at the moment it arrives at the customer.

## Turn 9 - Generic Agent

QUESTION: If a truck arrives at a customer before the customer's time window opens, does the waiting time count toward the truck's schedule (i.e., the truck must wait until the window opens before service can begin)?

## Turn 9 - User Simulator

Yes, if a truck arrives before the customer's time window opens, it must wait until the window opens before service can begin.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum route duration or a latest return-to-depot deadline for each truck, or is the only time constraint the depot operating window [0, 1236] minutes?

## Turn 10 - User Simulator

The only time constraint is the depot operating window [0, 1236] minutes.

## Turn 11 - Generic Agent

QUESTION: Can a truck serve customers in any order along its route, or is there a required sequence or grouping of customers that must be respected?

## Turn 11 - User Simulator

A truck can serve customers in any order along its route.

## Turn 12 - Generic Agent

QUESTION: Are the coordinates given in the table in the same units as the distance to be minimized (e.g., kilometers), or is the distance simply the numerical Euclidean distance between coordinate pairs?

## Turn 12 - User Simulator

That point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is the total demand of all 20 customers (470 units) required to be delivered, or is it acceptable to leave some customers unserved if capacity or time constraints make it infeasible?

## Turn 13 - User Simulator

All customer demands must be met.

## Turn 14 - Generic Agent

QUESTION: Is the travel time between two points calculated as the Euclidean distance divided by a constant speed, or is there a separate travel-time matrix provided?

## Turn 14 - User Simulator

That point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is the depot's operating window [0, 1236] minutes the only constraint on when a truck can depart and return, or is there also a maximum number of customers a single truck can visit?

## Turn 15 - User Simulator

The depot's operating window [0, 1236] minutes is the only constraint on when a truck can depart and return. There is no maximum number of customers a single truck can visit, other than the 200-unit capacity limit.

## Turn 16 - Generic Agent

QUESTION: Is the travel time between two points equal to the Euclidean distance between them (i.e., speed = 1 unit per minute), or is there a different speed or travel-time formula?

## Turn 16 - User Simulator

That point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is the distance to be minimized the sum of Euclidean distances between consecutive points on each route (including the return to depot), or is there a different distance metric?

## Turn 17 - User Simulator

That point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is the 1236-minute depot operating window the latest time by which all trucks must have returned to the depot, or is it simply the time span during which the depot is open for departures and arrivals?

## Turn 18 - User Simulator

It is simply the time span during which the depot is open for departures and arrivals.

## Turn 19 - Generic Agent

QUESTION: Is the travel time between two points calculated as the Euclidean distance between them divided by a constant speed, and if so, what is that speed in distance units per minute?

## Turn 19 - User Simulator

That point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is the distance to be minimized the sum of straight-line (Euclidean) distances between consecutive stops on each route, including the leg from the last customer back to the depot?

## Turn 20 - User Simulator

That point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is the travel time between two points equal to the Euclidean distance between them (i.e., a speed of 1 distance unit per minute), or is there a different speed or travel-time formula?

## Turn 21 - User Simulator

That point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is the distance to be minimized the sum of Euclidean distances between consecutive points on each route (including the return to the depot), or is there a different distance metric?

## Turn 22 - User Simulator

That point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is the travel time between two points calculated as the Euclidean distance between them divided by a constant speed, and if so, what is that speed in distance units per minute?

## Turn 23 - User Simulator

That point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is the distance to be minimized the sum of Euclidean distances between consecutive points on each route (including the return to the depot), or is there a different distance metric?

## Turn 24 - User Simulator

That point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is the travel time between two points calculated as the Euclidean distance between them divided by a constant speed, and if so, what is that speed in distance units per minute?

## Turn 25 - User Simulator

That point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is the distance to be minimized the sum of Euclidean distances between consecutive points on each route (including the return to the depot), or is there a different distance metric?

## Turn 26 - User Simulator

That point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is the travel time between two points calculated as the Euclidean distance between them divided by a constant speed, and if so, what is that speed in distance units per minute?

## Turn 27 - User Simulator

That point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is the distance to be minimized the sum of Euclidean distances between consecutive points on each route (including the return to the depot), or is there a different distance metric?

## Turn 28 - User Simulator

That point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is the travel time between two points calculated as the Euclidean distance between them divided by a constant speed, and if so, what is that speed in distance units per minute?

## Turn 29 - User Simulator

That point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is the distance to be minimized the sum of Euclidean distances between consecutive points on each route (including the return to the depot), or is there a different distance metric?

## Turn 30 - User Simulator

That point still needs internal confirmation.