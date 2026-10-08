## Turn 1 - Generic Agent

QUESTION: How should travel time between two locations be computed from the given coordinates — as Euclidean distance divided by a constant speed (in which case, what speed, e.g., 1 unit per minute), or as straight-line distance in minutes directly (i.e., travel time equals the Euclidean distance value)?

## Turn 1 - User Simulator

The travel time between two locations is the straight-line (Euclidean) distance in minutes directly. In other words, travel time equals the Euclidean distance value; there is no separate speed conversion.

## Turn 2 - Generic Agent

QUESTION: Should the objective minimize total distance traveled (sum of Euclidean distances over all arcs used, including the return to the depot), or total travel time (which, per your answer, is numerically the same)?

## Turn 2 - User Simulator

The objective is to minimize the total distance traveled by all vehicles.

## Turn 3 - Generic Agent

QUESTION: Should each truck that is used start at the depot and return to the depot after its last customer, or is it acceptable for a truck to end its route at the last customer served?

## Turn 3 - User Simulator

Each truck that is used must start at the depot and return to the depot after its last customer.

## Turn 4 - Generic Agent

QUESTION: Is there a limit on how many customers a single truck can visit on one route, or is the only per-route restriction the 200-unit capacity?

## Turn 4 - User Simulator

The only per-route restriction is the 200-unit capacity. There is no separate limit on the number of customers a single truck can visit.

## Turn 5 - Generic Agent

QUESTION: Can a truck leave the depot at any time within the depot's operating window [0, 1236], or must it depart at time 0?

## Turn 5 - User Simulator

A truck can leave the depot at any time within the depot's operating window [0, 1236]. It does not have to depart at time 0.

## Turn 6 - Generic Agent

QUESTION: Must a truck return to the depot by the end of the depot's operating window (time 1236), or is there no deadline for the return?

## Turn 6 - User Simulator

A truck must return to the depot by the end of the depot's operating window, time 1236.

## Turn 7 - Generic Agent

QUESTION: If a truck arrives at a customer before the customer's time window opens, it waits until the window opens and then begins service — is that waiting time counted as part of the route's timeline (i.e., it delays subsequent customers), or is it free and does not affect the schedule?

## Turn 7 - User Simulator

The waiting time is counted as part of the route's timeline. It delays subsequent customers.

## Turn 8 - Generic Agent

QUESTION: Are all 20 customers required to be served (i.e., every customer must be assigned to exactly one route), or is it acceptable to leave some customers unserved?

## Turn 8 - User Simulator

All 20 customers are required to be served. Every customer must be assigned to exactly one route.

## Turn 9 - Generic Agent

QUESTION: Is the service duration of 90 minutes the same for every customer, or does it vary by customer?

## Turn 9 - User Simulator

The service duration is 90 minutes for every customer.

## Turn 10 - Generic Agent

QUESTION: When a truck arrives at a customer exactly at the start of the customer's time window, is that considered on time (service can begin immediately), or must it arrive strictly after the window opens?

## Turn 10 - User Simulator

Arriving exactly at the start of the customer's time window is considered on time. Service can begin immediately.

## Turn 11 - Generic Agent

QUESTION: When a truck arrives at a customer exactly at the end of the customer's time window, is that considered on time (service can begin at that moment), or must it arrive strictly before the window closes?

## Turn 11 - User Simulator

Arriving exactly at the end of the customer's time window is considered on time. Service can begin at that moment.

## Turn 12 - Generic Agent

QUESTION: Can a truck visit the same customer more than once on its route, or must each customer be visited at most once?

## Turn 12 - User Simulator

Each customer must be visited at most once.

## Turn 13 - Generic Agent

QUESTION: Is there a maximum route duration (e.g., a maximum number of minutes a single truck can be out), or is the only time-related constraint the customer time windows and the depot return deadline of 1236?

## Turn 13 - User Simulator

There is no separate maximum route duration. The only time-related constraints are the customer time windows and the depot return deadline of 1236.

## Turn 14 - Generic Agent

QUESTION: If a truck is not used at all (i.e., fewer than 5 trucks are needed), is that allowed, or must exactly 5 trucks be dispatched?

## Turn 14 - User Simulator

It is allowed to use fewer than 5 trucks. At most 5 trucks can be used, but it is not required to dispatch all 5.

## Turn 15 - Generic Agent

QUESTION: When computing the distance for the objective, should the distance from the last customer back to the depot be included in the total distance traveled?

## Turn 15 - User Simulator

