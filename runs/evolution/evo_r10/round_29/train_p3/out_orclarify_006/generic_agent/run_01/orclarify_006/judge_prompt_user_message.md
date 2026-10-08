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

QUESTION: For each product and quarter, is the contract reservation a minimum delivery requirement (i.e., you must deliver at least that many units from production plus beginning inventory, and any shortfall is backordered and incurs the delay compensation), or is it an exact target that must be met precisely each quarter?

## Turn 1 - User Simulator

The contract reservation is a minimum delivery requirement. You must deliver at least that many units from production plus beginning inventory. Any shortfall is backordered and incurs the delay compensation.

## Turn 2 - Generic Agent

QUESTION: When a product is backordered (shortfall) in a quarter, how is the delay compensation calculated — is it 20 yuan (or 10 yuan for product III) per unit for each quarter that unit remains undelivered (i.e., the penalty accumulates quarter over quarter until the unit is finally delivered), or is it a one-time 20/10 yuan per unit charged only in the quarter where the shortfall first occurs?

## Turn 2 - User Simulator

The delay compensation is 20 yuan (or 10 yuan for product III) per unit for each quarter that unit remains undelivered. The penalty accumulates quarter over quarter until the unit is finally delivered.

## Turn 3 - Generic Agent

QUESTION: The brief states that at the end of the fourth quarter, inventory of each product must be 150 units — is this a hard constraint (the model must end with exactly at least 150 units in stock for each product, with no backorders allowed to remain at the end), or is it a target that can be violated if doing so reduces total cost?

## Turn 3 - User Simulator

This is a hard constraint. The model must end with exactly 150 units in stock for each product, with no backorders allowed to remain at the end.

## Turn 4 - Generic Agent

QUESTION: The brief mentions minimizing "compensation cost + inventory holding cost" — is the total cost to minimize only these two components (delay compensation + inventory holding), or should I also include a production cost (e.g., a per-unit or per-hour manufacturing cost) in the objective?

## Turn 4 - User Simulator

The total cost to minimize is only the two components: delay compensation and inventory holding cost. There is no production cost to include in the objective.

## Turn 5 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter applies to "products produced but not delivered in the current quarter" — does this holding cost apply to all three products (I, II, and III) at the same 5 yuan rate, or does it apply only to some products?

## Turn 5 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter applies to all three products (I, II, and III) at the same rate.

## Turn 6 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — is this a hard constraint that must be respected in every quarter (i.e., total hours used across all three products in a quarter cannot exceed 15,000), or is it a soft constraint that can be exceeded at some penalty cost?

## Turn 6 - User Simulator

This is a hard constraint. The total production hours used across all three products in each quarter cannot exceed 15,000 hours.

## Turn 7 - Generic Agent

QUESTION: Can production be fractional (e.g., produce 1500.5 units of product I in a quarter), or must all production quantities be whole numbers (integer units)?

## Turn 7 - User Simulator

The available business facts do not specify whether production quantities must be whole numbers or can be fractional. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: When a product is backordered in a quarter, can you still produce additional units of that product in the same quarter beyond what is needed to cover the backorder and the current quarter's minimum delivery (i.e., can you build up positive inventory in the same quarter you are also backordering), or does a backorder in a quarter mean you cannot produce any surplus for that product in that quarter?

## Turn 8 - User Simulator

The available business facts do not specify whether you can build up positive inventory in the same quarter you are also backordering. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: The delay compensation accumulates per unit per quarter until the unit is finally delivered — when a backordered unit is eventually delivered in a later quarter, is the delivery counted against that later quarter's minimum delivery requirement (i.e., it reduces the amount you still need to deliver in that later quarter), or is it a separate "catch-up" delivery that does not count toward the later quarter's minimum?

## Turn 9 - User Simulator

The available business facts do not specify whether a backordered unit delivered in a later quarter counts against that later quarter's minimum delivery requirement or is a separate catch-up delivery. This point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (i.e., units left in stock at the end of quarter t are charged 5 yuan for that quarter), or is it charged on the average of beginning and ending inventory for the quarter?

## Turn 10 - User Simulator

