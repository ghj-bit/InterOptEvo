## Turn 1 - Generic Agent

QUESTION: How should travel time between two locations be computed from the given coordinates — as Euclidean distance divided by a constant speed (and if so, what speed, e.g., 1 unit per minute), or as Manhattan (grid) distance?

## Turn 1 - User Simulator

The travel time between two locations should be computed as the Euclidean distance divided by a constant speed of 1 unit per minute.

## Turn 2 - Generic Agent

QUESTION: Do all trucks have to start at the depot and return to the depot after finishing their route, or is it acceptable for a truck to end its route at the last customer it serves?

## Turn 2 - User Simulator

All trucks must start at the depot and return to the depot after finishing their route.

## Turn 3 - Generic Agent

QUESTION: Can a truck serve customers in any order as long as each customer's time window is respected, or is there a required sequence (e.g., customers must be visited in increasing ID order)?

## Turn 3 - User Simulator

A truck can serve customers in any order, as long as each customer's time window is respected.

## Turn 4 - Generic Agent

QUESTION: Can a single truck visit the same customer more than once (e.g., split service across multiple stops), or must each customer be served exactly once by exactly one truck?

## Turn 4 - User Simulator

Each customer must be served exactly once by exactly one truck.

## Turn 5 - Generic Agent

QUESTION: Is the 90-minute service time the only time spent at a customer (i.e., the truck arrives, waits if early, spends 90 minutes, then departs), or is there additional loading/unloading time at the depot before a truck can depart?

## Turn 5 - User Simulator

The 90-minute service time is the only time spent at a customer. There is no additional loading/unloading time at the depot before a truck can depart.

## Turn 6 - Generic Agent

QUESTION: Can a truck depart the depot at any time within the depot's operating window [0, 1236], or must it depart at time 0?

## Turn 6 - User Simulator

A truck can depart the depot at any time within the depot's operating window [0, 1236].

## Turn 7 - Generic Agent

QUESTION: Must a truck return to the depot by the end of the depot's operating window (time 1236), or can it return after 1236 as long as all customer time windows are met?

## Turn 7 - User Simulator

A truck must return to the depot by the end of the depot's operating window (time 1236).

## Turn 8 - Generic Agent

QUESTION: If a truck is not used in the plan, is it simply idle at the depot (no cost), or does every truck incur a fixed cost regardless of whether it is used?

## Turn 8 - User Simulator

If a truck is not used in the plan, it is simply idle at the depot with no cost.

## Turn 9 - Generic Agent

QUESTION: Is the objective purely to minimize total distance traveled (sum of Euclidean distances over all arcs used by all trucks), with no penalty for the number of trucks used?

## Turn 9 - User Simulator

Yes, the objective is purely to minimize the total distance traveled by all vehicles, with no penalty for the number of trucks used.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum route duration or maximum number of customers per truck beyond the capacity of 200 units and the depot closing time of 1236 minutes?

## Turn 10 - User Simulator

No, there is no maximum route duration or maximum number of customers per truck beyond the capacity of 200 units and the depot closing time of 1236 minutes.

## Turn 11 - Generic Agent

QUESTION: Can a truck wait at a customer location (i.e., arrive early and wait until the time window opens), or must it arrive exactly at the start of the time window?

## Turn 11 - User Simulator

A truck can wait at a customer location if it arrives early; it must wait until the time window opens before service can begin.

## Turn 12 - Generic Agent

QUESTION: Can a truck wait at the depot before departing (i.e., depart later than time 0), or must it depart immediately at time 0?

## Turn 12 - User Simulator

A truck can wait at the depot before departing; it does not have to depart immediately at time 0.

## Turn 13 - Generic Agent

QUESTION: Can a truck wait at an intermediate customer location (i.e., arrive early, wait, then serve), or must it arrive exactly at the start of the time window?

## Turn 13 - User Simulator

A truck can wait at an intermediate customer location if it arrives early; it must wait until the time window opens before service can begin.

## Turn 14 - Generic Agent

QUESTION: Is the total demand of all 20 customers (sum of all demands) within the capacity of 5 trucks (5 × 200 = 1000 units), or could the total demand exceed this?

## Turn 14 - User Simulator

The total demand of all 20 customers is 340 units, which is within the capacity of 5 trucks (5 × 200 = 1000 units).

## Turn 15 - Generic Agent

QUESTION: Can a truck visit the depot in the middle of its route (i.e., return to the depot, then depart again to serve more customers), or must each truck's route be a single continuous path from depot to depot without intermediate depot visits?

## Turn 15 - User Simulator

Each truck's route must be a single continuous path from the depot to the depot without intermediate depot visits.

## Turn 16 - Generic Agent

