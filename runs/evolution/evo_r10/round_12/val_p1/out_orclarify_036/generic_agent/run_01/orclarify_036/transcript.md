## Turn 1 - Generic Agent

QUESTION: How should travel time between two points be computed from the given coordinates — as Euclidean distance divided by a constant speed (and if so, what speed, e.g., 1 unit per minute), or as straight-line distance in minutes directly?

## Turn 1 - User Simulator

The travel time between two points is computed as the straight-line (Euclidean) distance in minutes directly. There is no separate speed conversion; the distance value in coordinate units is used as the travel time in minutes.

## Turn 2 - Generic Agent

QUESTION: When a truck finishes its last customer and returns to the depot, does it need to arrive back at the depot by the end of the depot's operating window (1236 minutes), or is the return trip unconstrained as long as the route's customers are served within their time windows?

## Turn 2 - User Simulator

The truck must arrive back at the depot by the end of the depot's operating window (1236 minutes).

## Turn 3 - Generic Agent

QUESTION: Can a truck leave the depot at any time from 0 up to 1236 minutes, or must it depart at time 0?

## Turn 3 - User Simulator

A truck can leave the depot at any time from 0 up to 1236 minutes.

## Turn 4 - Generic Agent

QUESTION: If a truck is not used at all, is that allowed (i.e., can fewer than 5 trucks be deployed), and does an unused truck contribute zero distance to the objective?

## Turn 4 - User Simulator

Yes, fewer than 5 trucks can be deployed. An unused truck contributes zero distance to the objective.

## Turn 5 - Generic Agent

QUESTION: The objective is to minimize total distance traveled by all vehicles — does this include the distance from the depot to the first customer and from the last customer back to the depot, or only the distances between customers on a route?

## Turn 5 - User Simulator

The objective includes the distance from the depot to the first customer and from the last customer back to the depot.

## Turn 6 - Generic Agent

QUESTION: Can a single truck visit the same customer more than once, or must each customer be visited exactly once by exactly one truck?

## Turn 6 - User Simulator

Each customer must be visited exactly once by exactly one truck.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum number of customers a single truck can serve on one route (other than the capacity limit of 200 units), or is the only per-route limit the 200-unit capacity?

## Turn 7 - User Simulator

The only per-route limit is the 200-unit capacity. There is no separate maximum number of customers per route.

## Turn 8 - Generic Agent

QUESTION: When a truck arrives at a customer before the customer's time window opens, it waits until the window opens and then begins service — is the service duration of 90 minutes always fully completed within the customer's time window, or can service extend beyond the window's end as long as it started within the window?

## Turn 8 - User Simulator

Service can extend beyond the window's end as long as it started within the window.

## Turn 9 - Generic Agent

QUESTION: Are the coordinates and distances such that the Euclidean distance between any two points is always a whole number, or should I treat distances as continuous (real-valued) quantities?

## Turn 9 - User Simulator

Treat distances as continuous (real-valued) quantities.

## Turn 10 - Generic Agent

QUESTION: If a truck's route would require it to be at the depot at time 0 to start, but its first customer's time window doesn't open until later, is the truck simply idle at the depot until it departs, or must it depart exactly when it reaches the first customer's window?

## Turn 10 - User Simulator

The truck is simply idle at the depot until it departs. It does not have to depart exactly when it reaches the first customer's window; it can depart at any time that allows it to arrive at the first customer within that customer's time window.

## Turn 11 - Generic Agent

QUESTION: Is there any requirement that all trucks must return to the depot at the same time, or can each truck return at its own time as long as it's by 1236 minutes?

## Turn 11 - User Simulator

Each truck can return at its own time, as long as it is by 1236 minutes.

## Turn 12 - Generic Agent

QUESTION: Can a truck serve customers in any order, or is there a fixed sequence that must be followed?

## Turn 12 - User Simulator

A truck can serve customers in any order.

## Turn 13 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served across all routes combined, or is the only requirement that all 20 customers must be served?

## Turn 13 - User Simulator

The only requirement is that all 20 customers must be served.

