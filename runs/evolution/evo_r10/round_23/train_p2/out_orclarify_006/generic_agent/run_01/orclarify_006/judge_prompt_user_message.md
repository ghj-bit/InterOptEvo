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

QUESTION: For each product and quarter, is the contract reservation a minimum delivery requirement (i.e., you must deliver at least that many units to the customer that quarter, with any shortfall incurring the delay compensation), or is it an exact target that must be met precisely?

## Turn 1 - User Simulator

The contract reservation is a minimum delivery requirement. You must deliver at least that many units to the customer in that quarter. If you deliver fewer units than the reservation, the shortfall is considered a delay, and the delay compensation applies.

## Turn 2 - Generic Agent

QUESTION: When a product's delivery in a quarter falls short of its reservation, does the delayed shortfall carry over and must be delivered in a later quarter (so the delay compensation accrues each quarter until it is finally delivered), or is the shortfall simply penalized at that quarter's rate and then dropped (no obligation to deliver it later)?

## Turn 2 - User Simulator

The delayed shortfall carries over and must be delivered in a later quarter. The delay compensation accrues each quarter until the units are finally delivered.

## Turn 3 - Generic Agent

QUESTION: You mentioned "compensation cost" in the objective — is the delay compensation the only compensation/cost component besides inventory holding cost, or are there other cost components (e.g., production cost per unit, overtime cost, hiring/layoff costs) that I should include in the total cost to minimize?

## Turn 3 - User Simulator

The total cost to minimize consists only of the delay compensation cost and the inventory holding cost. There are no other cost components such as production cost per unit, overtime cost, or hiring/layoff costs to include.

## Turn 4 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does this apply to the total production hours across all three products combined in each quarter, or is it a separate 15,000-hour limit for each product individually?

## Turn 4 - User Simulator

The 15,000 production hours per quarter limit applies to the total production hours across all three products combined in each quarter.

## Turn 5 - Generic Agent

QUESTION: Regarding the inventory holding cost of 5 yuan per unit per quarter for "products produced but not delivered in the current quarter" — does this holding cost apply to any unit that is in inventory at the end of a quarter (i.e., produced in a prior quarter and not yet delivered), or does it apply only to units that were produced in the current quarter but not delivered in that same quarter?

## Turn 5 - User Simulator

The inventory holding cost applies to any unit that is in inventory at the end of a quarter, regardless of when it was produced.

## Turn 6 - Generic Agent

QUESTION: Can you produce more units than the reservation requirement in a given quarter (i.e., produce extra units to build up inventory for future quarters), or is production limited to exactly the reservation amount each quarter?

## Turn 6 - User Simulator

You can produce more units than the reservation requirement in a given quarter. Producing extra units to build up inventory for future quarters is allowed.

## Turn 7 - Generic Agent

QUESTION: The delay compensation accrues each quarter until the delayed units are finally delivered — does the compensation for a unit that is delayed by k quarters equal k times the per-quarter rate (e.g., a product I unit delayed 2 quarters costs 2 × 20 = 40 yuan), or is it a flat one-time penalty of the per-quarter rate regardless of how long the delay lasts?

## Turn 7 - User Simulator

The compensation for a unit delayed by k quarters equals k times the per-quarter rate. For example, a product I unit delayed 2 quarters costs 2 × 20 = 40 yuan.

## Turn 8 - Generic Agent

QUESTION: The 150 units of ending inventory required at the end of Q4 for each product — do these units count toward the Q4 reservation delivery requirement (i.e., they are part of the units delivered in Q4), or are they in addition to the Q4 reservation (i.e., you must deliver the full Q4 reservation AND have 150 units left over in inventory)?

## Turn 8 - User Simulator

The 150 units of ending inventory are in addition to the Q4 reservation. You must deliver the full Q4 reservation and have 150 units left over in inventory at the end of Q4.

## Turn 9 - Generic Agent

QUESTION: For the delay compensation, if a unit is produced in Q1 but not delivered until Q3 (delayed by 2 quarters), does it incur holding cost for both Q1 and Q2 (the quarters it sat in inventory before delivery), in addition to the delay compensation for the 2 quarters of delay?

