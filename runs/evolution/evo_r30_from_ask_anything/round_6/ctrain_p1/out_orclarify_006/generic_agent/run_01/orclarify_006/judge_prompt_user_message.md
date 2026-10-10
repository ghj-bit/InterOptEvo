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

QUESTION: When you say "total production hours used must not exceed 15,000 hours" per quarter, does this 15,000-hour limit apply to the sum of hours across all three products combined in each quarter, or is it a separate 15,000-hour limit for each product individually

## Turn 1 - User Simulator

It is a single 15,000-hour limit for the sum of hours across all three products combined in each quarter.

## Turn 2 - Generic Agent

QUESTION: Regarding the "delay compensation" cost, does this apply when production in a given quarter falls short of that quarter's contract reservation (i.e., unmet demand is carried over to a later quarter), and is the cost calculated as the number of units delayed multiplied by the per-unit rate multiplied by the number of quarters the units are delayed

## Turn 2 - User Simulator

Yes, that is correct. The delay compensation applies when production in a given quarter falls short of that quarter's contract reservation, and the cost is calculated as the number of units delayed multiplied by the per-unit rate multiplied by the number of quarters the units are delayed.

## Turn 3 - Generic Agent

QUESTION: Regarding the inventory holding cost, does this apply to units that are produced in a quarter but not delivered in that same quarter (i.e., units produced in excess of that quarter's contract reservation that are carried over to satisfy future demand), and is the cost calculated as the number of such units multiplied by 5 yuan per unit per quarter

## Turn 3 - User Simulator

Yes, that is correct. The inventory holding cost applies to units produced in a quarter but not delivered in that same quarter, and the cost is calculated as the number of such units multiplied by 5 yuan per unit per quarter.

## Turn 4 - Generic Agent

QUESTION: Regarding the "compensation cost" in your objective function, is this the same as the "delay compensation" cost you described earlier (20 yuan per unit per quarter for products I and II, 10 yuan per unit per quarter for product III), or is there a separate compensation cost

## Turn 4 - User Simulator

Yes, the "compensation cost" in the objective function is the same as the "delay compensation" cost described earlier (20 yuan per unit per quarter for products I and II, 10 yuan per unit per quarter for product III). There is no separate compensation cost.

## Turn 5 - Generic Agent

QUESTION: Regarding the production hours constraint, is the 15,000-hour limit per quarter a hard constraint that must be strictly satisfied (i.e., total hours used across all products in each quarter cannot exceed 15,000), or is it a soft constraint that can be violated

## Turn 5 - User Simulator

It is a hard constraint. The total production hours used across all products in each quarter must not exceed 15,000 hours.

## Turn 6 - Generic Agent

QUESTION: Regarding the inventory balance, can inventory be negative (i.e., can you produce less than demand in a quarter and make up the difference in a later quarter, incurring the delay compensation cost), or must inventory never go below zero

## Turn 6 - User Simulator

Inventory can be negative. You can produce less than demand in a quarter and make up the difference in a later quarter, incurring the delay compensation cost.

## Turn 7 - Generic Agent

QUESTION: Regarding the final inventory requirement, must the inventory of each product be exactly 150 units at the end of the fourth quarter, or at least 150 units

## Turn 7 - User Simulator

It must be exactly 150 units for each product at the end of the fourth quarter.

## Turn 8 - Generic Agent

QUESTION: Regarding the production quantities, must the number of units produced for each product in each quarter be a whole number (integer), or can they be fractional

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Since the integrality requirement is pending internal confirmation, should I proceed with the assumption that production quantities can be fractional (continuous) for now, and you can let me know later if they must be integers

## Turn 9 - User Simulator

Yes, please proceed with the assumption that production quantities can be fractional (continuous) for now.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Minimize total cost = (delay compensation cost + inventory holding cost) over 4 quarters.
   - Delay compensation cost: For products I and II, 20 yuan per unit per quarter delayed; for product III, 10 yuan per unit per quarter delayed.
   - Inventory holding cost: 5 yuan per unit per quarter for units produced but not delivered in the current quarter.

2. **Decision Variables:** Production quantity for each of the 3 products in each of the 4 quarters (continuous, non-negative).

3. **Hard Constraints:**
   - Total production hours per quarter ≤ 15,000 hours (combined across all products).
   - Hours per unit: Product I = 2 hours, Product II = 4 hours, Product III = 3 hours.
   - Final inventory at end of Q4 must be exactly 150 units for each product.

4. **Initial Conditions:**
   - Beginning inventory in Q1 is 0 for all three products.

5. **Demand (Contract Reservations):**
   - Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200
   - Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500
   - Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500

6. **Inventory Balance Rules:**
   - Inventory can be negative (backorders allowed).
   - Delay compensation is incurred when production < demand in a quarter, calculated as (units delayed) × (per-unit rate) × (number of quarters delayed).
   - Holding cost is incurred when production > demand in a quarter, calculated as (units held) × 5 yuan per unit per quarter.

7. **Assumptions:**
   - Production quantities are continuous (not required to be integers).
   - No other costs or constraints beyond those specified.