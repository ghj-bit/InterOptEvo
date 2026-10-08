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

QUESTION: For the "20 yuan per unit per quarter delay" compensation, is the delay measured as the number of quarters a unit is late (so a unit produced in Q3 to satisfy a Q1 contract costs 2×20 = 40 yuan), or is it a flat 20 yuan per unit regardless of how many quarters late it is?

## Turn 1 - User Simulator

It is measured as the number of quarters a unit is late. So, a unit produced in Q3 to satisfy a Q1 contract costs 2 × 20 = 40 yuan.

## Turn 2 - Generic Agent

QUESTION: The brief states "total production hours used must not exceed 15,000 hours" per quarter, but it does not mention any cost for the workers themselves. Is the "compensation cost" in the objective simply the delay compensation (backorder penalty), or is there a separate labor/wage cost per production hour that I should include?

## Turn 2 - User Simulator

The "compensation cost" in the objective is simply the delay compensation (backorder penalty). There is no separate labor or wage cost per production hour to include.

## Turn 3 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory requirement — is it a hard constraint that must be met exactly (or at least 150), or is it a target that can be violated if doing so reduces total cost?

## Turn 3 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 4 - Generic Agent

QUESTION: Can production in a given quarter be used to satisfy demand from a *later* quarter (i.e., build inventory to cover future contracts), or must each quarter's production only satisfy that quarter's own contract plus the final 150-unit requirement?

## Turn 4 - User Simulator

Yes, production in a given quarter can be used to satisfy demand from a later quarter. You can build inventory to cover future contracts, and the inventory holding cost of 5 yuan per unit per quarter applies to those units.

## Turn 5 - Generic Agent

QUESTION: Can production in a given quarter be used to satisfy demand from an *earlier* quarter (i.e., produce late and pay the delay compensation), or must each quarter's contract be satisfied by production in that same quarter or earlier only?

## Turn 5 - User Simulator

Yes, production in a given quarter can be used to satisfy demand from an earlier quarter. Late delivery is allowed, and the delay compensation costs apply for any delay.

## Turn 6 - Generic Agent

QUESTION: Is there a limit on how many quarters late a unit can be delivered? For example, can a Q1 contract be satisfied by production in Q4 (3 quarters late), or is there a maximum allowable delay?

## Turn 6 - User Simulator

There is no maximum allowable delay. A Q1 contract can be satisfied by production in Q4 (3 quarters late), and the delay compensation would apply for all 3 quarters.

## Turn 7 - Generic Agent

QUESTION: Can production in a given quarter exceed that quarter's contract demand (i.e., produce more than needed for current-quarter delivery and carry the surplus as inventory), or is production in each quarter capped at that quarter's contract quantity?

## Turn 7 - User Simulator

Yes, production in a given quarter can exceed that quarter's contract demand. You can produce more than needed for current-quarter delivery and carry the surplus as inventory, incurring the 5 yuan per unit per quarter holding cost.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on how many units of each product can be produced in a quarter (other than the 15,000-hour capacity constraint), or is the only production limit the total hours available?

## Turn 8 - User Simulator

The only production limit is the total 15,000 hours available per quarter. There is no separate upper limit on the number of units of each product that can be produced in a quarter.

## Turn 9 - Generic Agent

QUESTION: The 150-unit end-of-Q4 inventory requirement — does this 150 units count toward satisfying Q4's contract demand, or is it in addition to Q4's contract (i.e., Q4 must produce/deliver its contract amount AND have 150 units left over)?

## Turn 9 - User Simulator

The 150 units are in addition to Q4's contract demand. Q4 must deliver its contract amount and have 150 units left over in inventory at the end of the quarter.

## Turn 10 - Generic Agent

QUESTION: Can a unit be produced in a quarter and then used to satisfy a contract from the *same* quarter (i.e., same-quarter production counts as on-time delivery with zero delay cost), or does same-quarter production always incur at least one quarter of holding cost?

## Turn 10 - User Simulator

Same-quarter production counts as on-time delivery with zero delay cost.

## Turn 11 - Generic Agent

QUESTION: If a unit is produced in Q1 and used to satisfy a Q3 contract, does it incur 2 quarters of holding cost (Q1→Q2 and Q2→Q3), or only 1 quarter of holding cost?

## Turn 11 - User Simulator

It incurs 2 quarters of holding cost (Q1→Q2 and Q2→Q3).

## Turn 12 - Generic Agent

QUESTION: If a unit is produced in Q3 to satisfy a Q1 contract (2 quarters late), does it incur any inventory holding cost in addition to the delay compensation, or is the delay compensation the only cost for late-delivered units?

## Turn 12 - User Simulator

The delay compensation is the only cost for late-delivered units. There is no additional inventory holding cost for units produced late to satisfy earlier contracts.

## Turn 13 - Generic Agent

