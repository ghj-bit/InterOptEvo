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

QUESTION: For the end-of-quarter inventory requirement of 150 units per product, should I treat this as a hard constraint (inventory must be at least 150, with any excess allowed) or as an exact target (inventory must equal exactly 150)?

## Turn 1 - User Simulator

It must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 2 - Generic Agent

QUESTION: The contract reservations table gives a demand per product per quarter — should I treat these as minimum deliveries that must be met each quarter (with any extra production allowed to be carried as inventory), or as exact quantities that must be delivered in that quarter (so producing more than the reservation in a quarter is not allowed)?

## Turn 2 - User Simulator

These are minimum deliveries that must be met each quarter. Extra production is allowed and can be carried as inventory.

## Turn 3 - Generic Agent

QUESTION: The delay compensation (20 yuan per unit per quarter for products I and II, 10 yuan for product III) — since we just confirmed that the contract reservations are minimum deliveries that must be met each quarter, can a delay actually occur in this model, or should I treat the reservations as hard requirements that are always satisfied (making the delay compensation cost effectively zero and unused in the model)?

## Turn 3 - User Simulator

A delay can occur. The contract reservations are minimum deliveries, but late delivery is allowed. The delay compensation costs apply for any delay.

## Turn 4 - Generic Agent

QUESTION: When a delivery is delayed, how should I model the delay cost — specifically, if a unit of product I that was due in quarter 1 is finally delivered in quarter 3, is the delay cost 20 yuan × 2 quarters (i.e., 20 yuan for each quarter it was late), or is it a flat 20 yuan per unit regardless of how many quarters late it is?

## Turn 4 - User Simulator

The delay cost is 20 yuan per unit per quarter of delay. So if a unit of product I due in quarter 1 is delivered in quarter 3, the delay cost is 20 yuan × 2 quarters.

## Turn 5 - Generic Agent

QUESTION: When a unit is delivered late, how should I count the delay quarters — for example, if a unit of product I due in quarter 1 is delivered in quarter 3, is the delay 2 quarters (quarter 2 and quarter 3, i.e., delivery quarter minus due quarter), or 1 quarter (only the quarters between them)?

## Turn 5 - User Simulator

The delay is 2 quarters (delivery quarter minus due quarter).

## Turn 6 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to total production (including units produced for future quarters and carried as inventory), or only to units produced and delivered in the current quarter?

## Turn 6 - User Simulator

It applies to total production in that quarter, including units produced for future quarters and carried as inventory.

## Turn 7 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter applies to "products produced but not delivered in the current quarter" — should I apply this holding cost to all inventory carried at the end of each quarter (including the final 150 units at the end of quarter 4), or only to inventory carried between quarters (i.e., not charging holding cost on the end-of-quarter-4 inventory)?

## Turn 7 - User Simulator

Apply the holding cost to all inventory carried at the end of each quarter, including the final 150 units at the end of quarter 4.

## Turn 8 - Generic Agent

QUESTION: The objective mentions "compensation cost + inventory holding cost" — is the total cost to minimize just these two components (delay compensation + inventory holding), or are there also production costs (e.g., labor cost per hour or per unit) that I should include?

## Turn 8 - User Simulator

The total cost to minimize is just the delay compensation cost plus the inventory holding cost. There are no production costs to include.

## Turn 9 - Generic Agent

QUESTION: Can a unit of demand that is due in a given quarter be delivered more than one quarter late (e.g., a unit due in quarter 1 delivered in quarter 3 or 4), or is the maximum delay limited to one quarter (i.e., a unit due in quarter 1 can be delivered at the latest in quarter 2)?

## Turn 9 - User Simulator

A unit can be delivered more than one quarter late. There is no maximum delay limit; a unit due in quarter 1 can be delivered in quarter 3 or 4.

## Turn 10 - Generic Agent

QUESTION: Since there is no maximum delay limit, can a unit of demand due in quarter 4 be delivered after quarter 4 (i.e., beyond the planning horizon), or must all demand be delivered within the four quarters?

## Turn 10 - User Simulator

All demand must be delivered within the four quarters.

## Turn 11 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — is this a hard constraint (total production hours in any quarter must not exceed 15,000, with no penalty for exceeding), or is there a penalty/cost for exceeding it?

## Turn 11 - User Simulator

It is a hard constraint. Total production hours in any quarter must not exceed 15,000, with no penalty for exceeding.

## Turn 12 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is this the same rate for all three products (I, II, and III), or does it differ by product?

## Turn 12 - User Simulator

It is the same rate for all three products: 5 yuan per unit per quarter.

## Turn 13 - Generic Agent

