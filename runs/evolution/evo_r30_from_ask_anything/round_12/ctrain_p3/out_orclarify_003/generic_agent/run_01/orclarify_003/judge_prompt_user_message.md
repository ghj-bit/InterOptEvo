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

QUESTION: Is the 10,000-unit minimum ending inventory requirement for June only, or must the ending inventory be at least 10,000 units at the end of every month from January through June?

## Turn 1 - User Simulator

It is only for the end of June. The 10,000-unit minimum ending inventory requirement applies specifically to the end of June, not to the end of every month from January through June.

## Turn 2 - Generic Agent

QUESTION: Can the workforce size (number of employees) be changed in any month from January through June, or is the workforce fixed at 1,000 employees for the entire six-month period?

## Turn 2 - User Simulator

The workforce size can be changed in any month from January through June. We can hire or fire employees as needed, subject to the hiring cost of 5,000 Yuan per new worker and the firing cost of 8,000 Yuan per worker.

## Turn 3 - Generic Agent

QUESTION: When you hire or fire employees in a given month, do they contribute their full 160 regular hours and up to 20 overtime hours to that same month's production, or do they only become available for production starting the following month?

## Turn 3 - User Simulator

I don't have a specific rule on whether newly hired or fired employees contribute to production in the same month or only the following month. That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: For the purpose of this plan, should we assume that employees hired or fired in a given month are fully available for production in that same month, or should we assume they only affect production starting the following month?

## Turn 4 - User Simulator

I don't have a specific rule on whether employees hired or fired in a given month are fully available for production in that same month or only starting the following month. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum limit on the number of employees that can be hired or fired in any single month, or are hiring and firing quantities unlimited?

## Turn 5 - User Simulator

There is no maximum limit on the number of employees that can be hired or fired in any single month. Hiring and firing quantities are unlimited.

## Turn 6 - Generic Agent

QUESTION: Is there a minimum or maximum limit on the total number of employees the company can have at the end of any month, or can the workforce size be any non-negative integer?

## Turn 6 - User Simulator

There is no minimum or maximum limit on the total number of employees the company can have at the end of any month. The workforce size can be any non-negative integer.

## Turn 7 - Generic Agent

QUESTION: Is there a limit on the number of units that can be outsourced in any single month, or can the company outsource any non-negative quantity of units?

## Turn 7 - User Simulator

There is no limit on the number of units that can be outsourced in any single month. The company can outsource any non-negative quantity of units.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum limit on the inventory that can be held at the end of any month, or can inventory be any non-negative quantity?

## Turn 8 - User Simulator

There is no maximum limit on the inventory that can be held at the end of any month. Inventory can be any non-negative quantity.

## Turn 9 - Generic Agent

QUESTION: Is there a maximum limit on the number of units that can be back-ordered (unfulfilled demand carried over) at the end of any month, or can backorders be any non-negative quantity?

## Turn 9 - User Simulator

There is no maximum limit on the number of units that can be back-ordered at the end of any month. Backorders can be any non-negative quantity, with the only requirement being that all backorders must be cleared by the end of June.

## Turn 10 - Generic Agent

QUESTION: Does the requirement that all backorders must be cleared by the end of June mean that the ending inventory at the end of June must be at least 10,000 units AND there must be zero backorders, or does the 10,000-unit minimum ending inventory requirement already account for any remaining backorders?

## Turn 10 - User Simulator

It means both: the ending inventory at the end of June must be at least 10,000 units AND there must be zero backorders. These are two separate requirements that must both be satisfied.

## Turn 11 - Generic Agent

QUESTION: Is the 35 Yuan per unit backorder cost incurred for each unit of unfulfilled demand at the end of each month (including June if any backorders existed), or is it only incurred for backorders carried over from one month to the next (i.e., not for the final month)?

## Turn 11 - User Simulator

The 35 Yuan per unit backorder cost is incurred for each unit of unfulfilled demand carried over from one month to the next. Since all backorders must be cleared by the end of June, there are no backorders at the end of June, so no backorder cost is incurred for June.

## Turn 12 - Generic Agent

QUESTION: Is the 15 Yuan per unit inventory holding cost incurred for inventory held at the end of every month from January through June, or is it only incurred for months January through May (excluding June)?

## Turn 12 - User Simulator

The 15 Yuan per unit inventory holding cost is incurred for inventory held at the end of every month from January through June, including June.

## Turn 13 - Generic Agent

QUESTION: Is the regular wage cost of 30 Yuan per hour for 160 hours per worker incurred for every worker on the payroll for that month, regardless of how many hours they actually work, or is it only incurred for the hours actually worked up to 160?

## Turn 13 - User Simulator

The regular wage cost of 30 Yuan per hour for 160 hours per worker is incurred for every worker on the payroll for that month, regardless of how many hours they actually work.

## Turn 14 - Generic Agent

QUESTION: Is the 90 Yuan per unit raw material cost incurred for every unit produced in-house, regardless of whether that unit is sold in the current month or held in inventory, or is it only incurred for units that are actually sold?

## Turn 14 - User Simulator

The 90 Yuan per unit raw material cost is incurred for every unit produced in-house, regardless of whether that unit is sold in the current month or held in inventory.

## Turn 15 - Generic Agent

