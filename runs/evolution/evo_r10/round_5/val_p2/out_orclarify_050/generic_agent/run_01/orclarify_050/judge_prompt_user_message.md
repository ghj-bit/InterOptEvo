# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U7, U8, U2, U3, U4
I need help creating a purchase and sales plan for a product from July to December. The purchase and selling prices for each month are as given in Table 1-21. Inventory in the warehouse must not exceed its capacity, and the objective is to maximize total revenue over the six months.

Initial stock at the end of June: 200 units.

Warehouse capacity limit: 500 units.

Table 1-21:
| Month | 7  | 8  | 9  | 10 | 11 | 12 |
|-------|----|----|----|----|----|----|
| Buy   | 28 | 24 | 25 | 27 | 23 | 23 |
| Sell  | 29 | 24 | 26 | 28 | 22 | 25 |

## Problem units
- U1 (context): I need help creating a purchase and sales plan for a product from July to December.
- U2 (data): Initial stock at the end of June: 200 units.
- U3 (data): Warehouse capacity limit: 500 units.
- U4 (data): Table 1-21:
| Month | 7  | 8  | 9  | 10 | 11 | 12 |
|-------|----|----|----|----|----|----|
| Buy   | 28 | 24 | 25 | 27 | 23 | 23 |
| Sell  | 29 | 24 | 26 | 28 | 22 | 25 |
- U5 (assumption): Purchases are made at the beginning of each month.
- U6 (assumption): The purchase and selling prices for each month are as given in Table 1-21.
- U7 (constraint): Inventory in the warehouse must not exceed its capacity.
- U8 (objective): Maximize total revenue over the six months.

## Hidden slot scoring rules
## H1: purchase_at_month_start
- Severity: P1
- Severity reason: Without knowing when purchases occur relative to the sales period, the inventory capacity constraint cannot be correctly applied, potentially violating the capacity limit in practice.
- Problem unit ID: U5
- Semantic hit rule: The Agent's question must explicitly ask about the timing of purchases within the month (e.g., beginning of month, start of month, or when purchases are made).
- Reference acceptable questions:
  - Do purchases occur at the beginning of each month before any sales are made?
  - When exactly during the month do we purchase? At the start or end of the month?
- Failure modes:
  - Assuming purchases are made at the end of the month, which would change inventory peaks and may violate the true capacity limit.
  - Assuming the timing of purchases is irrelevant and using an aggregate monthly inventory balance without considering intra-month capacity.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When you say "maximize total revenue," do you mean to maximize total sales revenue (sum of sell price × units sold) only, or to maximize net profit (total sales revenue minus total purchase cost)?

## Turn 1 - User Simulator

I mean to maximize total sales revenue only (sum of sell price × units sold).

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units can be purchased or sold in a given month, or are those quantities unlimited as long as inventory stays within the 500-unit capacity?

## Turn 2 - User Simulator

There is no limit on how many units can be purchased or sold in a given month, as long as inventory stays within the 500-unit capacity.

## Turn 3 - Generic Agent

QUESTION: At the end of December, does the remaining inventory have any value (e.g., it can be carried over and counted), or is it simply leftover stock with no benefit or penalty?

## Turn 3 - User Simulator

The remaining inventory at the end of December is simply leftover stock with no benefit or penalty.

## Turn 4 - Generic Agent

QUESTION: Can the warehouse inventory ever go negative (i.e., can you sell more in a month than you have on hand plus what you buy that month), or must inventory stay at zero or above in every month?

## Turn 4 - User Simulator

Inventory must stay at zero or above in every month.

## Turn 5 - Generic Agent

QUESTION: For the inventory balance in each month, does the purchase happen before the sale (so you can sell units bought in the same month), or does the sale happen before the purchase (so you can only sell from stock carried in from the previous month)?

## Turn 5 - User Simulator

The purchase happens before the sale, so you can sell units bought in the same month.

## Turn 6 - Generic Agent

QUESTION: Is the 500-unit warehouse capacity limit checked at the end of each month (after purchases and sales), or must it also hold at all intermediate points within a month (e.g., right after purchasing, before selling)?

## Turn 6 - User Simulator

The 500-unit warehouse capacity limit is checked at the end of each month, after purchases and sales.

## Turn 7 - Generic Agent

QUESTION: Are the purchase and sale quantities in each month required to be whole numbers (integer units), or can they be fractional?

## Turn 7 - User Simulator

The purchase and sale quantities in each month are required to be whole numbers (integer units).

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** July through December (6 months).
- **Objective:** Maximize total sales revenue = sum over months of (sell price × units sold). Purchase cost is NOT subtracted.
- **Decision variables (per month):** units purchased (integer, ≥ 0) and units sold (integer, ≥ 0). No per-month upper bound on purchases or sales.
- **Inventory balance:** Inventory must stay ≥ 0 in every month. Purchase happens before sale, so units bought in a month can be sold in that same month.
  - End-of-month inventory = previous month's end inventory + purchases − sales.
- **Initial stock:** 200 units at the end of June (start of July).
- **Capacity:** End-of-month inventory (after purchases and sales) must not exceed 500 units in each month.
- **End of December:** Remaining inventory is leftover with no benefit or penalty (not counted in the objective).
- **Prices (Table 1-21):**
  - Buy: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25
- **Model class:** Integer linear program (all variables integer, all constraints linear).