# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U18, U19, U20, U21, U22, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12, U13, U14, U15, U16, U17
I need help creating a production and human resources plan for a six-month period (January to June) for a foldable tables company, with the objective of maximizing total net profit. Unfulfilled demand from one month is back-ordered and must be met in subsequent months, and orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units. Total overtime hours per month for the entire workforce cannot exceed 20 hours per worker, and the ending inventory at the end of June must be at least 10,000 units.

Initial workforce at the start of January: 1,000 employees.

Initial inventory at the start of January: 15,000 units.

Sales price: 300 Yuan per unit sold.

Raw material cost: 90 Yuan per unit, applicable only to units produced in-house.

Outsourcing cost: 200 Yuan per unit for finished tables (all-inclusive).

Inventory holding cost: 15 Yuan per unit for inventory held at the end of a month.

Backorder cost: 35 Yuan per unit for unfulfilled demand carried over to the next month.

Labor requirement: each in-house unit requires 5 labor hours to produce.

Each worker provides 160 regular working hours per month.

Regular wage rate: 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization.

Overtime wage rate: 40 Yuan per hour.

Maximum overtime hours per worker per month: 20 hours.

Hiring cost per new worker: 5,000 Yuan.

Firing cost per worker: 8,000 Yuan.

Demand forecast (in units):
| Month | January | February | March | April | May | June |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demand | 20,000 | 40,000 | 42,000 | 35,000 | 19,000 | 18,500 |

Minimum ending inventory requirement: 10,000 units.

## Problem units
- U1 (context): I need help creating a production and human resources plan for a six-month period (January to June) for a foldable tables company.
- U2 (data): Initial workforce at the start of January: 1,000 employees.
- U3 (data): Initial inventory at the start of January: 15,000 units.
- U4 (data): Sales price: 300 Yuan per unit sold.
- U5 (data): Raw material cost: 90 Yuan per unit, applicable only to units produced in-house.
- U6 (data): Outsourcing cost: 200 Yuan per unit for finished tables (all-inclusive).
- U7 (data): Inventory holding cost: 15 Yuan per unit for inventory held at the end of a month.
- U8 (data): Backorder cost: 35 Yuan per unit for unfulfilled demand carried over to the next month.
- U9 (data): Labor requirement: each in-house unit requires 5 labor hours to produce.
- U10 (data): Each worker provides 160 regular working hours per month.
- U11 (data): Regular wage rate: 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization.
- U12 (data): Overtime wage rate: 40 Yuan per hour.
- U13 (data): Maximum overtime hours per worker per month: 20 hours.
- U14 (data): Hiring cost per new worker: 5,000 Yuan.
- U15 (data): Firing cost per worker: 8,000 Yuan.
- U16 (data): Demand forecast (in units):
| Month | January | February | March | April | May | June |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demand | 20,000 | 40,000 | 42,000 | 35,000 | 19,000 | 18,500 |
- U17 (data): Minimum ending inventory requirement: 10,000 units.
- U18 (objective): Maximize total net profit.
- U19 (constraint): Unfulfilled demand from one month is back-ordered and must be met in subsequent months.
- U20 (constraint): Orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units.
- U21 (constraint): Total overtime hours per month for the entire workforce cannot exceed 20 hours per worker.
- U22 (constraint): The ending inventory at the end of June must be at least 10,000 units.
- U23 (constraint): All backorders must be cleared by the end of June (ending backorders must be zero).

## Hidden slot scoring rules
## H1: ending_backorders_zero
- Severity: P1
- Severity reason: Without this terminal condition, the agent could model a scenario where backorders persist indefinitely beyond the planning horizon, resulting in a materially different (and likely invalid) profit-maximizing plan that does not force demand satisfaction.
- Problem unit ID: U23
- Semantic hit rule: The Agent's question must explicitly ask about a terminal condition on backorders, such as whether they must be zero at the end of June or whether all demand must be fulfilled by the end of the planning horizon.
- Reference acceptable questions:
  - At the end of June, do we need to clear all backorders so that nothing is left pending?
  - Is there a requirement that all customer demand must eventually be met by the end of the six‑month period, with no backorders carried forward afterward?
