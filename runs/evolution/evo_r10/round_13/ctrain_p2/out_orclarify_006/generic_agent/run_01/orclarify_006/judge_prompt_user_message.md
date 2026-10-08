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

QUESTION: For the end-of-quarter inventory requirement of 150 units per product, is this a minimum (at least 150), an exact value (exactly 150), or a maximum (at most 150)?

## Turn 1 - User Simulator

It is an exact value: exactly 150 units for each product at the end of the fourth quarter.

## Turn 2 - Generic Agent

QUESTION: The table is labeled "contract reservations" — does each quarter's number represent demand that must be delivered in that same quarter (so producing more than the reservation in a quarter creates inventory, and producing less creates a delay/backorder), or is it a minimum that must be met with the option to deliver extra early?

## Turn 2 - User Simulator

The number represents demand that must be delivered in that same quarter. Producing more than the reservation in a quarter creates inventory, and producing less creates a delay/backorder.

## Turn 3 - Generic Agent

QUESTION: When a product is short in a quarter (produced less than that quarter's demand), is the shortfall carried forward as a backorder that must be made up in later quarters (so the delay cost is 20/20/10 yuan per unit per quarter of delay, accumulating each quarter until delivered), or is each quarter's demand independent and any shortfall is simply lost (charged once at the delay rate, never delivered)?

## Turn 3 - User Simulator

The shortfall is carried forward as a backorder that must be made up in later quarters. The delay cost accumulates each quarter until the units are delivered.

## Turn 4 - Generic Agent

QUESTION: The objective mentions "compensation cost + inventory holding cost" — is the total cost to minimize exactly the sum of the delay compensation cost and the inventory holding cost, with no other cost components (such as production cost or labor cost)?

## Turn 4 - User Simulator

Yes, the total cost to minimize is exactly the sum of the delay compensation cost and the inventory holding cost, with no other cost components.

## Turn 5 - Generic Agent

QUESTION: For the delay compensation cost, is it charged on the backorder quantity at the end of each quarter (i.e., each unit still undelivered at the end of quarter t is charged that quarter's rate once), so a unit delayed across two quarters is charged twice?

## Turn 5 - User Simulator

Yes, the delay compensation cost is charged on the backorder quantity at the end of each quarter. Each unit still undelivered at the end of a quarter is charged that quarter's rate once, so a unit delayed across two quarters is charged twice.

## Turn 6 - Generic Agent

QUESTION: For the inventory holding cost of 5 yuan per unit per quarter, is it charged on the inventory quantity at the end of each quarter (including the required 150 units at the end of quarter 4), or only on inventory carried into the next quarter (so the end-of-quarter-4 inventory of 150 would not be charged)?

## Turn 6 - User Simulator

The inventory holding cost is charged on the inventory quantity at the end of each quarter, including the required 150 units at the end of quarter 4.

## Turn 7 - Generic Agent

QUESTION: Can a product's inventory and backorder be positive at the same time in the same quarter (i.e., can you hold some units in stock while others are backordered), or must each product be in exactly one state per quarter — either in inventory or in backorder, but not both?

## Turn 7 - User Simulator

Each product must be in exactly one state per quarter — either in inventory or in backorder, but not both.

## Turn 8 - Generic Agent

QUESTION: Are production quantities required to be whole units (integer), or can they be fractional?

## Turn 8 - User Simulator

Production quantities are required to be whole units (integer).

## Turn 9 - Generic Agent

QUESTION: The 15,000 production hours per quarter limit — is this a hard cap that must not be exceeded in any quarter, with any unused hours simply wasted (no cost, no carryover to other quarters)?

## Turn 9 - User Simulator

Yes, the 15,000 production hours per quarter is a hard cap that must not be exceeded in any quarter. Any unused hours are simply wasted, with no cost and no carryover to other quarters.

## Turn 10 - Generic Agent

QUESTION: At the end of quarter 4, the backorder for each product must be zero (all demand delivered), right? In other words, the only end-of-horizon conditions are: inventory exactly 150 per product and no outstanding backorders.

## Turn 10 - User Simulator

Yes, at the end of quarter 4, the backorder for each product must be zero. The only end-of-horizon conditions are: inventory exactly 150 per product and no outstanding backorders.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Production scheduling for 3 products (I, II, III) over 4 quarters, minimizing total cost = delay compensation cost + inventory holding cost.

**Demand (must be delivered in the same quarter):**
| Product | Q1 | Q2 | Q3 | Q4 |
|---------|------|------|------|------|
| I | 1500 | 1000 | 2000 | 1200 |
| II | 1500 | 1500 | 1200 | 1500 |
| III | 1000 | 2000 | 1500 | 2500 |

**Parameters:**
- Production hours per unit: I = 2, II = 4, III = 3
- Production hours cap: 15,000 per quarter (hard cap, unused hours wasted, no carryover)
- Delay compensation (per unit per quarter of backorder): I = 20, II = 20, III = 10
- Inventory holding cost (per unit per quarter): 5 for all products

**Initial conditions:** Inventory = 0, backorder = 0 for all products at start of Q1.

**End-of-horizon conditions (end of Q4):**
- Inventory = exactly 150 for each product
- Backorder = 0 for each product

**Key rules:**
- Producing more than demand in a quarter → surplus becomes inventory (charged 5/unit/quarter at end of each quarter it is held, including Q4).
- Producing less than demand → shortfall becomes backorder (charged delay rate per unit per quarter at end of each quarter it is outstanding).
- A product cannot be in both inventory and backorder in the same quarter (mutually exclusive states).
- Backorders must be made up in later quarters (carried forward).
- Production quantities must be integers (whole units).
- No other cost components (no production cost, no labor cost).

**Decision variables:** Production quantity of each product in each quarter (integer, non-negative).

**Objective:** Minimize total delay compensation cost + total inventory holding cost over 4 quarters.