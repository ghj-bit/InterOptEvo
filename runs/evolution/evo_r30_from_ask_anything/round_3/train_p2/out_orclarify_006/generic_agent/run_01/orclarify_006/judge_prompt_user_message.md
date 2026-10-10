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

QUESTION: Are the contract reservation numbers in the table the minimum units that must be delivered to customers in each quarter, or are they the exact units that must be delivered (meaning any production beyond that number in a quarter would be excess that must be held in inventory)?

## Turn 1 - User Simulator

The contract reservation numbers in the table are the exact units that must be delivered to customers in each quarter. Any production beyond that number in a given quarter is excess that must be held in inventory.

## Turn 2 - Generic Agent

QUESTION: When you mention "delay compensation" for products I, II, and III, does this cost apply to units that are produced but not delivered in the quarter they were produced (i.e., held in inventory), or does it apply to units that are not produced at all and must be backordered to a later quarter?

## Turn 2 - User Simulator

The delay compensation applies to units that are not produced at all and must be backordered to a later quarter.

## Turn 3 - Generic Agent

QUESTION: Since the contract reservations are exact delivery requirements, are you allowed to backorder units (i.e., deliver them in a later quarter than the quarter they are due) and pay the delay compensation, or must every quarter's contract be fully satisfied from production in that same quarter or from inventory carried forward from previous quarters?

## Turn 3 - User Simulator

Yes, you are allowed to backorder units and pay the delay compensation.

## Turn 4 - Generic Agent

QUESTION: When a unit is backordered from one quarter to the next, does it incur the delay compensation cost for each quarter it remains undelivered (e.g., a unit backordered from Q1 to Q3 pays delay compensation for both Q1 and Q2), or is the delay compensation charged only once for the total delay period?

## Turn 4 - User Simulator

The delay compensation is charged for each quarter the unit remains undelivered.

## Turn 5 - Generic Agent

QUESTION: Does the inventory holding cost of 5 yuan per unit per quarter apply to all products (I, II, and III) that are produced but not delivered in the current quarter, or does it apply only to specific products?

## Turn 5 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter applies to all products (I, II, and III) that are produced but not delivered in the current quarter.

## Turn 6 - Generic Agent

QUESTION: Can a single unit of a product be both backordered (incurring delay compensation) and held in inventory (incurring holding cost) in the same quarter, or are these two states mutually exclusive for any given unit in any given quarter?

## Turn 6 - User Simulator

These two states are mutually exclusive for any given unit in any given quarter.

## Turn 7 - Generic Agent

QUESTION: Is the 15,000 production hours per quarter limit a hard constraint that must not be exceeded, or is it a target that can be exceeded if additional costs are incurred?

## Turn 7 - User Simulator

The 15,000 production hours per quarter limit is a hard constraint that must not be exceeded.

## Turn 8 - Generic Agent

QUESTION: Are the production quantities for each product in each quarter required to be whole numbers (integer units), or can they be fractional values?

## Turn 8 - User Simulator

The production quantities for each product in each quarter are required to be whole numbers (integer units).

## Turn 9 - Generic Agent

QUESTION: Can production quantities be zero in any quarter for any product, or is there a minimum production requirement for each product in each quarter?

## Turn 9 - User Simulator

Production quantities can be zero in any quarter for any product.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum inventory level (capacity limit) for any product at the end of any quarter, or can inventory grow without bound as long as the holding cost is paid?

## Turn 10 - User Simulator

There is no maximum inventory level (capacity limit) for any product at the end of any quarter.

## Turn 11 - Generic Agent

QUESTION: Can the backorder quantity (units not yet delivered) for any product at the end of any quarter be negative, or must it be zero or positive?

## Turn 11 - User Simulator

The backorder quantity for any product at the end of any quarter must be zero or positive.

## Turn 12 - Generic Agent

QUESTION: Is there a maximum backorder level (capacity limit) for any product at the end of any quarter, or can backorders grow without bound as long as the delay compensation is paid?

## Turn 12 - User Simulator

There is no maximum backorder level (capacity limit) for any product at the end of any quarter.

## Turn 13 - Generic Agent

QUESTION: At the end of the fourth quarter, must the backorder quantity for each product be zero (i.e., all contract units must be fully delivered by the end of Q4), or is it acceptable to have outstanding backorders at the end of the year?

## Turn 13 - User Simulator

At the end of the fourth quarter, the backorder quantity for each product must be zero.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs over the four quarters.
2.  **Time Horizon:** 4 quarters (Q1, Q2, Q3, Q4).
3.  **Products:** I, II, III.
4.  **Decision Variables:**
    *   Production quantity for each product in each quarter (integer, non-negative).
    *   Inventory level for each product at the end of each quarter (integer, non-negative).
    *   Backorder level for each product at the end of each quarter (integer, non-negative).
5.  **Demand/Delivery Requirements:**
    *   Contract reservations are exact delivery requirements per quarter per product (Table 1-10).
    *   Backordering is allowed; units can be delivered in later quarters.
    *   At the end of Q4, backorders for all products must be zero.
6.  **Inventory Constraints:**
    *   Initial inventory (start of Q1) is 0 for all products.
    *   Ending inventory (end of Q4) must be exactly 150 units for each product.
    *   No maximum inventory capacity limits.
    *   Inventory and backorder states are mutually exclusive for any unit in any quarter (a unit cannot be both in inventory and backordered).
7.  **Production Constraints:**
    *   Total production hours per quarter must not exceed 15,000 hours (hard constraint).
    *   Processing times: Product I = 2 hours/unit, Product II = 4 hours/unit, Product III = 3 hours/unit.
    *   Production quantities can be zero.
8.  **Costs:**
    *   **Delay Compensation:** Charged per unit per quarter for units that are backordered (not produced/delivered when due).
        *   Product I: 20 yuan/unit/quarter.
        *   Product II: 20 yuan/unit/quarter.
        *   Product III: 10 yuan/unit/quarter.
    *   **Inventory Holding Cost:** Charged per unit per quarter for units produced but not delivered in the current quarter (held in inventory).
        *   All products: 5 yuan/unit/quarter.
9.  **Integrality:** All production, inventory, and backorder quantities must be integers.