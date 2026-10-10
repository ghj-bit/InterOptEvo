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

QUESTION: Is there a minimum required inventory level at the end of December that must be met?

## Turn 1 - User Simulator

No, there is no minimum required inventory level at the end of December.

## Turn 2 - Generic Agent

QUESTION: Is there a limit on the maximum number of units that can be purchased in any single month?

## Turn 2 - User Simulator

No, there is no limit on the maximum number of units that can be purchased in any single month.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on the maximum number of units that can be sold in any single month?

## Turn 3 - User Simulator

No, there is no limit on the maximum number of units that can be sold in any single month.

## Turn 4 - Generic Agent

QUESTION: Is there a minimum required inventory level at the end of any month during the planning period (July through December)?

## Turn 4 - User Simulator

No, there is no minimum required inventory level at the end of any month during the planning period.

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize total profit (revenue minus purchase costs) or strictly total revenue from sales?

## Turn 5 - User Simulator

The objective is to maximize total revenue over the six months.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:
- Planning horizon: July through December (6 months).
- Decision variables: Units to purchase and units to sell in each month.
- Initial inventory (end of June): 200 units.
- Warehouse capacity: Inventory at the end of each month must not exceed 500 units.
- No minimum inventory requirements at the end of any month.
- No upper limits on monthly purchases or sales.
- Purchase and selling prices are as given in Table 1-21.
- Objective: Maximize total revenue from sales over the six months (purchase costs are not subtracted from the objective).
- Inventory balance: Ending inventory for a month = Beginning inventory + Purchases - Sales.