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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 × number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: When demand is back-ordered and fulfilled in a later month, is the sales revenue of 300 Yuan per unit recognized in the month the order was originally placed, or in the month the unit is actually delivered?

## Turn 2 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the month the unit is actually delivered.

## Turn 3 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it incurred only on units produced in-house during that month (i.e., it is a per-unit production cost that does not depend on when the unit is eventually sold), or is it tied to units that are actually sold/delivered?

## Turn 3 - User Simulator

The raw material cost of 90 Yuan per unit is incurred only on units produced in-house during that month. It is a per-unit production cost and does not depend on when the unit is eventually sold.

## Turn 4 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (including June's ending inventory of at least 10,000 units), or is it charged only on inventory held at the end of months January through May?

## Turn 4 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including June's ending inventory.

## Turn 5 - Generic Agent

QUESTION: When a worker is hired in a given month, is that worker available to work (regular and overtime hours) in that same month, or do they only become available starting the following month?

## Turn 5 - User Simulator

A worker hired in a given month is available to work (regular and overtime hours) in that same month.

## Turn 6 - Generic Agent

QUESTION: When a worker is fired in a given month, is that worker still available to work (regular and overtime hours) in that same month, or are they removed and no longer available starting that month?

## Turn 6 - User Simulator

A worker fired in a given month is removed and no longer available to work (regular and overtime hours) starting that month.

## Turn 7 - Generic Agent

QUESTION: Can the workforce size change by more than one worker in a single month (i.e., can you hire or fire multiple workers in the same month), or is the workforce change limited to at most one worker per month?

## Turn 7 - User Simulator

The workforce size can change by more than one worker in a single month. You can hire or fire multiple workers in the same month.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many units can be outsourced in a given month, or is outsourcing unlimited as long as the 200 Yuan per unit cost is paid?

## Turn 8 - User Simulator

There is no limit on how many units can be outsourced in a given month. Outsourcing is unlimited as long as the 200 Yuan per unit cost is paid.

## Turn 9 - Generic Agent

QUESTION: Can the workforce size ever go below zero or below some minimum level, or is the only constraint that you start with 1,000 workers and can hire/fire freely (so the workforce can in principle go down to zero)?

## Turn 9 - User Simulator

The only constraint is that you start with 1,000 workers and can hire or fire freely. The workforce can in principle go down to zero.

## Turn 10 - Generic Agent

QUESTION: When back-ordered demand is fulfilled in a later month, is the backorder cost of 35 Yuan per unit charged for each month the unit remains unfulfilled (i.e., a unit back-ordered for two months incurs 70 Yuan in backorder cost), or is it charged only once per unit regardless of how many months it is delayed?

## Turn 10 - User Simulator

