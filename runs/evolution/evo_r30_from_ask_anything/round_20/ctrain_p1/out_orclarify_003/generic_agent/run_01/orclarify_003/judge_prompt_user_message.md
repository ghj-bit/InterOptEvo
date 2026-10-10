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

QUESTION: Is the 20-hour overtime limit a per-worker cap that applies to each individual worker, or is it a total cap for the entire workforce per month?

## Turn 1 - User Simulator

It is a per-worker cap. Each individual worker can work at most 20 overtime hours in a given month.

## Turn 2 - Generic Agent

QUESTION: Is the workforce size (number of employees) a decision variable that can change each month through hiring and firing, or is it fixed at 1,000 employees for all six months?

## Turn 2 - User Simulator

The workforce size is a decision variable. We can hire or fire employees each month, subject to the hiring and firing costs.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units, is there any limit on how many units can be outsourced per month, or is outsourcing unlimited?

## Turn 3 - User Simulator

Outsourcing is unlimited. There is no cap on the number of units that can be outsourced per month.

## Turn 4 - Generic Agent

QUESTION: Is the 15,000-unit initial inventory at the start of January available to fulfill January demand, or is it only available starting in February?

## Turn 4 - User Simulator

The 15,000-unit initial inventory is available to fulfill January demand.

## Turn 5 - Generic Agent

QUESTION: Is the 10,000-unit minimum ending inventory requirement a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 5 - User Simulator

It is a hard constraint. The ending inventory at the end of June must be at least 10,000 units.

## Turn 6 - Generic Agent

QUESTION: Are the number of workers, in-house production units, and outsourced units required to be integer values, or can they be treated as continuous variables in the model?

## Turn 6 - User Simulator

The number of workers must be an integer. In-house production units and outsourced units can be treated as continuous variables.

## Turn 7 - Generic Agent

QUESTION: Is there a minimum or maximum limit on the number of workers that can be employed in any given month, or can the workforce size vary freely from zero to any positive integer?

## Turn 7 - User Simulator

There is no minimum or maximum limit on the number of workers. The workforce size can vary freely from zero to any positive integer.

## Turn 8 - Generic Agent

QUESTION: Are there any additional constraints or requirements not mentioned in the brief, such as limits on the number of hires or fires per month, minimum workforce levels, or other operational restrictions?

## Turn 8 - User Simulator

No, there are no additional constraints or requirements beyond what was mentioned in the brief.

## Turn 9 - Generic Agent

QUESTION: Is the 90 Yuan raw material cost applied to all in-house produced units regardless of whether they are sold in the current month or held in inventory, or only to units that are actually sold?

## Turn 9 - User Simulator

The 90 Yuan raw material cost is applied to all in-house produced units, regardless of whether they are sold in the current month or held in inventory.

## Turn 10 - Generic Agent

QUESTION: Is the 15 Yuan inventory holding cost applied to the ending inventory of each month, including the ending inventory at the end of June, or only to months January through May?

## Turn 10 - User Simulator

The 15 Yuan inventory holding cost is applied to the ending inventory of each month, including the ending inventory at the end of June.

## Turn 11 - Generic Agent

QUESTION: Is the 35 Yuan backorder cost applied to the number of units backordered at the end of each month, including the end of June, or only to months January through May?

## Turn 11 - User Simulator

The 35 Yuan backorder cost is applied to the number of units backordered at the end of each month, including the end of June.

## Turn 12 - Generic Agent

QUESTION: Is the 300 Yuan sales price revenue recognized when a unit is sold to fulfill demand in a given month, or when the unit is produced?

## Turn 12 - User Simulator

The 300 Yuan sales price revenue is recognized when a unit is sold to fulfill demand in a given month.

## Turn 13 - Generic Agent

QUESTION: Is the 160 regular hours per worker per month a fixed capacity that is always available, or can it be reduced if the workforce is underutilized?

## Turn 13 - User Simulator

The 160 regular hours per worker per month is a fixed capacity that is always available.

## Turn 14 - Generic Agent

QUESTION: Is the regular wage of 30 Yuan per hour paid for all 160 hours per worker per month regardless of how many hours are actually used for production, or is it paid only for the hours actually utilized?

## Turn 14 - User Simulator

The regular wage of 30 Yuan per hour is paid for all 160 hours per worker per month regardless of how many hours are actually used for production.

## Turn 15 - Generic Agent

