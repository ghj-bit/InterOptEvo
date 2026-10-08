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

QUESTION: When a quarter's demand (contract reservation) exceeds what is produced and available from inventory, is the shortfall allowed to be carried over as backorder into the next quarter (incurring the delay compensation for each quarter it is late), or must every quarter's demand be fully met by the end of that same quarter?

## Turn 1 - User Simulator

The shortfall is allowed to be carried over as a backorder into the next quarter. You incur the delay compensation for each quarter the delivery is late.

## Turn 2 - Generic Agent

QUESTION: The delay compensation is charged per unit per quarter that a unit is late — is this charged on the cumulative backorder balance at the end of each quarter (i.e., a unit that is still undelivered at the end of Q1 and Q2 pays the penalty in both Q1 and Q2), or is it charged only once per unit for the first quarter it is late?

## Turn 2 - User Simulator

The delay compensation is charged on the cumulative backorder balance at the end of each quarter. A unit that is still undelivered at the end of Q1 and Q2 pays the penalty in both Q1 and Q2.

## Turn 3 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — does it apply to the total hours used to produce all three products combined in that quarter (i.e., 2×units of I + 4×units of II + 3×units of III ≤ 15,000), or is there a separate 15,000-hour limit for each product?

## Turn 3 - User Simulator

The 15,000 production hours per quarter limit applies to the total hours used to produce all three products combined in that quarter.

## Turn 4 - Generic Agent

QUESTION: The 150 units of ending inventory required at the end of Q4 for each product — does this 150 count as physical units on hand (i.e., produced but not yet delivered), or does it mean the net inventory position (on-hand minus any outstanding backorder) must equal 150?

## Turn 4 - User Simulator

The 150 units of ending inventory required at the end of Q4 for each product means the net inventory position (on-hand minus any outstanding backorder) must equal 150.

## Turn 5 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter applies to units produced but not delivered in the current quarter — is this charged on the positive on-hand inventory balance at the end of each quarter (i.e., only when you have surplus stock, and only for the units actually sitting in inventory), and is it charged in every quarter the units remain in inventory, including Q4?

## Turn 5 - User Simulator

Yes, the inventory holding cost is charged on the positive on-hand inventory balance at the end of each quarter. It is charged in every quarter the units remain in inventory, including Q4.

## Turn 6 - Generic Agent

QUESTION: The delay compensation is charged on the cumulative backorder balance at the end of each quarter — is it also charged on the backorder balance at the end of Q4 (i.e., if any units are still undelivered at the end of Q4, they pay the penalty for Q4 as well), or is the penalty only charged for quarters Q1 through Q3?

## Turn 6 - User Simulator

The delay compensation is charged on the backorder balance at the end of Q4 as well. If any units are still undelivered at the end of Q4, they pay the penalty for Q4.

## Turn 7 - Generic Agent

QUESTION: The net inventory position at the end of Q4 must equal 150 for each product — does this mean the backorder at the end of Q4 must be zero (i.e., all demand through Q4 must be fully delivered by the end of Q4, and the 150 is pure on-hand stock), or could there still be outstanding backorders at the end of Q4 as long as on-hand minus backorder equals 150?

## Turn 7 - User Simulator

The backorder at the end of Q4 must be zero. All demand through Q4 must be fully delivered by the end of Q4, and the 150 is pure on-hand stock.

## Turn 8 - Generic Agent

QUESTION: The production hours per unit (2 for I, 4 for II, 3 for III) — are these the only production costs, or is there also a per-unit production/compensation cost (e.g., a wage or labor cost per hour or per unit) that should be included in the "compensation cost" part of the objective?

## Turn 8 - User Simulator

The production hours per unit are the only production costs. There is no additional per-unit production or labor cost. The "compensation cost" in the objective refers solely to the delay compensation for late deliveries.

## Turn 9 - Generic Agent

QUESTION: The inventory holding cost of 5 yuan per unit per quarter — does this apply to all three products (I, II, and III) at the same rate of 5 yuan, or does it differ by product?

## Turn 9 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter applies to all three products (I, II, and III) at the same rate.

## Turn 10 - Generic Agent

QUESTION: Can production in a given quarter be used to satisfy demand from a previous quarter (i.e., can you produce in Q2 to cover a backorder that originated in Q1), or must each quarter's demand be satisfied only by production in that same quarter or earlier?

## Turn 10 - User Simulator

Yes, production in a given quarter can be used to satisfy demand from a previous quarter. You can produce in Q2 to cover a backorder that originated in Q1.

## Turn 11 - Generic Agent

QUESTION: Is there any upper limit on how much can be produced per quarter per product (other than the 15,000 total hours constraint), or is production only limited by the total hours available?

## Turn 11 - User Simulator

Production is only limited by the total 15,000 hours available per quarter. There is no separate upper limit on how much can be produced per quarter per product.

## Turn 12 - Generic Agent

QUESTION: Can production quantities be fractional (e.g., produce 100.5 units of product I in a quarter), or must they be whole numbers (integers)?

## Turn 12 - User Simulator

Production quantities must be whole numbers (integers).

## Turn 13 - Generic Agent

QUESTION: The contract reservations in the table (e.g., 1500 units of product I in Q1) — are these minimum delivery requirements that must be met (with the possibility of delivering more), or are they exact quantities that must be delivered in that specific quarter (no more, no less)?

## Turn 13 - User Simulator

The contract reservations are minimum delivery requirements that must be met. You can deliver more than the reservation amount in a given quarter.

