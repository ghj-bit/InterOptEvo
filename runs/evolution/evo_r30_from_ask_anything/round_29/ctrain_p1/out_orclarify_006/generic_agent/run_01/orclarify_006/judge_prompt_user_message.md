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

QUESTION: When you say "total production hours used must not exceed 15,000 hours" per quarter, does that 15,000-hour limit apply to the sum of hours across all three products combined in that quarter?

## Turn 1 - User Simulator

Yes, the 15,000-hour limit is the total production hours available for all three products combined in each quarter.

## Turn 2 - Generic Agent

QUESTION: For the "contract reservations" in the table, are these quantities that must be delivered to customers in that specific quarter (i.e., demand that must be met on time), or are they minimum production targets that can be produced and held in inventory?

## Turn 2 - User Simulator

They are quantities that must be delivered to customers in that specific quarter. Late delivery is allowed, but it incurs the delay compensation costs.

## Turn 3 - Generic Agent

QUESTION: When a unit is delivered late, does it count toward the 15,000-hour production limit in the quarter it is actually produced, or in the quarter it was originally due?

## Turn 3 - User Simulator

It counts toward the 15,000-hour production limit in the quarter it is actually produced.

## Turn 4 - Generic Agent

QUESTION: For the delay compensation cost, if a unit of product I due in quarter 1 is delivered in quarter 3, is the penalty 20 yuan × 2 quarters (one quarter for each quarter of delay), or is it a flat 20 yuan regardless of how late it is?

## Turn 4 - User Simulator

It is 20 yuan per unit per quarter of delay. So if a unit of product I due in quarter 1 is delivered in quarter 3, the penalty is 20 yuan × 2 quarters.

## Turn 5 - Generic Agent

QUESTION: Can a unit that is delivered late still be counted toward the 150-unit end-of-quarter-4 inventory requirement for each product?

## Turn 5 - User Simulator

No. The 150-unit end-of-quarter-4 inventory requirement is for units in stock at the end of quarter 4. A unit delivered late has already been delivered to the customer, so it is not in inventory.

## Turn 6 - Generic Agent

QUESTION: Can a unit that is delivered late still be counted toward the 150-unit end-of-quarter-4 inventory requirement for each product?

## Turn 6 - User Simulator

No. A unit that is delivered late has been delivered to the customer, so it is not in inventory. The 150-unit requirement is for units remaining in stock at the end of quarter 4.

## Turn 7 - Generic Agent

QUESTION: For the inventory holding cost of 5 yuan per unit per quarter, does this apply to all units in inventory at the end of each quarter (including units produced early for future quarters), or only to units that are "produced but not delivered in the current quarter"?

## Turn 7 - User Simulator

It applies to all units in inventory at the end of each quarter, including units produced early for future quarters.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum inventory capacity limit per product per quarter, or can inventory grow without bound?

## Turn 8 - User Simulator

There is no maximum inventory capacity limit per product per quarter.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about, such as minimum production quantities per quarter, workforce limits, or restrictions on which products can be produced in which quarters?

## Turn 9 - User Simulator

Yes, there is one additional restriction: Product I cannot be produced in the second quarter due to an equipment change.

## Turn 10 - Generic Agent

QUESTION: Is the production of Product I in the second quarter completely zero, or is there a reduced capacity available?

## Turn 10 - User Simulator

Production of Product I in the second quarter is completely zero.

## Turn 11 - Generic Agent

QUESTION: Are there any other restrictions or constraints I should know about, such as minimum production quantities per quarter, workforce limits, or restrictions on which products can be produced in which quarters?

## Turn 11 - User Simulator

No, there are no other restrictions or constraints beyond what has already been discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Minimize total cost = total delay compensation cost + total inventory holding cost over 4 quarters.

**Decision Variables:**
- Production quantity of each product (I, II, III) in each quarter (1–4).
- These are continuous, non-negative quantities (no integrality requirement stated).

**Parameters:**
- **Demand (contract reservations) per product per quarter:**
  - Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200
  - Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500
  - Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500
- **Production hours per unit:** Product I = 2 hrs, Product II = 4 hrs, Product III = 3 hrs.
- **Production capacity:** 15,000 total hours per quarter (shared across all products).
- **Initial inventory:** 0 for all products at start of Q1.
- **End-of-Q4 inventory requirement:** Exactly 150 units of each product must be in stock at the end of Q4.
- **Delay compensation:** Product I = 20 yuan/unit/quarter of delay; Product II = 20 yuan/unit/quarter of delay; Product III = 10 yuan/unit/quarter of delay. A unit due in quarter *d* delivered in quarter *q* incurs penalty = rate × (q − d).
- **Inventory holding cost:** 5 yuan/unit/quarter for all units in inventory at the end of each quarter.
- **Production restriction:** Product I cannot be produced in Q2 (production = 0).

**Constraints:**
1. **Production capacity (per quarter):** 2×(Prod I) + 4×(Prod II) + 3×(Prod III) ≤ 15,000 hours, for each quarter.
2. **Inventory balance (per product, per quarter):** Inventory at end of quarter = Inventory at start of quarter + Production in quarter − Deliveries in quarter.
3. **Delivery timing:** Units can be delivered in the quarter they are due or later. A unit delivered in quarter *q* for demand due in quarter *d* (where q ≥ d) incurs delay penalty of rate × (q − d).
4. **End-of-Q4 inventory:** Inventory of each product at end of Q4 = 150 units.
5. **Product I in Q2:** Production of Product I in Q2 = 0.
6. **Non-negativity:** All production and inventory quantities ≥ 0.

**Assumptions (none required — all key facts confirmed by the user).**