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

QUESTION: Is the 15,000 production hours per quarter a hard upper limit that must not be exceeded, or is it a target that can be exceeded if additional cost is incurred?

## Turn 1 - User Simulator

It is a hard upper limit. Total production hours used in each quarter must not exceed 15,000 hours.

## Turn 2 - Generic Agent

QUESTION: Are the contract reservation quantities in the table minimum delivery requirements that must be met each quarter, or are they exact targets where any deviation (over or under) incurs a penalty?

## Turn 2 - User Simulator

The contract reservation quantities are minimum delivery requirements. All contract reservations must be delivered, but late delivery is allowed with the applicable compensation cost.

## Turn 3 - Generic Agent

QUESTION: When a product is delivered late, does the delay compensation cost apply for each quarter the unit remains undelivered until it is finally delivered, or is it a one-time penalty charged only once per unit regardless of how many quarters it is late?

## Turn 3 - User Simulator

The delay compensation cost applies for each quarter the unit remains undelivered until it is finally delivered.

## Turn 4 - Generic Agent

QUESTION: Is the 150-unit inventory requirement for each product at the end of the fourth quarter a hard constraint that must be exactly met, or is it a minimum target that can be exceeded?

## Turn 4 - User Simulator

It is a hard constraint that must be exactly met.

## Turn 5 - Generic Agent

QUESTION: Is the inventory holding cost of 5 yuan per unit per quarter applied to all units of inventory held at the end of each quarter, or only to units that were produced in that specific quarter but not delivered?

## Turn 5 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter is applied to all units of inventory held at the end of each quarter.

## Turn 6 - Generic Agent

QUESTION: Are there any additional constraints or requirements not mentioned in the brief, such as limits on the number of units that can be produced per quarter per product, minimum production quantities, or restrictions on when production can occur?

## Turn 6 - User Simulator

Yes, there is one additional constraint: Product I cannot be produced in the second quarter due to an equipment change.

## Turn 7 - Generic Agent

QUESTION: Is the production of Product I in the second quarter completely prohibited (zero units), or is there a reduced capacity limit for that quarter?

## Turn 7 - User Simulator

Production of Product I in the second quarter is completely prohibited (zero units).

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as limits on production quantities per quarter for products II and III, or restrictions on inventory levels during the year?

## Turn 8 - User Simulator

No, there are no other constraints or requirements beyond what has already been discussed.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs over the four quarters.
2.  **Time Horizon:** 4 quarters (Q1, Q2, Q3, Q4).
3.  **Products:** I, II, III.
4.  **Decision Variables:**
    *   $P_{i,t}$: Units of product $i$ produced in quarter $t$.
    *   $I_{i,t}$: Inventory of product $i$ at the end of quarter $t$.
    *   $L_{i,t}$: Units of product $i$ delivered late in quarter $t$ (or equivalently, the backlog carried over).
    *   *Note: The specific algebraic formulation of "delay" vs "inventory" will depend on how we track unmet demand. Typically, this is modeled with a backlog variable $B_{i,t}$ representing units of demand from previous quarters that are still unmet at the end of quarter $t$.*
5.  **Demand (Contract Reservations):**
    *   Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200.
    *   Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500.
    *   Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500.
    *   These are minimum delivery requirements.
6.  **Production Capacity:**
    *   Total production hours per quarter $\le$ 15,000.
    *   Hours per unit: Product I = 2, Product II = 4, Product III = 3.
    *   Constraint: $2P_{I,t} + 4P_{II,t} + 3P_{III,t} \le 15,000$ for all $t$.
7.  **Specific Production Restriction:**
    *   $P_{I,2} = 0$ (Product I cannot be produced in Q2).
8.  **Inventory Dynamics:**
    *   Initial Inventory: $I_{i,0} = 0$ for all $i$.
    *   Flow Balance: $I_{i,t} = I_{i,t-1} + P_{i,t} - D_{i,t}^{delivered}$.
    *   *Clarification on Delay/Backlog:* Since late delivery is allowed with a penalty, we must track unmet demand. Let $B_{i,t}$ be the backlog (unmet demand from prior quarters) at the end of quarter $t$.
    *   The standard formulation for this type of problem usually involves:
        *   $I_{i,t} \ge 0$ (Inventory cannot be negative).
        *   $B_{i,t} \ge 0$ (Backlog cannot be negative).
        *   $I_{i,t} \cdot B_{i,t} = 0$ (Cannot have both inventory and backlog for the same product at the same time).
        *   Balance: $I_{i,t} = I_{i,t-1} + P_{i,t} - D_{i,t} + B_{i,t-1} - B_{i,t}$.
        *   Alternatively, a simpler net inventory approach: $S_{i,t} = S_{i,t-1} + P_{i,t} - D_{i,t}$. If $S_{i,t} < 0$, it represents backlog.
9.  **Costs:**
    *   **Inventory Holding Cost:** 5 yuan per unit per quarter for all units in inventory ($I_{i,t} > 0$) at the end of each quarter.
    *   **Delay Compensation Cost:**
        *   Product I: 20 yuan per unit per quarter of delay.
        *   Product II: 20 yuan per unit per quarter of delay.
        *   Product III: 10 yuan per unit per quarter of delay.
        *   This cost is incurred for each unit in the backlog ($B_{i,t} > 0$) at the end of each quarter.
10. **Final Inventory Constraint:**
    *   $I_{I,4} = 150$
    *   $I_{II,4} = 150$
    *   $I_{III,4} = 150$
    *   *Assumption:* This implies that all demand must be fully met by the end of Q4, and the final state is exactly 150 units of inventory for each product. This means the backlog $B_{i,4}$ must be 0.

**Assumptions:**
1.  Production and delivery occur within the quarter. The "end of quarter" inventory is the state after all production and deliveries for that quarter are complete.
2.  The "delay compensation" is charged on the backlog units at the end of each quarter. If a unit is produced in Q3 to meet Q1 demand, it incurs delay costs for Q1 and Q2 (assuming it was in backlog at end of Q1 and end of Q2).
3.  The final inventory constraint of 150 units is a hard equality constraint.
4.  There are no other costs (e.g., fixed production costs, overtime costs) included in the objective function.