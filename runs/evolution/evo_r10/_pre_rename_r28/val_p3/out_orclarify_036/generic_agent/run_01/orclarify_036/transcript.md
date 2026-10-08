## Turn 1 - Generic Agent

QUESTION: When a truck finishes serving its last customer, must it return to the central depot (Depot 0), and should that return leg be counted in the total distance to be minimized?

## Turn 1 - User Simulator

Yes. Every truck must return to the central depot (Depot 0) after serving its last customer, and that return leg is included in the total distance to be minimized.

## Turn 2 - Generic Agent

QUESTION: How should travel time between two points be computed from the coordinates — is it Euclidean distance divided by a constant speed (e.g., 1 unit of distance per minute), or should I use Manhattan distance, or is there a specific speed value you want me to use?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the time-window feasibility check, should I assume travel time equals Euclidean distance in minutes (i.e., a speed of 1 unit per minute), or do you have a different speed or distance metric in mind?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the travel-time metric is still being confirmed internally, should I proceed by assuming travel time equals Euclidean distance in minutes (speed of 1 unit per minute), so that the model is ready to go and the speed can be swapped in as a single parameter later?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Do all 5 trucks start at the central depot at time 0, or can they depart later (e.g., staggered start times)?

## Turn 5 - User Simulator

All trucks start at the central depot at time 0.

## Turn 6 - Generic Agent

QUESTION: Can a single truck serve customers in any order as long as it respects each customer's time window, or is there a fixed visiting order that must be followed?

## Turn 6 - User Simulator

A single truck can serve customers in any order, as long as it respects each customer's time window.

## Turn 7 - Generic Agent

QUESTION: Can a truck visit the same customer more than once, or must each customer be served exactly once by exactly one truck?

## Turn 7 - User Simulator

Each customer must be served exactly once by exactly one truck.