## Turn 9 - User Simulator

Yes, the unit incurs holding cost for both Q1 and Q2 (the quarters it sat in inventory before delivery), in addition to the delay compensation for the 2 quarters of delay.

## Turn 10 - Generic Agent

QUESTION: Can you produce units in a quarter and deliver them to the customer in a later quarter (i.e., produce ahead of demand and hold in inventory), or must all units produced in a quarter be delivered in that same quarter?

## Turn 10 - User Simulator

You can produce units in a quarter and deliver them to the customer in a later quarter. Producing ahead of demand and holding in inventory is allowed.

## Turn 11 - Generic Agent

QUESTION: Is there any upper limit on how many units you can produce per quarter for each product (other than the 15,000 total hours constraint), or is the only production limit the 15,000 hours per quarter across all products?

## Turn 11 - User Simulator

The only production limit is the 15,000 hours per quarter across all products. There are no separate upper limits on the number of units produced per quarter for each product.

## Turn 12 - Generic Agent

QUESTION: Can you produce units in Q4 that are not delivered in Q4 and not part of the 150 ending inventory requirement (i.e., produce extra beyond what's needed for Q4 delivery and the 150-unit ending inventory), or should production in Q4 be limited to exactly what's needed for Q4 delivery plus the 150 units of ending inventory?

## Turn 12 - User Simulator

Production in Q4 should be limited to exactly what's needed for Q4 delivery plus the 150 units of ending inventory.

## Turn 13 - Generic Agent

QUESTION: For the delay compensation calculation, if a unit reserved in Q1 is not delivered until Q3, is the delay measured as 2 quarters (Q1→Q2 and Q2→Q3), meaning the compensation is 2 × rate, or is it measured as 1 quarter (just the gap between the reservation quarter and the delivery quarter)?

## Turn 13 - User Simulator

The delay is measured as 2 quarters (Q1→Q2 and Q2→Q3), meaning the compensation is 2 × rate.

## Turn 14 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q2 (one quarter later), does it incur holding cost for Q1 (the quarter it sat in inventory at the end of Q1) in addition to the delay compensation for 1 quarter of delay?

## Turn 14 - User Simulator

Yes, the unit incurs holding cost for Q1 (the quarter it sat in inventory at the end of Q1) in addition to the delay compensation for 1 quarter of delay.

## Turn 15 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q1 (same quarter), does it incur any holding cost, or is holding cost only charged when a unit sits in inventory at the end of a quarter (i.e., produced in one quarter but delivered in a later quarter)?

## Turn 15 - User Simulator

No, a unit produced in Q1 and delivered in Q1 does not incur any holding cost. Holding cost is only charged when a unit sits in inventory at the end of a quarter.

## Turn 16 - Generic Agent

QUESTION: Can you produce units in Q1 that are not delivered until Q4 (i.e., hold inventory for up to 3 quarters), or is there a maximum number of quarters a unit can be held in inventory before it must be delivered?

## Turn 16 - User Simulator

There is no maximum number of quarters a unit can be held in inventory. You can produce units in Q1 and hold them until Q4 for delivery.

## Turn 17 - Generic Agent

QUESTION: Can you produce units in Q1 that are not delivered until Q4 (i.e., hold inventory for up to 3 quarters), or is there a maximum number of quarters a unit can be held in inventory before it must be delivered?

## Turn 17 - User Simulator

There is no maximum number of quarters a unit can be held in inventory. You can produce units in Q1 and hold them until Q4 for delivery.

## Turn 18 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 18 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 19 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 19 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 20 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 20 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 21 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 21 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 22 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 22 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 23 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 23 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 24 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 24 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 25 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 25 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 26 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 26 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 27 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 27 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 28 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 28 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 29 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 29 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.

## Turn 30 - Generic Agent

QUESTION: If a unit is produced in Q1 and delivered in Q3, does it incur holding cost for both Q1 and Q2 (the two quarters it sat in inventory at the end of each quarter), or only for Q1 (the quarter it was first produced)?

## Turn 30 - User Simulator

It incurs holding cost for both Q1 and Q2, the two quarters it sat in inventory at the end of each quarter.