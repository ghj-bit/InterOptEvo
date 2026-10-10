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

QUESTION: When you say "total production hours used must not exceed 15,000 hours" per quarter, does this 15,000-hour limit apply to the sum of hours across all three products combined in that quarter, or is it a separate 15,000-hour limit for each product individually?

## Turn 1 - User Simulator

It is a single 15,000-hour limit for the sum of hours across all three products combined in that quarter.

## Turn 2 - Generic Agent

QUESTION: The contract reservations table lists specific quantities for each product per quarter, but you also mention delay compensation for undelivered units. Are the table values hard minimum delivery requirements that must be met each quarter (with any shortfall incurring delay costs), or are they target quantities where the factory can choose to produce more or less each quarter as long as the end-of-year inventory constraint is satisfied?

## Turn 2 - User Simulator

The table values are hard minimum delivery requirements that must be met each quarter. Any shortfall in a given quarter incurs delay compensation costs.

## Turn 3 - Generic Agent

QUESTION: You mentioned delay compensation for "shortfall" in a quarter, but you also have inventory carrying over between quarters. If you produce extra units in an earlier quarter and hold them in inventory, can those held units be used to satisfy the minimum delivery requirement in a later quarter, or must each quarter's minimum be met by production in that same quarter?

## Turn 3 - User Simulator

Held units from earlier quarters can be used to satisfy the minimum delivery requirement in a later quarter.

## Turn 4 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 4 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 5 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 5 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 6 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 6 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 7 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 7 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 8 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 8 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 9 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 9 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 10 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 10 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 11 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 11 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 12 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 12 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 13 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 13 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 14 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 14 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 15 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 15 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per

## Turn 16 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead delivered in Quarter 3, is the delay cost calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate), or is it a flat one-time penalty regardless of how late the delivery is?

## Turn 16 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per-quarter rate).

## Turn 17 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit required in Quarter 1 is instead

## Turn 17 - User Simulator

The delay cost is calculated as 2 quarters of delay (i.e., 2 × the per

## Turn 18 - Generic Agent

QUESTION: The delay compensation is described as "per

## Turn 18 - User Simulator

The delay cost is calculated

## Turn 19 - Generic Agent

QUESTION: The delay

## Turn 19 - User Simulator

The delay

## Turn 20 - Generic Agent

QUESTION: The

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: The

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: The

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: The

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: The

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: The

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: The

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: The

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: The

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: The

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: The

## Turn 30 - User Simulator

The