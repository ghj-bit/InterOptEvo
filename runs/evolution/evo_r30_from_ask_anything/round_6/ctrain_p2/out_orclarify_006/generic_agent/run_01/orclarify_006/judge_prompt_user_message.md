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

QUESTION: When you say "total production hours used must not exceed 15,000 hours" per quarter, does this limit apply to the sum of hours across all three products combined, or is it a separate 15,000-hour limit for each individual product

## Turn 1 - User Simulator

It is a single 15,000-hour limit for the sum of hours across all three products combined in each quarter.

## Turn 2 - Generic Agent

QUESTION: Regarding the "contract reservations" in the table, are these quantities that must be delivered to customers in that specific quarter (meaning any shortfall results in the stated delay compensation), or are they minimum production targets that must be met

## Turn 2 - User Simulator

They are quantities that must be delivered to customers in that specific quarter. Any shortfall results in the stated delay compensation.

## Turn 3 - Generic Agent

QUESTION: Regarding the delay compensation, if a unit is produced in a later quarter than the one it was reserved for, is the penalty calculated as the stated rate multiplied by the number of quarters late (e.g., a product I unit reserved for Q1 but delivered in Q3 incurs 2 * 20 yuan), or is it a flat penalty of the stated rate regardless of how many quarters late

## Turn 3 - User Simulator

The penalty is calculated as the stated rate multiplied by the number of quarters late.

## Turn 4 - Generic Agent

QUESTION: Regarding the "compensation cost" in your objective function, does this term refer only to the delay compensation for late deliveries, or does it also include other labor or wage

## Turn 4 - User Simulator

It refers only to the delay compensation for late deliveries.

## Turn 5 - Generic Agent

QUESTION: Regarding the inventory holding cost, is it incurred on the ending inventory of each quarter (i.e., units left over after meeting that quarter's delivery

## Turn 5 - User Simulator

Yes, it is incurred on the ending inventory of each quarter.

## Turn 6 - Generic Agent

QUESTION: Regarding the production schedule, are the production quantities for each product in each quarter required to be whole

## Turn 6 - User Simulator

Yes, production quantities must be whole units.

## Turn 7 - Generic Agent

QUESTION: Regarding the inventory balance, can inventory be carried over from one quarter to the next to help meet future

## Turn 7 - User Simulator

Yes, inventory can be carried over from one quarter to the next to help meet future deliveries.

## Turn 8 - Generic Agent

QUESTION: Regarding the final inventory requirement of 150 units per product at the end of Q4, does this 150 units need to be in addition to any units produced in Q4 to meet the Q4

## Turn 8 - User Simulator

Yes, the 150 units must be in addition to any units produced in Q4 to meet the Q4 contract reservations.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs over the four quarters.
2.  **Decision Variables:** Integer production quantities for each of the three products (I, II, III) in each of the four quarters.
3.  **Time Horizon:** Four quarters (Q1 to Q4).
4.  **Initial State:** Inventory for all products is 0 at the start of Q1.
5.  **Demand/Reservations:**
    *   Product I: 1500 (Q1), 1000 (Q2), 2000 (Q3), 1200 (Q4)
    *   Product II: 1500 (Q1), 1500 (Q2), 1200 (Q3), 1500 (Q4)
    *   Product III: 1000 (Q1), 2000 (Q2), 1500 (Q3), 2500 (Q4)
    *   These are delivery targets. Shortfalls incur delay compensation.
6.  **Production Capacity:** Total production hours across all products in any quarter must not exceed 15,000 hours.
    *   Product I: 2 hours/unit
    *   Product II: 4 hours/unit
    *   Product III: 3 hours/unit
7.  **Costs:**
    *   **Delay Compensation:** Charged if delivery is late. Rate = (Base Rate) × (Number of Quarters Late).
        *   Product I: 20 yuan/unit/quarter
        *   Product II: 20 yuan/unit/quarter
        *   Product III: 10 yuan/unit/quarter
    *   **Inventory Holding:** 5 yuan/unit/quarter, charged on the ending inventory of each quarter for all products.
8.  **Inventory Dynamics:**
    *   Inventory can be carried over between quarters.
    *   Ending Inventory(t) = Beginning Inventory(t) + Production(t) - Delivered(t).
    *   Delivered(t) is the amount of the current quarter's reservation that is actually met from available stock (current production + beginning inventory).
    *   Unmet demand from previous quarters can be fulfilled in later quarters, incurring delay penalties based on how many quarters late.
9.  **Terminal Constraint:** At the end of Q4, the ending inventory for each product must be exactly 150 units. This is in addition to meeting the Q4 contract reservations.
10. **Integrality:** All production quantities must be non-negative integers.