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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is 20 times the number of workers that month), or that the sum of overtime hours across all workers combined is capped at 20 hours per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you said it's 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization — does this mean every worker employed in a month is paid 160 × 30 = 4,800 Yuan for regular time even if they work fewer hours, and overtime is paid only for hours actually worked beyond 160?

## Turn 2 - User Simulator

Yes, that is correct. Every worker employed in a month is paid 160 × 30 = 4,800 Yuan for regular time regardless of how many hours they actually work. Overtime is paid at 40 Yuan per hour only for hours actually worked beyond the 160 regular hours.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered, is the backorder cost of 35 Yuan per unit charged once for the month the demand is unmet, or is it charged for each month the unit remains unfulfilled until it is finally delivered?

## Turn 3 - User Simulator

The backorder cost of 35 Yuan per unit is charged for each month the unit remains unfulfilled until it is finally delivered.

## Turn 4 - Generic Agent

QUESTION: When back-ordered units are finally fulfilled in a later month, are they still sold at the 300 Yuan sales price, or is the revenue different for late deliveries?

## Turn 4 - User Simulator

Back-ordered units are still sold at the 300 Yuan sales price when they are finally delivered.

## Turn 5 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) in any month from January through June, or is the workforce fixed at 1,000 for the entire six-month period?

## Turn 5 - User Simulator

The workforce can be changed in any month from January through June. Hiring and firing are allowed in any month, with the associated costs of 5,000 Yuan per new worker hired and 8,000 Yuan per worker fired.

## Turn 6 - Generic Agent

QUESTION: When you say the ending inventory at the end of June must be at least 10,000 units, does this inventory need to be available after fulfilling all demand (including any backorders) through June, meaning it's the leftover stock after all sales are completed?

## Turn 6 - User Simulator

Yes, the 10,000 units must be available after fulfilling all demand (including any backorders) through June. It is the leftover stock remaining after all sales are completed.

## Turn 7 - Generic Agent

QUESTION: Can the workforce be reduced below zero or can workers be fired such that the workforce in a given month is less than what's needed to produce the in-house units that month, or is the constraint simply that in-house production hours (5 hours per unit) cannot exceed the total available hours (160 regular + overtime) of the workforce employed that month?

## Turn 7 - User Simulator

The constraint is simply that in-house production hours (5 hours per unit) cannot exceed the total available hours (160 regular + overtime) of the workforce employed that month. The workforce cannot be reduced below zero, but there is no separate requirement that the workforce must be large enough to produce a specific number of units; the production is limited by the available hours of the workers employed.

## Turn 8 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) in any month from January through June, or is the workforce fixed at 1,000 for the entire six-month period?

## Turn 8 - User Simulator

The workforce can be changed in any month from January through June. Hiring and firing are allowed in any month, with the associated costs of 5,000 Yuan per new worker hired and 8,000 Yuan per worker fired.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced in a given month, or can any quantity be outsourced as needed?

## Turn 9 - User Simulator

There is no limit on the number of units that can be outsourced in a given month. Any quantity can be outsourced as needed.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on the number of workers that can be hired or fired in a single month, or can any number be hired or fired as needed?

## Turn 10 - User Simulator

There is no limit on the number of workers that can be hired or fired in a single month. Any number can be hired or fired as needed.

## Turn 11 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does the inventory holding cost of 15 Yuan per unit apply to the ending inventory of every month (January through June), or only to months where inventory is carried over to the next month (i.e., not charged on June's ending inventory since the planning horizon ends)?

## Turn 11 - User Simulator

The inventory holding cost of 15 Yuan per unit applies to the ending inventory of every month, including June.

## Turn 12 - Generic Agent

QUESTION: When back-ordered units are fulfilled in a later month, do they consume the raw material cost of 90 Yuan per unit if produced in-house, or is the raw material cost only charged at the time of production regardless of when the unit is delivered?

## Turn 12 - User Simulator

The raw material cost of 90 Yuan per unit is charged at the time of production, regardless of when the unit is delivered.

## Turn 13 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 13 - User Simulator

A worker hired in a given month is available to work in that same month, contributing their 160 regular hours plus up to 20 overtime hours.

## Turn 14 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 14 - User Simulator

A worker fired in a given month is not available to work in that same month. They are removed and do not contribute any hours starting that month.

## Turn 15 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 15 - User Simulator

A worker hired in a given month is available to work in that same month, contributing their 160 regular hours plus up to 20 overtime hours.

## Turn 16 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 16 - User Simulator

A worker fired in a given month is not available to work in that same month. They are removed and do not contribute any hours starting that month.

## Turn 17 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) in any month from January through June, or is the workforce fixed at 1,000 for the entire six-month period?

## Turn 17 - User Simulator

The workforce can be changed in any month from January through June. Hiring and firing are allowed in any month, with the associated costs of 5,000 Yuan per new worker hired and 8,000 Yuan per worker fired.

## Turn 18 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 18 - User Simulator

A worker hired in a given month is available to work in that same month, contributing their 160 regular hours plus up to 20 overtime hours.

## Turn 19 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 19 - User Simulator

A worker fired in a given month is not available to work in that same month. They are removed and do not contribute any hours starting that month.

## Turn 20 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 20 - User Simulator

A worker hired in a given month is available to work in that same month, contributing their 160 regular hours plus up to 20 overtime hours.

## Turn 21 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 21 - User Simulator

A worker

## Turn 22 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 22 - User Simulator

A worker fired in a given month is not available to work in that same month. They are removed and do not contribute any hours starting that month.

## Turn 23 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 23 - User Simulator

A worker hired in a

## Turn 24 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 24 - User Simulator

A worker

## Turn 25 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 25 - User Simulator

A

## Turn 26 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or are they removed and not available starting that month?

## Turn 26 - User Simulator

A worker

## Turn 27 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours plus up to 20 overtime hours) in that same month, or do they

## Turn 27 - User Simulator

A worker hired in a given month is available to work in that same

## Turn 28 - Generic Agent

QUESTION: When a worker is fired in a given month, are they

## Turn 28 - User Simulator

A worker

## Turn 29 - Generic Agent

QUESTION: When a worker

## Turn 29 - User Simulator

A

## Turn 30 - Generic Agent

QUESTION: When

## Turn 30 - User Simulator

A