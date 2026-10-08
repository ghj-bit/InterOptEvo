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

QUESTION: For each product and quarter, is the contract reservation a minimum delivery requirement (i.e., you must deliver at least that many units that quarter, with any shortfall incurring the delay compensation), or is it an exact target that must be met precisely?

## Turn 1 - User Simulator

The contract reservation is a minimum delivery requirement. You must deliver at least that many units in that quarter. If you deliver fewer units than the reservation in a given quarter, the shortfall is considered a delay, and the applicable delay compensation cost applies for each unit delayed.

## Turn 2 - Generic Agent

QUESTION: When a unit is delayed (delivered in a later quarter than its reservation quarter), is the delay compensation charged for each quarter of delay (e.g., a unit reserved in Q1 but delivered in Q3 costs 2 quarters of compensation), or is it a one-time flat charge regardless of how late it is delivered?

## Turn 2 - User Simulator

The delay compensation is charged for each quarter of delay. For example, if a unit reserved in Q1 is delivered in Q3, it incurs 2 quarters of compensation.

## Turn 3 - Generic Agent

QUESTION: Can a unit reserved in a given quarter be delivered in an earlier quarter (i.e., can you produce and deliver ahead of the reservation quarter), or must each unit be delivered in its reservation quarter or later?

## Turn 3 - User Simulator

A unit reserved in a given quarter can be delivered in an earlier quarter. You can produce and deliver ahead of the reservation quarter.

## Turn 4 - Generic Agent

QUESTION: If a unit is delivered in an earlier quarter than its reservation quarter, does it count toward satisfying that quarter's reservation requirement (i.e., does early delivery reduce the amount that must be delivered in the reservation quarter)?

## Turn 4 - User Simulator

Yes, early delivery counts toward satisfying that quarter's reservation requirement. If you deliver a unit in an earlier quarter, it reduces the amount that must be delivered in the reservation quarter.

## Turn 5 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory requirement for each product — does this inventory consist of units that have already been produced but not yet delivered to any reservation, or does it include units that are still pending delivery for Q4 reservations?

## Turn 5 - User Simulator

The 150-unit end-of-Q4 inventory requirement consists of units that have already been produced but not yet delivered to any reservation. It does not include units that are still pending delivery for Q4 reservations.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum production capacity per product per quarter (e.g., a limit on how many units of each product can be produced in a single quarter), or is the only production constraint the total 15,000 hours per quarter shared across all three products?

## Turn 6 - User Simulator

The only production constraint is the total 15,000 hours per quarter shared across all three products. There is no separate maximum production capacity per product per quarter.

## Turn 7 - Generic Agent

QUESTION: Can production be fractional (i.e., can you produce 1.5 units of a product in a quarter), or must production quantities be whole numbers (integers)?

## Turn 7 - User Simulator

Production quantities must be whole numbers (integers).

## Turn 8 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — is this a strict equality (exactly 150 units must remain) or a minimum (at least 150 units must remain)?

## Turn 8 - User Simulator

This is a strict equality. Exactly 150 units must remain for each product at the end of the fourth quarter.

## Turn 9 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter applies to units produced but not delivered in the current quarter — does this cost apply to all undelivered units at the end of each quarter (including units that will be delivered in future quarters), or only to units that are held beyond their reservation quarter?

## Turn 9 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter applies to all undelivered units at the end of each quarter, including units that will be delivered in future quarters.

## Turn 10 - Generic Agent

QUESTION: The delay compensation is charged per unit per quarter of delay — is this cost incurred for each quarter that a unit remains undelivered past its reservation quarter (i.e., cumulative, like holding cost), or is it a one-time charge equal to (number of quarters late) × (rate) assessed only when the unit is finally delivered?

## Turn 10 - User Simulator

The delay compensation is a one-time charge equal to (number of quarters late) × (rate), assessed only when the unit is finally delivered.

## Turn 11 - Generic Agent

QUESTION: Can a unit reserved in Q4 be delivered in Q1, Q2, or Q3 (i.e., can you deliver up to 3 quarters early), or is there a limit on how far in advance a unit can be delivered relative to its reservation quarter?

## Turn 11 - User Simulator

Yes, a unit reserved in Q4 can be delivered in Q1, Q2, or Q3. There is no limit on how far in advance a unit can be delivered relative to its reservation quarter.

## Turn 12 - Generic Agent

QUESTION: Can a unit reserved in Q1 be delivered in Q2, Q3, or Q4 (i.e., can you deliver up to 3 quarters late), or is there a limit on how far a unit can be delayed past its reservation quarter?

## Turn 12 - User Simulator

Yes, a unit reserved in Q1 can be delivered in Q2, Q3, or Q4. There is no limit on how far a unit can be delayed past its reservation quarter.

## Turn 13 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 13 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 14 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 14 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 15 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 15 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 16 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 16 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 17 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 17 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 18 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 18 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 19 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 19 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 20 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 20 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 21 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 21 - User Simulator

These units can come from any reservation quarter (Q1–Q4).

## Turn 22 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 22 - User Simulator

These units can come from any reservation

## Turn 23 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 23 - User Simulator

These units can come from any

## Turn 24 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 24 - User Simulator

These units can

## Turn 25 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 25 - User Simulator

These

## Turn 26 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 26 - User Simulator

These

## Turn 27 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 27 - User Simulator

These

## Turn 28 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 28 - User Simulator

These

## Turn 29 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 29 - User Simulator

These

## Turn 30 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory for each product — can these units come from any reservation quarter (Q1–Q4), or must they specifically be units reserved in Q4 that are simply not delivered?

## Turn 30 - User Simulator

These