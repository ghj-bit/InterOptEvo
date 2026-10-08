# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U10, U11, U12, U2, U3, U4, U5, U6, U7, U8
I need help planning the transportation of products from the warehouse to sales points, ensuring that total pollution from all trips must not exceed 2000 units, the number of truck trips must be at least 10, and total units delivered must be at least 1800 units.

Number of sales points: 3.

Transportation options: truck, van, motorcycle, electric vehicle.

Transport capacities per trip (units): truck 100, van 80, motorcycle 40, electric vehicle 60.

Pollution generated per trip (units): truck 100, van 50, motorcycle 10, electric vehicle 0.

Delivery target: 1800 units.

Maximum total pollution allowed: 2000 units.

Minimum number of truck trips: 10.

## Problem units
- U1 (context): I need help planning the transportation of products from the warehouse to sales points.
- U2 (data): Number of sales points: 3.
- U3 (data): Transportation options: truck, van, motorcycle, electric vehicle.
- U4 (data): Transport capacities per trip (units): truck 100, van 80, motorcycle 40, electric vehicle 60.
- U5 (data): Pollution generated per trip (units): truck 100, van 50, motorcycle 10, electric vehicle 0.
- U6 (data): Delivery target: 1800 units.
- U7 (data): Maximum total pollution allowed: 2000 units.
- U8 (data): Minimum number of truck trips: 10.
- U9 (constraint): Either vans or electric vehicles can be used, but not both.
- U10 (constraint): Total pollution from all trips must not exceed 2000 units.
- U11 (constraint): The number of truck trips must be at least 10.
- U12 (constraint): Total units delivered must be at least 1800 units.
- U13 (objective): Minimize the total pollution generated.

## Hidden slot scoring rules
## H1: van_ev_mutual_exclusion
- Severity: P1
- Severity reason: Without this constraint, the model could allow both vans and electric vehicles, leading to a solution that violates the operational restriction. The problem remains coherent, but the plan would be business-invalid.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must explicitly ask whether vans and electric vehicles can be used together or must be mutually exclusive.
- Reference acceptable questions:
  - Can I use both vans and electric vehicles in the transportation plan, or must I choose only one type?
  - Is it allowed to mix vans and electric vehicles, or do they need to be mutually exclusive?
- Failure modes:
  - Assuming both vans and electric vehicles can be used simultaneously without restriction.
  - Not considering the mutual exclusivity clause, leading to a model that combines them.

## H2: minimize_total_pollution_objective
- Severity: P0
- Severity reason: Without a stated objective, the optimization problem is ill-posed; the modeling agent cannot define optimality, making modeling impossible.
- Problem unit ID: U13
- Semantic hit rule: The agent must ask about the objective function, specifically confirming whether it is to minimize total pollution or clarifying what to optimize.
- Reference acceptable questions:
  - What is the objective we should optimize? For example, is it minimizing total pollution, total cost, or something else?
  - You mentioned minimizing total pollution; is that the primary goal for this transportation plan?
- Failure modes:
  - Assuming the objective is to minimize total cost when no cost data is provided.
  - Assuming the objective is to minimize the number of trips.
  - Leaving the objective unspecified and formulating an arbitrary or infeasible model.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: The brief says "the number of truck trips must be at least 10" — does this mean at least 10 trips using any vehicle type (total trips ≥ 10), or specifically at least 10 trips made by trucks?

## Turn 1 - User Simulator

It means specifically at least 10 trips made by trucks.

## Turn 2 - Generic Agent

QUESTION: Is the goal to minimize total pollution, minimize total cost, or is this a feasibility problem where any plan meeting the constraints is acceptable?

## Turn 2 - User Simulator

The goal is to minimize total pollution.

## Turn 3 - Generic Agent

QUESTION: Are the 1800 units a minimum that must be delivered (i.e., delivering more is allowed), or must exactly 1800 units be delivered?

## Turn 3 - User Simulator

The 1800 units are a minimum that must be delivered; delivering more is allowed.

## Turn 4 - Generic Agent

QUESTION: Are there any limits on how many trips each vehicle type can make (e.g., a maximum number of trucks, vans, motorcycles, or electric vehicles available)?

## Turn 4 - User Simulator

No, there are no limits on how many trips each vehicle type can make.

## Turn 5 - Generic Agent

QUESTION: Are the decision variables (number of trips per vehicle type) required to be whole numbers, or can they be fractional?

## Turn 5 - User Simulator

The number of trips per vehicle type must be whole numbers.

## Turn 6 - Generic Agent

QUESTION: The 3 sales points — do the trips need to be assigned to specific sales points (i.e., each sales point has its own delivery requirement), or is the 1800-unit target a single aggregate total across all 3 sales points combined?

## Turn 6 - User Simulator

The 1800-unit target is a single aggregate total across all 3 sales points combined.

## Turn 7 - Generic Agent

QUESTION: Is there any cost associated with each vehicle type per trip, or is pollution the only factor to consider in the objective?

## Turn 7 - User Simulator

Pollution is the only factor to consider in the objective.

## Turn 8 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding:

**Problem:** Plan the number of trips per vehicle type (truck, van, motorcycle, electric vehicle) to transport products from a warehouse to 3 sales points.

**Decision variables:**
- x_truck, x_van, x_motorcycle, x_electric — non-negative integers (whole number of trips per vehicle type)

**Objective:**
- Minimize total pollution = 100·x_truck + 50·x_van + 10·x_motorcycle + 0·x_electric

**Constraints:**
1. Total pollution ≤ 2000 units
2. x_truck ≥ 10 (at least 10 truck trips specifically)
3. Total units delivered ≥ 1800 units, where total units = 100·x_truck + 80·x_van + 40·x_motorcycle + 60·x_electric
4. No upper bounds on any vehicle type's trip count
5. The 1800-unit target is an aggregate minimum across all 3 sales points (no per-point breakdown needed)
6. Pollution is the sole objective factor (no cost)

**Key confirmed facts:**
- "At least 10 truck trips" refers specifically to trucks, not total trips.
- 1800 units is a minimum (over-delivery allowed).
- All trip counts must be integers.
- No per-vehicle-type upper limits.
- The 3 sales points do not introduce additional structure; the problem is a single aggregate delivery target.