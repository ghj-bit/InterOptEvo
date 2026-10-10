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

QUESTION: When you say "total production hours used must not exceed 15,000 hours" per quarter, does this 15,000-hour limit apply to the sum of hours across all three products combined in each quarter, or is it a separate 15,000-hour limit for each product individually?

## Turn 1 - User Simulator

It is a single 15,000-hour limit for the sum of hours across all three products combined in each quarter.

## Turn 2 - Generic Agent

QUESTION: Regarding the "contract reservations" in the table, are these quantities that must be delivered exactly in that quarter (i.e., they represent demand that must be met from production or inventory in that specific quarter), or are they minimum commitments that can be delivered early or late as long as the total over the year is met?

## Turn 2 - User Simulator

They are demand that must be met from production or inventory in that specific quarter. Late delivery is allowed, but it incurs the compensation cost you mentioned.

## Turn 3 - Generic Agent

QUESTION: Regarding the "150 units in stock for each product by the end of the fourth quarter" requirement, is this a strict equality constraint (inventory must be exactly 150 units) or a minimum constraint (inventory must be at least 150 units)?

## Turn 3 - User Simulator

It is a strict equality constraint: the inventory of each product must be exactly 150 units at the end of the fourth quarter.

## Turn 4 - Generic Agent

QUESTION: Regarding the production variables, is the number of units produced for each product in each quarter required to be an integer, or can it be a continuous (fractional) value?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Regarding the delay compensation cost, is the "per quarter delay" calculated based on the number of quarters the unit is late (e.g., if a unit demanded in Q1 is delivered in Q3, it incurs 2 quarters of delay cost), or is it a flat penalty applied once for any late delivery regardless of how late it is?

## Turn 5 - User Simulator

It is calculated based on the number of quarters the unit is late. For example, if a unit demanded in Q1 is delivered in Q3, it incurs 2 quarters of delay cost.

## Turn 6 - Generic Agent

QUESTION: Regarding the inventory holding cost, does it apply to all units held in inventory at the end of each quarter (including units produced in that quarter but not yet delivered), or only to units that were carried over from previous quarters?

## Turn 6 - User Simulator

It applies to all units held in inventory at the end of each quarter, including units produced in that quarter but not yet delivered.

## Turn 7 - Generic Agent

QUESTION: Regarding the production variables, is the number of units produced for each product in each quarter required to be an integer, or can it be a continuous (fractional) value?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are there any additional constraints or requirements not yet mentioned, such as maximum production capacity per product per quarter, minimum production levels, or restrictions on how many quarters a unit can be delayed before it is no longer acceptable?

## Turn 8 - User Simulator

Yes, there is one additional constraint: Product I cannot be produced in the second quarter due to an equipment change.

## Turn 9 - Generic Agent

QUESTION: Regarding the production variables, is the number of units produced for each product in each quarter required to be an integer, or can it be a continuous (fractional) value?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum number of quarters a unit can be delayed before it is no longer acceptable, or can units be delayed indefinitely as long as the compensation cost is paid?

## Turn 10 - User Simulator

Units can be delayed indefinitely as long as the compensation cost is paid.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as maximum production capacity per product per quarter, minimum production levels, or restrictions on inventory levels?

## Turn 11 - User Simulator

No, there are no other constraints or requirements beyond what has already been discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs.
2.  **Time Horizon:** 4 quarters (Q1 to Q4).
3.  **Products:** I, II, III.
4.  **Demand (Contract Reservations):**
    *   Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200.
    *   Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500.
    *   Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500.
    *   Demand must be met in the specific quarter. Late delivery is allowed but incurs compensation costs.
5.  **Initial Inventory:** 0 units for all products at the start of Q1.
6.  **Final Inventory Constraint:** Exactly 150 units of each product must be in inventory at the end of Q4.
7.  **Production Capacity:** Total production hours across all products combined must not exceed 15,000 hours per quarter.
8.  **Processing Times:**
    *   Product I: 2 hours/unit.
    *   Product II: 4 hours/unit.
    *   Product III: 3 hours/unit.
9.  **Production Restriction:** Product I cannot be produced in Q2 (production quantity for Product I in Q2 is 0).
10. **Delay Compensation Cost:**
    *   Calculated per unit per quarter of delay.
    *   Product I: 20 yuan/unit/quarter.
    *   Product II: 20 yuan/unit/quarter.
    *   Product III: 10 yuan/unit/quarter.
    *   Delay is defined as the number of quarters between the demand quarter and the delivery quarter.
11. **Inventory Holding Cost:**
    *   5 yuan/unit/quarter for all products.
    *   Applies to all units in inventory at the end of each quarter (including units produced in that quarter but not delivered).
12. **No Other Constraints:** No maximum production per product, no minimum production, no maximum delay limit.

**Assumptions:**
1.  **Variable Domain:** The number of units produced for each product in each quarter is assumed to be a **continuous non-negative variable**. (The user indicated this point requires internal confirmation and did not specify integrality; continuous is the standard default for linear programming formulations unless integer constraints are explicitly required).
2.  **Cost Structure:** "Compensation cost" in the objective refers specifically to the delay compensation costs described. There are no other fixed or variable production costs (e.g., labor cost per hour, material cost) included in the objective function, as only delay and holding costs were specified.
3.  **Inventory Flow:** Inventory can carry over from one quarter to the next. Units produced in a quarter can be used to satisfy demand in that quarter or future quarters. Units from previous quarters can be used to satisfy current demand.
4.  **Delay Calculation:** If a unit demanded in quarter $t$ is delivered in quarter $t+k$ (where $k > 0$), the delay cost is $k \times \text{rate}$. If delivered in the same quarter ($k=0$), delay cost is 0.