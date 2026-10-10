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

QUESTION: For the production hours constraint, should the 15,000 hours be a separate limit applied to each individual quarter (so each of the four quarters has its own 15,000-hour cap), or is it a single total cap of 15,000 hours spread across the entire year

## Turn 1 - User Simulator

It is a separate limit applied to each individual quarter. Each of the four quarters has its own 15,000-hour cap.

## Turn 2 - Generic Agent

QUESTION: Regarding the "contract reservations" table, are these figures the minimum demand that must be delivered in each quarter (meaning you can produce and deliver more than this amount if it reduces total cost), or are they the exact quantity that must be delivered in each quarter

## Turn 2 - User Simulator

These figures are the minimum demand that must be delivered in each quarter. You can produce and deliver more than this amount if it reduces total cost.

## Turn 3 - Generic Agent

QUESTION: Regarding the delay compensation cost, is this cost incurred for any units of demand that are not delivered by the end of the quarter in which they were originally required (i.e., backorders), or is it a penalty applied to the difference between the contract reservation and the actual delivery whenever the actual delivery is less than the reservation

## Turn 3 - User Simulator

The delay compensation cost is incurred for any units of demand that are not delivered by the end of the quarter in which they were originally required. This is a backorder cost.

## Turn 4 - Generic Agent

QUESTION: Regarding the inventory holding cost, does this 5 yuan per unit per quarter apply to all units of inventory held at the end of a quarter (including both units produced early to meet future demand and any excess above the minimum contract reservation), or does it only apply to units that are produced but not delivered in the current quarter

## Turn 4 - User Simulator

The 5 yuan per unit per quarter applies to all units of inventory held at the end of a quarter.

## Turn 5 - Generic Agent

QUESTION: Regarding the final inventory requirement, does the 150 units per product at the end of the fourth quarter represent the total physical inventory on hand (which would include any units produced early to satisfy future demand), or is it a separate requirement that must be met in addition to any backorders

## Turn 5 - User Simulator

The 150 units per product at the end of the fourth quarter represents the total physical inventory on hand.

## Turn 6 - Generic Agent

QUESTION: Regarding the backorder cost, if a unit of demand from a specific quarter is not delivered by the end of that quarter, is the penalty calculated as a flat amount for the entire delay period (e.g., 20 yuan total for product I regardless of how many quarters it is late), or is it calculated per quarter of delay (e.g., 20 yuan for the first quarter late, plus another 20 yuan for the second quarter late

## Turn 6 - User Simulator

It is calculated per quarter of delay. For example, for product I, it is 20 yuan for the first quarter late, plus another 20 yuan for the second quarter late, and so on.

## Turn 7 - Generic Agent

QUESTION: Regarding the production hours constraint, are the 15,000 hours per quarter a hard limit that cannot be exceeded under any circumstances, or is it a soft constraint that can be violated if the cost of doing so is less than the benefit

## Turn 7 - User Simulator

The 15,000 hours per quarter is a hard limit that cannot be exceeded under any circumstances.

## Turn 8 - Generic Agent

QUESTION: Regarding the production quantities, are the units of products I, II, and III required to be whole numbers (integers), or can they be fractional

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Regarding the production quantities, are the units of products I, II, and III required to be whole numbers (integers), or can they be fractional

## Turn 9 - User Simulator

The units of products I, II, and III are required to be whole numbers (integers).

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs (backorder penalties) and inventory holding costs.
2.  **Time Horizon:** 4 quarters.
3.  **Products:** I, II, and III.
4.  **Decision Variables:**
    *   Production quantity for each product in each quarter (must be non-negative integers).
    *   Inventory on hand for each product at the end of each quarter (must be non-negative integers).
    *   Backorder quantity for each product at the end of each quarter (must be non-negative integers).
5.  **Demand (Contract Reservations):**
    *   These are minimum delivery requirements.
    *   Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200.
    *   Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500.
    *   Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500.
    *   Deliveries can exceed these minimums if beneficial.
6.  **Constraints:**
    *   **Production Capacity:** Total production hours in each quarter must not exceed 15,000 hours.
        *   Product I: 2 hours/unit.
        *   Product II: 4 hours/unit.
        *   Product III: 3 hours/unit.
    *   **Initial Inventory:** 0 units for all products at the start of Q1.
    *   **Final Inventory:** Exactly 150 units of each product must be in physical inventory at the end of Q4.
    *   **Inventory Balance:** For each product and quarter, `Beginning Inventory + Production - Delivery = Ending Inventory`.
    *   **Backorder Logic:** If delivery is less than the minimum demand for a quarter, the difference is a backorder. Backorders persist until fulfilled.
7.  **Costs:**
    *   **Inventory Holding Cost:** 5 yuan per unit per quarter for all units in physical inventory at the end of each quarter.
    *   **Delay Compensation (Backorder) Cost:**
        *   Product I: 20 yuan per unit per quarter of delay.
        *   Product II: 20 yuan per unit per quarter of delay.
        *   Product III: 10 yuan per unit per quarter of delay.
        *   Cost accumulates for each quarter a unit remains in backorder.

**Assumptions:**
*   None. All structural and parametric facts were confirmed by the user.