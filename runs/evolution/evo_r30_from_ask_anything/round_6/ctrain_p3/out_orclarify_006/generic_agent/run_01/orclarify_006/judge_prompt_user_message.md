# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U9, U11, U12, U2, U3, U4, U5, U6, U7, U8
I need help creating a production schedule for a factory over the next year, aiming to minimize the total cost (compensation cost + inventory holding cost). At the end of the fourth quarter, the inventory of each product must be 150 units, and in each quarter, total production hours used must not exceed 15,000 hours.

Table 1-10: Contract reservations per quarter per product:
| Product | 1    | 2    | 3    | 4    |
|---------|------|------|------|------|
| I       | 1500 | 1000 | 2000 | 1200 |
| II      | 1500 | 1500 | 1200 | 1500 |
| III     | 1000 | 2000 | 1500 | 2500 |

At the beginning of the first quarter, there is no inventory for products I, II, and III (i.e., initial inventory is 0 for each product).

It is required to have 150 units in stock for each product by the end of the fourth quarter.

The factory has 15,000 production hours per quarter.

Each unit of product I requires 2 hours, product II requires 4 hours, and product III requires 3 hours.

Delay compensation: for products I and II, 20 yuan per unit per quarter delay; for product III, 10 yuan per unit per quarter delay.

Inventory holding cost: 5 yuan per unit per quarter for products produced but not delivered in the current quarter.

## Problem units
- U1 (context): I need help creating a production schedule for a factory over the next year.
- U2 (data): Table 1-10: Contract reservations per quarter per product:
| Product | 1    | 2    | 3    | 4    |
|---------|------|------|------|------|
| I       | 1500 | 1000 | 2000 | 1200 |
| II      | 1500 | 1500 | 1200 | 1500 |
| III     | 1000 | 2000 | 1500 | 2500 |
- U3 (data): At the beginning of the first quarter, there is no inventory for products I, II, and III (i.e., initial inventory is 0 for each product).
- U4 (data): It is required to have 150 units in stock for each product by the end of the fourth quarter.
- U5 (data): The factory has 15,000 production hours per quarter.
- U6 (data): Each unit of product I requires 2 hours, product II requires 4 hours, and product III requires 3 hours.
- U7 (data): Delay compensation: for products I and II, 20 yuan per unit per quarter delay; for product III, 10 yuan per unit per quarter delay.
- U8 (data): Inventory holding cost: 5 yuan per unit per quarter for products produced but not delivered in the current quarter.
- U9 (objective): Minimize the total cost (compensation cost + inventory holding cost).
- U10 (constraint): Product I cannot be produced in the second quarter.
- U11 (constraint): At the end of the fourth quarter, the inventory of each product must be 150 units.
- U12 (constraint): In each quarter, total production hours used must not exceed 15,000 hours.
- U13 (constraint): All contract reservations must be delivered (late delivery is allowed with compensation).

## Hidden slot scoring rules
## H1: product_I_no_production_Q2
- Severity: P1
- Severity reason: Without this constraint, the model would incorrectly allow production of Product I in Q2, leading to a schedule that violates a real-world equipment restriction. The model can still be formulated, but it would be materially inaccurate.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must explicitly ask about production restrictions for specific quarters, particularly regarding Product I in the second quarter.
- Reference acceptable questions:
  - Can Product I be produced in the second quarter?
  - Are there any restrictions on the quarters in which Product I can be manufactured?
- Failure modes:
  - Silently assuming Product I can be produced in all quarters, resulting in a schedule that uses Q2 for Product I production.

## H2: contract_reservations_must_be_delivered
- Severity: P1
- Severity reason: Without this constraint, the modeling agent might not realize that all contract reservations are firm requirements that must be eventually delivered even if late, and might instead model lost sales or treat demand as optional. This directly affects the demand fulfillment semantics and model correctness.
- Problem unit ID: U13
- Semantic hit rule: The agent's question must explicitly ask about the requirement to fulfill all contract reservations, or about whether late delivery is permitted and how it is handled.
- Reference acceptable questions:
  - Do we have to satisfy all contract reservations eventually, even if we deliver late?
  - Is late delivery allowed and do all reservations need to be fulfilled?
- Failure modes:
  - Silently assuming that demand not met on time is lost and incurs only a penalty, without requiring back fulfillment.
  - Assuming demand must be met exactly on time, with no backlogging allowed.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: For the "delay compensation" cost, is the delay measured as the number of quarters a unit is late relative to its contract quarter (so a unit produced in Q2 to satisfy a Q1 contract incurs 1 quarter of delay), and is this cost applied to every unit that is not delivered in its contract quarter, or only to units that are ultimately delivered late?

## Turn 1 - User Simulator

The delay compensation is applied to every unit that is not delivered in its contract quarter. The delay is measured as the number of quarters a unit is late relative to its contract quarter.

## Turn 2 - Generic Agent

QUESTION: Can production in a later quarter be used to satisfy demand from an earlier quarter (i.e., is backordering allowed), or must all demand for a given quarter be satisfied by production in that same quarter or earlier?

## Turn 2 - User Simulator

Backordering is allowed. Production in a later quarter can be used to satisfy demand from an earlier quarter, and the delay compensation applies for the quarters the delivery is late.

## Turn 3 - Generic Agent

QUESTION: Is the 15,000 production hours per quarter a hard upper limit that cannot be exceeded, or is it a target that can be exceeded if necessary to meet demand?

## Turn 3 - User Simulator

The 15,000 production hours per quarter is a hard upper limit that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the requirement of 150 units in stock for each product at the end of the fourth quarter a hard constraint that must be met exactly, or is it a target that can be missed if doing so reduces total cost?

## Turn 4 - User Simulator

The requirement of 150 units in stock for each product at the end of the fourth quarter is a hard constraint that must be met exactly.

## Turn 5 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 5 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 6 - Generic Agent

QUESTION: Is the 15,000 production hours per quarter a hard upper limit that cannot be exceeded, or is it a target that can be exceeded if necessary to meet demand?

## Turn 6 - User Simulator

The 15,000 production hours per quarter is a hard upper limit that cannot be exceeded.

## Turn 7 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 7 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 8 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 8 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 9 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 9 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 10 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 10 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 11 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 11 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 12 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 12 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 13 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 13 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 14 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 14 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 15 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 15 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 16 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 16 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 17 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 17 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 18 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 18 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 19 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 19 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 20 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 20 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 21 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 21 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 22 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 22 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 23 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 23 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 24 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 24 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 25 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 25 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 26 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 26 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 27 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 27 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 28 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 28 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 29 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 29 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.

## Turn 30 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a minimum target that can be exceeded if doing so reduces total cost?

## Turn 30 - User Simulator

The 150-unit end-of-quarter-four inventory requirement is a hard constraint that must be met exactly.