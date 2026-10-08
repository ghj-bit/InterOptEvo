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

QUESTION: When you say "maximize total revenue," do you mean (a) maximize total sales revenue only (sum of sell price × units sold, ignoring purchase cost), (b) maximize net profit (sales revenue minus purchase cost), or (c) maximize net cash flow including the value of any leftover inventory at the end of December?

## Turn 1 - User Simulator

I mean (b) maximize net profit (sales revenue minus purchase cost).

## Turn 2 - Generic Agent

QUESTION: Is there a limit on how many units can be purchased in any single month (e.g., a monthly purchase budget or supplier cap), or can you buy any non-negative quantity each month as long as the resulting warehouse inventory stays within the 500-unit capacity?

## Turn 2 - User Simulator

There is no limit on how many units can be purchased in any single month. You can buy any non-negative quantity each month as long as the resulting warehouse inventory stays within the 500-unit capacity.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on how many units can be sold in any single month (e.g., a monthly demand cap), or can you sell any non-negative quantity each month as long as you have enough inventory available?

## Turn 3 - User Simulator

There is no limit on how many units can be sold in any single month. You can sell any non-negative quantity each month as long as you have enough inventory available.

## Turn 4 - Generic Agent

QUESTION: At the end of December, is any leftover inventory in the warehouse worth anything (e.g., valued at the December sell price or some salvage value), or is it simply worthless and only the six months of sales revenue and purchase costs count toward profit?

## Turn 4 - User Simulator

Leftover inventory at the end of December is simply worthless. Only the six months of sales revenue and purchase costs count toward profit.

## Turn 5 - Generic Agent

QUESTION: In the inventory balance for each month, does the warehouse capacity limit of 500 units apply to the inventory at the end of the month (after that month's purchases and sales are settled), or to the inventory at the beginning of the month before any transactions?

## Turn 5 - User Simulator

The warehouse capacity limit of 500 units applies to the inventory at the end of the month, after that month's purchases and sales are settled.

## Turn 6 - Generic Agent

QUESTION: Can purchases and sales in a given month be fractional (e.g., 150.5 units), or must all purchase and sale quantities be whole units?

## Turn 6 - User Simulator

All purchase and sale quantities must be whole units.

## Turn 7 - Generic Agent

QUESTION: Is there any constraint that you must sell at least some minimum quantity each month (e.g., a contractual minimum), or can you choose to sell zero units in a month if that is optimal?

## Turn 7 - User Simulator

There is no minimum quantity constraint. You can choose to sell zero units in a month if that is optimal.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** 6 months, July through December (months 1–6).
- **Decision variables (all non-negative integers):**
  - `x_t` = units purchased in month t
  - `y_t` = units sold in month t
  - `I_t` = inventory at the end of month t
- **Data (Table 1-21):**
  - Buy prices: July 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell prices: July 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25
- **Initial condition:** Inventory at end of June (start of July) = 200 units.
- **Inventory balance:** `I_t = I_{t-1} + x_t - y_t` for each month t, with `I_0 = 200`.
- **Capacity constraint:** `I_t ≤ 500` for each month t (end-of-month inventory).
- **No purchase cap, no sales cap, no minimum sales** — only the inventory balance and capacity bind.
- **Objective:** Maximize net profit = Σ (sell price_t × y_t) − Σ (buy price_t × x_t) over the six months.
- **Leftover inventory at end of December is worthless** — no salvage term.
- **Integrality:** All purchase, sale, and inventory quantities are whole units (integers).