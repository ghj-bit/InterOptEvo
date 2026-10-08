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

QUESTION: For the delay compensation, is the 20 yuan (products I and II) / 10 yuan (product III) charged per unit for each quarter that a unit of demand remains undelivered (i.e., if a unit is short in Q1 and finally delivered in Q3, it incurs 2 quarters of delay compensation), or is it a one-time penalty of that amount per unit whenever any shortage occurs in a quarter?

## Turn 1 - User Simulator

It is charged per unit for each quarter that a unit of demand remains undelivered. If a unit is short in Q1 and finally delivered in Q3, it incurs 2 quarters of delay compensation.

## Turn 2 - Generic Agent

QUESTION: When a unit of demand is short in a quarter and finally delivered in a later quarter, is the delay compensation charged for every quarter from the original due quarter up to and including the delivery quarter (so a Q1 demand delivered in Q3 incurs 3 quarters of compensation), or only for the quarters it was actually short before delivery (so the same case incurs 2 quarters of compensation)?

## Turn 2 - User Simulator

It is charged only for the quarters it was actually short before delivery. A Q1 demand delivered in Q3 incurs 2 quarters of compensation.

## Turn 3 - Generic Agent

QUESTION: Can production in a given quarter be used to satisfy demand from a previous quarter (i.e., is backlogging allowed, where a unit produced in Q3 can cover a Q1 demand that was short in Q1 and Q2), or must each quarter's demand be satisfied only by production from that same quarter or earlier (no backlogging)?

## Turn 3 - User Simulator

Backlogging is allowed. A unit produced in Q3 can cover a Q1 demand that was short in Q1 and Q2.

## Turn 4 - Generic Agent

QUESTION: For the 150-unit end-of-Q4 inventory requirement, does this 150 units need to be available at the end of Q4 after satisfying all demand (including any backlogged demand from earlier quarters), or is it a separate requirement that 150 units must be produced and held in inventory by end of Q4 regardless of demand fulfillment?

## Turn 4 - User Simulator

The 150 units must be available at the end of Q4 after satisfying all demand, including any backlogged demand from earlier quarters.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on how much demand can be backlogged (i.e., a maximum number of quarters a unit can be delayed before it must be delivered), or can demand be backlogged indefinitely as long as it is eventually satisfied by the end of Q4?

## Turn 5 - User Simulator

There is no upper limit on how much demand can be backlogged. Demand can be backlogged as long as it is eventually satisfied by the end of Q4.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum production capacity per product per quarter (e.g., a limit on how many units of product I can be produced in a single quarter), or is the only production constraint the 15,000 total hours per quarter shared across all three products?

## Turn 6 - User Simulator

The only production constraint is the 15,000 total hours per quarter shared across all three products. There is no separate maximum production capacity per product per quarter.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much inventory can be held at the end of any quarter (e.g., a warehouse capacity cap), or is inventory unlimited as long as the holding cost is paid?

## Turn 7 - User Simulator

There is no limit on how much inventory can be held at the end of any quarter. Inventory is unlimited as long as the holding cost is paid.

## Turn 8 - Generic Agent

QUESTION: For the inventory holding cost of 5 yuan per unit per quarter, is this charged on the ending inventory of each quarter (i.e., units remaining at the end of Q1 are charged 5 yuan, units remaining at the end of Q2 are charged 5 yuan, etc.), or is it charged on the average inventory during the quarter, or on the beginning inventory?

## Turn 8 - User Simulator

The inventory holding cost is charged on the ending inventory of each quarter.

## Turn 9 - Generic Agent

QUESTION: Is the 150-unit end-of-Q4 inventory requirement a hard constraint (the model must have exactly 150 units of each product in inventory at the end of Q4, with no penalty for deviating), or is it a target that can be exceeded or fallen short of with some penalty?

## Turn 9 - User Simulator

It is a hard constraint. The model must have exactly 150 units of each product in inventory at the end of Q4.

## Turn 10 - Generic Agent

QUESTION: Is the 15,000 production hours per quarter a hard constraint (total hours used must be ≤ 15,000, with no option to exceed it), or can the factory exceed 15,000 hours in a quarter by paying overtime or some additional cost?

## Turn 10 - User Simulator

It is a hard constraint. Total hours used must be ≤ 15,000 per quarter, with no option to exceed it.

## Turn 11 - Generic Agent

QUESTION: Is there any fixed cost or setup cost associated with producing a product in a quarter (e.g., a cost incurred if production of product I is greater than zero in a quarter), or is the total cost purely the sum of delay compensation and inventory holding costs with no fixed or setup costs?

## Turn 11 - User Simulator

The total cost is purely the sum of delay compensation and inventory holding costs. There are no fixed or setup costs.

## Turn 12 - Generic Agent

QUESTION: Is there any requirement that all demand must be satisfied by the end of Q4 (i.e., no demand can remain unfulfilled after Q4), or is it acceptable to leave some demand unmet at the end of the planning horizon?

## Turn 12 - User Simulator

All demand must be satisfied by the end of Q4. No demand can remain unfulfilled after Q4.

## Turn 13 - Generic Agent

QUESTION: Can production in a quarter be used to satisfy demand from a future quarter (i.e., can you produce extra units in Q1 and hold them in inventory to cover Q2 or Q3 demand), or must each quarter's demand be satisfied only by production from that quarter or earlier?

## Turn 13 - User Simulator

