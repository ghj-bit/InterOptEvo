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

QUESTION: Is there a limit on how many units can be purchased in any single month (a monthly purchase budget or supplier cap), or can you buy any quantity you want at that month's purchase price?

## Turn 1 - User Simulator

There is no limit on how many units can be purchased in any single month. You can buy any quantity you want at that month's purchase price.

## Turn 2 - Generic Agent

QUESTION: Is there a limit on how many units can be sold in any single month (a monthly sales demand cap), or can you sell any quantity you want at that month's selling price?

## Turn 2 - User Simulator

There is no limit on how many units can be sold in any single month. You can sell any quantity you want at that month's selling price.

## Turn 3 - Generic Agent

QUESTION: When you say "maximize total revenue," do you mean maximize total sales revenue (selling price times units sold) only, or maximize net profit (sales revenue minus purchase costs)?

## Turn 3 - User Simulator

Maximize total sales revenue (selling price times units sold) only.

## Turn 4 - Generic Agent

QUESTION: At the end of December, does the leftover inventory in the warehouse have any value (e.g., it carries over into January and counts toward the objective), or is it simply leftover with no value?

## Turn 4 - User Simulator

The leftover inventory at the end of December is simply leftover with no value.

## Turn 5 - Generic Agent

QUESTION: Can the warehouse inventory ever go negative (i.e., can you sell more in a month than you have on hand plus what you buy that month), or must inventory stay at zero or above at the end of every month?

## Turn 5 - User Simulator

Inventory must stay at zero or above at the end of every month.

## Turn 6 - Generic Agent

QUESTION: When you buy units in a given month, can those units be sold in that same month, or must purchased units wait until the following month to be sold?

## Turn 6 - User Simulator

Purchased units can be sold in that same month.

## Turn 7 - Generic Agent

QUESTION: Are the purchase and sale quantities required to be whole numbers (integer units), or can they be any fractional amount?

## Turn 7 - User Simulator

The purchase and sale quantities are required to be whole numbers (integer units).

## Turn 8 - Generic Agent

QUESTION: Is the warehouse capacity limit of 500 units checked at the end of each month (after that month's purchases and sales are settled), or must it also hold at every point during the month?

## Turn 8 - User Simulator

The warehouse capacity limit of 500 units is checked at the end of each month, after that month's purchases and sales are settled.

## Turn 9 - Generic Agent

QUESTION: Is the initial stock of 200 units at the end of June already within the 500-unit capacity, and does the 500-unit limit apply to the end-of-month inventory for all six months (July through December) including December?

## Turn 9 - User Simulator

Yes, the initial stock of 200 units is within the 500-unit capacity. The 500-unit limit applies to the end-of-month inventory for all six months, July through December, including December.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** Six months, July through December.
- **Decision variables (per month m):**
  - x_m = units purchased in month m (integer, ≥ 0, no upper bound)
  - s_m = units sold in month m (integer, ≥ 0, no upper bound)
  - I_m = inventory at end of month m (integer, ≥ 0)
- **Prices (Table 1-21):**
  - Buy: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25
- **Objective:** Maximize total sales revenue = Σ_m (sell_price_m × s_m). Purchase costs are NOT subtracted.
- **Inventory balance (per month):** I_m = I_{m-1} + x_m − s_m, with I_6 (end of June) = 200.
- **Capacity:** I_m ≤ 500 for m = Jul…Dec (checked at end of each month, including December).
- **Non-negativity:** I_m ≥ 0 for all months; x_m, s_m ≥ 0.
- **Same-month flow:** Units bought in month m can be sold in month m (captured by the balance equation).
- **End of December:** Leftover inventory I_Dec has no value (not in objective, no salvage).
- **Integrality:** x_m, s_m, I_m are all integers.

This is a linear integer program. Because the objective only rewards selling and there is no purchase cap, the model will buy and sell in months where sell price exceeds buy price (Jul, Sep, Oct, Dec), and the capacity constraint will bind the amount that can be carried into high-margin months.