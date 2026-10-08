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

QUESTION: When you say "maximize total revenue," do you mean net profit (total sales revenue minus total purchase costs), or gross sales revenue only (ignoring what you pay to buy the units)?

## Turn 1 - User Simulator

I mean net profit: total sales revenue minus total purchase costs.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units can be purchased or sold in a single month, or are those quantities only constrained by the warehouse capacity and the inventory balance?

## Turn 2 - User Simulator

There is no separate limit on monthly purchase or sale quantities. They are only constrained by the warehouse capacity and the inventory balance.

## Turn 3 - Generic Agent

QUESTION: At the end of December, does the remaining inventory have any value (e.g., it can be carried over and counted as worth the December sell price, or it has a salvage value), or is it simply leftover with no value in the objective?

## Turn 3 - User Simulator

The remaining inventory at the end of December is simply leftover with no value in the objective.

## Turn 4 - Generic Agent

QUESTION: Is the warehouse capacity limit of 500 units a constraint on the inventory level at the end of each month (after that month's purchases and sales are settled), or does it also apply to the inventory level at the beginning of each month?

## Turn 4 - User Simulator

The 500-unit limit applies to the inventory level at the end of each month, after that month's purchases and sales are settled.

## Turn 5 - Generic Agent

QUESTION: Are purchase and sale quantities required to be whole units (integers), or can they be fractional?

## Turn 5 - User Simulator

Purchase and sale quantities must be whole units (integers).

## Turn 6 - Generic Agent

QUESTION: Can the warehouse inventory ever go negative (i.e., can you sell more in a month than you have on hand plus what you buy that month), or must inventory always stay at zero or above?

## Turn 6 - User Simulator

Inventory must always stay at zero or above.

## Turn 7 - Generic Agent

QUESTION: Is the initial stock of 200 units at the end of June already in the warehouse and available for sale in July, or does it arrive at some other time?

## Turn 7 - User Simulator

The 200 units are already in the warehouse and available for sale in July.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 6 months, July through December.
- **Decision variables:** For each month, the number of units purchased (integer, ≥ 0) and the number of units sold (integer, ≥ 0). No separate upper bounds on these; they are limited only by inventory balance and warehouse capacity.
- **Inventory balance:** Inventory at the end of month t = inventory at the end of month t−1 + purchases in month t − sales in month t. Initial inventory (end of June) = 200 units, available in July.
- **Inventory constraints:** Inventory at the end of every month must be ≥ 0 and ≤ 500 (the 500-unit capacity applies to end-of-month levels).
- **Objective:** Maximize net profit = (sum over all months of sell price × units sold) − (sum over all months of buy price × units purchased).
- **End of December:** Remaining inventory has no value in the objective (no salvage, no carry-over credit).
- **Prices (Table 1-21):**
  - Buy: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25

All quantities are integers.