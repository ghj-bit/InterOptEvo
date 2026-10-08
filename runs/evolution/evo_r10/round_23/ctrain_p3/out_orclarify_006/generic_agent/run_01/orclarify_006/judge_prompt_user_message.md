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

QUESTION: For the "150 units in stock for each product by the end of the fourth quarter" requirement, should I treat this as an exact equality (ending inventory must be exactly 150 units per product) or as a minimum (ending inventory must be at least 150 units per product)?

## Turn 1 - User Simulator

It must be an exact equality. The ending inventory for each product at the end of the fourth quarter must be exactly 150 units.

## Turn 2 - Generic Agent

QUESTION: The contract reservations table gives a required delivery quantity per product per quarter, but it is not clear whether these are hard minimums that must be met on time (with any shortfall incurring the delay compensation) or exact targets that must be delivered in that quarter. Should I treat the table values as minimum on-time delivery requirements, where delivering less than the reservation in a quarter creates a backlog that is compensated at the delay rate and must be made up in a later quarter?

## Turn 2 - User Simulator

Yes, treat the table values as minimum on-time delivery requirements. If less than the reservation is delivered in a quarter, the shortfall creates a backlog that incurs the delay compensation and must be made up in a later quarter.

## Turn 3 - Generic Agent

QUESTION: When a backlog (delayed units) is made up in a later quarter, does the delay compensation accumulate for each quarter the unit is delayed (i.e., a unit delayed by 2 quarters pays the per-quarter delay rate twice), or is the delay compensation charged only once per unit regardless of how many quarters it is delayed?

## Turn 3 - User Simulator

The delay compensation accumulates for each quarter the unit is delayed. A unit delayed by 2 quarters pays the per-quarter delay rate twice.

## Turn 4 - Generic Agent

QUESTION: The objective mentions "compensation cost + inventory holding cost" but does not mention a production cost. Should the objective be only the sum of delay compensation cost and inventory holding cost (with no per-unit production cost), or is there a production cost per unit (or per hour) that I should include?

## Turn 4 - User Simulator

The objective is only the sum of delay compensation cost and inventory holding cost. There is no per-unit production cost to include.

## Turn 5 - Generic Agent

QUESTION: The 15,000 production hours per quarter is a cap on total hours used. Is there any lower bound on production hours per quarter (i.e., a minimum number of hours that must be used), or can the factory use anywhere from 0 up to 15,000 hours in a quarter?

## Turn 5 - User Simulator

There is no lower bound on production hours per quarter. The factory can use anywhere from 0 up to 15,000 hours in a quarter.

## Turn 6 - Generic Agent

QUESTION: The inventory holding cost is 5 yuan per unit per quarter for products produced but not delivered in the current quarter. Does this holding cost apply to all units in inventory at the end of each quarter (including the 150 units that must be held at the end of Q4), or does it apply only to units that are in inventory during quarters 1-3 (i.e., not charged on the final Q4 ending inventory)?

## Turn 6 - User Simulator

The holding cost applies to all units in inventory at the end of each quarter, including the 150 units held at the end of Q4.

## Turn 7 - Generic Agent

QUESTION: The delay compensation is charged per unit per quarter for units that are delayed. If a unit is produced in quarter t but the reservation it was meant to satisfy was in an earlier quarter, is the delay compensation charged starting from the quarter after the reservation quarter (i.e., a unit reserved in Q1 but delivered in Q2 pays 1 quarter of delay, delivered in Q3 pays 2 quarters of delay), or is it charged from the quarter of production?

## Turn 7 - User Simulator

The delay compensation is charged starting from the quarter after the reservation quarter. A unit reserved in Q1 but delivered in Q2 pays 1 quarter of delay; delivered in Q3 pays 2 quarters of delay.

## Turn 8 - Generic Agent

QUESTION: Can a unit produced in a given quarter be used to satisfy a reservation from an earlier quarter in that same quarter (i.e., can production in Q2 be delivered in Q2 to cover a Q1 backlog), or must a unit be produced in a strictly earlier quarter to count toward a reservation?

## Turn 8 - User Simulator

Yes, a unit produced in a given quarter can be used to satisfy a reservation from an earlier quarter in that same quarter. Production in Q2 can be delivered in Q2 to cover a Q1 backlog.

## Turn 9 - Generic Agent

QUESTION: Can a unit produced in a given quarter be used to satisfy a reservation from a later quarter (i.e., can production in Q1 be held in inventory and delivered in Q2 to count toward the Q2 reservation), or can units only be delivered in the quarter they are produced or later quarters?

