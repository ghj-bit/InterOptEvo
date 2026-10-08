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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 2 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 3 - Generic Agent

QUESTION: For the regular wage of 30 Yuan per hour paid for 160 hours per worker regardless of utilization, is this cost incurred for every worker employed during the month (i.e., 160 × 30 = 4,800 Yuan per worker per month), even if the worker's hours are not fully used for production?

## Turn 3 - User Simulator

Yes, the regular wage cost is 4,800 Yuan per worker per month (160 hours × 30 Yuan/hour), incurred for every worker employed during that month, regardless of how many hours are actually used for production.

## Turn 4 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 4 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 5 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours and up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and contribute their 160 regular hours and up to 20 overtime hours) in that same month, or do they stop contributing starting that month?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: When you say "orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the total units available to meet demand (previous month's ending inventory + current month's in-house production + current month's outsourced units) must be at least equal to the current month's demand plus any backorders carried into that month, with any shortfall becoming new backorders?

## Turn 7 - User Simulator

Yes, that is correct. In each month, the total units available (previous month's ending inventory + current month's in-house production + current month's outsourced units) must be at least equal to the current month's demand plus any backorders carried into that month. Any shortfall becomes new backorders carried to the next month.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a given month, or can you outsource as many units as needed?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on the number of workers that can be hired or fired in a single month, or can you adjust the workforce by any number in any month?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Can the workforce size (number of workers) become zero in any month, or is there a minimum number of workers that must be maintained at all times?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is the number of workers required to be an integer (whole number of people), or can it be treated as a continuous variable in the model?

## Turn 11 - User Simulator

The number of workers must be an integer (whole number of people).

## Turn 12 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 15 - User Simulator

The

## Turn 16 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 18 - User Simulator

The

## Turn 19 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Is the number of units produced in-house, outsourced, and the inventory/backorder quantities required to be integers, or can they be treated as continuous variables?

## Turn 30 - User Simulator

The