QUESTION: When a unit is delivered late, does it still count toward the minimum delivery requirement of the quarter it was originally due in (i.e., the late delivery satisfies the original quarter's reservation), or does it count toward the delivery requirement of the quarter in which it is actually delivered?

## Turn 13 - User Simulator

It counts toward the minimum delivery requirement of the quarter it was originally due in.

## Turn 14 - Generic Agent

QUESTION: If a unit of product I due in quarter 1 is delivered in quarter 3, does it incur delay cost for both quarter 2 and quarter 3 (i.e., 20 yuan × 2 = 40 yuan), or only for the quarters between the due date and delivery (i.e., just quarter 2, so 20 yuan × 1 = 20 yuan)?

## Turn 14 - User Simulator

It incurs delay cost for both quarter 2 and quarter 3 (i.e., 20 yuan × 2 = 40 yuan).

## Turn 15 - Generic Agent

QUESTION: Can inventory be negative at the end of any quarter (i.e., can we "owe" units that will be produced and delivered in a later quarter), or must inventory at the end of every quarter be non-negative?

## Turn 15 - User Simulator

Inventory at the end of every quarter must be non-negative.

## Turn 16 - Generic Agent

QUESTION: The end-of-quarter-4 inventory must be exactly 150 units per product — does this mean that after all deliveries (including any late deliveries) are accounted for in quarter 4, the remaining inventory is exactly 150, or does it mean that 150 units must be produced in quarter 4 specifically for the ending inventory (in addition to whatever is produced for deliveries)?

## Turn 16 - User Simulator

It means that after all deliveries (including any late deliveries) are accounted for in quarter 4, the remaining inventory is exactly 150 units per product.

## Turn 17 - Generic Agent

QUESTION: Can a unit of demand due in quarter 1 be delivered in quarter 4 (i.e., 3 quarters late), or is there a practical limit on how many quarters late a delivery can be within the planning horizon?

## Turn 17 - User Simulator

Yes, a unit of demand due in quarter 1 can be delivered in quarter 4.

## Turn 18 - Generic Agent

QUESTION: When a unit is delivered late, does it still count toward the minimum delivery requirement of the quarter it was originally due in (i.e., the late delivery satisfies the original quarter's reservation), or does it count toward the delivery requirement of the quarter in which it is actually delivered?

## Turn 18 - User Simulator

It counts toward the minimum delivery requirement of the quarter it was originally due in.

## Turn 19 - Generic Agent

QUESTION: The delay compensation cost — is it charged only on the units that are actually delivered late (i.e., the cost is proportional to the number of units delivered late and how many quarters late they are), or is it charged on all units of the original quarter's reservation regardless of whether they are delivered on time or late?

## Turn 19 - User Simulator

It is charged only on the units that are actually delivered late.

## Turn 20 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (i.e., the inventory remaining after all deliveries in that quarter are made), or on the average inventory during the quarter (i.e., the average of beginning and ending inventory)?

## Turn 20 - User Simulator

It is charged on the ending inventory of each quarter.

## Turn 21 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to the total production hours across all three products combined in that quarter, or is there a separate 15,000-hour limit for each product?

## Turn 21 - User Simulator

It applies to the total production hours across all three products combined in that quarter.

## Turn 22 - Generic Agent

QUESTION: The delay compensation cost — is it charged on the units that are delivered late based on the number of quarters late (i.e., a unit due in quarter 1 delivered in quarter 3 incurs 20 yuan × 2 = 40 yuan for products I and II, or 10 yuan × 2 = 20 yuan for product III), or is it a flat penalty per unit regardless of how many quarters late?

## Turn 22 - User Simulator

It is charged based on the number of quarters late. A unit due in quarter 1 delivered in quarter 3 incurs 20 yuan × 2 = 40 yuan for products I and II, or 10 yuan × 2 = 20 yuan for product III.

## Turn 23 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (i.e., the inventory remaining after all deliveries in that quarter are made), or on the average inventory during the quarter (i.e., the average of beginning and ending inventory)?

## Turn 23 - User Simulator

It is charged on the ending inventory of each quarter.

## Turn 24 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to the total production hours across all three products combined in that quarter, or is there a separate 15,000-hour limit for each product?

## Turn 24 - User Simulator

It applies to the total production hours across all three products combined in that quarter.

## Turn 25 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (i.e., the inventory remaining after all deliveries in that quarter are made), or on the average inventory during the quarter (i.e., the average of beginning and ending inventory)?

## Turn 25 - User Simulator

It is charged on the ending inventory of each quarter.

## Turn 26 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to the total production hours across all three products combined in that quarter, or is there a separate 15,000-hour limit for each product?

## Turn 26 - User Simulator

It applies to the total production hours across all three products combined in that quarter.

## Turn 27 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (i.e., the inventory remaining after all deliveries in that quarter are made), or on the average inventory during the quarter (i.e., the average of beginning and ending inventory)?

## Turn 27 - User Simulator

It is charged on the ending inventory of each quarter.

## Turn 28 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to the total production hours across all three products combined in that quarter, or is there a separate 15,000-hour limit for each product?

## Turn 28 - User Simulator

It applies to the total production hours across all three products combined in that quarter.

## Turn 29 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — is it charged on the ending inventory of each quarter (i.e., the inventory remaining after all deliveries in that quarter are made), or on the average inventory during the quarter (i.e., the average of beginning and ending inventory)?

## Turn 29 - User Simulator

It is charged on the ending inventory of each quarter.

## Turn 30 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to the total production hours across all three products combined in that quarter, or is there a separate 15,000-hour limit for each product?

## Turn 30 - User Simulator

It applies to the total production hours across all three products combined in that quarter.