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

QUESTION: When you say "maximize total revenue," do you mean net profit (total sales revenue minus total purchase cost), or literally just total sales revenue (ignoring what you pay to buy)?

## Turn 1 - User Simulator

I mean net profit: total sales revenue minus total purchase cost.

## Turn 2 - Generic Agent

QUESTION: Is there a limit on how many units you can purchase in any given month, or can you buy as many units as you want at that month's buy price?

## Turn 2 - User Simulator

There is no limit on how many units can be purchased in any given month, other than the warehouse capacity constraint.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on how many units you can sell in any given month, or can you sell as many units as you want at that month's sell price?

## Turn 3 - User Simulator

There is no limit on how many units can be sold in any given month, other than the inventory available in the warehouse.

## Turn 4 - Generic Agent

QUESTION: At the end of December, does the remaining inventory have any value (e.g., it can be carried over and counted as worth something), or is it simply leftover with no value in the objective?

## Turn 4 - User Simulator

The remaining inventory at the end of December has no value in the objective.

## Turn 5 - Generic Agent

QUESTION: Is the warehouse capacity limit of 500 units a constraint on the inventory level at the end of each month (after that month's purchases and sales), or on the inventory at any point during the month?

## Turn 5 - User Simulator

The 500-unit limit applies to the inventory level at the end of each month, after that month's purchases and sales.

## Turn 6 - Generic Agent

QUESTION: Can the inventory level at the end of any month be zero or negative, or must you always keep at least some minimum stock in the warehouse?

## Turn 6 - User Simulator

The inventory level at the end of any month can be zero, but it cannot be negative.

## Turn 7 - Generic Agent

QUESTION: Are the purchase and sales quantities required to be whole numbers (you can't buy or sell a fraction of a unit), or can they be any real number?

## Turn 7 - User Simulator

The purchase and sales quantities must be whole numbers.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint linking purchases and sales within the same month, such as a requirement that you must sell at least as much as you buy, or that sales can only come from beginning inventory (not from the same month's purchases)?

## Turn 8 - User Simulator

There is no constraint linking purchases and sales within the same month. Sales can come from both beginning inventory and the same month's purchases.

## Turn 9 - Generic Agent

QUESTION: Is there any minimum purchase requirement, such as you must buy at least a certain number of units each month, or can you choose to buy zero units in a given month?

## Turn 9 - User Simulator

You can choose to buy zero units in a given month.

## Turn 10 - Generic Agent

QUESTION: Is there any minimum sales requirement, such as you must sell at least a certain number of units each month, or can you choose to sell zero units in a given month?

## Turn 10 - User Simulator

You can choose to sell zero units in a given month.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize net profit over July–December, where net profit = total sales revenue − total purchase cost.

**Decision variables (per month m = 7, 8, 9, 10, 11, 12):**
- x_m = units purchased in month m (non-negative integer)
- y_m = units sold in month m (non-negative integer)
- I_m = inventory at the end of month m (non-negative integer)

**Parameters:**
- Buy prices: [28, 24, 25, 27, 23, 23]
- Sell prices: [29, 24, 26, 28, 22, 25]
- Initial inventory (end of June): 200 units
- Warehouse capacity: 500 units

**Constraints:**
1. Inventory balance: I_m = I_{m−1} + x_m − y_m for each month (with I_6 = 200)
2. Capacity: I_m ≤ 500 for each month
3. Non-negativity: x_m ≥ 0, y_m ≥ 0, I_m ≥ 0 for all months
4. Integrality: all variables are integers
5. No per-month purchase or sales limits beyond inventory availability
6. No minimum purchase or sales requirement
7. End-of-December inventory has no value in the objective
8. No intra-month linkage between purchases and sales (sales can use same-month purchases)