The available business facts do not specify whether the inventory holding cost is charged on the ending inventory or the average of beginning and ending inventory. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: The 150 units of ending inventory required at the end of the fourth quarter — does this 150 units also incur the 5 yuan per unit per quarter holding cost for the fourth quarter (i.e., it is charged like any other ending inventory), or is it exempt from holding cost since it is a required minimum stock?

## Turn 11 - User Simulator

The available business facts do not specify whether the required 150 units of ending inventory at the end of the fourth quarter incur the 5 yuan per unit per quarter holding cost or are exempt. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: The delay compensation for a backordered unit — is it charged for each quarter the unit is undelivered starting from the quarter in which it was first due (i.e., if a unit due in Q1 is delivered in Q3, it incurs 2 quarters of penalty: Q1 and Q2), or does the penalty start accruing only from the quarter after the due quarter (i.e., the same example would incur only 1 quarter of penalty: Q2)?

## Turn 12 - User Simulator

The available business facts do not specify whether the delay compensation starts accruing from the quarter in which the unit was first due or from the quarter after the due quarter. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: The 15,000 production hours per quarter — is this the total available capacity that can be allocated freely across the three products (i.e., a shared pool where 2×units_I + 4×units_II + 3×units_III ≤ 15,000), or is there a separate per-product hour limit in addition to the total?

## Turn 13 - User Simulator

This is a shared pool. The total available capacity is 15,000 hours per quarter, allocated freely across the three products, subject to the constraint that 2×units_I + 4×units_II + 3×units_III ≤ 15,000. There is no separate per-product hour limit.

## Turn 14 - Generic Agent

QUESTION: When a backordered unit is eventually delivered in a later quarter, does that delivery count toward satisfying that later quarter's minimum delivery requirement (i.e., it reduces the amount you still need to deliver in that later quarter), or is it a separate catch-up delivery that does not count toward the later quarter's minimum?

## Turn 14 - User Simulator

The available business facts do not specify whether a backordered unit delivered in a later quarter counts toward satisfying that later quarter's minimum delivery requirement or is a separate catch-up delivery. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (units left in stock at the end of quarter t are charged 5 yuan for that quarter), or is it charged on the average of beginning and ending inventory for the quarter?

## Turn 15 - User Simulator

The available business facts do not specify whether the inventory holding cost is charged on the ending inventory or the average of beginning and ending inventory. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: The delay compensation for a backordered unit — is it charged for each quarter the unit is undelivered starting from the quarter in which it was first due (i.e., if a unit due in Q1 is delivered in Q3, it incurs 2 quarters of penalty: Q1 and Q2), or does the penalty start accruing only from the quarter after the due quarter (i.e., the same example would incur only 1 quarter of penalty: Q2)?

## Turn 16 - User Simulator

The available business facts do not specify whether the delay compensation starts accruing from the quarter in which the unit was first due or from the quarter after the due quarter. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: The 150 units of ending inventory required at the end of the fourth quarter — does this 150 units also incur the 5 yuan per unit per quarter holding cost for the fourth quarter (i.e., it is charged like any other ending inventory), or is it exempt from holding cost since it is a required minimum stock?

## Turn 17 - User Simulator

The available business facts do not specify whether the required 150 units of ending inventory at the end of the fourth quarter incur the 5 yuan per unit per quarter holding cost or are exempt. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Can production quantities be fractional (e.g., produce 1500.5 units of product I in a quarter), or must all production quantities be whole numbers (integer units)?

## Turn 18 - User Simulator

The available business facts do not specify whether production quantities must be whole numbers or can be fractional. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: When a product is backordered in a quarter, can you still produce additional units of that product in the same quarter beyond what is needed to cover the backorder and the current quarter's minimum delivery (i.e., can you build up positive inventory in the same quarter you are also backordering), or does a backorder in a quarter mean you cannot produce any surplus for that product in that quarter?

## Turn 19 - User Simulator

The available business facts do not specify whether you can build up positive inventory in the same quarter you are also backordering. This point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (units left in stock at the end of quarter t are charged 5 yuan for that quarter), or is it charged on the average of beginning and ending inventory for the quarter?

## Turn 20 - User Simulator

