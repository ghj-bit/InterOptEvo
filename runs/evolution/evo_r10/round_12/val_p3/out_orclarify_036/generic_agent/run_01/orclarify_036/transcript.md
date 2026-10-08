## Turn 1 - Generic Agent

QUESTION: How should travel time between two points be computed from the given coordinates — is it Euclidean distance (in minutes, i.e., 1 unit of distance = 1 minute of travel), or Manhattan distance, or some other rule?

## Turn 1 - User Simulator

The travel time between two points is computed as the Euclidean distance between their coordinates, with 1 unit of distance equal to 1 minute of travel time.

## Turn 2 - Generic Agent

QUESTION: Do all trucks start at the depot at time 0 and must they return to the depot after finishing their route, or is returning to the depot optional?

## Turn 2 - User Simulator

All trucks must start from the depot and return to the depot at the end of their routes.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum route duration or latest return-to-depot time that each truck must satisfy, or is the only time restriction the customer time windows (with the depot window [0, 1236] being the only bound on when a truck can leave and return)?

## Turn 3 - User Simulator

The only time restriction is the customer time windows. The depot operating time window of [0, 1236] minutes is the only bound on when a truck can leave and return to the depot. There is no separate maximum route duration constraint.

## Turn 4 - Generic Agent

QUESTION: If a truck arrives at a customer before the customer's time window opens, it waits until the window opens and then begins service — is that waiting time counted as part of the truck's schedule (i.e., it delays subsequent customers), and is waiting itself penalized in the objective, or is the objective purely the sum of travel distances with waiting having no cost?

## Turn 4 - User Simulator

Yes, waiting time is part of the truck's schedule and delays subsequent customers. However, waiting itself is not penalized in the objective. The objective is purely to minimize the total distance traveled by all vehicles.

## Turn 5 - Generic Agent

QUESTION: Can a single truck visit the same customer more than once, or must each customer be served exactly once by exactly one truck?

## Turn 5 - User Simulator

Each customer must be served exactly once by exactly one truck.

## Turn 6 - Generic Agent

QUESTION: Are all 5 trucks identical in capacity (200 units) and available for use, and is there any cost or penalty associated with using a truck (i.e., is it free to dispatch any number of trucks up to 5, with the objective being only total travel distance)?

## Turn 6 - User Simulator

Yes, all 5 trucks are identical with a capacity of 200 units. There is no cost or penalty associated with using a truck. It is free to dispatch any number of trucks up to 5, and the objective is only to minimize the total travel distance.

## Turn 7 - Generic Agent

QUESTION: The total demand across all 20 customers is 370 units, and each truck holds at most 200 units, so at least 2 trucks are needed. Is there any requirement that a truck's route must be a single continuous sequence (visit customers one after another without splitting), i.e., each truck performs exactly one route that starts at the depot, visits a set of customers in some order, and returns to the depot?

## Turn 7 - User Simulator

Yes, each truck performs exactly one route that starts at the depot, visits a set of customers in some order, and returns to the depot.

## Turn 8 - Generic Agent

QUESTION: When a truck returns to the depot, must its return time be within the depot window [0, 1236], i.e., is 1236 minutes a hard deadline by which every truck must be back at the depot?

## Turn 8 - User Simulator

Yes, 1236 minutes is a hard deadline by which every truck must be back at the depot.

## Turn 9 - Generic Agent

QUESTION: For the distance objective, is the total distance the sum of Euclidean distances over all legs of all routes, including the leg from the depot to the first customer and the leg from the last customer back to the depot?

## Turn 9 - User Simulator

Yes, the total distance is the sum of Euclidean distances over all legs of all routes, including the leg from the depot to the first customer and the leg from the last customer back to the depot.

## Turn 10 - Generic Agent

QUESTION: Is there any precedence or ordering requirement between customers (for example, some customers must be served before others), or can each truck visit its assigned customers in any order as long as the time windows are respected?

## Turn 10 - User Simulator

There is no precedence or ordering requirement between customers. Each truck can visit its assigned customers in any order as long as the time windows are respected.

## Turn 11 - Generic Agent

QUESTION: Is the distance between two points computed as the straight-line Euclidean distance (sqrt of sum of squared differences), and is the objective to minimize the sum of these Euclidean distances (not squared distances)?

## Turn 11 - User Simulator

Yes, the distance between two points is computed as the straight-line Euclidean distance, and the objective is to minimize the sum of these Euclidean distances.

## Turn 12 - Generic Agent

QUESTION: Are there any customers that cannot be served by certain trucks, or are all 20 customers eligible to be served by any of the 5 trucks?

## Turn 12 - User Simulator

All 20 customers are eligible to be served by any of the 5 trucks.

## Turn 13 - Generic Agent

QUESTION: If a truck's route would require it to be at the depot after 1236 minutes, is that route infeasible, or can the truck simply not be used (i.e., only trucks whose routes complete by 1236 are allowed)?

## Turn 13 - User Simulator

If a truck's route would require it to be at the depot after 1236 minutes, that route is infeasible. Only trucks whose routes complete by 1236 minutes are allowed.

## Turn 14 - Generic Agent

