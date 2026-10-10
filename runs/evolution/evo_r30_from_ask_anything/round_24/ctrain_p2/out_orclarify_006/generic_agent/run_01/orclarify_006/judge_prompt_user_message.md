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

QUESTION: Are the contract reservation figures in Table 1-10 the minimum quantities that must be delivered to customers in each quarter (with any excess production allowed to be held in inventory), or are they the exact quantities that must be delivered in each quarter (with no excess delivery permitted)?

## Turn 1 - User Simulator

The contract reservation figures in Table 1-10 are the minimum quantities that must be delivered to customers in each quarter. Excess production is allowed and can be held in inventory.

## Turn 2 - Generic Agent

QUESTION: Is the 15,000-hour production limit a hard ceiling that must not be exceeded in any quarter, or is it a soft target where exceeding it incurs an additional penalty cost?

## Turn 2 - User Simulator

The 15,000-hour production limit is a hard ceiling that must not be exceeded in any quarter.

## Turn 3 - Generic Agent

QUESTION: Is the 150-unit end-of-quarter-4 inventory requirement a hard constraint that must be met exactly, or is it a minimum target where having more than 150 units is allowed?

## Turn 3 - User Simulator

The 150-unit end-of-quarter-4 inventory requirement is a hard constraint that must be met exactly.

## Turn 4 - Generic Agent

QUESTION: Is the delay compensation cost of 20 yuan per unit per quarter for products I and II (and 10 yuan for product III) charged for each quarter that a unit remains undelivered beyond its contract quarter, accumulating quarter over quarter until it is finally delivered?

## Turn 4 - User Simulator

Yes, the delay compensation cost is charged for each quarter that a unit remains undelivered beyond its contract quarter, accumulating quarter over quarter until it is finally delivered.

## Turn 5 - Generic Agent

QUESTION: Is the inventory holding cost of 5 yuan per unit per quarter applied to all units in inventory at the end of each quarter, or only to units that were produced in the current quarter but not delivered in that same quarter?

## Turn 5 - User Simulator

The inventory holding cost of 5 yuan per unit per quarter is applied to all units in inventory at the end of each quarter.

## Turn 6 - Generic Agent

QUESTION: Is the "compensation cost" in your objective function referring only to the delay compensation cost for undelivered units, or does it also include a separate cost for the labor hours used in production (e.g., a wage rate per hour)?

## Turn 6 - User Simulator

The "compensation cost" in the objective function refers only to the delay compensation cost for undelivered units. It does not include a separate cost for labor hours used in production.

## Turn 7 - Generic Agent

QUESTION: Are the production quantities for each product in each quarter required to be whole numbers (integers), or can they be fractional values?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: If the production quantities are not confirmed as integers, should I treat them as continuous (allowing fractional units) for the model, or would you prefer I assume they must be whole numbers?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Since the integrality of production quantities remains unconfirmed, I will proceed with the assumption that production quantities are continuous (fractional units allowed); is that acceptable as a working assumption for now?

## Turn 9 - User Simulator

Yes, that is acceptable as a working assumption for now.

## Turn 10 - Generic Agent

QUESTION: Are there any additional constraints or requirements beyond those already stated (the 15,000-hour quarterly ceiling, the minimum delivery quantities, the exact 150-unit end-of-Q4 inventory, and the zero initial inventory) that I should include in the model, such as maximum inventory capacity, minimum production levels, or restrictions on which products can be produced in which quarters?

## Turn 10 - User Simulator

Yes, there is one additional constraint: Product I cannot be produced in the second quarter due to an equipment change.

## Turn 11 - Generic Agent

QUESTION: Is the restriction that Product I cannot be produced in the second quarter a hard constraint (production of Product I in Q2 must be exactly zero), or is it a soft constraint where producing Product I in Q2 incurs an additional penalty cost?

## Turn 11 - User Simulator

It is a hard constraint; production of Product I in the second quarter must be exactly zero.

## Turn 12 - Generic Agent

QUESTION: Are there any other additional constraints or requirements beyond the ones already confirmed (the 15,000-hour quarterly ceiling, minimum delivery quantities, exact 150-unit end-of-Q4 inventory, zero initial inventory, and Product I not produced in Q2) that I should include in the model?

## Turn 12 - User Simulator

No, there are no other additional constraints or requirements beyond those already confirmed.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Minimize total cost = total delay compensation cost + total inventory holding cost over four quarters.

**Decision Variables:**
- Production quantity of each product (I, II, III) in each quarter (1–4), continuous and non-negative.
- Inventory level of each product at the end of each quarter, non-negative.
- Delivery quantity of each product in each quarter, non-negative.

**Confirmed Facts:**

1. **Objective sense:** Minimize (total delay compensation + total inventory holding). Confirmed.
2. **Delay compensation cost:** Charged per unit per quarter for each quarter a unit remains undelivered beyond its contract quarter, accumulating until delivered. Rates: 20 yuan/unit/quarter for Products I and II; 10 yuan/unit/quarter for Product III. Confirmed.
3. **Inventory holding cost:** 5 yuan per unit per quarter, applied to all units in inventory at the end of each quarter. Confirmed.
4. **Contract reservations (minimum deliveries per quarter):**
   - Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200
   - Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500
   - Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500
   These are minimums; excess production may be held in inventory. Confirmed.
5. **Production hours per unit:** Product I = 2 hrs, Product II = 4 hrs, Product III = 3 hrs. Confirmed.
6. **Quarterly production hour ceiling:** Total production hours across all products in each quarter ≤ 15,000 (hard constraint). Confirmed.
7. **Initial inventory:** 0 units for each product at the start of Q1. Confirmed.
8. **End-of-Q4 inventory:** Exactly 150 units for each product (hard constraint). Confirmed.
9. **Product I in Q2:** Production of Product I in Q2 = 0 (hard constraint). Confirmed.
10. **No other constraints** beyond those listed. Confirmed.

**Explicit Assumptions:**

1. **Production quantities are continuous** (fractional units allowed). Flagged as an open assumption pending internal confirmation.
2. **No maximum inventory capacity** is imposed.
3. **No minimum production level** is required in any quarter (other than what is implied by meeting minimum deliveries and the end-of-Q4 inventory target).
4. **All three products can be produced in all quarters** except Product I in Q2 (which is zero).
5. **Delivery in a given quarter can come from current-quarter production or from prior inventory**, and undelivered contract units carry forward with accumulating delay cost.
6. **The 15,000-hour limit applies to total production hours** (sum over all products) in each quarter, not per product.

**Model Structure (Linear Program):**

- **Variables:** P[p,q] = production of product p in quarter q; I[p,q] = inventory of product p at end of quarter q; D[p,q] = delivery of product p in quarter q.
- **Flow balance:** I[p,q] = I[p,q-1] + P[p,q] − D[p,q], with I[p,0] = 0.
- **Minimum delivery:** D[p,q] ≥ contract[p,q].
- **End-of-Q4 inventory:** I[p,4] = 150 for each product p.
- **Hour constraint:** 2·P[I,q] + 4·P[II,q] + 3·P[III,q] ≤ 15,000 for each quarter q.
- **Product I Q2:** P[I,2] = 0.
- **Non-negativity:** All variables ≥ 0.
- **Objective:** Minimize Σ over all products and quarters of [delay_cost_rate[p] × (undelivered units carried beyond contract quarter) + 5 × I[p,q]].