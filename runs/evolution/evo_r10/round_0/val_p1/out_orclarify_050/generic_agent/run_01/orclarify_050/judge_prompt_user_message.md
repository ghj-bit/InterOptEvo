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

QUESTION: When you sell units in a given month, do they have to come from the stock on hand at the start of that month (i.e., you cannot sell units you purchase in the same month), or can units bought in a month also be sold in that same month?

## Turn 2 - User Simulator

Units bought in a month can also be sold in that same month.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum stock level that must be kept in the warehouse at the end of each month (a safety stock requirement), or is it acceptable for the warehouse to be empty (0 units) at month-end?

## Turn 3 - User Simulator

There is no minimum stock level requirement. It is acceptable for the warehouse to be empty (0 units) at month-end.

## Turn 4 - Generic Agent

QUESTION: Is there any requirement on the stock level at the end of December (end of the planning horizon), or is it fine to end with whatever stock remains, including zero?

## Turn 4 - User Simulator

There is no specific requirement on the stock level at the end of December. It is fine to end with whatever stock remains, including zero.

## Turn 5 - Generic Agent

QUESTION: When you say "maximize total revenue," do you mean maximize total sales revenue (sell price × units sold) only, or maximize net profit (sales revenue minus purchase cost)?

## Turn 5 - User Simulator

Maximize total sales revenue (sell price × units sold) only.

## Turn 6 - Generic Agent

QUESTION: Are the purchase and sales quantities required to be whole numbers (integer units), or can they be treated as continuous (fractional units allowed)?

## Turn 6 - User Simulator

The purchase and sales quantities are required to be whole numbers (integer units).

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** 6 months, July through December (months 1–6).
- **Decision variables (per month m):**
  - `x_m` = units purchased in month m (integer, ≥ 0, no upper bound).
  - `s_m` = units sold in month m (integer, ≥ 0).
  - `I_m` = inventory at the end of month m (integer, ≥ 0).
- **Prices (Table 1-21):**
  - Buy:  Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell:  Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25
- **Inventory balance (per month):** `I_m = I_{m-1} + x_m − s_m`, with `I_0 = 200` (initial stock at end of June). Units bought in a month may be sold in the same month.
- **Capacity constraint:** `I_m ≤ 500` for every month m.
- **No minimum stock** at any month-end; ending December stock is free (can be 0).
- **Objective:** Maximize total sales revenue = Σ_m (sell price_m × s_m). Purchase cost is NOT subtracted.
- **Integrality:** All decision variables are non-negative integers.

Note: Since the objective rewards selling as much as possible and there is no purchase limit, the model will buy enough to sell whenever the sell price is attractive, subject only to the 500-unit capacity cap on ending inventory.