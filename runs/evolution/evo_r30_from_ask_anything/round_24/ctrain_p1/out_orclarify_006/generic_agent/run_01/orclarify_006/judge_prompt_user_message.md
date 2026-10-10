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

QUESTION: Are the contract reservation figures in the table the minimum quantities that must be delivered to customers in each quarter, or are they the exact quantities that must be delivered in each quarter?

## Turn 1 - User Simulator

They are the minimum quantities that must be delivered to customers in each quarter. Late delivery is allowed, and the compensation costs apply for any delay.

## Turn 2 - Generic Agent

QUESTION: When a unit is produced in one quarter but delivered in a later quarter to satisfy a contract, is the inventory holding cost of 5 yuan per unit per quarter charged for every quarter the unit sits in inventory before delivery, or is it charged only for the first quarter it is held?

## Turn 2 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter is charged for every quarter the unit sits in inventory before delivery.

## Turn 3 - Generic Agent

QUESTION: Is the delay compensation cost charged for every quarter a unit is delayed beyond its contract quarter, or is it charged only for the first quarter of delay?

## Turn 3 - User Simulator

The delay compensation cost is charged for every quarter a unit is delayed beyond its contract quarter.

## Turn 4 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-4 inventory requirement a minimum (at least 150 units) or an exact target (exactly 150 units) for each product?

## Turn 4 - User Simulator

It is an exact target: exactly 150 units for each product at the end of the fourth quarter.

## Turn 5 - Generic Agent

QUESTION: Can the factory produce more units in a quarter than the minimum contract delivery requirement for that quarter, with the extra units held in inventory for future quarters?

## Turn 5 - User Simulator

Yes, the factory can produce more units in a quarter than the minimum contract delivery requirement for that quarter, with the extra units held in inventory for future quarters.

## Turn 6 - Generic Agent

QUESTION: Is the 15,000 production hours per quarter a hard ceiling that must not be exceeded, or is it a soft target where exceeding it incurs an additional penalty cost?

## Turn 6 - User Simulator

It is a hard ceiling that must not be exceeded.

## Turn 7 - Generic Agent

QUESTION: Are the production quantities for each product in each quarter required to be whole numbers (integers), or can they be fractional values?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: If the production quantities are not confirmed as integers, should I treat them as continuous (allowing fractional units) or as integers (whole units only)?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any additional constraints or requirements not yet mentioned, such as maximum production limits per product per quarter, minimum production levels, or restrictions on which products can be produced in which quarters?

## Turn 9 - User Simulator

Yes, there is one additional restriction: Product I cannot be produced in the second quarter due to an equipment change.

## Turn 10 - Generic Agent

QUESTION: Is the restriction that Product I cannot be produced in the second quarter a hard constraint (zero production of Product I in Q2) or a soft constraint where producing Product I in Q2 incurs a penalty cost?

## Turn 10 - User Simulator

It is a hard constraint: zero production of Product I in the second quarter.

## Turn 11 - Generic Agent

QUESTION: Are there any other additional constraints or requirements not yet mentioned, such as maximum production limits per product per quarter, minimum production levels, or restrictions on which products can be produced in which quarters?

## Turn 11 - User Simulator

No, there are no other additional constraints or requirements beyond what has already been discussed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Minimize total cost = (total delay compensation cost) + (total inventory holding cost).

**Planning Horizon:** 4 quarters.

**Products:** I, II, III.

**Decision Variables:** Production quantity of each product in each quarter (continuous, non-negative). Production of Product I in Q2 is forced to zero.

**Contract Reservations (minimum deliveries per quarter per product):**
- Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200
- Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500
- Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500

**Initial Inventory:** 0 units for each product at the start of Q1.

**End-of-Horizon Inventory:** Exactly 150 units for each product at the end of Q4.

**Production Hours:**
- Product I: 2 hours/unit
- Product II: 4 hours/unit
- Product III: 3 hours/unit
- Hard ceiling: Total production hours per quarter ≤ 15,000.

**Hard Constraint:** Product I production in Q2 = 0.

**Costs:**
- Inventory holding cost: 5 yuan per unit per quarter, charged for every quarter a unit sits in inventory before delivery.
- Delay compensation: Charged for every quarter a unit is delayed beyond its contract quarter.
  - Product I: 20 yuan per unit per quarter of delay.
  - Product II: 20 yuan per unit per quarter of delay.
  - Product III: 10 yuan per unit per quarter of delay.

**Open Assumptions:**
- Production quantities are treated as continuous (non-integer) values, as integrality was not confirmed. If integer production is required, the model would need to be adjusted to an integer program.