## Turn 14 - Generic Agent

QUESTION: If a truck arrives at a customer exactly at the start of the customer's time window, is that considered on-time (i.e., the window is inclusive of its endpoints)?

## Turn 14 - User Simulator

Yes, arriving exactly at the start of the customer's time window is considered on-time. The window is inclusive of its endpoints.

## Turn 15 - Generic Agent

QUESTION: If a truck arrives at a customer exactly at the end of the customer's time window, is that still considered on-time (i.e., can service begin at the exact end of the window)?

## Turn 15 - User Simulator

Yes, arriving exactly at the end of the customer's time window is still considered on-time. Service can begin at the exact end of the window.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve two customers at the same time, or is it implicitly understood that each truck serves customers sequentially?

## Turn 16 - User Simulator

It is implicitly understood that each truck serves customers sequentially.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint on the total number of routes (i.e., the number of trucks actually used), or is the only limit that at most 5 trucks can be used?

## Turn 17 - User Simulator

The only limit is that at most 5 trucks can be used.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that a truck must return to the depot after serving its last customer, or can it end its route at the last customer's location?

## Turn 18 - User Simulator

A truck must return to the depot after serving its last customer.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served by a single truck in terms of time, or is the only time constraint that the truck must return to the depot by 1236 minutes?

## Turn 19 - User Simulator

The only time constraint is that the truck must return to the depot by 1236 minutes.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve a customer if the truck's arrival time at that customer would be after the customer's time window has closed, even if the truck could have arrived earlier but chose not to?

## Turn 20 - User Simulator

Yes, a truck cannot serve a customer if its arrival time is after the customer's time window has closed.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that a truck must depart the depot before its first customer's time window opens, or can it depart at any time as long as it arrives at the first customer within that customer's time window?

## Turn 21 - User Simulator

A truck can depart at any time as long as it arrives at the first customer within that customer's time window.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that a truck cannot wait at a customer's location after completing service, or can it wait there before departing to the next customer?

## Turn 22 - User Simulator

A truck can wait at a customer's location after completing service before departing to the next customer.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that a truck must serve customers in a specific geographic order, or can it serve them in any order as long as all time windows are respected?

## Turn 23 - User Simulator

A truck can serve customers in any order as long as all time windows are respected.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve a customer if the truck's departure time from the previous customer would cause it to arrive at the next customer after that customer's time window has closed, even if the truck could have departed earlier?

## Turn 24 - User Simulator

Yes, a truck cannot serve a customer if its arrival time is after that customer's time window has closed.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that a truck must return to the depot immediately after serving its last customer, or can it wait at the last customer's location before returning to the depot?

## Turn 25 - User Simulator

A truck can wait at the last customer's location before returning to the depot, as long as it arrives back at the depot by 1236 minutes.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve a customer if the truck's arrival time at that customer is before the customer's time window opens, even if the truck waits until the window opens?

## Turn 26 - User Simulator

No, a truck can serve a customer if it arrives before the time window opens, as long as it waits until the window opens and then begins service.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that a truck must serve all customers on its route within a single continuous trip, or can it return to the depot mid-route and then depart again to continue serving customers?

## Turn 27 - User Simulator

A truck must serve all customers on its route within a single continuous trip. It cannot return to the depot mid-route and then depart again to continue serving customers.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve a customer if the truck's arrival time at that customer is exactly at the end of the customer's time window, even if service can begin at that exact time?

## Turn 28 - User Simulator

No, a truck can serve a customer if it arrives exactly at the end of the customer's time window, as long as service begins at that exact time.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that a truck must serve customers in a specific order based on their time windows, or can it serve them in any order as long as all time windows are respected?

## Turn 29 - User Simulator

A truck can serve customers in any order as long as all time windows are respected.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve a customer if the truck's arrival time at that customer is after the customer's time window has closed, even if the truck could have arrived earlier but chose not to?

## Turn 30 - User Simulator

Yes, a truck cannot serve a customer if its arrival time is after the customer's time window has closed.