Yes, the distance from the last customer back to the depot is included in the total distance traveled.

## Turn 16 - Generic Agent

QUESTION: Are the coordinates given in the table in the same units as the Euclidean distance used for both travel time and the objective, so that the distance value serves double duty as both the time (in minutes) and the distance (in the objective)?

## Turn 16 - User Simulator

Yes, the coordinates are in the same units. The Euclidean distance value serves as both the travel time (in minutes) and the distance for the objective.

## Turn 17 - Generic Agent

QUESTION: Is there any fixed cost per truck used, or is the objective purely the total distance traveled with no penalty for using more trucks?

## Turn 17 - User Simulator

There is no fixed cost per truck used. The objective is purely to minimize the total distance traveled, with no penalty for using more trucks.

## Turn 18 - Generic Agent

QUESTION: Can a truck pass through (drive past) a customer's location without stopping to serve it, or must it stop at every customer it passes by?

## Turn 18 - User Simulator

A truck can pass through a customer's location without stopping to serve it. It is not required to stop at every customer it passes by.

## Turn 19 - Generic Agent

QUESTION: Is the depot's operating window [0, 1236] a constraint that applies to both the departure and return of every truck, or does it only apply to the return (i.e., trucks can depart at any time but must return by 1236)?

## Turn 19 - User Simulator

The depot's operating window [0, 1236] applies to both the departure and return of every truck.

## Turn 20 - Generic Agent

QUESTION: If a truck departs the depot and its first customer's time window opens at, say, minute 912, is the truck allowed to wait at the depot until minute 912 before departing, or must it depart immediately and wait at the customer?

## Turn 20 - User Simulator

The truck is allowed to wait at the depot until minute 912 before departing.

## Turn 21 - Generic Agent

QUESTION: Can a truck visit customers in any order, or is there a required sequence (e.g., by customer ID or by time window)?

## Turn 21 - User Simulator

A truck can visit customers in any order. There is no required sequence.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served across all routes combined, or is the only constraint that each of the 20 customers is served exactly once?

## Turn 22 - User Simulator

The only constraint is that each of the 20 customers is served exactly once. There is no separate constraint on the total number of customers served across all routes combined.

## Turn 23 - Generic Agent

QUESTION: Can a truck serve customers from different "clusters" or regions in a single route, or is there any geographic restriction on which customers can be grouped together on the same route?

## Turn 23 - User Simulator

There is no geographic restriction. A truck can serve customers from any locations in a single route, as long as the other constraints (capacity, time windows, etc.) are satisfied.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint on the total number of routes (i.e., the number of trucks actually used), or is the only constraint that at most 5 trucks can be used?

## Turn 24 - User Simulator

The only constraint is that at most 5 trucks can be used. There is no minimum number of routes required.

## Turn 25 - Generic Agent

QUESTION: When a truck arrives at a customer and the customer's time window has already closed (i.e., the truck arrives after the end of the window), is that a hard violation (the route is infeasible), or is there a penalty for late arrival?

## Turn 25 - User Simulator

Arriving after the end of the customer's time window is a hard violation. The route is infeasible.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served by a single truck in terms of the number of stops, or is the only per-route constraint the 200-unit capacity?

## Turn 26 - User Simulator

The only per-route constraint is the 200-unit capacity. There is no separate limit on the number of stops a single truck can make.

## Turn 27 - Generic Agent

QUESTION: Can a truck visit the depot in the middle of its route (i.e., return to the depot, pick up more goods, and continue to more customers), or must each truck's route be a single continuous path from depot to depot with no intermediate depot visits?

## Turn 27 - User Simulator

Each truck's route must be a single continuous path from the depot to the depot with no intermediate depot visits.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served by all trucks combined, or is the only constraint that each of the 20 customers is served exactly once?

## Turn 28 - User Simulator

The only constraint is that each of the 20 customers is served exactly once. There is no separate constraint on the total number of customers served by all trucks combined.

## Turn 29 - Generic Agent

QUESTION: Can a truck's route include a customer whose time window is entirely before the truck's departure time from the depot, as long as the truck can still arrive within that customer's time window?

## Turn 29 - User Simulator

No. If a customer's time window is entirely before the truck's departure time from the depot, the truck cannot arrive within that customer's time window, so that customer cannot be included in that truck's route.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served by a single truck in terms of the total service time, or is the only per-route constraint the 200-unit capacity?

## Turn 30 - User Simulator

The only per-route constraint is the 200-unit capacity. There is no separate constraint on the total service time for a single truck.