- Failure modes:
  - Silently assuming backorders can be carried forward indefinitely beyond the planning horizon
  - Assuming no end-of-horizon constraint on backorders, leading to a model that may leave some demand permanently unmet


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker per month (so total workforce overtime is 20 × number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime available in any given month is 20 hours multiplied by the number of workers on staff that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce, can you hire and/or fire workers in any month (including January), and is the workforce level for a month determined by the workers on staff during that month (i.e., hires/fires take effect within the same month they occur)?

## Turn 2 - User Simulator

Yes, you can hire and/or fire workers in any month, including January. The workforce level for a given month is determined by the workers on staff during that month, meaning hires and fires take effect within the same month they occur.

## Turn 3 - Generic Agent

QUESTION: For the regular wage, you said it is paid "regardless of utilization" — does this mean each worker on staff in a month is paid 160 × 30 = 4,800 Yuan for that month even if they work fewer than 160 regular hours (e.g., because production is low), so regular labor cost is simply 4,800 × (number of workers on staff that month)?

## Turn 3 - User Simulator

Yes, that is correct. Each worker on staff in a month is paid 4,800 Yuan for that month regardless of how many regular hours they actually work. So the regular labor cost for a month is simply 4,800 Yuan multiplied by the number of workers on staff that month.

## Turn 4 - Generic Agent

QUESTION: For the inventory/backorder balance, is the ending inventory at the end of a month allowed to be negative (representing backorders), or must inventory and backorders be tracked as two separate non-negative quantities where ending inventory is the leftover stock and backorders are the unmet demand carried forward?

## Turn 4 - User Simulator

Inventory and backorders must be tracked as two separate non-negative quantities. Ending inventory is the leftover stock, and backorders are the unmet demand carried forward. The ending inventory at the end of a month is not allowed to be negative.

## Turn 5 - Generic Agent

QUESTION: When fulfilling a month's orders (current demand plus backorders carried in), you said they are fulfilled using previous-month inventory, current in-house production, and outsourced units — is there any priority or restriction on which source is used first (e.g., must use inventory before producing/outsourcing), or can the model freely allocate among the three sources as long as total fulfillment equals total orders?

## Turn 5 - User Simulator

There is no priority or restriction on which source is used first. The model can freely allocate among previous-month inventory, current in-house production, and outsourced units, as long as the total fulfillment equals the total orders (current demand plus backorders carried in) for that month.

## Turn 6 - Generic Agent

QUESTION: For the sales price of 300 Yuan per unit sold — is revenue recognized on the units actually fulfilled/delivered in a month (i.e., current demand plus backorders that are met that month), or is it recognized on the original demand of that month regardless of when it is actually delivered?

## Turn 6 - User Simulator

Revenue is recognized on the units actually fulfilled/delivered in a month. That means it is based on the current demand plus any backorders that are met in that month, not on the original demand of that month regardless of when it is delivered.

## Turn 7 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit — is this charged on the number of units that are backordered at the end of each month (i.e., the backorder quantity carried into the next month), for every month including June, or only for months where the backorder is actually carried forward and later fulfilled?

## Turn 7 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the number of units that are backordered at the end of each month (i.e., the backorder quantity carried into the next month). This applies to every month where backorders exist at month-end, including June.

## Turn 8 - Generic Agent

QUESTION: Since backorders must be met in subsequent months and the horizon ends in June, is it required that all backorders be fully cleared by the end of June (i.e., ending backorder in June must be zero), or can some backorders remain unfulfilled at the end of June?

## Turn 8 - User Simulator

Yes, it is required that all backorders be fully cleared by the end of June. The ending backorder in June must be zero; no outstanding customer orders can remain after June.

## Turn 9 - Generic Agent

QUESTION: For the ending inventory requirement of at least 10,000 units at the end of June — does this 10,000 units need to be in addition to any units needed to fulfill June's demand and clear backorders, meaning it is the leftover stock after all June fulfillment, or is it a total stock level that includes units still to be delivered?

## Turn 9 - User Simulator

The 10,000 units is the leftover stock at the end of June, after all of June's demand and any backorders carried into June have been fulfilled. It is in addition to the units needed for fulfillment, not a total stock level that includes units still to be delivered.

## Turn 10 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit — is it incurred only on units produced in-house (as you stated), and is there any separate raw material cost for outsourced units, or is the 200 Yuan outsourcing cost fully all-inclusive with no additional material cost?

## Turn 10 - User Simulator

The 90 Yuan raw material cost is incurred only on units produced in-house. The 200 Yuan outsourcing cost is fully all-inclusive, with no additional raw material cost for outsourced units.

## Turn 11 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit — is it charged on the ending inventory at the end of each month (including June), or only on the ending inventory for months January through May (excluding June)?

## Turn 11 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory at the end of each month, including June.

## Turn 12 - Generic Agent

QUESTION: Are there any constraints on the workforce size, such as a maximum number of workers the company can employ in any month, or a minimum workforce level that must be maintained?

## Turn 12 - User Simulator

There are no constraints on the workforce size. There is no maximum number of workers the company can employ in any month, and there is no minimum workforce level that must be maintained.

## Turn 13 - Generic Agent

QUESTION: For the in-house production labor, is the total labor hours used in a month (regular hours worked plus overtime hours) allowed to exceed the total available hours (160 regular + 20 overtime per worker), or must total labor hours used be at most the total available hours for the workforce that month?

## Turn 13 - User Simulator

Total labor hours used in a month must be at most the total available hours for the workforce that month. The total available hours are 160 regular hours plus 20 overtime hours per worker, so the total labor hours used cannot exceed 180 hours per worker for that month.

## Turn 14 - Generic Agent

QUESTION: For the overtime cost — is overtime cost incurred only on the overtime hours actually used (i.e., 40 Yuan per overtime hour actually worked), or is there any fixed overtime cost regardless of usage?

## Turn 14 - User Simulator

Overtime cost is incurred only on the overtime hours actually used. It is 40 Yuan per overtime hour actually worked, with no fixed overtime cost regardless of usage.

## Turn 15 - Generic Agent

QUESTION: For the regular hours — since regular wage is paid regardless of utilization, is there any separate cost for regular hours actually worked, or is the only regular labor cost the fixed 4,800 Yuan per worker per month (with no additional per-hour charge for regular hours used)?

## Turn 15 - User Simulator

There is no separate cost for regular hours actually worked. The only regular labor cost is the fixed 4,800 Yuan per worker per month, with no additional per-hour charge for regular hours used.

## Turn 16 - Generic Agent

QUESTION: For the in-house production, is there any capacity limit on the number of units that can be produced in-house in a month other than the labor hour constraint (i.e., is the only limit on in-house production the available labor hours, with no separate machine or facility capacity cap)?

## Turn 16 - User Simulator

Yes, the only limit on in-house production is the available labor hours. There is no separate machine or facility capacity cap.

## Turn 17 - Generic Agent

QUESTION: For outsourcing, is there any limit on the number of units that can be outsourced in a month, or can the company outsource any number of units as needed?

## Turn 17 - User Simulator

There is no limit on the number of units that can be outsourced in a month. The company can outsource any number of units as needed.

## Turn 18 - Generic Agent

QUESTION: For the initial inventory of 15,000 units at the start of January — is there any initial backorder at the start of January, or does the company start January with zero backorders?

## Turn 18 - User Simulator

The company starts January with zero backorders.

## Turn 19 - Generic Agent

QUESTION: For the net profit objective — is it simply total revenue minus all costs (raw material, outsourcing, inventory holding, backorder, regular labor, overtime, hiring, firing), with no other costs or taxes to consider?

## Turn 19 - User Simulator

Yes, the net profit objective is simply total revenue minus all costs: raw material, outsourcing, inventory holding, backorder, regular labor, overtime, hiring, and firing. There are no other costs or taxes to consider.

## Turn 20 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Problem:** Production and workforce planning for a foldable tables company over 6 months (January–June), maximizing total net profit.

**Decision variables (per month t = 1..6):**
- Workforce on staff (integer, ≥ 0)
- Hires (integer, ≥ 0)
- Fires (integer, ≥ 0)
- In-house production (continuous or integer, ≥ 0)
- Outsourced units (continuous or integer, ≥ 0)
- Ending inventory (continuous or integer, ≥ 0)
- Ending backorders (continuous or integer, ≥ 0)
- Regular hours used (continuous, ≥ 0)
- Overtime hours used (continuous, ≥ 0)

**Workforce balance:**
- Workforce_t = Workforce_{t-1} + Hires_t − Fires_t
- Workforce_0 = 1,000
- Hires and fires take effect in the same month.

**Production capacity:**
- In-house production_t × 5 ≤ Regular hours used_t + Overtime hours used_t
- Regular hours used_t ≤ 160 × Workforce_t
- Overtime hours used_t ≤ 20 × Workforce_t

**Inventory/backorder balance (two separate non-negative quantities):**
- Inventory_t + Production_t + Outsourced_t = Demand_t + Backorders_{t-1} + Backorders_t
- (Units available = units fulfilled + units carried as backorders)
- Inventory_0 = 15,000; Backorders_0 = 0
- Backorders_6 = 0 (all backorders cleared by end of June)
- Inventory_6 ≥ 10,000

**Revenue:**
- 300 × (Demand_t + Backorders_{t-1} − Backorders_t) per month (units actually fulfilled)

**Costs:**
- Raw material: 90 × In-house production_t
- Outsourcing: 200 × Outsourced_t
- Inventory holding: 15 × Inventory_t (each month including June)
- Backorder: 35 × Backorders_t (each month including June)
- Regular labor: 4,800 × Workforce_t (fixed per worker, regardless of utilization)
- Overtime: 40 × Overtime hours used_t
- Hiring: 5,000 × Hires_t
- Firing: 8,000 × Fires_t

**Objective:** Maximize total revenue − total costs over all 6 months.

**No other constraints:** No workforce min/max, no outsourcing cap, no machine capacity cap, no other costs or taxes.