QUESTION: Is there any limit on how many units can be delivered late in a single quarter (i.e., can all of a quarter's contract be satisfied by production from a later quarter), or is there a maximum fraction or number of units that can be delayed per quarter?

## Turn 13 - User Simulator

There is no limit on how many units can be delivered late in a single quarter. All of a quarter's contract can be satisfied by production from a later quarter, with the delay compensation applying for each quarter of delay.

## Turn 14 - Generic Agent

QUESTION: Is there any minimum production requirement per quarter (e.g., the factory must produce at least some number of units each quarter), or can a quarter have zero production if all demand is met from inventory or future production?

## Turn 14 - User Simulator

There is no minimum production requirement per quarter. A quarter can have zero production if all demand is met from inventory or future production.

## Turn 15 - Generic Agent

QUESTION: For the 150-unit end-of-Q4 inventory, is it exactly 150 units (no more, no less) or at least 150 units?

## Turn 15 - User Simulator

It is exactly 150 units.

## Turn 16 - Generic Agent

QUESTION: If a unit is produced in Q2 to satisfy a Q1 contract (1 quarter late), does it incur 1 quarter of delay compensation (20 or 10 yuan depending on product), or does it also incur 1 quarter of holding cost (5 yuan) for the period it sits in inventory before being delivered?

## Turn 16 - User Simulator

It incurs only 1 quarter of delay compensation (20 or 10 yuan depending on product). There is no additional inventory holding cost for units produced late to satisfy earlier contracts.

## Turn 17 - Generic Agent

QUESTION: Can a unit be produced in a quarter and then used to satisfy a contract from a *later* quarter while also incurring holding cost for each quarter it sits in inventory, or is the holding cost only applied to units that are produced and not delivered in the current quarter (i.e., carried to the next quarter)?

## Turn 17 - User Simulator

The holding cost is applied to units that are produced and not delivered in the current quarter. Each quarter a unit sits in inventory before being delivered to a later contract, it incurs 5 yuan per unit per quarter of holding cost.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that all contract demand must eventually be satisfied (i.e., every unit in the contract table must be delivered by the end of Q4), or can some contract units go undelivered if the cost of producing them is too high?

## Turn 18 - User Simulator

All contract demand must eventually be satisfied. Every unit in the contract table must be delivered by the end of Q4.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the total production across all four quarters must equal the total contract demand plus the 150-unit end-of-Q4 inventory (i.e., no excess production allowed), or can the factory produce more than the total demand if it reduces total cost?

## Turn 19 - User Simulator

The total production across all four quarters must equal the total contract demand plus the 150-unit end-of-Q4 inventory. No excess production is allowed.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint on the inventory level at the end of Q1, Q2, or Q3 (e.g., a minimum or maximum inventory level), or are the only inventory constraints the initial inventory of 0 at the start of Q1 and the final inventory of exactly 150 units per product at the end of Q4?

## Turn 20 - User Simulator

There are no constraints on the inventory level at the end of Q1, Q2, or Q3. The only inventory constraints are the initial inventory of 0 at the start of Q1 and the final inventory of exactly 150 units per product at the end of Q4.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that inventory levels must be non-negative at all times (i.e., you cannot have negative inventory), or can inventory go negative (representing backorders) as long as the final Q4 inventory is exactly 150 units?

## Turn 21 - User Simulator

Inventory levels must be non-negative at all times. You cannot have negative inventory.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the production hours used in a quarter must be exactly 15,000 hours, or can they be less than 15,000 hours (i.e., the 15,000 hours is an upper bound, not a requirement)?

## Turn 22 - User Simulator

The 15,000 hours is an upper bound, not a requirement. Production hours used in a quarter can be less than 15,000 hours.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the production of each product in a quarter must be an integer number of units, or can production be fractional (e.g., 150.5 units)?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the delivery of each product to each quarter's contract must be an integer number of units, or can deliveries be fractional?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the inventory level of each product at the end of each quarter must be an integer number of units, or can inventory be fractional?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the delay compensation is only incurred for units that are delivered late (i.e., produced after the contract quarter), or is there also a penalty for units that are produced early and held in inventory (in addition to the 5 yuan holding cost)?

## Turn 26 - User Simulator

The delay compensation is only incurred for units that are delivered late (i.e., produced after the contract quarter). There is no additional penalty for units that are produced early and held in inventory, other than the 5 yuan per unit per quarter holding cost.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the total production hours used across all four quarters must not exceed some annual limit (in addition to the 15,000 hours per quarter limit), or is the only production capacity constraint the 15,000 hours per quarter?

## Turn 27 - User Simulator

The only production capacity constraint is the 15,000 hours per quarter. There is no separate annual limit on total production hours.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the factory must produce all three products in every quarter, or can a quarter have zero production of one or more products?

## Turn 28 - User Simulator

There is no constraint that the factory must produce all three products in every quarter. A quarter can have zero production of one or more products.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the inventory holding cost of 5 yuan per unit per quarter applies to all products equally, or does it vary by product?

## Turn 29 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter applies to all products equally.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the delay compensation rates (20 yuan for products I and II, 10 yuan for product III) are per unit per quarter of delay, or are they flat rates per unit regardless of how many quarters late?

## Turn 30 - User Simulator

The delay compensation rates are per unit per quarter of delay.