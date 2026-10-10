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

QUESTION: When you say "total production hours used must not exceed 15,000 hours" per quarter, does this 15,000-hour limit apply to the sum of hours across all three products combined in that quarter, or is it a separate 15,000-hour limit for each product individually

## Turn 1 - User Simulator

It is a single 15,000-hour limit for the sum of hours across all three products combined in that quarter.

## Turn 2 - Generic Agent

QUESTION: Regarding the "contract reservations" in the table, are these quantities that must be delivered in that specific quarter (i.e., demand that must be met from production or inventory in that quarter), or are they minimum production targets that must be produced in that quarter regardless of when they are delivered

## Turn 2 - User Simulator

They are quantities that must be delivered in that specific quarter.

## Turn 3 - Generic Agent

QUESTION: Regarding the "delay compensation" cost, does this apply when the cumulative production of a product up to a given quarter is less than the cumulative contract reservations for that product up to that same quarter

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: Regarding the "inventory holding cost" of 5 yuan per unit per quarter, does this cost apply to any units of a product that are in inventory at the end of a quarter, regardless of whether those units were produced in the current quarter or carried over from previous quarters

## Turn 4 - User Simulator

Yes, the 5 yuan per unit per quarter cost applies to any units of a product that are in inventory at the end of a quarter, regardless of when they were produced.

## Turn 5 - Generic Agent

QUESTION: Regarding the "compensation cost" in your objective function, is this the same as the "delay compensation" cost you described (20 yuan per unit per quarter for products I and II, and 10 yuan per unit per quarter for product III), or is there a separate compensation cost component

## Turn 5 - User Simulator

It is the same as the delay compensation cost you described.

## Turn 6 - Generic Agent

QUESTION: Regarding the inventory balance, can inventory be negative in any quarter (meaning you can deliver more than you have produced and held in stock, effectively borrowing from future production), or must inventory always be non-negative

## Turn 6 - User Simulator

Inventory must always be non-negative.

## Turn 7 - Generic Agent

QUESTION: Regarding the production variables, must the number of units produced for each product in each quarter be a whole number (integer), or can they be fractional

## Turn 7 - User Simulator

The number of units produced for each product in each quarter must be a whole number.

## Turn 8 - Generic Agent

QUESTION: Regarding the final inventory requirement of 150 units for each product at the end of the fourth quarter, is this a strict equality constraint (inventory must be exactly 150 units) or a minimum constraint (inventory must be at least 150 units)

## Turn 8 - User Simulator

It is a strict equality constraint; the inventory must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 9 - Generic Agent

QUESTION: Regarding the delay compensation cost, is it calculated based on the cumulative shortfall (i.e., the difference between cumulative demand and cumulative production up to that quarter) for each quarter, or is it calculated based on the shortfall in that specific quarter only

## Turn 9 - User Simulator

It is calculated based on the cumulative shortfall for each quarter.

## Turn 10 - Generic Agent

QUESTION: Regarding the delay compensation cost, is it calculated as the cumulative shortfall at the end of each quarter multiplied by the per-unit rate, and then summed across all four quarters

## Turn 10 - User Simulator

Yes, that is correct.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, which is the sum of:
    *   **Delay Compensation Cost:** Calculated for each quarter $t$ (1 to 4) as the cumulative shortfall (Cumulative Demand up to $t$ - Cumulative Production up to $t$) multiplied by the per-unit rate. The rates are 20 yuan/unit for Products I and II, and 10 yuan/unit for Product III. This is summed across all four quarters.
    *   **Inventory Holding Cost:** Calculated for each quarter $t$ (1 to 4) as the ending inventory of each product at the end of quarter $t$ multiplied by 5 yuan/unit. This is summed across all products and all four quarters.

2.  **Decision Variables:**
    *   $P_{i,t}$: Number of units of product $i$ (I, II, III) produced in quarter $t$ (1, 2, 3, 4).
    *   Domain: Non-negative integers.

3.  **Parameters:**
    *   **Demand ($D_{i,t}$):** Contract reservations that must be delivered in quarter $t$.
        *   Product I: [1500, 1000, 2000, 1200]
        *   Product II: [1500, 1500, 1200, 1500]
        *   Product III: [1000, 2000, 1500, 2500]
    *   **Production Hours per Unit:**
        *   Product I: 2 hours
        *   Product II: 4 hours
        *   Product III: 3 hours
    *   **Initial Inventory:** 0 for all products at the start of Quarter 1.
    *   **Final Inventory:** Exactly 150 units for each product at the end of Quarter 4.

4.  **Constraints:**
    *   **Production Capacity:** For each quarter $t$, the total production hours used across all products must not exceed 15,000 hours.
        *   $2 \cdot P_{I,t} + 4 \cdot P_{II,t} + 3 \cdot P_{III,t} \le 15,000$ for $t=1,2,3,4$.
    *   **Inventory Balance:** For each product $i$ and quarter $t$:
        *   $I_{i,t} = I_{i,t-1} + P_{i,t} - D_{i,t}$
        *   Where $I_{i,0} = 0$ and $I_{i,4} = 150$.
    *   **Non-Negative Inventory:** $I_{i,t} \ge 0$ for all products $i$ and quarters $t=1,2,3,4$.
    *   **Integer Production:** $P_{i,t}$ must be integers.

5.  **Assumptions:**
    *   None. All formulation-critical facts were confirmed with the user.