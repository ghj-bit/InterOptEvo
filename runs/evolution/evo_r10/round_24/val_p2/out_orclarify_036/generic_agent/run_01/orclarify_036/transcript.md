## Turn 1 - Generic Agent

QUESTION: How should travel time between two points be computed from the given coordinates — should I use Euclidean distance (straight-line) as the travel time in minutes, or is there a different convention (e.g., Manhattan distance, or a speed factor applied to Euclidean distance)?

## Turn 1 - User Simulator

Use Euclidean distance (straight-line) between the coordinates as the travel time in minutes. There is no speed factor or Manhattan convention to apply.

## Turn 2 - Generic Agent

QUESTION: When a truck finishes its last customer and returns to the depot, does it need to arrive back at the depot within the depot's operating window [0, 1236] minutes, or is the return trip unconstrained (only the outbound departure from the depot at time 0 matters)?

## Turn 2 - User Simulator

The truck must arrive back at the depot within the depot's operating window [0, 1236] minutes.

## Turn 3 - Generic Agent

QUESTION: Can a truck leave the depot at any time during its operating window [0, 1236], or must every truck depart the depot at time 0?

## Turn 3 - User Simulator

A truck can leave the depot at any time during its operating window [0, 1236].

## Turn 4 - Generic Agent

QUESTION: Do all 5 trucks start at the depot at time 0 (so a truck that is not used simply stays at the depot), or can a truck's route begin at any later time within the depot window as its first departure?

## Turn 4 - User Simulator

A truck's route can begin at any later time within the depot window [0, 1236] as its first departure.

## Turn 5 - Generic Agent

QUESTION: The objective is to minimize total distance traveled by all vehicles — should this total include the return leg from the last customer back to the depot, or only the distance traveled while serving customers (i.e., excluding the final return to depot)?

## Turn 5 - User Simulator

The total distance should include the return leg from the last customer back to the depot.

## Turn 6 - Generic Agent

QUESTION: If a truck is not used at all (i.e., it stays at the depot and serves no customers), does it contribute zero distance to the objective, or is there any fixed cost or distance associated with an unused truck?

## Turn 6 - User Simulator

An unused truck contributes zero distance to the objective.

## Turn 7 - Generic Agent

QUESTION: Is there a limit on how many customers a single truck can visit on one route (other than the capacity constraint of 200 units), or is the only per-route restriction the 200-unit capacity?

## Turn 7 - User Simulator

The only per-route restriction is the 200-unit capacity. There is no separate limit on the number of customers a single truck can visit.

## Turn 8 - Generic Agent

QUESTION: Does each customer need to be served by exactly one truck (i.e., its full demand is delivered in a single visit), or can a customer's demand be split across multiple trucks/visits?

## Turn 8 - User Simulator

Each customer must be served by exactly one truck. Its full demand is delivered in a single visit.

## Turn 9 - Generic Agent

QUESTION: When a truck arrives at a customer before the customer's time window opens, it waits until the window opens and then begins service. Is the service duration of 90 minutes counted starting from when the window opens (i.e., service ends at window-open + 90), regardless of how long the truck waited?

## Turn 9 - User Simulator

Yes. The 90-minute service duration starts when the time window opens, so service ends at window-open + 90, regardless of how long the truck waited.

## Turn 10 - Generic Agent

QUESTION: For the time-window feasibility check, is the constraint that the truck must *arrive* at the customer no later than the window's end time, or that *service must be completed* (arrival + wait + 90 min service) by the window's end time?

## Turn 10 - User Simulator

The constraint is that the truck must *arrive* at the customer no later than the window's end time.

## Turn 11 - Generic Agent

QUESTION: When a truck departs the depot, does it need to arrive at its first customer within that customer's time window (i.e., the same arrival-by-window-end rule applies to the first stop), or is the first stop treated differently?

## Turn 11 - User Simulator

The same arrival-by-window-end rule applies to the first stop. The truck must arrive at its first customer no later than that customer's time window end time.

## Turn 12 - Generic Agent

QUESTION: If a truck's route is empty (it serves no customers), is it simply not part of the solution, or does it still count toward the "at most 5 trucks" limit in a way that affects the model?

## Turn 12 - User Simulator

An empty route is simply not part of the solution. It does not count toward the "at most 5 trucks" limit.

## Turn 13 - Generic Agent

