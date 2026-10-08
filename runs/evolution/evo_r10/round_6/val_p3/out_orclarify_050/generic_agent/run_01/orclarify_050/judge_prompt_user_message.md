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

QUESTION: When you say "maximize total revenue," do you mean to maximize total sales revenue only (sum of units sold × selling price), or to maximize net profit (total sales revenue minus total purchase cost)?

## Turn 1 - User Simulator

I mean to maximize total sales revenue only (sum of units sold × selling price).

## Turn 2 - Generic Agent

QUESTION: Is there a limit on how many units can be purchased in any given month, or can you buy any non-negative quantity at that month's purchase price?

## Turn 2 - User Simulator

There is no limit on how many units can be purchased in any given month, other than the warehouse capacity constraint.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on how many units can be sold in any given month, or can you sell any non-negative quantity (up to what's available) at that month's selling price?

## Turn 3 - User Simulator

There is no limit on how many units can be sold in any given month, other than what is available in inventory.

## Turn 4 - Generic Agent

QUESTION: At the end of December, does the leftover inventory in the warehouse have any value (e.g., it carries over to next year and should be counted), or is it simply discarded with no value?

## Turn 4 - User Simulator

The leftover inventory at the end of December is simply discarded with no value.

## Turn 5 - Generic Agent

QUESTION: Is there any requirement that the warehouse must be empty at the end of December, or is it fine to have leftover inventory (which is just discarded)?

## Turn 5 - User Simulator

It is fine to have leftover inventory at the end of December; it is simply discarded with no value.

## Turn 6 - Generic Agent

QUESTION: For the inventory balance each month, is the warehouse capacity of 500 units checked at the end of each month (after purchases and sales are settled), or at some other point during the month?

## Turn 6 - User Simulator

The warehouse capacity of 500 units is checked at the end of each month, after purchases and sales are settled.

## Turn 7 - Generic Agent

QUESTION: Can the number of units purchased or sold in a month be fractional, or must they be whole numbers (integers)?

## Turn 7 - User Simulator

The number of units purchased or sold in a month must be whole numbers (integers).

## Turn 8 - Generic Agent

QUESTION: Is there any minimum requirement that the warehouse must hold at least some number of units at the end of each month, or can inventory drop to zero?

## Turn 8 - User Simulator

There is no minimum requirement; inventory can drop to zero at the end of any month.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total sales revenue over July–December (sum of units sold × selling price for each month).

**Decision variables (all non-negative integers):**
- x_m = units purchased in month m
- y_m = units sold in month m
- I_m = inventory at the end of month m

**Parameters:**
- Initial inventory I_6 = 200
- Warehouse capacity = 500
- Purchase prices: [28, 24, 25, 27, 23, 23]
- Selling prices: [29, 24, 26, 28, 22, 25]

**Constraints:**
1. Inventory balance for each month m (July=1 … December=6):
   I_m = I_{m-1} + x_m − y_m
2. Warehouse capacity: I_m ≤ 500 for each month m
3. Non-negativity: x_m ≥ 0, y_m ≥ 0, I_m ≥ 0 for all m
4. Integrality: x_m, y_m, I_m are integers
5. No upper bound on purchases or sales other than what inventory/capacity implies
6. End-of-December inventory is discarded (no value, no requirement to be zero)

**Notes:**
- Revenue is sales revenue only (no subtraction of purchase costs)
- Capacity is checked at end of each month
- No minimum inventory requirement
- No per-month purchase or sales limits beyond availability