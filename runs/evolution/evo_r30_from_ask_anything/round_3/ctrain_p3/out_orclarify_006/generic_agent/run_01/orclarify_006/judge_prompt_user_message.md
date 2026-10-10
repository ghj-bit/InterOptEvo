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

QUESTION: For the production hours limit of 15,000 hours per quarter, is this a hard constraint that must not be exceeded in any quarter, or is it a target that can be exceeded if a penalty is paid?

## Turn 1 - User Simulator

It is a hard constraint. The 15,000 production hours per quarter must not be exceeded in any quarter.

## Turn 2 - Generic Agent

QUESTION: Regarding the "contract reservations" in the table, are these the minimum quantities that must be delivered to customers in each quarter (meaning any shortfall incurs the delay compensation), or are they the total quantities that must be produced in each quarter regardless of delivery timing?

## Turn 2 - User Simulator

They are the minimum quantities that must be delivered to customers in each quarter. Any shortfall incurs the delay compensation.

## Turn 3 - Generic Agent

QUESTION: Regarding the delay compensation, if a unit is delivered late, is the penalty calculated based on the number of quarters it is late (e.g., a unit due in Q1 but delivered in Q3 incurs 2 quarters of penalty), or is it a flat penalty per unit regardless of how late it is?

## Turn 3 - User Simulator

The penalty is calculated based on the number of quarters it is late. For example, a unit due in Q1 but delivered in Q3 incurs 2 quarters of penalty.

## Turn 4 - Generic Agent

QUESTION: Regarding the inventory holding cost, does the 5 yuan per unit per quarter apply to all units held in inventory at the end of a quarter, or only to units that were produced in that specific quarter and not delivered?

## Turn 4 - User Simulator

It applies to all units held in inventory at the end of a quarter, regardless of when they were produced.

## Turn 5 - Generic Agent

QUESTION: Regarding the final inventory requirement of 150 units per product at the end of the fourth quarter, is this a hard constraint that must be met exactly, or is it a minimum target where having more than 150 units is allowed but incurs holding costs?

## Turn 5 - User Simulator

It is a hard constraint that must be met exactly.

## Turn 6 - Generic Agent

QUESTION: Regarding the production quantities, are they required to be whole numbers (integer units), or can they be fractional?

## Turn 6 - User Simulator

They are required to be whole numbers (integer units).

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs over the four quarters.
2.  **Time Horizon:** 4 quarters (Q1, Q2, Q3, Q4).
3.  **Products:** I, II, and III.
4.  **Decision Variables:**
    *   $P_{p,t}$: Integer production quantity of product $p$ in quarter $t$.
    *   $I_{p,t}$: Integer inventory level of product $p$ at the end of quarter $t$.
    *   $D_{p,t}$: Integer delivery quantity of product $p$ in quarter $t$.
    *   $L_{p,t}$: Integer quantity of product $p$ delivered late in quarter $t$ (specifically, units due in earlier quarters but delivered in $t$).
5.  **Parameters:**
    *   **Demand (Contract Reservations):**
        *   Product I: [1500, 1000, 2000, 1200]
        *   Product II: [1500, 1500, 1200, 1500]
        *   Product III: [1000, 2000, 1500, 2500]
    *   **Production Hours per Unit:**
        *   Product I: 2 hours
        *   Product II: 4 hours
        *   Product III: 3 hours
    *   **Capacity:** 15,000 hours per quarter (Hard Constraint).
    *   **Initial Inventory:** 0 for all products at the start of Q1.
    *   **Final Inventory:** Exactly 150 units for each product at the end of Q4 (Hard Constraint).
    *   **Delay Compensation Rates (per unit per quarter late):**
        *   Product I: 20 yuan
        *   Product II: 20 yuan
        *   Product III: 10 yuan
    *   **Inventory Holding Cost:** 5 yuan per unit per quarter (applied to all units in inventory at the end of each quarter).

6.  **Constraints:**
    *   **Capacity:** For each quarter $t$, $\sum_{p} (\text{Hours}_p \times P_{p,t}) \le 15,000$.
    *   **Inventory Balance:** For each product $p$ and quarter $t$:
        $I_{p,t} = I_{p,t-1} + P_{p,t} - D_{p,t}$
        (Where $I_{p,0} = 0$).
    *   **Final Inventory:** $I_{p,4} = 150$ for all $p \in \{I, II, III\}$.
    *   **Delivery Logic:**
        *   Deliveries $D_{p,t}$ satisfy demand.
        *   If $D_{p,t} < \text{Demand}_{p,t}$, the shortfall is carried over as late demand.
        *   Late units incur penalties based on how many quarters late they are. Specifically, if a unit due in quarter $k$ is delivered in quarter $t > k$, it incurs a penalty of $(t-k) \times \text{Rate}_p$.
        *   Total delivered over the horizon must equal Total Demand + Final Inventory (since final inventory is fixed, total production must cover total demand + 150 per product).
    *   **Integrality:** All decision variables ($P, I, D, L$) must be non-negative integers.

7.  **Cost Calculation:**
    *   **Holding Cost:** $\sum_{t=1}^{4} \sum_{p} 5 \times I_{p,t}$.
    *   **Delay Cost:** $\sum_{t=1}^{4} \sum_{p} \sum_{k=1}^{t-1} (\text{Rate}_p \times (t-k) \times \text{Units of } p \text{ due in } k \text{ delivered in } t)$.
    *   *Note:* The model must track which specific units are late to calculate the exact penalty based on the number of quarters late. This can be modeled by tracking backlogs or using specific variables for late deliveries from each prior quarter.