## Turn 9 - User Simulator

Yes, a unit produced in a given quarter can be held in inventory and delivered in a later quarter to count toward that later quarter's reservation.

## Turn 10 - Generic Agent

QUESTION: Is there any constraint on the maximum inventory level per product per quarter (a storage capacity limit), or can inventory grow without bound as long as the production hours cap is respected?

## Turn 10 - User Simulator

There is no maximum inventory level constraint. Inventory can grow without bound as long as the production hours cap is respected.

## Turn 11 - Generic Agent

QUESTION: Are there any constraints on the workforce or labor that I should model (e.g., hiring/firing costs, a fixed number of workers, overtime limits), or is the only labor-related constraint the 15,000 production hours per quarter cap?

## Turn 11 - User Simulator

The only labor-related constraint is the 15,000 production hours per quarter cap. There are no hiring/firing costs, fixed worker counts, or overtime limits to model.

## Turn 12 - Generic Agent

QUESTION: The delay compensation rates are 20 yuan per unit per quarter for products I and II, and 10 yuan per unit per quarter for product III. Is this the only form of penalty for not meeting a reservation on time, or is there also a maximum allowable delay (i.e., a deadline by which all backlogs must be cleared)?

## Turn 12 - User Simulator

The delay compensation is the only form of penalty for not meeting a reservation on time. There is no maximum allowable delay or deadline by which all backlogs must be cleared.

## Turn 13 - Generic Agent

QUESTION: The problem states that at the end of Q4, inventory must be exactly 150 units per product. Does this mean that all reservations (including any backlogged units) must be fully satisfied by the end of Q4, or could there still be unsatisfied backlogs at the end of Q4 as long as the 150-unit inventory requirement is met?

## Turn 13 - User Simulator

All reservations, including any backlogged units, must be fully satisfied by the end of Q4. There cannot be unsatisfied backlogs at the end of Q4.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Minimize total cost = delay compensation cost + inventory holding cost. No production cost.

**Time horizon:** 4 quarters (Q1–Q4).

**Products:** I, II, III.

**Decision variables:**
- Production quantity of each product in each quarter (continuous or integer — I will treat as continuous unless otherwise specified).
- Delivery quantity of each product in each quarter (allocated to satisfy reservations and backlogs).
- Inventory at the end of each quarter for each product.
- Backlog (unsatisfied reservation) at the end of each quarter for each product.

**Data:**
- Reservation (minimum on-time delivery) per product per quarter:
  - Product I: Q1=1500, Q2=1000, Q3=2000, Q4=1200
  - Product II: Q1=1500, Q2=1500, Q3=1200, Q4=1500
  - Product III: Q1=1000, Q2=2000, Q3=1500, Q4=2500
- Production hours per unit: I=2, II=4, III=3.
- Production hours cap: 15,000 hours per quarter (no lower bound).
- Initial inventory: 0 for all products at start of Q1.
- Ending inventory: exactly 150 units per product at end of Q4.
- No maximum inventory constraint.
- No workforce constraints beyond the hours cap.

**Costs:**
- Inventory holding cost: 5 yuan per unit per quarter, charged on all units in inventory at the end of each quarter (including Q4).
- Delay compensation: charged per unit per quarter of delay, starting from the quarter after the reservation quarter.
  - Products I and II: 20 yuan per unit per quarter of delay.
  - Product III: 10 yuan per unit per quarter of delay.
  - A unit reserved in Q1 delivered in Q2 pays 1 quarter of delay; delivered in Q3 pays 2 quarters; delivered in Q4 pays 3 quarters.

**Constraints:**
1. Production hours per quarter ≤ 15,000.
2. Inventory balance: for each product and quarter, beginning inventory + production − delivery = ending inventory.
3. Delivery in a quarter can satisfy current-quarter reservations and prior backlogs.
4. All reservations (including backlogs) must be fully satisfied by end of Q4 (no remaining backlog).
5. Ending inventory at end of Q4 = exactly 150 units per product.
6. Inventory and backlog are non-negative.
7. Production is non-negative.

**Key modeling notes:**
- A unit can be produced in any quarter and delivered in that quarter or any later quarter.
- Delay compensation accumulates linearly with the number of quarters a unit is delayed beyond its reservation quarter.
- The holding cost is charged on physical inventory (units produced but not yet delivered), not on backlogs.