The backorder cost of 35 Yuan per unit is charged for each month the unit remains unfulfilled. So a unit back-ordered for two months incurs 70 Yuan in backorder cost.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how much demand can be back-ordered in a given month (i.e., can all of a month's demand be deferred to later months), or must at least some portion of each month's demand be fulfilled in that same month?

## Turn 11 - User Simulator

There is no limit on how much demand can be back-ordered in a given month. All of a month's demand can be deferred to later months, as long as all backorders are cleared by the end of June.

## Turn 12 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June. Does this mean that by the end of June, all demand from January through June must have been fulfilled (i.e., no backorders can remain at the end of June), or can some backorders from earlier months still be outstanding at the end of June as long as the ending inventory requirement of 10,000 units is met?

## Turn 12 - User Simulator

By the end of June, all demand from January through June must have been fulfilled. No backorders can remain at the end of June.

## Turn 13 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in any given month, the fulfillment of that month's demand (plus any backorders) can draw from the beginning inventory of that month, the in-house production of that month, and the outsourced units of that month, with no restriction on the order or proportion of these sources?

## Turn 13 - User Simulator

Yes, in any given month, the fulfillment of that month's demand (plus any backorders) can draw from the beginning inventory of that month, the in-house production of that month, and the outsourced units of that month, with no restriction on the order or proportion of these sources.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that limits the total number of units that can be produced in-house in a given month beyond the labor-hour constraint (i.e., in-house production is limited only by available regular and overtime labor hours), or is there an additional capacity cap on in-house production?

## Turn 14 - User Simulator

There is no additional capacity cap on in-house production. In-house production is limited only by the available regular and overtime labor hours.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint on the ending inventory of months January through May (e.g., a minimum inventory level that must be maintained at the end of each of those months), or is the only inventory constraint the minimum of 10,000 units at the end of June?

## Turn 15 - User Simulator

There is no minimum inventory constraint for the ending inventory of months January through May. The only inventory constraint is the minimum of 10,000 units at the end of June.

## Turn 16 - Generic Agent

QUESTION: Can the ending inventory in any month be negative (i.e., can you have more demand than available supply in a month, with the shortfall automatically becoming backorders), or must the ending inventory be non-negative in every month with backorders tracked separately?

## Turn 16 - User Simulator

The ending inventory in any month can be negative, with the shortfall automatically becoming backorders.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that limits the total number of units that can be outsourced across the entire six-month period, or is the only constraint on outsourcing the per-unit cost of 200 Yuan?

## Turn 17 - User Simulator

There is no constraint that limits the total number of units that can be outsourced across the entire six-month period. The only constraint on outsourcing is the per-unit cost of 200 Yuan.

## Turn 18 - Generic Agent

QUESTION: When you say the regular wage of 30 Yuan per hour for 160 hours per worker is "paid regardless of utilization," does this mean the total regular wage cost for a month is simply 30 × 160 × (number of workers employed that month), even if the actual regular hours used for production are less than 160 per worker?

## Turn 18 - User Simulator

Yes, the total regular wage cost for a month is simply 30 × 160 × (number of workers employed that month), even if the actual regular hours used for production are less than 160 per worker.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that requires the workforce to be non-decreasing (i.e., you can only hire, not fire), or can the workforce both increase and decrease from month to month?

## Turn 19 - User Simulator

The workforce can both increase and decrease from month to month. There is no constraint requiring the workforce to be non-decreasing.

## Turn 20 - Generic Agent

QUESTION: When a unit is produced in-house in a given month but not sold until a later month, is the raw material cost of 90 Yuan still incurred in the month of production (as you confirmed earlier), and is the inventory holding cost of 15 Yuan per unit charged on that unit at the end of each month it sits in inventory until it is sold?

## Turn 20 - User Simulator

Yes, the raw material cost of 90 Yuan is incurred in the month of production, and the inventory holding cost of 15 Yuan per unit is charged on that unit at the end of each month it sits in inventory until it is sold.

## Turn 21 - Generic Agent

QUESTION: When a unit is outsourced in a given month but not sold until a later month, is the outsourcing cost of 200 Yuan incurred in the month of outsourcing (i.e., when the unit is produced/received), and is the inventory holding cost of 15 Yuan per unit charged on that unit at the end of each month it sits in inventory until it is sold?

## Turn 21 - User Simulator

Yes, the outsourcing cost of 200 Yuan is incurred in the month of outsourcing, and the inventory holding cost of 15 Yuan per unit is charged on that unit at the end of each month it sits in inventory until it is sold.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that limits the total number of units that can be produced in-house across the entire six-month period, or is the only constraint on in-house production the labor-hour constraint in each month?

## Turn 22 - User Simulator

There is no constraint that limits the total number of units that can be produced in-house across the entire six-month period. The only constraint on in-house production is the labor-hour constraint in each month.

## Turn 23 - Generic Agent

QUESTION: When a worker is hired in a given month, is the hiring cost of 5,000 Yuan incurred in that same month, and when a worker is fired in a given month, is the firing cost of 8,000 Yuan incurred in that same month?

## Turn 23 - User Simulator

Yes, the hiring cost of 5,000 Yuan is incurred in the same month the worker is hired, and the firing cost of 8,000 Yuan is incurred in the same month the worker is fired.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that limits the total number of workers that can be hired or fired in a single month, or can you hire or fire any number of workers in a given month as long as the per-worker costs are paid?

## Turn 24 - User Simulator

There is no constraint that limits the total number of workers that can be hired or fired in a single month. You can hire or fire any number of workers in a given month as long as the per-worker costs are paid.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that requires the workforce at the end of June to be at least some minimum level, or can the workforce at the end of June be any non-negative number?

## Turn 25 - User Simulator

There is no constraint that requires the workforce at the end of June to be at least some minimum level. The workforce at the end of June can be any non-negative number.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that limits the total number of units that can be held in inventory at the end of any month (i.e., a maximum inventory capacity), or is inventory unlimited as long as the holding cost is paid?

## Turn 26 - User Simulator

There is no constraint that limits the total number of units that can be held in inventory at the end of any month. Inventory is unlimited as long as the holding cost is paid.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that limits the total number of units that can be back-ordered at the end of any month (i.e., a maximum backorder level), or is the backorder level unlimited as long as the backorder cost is paid?

## Turn 27 - User Simulator

There is no constraint that limits the total number of units that can be back-ordered at the end of any month. The backorder level is unlimited as long as the backorder cost is paid.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that requires the workforce to be an integer number of workers (i.e., you can only hire or fire whole workers), or can the workforce be a fractional number?

## Turn 28 - User Simulator

The workforce must be an integer number of workers. You can only hire or fire whole workers.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that requires the number of units produced in-house, outsourced, or sold in a given month to be integers, or can these quantities be fractional?

## Turn 29 - User Simulator

There is no constraint that requires the number of units produced in-house, outsourced, or sold in a given month to be integers. These quantities can be fractional.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that requires the ending inventory or backorder level at the end of any month to be an integer, or can these quantities be fractional?

## Turn 30 - User Simulator

There is no constraint that requires the ending inventory or backorder level at the end of any month to be an integer. These quantities can be fractional.