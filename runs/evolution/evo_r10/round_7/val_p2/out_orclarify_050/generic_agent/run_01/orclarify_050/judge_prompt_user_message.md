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

QUESTION: In this plan, is the amount you can buy in each month unlimited (you may purchase any quantity at that month's buy price), or is there a maximum purchase quantity per month?

## Turn 1 - User Simulator

There is no maximum purchase quantity per month. You may purchase any quantity at that month's buy price.

## Turn 2 - Generic Agent

QUESTION: When you sell units in a month, is the quantity you can sell limited by the stock available in the warehouse at the start of that month (i.e., you cannot sell more than you have on hand), or is there any other rule governing how much can be sold each month?

## Turn 2 - User Simulator

The quantity you can sell in a month is limited by the stock available in the warehouse. You cannot sell more than you have on hand.

## Turn 3 - Generic Agent

QUESTION: The warehouse capacity limit of 500 units — does it apply to the stock level at the end of each month (after that month's purchases and sales are settled), or to the stock at the beginning of each month?

## Turn 3 - User Simulator

The warehouse capacity limit of 500 units applies to the stock level at the end of each month, after that month's purchases and sales are settled.

## Turn 4 - Generic Agent

QUESTION: For the objective of maximizing total revenue over the six months, is "total revenue" the total sales revenue (sum of units sold times the sell price each month) minus the total purchase cost (sum of units bought times the buy price each month), i.e., net profit, or is it just the gross sales revenue without subtracting purchase costs?

## Turn 4 - User Simulator

"Total revenue" in this context means net profit: the total sales revenue (sum of units sold times the sell price each month) minus the total purchase cost (sum of units bought times the buy price each month).

## Turn 5 - Generic Agent

QUESTION: At the end of December, is there any requirement or value attached to the remaining stock in the warehouse (for example, it must be zero, or it earns some salvage value), or is leftover stock simply free with no cost or benefit?

## Turn 5 - User Simulator

Leftover stock at the end of December is simply free with no cost or benefit.

## Turn 6 - Generic Agent

QUESTION: In a given month, can you both buy and sell units (i.e., purchases and sales in the same month are allowed and independent), or is there a rule that restricts buying and selling in the same month?

## Turn 6 - User Simulator

You can both buy and sell units in the same month. Purchases and sales in the same month are allowed and independent.

## Turn 7 - Generic Agent

QUESTION: Are the purchase and sale quantities in each month required to be whole numbers (integer units), or can they be fractional (continuous) quantities?

## Turn 7 - User Simulator

The purchase and sale quantities in each month are required to be whole numbers (integer units).

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** 6 months, July through December (months 7–12).
- **Decisions (per month):** purchase quantity (integer, ≥ 0, unbounded above) and sale quantity (integer, ≥ 0).
- **Initial stock:** 200 units at the end of June (start of July).
- **Inventory balance:** end-of-month stock = previous end-of-month stock + purchases − sales.
- **Sales constraint:** sales in a month cannot exceed stock available on hand (i.e., end-of-month stock must be ≥ 0).
- **Capacity constraint:** end-of-month stock (after that month's purchases and sales) must not exceed 500 units, for each of the six months.
- **Same-month buying and selling:** allowed and independent.
- **Objective:** maximize net profit = Σ(units sold × sell price) − Σ(units bought × buy price) over the six months.
- **End-of-December leftover stock:** free, no cost or salvage value.
- **Prices (Table 1-21):**
  - Buy: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25

I will now formulate the integer linear program.