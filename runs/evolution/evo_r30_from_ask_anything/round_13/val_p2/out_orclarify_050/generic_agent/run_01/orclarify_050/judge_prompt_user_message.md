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

QUESTION: Is the objective to maximize total profit (revenue from sales minus cost of purchases) or to maximize total sales revenue only, ignoring purchase costs?

## Turn 1 - User Simulator

The objective is to maximize total revenue over the six months.

## Turn 2 - Generic Agent

QUESTION: Is there a limit on how many units can be purchased in any single month, or is the only constraint on inventory the 500-unit warehouse capacity?

## Turn 2 - User Simulator

The only constraint on inventory is the 500-unit warehouse capacity.

## Turn 3 - Generic Agent

QUESTION: Is there a limit on how many units can be sold in any single month, or can you sell any quantity up to the available inventory?

## Turn 3 - User Simulator

You can sell any quantity up to the available inventory.

## Turn 4 - Generic Agent

QUESTION: Is there a limit on how many units can be purchased in any single month, or can you buy any quantity as long as the resulting inventory stays within the 500-unit capacity?

## Turn 4 - User Simulator

You can buy any quantity as long as the resulting inventory stays within the 500-unit capacity.

## Turn 5 - Generic Agent

QUESTION: Does the 500-unit warehouse capacity limit apply to the inventory level at the end of each month (after that month's purchases and sales are settled), or does it also constrain the inventory level at any point during the month?

## Turn 5 - User Simulator

The 500-unit warehouse capacity limit applies to the inventory level at the end of each month.

## Turn 6 - Generic Agent

QUESTION: Is there a minimum inventory level that must be maintained at the end of each month, or can inventory drop to zero?

## Turn 6 - User Simulator

Inventory can drop to zero.

## Turn 7 - Generic Agent

QUESTION: Is there a requirement to end December with a specific inventory level, or can the ending inventory in December be any value from zero to 500?

## Turn 7 - User Simulator

The ending inventory in December can be any value from zero to 500.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Maximize total sales revenue over the six months (July–December). Purchase costs are not subtracted from the objective.
- **Decision Variables:** For each month m ∈ {7, 8, 9, 10, 11, 12}, choose:
  - Purchase quantity P_m ≥ 0 (continuous)
  - Sales quantity S_m ≥ 0 (continuous)
- **Inventory Balance:** I_m = I_{m-1} + P_m − S_m, where I_6 = 200 (initial stock at end of June).
- **Inventory Capacity Constraint:** I_m ≤ 500 for each month m ∈ {7, 8, 9, 10, 11, 12}.
- **Non-negativity:** I_m ≥ 0, P_m ≥ 0, S_m ≥ 0 for all months.
- **No other constraints:** No minimum inventory, no purchase or sales caps beyond inventory availability, no requirement on ending December inventory (can be 0 to 500).
- **Prices (per unit):**
  - Buy: 28, 24, 25, 27, 23, 23
  - Sell: 29, 24, 26, 28, 22, 25
- **Revenue:** Sum over months of (Sell price_m × S_m). Purchase costs do not enter the objective.

**Assumptions (none critical — all key facts confirmed):**
- All quantities are continuous (not required to be integer).
- No holding cost or storage fee is incurred.
- No spoilage or obsolescence of inventory.