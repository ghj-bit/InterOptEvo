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

QUESTION: When you say "maximize total revenue," do you mean (a) maximize total sales revenue only (sum of sell price × units sold, ignoring purchase costs), or (b) maximize net profit (total sales revenue minus total purchase costs)?

## Turn 1 - User Simulator

I mean (b) maximize net profit (total sales revenue minus total purchase costs).

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how many units can be purchased or sold in a given month (e.g., a monthly purchase budget or a monthly sales demand cap), or are the only constraints the warehouse capacity of 500 units and non-negativity?

## Turn 2 - User Simulator

The only constraints are the warehouse capacity of 500 units and non-negativity. There are no monthly purchase budgets or sales demand caps.

## Turn 3 - Generic Agent

QUESTION: Regarding the December ending inventory: is there any requirement about what the warehouse stock should be at the end of December (for example, it must be zero, or it must be at least some minimum level), or is any leftover stock at the end of December simply allowed with no penalty or requirement?

## Turn 3 - User Simulator

Any leftover stock at the end of December is simply allowed with no penalty or requirement.

## Turn 4 - Generic Agent

QUESTION: Are the purchase and sales quantities required to be whole numbers (integer units), or can they be fractional?

## Turn 4 - User Simulator

The purchase and sales quantities are required to be whole numbers (integer units).

## Turn 5 - Generic Agent

QUESTION: For the inventory balance, is the warehouse capacity limit of 500 units applied to the stock at the end of each month (after that month's purchases and sales are settled), or to the stock at the beginning of each month?

## Turn 5 - User Simulator

The warehouse capacity limit of 500 units is applied to the stock at the end of each month, after that month's purchases and sales are settled.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Planning horizon:** 6 months, July (t=1) through December (t=6).
- **Decision variables (all integer, non-negative):**
  - x_t = units purchased in month t
  - s_t = units sold in month t
  - I_t = inventory at the end of month t
- **Data (Table 1-21):**
  - Buy prices: Jul 28, Aug 24, Sep 25, Oct 27, Nov 23, Dec 23
  - Sell prices: Jul 29, Aug 24, Sep 26, Oct 28, Nov 22, Dec 25
- **Initial condition:** I_0 (end of June) = 200 units.
- **Inventory balance:** I_t = I_{t-1} + x_t − s_t, for t = 1..6.
- **Capacity constraint:** I_t ≤ 500 for each month t = 1..6 (end-of-month stock).
- **Non-negativity / integrality:** x_t, s_t, I_t ≥ 0 and integer for all t.
- **No other constraints:** no monthly purchase budget, no sales demand cap, no minimum or required ending stock in December (leftover stock is free).
- **Objective:** maximize net profit = Σ_t (sell_price_t × s_t) − Σ_t (buy_price_t × x_t).