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

QUESTION: Is the 150-unit inventory requirement for each product at the end of the fourth quarter a strict minimum (at least 150 units), or must it be exactly 150 units?

## Turn 1 - User Simulator

It must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 2 - Generic Agent

QUESTION: Are the contract reservation quantities in the table (e.g., 1500 for Product I in Q1) the exact demand that must be delivered in that specific quarter, or are they minimum requirements that can be met with additional production?

## Turn 2 - User Simulator

They are the exact demand that must be delivered in that specific quarter.

## Turn 3 - Generic Agent

QUESTION: Is the 15,000 production hours limit per quarter a hard constraint that must not be exceeded, or is it a soft target where exceeding it incurs a penalty?

## Turn 3 - User Simulator

It is a hard constraint that must not be exceeded.

## Turn 4 - Generic Agent

QUESTION: Are the production hours per unit (2 hours for Product I, 4 hours for Product II, 3 hours for Product III) fixed constants, or do they vary depending on the quarter or production volume?

## Turn 4 - User Simulator

They are fixed constants.

## Turn 5 - Generic Agent

QUESTION: Is the delay compensation cost (20 yuan per unit per quarter for Products I and II, 10 yuan per unit per quarter for Product III) incurred for each unit of demand that is not delivered in the quarter it is due, and does this cost accumulate for each subsequent quarter the unit remains undelivered?

## Turn 5 - User Simulator

Yes, the delay compensation cost is incurred for each unit of demand that is not delivered in the quarter it is due, and it accumulates for each subsequent quarter the unit remains undelivered.

## Turn 6 - Generic Agent

QUESTION: Is the inventory holding cost of 5 yuan per unit per quarter applied to all units of inventory held at the end of each quarter, or only to units that were produced in the current quarter but not delivered?

## Turn 6 - User Simulator

It is applied to all units of inventory held at the end of each quarter.

## Turn 7 - Generic Agent

QUESTION: Is the production schedule decision variable the number of units of each product produced in each quarter, or is it the number of units of each product delivered in each quarter?

## Turn 7 - User Simulator

The decision variable is the number of units of each product produced in each quarter.

## Turn 8 - Generic Agent

QUESTION: Are the production quantities for each product in each quarter required to be integer values, or can they be continuous (fractional) values?

## Turn 8 - User Simulator

They must be integer values.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint on the maximum inventory level that can be held for each product at the end of any quarter, or is inventory capacity unlimited?

## Turn 9 - User Simulator

Inventory capacity is unlimited.

## Turn 10 - Generic Agent

QUESTION: Is there a constraint that production in a given quarter can only be used to satisfy demand in that same quarter or future quarters, or can production in a future quarter be used to satisfy demand in a past quarter?

## Turn 10 - User Simulator

Production in a given quarter can only be used to satisfy demand in that same quarter or future quarters.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint on the minimum production quantity for each product in each quarter, or can production be zero in any quarter?

## Turn 11 - User Simulator

Production can be zero in any quarter, except that Product I cannot be produced in the second quarter.

## Turn 12 - Generic Agent

QUESTION: Is the constraint that Product I cannot be produced in the second quarter a hard constraint (production must be exactly zero), or is it a soft constraint where producing Product I in the second quarter incurs a penalty?

## Turn 12 - User Simulator

It is a hard constraint; production of Product I in the second quarter must be exactly zero.

## Turn 13 - Generic Agent

QUESTION: Are there any other constraints on production, such as minimum production quantities, maximum production quantities, or restrictions on which products can be produced in specific quarters, besides the one already mentioned for Product I in the second quarter?

## Turn 13 - User Simulator

No, there are no other constraints on production besides the one for Product I in the second quarter.

## Turn 14 - Generic Agent

QUESTION: Is the total cost to be minimized the sum of the delay compensation costs and the inventory holding costs only, or are there other cost components such as production costs or labor costs that should be included?

## Turn 14 - User Simulator

The total cost to be minimized is the sum of the delay compensation costs and the inventory holding costs only.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total cost, defined as the sum of delay compensation costs and inventory holding costs.
2.  **Time Horizon:** 4 quarters.
3.  **Products:** I, II, III.
4.  **Decision Variables:** $x_{p,t}$ = integer number of units of product $p$ produced in quarter $t$.
5.  **Demand:** Exact demand must be delivered in the specific quarter listed in the table.
    *   Product I: [1500, 1000, 2000, 1200]
    *   Product II: [1500, 1500, 1200, 1500]
    *   Product III: [1000, 2000, 1500, 2500]
6.  **Initial Inventory:** 0 units for all products at the start of Q1.
7.  **Final Inventory Constraint:** Exactly 150 units of each product must be in inventory at the end of Q4.
8.  **Production Capacity:** Total production hours used in each quarter must not exceed 15,000 hours (hard constraint).
9.  **Processing Times:** Fixed constants: Product I = 2 hours/unit, Product II = 4 hours/unit, Product III = 3 hours/unit.
10. **Production Restriction:** Product I cannot be produced in Q2 ($x_{I,2} = 0$).
11. **Inventory Flow:** Production in a quarter can satisfy demand in that quarter or future quarters. Inventory carries over.
12. **Delay Compensation Cost:**
    *   Product I: 20 yuan/unit/quarter.
    *   Product II: 20 yuan/unit/quarter.
    *   Product III: 10 yuan/unit/quarter.
    *   Cost accumulates for each quarter a unit of demand remains undelivered.
13. **Inventory Holding Cost:** 5 yuan/unit/quarter for all units held in inventory at the end of each quarter.
14. **Integrality:** Production quantities must be integers.
15. **Non-negativity:** Production quantities must be non-negative.
16. **Inventory Capacity:** Unlimited.
17. **Other Costs:** None (no production/labor costs included in objective).