Yes, production in a quarter can be used to satisfy demand from a future quarter. You can produce extra units in Q1 and hold them in inventory to cover Q2 or Q3 demand.

## Turn 14 - Generic Agent

QUESTION: Is there any minimum production requirement per product per quarter (e.g., you must produce at least X units of each product each quarter), or can production of any product in any quarter be zero?

## Turn 14 - User Simulator

There is no minimum production requirement per product per quarter. Production of any product in any quarter can be zero, except that product I cannot be produced in the second quarter.

## Turn 15 - Generic Agent

QUESTION: Is the restriction that product I cannot be produced in the second quarter a hard constraint (production of product I in Q2 must be exactly zero), or is it a soft constraint with a penalty if violated?

## Turn 15 - User Simulator

It is a hard constraint. Production of product I in Q2 must be exactly zero.

## Turn 16 - Generic Agent

QUESTION: Are there any other production restrictions similar to the product I / Q2 constraint (e.g., other product-quarter combinations where production is not allowed), or is product I in Q2 the only such restriction?

## Turn 16 - User Simulator

Product I in Q2 is the only such restriction.

## Turn 17 - Generic Agent

QUESTION: For the delay compensation, is it charged on the cumulative backlog at the end of each quarter (i.e., if 100 units of product I are short at the end of Q1 and 50 more are short at the end of Q2, the Q2 delay cost is based on 150 units), or is it charged only on the net new shortage in each quarter (i.e., Q2 delay cost is based on only the 50 additional units that became short in Q2)?

## Turn 17 - User Simulator

It is charged on the cumulative backlog at the end of each quarter. If 100 units of product I are short at the end of Q1 and 50 more are short at the end of Q2, the Q2 delay cost is based on 150 units.

## Turn 18 - Generic Agent

QUESTION: Is there any requirement that production must be an integer number of units (i.e., you can only produce whole units of each product), or can production be a continuous (fractional) quantity?

## Turn 18 - User Simulator

Production must be an integer number of units.

## Turn 19 - Generic Agent

QUESTION: Is there any requirement that the inventory levels at the end of each quarter must also be integer values, or can inventory be fractional as long as production is integer?

## Turn 19 - User Simulator

Inventory levels at the end of each quarter must also be integer values.

## Turn 20 - Generic Agent

QUESTION: Is there any requirement that the backlog (unmet demand) at the end of each quarter must also be an integer value, or can backlog be fractional as long as production and inventory are integers?

## Turn 20 - User Simulator

The backlog at the end of each quarter must also be an integer value.

## Turn 21 - Generic Agent

QUESTION: Is there any requirement that the total production hours used in each quarter must be an integer number of hours, or can the hours be fractional as long as the production units are integers?

## Turn 21 - User Simulator

The total production hours used in each quarter must be an integer number of hours.

## Turn 22 - Generic Agent

QUESTION: Is there any requirement that the total cost (delay compensation + inventory holding cost) must be minimized subject to all the constraints we've discussed, or is there any other objective or secondary criterion (e.g., minimize total production, maximize on-time delivery rate) that should also be considered?

## Turn 22 - User Simulator

The objective is to minimize the total cost (delay compensation + inventory holding cost) subject to all the constraints we've discussed. There are no other objectives or secondary criteria.

## Turn 23 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of the production scheduling problem:

**Planning Horizon:** 4 quarters (Q1–Q4).

**Products:** I, II, III.

**Decision Variables (all integer):**
- Production of each product in each quarter (units).
- Ending inventory of each product at the end of each quarter (units).
- Cumulative backlog (unmet demand) of each product at the end of each quarter (units).

**Parameters:**
- Demand (contract reservations) per product per quarter:
  - Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200
  - Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500
  - Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500
- Production hours per unit: Product I = 2, Product II = 4, Product III = 3.
- Delay compensation per unit per quarter of backlog: Product I = 20 yuan, Product II = 20 yuan, Product III = 10 yuan.
- Inventory holding cost per unit per quarter (on ending inventory): 5 yuan for all products.

**Objective:** Minimize total cost = sum over all quarters of (delay compensation on cumulative backlog at end of each quarter + inventory holding cost on ending inventory at each quarter).

**Constraints:**
1. **Production hours:** In each quarter, total production hours (sum over products of units × hours per unit) ≤ 15,000.
2. **Initial inventory:** 0 for all products at the start of Q1.
3. **End-of-Q4 inventory:** Exactly 150 units of each product must be in inventory at the end of Q4 (after satisfying all demand).
4. **All demand satisfied by end of Q4:** No backlog may remain after Q4.
5. **Backlogging allowed:** Production in a later quarter can satisfy demand from an earlier quarter.
6. **Forward production allowed:** Production in an earlier quarter can satisfy demand from a later quarter (held in inventory).
7. **Product I in Q2:** Production of product I in Q2 must be exactly zero (hard constraint).
8. **No other production restrictions:** No per-product capacity caps, no minimum production, no other product-quarter prohibitions.
9. **Inventory and backlog:** Unlimited (no caps), but must be non-negative integers.
10. **All variables integer:** Production units, inventory levels, and backlog levels must all be integers.
11. **No fixed/setup costs:** Total cost is purely delay compensation + inventory holding.
12. **Delay compensation basis:** Charged on cumulative backlog at the end of each quarter (i.e., if 100 units are short at end of Q1 and 150 units are short at end of Q2, Q2 delay cost is based on 150 units).
13. **Holding cost basis:** Charged on ending inventory of each quarter.