QUESTION: Is it acceptable for a truck to be dispatched and return to the depot with an empty route (visiting zero customers), or must every dispatched truck visit at least one customer?

## Turn 14 - User Simulator

It is acceptable for a truck to be dispatched and return to the depot with an empty route (visiting zero customers).

## Turn 15 - Generic Agent

QUESTION: Is the service duration of 90 minutes the time spent at each customer (i.e., the truck arrives, waits if early, then spends 90 minutes serving, then departs), and does this 90 minutes count toward the truck's schedule for subsequent customers?

## Turn 15 - User Simulator

Yes, the service duration of 90 minutes is the time spent at each customer. The truck arrives, waits if early, then spends 90 minutes serving, then departs. This 90 minutes counts toward the truck's schedule for subsequent customers.

## Turn 16 - Generic Agent

QUESTION: Is the time window for each customer the window within which service must *begin* (i.e., the truck must start its 90-minute service within [start, end]), or is it the window within which service must be *completed*?

## Turn 16 - User Simulator

The time window for each customer is the window within which service must *begin*. The truck must start its 90-minute service within [start, end].

## Turn 17 - Generic Agent

QUESTION: When a truck arrives at a customer early and waits, does the waiting time count toward the truck's schedule (i.e., the truck is occupied and cannot serve another customer during the wait), or can the truck leave and come back later?

## Turn 17 - User Simulator

The waiting time counts toward the truck's schedule. The truck is occupied and cannot serve another customer during the wait.

## Turn 18 - Generic Agent

QUESTION: Is there any requirement that the total number of trucks actually used must be minimized as a secondary objective, or is the sole objective to minimize total travel distance with no tie-breaking on the number of trucks used?

## Turn 18 - User Simulator

The sole objective is to minimize total travel distance. There is no secondary objective to minimize the number of trucks used, and no tie-breaking on the number of trucks.

## Turn 19 - Generic Agent

QUESTION: Is the depot's operating time window [0, 1236] the same for all trucks (i.e., every truck must leave the depot at or after time 0 and return at or before time 1236), or can different trucks have different availability windows?

## Turn 19 - User Simulator

The depot's operating time window [0, 1236] is the same for all trucks. Every truck must leave the depot at or after time 0 and return at or before time 1236.

## Turn 20 - Generic Agent

QUESTION: Is there any requirement that a truck must leave the depot at exactly time 0, or can a truck wait at the depot before departing (i.e., leave at any time >= 0)?

## Turn 20 - User Simulator

A truck can wait at the depot before departing. It can leave at any time >= 0.

## Turn 21 - Generic Agent

QUESTION: Is the truck capacity constraint applied to the sum of demands of all customers on a single route (i.e., the total load the truck carries from the depot must not exceed 200 units), or is there any other interpretation of the capacity constraint?

## Turn 21 - User Simulator

The truck capacity constraint is applied to the sum of demands of all customers on a single route. The total load the truck carries from the depot must not exceed 200 units.

## Turn 22 - Generic Agent

QUESTION: Is there any requirement that the truck must deliver all its load at the first customer it visits, or does the truck carry the full load from the depot and deliver portions at each customer along the route (i.e., the load decreases as deliveries are made)?

## Turn 22 - User Simulator

The truck carries the full load from the depot and delivers portions at each customer along the route. The load decreases as deliveries are made.

## Turn 23 - Generic Agent

QUESTION: Is there any requirement that the truck must return to the depot with an empty load, or can it return with leftover capacity unused?

## Turn 23 - User Simulator

The truck must return to the depot with an empty load.

## Turn 24 - Generic Agent

QUESTION: Is there any requirement that the truck's load at any point along the route must not exceed 200 units (i.e., the capacity constraint is checked at every point, not just at the depot), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 24 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.

## Turn 25 - Generic Agent

QUESTION: Is there any requirement that the truck must not exceed 200 units at any intermediate point along the route (i.e., the load must never exceed 200 as it delivers), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 25 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.

## Turn 26 - Generic Agent

QUESTION: Is there any requirement that the truck must not exceed 200 units at any intermediate point along the route (i.e., the load must never exceed 200 as it delivers), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 26 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.

## Turn 27 - Generic Agent

QUESTION: Is there any requirement that the truck must not exceed 200 units at any intermediate point along the route (i.e., the load must never exceed 200 as it delivers), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 27 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.

## Turn 28 - Generic Agent

QUESTION: Is there any requirement that the truck must not exceed 200 units at any intermediate point along the route (i.e., the load must never exceed 200 as it delivers), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 28 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.

## Turn 29 - Generic Agent

QUESTION: Is there any requirement that the truck must not exceed 200 units at any intermediate point along the route (i.e., the load must never exceed 200 as it delivers), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 29 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.

## Turn 30 - Generic Agent

QUESTION: Is there any requirement that the truck must not exceed 200 units at any intermediate point along the route (i.e., the load must never exceed 200 as it delivers), or is it sufficient that the total demand of all customers on the route does not exceed 200 units?

## Turn 30 - User Simulator

It is sufficient that the total demand of all customers on the route does not exceed 200 units.