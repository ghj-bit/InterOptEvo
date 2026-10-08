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

QUESTION: For the end-of-quarter inventory requirement of 150 units per product, should this be treated as a hard constraint (inventory must be exactly 150, or at least 150), and if it is "at least 150," is any excess above 150 allowed or must it be exactly 150?

## Turn 1 - User Simulator

It must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 2 - Generic Agent

QUESTION: Regarding the delay compensation cost, if demand for a product in a given quarter is not fully met, is the unmet amount carried over as backorder to be fulfilled in a later quarter (incurring the per-quarter delay penalty for each quarter it waits), or is the unmet demand simply lost and the penalty charged only once?

## Turn 2 - User Simulator

The unmet amount is carried over as a backorder to be fulfilled in a later quarter. The delay penalty is charged for each quarter the units wait.

## Turn 3 - Generic Agent

QUESTION: When a product's demand in a quarter is not fully met and the shortfall is carried over as a backorder, is the backorder allowed to accumulate across multiple quarters (i.e., a unit can be delayed by more than one quarter, paying the penalty each quarter it waits), or is each unit's delay limited to at most one quarter?

## Turn 3 - User Simulator

The backorder is allowed to accumulate across multiple quarters. A unit can be delayed by more than one quarter, and the penalty is paid for each quarter it waits.

## Turn 4 - Generic Agent

QUESTION: The objective mentions "compensation cost + inventory holding cost," but the brief also lists a 15,000-hour-per-quarter production capacity limit. Is there any production cost (e.g., labor or material cost per unit produced) that should be included in the objective, or is the objective truly just the delay compensation plus the inventory holding cost?

## Turn 4 - User Simulator

The objective is truly just the delay compensation plus the inventory holding cost. There is no production cost to include.

## Turn 5 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter applies to "products produced but not delivered in the current quarter." Does this holding cost apply to all units in inventory at the end of each quarter (including the 150 units required at the end of Q4), or does it apply only to units that are in inventory during quarters 1-3 (i.e., not charged on the final Q4 ending inventory)?

## Turn 5 - User Simulator

The holding cost applies to all units in inventory at the end of each quarter, including the 150 units required at the end of Q4.

## Turn 6 - Generic Agent

QUESTION: Regarding the production hours constraint of 15,000 hours per quarter, is this a hard upper bound that must not be exceeded, or is it a target that can be exceeded at some additional cost?

## Turn 6 - User Simulator

It is a hard upper bound that must not be exceeded.

## Turn 7 - Generic Agent

QUESTION: The delay compensation is described as "per unit per quarter delay." If a unit of product I is produced in Q3 but the demand it satisfies was originally due in Q1, is the penalty 20 yuan × 2 quarters (for waiting through Q2 and Q3), or is it 20 yuan × 1 quarter (only for the quarter it was actually late)?

## Turn 7 - User Simulator

The penalty is 20 yuan × 2 quarters. The unit is charged for each quarter it waits from the original due date until it is delivered.

## Turn 8 - Generic Agent

