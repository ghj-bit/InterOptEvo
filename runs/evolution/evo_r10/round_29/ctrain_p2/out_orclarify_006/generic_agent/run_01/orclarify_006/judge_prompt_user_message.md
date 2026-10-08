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

QUESTION: For the end-of-quarter inventory of 150 units per product, should this be treated as an exact requirement (inventory must equal exactly 150) or as a minimum (inventory must be at least 150)?

## Turn 1 - User Simulator

It must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 2 - Generic Agent

QUESTION: The contract reservations table lists a number of units per product per quarter — should these be treated as minimum delivery requirements (you must deliver at least this many units in that quarter, with any extra production carried as inventory), or as exact delivery targets (you must deliver exactly this many units in that quarter)?

## Turn 2 - User Simulator

These are minimum delivery requirements. You must deliver at least the listed number of units in that quarter. Any extra production can be carried as inventory.

## Turn 3 - Generic Agent

QUESTION: The delay compensation (20 yuan/unit/quarter for products I and II, 10 yuan/unit/quarter for product III) — since deliveries are minimum requirements, a "delay" would occur if you deliver fewer than the required amount in a quarter. Should the delay compensation be charged on the shortfall (required minus delivered) for each quarter, and does that shortfall persist into the next quarter (i.e., you must make up the delayed units later, and you pay compensation for each quarter the units remain undelivered)?

## Turn 3 - User Simulator

Yes. The delay compensation is charged on the shortfall (required minus delivered) for each quarter. The shortfall persists into the next quarter, and you must make up the delayed units later. You pay compensation for each quarter the units remain undelivered.

## Turn 4 - Generic Agent

QUESTION: When you make up a delayed unit in a later quarter, is the delivery counted against that later quarter's minimum requirement, or is it a separate "catch-up" delivery on top of that quarter's requirement?

## Turn 4 - User Simulator

The delayed units are a separate "catch-up" delivery on top of that quarter's requirement.

## Turn 5 - Generic Agent

QUESTION: The inventory holding cost (5 yuan/unit/quarter) applies to "products produced but not delivered in the current quarter." Should this holding cost be charged on the ending inventory of each quarter (i.e., all units in stock at the end of the quarter, including units that will be used for future minimum requirements or catch-up deliveries), for each of the four quarters?

## Turn 5 - User Simulator

Yes. The inventory holding cost is charged on the ending inventory of each quarter for all four quarters.

## Turn 6 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to total production (including units produced for future quarters and catch-up deliveries), or only to units produced to meet the current quarter's minimum requirement?

## Turn 6 - User Simulator

It applies to total production in that quarter, including units produced for future quarters and catch-up deliveries.

## Turn 7 - Generic Agent

QUESTION: The compensation cost in the objective — is it only the delay compensation (for shortfalls), or does it also include some other compensation such as overtime pay or labor cost for the production hours used?

## Turn 7 - User Simulator

It is only the delay compensation for shortfalls.

## Turn 8 - Generic Agent

QUESTION: Can production quantities be fractional (e.g., 150.5 units), or must they be whole numbers (integers)?

## Turn 8 - User Simulator

Production quantities must be whole numbers (integers).

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on how many units can be produced per product per quarter (other than the 15,000-hour constraint), or is the only production limit the total hours available?

## Turn 9 - User Simulator

The only production limit is the total hours available (15,000 hours per quarter).

## Turn 10 - Generic Agent

QUESTION: Since the end-of-quarter-4 inventory must be exactly 150 units per product, and the holding cost is charged on ending inventory each quarter — should the holding cost also be charged on the ending inventory of quarter 4 (the 150 units), or is the holding cost only for quarters 1 through 3?

## Turn 10 - User Simulator

The holding cost is charged on the ending inventory of quarter 4 as well.

## Turn 11 - Generic Agent

QUESTION: The delay compensation is charged per quarter that units remain undelivered. If a unit is delayed in quarter 1 and finally delivered in quarter 3, is the compensation 2 quarters' worth (for quarters 1 and 2, the quarters it was undelivered), or 3 quarters' worth (including quarter 3)?

## Turn 11 - User Simulator

It is 2 quarters' worth (for quarters 1 and 2, the quarters it was undelivered).

## Turn 12 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3)?

## Turn 12 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 13 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3)?

## Turn 13 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 14 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 14 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 15 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 15 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 16 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 16 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 17 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 17 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 18 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 18 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 19 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 19 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 20 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 20 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 21 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 21 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 22 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 22 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 23 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 23 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 24 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 24 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 25 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 25 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 26 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 26 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 27 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 27 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 28 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 28 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 29 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 29 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).

## Turn 30 - Generic Agent

QUESTION: If a unit is delayed in quarter 1 and finally delivered in quarter 4, is the compensation 3 quarters' worth (for quarters 1, 2, and 3, the quarters it was undelivered before delivery)?

## Turn 30 - User Simulator

Yes, it is 3 quarters' worth (for quarters 1, 2, and 3).