QUESTION: Is the distance between two locations computed as the straight-line Euclidean distance (sqrt((x1-x2)^2 + (y1-y2)^2)), or is there a road network or grid that affects the actual travel distance?

## Turn 16 - User Simulator

The distance between two locations is computed as the straight-line Euclidean distance.

## Turn 17 - Generic Agent

QUESTION: Can a truck serve customers in any order as long as each customer's time window is respected, or is there a required sequence (e.g., customers must be visited in increasing ID order)?

## Turn 17 - User Simulator

A truck can serve customers in any order, as long as each customer's time window is respected.

## Turn 18 - Generic Agent

QUESTION: Is the service time of 90 minutes the only time spent at a customer (i.e., the truck arrives, waits if early, spends 90 minutes, then departs), or is there additional loading/unloading time at the depot before a truck can depart?

## Turn 18 - User Simulator

The 90-minute service time is the only time spent at a customer. There is no additional loading/unloading time at the depot before a truck can depart.

## Turn 19 - Generic Agent

QUESTION: Can a truck depart the depot at any time within the depot's operating window [0, 1236], or must it depart at time 0?

## Turn 19 - User Simulator

A truck can depart the depot at any time within the depot's operating window [0, 1236].

## Turn 20 - Generic Agent

QUESTION: Must a truck return to the depot by the end of the depot's operating window (time 1236), or can it return after 1236 as long as all customer time windows are met?

## Turn 20 - User Simulator

A truck must return to the depot by the end of the depot's operating window (time 1236).

## Turn 21 - Generic Agent

QUESTION: If a truck is not used in the plan, is it simply idle at the depot (no cost), or does every truck incur a fixed cost regardless of whether it is used?

## Turn 21 - User Simulator

If a truck is not used in the plan, it is simply idle at the depot with no cost.

## Turn 22 - Generic Agent

QUESTION: Is the objective purely to minimize total distance traveled (sum of Euclidean distances over all arcs used by all trucks), with no penalty for the number of trucks used?

## Turn 22 - User Simulator

Yes, the objective is purely to minimize the total distance traveled by all vehicles, with no penalty for the number of trucks used.

## Turn 23 - Generic Agent

QUESTION: Is there a maximum route duration or maximum number of customers per truck beyond the capacity of 200 units and the depot closing time of 1236 minutes?

## Turn 23 - User Simulator

No, there is no maximum route duration or maximum number of customers per truck beyond the capacity of 200 units and the depot closing time of 1236 minutes.

## Turn 24 - Generic Agent

QUESTION: Can a truck wait at a customer location (i.e., arrive early and wait until the time window opens), or must it arrive exactly at the start of the time window?

## Turn 24 - User Simulator

A truck can wait at a customer location if it arrives early; it must wait until the time window opens before service can begin.

## Turn 25 - Generic Agent

QUESTION: Can a truck wait at the depot before departing (i.e., depart later than time 0), or must it depart immediately at time 0?

## Turn 25 - User Simulator

A truck can wait at the depot before departing; it does not have to depart immediately at time 0.

## Turn 26 - Generic Agent

QUESTION: Can a truck wait at an intermediate customer location (i.e., arrive early, wait, then serve), or must it arrive exactly at the start of the time window?

## Turn 26 - User Simulator

A truck can wait at an intermediate customer location if it arrives early; it must wait until the time window opens before service can begin.

## Turn 27 - Generic Agent

QUESTION: Is the total demand of all 20 customers (sum of all demands) within the capacity of 5 trucks (5 × 200 = 1000 units), or could the total demand exceed this?

## Turn 27 - User Simulator

The total demand of all 20 customers is 340 units, which is within the capacity of 5 trucks (5 × 200 = 1000 units).

## Turn 28 - Generic Agent

QUESTION: Can a truck visit the depot in the middle of its route (i.e., return to the depot, then depart again to serve more customers), or must each truck's route be a single continuous path from depot to depot without intermediate depot visits?

## Turn 28 - User Simulator

Each truck's route must be a single continuous path from the depot to the depot without intermediate depot visits.

## Turn 29 - Generic Agent

QUESTION: Is the distance between two locations computed as the straight-line Euclidean distance (sqrt((x1-x2)^2 + (y1-y2)^2)), or is there a road network or grid that affects the actual travel distance?

## Turn 29 - User Simulator

The distance between two locations is computed as the straight-line Euclidean distance.

## Turn 30 - Generic Agent

QUESTION: Can a truck serve customers in any order as long as each customer's time window is respected, or is there a required sequence (e.g., customers must be visited in increasing ID order)?

## Turn 30 - User Simulator

A truck can serve customers in any order, as long as each customer's time window is respected.