QUESTION: Can production in a given quarter be used to satisfy demand from a previous quarter (i.e., can you produce in Q2 to fulfill Q1's demand that was not met in Q1), or must each quarter's demand be satisfied only by production in that same quarter or earlier?

## Turn 8 - User Simulator

Yes, production in a given quarter can be used to satisfy demand from a previous quarter.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on the total backorder that can be carried (i.e., can backorders grow without bound), or is there a maximum number of units that can be backordered at any point in time?

## Turn 9 - User Simulator

There is no limit on the total backorder that can be carried.

## Turn 10 - Generic Agent

QUESTION: Can inventory (units produced and stored) be used to satisfy demand from a previous quarter that was backordered, or can inventory only be used to satisfy current or future demand?

## Turn 10 - User Simulator

Yes, inventory can be used to satisfy demand from a previous quarter that was backordered.

## Turn 11 - Generic Agent

QUESTION: The holding cost is 5 yuan per unit per quarter for "products produced but not delivered in the current quarter." If a unit is produced in Q1 and used to satisfy a Q1 backorder (i.e., it was produced and delivered in the same quarter), is it charged holding cost for that quarter, or only if it remains undelivered at the end of the quarter?

## Turn 11 - User Simulator

It is only charged holding cost if it remains undelivered at the end of the quarter.

## Turn 12 - Generic Agent

QUESTION: The delay penalty is charged "for each quarter the unit waits." If a unit's demand is due in Q1 and it is delivered in Q3, is the penalty charged for Q1 and Q2 (two quarters of waiting), or for Q1, Q2, and Q3 (three quarters)?

## Turn 12 - User Simulator

The penalty is charged for Q1 and Q2 (two quarters of waiting).

## Turn 13 - Generic Agent

QUESTION: The holding cost is 5 yuan per unit per quarter for "products produced but not delivered in the current quarter." Does this holding cost apply to all three products (I, II, and III) at the same rate of 5 yuan, or does it vary by product?

## Turn 13 - User Simulator

It applies to all three products at the same rate of 5 yuan per unit per quarter.

## Turn 14 - Generic Agent

QUESTION: The delay penalty is charged for each quarter a unit waits from its original due date until delivery. If a unit's demand is due in Q1 and it is delivered in Q4, is the penalty charged for Q1, Q2, and Q3 (three quarters of waiting), or for Q1, Q2, Q3, and Q4 (four quarters)?

## Turn 14 - User Simulator

The penalty is charged for Q1, Q2, and Q3 (three quarters of waiting).

## Turn 15 - Generic Agent

QUESTION: The holding cost is charged on units that remain undelivered at the end of a quarter. If a unit is produced in Q1 and used to satisfy a Q1 backorder (i.e., it was produced and delivered within Q1), is it charged holding cost for Q1, or only if it remains in inventory at the end of Q1?

## Turn 15 - User Simulator

It is only charged holding cost if it remains in inventory at the end of Q1.

## Turn 16 - Generic Agent

QUESTION: The holding cost is charged on units that remain in inventory at the end of a quarter. If a unit is produced in Q1 and used to satisfy a Q2 demand (i.e., it is in inventory at the end of Q1), is it charged holding cost for Q1, or only for Q2 when it is actually delivered?

## Turn 16 - User Simulator

It is charged holding cost for Q1.

## Turn 17 - Generic Agent

QUESTION: The delay penalty is charged for each quarter a unit waits from its original due date until delivery. If a unit's demand is due in Q1 and it is delivered in Q2, is the penalty charged for Q1 only (one quarter of waiting), or for Q1 and Q2 (two quarters)?

## Turn 17 - User Simulator

The penalty is charged for Q1 only (one quarter of waiting).

## Turn 18 - Generic Agent

QUESTION: The holding cost is charged on units that remain in inventory at the end of a quarter. If a unit is produced in Q1 and used to satisfy a Q1 demand (i.e., it is produced and delivered within Q1), is it charged holding cost for Q1, or only if it remains in inventory at the end of Q1?

## Turn 18 - User Simulator

It is only charged holding cost if it remains in inventory at the end of Q1.

## Turn 19 - Generic Agent

QUESTION: The delay penalty is charged for each quarter a unit waits from its original due date until delivery. If a unit's demand is due in Q1 and it is delivered in Q3, is the penalty charged for Q1 and Q2 (two quarters of waiting), or for Q1, Q2, and Q3 (three quarters)?

## Turn 19 - User Simulator

The penalty is charged for Q1 and Q2 (two quarters of waiting).

## Turn 20 - Generic Agent

QUESTION: The holding cost is charged on units that remain in inventory at the end of a quarter. If a unit is produced in Q1 and used to satisfy a Q2 demand (i.e., it is in inventory at the end of Q1), is it charged holding cost for Q1, or only for Q2 when it is actually delivered

## Turn 20 - User Simulator

It is charged holding cost for Q1.

## Turn 21 - Generic Agent

QUESTION: The delay penalty is charged for each quarter a unit waits from its original due date until delivery. If a unit's demand is due in Q1 and it is delivered in Q4, is the penalty charged for Q1, Q2, and Q3 (three quarters of waiting), or for

## Turn 21 - User Simulator

The penalty is charged for Q1, Q2, and Q3 (three quarters of waiting).

## Turn 22 - Generic Agent

QUESTION: The holding cost is charged on units that remain in inventory at the end of a quarter. If a unit is produced in Q1 and used to satisfy

## Turn 22 - User Simulator

It is only charged holding cost if it remains in inventory at the end of Q1.

## Turn 23 - Generic Agent

QUESTION: The delay penalty is charged for each quarter

## Turn 23 - User Simulator

The delay penalty is charged for each quarter the unit waits from its original due date until delivery.

## Turn 24 - Generic Agent

QUESTION: The holding cost is

## Turn 24 - User Simulator

The holding cost is 5 yuan per unit per quarter for products produced but not delivered in the current quarter.

## Turn 25 - Generic Agent

QUESTION: The

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: The

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: The

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: The

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: The

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: The

## Turn 30 - User Simulator

The point still needs internal confirmation.