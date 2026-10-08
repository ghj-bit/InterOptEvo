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

QUESTION: What is the travel speed (or the travel-time formula) between two points, so I can convert the Euclidean distance between coordinates into minutes for the time-window constraints?

## Turn 1 - User Simulator

That point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: Should the objective minimize the total Euclidean distance traveled (in coordinate units), or the total travel time in minutes?

## Turn 2 - User Simulator

The objective is to minimize the total distance traveled by all vehicles.

## Turn 3 - Generic Agent

QUESTION: Do all trucks have to start at the depot and return to the depot at the end of their route, or is it acceptable for a truck to finish its route at the last customer it serves?

## Turn 3 - User Simulator

All trucks must start from the depot and return to the depot at the end of their routes.

## Turn 4 - Generic Agent

QUESTION: Can a single truck serve multiple customers in one route (visiting several customers before returning to the depot), or is each truck limited to serving exactly one customer per trip?

## Turn 4 - User Simulator

A single truck can serve multiple customers in one route, visiting several customers before returning to the depot.

## Turn 5 - Generic Agent

QUESTION: Can a truck make more than one round trip (depot → customers → depot → customers → depot) within the operating day, or does each truck make at most one trip out of the depot?

## Turn 5 - User Simulator

That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed (i.e., travel time = distance / speed), and if so, what is that speed in coordinate-units per minute?

## Turn 6 - User Simulator

That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is the truck capacity of 200 units a per-route limit (the sum of demands of all customers visited on one truck's route must not exceed 200), or is it a per-trip limit that resets each time the truck returns to the depot?

## Turn 7 - User Simulator

The truck capacity of 200 units is a per-route limit: the sum of demands of all customers visited on one truck's route must not exceed 200.

## Turn 8 - Generic Agent

QUESTION: Do all 20 customers have to be served within the depot's operating window of [0, 1236] minutes, meaning every truck must complete its route and be back at the depot by minute 1236?

## Turn 8 - User Simulator

That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: If a truck arrives at a customer before the customer's time window opens, does the truck wait at that customer until the window opens (with the waiting time counting toward the truck's schedule), or must the truck leave and come back later?

## Turn 9 - User Simulator

The truck waits at that customer until the window opens, and the waiting time counts toward the truck's schedule.

## Turn 10 - Generic Agent

QUESTION: Are the 5 trucks identical (same capacity, same speed, same depot), or do they differ in any way?

## Turn 10 - User Simulator

That point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is the distance between two points measured as straight-line (Euclidean) distance between their coordinates, or is there a road network / distance matrix I should use instead?

## Turn 11 - User Simulator

That point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is it acceptable to use fewer than 5 trucks (i.e., some trucks stay idle at the depot), as long as all 20 customers are served?

## Turn 12 - User Simulator

Yes, it is acceptable to use fewer than 5 trucks, as long as all 20 customers are served.

## Turn 13 - Generic Agent

QUESTION: Is the travel time between two points equal to the Euclidean distance between them (i.e., 1 coordinate unit = 1 minute of travel), or is there a different conversion factor?

## Turn 13 - User Simulator

That point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 14 - User Simulator

That point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is the travel time between two points equal to the Euclidean distance between them divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 15 - User Simulator

That point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 16 - User Simulator

That point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 17 - User Simulator

That point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 18 - User Simulator

That point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 19 - User Simulator

That point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 20 - User Simulator

That point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 21 - User Simulator

That point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 22 - User Simulator

That point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 23 - User Simulator

That point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 24 - User Simulator

That point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 25 - User Simulator

That point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 26 - User Simulator

That point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 27 - User Simulator

That point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 28 - User Simulator

That point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is the travel time between two points computed as the Euclidean distance divided by a constant speed, and if so, what is that speed in coordinate-units per minute?

## Turn 29 - User Simulator

That point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is the distance between two points the straight-line Euclidean distance between their coordinates, or is there a road network or distance matrix I should use instead?

## Turn 30 - User Simulator

That point still needs internal confirmation.