QUESTION: Is the 5,000 Yuan hiring cost incurred for each new worker hired in a given month, and is the 8,000 Yuan firing cost incurred for each worker fired in a given month, with these costs applied in the month the hire or fire occurs?

## Turn 15 - User Simulator

Yes, the 5,000 Yuan hiring cost is incurred for each new worker hired in a given month, and the 8,000 Yuan firing cost is incurred for each worker fired in a given month, with these costs applied in the month the hire or fire occurs.

## Turn 16 - Generic Agent

QUESTION: Is the workforce size at the start of January fixed at 1,000 employees, or can hiring or firing occur in January as well?

## Turn 16 - User Simulator

The workforce size at the start of January is fixed at 1,000 employees. Hiring or firing can occur in January as well, meaning the workforce can change from the initial 1,000 during January.

## Turn 17 - Generic Agent

QUESTION: Is the workforce size at the end of June required to match any specific value, or can it be any non-negative integer?

## Turn 17 - User Simulator

The workforce size at the end of June can be any non-negative integer. There is no specific required value.

## Turn 18 - Generic Agent

QUESTION: Is the 20-hour overtime cap per worker per month a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 18 - User Simulator

It is a hard constraint. The 20-hour overtime cap per worker per month must be strictly satisfied.

## Turn 19 - Generic Agent

QUESTION: Is the 5 labor hours per in-house unit a fixed requirement that applies to all in-house production, or can it vary depending on the month or production volume?

## Turn 19 - User Simulator

The 5 labor hours per in-house unit is a fixed requirement that applies to all in-house production.

## Turn 20 - Generic Agent

QUESTION: Is the demand forecast for each month a hard requirement that must be fully met by the end of June, or can some demand remain unfulfilled at the end of the planning horizon?

## Turn 20 - User Simulator

The demand forecast for each month is a hard requirement that must be fully met by the end of June. All backorders must be cleared by the end of June, meaning no outstanding customer orders can remain after June.

## Turn 21 - Generic Agent

QUESTION: Is the 15,000-unit initial inventory at the start of January subject to the 15 Yuan per unit holding cost for January, or is it exempt from holding costs since it was already on hand before the planning period began?

## Turn 21 - User Simulator

The 15,000-unit initial inventory is subject to the 15 Yuan per unit holding cost for January if any of it remains in inventory at the end of January.

## Turn 22 - Generic Agent

QUESTION: Is the 35 Yuan backorder cost applied to the number of units backordered at the end of each month, or is it applied to the total number of units that were backordered during the month (i.e., the cumulative backorder quantity)?

## Turn 22 - User Simulator

The 35 Yuan backorder cost is applied to the number of units backordered at the end of each month.

## Turn 23 - Generic Agent

QUESTION: Is the 15 Yuan inventory holding cost applied to the ending inventory of each month, including the ending inventory at the end of June, or only to months January through May?

## Turn 23 - User Simulator

The 15 Yuan inventory holding cost is applied to the ending inventory of each month, including the ending inventory at the end of June.

## Turn 24 - Generic Agent

QUESTION: Is the 35 Yuan backorder cost applied to the number of units backordered at the end of each month, including the end of June, or only to months January through May?

## Turn 24 - User Simulator

The 35 Yuan backorder cost is applied to the number of units backordered at the end of each month, including the end of June.

## Turn 25 - Generic Agent

QUESTION: Is the 300 Yuan sales price revenue recognized when a unit is sold to fulfill demand in a given month, or when the unit is produced?

## Turn 25 - User Simulator

The 300 Yuan sales price revenue is recognized when a unit is sold to fulfill demand in a given month.

## Turn 26 - Generic Agent

QUESTION: Is the 160 regular hours per worker per month a fixed capacity that is always available, or can it be reduced if the workforce is underutilized?

## Turn 26 - User Simulator

The 160 regular hours per worker per month is a fixed capacity that is always available.

## Turn 27 - Generic Agent

QUESTION: Is the regular wage of 30 Yuan per hour paid for all 160 hours per worker per month regardless of how many hours are actually used for production, or is it

## Turn 27 - User Simulator

The regular wage of 30 Yuan per hour is paid for all 160 hours per worker per month regardless of how many hours are actually used for production.

## Turn 28 - Generic Agent

QUESTION: Is the 5,

## Turn 28 - User Simulator

The 5,000 Yuan hiring cost is incurred for each new

## Turn 29 - Generic Agent

QUESTION: Is the 5

## Turn 29 - User Simulator

The 5

## Turn 30 - Generic Agent

QUESTION: Is

## Turn 30 - User Simulator

The