## Turn 14 - Generic Agent

QUESTION: Since the contract reservations are minimums and you can deliver more, is there any upper bound on how much extra you can deliver in a given quarter beyond the reservation, or is the only constraint that you must deliver at least the reservation amount (with any extra delivery simply reducing future backorders or building inventory)?

## Turn 14 - User Simulator

There is no upper bound on how much extra you can deliver in a given quarter beyond the reservation. The only constraint is that you must deliver at least the reservation amount. Any extra delivery simply reduces future backorders or builds inventory.

## Turn 15 - Generic Agent

QUESTION: The delay compensation rates (20 yuan per unit per quarter for products I and II, 10 yuan per unit per quarter for product III) — are these the only "compensation" costs, or is there also a fixed compensation or penalty if the end-of-Q4 inventory target of 150 units is not met?

## Turn 15 - User Simulator

The delay compensation rates are the only "compensation" costs. There is no fixed compensation or penalty if the end-of-Q4 inventory target of 150 units is not met.

## Turn 16 - Generic Agent

QUESTION: The end-of-Q4 requirement that each product must have exactly 150 units of on-hand inventory (with zero backorder) — is this a hard constraint (the schedule must satisfy it exactly), or is it a target that can be violated at some cost?

## Turn 16 - User Simulator

This is a hard constraint. The schedule must satisfy it exactly.

## Turn 17 - Generic Agent

QUESTION: The 15,000 production hours per quarter — is this a hard constraint (total hours used must be ≤ 15,000 in every quarter), or can it be exceeded at some penalty cost?

## Turn 17 - User Simulator

This is a hard constraint. Total hours used must be ≤ 15,000 in every quarter.

## Turn 18 - Generic Agent

QUESTION: The initial inventory at the beginning of Q1 is 0 for all three products — is there any initial backorder (i.e., demand from before Q1 that is already undelivered), or does the planning horizon start fresh with zero inventory and zero backorder?

## Turn 18 - User Simulator

The planning horizon starts fresh with zero inventory and zero backorder.

## Turn 19 - Generic Agent

QUESTION: The inventory holding cost is charged on the positive on-hand inventory balance at the end of each quarter — is the on-hand inventory balance calculated as (cumulative production minus cumulative deliveries) for each product, where deliveries can exceed the reservation in any quarter, and the holding cost applies to whatever positive balance remains at the end of each quarter?

## Turn 19 - User Simulator

Yes, the on-hand inventory balance is calculated as (cumulative production minus cumulative deliveries) for each product. The holding cost applies to whatever positive balance remains at the end of each quarter.

## Turn 20 - Generic Agent

QUESTION: The backorder balance at the end of each quarter is calculated as (cumulative deliveries minus cumulative production) when deliveries exceed production — is the delay compensation charged on this positive backorder balance at the end of each quarter, and can the backorder balance be negative (i.e., can you have both on-hand inventory and backorder simultaneously for the same product in the same quarter)?

## Turn 20 - User Simulator

The delay compensation is charged on the positive backorder balance at the end of each quarter. No, you cannot have both on-hand inventory and backorder simultaneously for the same product in the same quarter.

## Turn 21 - Generic Agent

QUESTION: The objective is to minimize total cost (delay compensation + inventory holding cost) — is there any other cost component I should include, such as a cost for unused production hours, a cost for overtime, or any other term?

## Turn 21 - User Simulator

No, there are no other cost components. The objective is solely to minimize the sum of delay compensation and inventory holding cost.

## Turn 22 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Planning horizon:** 4 quarters (Q1–Q4), 3 products (I, II, III).

**Decision variables (integer, non-negative):**
- Production quantity of each product in each quarter (units).
- Delivery quantity of each product in each quarter (units).

**Parameters:**
- Contract reservations (minimum deliveries) per product per quarter as given in the table.
- Production hours per unit: I = 2, II = 4, III = 3.
- Total production hours available per quarter: 15,000 (hard constraint, all products combined).
- Delay compensation per unit per quarter: I = 20, II = 20, III = 10 (charged on positive backorder balance at end of each quarter, including Q4).
- Inventory holding cost: 5 yuan per unit per quarter for all products (charged on positive on-hand inventory balance at end of each quarter, including Q4).
- Initial inventory = 0, initial backorder = 0 for all products.

**Constraints:**
1. **Production hours:** For each quarter, 2×(units of I) + 4×(units of II) + 3×(units of III) ≤ 15,000.
2. **Minimum delivery:** Deliveries in each quarter ≥ contract reservation for each product.
3. **No simultaneous inventory and backorder:** For each product at the end of each quarter, either on-hand inventory ≥ 0 with backorder = 0, or backorder ≥ 0 with on-hand inventory = 0 (mutually exclusive).
4. **End-of-Q4 requirement (hard):** For each product, on-hand inventory = 150 and backorder = 0 at the end of Q4.
5. **Integrality:** All production and delivery quantities are non-negative integers.

**Objective:** Minimize total delay compensation (sum over all quarters and products of penalty rate × positive backorder balance at end of quarter) + total inventory holding cost (sum over all quarters and products of 5 × positive on-hand inventory balance at end of quarter).

**Key clarifications confirmed:**
- Backorders can be carried forward and paid each quarter they persist.
- Production in any quarter can satisfy demand from any prior quarter.
- Deliveries can exceed reservations (no upper bound on extra delivery).
- No other cost components exist.
- All constraints (hours, end-of-Q4 inventory) are hard.