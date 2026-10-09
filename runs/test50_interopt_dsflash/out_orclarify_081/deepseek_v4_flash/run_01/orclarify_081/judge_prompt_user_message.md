# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U2
I need help planning a parking arrangement on Danzig Street for party guests arriving in cars, where vehicles can park on both sides of the street.

The lengths of the 15 cars (i from 1 to 15, λ_i in meters) are:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|----|----|-----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| λ_i | 4 | 4.5 | 5 | 4.1 | 2.4 | 5.2 | 3.7 | 3.5 | 3.2 | 4.5 | 2.3 | 3.3 | 3.8 | 4.6 | 3 |

## Problem units
- U1 (context): I need help planning a parking arrangement on Danzig Street for party guests arriving in cars.
- U2 (data): The lengths of the 15 cars (i from 1 to 15, λ_i in meters) are:

| i | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|----|----|-----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| λ_i | 4 | 4.5 | 5 | 4.1 | 2.4 | 5.2 | 3.7 | 3.5 | 3.2 | 4.5 | 2.3 | 3.3 | 3.8 | 4.6 | 3 |
- U3 (assumption): Vehicles can park on both sides of the street.
- U4 (objective): Minimize the total length of the street occupied by the parked vehicles.

## Hidden slot scoring rules
## H1: missing_objective_definition
- Severity: P0
- Severity reason: Without the objective, the modeling agent cannot define the objective function of the optimization model. The problem statement would be missing the goal of the parking arrangement, making it impossible to formulate a meaningful optimization problem.
- Problem unit ID: U4
- Semantic hit rule: The Agent's question must ask about the objective or what to minimize/maximize in the parking problem. It should specifically mention the need for an optimization goal.
- Reference acceptable questions:
  - What exactly should I minimize? The total length of street occupied?
  - What is the objective: to minimize the space used on the street?
- Failure modes:
  - Silent incorrect assumption: Assuming the objective is to minimize the maximum length used on either side of the street.
  - Silent incorrect assumption: Assuming the objective is to minimize the number of cars parked on the street.


# Atomic Question Map

Q1 (turn 1): What is the total usable parking length on each side of Danzig Street?
Q2 (turn 1): Are there any fixed no-parking zones, driveways, or other obstructions?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the total usable parking length on each side of Danzig Street, and are there any fixed no-parking zones, driveways, or other obstructions?

## Turn 1 - User Simulator

I don't have that information. The request only gives the car lengths and says vehicles can park on both sides of the street — it doesn't specify the usable parking length per side or any no-parking zones, driveways, or other obstructions. That point still needs internal confirmation.