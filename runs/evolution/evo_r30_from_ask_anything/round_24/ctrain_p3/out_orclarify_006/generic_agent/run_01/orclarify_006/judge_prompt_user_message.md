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

QUESTION: Is the 150-unit end-of-quarter-four inventory requirement a hard constraint that must be met exactly, or is it a target that can be exceeded if doing so reduces total cost

## Turn 1 - User Simulator

It is a hard constraint. The inventory of each product must be exactly 150 units at the end of the fourth quarter.

## Turn 2 - Generic Agent

QUESTION: Does the 15,000 production hours per quarter limit apply to the sum of hours used for all three products combined in that

## Turn 2 - User Simulator

Yes, the 15,000 production hours per quarter limit applies to the total production hours used for all three products combined in that quarter.

## Turn 3 - Generic Agent

QUESTION: Are the contract reservation figures in Table 1-10 minimum delivery requirements that must be met each quarter, or are they exact delivery targets

## Turn 3 - User Simulator

They are minimum delivery requirements. All contract reservations must be delivered, but late delivery is allowed with the applicable compensation cost.

## Turn 4 - Generic Agent

QUESTION: When a product is delivered late, does the delay compensation cost accumulate for each quarter the unit remains undelivered

## Turn 4 - User Simulator

Yes, the delay compensation cost accumulates for each quarter the unit remains undelivered.

## Turn 5 - Generic Agent

QUESTION: Can production in a given quarter be used to satisfy contract reservations from

## Turn 5 - User Simulator

Yes, production in a given quarter can be used to satisfy contract reservations from previous quarters, with the applicable delay compensation cost incurred for each quarter of delay.

## Turn 6 - Generic Agent

QUESTION: Is the inventory holding cost of 5 yuan per unit per

## Turn 6 - User Simulator

Yes, the inventory holding cost is 5 yuan per unit per quarter for products produced but not delivered in the current quarter.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on the amount of inventory that

## Turn 7 - User Simulator

No, there is no upper limit on the amount of inventory that can be held.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or

## Turn 8 - User Simulator

Yes, product I cannot be produced in the second quarter due to an equipment change.

## Turn 9 - Generic Agent

QUESTION: Is the production of product I in the second

## Turn 9 - User Simulator

No, product I cannot be produced in the second quarter.

## Turn 10 - Generic Agent

QUESTION: Are there any other

## Turn 10 - User Simulator

No, there are no other constraints beyond those already mentioned.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs.
2.  **Time Horizon:** 4 quarters (Q1, Q2, Q3, Q4).
3.  **Products:** I, II, III.
4.  **Decision Variables:**
    *   $P_{i,t}$: Units of product $i$ produced in quarter $t$.
    *   $I_{i,t}$: Inventory of product $i$ at the end of quarter $t$.
    *   $D_{i,t}$: Units of product $i$ delivered in quarter $t$ (to satisfy contract reservations).
    *   *Note: The model will likely track inventory and production to implicitly determine delivery timing and associated delay costs.*
5.  **Parameters:**
    *   **Contract Reservations (Minimum Demand):**
        *   Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200.
        *   Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500.
        *   Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500.
    *   **Production Hours per Unit:**
        *   Product I: 2 hours/unit.
        *   Product II: 4 hours/unit.
        *   Product III: 3 hours/unit.
    *   **Production Capacity:** 15,000 hours per quarter (total for all products).
    *   **Delay Compensation (Backorder Cost):**
        *   Product I: 20 yuan/unit/quarter.
        *   Product II: 20 yuan/unit/quarter.
        *   Product III: 10 yuan/unit/quarter.
        *   *Accumulates for each quarter of delay.*
    *   **Inventory Holding Cost:** 5 yuan/unit/quarter for all products.
6.  **Constraints:**
    *   **Initial Inventory:** $I_{i,0} = 0$ for all products $i$.
    *   **Final Inventory:** $I_{i,4} = 150$ for all products $i$ (Hard constraint, exact).
    *   **Production Capacity:** $\sum_{i} (\text{Hours}_i \times P_{i,t}) \le 15,000$ for each quarter $t$.
    *   **Production Restriction:** $P_{I,2} = 0$ (Product I cannot be produced in Q2).
    *   **Flow Balance:** Inventory and delivery must satisfy demand. Specifically, production plus beginning inventory must cover deliveries plus ending inventory.
    *   **Demand Satisfaction:** Total deliveries over the 4 quarters for each product must meet or exceed the sum of contract reservations for that product. (Since late delivery is allowed with cost, the model will decide *when* to deliver to minimize cost, but all reserved units must eventually be delivered).
    *   **Non-negativity:** $P_{i,t} \ge 0$, $I_{i,t} \ge 0$, $D_{i,t} \ge 0$.

**Assumptions:**
*   Production and delivery occur within the same quarter.
*   The "delay compensation" is incurred for each quarter a unit is held in backorder (i.e., if a unit due in Q1 is delivered in Q3, it incurs 2 quarters of delay cost).
*   The inventory holding cost applies to units produced but not yet delivered (i.e., units in inventory at the end of the quarter).
*   There are no setup costs or fixed costs for production.
*   The 150-unit final inventory is in addition to the contract reservations, meaning total production for each product over the year must equal (Total Reservations + 150).