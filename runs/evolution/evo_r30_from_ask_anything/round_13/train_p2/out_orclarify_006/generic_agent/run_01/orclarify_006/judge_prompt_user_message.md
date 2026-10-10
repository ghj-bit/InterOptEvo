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

QUESTION: Regarding the "contract reservations" in the table, are these quantities that must be delivered to customers in that specific quarter (i.e., demand that must be met from production or inventory in that quarter), or are they just forecasted sales that can be fulfilled from inventory accumulated in previous quarters

## Turn 2 - User Simulator

They are quantities that must be delivered to customers in that specific quarter.

## Turn 3 - Generic Agent

QUESTION: Regarding the "delay compensation" cost, if a product's demand for a specific quarter is not fully met by the end of that quarter, is the penalty calculated based on the number of units short multiplied by the delay rate for each quarter the units remain undelivered

## Turn 3 - User Simulator

Yes, the penalty is calculated based on the number of units short multiplied by the delay rate for each quarter the units remain undelivered.

## Turn 4 - Generic Agent

QUESTION: Regarding the inventory holding cost of 5 yuan per unit per quarter, does this cost apply to all units held in inventory at the end of each quarter (including units produced in previous quarters), or only to units that were produced in the current quarter but not delivered

## Turn 4 - User Simulator

It applies to all units held in inventory at the end of each quarter, including units produced in previous quarters.

## Turn 5 - Generic Agent

QUESTION: Regarding the requirement that inventory of each product must be 150 units at the end of the fourth quarter, is this an exact equality constraint (inventory must be exactly 150), or is it a minimum requirement (inventory must be at least 150

## Turn 5 - User Simulator

It is an exact equality constraint; the inventory must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 6 - Generic Agent

QUESTION: Are there any upper limits on the production quantity for each product in each quarter

## Turn 6 - User Simulator

No, there are no upper limits on the production quantity for each product in each quarter.

## Turn 7 - Generic Agent

QUESTION: Are the production quantities for each product in each quarter required to be integer values

## Turn 7 - User Simulator

Yes, the production quantities for each product in each quarter must be integer values.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned

## Turn 8 - User Simulator

Yes, product I cannot be produced in the second quarter due to an equipment change.

## Turn 9 - Generic Agent

QUESTION: Is the restriction that product I cannot be produced in the second quarter a hard constraint (production of product I in Q2 must be exactly zero

## Turn 9 - User Simulator

Yes, it is a hard constraint; production of product I in the second quarter must be exactly zero.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, which is the sum of:
    *   **Delay Compensation Cost:**
        *   Product I: 20 yuan/unit/quarter for each unit of demand not met by the end of the quarter.
        *   Product II: 20 yuan/unit/quarter for each unit of demand not met by the end of the quarter.
        *   Product III: 10 yuan/unit/quarter for each unit of demand not met by the end of the quarter.
    *   **Inventory Holding Cost:** 5 yuan/unit/quarter for all units held in inventory at the end of each quarter (for all products).

2.  **Time Horizon:** 4 Quarters (Q1, Q2, Q3, Q4).

3.  **Decision Variables:**
    *   $P_{i,t}$: Integer production quantity of product $i$ in quarter $t$.
    *   $I_{i,t}$: Integer inventory level of product $i$ at the end of quarter $t$.
    *   $D_{i,t}$: Integer units of demand for product $i$ in quarter $t$ that are delayed (unmet) beyond quarter $t$.

4.  **Parameters:**
    *   **Demand (Contract Reservations):**
        *   Product I: [1500, 1000, 2000, 1200]
        *   Product II: [1500, 1500, 1200, 1500]
        *   Product III: [1000, 2000, 1500, 2500]
    *   **Production Hours per Unit:**
        *   Product I: 2 hours
        *   Product II: 4 hours
        *   Product III: 3 hours
    *   **Initial Inventory:** 0 for all products at the start of Q1.
    *   **Final Inventory Constraint:** Exactly 150 units for each product at the end of Q4.

5.  **Constraints:**
    *   **Production Capacity:** For each quarter $t$, $\sum_{i} (\text{Hours}_i \times P_{i,t}) \le 15,000$.
    *   **Inventory Balance:** For each product $i$ and quarter $t$:
        $I_{i,t-1} + P_{i,t} - D_{i,t}^{\text{met}} = I_{i,t}$
        Where $D_{i,t}^{\text{met}}$ is the amount of demand met in quarter $t$.
        Alternatively, using backlogging variables:
        $I_{i,t} = I_{i,t-1} + P_{i,t} - \text{Demand}_{i,t} + \text{Backlog}_{i,t} - \text{Backlog}_{i,t-1}$
        (Note: The specific formulation of backlog vs. unmet demand needs to align with the "delay compensation" definition. The delay cost is incurred on the *cumulative* unmet demand or the *flow* of unmet demand? The user stated: "penalty is calculated based on the number of units short multiplied by the delay rate for each quarter the units remain undelivered." This implies if 10 units are short in Q1, and still short in Q2, the cost is $10 \times \text{rate} \times 1$ for Q1 and $10 \times \text{rate} \times 1$ for Q2? Or is it $10 \times \text{rate} \times 2$ total? The phrase "for each quarter the units remain undelivered" suggests a per-quarter charge on the outstanding backlog. So if 10 units are backlogged at end of Q1, cost is $10 \times \text{rate}$. If they are still backlogged at end of Q2, cost is another $10 \times \text{rate}$. This is equivalent to charging the backlog level at the end of each quarter.)
    *   **Specific Production Restriction:** $P_{I,2} = 0$.
    *   **Final Inventory:** $I_{i,4} = 150$ for $i \in \{I, II, III\}$.
    *   **Non-negativity:** $P_{i,t} \ge 0$, $I_{i,t} \ge 0$, Backlog variables $\ge 0$.
    *   **Integrality:** All decision variables are integers.

**Assumptions:**
*   The "delay compensation" is charged on the level of backlog (unmet demand) at the end of each quarter. That is, if there are $B_{i,t}$ units of product $i$ still undelivered from previous quarters at the end of quarter $t$, the cost is $B_{i,t} \times \text{Rate}_i$.
*   Demand can be met from current production or previous inventory.
*   Backlogged units can be delivered in future quarters using future production or inventory.