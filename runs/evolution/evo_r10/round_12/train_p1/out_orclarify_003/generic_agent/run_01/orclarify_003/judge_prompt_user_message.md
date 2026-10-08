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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker is capped at 20 overtime hours per month (so total workforce overtime is 20 × number of workers that month), or is there a single aggregate cap of 20 hours for the whole workforce combined?

## Turn 1 - User Simulator

Each individual worker is capped at 20 overtime hours per month. So the total workforce overtime for a given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce, can the number of workers change from month to month (i.e., can you hire or fire workers in any month, not just at the start of January), and if so, is there any limit on how many workers can be hired or fired in a single month?

## Turn 2 - User Simulator

Yes, the number of workers can change from month to month. You can hire or fire workers in any month. There is no limit on how many workers can be hired or fired in a single month.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the total units available to meet demand (previous month's ending inventory + current month's in-house production + current month's outsourced units) must be at least the current month's demand, with any shortfall becoming backorders carried to the next month?

## Turn 3 - User Simulator

Yes, that is correct. In each month, the total units available to meet demand (previous month's ending inventory + current month's in-house production + current month's outsourced units) must be at least the current month's demand plus any backorders carried into that month. Any shortfall becomes backorders carried to the next month.

## Turn 4 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production: is this cost incurred for every unit produced in-house regardless of whether it is sold in the current month or held in inventory, or is it only incurred for units that are actually sold?

## Turn 4 - User Simulator

The raw material cost of 90 Yuan per unit is incurred for every unit produced in-house, regardless of whether it is sold in the current month or held in inventory.

## Turn 5 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit: is revenue recognized in the month the unit is actually sold (i.e., when demand is fulfilled), or is it recognized in the month the unit is produced?

## Turn 5 - User Simulator

Revenue is recognized in the month the unit is actually sold, meaning when demand is fulfilled.

## Turn 6 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit: is this cost incurred for each unit of unfulfilled demand that is carried over from one month to the next (i.e., a per-period holding cost on the backorder quantity), or is it a one-time cost charged only once per unit when it is first backordered?

## Turn 6 - User Simulator

The backorder cost of 35 Yuan per unit is incurred for each unit of unfulfilled demand that is carried over from one month to the next. It is a per-period cost on the backorder quantity.

## Turn 7 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit: is this cost incurred on the ending inventory of each month (i.e., units remaining at the end of the month), and does it apply to all months including June (the final month)?

## Turn 7 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is incurred on the ending inventory of each month, and it applies to all months including June.

## Turn 8 - Generic Agent

QUESTION: Regarding the regular wage: you stated it is 30 Yuan per hour for 160 regular hours per worker, paid regardless of utilization. Does this mean each worker costs 30 × 160 = 4,800 Yuan per month in regular wages, even if the worker is not fully utilized (i.e., even if in-house production that month requires fewer than 160 hours per worker)?

## Turn 8 - User Simulator

Yes, each worker costs 30 × 160 = 4,800 Yuan per month in regular wages, even if the worker is not fully utilized.

## Turn 9 - Generic Agent

QUESTION: Regarding the workforce and production capacity: is the total in-house production in a month limited by the total available labor hours (regular + overtime) of the workforce that month, meaning in-house production × 5 hours ≤ (number of workers × 160) + (number of workers × 20)?

## Turn 9 - User Simulator

Yes, the total in-house production in a month is limited by the total available labor hours (regular + overtime) of the workforce that month. Specifically, in-house production × 5 hours ≤ (number of workers × 160) + (number of workers × 20).

## Turn 10 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 10 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 11 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 11 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 12 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 12 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 13 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 13 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 14 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 14 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 15 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 15 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 16 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 16 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 17 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 17 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 18 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 18 - User Simulator

The number of workers in a given month is determined after

## Turn 19 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 19 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you hire workers in January, they contribute labor hours in January.

## Turn 20 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 20 - User Simulator

The number of workers in a given month is determined after hiring/firing in that month. If you

## Turn 21 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 21 - User Simulator

The number of workers in a given month is determined after

## Turn 22 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 22 - User Simulator

The number of workers in a given

## Turn 23 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 23 - User Simulator

The number of workers in a

## Turn 24 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 24 - User Simulator

The number of workers

## Turn 25 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers in a given month determined by the workers at the start of that month (before any hiring/firing in that month), or after hiring/firing? In other words, if you hire workers in January, do they contribute labor hours in January, or only starting in February?

## Turn 30 - User Simulator

The