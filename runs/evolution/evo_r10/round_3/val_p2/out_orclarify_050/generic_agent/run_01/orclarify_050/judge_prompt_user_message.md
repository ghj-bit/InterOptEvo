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

QUESTION: When you say "maximize total revenue," do you mean net profit (total sales revenue minus total purchase cost), or literally just the sales revenue with purchases treated as a separate, non-deducted cost?

## Turn 1 - User Simulator

I mean net profit: total sales revenue minus total purchase cost.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units can be purchased or sold in a given month, or are those quantities unlimited as long as inventory stays within the 500-unit capacity?

## Turn 2 - User Simulator

There is no separate limit on monthly purchase or sale quantities. The only restriction is that inventory must not exceed the 500-unit warehouse capacity.

## Turn 3 - Generic Agent

QUESTION: At the end of December, does the remaining inventory have any value (e.g., it can be carried over and counted as salvage value in the objective), or is it simply leftover stock with no value in the profit calculation?

## Turn 3 - User Simulator

The remaining inventory at the end of December has no value in the profit calculation. It is simply leftover stock.

## Turn 4 - Generic Agent

QUESTION: Can inventory ever go negative (i.e., can you sell more in a month than you have on hand plus what you buy that month), or must inventory stay at zero or above every month?

## Turn 4 - User Simulator

Inventory must stay at zero or above every month. You cannot sell more than what you have on hand plus what you buy that month.

## Turn 5 - Generic Agent

QUESTION: Are purchase and sale quantities required to be whole numbers (integer units), or can they be fractional?

## Turn 5 - User Simulator

Purchase and sale quantities must be whole numbers (integer units).

## Turn 6 - Generic Agent

QUESTION: In a given month, does the purchase happen before or after the sale, and does the 500-unit capacity limit apply to the inventory level at the end of the month (after both purchase and sale), or must it also hold at every intermediate point within the month?

## Turn 6 - User Simulator

Purchases happen at the beginning of the month, before sales. The 500-unit capacity limit applies to the inventory level at the end of the month, after both purchase and sale.

## Turn 7 - Generic Agent

QUESTION: Since purchases happen at the beginning of the month before sales, does the 500-unit capacity limit also need to hold at the moment right after the purchase (before the sale), or is it only checked at the end of the month after the sale?

## Turn 7 - User Simulator

The 500-unit capacity limit must also hold at the moment right after the purchase, before the sale.

## Turn 8 - Generic Agent

QUESTION: Is there any requirement that a certain minimum amount of inventory must be on hand at the end of December, or is zero ending inventory perfectly acceptable?

## Turn 8 - User Simulator

There is no minimum inventory requirement at the end of December. Zero ending inventory is perfectly acceptable.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** July through December (6 months).
- **Objective:** Maximize net profit = total sales revenue − total purchase cost over the six months.
- **Decision variables:** For each month, the number of units purchased (integer, ≥ 0) and the number of units sold (integer, ≥ 0). No separate upper bound on either; the only binding restriction is warehouse capacity.
- **Inventory dynamics:**
  - Initial stock at end of June: 200 units.
  - Within a month, purchases occur first, then sales.
  - Inventory at end of month = inventory at start of month + purchases − sales.
  - Inventory must be ≥ 0 at all times (cannot sell more than on-hand + purchases).
- **Capacity constraints:**
  - Warehouse capacity: 500 units.
  - The 500-unit limit must hold both (a) immediately after the purchase (before the sale) and (b) at the end of the month (after the sale).
- **Prices (per unit):**
  - Buy: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23.
  - Sell: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25.
- **End of horizon:** Remaining inventory at end of December has no value; no minimum ending inventory required.
- **Integrality:** All purchase and sale quantities are non-negative integers.