QUESTION: Is there any requirement that all used trucks must return to the depot by the same time, or can different trucks return at different times as long as each is within [0, 1236]?

## Turn 13 - User Simulator

Different trucks can return at different times, as long as each is within [0, 1236].

## Turn 14 - Generic Agent

QUESTION: Can a truck visit the same customer more than once (e.g., pass through a customer's location without serving it, or serve it, leave, and come back), or is each customer visited at most once in the entire solution?

## Turn 14 - User Simulator

Each customer is visited at most once in the entire solution.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint on the total number of customers that can be served per route beyond the 200-unit capacity, such as a maximum route duration or a maximum number of stops?

## Turn 15 - User Simulator

No. There is no maximum route duration or maximum number of stops. The only per-route constraint is the 200-unit capacity.

## Turn 16 - Generic Agent

QUESTION: Can a truck pass through a customer's location (i.e., travel along a path that goes through that customer's coordinates) without stopping to serve it, or must the truck only travel directly between the locations it actually serves?

## Turn 16 - User Simulator

A truck can pass through a customer's location without stopping to serve it.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that a truck cannot visit two customers at the same time (i.e., no two trucks can be at the same customer simultaneously), or is there no such restriction since each customer is served by exactly one truck?

## Turn 17 - User Simulator

There is no such restriction. Since each customer is served by exactly one truck, there is no constraint preventing two trucks from being at the same location at the same time.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint on the total number of routes (i.e., the number of trucks actually used) that must be at least some minimum, or can the solution use as few as 1 truck if capacity and time windows allow?

## Turn 18 - User Simulator

There is no minimum number of routes. The solution can use as few as 1 truck if capacity and time windows allow.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that a truck cannot serve a customer if the truck's arrival time is before the customer's time window opens, other than the waiting rule (i.e., the truck must wait until the window opens)?

## Turn 19 - User Simulator

No. The only constraint is the waiting rule: if the truck arrives before the window opens, it must wait until the window opens to begin service.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that a truck cannot depart the depot before time 0, or is time 0 the earliest possible departure time?

## Turn 20 - User Simulator

Time 0 is the earliest possible departure time.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that a truck cannot arrive at the depot after time 1236, or is 1236 the latest possible arrival time at the depot?

## Turn 21 - User Simulator

1236 is the latest possible arrival time at the depot.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that a truck cannot arrive at a customer before time 0, or is time 0 the earliest possible arrival time at any customer?

## Turn 22 - User Simulator

Time 0 is the earliest possible arrival time at any customer.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that a truck cannot depart a customer before the service is completed (i.e., the truck must wait the full 90 minutes of service before departing), or can the truck depart before service is complete?

## Turn 23 - User Simulator

The truck must wait the full 90 minutes of service before departing.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that a truck cannot arrive at a customer after the customer's time window has closed, other than the arrival-by-window-end rule?

## Turn 24 - User Simulator

No. The arrival-by-window-end rule is the only constraint regarding arrival time relative to the customer's time window.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that a truck cannot depart the depot after time 1236, or is 1236 the latest possible departure time from the depot?

## Turn 25 - User Simulator

1236 is the latest possible departure time from the depot.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that a truck cannot arrive at the depot before time 0, or is time 0 the earliest possible arrival time at the depot?

## Turn 26 - User Simulator

Time 0 is the earliest possible arrival time at the depot.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that a truck cannot depart a customer before the customer's time window opens, or can the truck depart a customer at any time after service is completed?

## Turn 27 - User Simulator

The truck can depart a customer at any time after service is completed. There is no constraint preventing departure before the customer's time window opens, because service cannot begin until the window opens, so the truck would not be at the customer before that point.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that a truck cannot arrive at a customer before the customer's time window opens, other than the waiting rule?

## Turn 28 - User Simulator

No. The waiting rule is the only constraint regarding arrival before the customer's time window opens.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that a truck cannot depart the depot before the first customer's time window opens, or can the truck depart the depot at any time within [0, 1236] regardless of when its first customer's window opens?

## Turn 29 - User Simulator

The truck can depart the depot at any time within [0, 1236] regardless of when its first customer's window opens.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that a truck cannot arrive at a customer after the depot's operating window closes (time 1236), or is the only constraint on arrival at a customer the customer's own time window?

## Turn 30 - User Simulator

The only constraint on arrival at a customer is the customer's own time window.