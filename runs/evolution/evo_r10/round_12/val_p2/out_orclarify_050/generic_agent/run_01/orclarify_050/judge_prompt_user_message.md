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

QUESTION: Is there a limit on how many units can be purchased in any single month (a monthly purchase budget or supplier cap), or can you buy any non-negative quantity at that month's buy price?

## Turn 1 - User Simulator

There is no limit on how many units can be purchased in any single month. You can buy any non-negative quantity at that month's buy price.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units can be sold in a given month (such as a monthly demand cap), or can you sell any non-negative quantity up to what you have in stock?

## Turn 2 - User Simulator

There is no limit on how many units can be sold in a given month. You can sell any non-negative quantity up to what you have in stock.

## Turn 3 - Generic Agent

QUESTION: At the end of December, must the warehouse be empty (all stock sold), or is it acceptable to have leftover inventory remaining?

## Turn 3 - User Simulator

It is acceptable to have leftover inventory remaining at the end of December.

## Turn 4 - Generic Agent

QUESTION: Is the warehouse capacity limit of 500 units checked at the end of each month (after that month's purchases and sales are settled), or must it also hold at every intermediate point within a month?

## Turn 4 - User Simulator

The warehouse capacity limit of 500 units is checked at the end of each month, after that month's purchases and sales are settled.

## Turn 5 - Generic Agent

QUESTION: Is the 500-unit capacity limit also required to hold at the end of December (i.e., the final leftover stock must be at most 500 units), or does the capacity constraint only apply to the end of months July through November?

## Turn 5 - User Simulator

The 500-unit capacity limit is required to hold at the end of December as well.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize total profit (total sales revenue minus total purchase costs), or literally total sales revenue only (ignoring what was paid to buy the units)?

## Turn 6 - User Simulator

The objective is to maximize total profit, which is total sales revenue minus total purchase costs.

## Turn 7 - Generic Agent

QUESTION: Are the buy and sell prices fixed constants for each month as shown in the table, or can they vary (for example, depending on the quantity bought or sold in that month)?

## Turn 7 - User Simulator

The buy and sell prices are fixed constants for each month as shown in the table.

## Turn 8 - Generic Agent

QUESTION: Can purchases and sales in a given month be any non-negative real (fractional) quantities, or must they be whole units?

## Turn 8 - User Simulator

Purchases and sales in a given month can be any non-negative real (fractional) quantities.

## Turn 9 - Generic Agent

QUESTION: Is the initial stock of 200 units at the end of June available to be sold in July (i.e., it counts toward July's available inventory), or is it locked and cannot be sold?

## Turn 9 - User Simulator

The initial stock of 200 units at the end of June is available to be sold in July.

## Turn 10 - Generic Agent

QUESTION: In a given month, is the sequence "buy first, then sell" (so you can sell units you just bought that same month), or "sell first, then buy" (so you can only sell from stock carried in from before)?

## Turn 10 - User Simulator

The sequence is "buy first, then sell," so you can sell units you just bought that same month.

## Turn 11 - Generic Agent

QUESTION: Is there any cost associated with holding inventory (such as a per-unit storage cost per month), or is holding inventory free?

## Turn 11 - User Simulator

Holding inventory is free. There is no cost associated with holding inventory.

## Turn 12 - Generic Agent

QUESTION: Is there any minimum stock level that must be maintained in the warehouse at the end of each month (a safety stock floor), or can the warehouse go down to zero units?

## Turn 12 - User Simulator

There is no minimum stock level that must be maintained. The warehouse can go down to zero units.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** 6 months, July through December.
- **Decision variables (per month m):** purchase quantity p_m ≥ 0 (real), sales quantity s_m ≥ 0 (real).
- **Prices (fixed constants):**
  - Buy: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25
- **Inventory balance:** I_m = I_{m-1} + p_m − s_m, with I_0 (end of June) = 200.
- **Capacity:** I_m ≤ 500 for every month m = Jul…Dec (checked at end of each month, including December).
- **Non-negativity:** I_m ≥ 0 (no minimum stock; warehouse may reach zero).
- **No purchase or sales caps:** p_m and s_m are unbounded above except by the inventory/capacity constraints.
- **Buy-then-sell within a month:** units bought in month m can be sold in month m (captured by the balance equation).
- **Leftover stock allowed** at end of December (subject to the 500 capacity).
- **Holding is free** (no storage cost).
- **Objective:** maximize total profit = Σ (sell_m · s_m) − Σ (buy_m · p_m) over the six months.

This is a linear program.