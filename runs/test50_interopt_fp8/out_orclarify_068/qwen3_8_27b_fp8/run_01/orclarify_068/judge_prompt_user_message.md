# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U7, U2, U3, U4
I need help planning the distribution of coal from two coal yards to three residential areas, and the total coal supplied to each residential area must meet its monthly demand.

Three residential areas require 55 tons, 75 tons, and 50 tons of coal per month, respectively.

Coal yard A receives no less than 80 tons of coal per month; coal yard B receives no less than 100 tons of coal per month.

Distances (in km):
|               | Residential Area 1 | Residential Area 2 | Residential Area 3 |
|---------------|--------------------|--------------------|--------------------|
| Coal Yard A   | 10                 | 5                  | 6                  |
| Coal Yard B   | 4                  | 8                  | 15                 |

## Problem units
- U1 (context): I need help planning the distribution of coal from two coal yards to three residential areas.
- U2 (data): Three residential areas require 55 tons, 75 tons, and 50 tons of coal per month, respectively.
- U3 (data): Coal yard A receives no less than 80 tons of coal per month; coal yard B receives no less than 100 tons of coal per month.
- U4 (data): Distances (in km):
|               | Residential Area 1 | Residential Area 2 | Residential Area 3 |
|---------------|--------------------|--------------------|--------------------|
| Coal Yard A   | 10                 | 5                  | 6                  |
| Coal Yard B   | 4                  | 8                  | 15                 |
- U5 (objective): Minimize the ton-kilometers of transportation.
- U6 (constraint): The amount of coal distributed from each coal yard must not exceed the amount of coal it receives per month.
- U7 (constraint): The total coal supplied to each residential area must meet its monthly demand.

## Hidden slot scoring rules
## H1: unknown_objective
- Severity: P0
- Severity reason: Without the objective, the optimization problem is undefined; a responsible modeling agent cannot determine what to minimize, making model formulation impossible.
- Problem unit ID: U5
- Semantic hit rule: The agent’s question must inquire about the optimization goal, specifically asking what metric to minimize (e.g., total ton-kilometers, total cost, or total weighted distance).
- Reference acceptable questions:
  - What is the objective we are trying to minimize?
  - Should we minimize total ton-kilometers traveled?
- Failure modes:
  - Assuming the goal is to minimize total unweighted distance traveled (ignoring tonnage).
  - Assuming the goal is to minimize total cost based on some implicit rate.

## H2: undisclosed_distribution_limit
- Severity: P1
- Severity reason: Without this constraint, the model could either assume unbounded supply or fix supplies at the given minimal amounts, but the precise condition that distribution cannot exceed what each yard actually receives is a key business rule that may change the feasible region and optimal solution.
- Problem unit ID: U6
- Semantic hit rule: The agent’s question must explicitly ask about the upper bound on outgoing coal from each yard, or whether the distribution amount can exceed the amount the yard receives.
- Reference acceptable questions:
  - Is there a limit on how much coal each yard can send out?
  - Can a coal yard distribute more coal than it receives?
- Failure modes:
  - Assuming the yards can supply any amount without limit.
  - Assuming the supply at each yard is exactly 80 and 100 tons with no dependence on the actual received quantity.


# Atomic Question Map

Q1 (turn 1): What is the primary objective of this distribution plan: minimizing total transportation cost, minimizing total distance traveled, or something else?
Q2 (turn 2): Are the amounts received by Coal Yard A (at least 80 tons) and Coal Yard B (at least 100 tons) minimum requirements that can be exceeded, or are they exact fixed supply limits that must be fully distributed?
Q3 (turn 3): What is the maximum amount of coal Coal Yard A can receive per month?
Q4 (turn 3): What is the maximum amount of coal Coal Yard B can receive per month?
Q5 (turn 4): If the yards receive more coal than the total residential demand (180 tons), is it allowed to leave the excess coal at the yards, or must all received coal be distributed to the residential areas?
Q6 (turn 5): Are there any maximum monthly supply capacities for Coal Yard A and Coal Yard B, or is there no upper limit on how much coal they can receive and distribute?
Q7 (turn 6): Since the maximum supply capacities are currently under internal confirmation, should the model assume that the yards can supply any amount up to the total residential demand (180 tons), or are there known hard upper limits that are lower than the demand?
Q8 (turn 7): Are there any known hard upper limits on the monthly supply capacity for Coal Yard A or Coal Yard B that are lower than the total residential demand of 180 tons?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the primary objective of this distribution plan: minimizing total transportation cost, minimizing total distance traveled, or something else?

## Turn 1 - User Simulator

The primary objective is to minimize the total ton-kilometers of transportation. This means we want the sum of the tons of coal multiplied by the distance traveled for each delivery to be as small as possible.

## Turn 2 - Generic Agent

QUESTION: Are the amounts received by Coal Yard A (at least 80 tons) and Coal Yard B (at least 100 tons) minimum requirements that can be exceeded, or are they exact fixed supply limits that must be fully distributed?

## Turn 2 - User Simulator

They are minimum requirements that can be exceeded. The yards receive at least those amounts, and the total coal each yard sends out cannot exceed the amount it actually receives that month.

## Turn 3 - Generic Agent

QUESTION: Since the yards can receive more than the minimums, what are the maximum amounts of coal Coal Yard A and Coal Yard B can receive per month?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: If the yards receive more coal than the total residential demand (180 tons), is it allowed to leave the excess coal at the yards, or must all received coal be distributed to the residential areas?

## Turn 4 - User Simulator

It is allowed to leave the excess coal at the yards. The constraint is that the amount of coal distributed from each yard must not exceed the amount it receives; it does not require all received coal to be distributed.

## Turn 5 - Generic Agent

QUESTION: Are there any maximum monthly supply capacities for Coal Yard A and Coal Yard B, or is there no upper limit on how much coal they can receive and distribute?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the maximum supply capacities are currently under internal confirmation, should the model assume that the yards can supply any amount up to the total residential demand (180 tons), or are there known hard upper limits that are lower than the demand?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any known hard upper limits on the monthly supply capacity for Coal Yard A or Coal Yard B that are lower than the total residential demand of 180 tons?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.950

Confidence rationale: The request is sufficiently specified for a standard transportation model. Although the exact maximum supply capacities are under internal confirmation, the problem structure allows for a robust formulation: the supply variables are bounded below by the minimums (80 and 100 tons) and above by the total demand (180 tons) because any supply exceeding demand would be left at the yards and would not contribute to the objective function (minimizing ton-kilometers) or satisfy any additional demand. Therefore, the effective upper bound for each yard's supply is implicitly constrained by the total demand, making the 'unknown' maximum capacity non-binding for the optimal solution unless it is lower than the minimums (which would make the problem infeasible, a separate validation step). The model can proceed with the assumption that the yards can supply up to the demand level.

Summary: Minimize total ton-kilometers of coal distribution from two yards to three residential areas. Yard A supplies at least 80 tons, Yard B at least 100 tons. Total demand is 180 tons (55+75+50). Excess coal can be left at yards. Distances are provided. The model will determine the optimal flow from each yard to each area to minimize transportation cost (tons * km), subject to demand satisfaction and minimum supply constraints.