QUESTION: Is the 200 Yuan per unit outsourcing cost incurred for every outsourced unit produced, regardless of whether that unit is sold in the current month or held in inventory, or is it only incurred for units that are actually sold?

## Turn 15 - User Simulator

The 200 Yuan per unit outsourcing cost is incurred for every outsourced unit produced, regardless of whether that unit is sold in the current month or held in inventory.

## Turn 16 - Generic Agent

QUESTION: Is the 300 Yuan per unit sales price revenue earned for every unit sold, regardless of whether that unit was produced in-house or outsourced, or is the sales price only applicable to in-house produced units?

## Turn 16 - User Simulator

The 300 Yuan per unit sales price revenue is earned for every unit sold, regardless of whether that unit was produced in-house or outsourced.

## Turn 17 - Generic Agent

QUESTION: Are the decision variables for in-house production, outsourcing, hiring, firing, and workforce size required to be integers, or can they be treated as continuous values?

## Turn 17 - User Simulator

I don't have a specific rule on whether the decision variables for in-house production, outsourcing, hiring, firing, and workforce size must be integers or can be treated as continuous values. That point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint linking the number of units produced in-house to the total labor hours available (regular plus overtime) for that month, or can in-house production be any non-negative quantity independent of labor hours?

## Turn 18 - User Simulator

There is a constraint linking in-house production to labor hours. Each in-house unit requires 5 labor hours to produce, and the total labor hours available in a month are determined by the workforce size (160 regular hours per worker plus up to 20 overtime hours per worker). In-house production cannot exceed what the available labor hours can support.

## Turn 19 - Generic Agent

QUESTION: Is the total labor hours available in a month calculated as (workforce size × 160) + (workforce size × 20), meaning every worker can work up to 20 overtime hours, or is there a separate decision variable for how many overtime hours are actually used, capped at 20 per worker?

## Turn 19 - User Simulator

There is a separate decision variable for how many overtime hours are actually used, capped at 20 per worker. The total labor hours available in a month are (workforce size × 160) regular hours plus the actual overtime hours used, where the actual overtime hours cannot exceed 20 per worker.

## Turn 20 - Generic Agent

QUESTION: Is the overtime wage cost of 40 Yuan per hour incurred only for the actual overtime hours used, or is it incurred for the full 20 hours per worker regardless of how many overtime hours are actually worked?

## Turn 20 - User Simulator

The overtime wage cost of 40 Yuan per hour is incurred only for the actual overtime hours used, not for the full 20 hours per worker regardless of how many overtime hours are actually worked.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that links the workforce size at the end of one month to the workforce size at the beginning of the next month, such as the workforce at the start of a month being equal to the workforce at the end of the previous month plus hires minus fires in that month?

## Turn 21 - User Simulator

Yes, the workforce at the start of a month is equal to the workforce at the end of the previous month plus hires minus fires in that month.

## Turn 22 - Generic Agent

QUESTION: Is the workforce size at the start of January fixed at 1,000 employees, or can the company hire or fire employees in January before production begins?

## Turn 22 - User Simulator

The workforce size at the start of January is fixed at 1,000 employees. The company can hire or fire employees in January, but the starting point is 1,000 employees.

## Turn 23 - Generic Agent

QUESTION: Is the inventory at the start of January fixed at 15,000 units, or can the company adjust this initial inventory level?

## Turn 23 - User Simulator

The inventory at the start of January is fixed at 15,000 units.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that links the inventory at the end of one month to the inventory at the beginning of the next month, such as the inventory at the start of a month being equal to the inventory at the end of the previous month?

## Turn 24 - User Simulator

Yes, the inventory at the start of a month is equal to the inventory at the end of the previous month.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that links the backorders at the end of one month to the backorders at the beginning of the next month, such as the backorders at the start of a month being equal to the backorders at the end of the previous month?

## Turn 25 - User Simulator

Yes, the backorders at the start of a month are equal to the backorders at the end of the previous month.

## Turn 26 - Generic Agent

QUESTION: Is the demand forecast for each month a fixed quantity that must be met (either in that month or via backorders), or is it a target that can be exceeded or undershot?

## Turn 26 - User Simulator

The demand forecast for each month is a fixed quantity that must be met, either in that month or via backorders.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that links the units sold in a month to the demand for that month plus backorders from the previous month, such as units sold in a month being equal to demand plus previous backorders minus new backorders?

## Turn 27 - User Simulator

Yes, the units sold in a month are equal to the demand for that month plus backorders from the previous month minus new backorders created in that month.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that links the inventory at the end of a month to the inventory at the start of the month, in-house production, outsourcing, and units sold, such as ending inventory equaling starting inventory plus in-house production plus outsourcing minus units sold?

## Turn 28 - User Simulator

Yes, the inventory at the end of a month equals the inventory at the start of the month plus in-house production plus outsourcing minus units sold.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that links the backorders at the end of a month to the demand for that month, backorders from the previous month, and units sold, such as ending backorders equaling previous backorders plus demand minus units sold?

## Turn 29 - User Simulator

Yes, the backorders at the end of a month equal the backorders from the previous month plus the demand for that month minus the units sold in that month.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that prevents both inventory and backorders from being positive at the end of the same month, or can both be positive simultaneously?

## Turn 30 - User Simulator

I don't have a specific rule on whether both inventory and backorders can be positive at the end of the same month. That point still needs internal confirmation.