The available business facts do not specify whether the inventory holding cost is charged on the ending inventory or the average of beginning and ending inventory. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: The delay compensation for a backordered unit — is it charged for each quarter the unit is undelivered starting from the quarter in which it was first due (i.e., if a unit due in Q1 is delivered in Q3, it incurs 2 quarters of penalty: Q1 and Q2), or does the penalty start accruing only from the quarter after the due quarter (i.e., the same example would incur only 1 quarter of penalty: Q2)?

## Turn 21 - User Simulator

The available business facts do not specify whether the delay compensation starts accruing from the quarter in which the unit was first due or from the quarter after the due quarter. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: The 150 units of ending inventory required at the end of the fourth quarter — does this 150 units also incur the 5 yuan per unit per quarter holding cost for the fourth quarter (i.e., it is charged like any other ending inventory), or is it exempt from holding cost since it is a required minimum stock?

## Turn 22 - User Simulator

The available business facts do not specify whether the required 150 units of ending inventory at the end of the fourth quarter incur the 5 yuan per unit per quarter holding cost or are exempt. This point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: When a backordered unit is eventually delivered in a later quarter, does that delivery count toward satisfying that later quarter's minimum delivery requirement (i.e., it reduces the amount you still need to deliver in that later quarter), or is it a separate catch-up delivery that does not count toward the later quarter's minimum?

## Turn 23 - User Simulator

The available business facts do not specify whether a backordered unit delivered in a later quarter counts toward satisfying that later quarter's minimum delivery requirement or is a separate catch-up delivery. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Can production quantities be fractional (e.g., produce 1500.5 units of product I in a quarter), or must all production quantities be whole numbers (integer units)?

## Turn 24 - User Simulator

The available business facts do not specify whether production quantities must be whole numbers or can be fractional. This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: When a product is backordered in a quarter, can you still produce additional units of that product in the same quarter beyond what is needed to cover the backorder and the current quarter's minimum delivery (i.e., can you build up positive inventory in the same quarter you are also backordering), or does a backorder in a quarter mean you cannot produce any surplus for that product in that quarter?

## Turn 25 - User Simulator

The available business facts do not specify whether you can build up positive inventory in the same quarter you are also backordering. This point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (units left in stock at the end of quarter t are charged 5 yuan for that quarter), or is it charged on the average of beginning and ending inventory for the quarter?

## Turn 26 - User Simulator

The available business facts do not specify whether the inventory holding cost is charged on the ending inventory or the average of beginning and ending inventory. This point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: The delay compensation for a backordered unit — is it charged for each quarter the unit is undelivered starting from the quarter in which it was first due (i.e., if a unit due in Q1 is delivered in Q3, it incurs 2 quarters of penalty: Q1 and Q2), or does the penalty start accruing only from the quarter after the due quarter (i.e., the same example would incur only 1 quarter of penalty: Q2)?

## Turn 27 - User Simulator

The available business facts do not specify whether the delay compensation starts accruing from the quarter in which the unit was first due or from the quarter after the due quarter. This point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: The 150 units of ending inventory required at the end of the fourth quarter — does this 150 units also incur the 5 yuan per unit per quarter holding cost for the fourth quarter (i.e., it is charged like any other ending inventory), or is it exempt from holding cost since it is a required minimum stock?

## Turn 28 - User Simulator

The available business facts do not specify whether the required 150 units of ending inventory at the end of the fourth quarter incur the 5 yuan per unit per quarter holding cost or are exempt. This point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: When a backordered unit is eventually delivered in a later quarter, does that delivery count toward satisfying that later quarter's minimum delivery requirement (i.e., it reduces the amount you still need to deliver in that later quarter), or is it a separate catch-up delivery that does not count toward the later quarter's minimum?

## Turn 29 - User Simulator

The available business facts do not specify whether a backordered unit delivered in a later quarter counts toward satisfying that later quarter's minimum delivery requirement or is a separate catch-up delivery. This point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Can production quantities be fractional (e.g., produce 1500.5 units of product I in a quarter), or must all production quantities be whole numbers (integer units)?

## Turn 30 - User Simulator

The available business facts do not specify whether production quantities must be whole numbers or can be fractional. This point still needs internal confirmation.