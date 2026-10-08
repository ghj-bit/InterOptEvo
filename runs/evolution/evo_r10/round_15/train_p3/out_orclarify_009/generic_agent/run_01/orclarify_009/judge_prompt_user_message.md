# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U8, U9, U10, U11, U2, U3, U4, U5, U6
I need help planning the manufacture of toy trucks, toy airplanes, toy boats, and toy trains, where total wood consumption cannot exceed 890 units and total steel consumption cannot exceed 500 units. Additionally, if trucks are manufactured, then trains are not manufactured, and if boats are manufactured, then airplanes are also manufactured.

Profit per toy: truck $5, airplane $10, boat $8, train $7.

Available wood: 890 units.

Wood required per toy: truck 12 units, airplane 20 units, boat 15 units, train 10 units.

Available steel: 500 units.

Steel required per toy: truck 6 units, airplane 3 units, boat 5 units, train 4 units.

## Problem units
- U1 (context): I need help planning the manufacture of toy trucks, toy airplanes, toy boats, and toy trains.
- U2 (data): Profit per toy: truck $5, airplane $10, boat $8, train $7.
- U3 (data): Available wood: 890 units.
- U4 (data): Wood required per toy: truck 12 units, airplane 20 units, boat 15 units, train 10 units.
- U5 (data): Available steel: 500 units.
- U6 (data): Steel required per toy: truck 6 units, airplane 3 units, boat 5 units, train 4 units.
- U7 (objective): Maximize total profit.
- U8 (constraint): Total wood consumption cannot exceed 890 units.
- U9 (constraint): Total steel consumption cannot exceed 500 units.
- U10 (constraint): If trucks are manufactured, then trains are not manufactured.
- U11 (constraint): If boats are manufactured, then airplanes are also manufactured.
- U12 (constraint): Number of toy boats manufactured cannot exceed number of toy trains manufactured.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without an objective function, the optimization problem is undefined. A modeling agent cannot proceed to formulate a meaningful model unless the objective is clarified.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must explicitly ask about the objective of the optimization, specifically whether profit should be maximized.
- Reference acceptable questions:
  - What are we trying to maximize? Should we maximize total profit?
  - Is the goal to maximize profit, or something else like revenue or number of toys produced?
- Failure modes:
  - Silently assuming the objective is to maximize production volume or market share.
  - Assuming the goal is to minimize cost without asking.

## H2: boat_not_exceed_train
- Severity: P2
- Severity reason: The optimization model remains well-defined and solvable without this constraint. The missing rule is a specific business preference that would make the solution more accurate, but its omission does not make the model impossible or fundamentally ill-posed.
- Problem unit ID: U12
- Semantic hit rule: The agent must inquire about a constraint that limits the number of boats relative to the number of trains, specifically asking if boats must be less than or equal to trains.
- Reference acceptable questions:
  - Is there any rule linking the number of boats and trains, like boats can't exceed trains?
  - Do we have any production restriction tying the number of boats to the number of trains?
- Failure modes:
  - Silently assuming no relationship between boats and trains and building the model without this constraint.
  - Assuming that boats cannot exceed airplanes instead.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Are the production quantities of trucks, airplanes, boats, and trains required to be whole numbers (integer units), or can they be fractional?

## Turn 1 - User Simulator

The production quantities must be whole numbers (integer units).

## Turn 2 - Generic Agent

QUESTION: For the rule "if trucks are manufactured, then trains are not manufactured," should I read this as a strict mutual exclusion (trucks and trains can never both be produced in any positive amount), or only as a one-way implication (trucks force trains to zero, but trains may still be produced when trucks are zero)?

## Turn 2 - User Simulator

It is a one-way implication: if trucks are produced, trains must be zero. Trains may still be produced when trucks are zero.

## Turn 3 - Generic Agent

QUESTION: For the rule "if boats are manufactured, then airplanes are also manufactured," should I read this as a one-way implication (boats force airplanes to be positive, but airplanes may be produced even when boats are zero), or as a strict mutual requirement (airplanes can only be produced if boats are also produced)?

## Turn 3 - User Simulator

It is a one-way implication: if boats are produced, airplanes must also be produced. Airplanes may be produced even when boats are zero.

## Turn 4 - Generic Agent

QUESTION: When boats are produced, does "airplanes are also manufactured" require at least one airplane to be produced, or is it enough that airplanes are simply allowed to be produced (i.e., the constraint only links the two products' availability)?

## Turn 4 - User Simulator

It requires at least one airplane to be produced.

## Turn 5 - Generic Agent

QUESTION: Are the wood and steel limits (890 and 500 units) hard caps that must not be exceeded, with any unused material simply left over and unpenalized?

## Turn 5 - User Simulator

Yes, they are hard caps that must not be exceeded. Any unused material is simply left over and unpenalized.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Integer production planning for four toy types — trucks, airplanes, boats, trains.

**Decision variables:** Non-negative integers x_truck, x_airplane, x_boat, x_train (whole units of each toy).

**Objective:** Maximize total profit = 5·x_truck + 10·x_airplane + 8·x_boat + 7·x_train.

**Resource constraints (hard caps, unused material unpenalized):**
- Wood: 12·x_truck + 20·x_airplane + 15·x_boat + 10·x_train ≤ 890
- Steel: 6·x_truck + 3·x_airplane + 5·x_boat + 4·x_train ≤ 500

**Conditional rules (both one-way implications):**
1. If trucks are produced (x_truck ≥ 1), then trains must be zero (x_train = 0). Trains may be produced when trucks are zero.
2. If boats are produced (x_boat ≥ 1), then at least one airplane must be produced (x_airplane ≥ 1). Airplanes may be produced even when boats are zero.

**Integrality:** All four production variables are integers ≥ 0.

No other costs, lower bounds, or additional constraints apply.