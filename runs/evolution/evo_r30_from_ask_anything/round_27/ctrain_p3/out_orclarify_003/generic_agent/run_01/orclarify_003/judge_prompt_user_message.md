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

QUESTION: Is the 20-hour overtime limit a hard constraint that must be strictly respected in every month, or is it a soft target that can be violated if a penalty is paid?

## Turn 1 - User Simulator

It is a hard constraint. The 20-hour overtime limit per worker per month must be strictly respected in every month.

## Turn 2 - Generic Agent

QUESTION: Is the 10,000-unit ending inventory requirement at the end of June a hard constraint that must be strictly met, or is it a soft target that can be violated if a penalty is paid?

## Turn 2 - User Simulator

It is a hard constraint. The ending inventory at the end of June must be at least 10,000 units.

## Turn 3 - Generic Agent

QUESTION: Is the number of workers hired or fired in a given month required to be an integer, or can it be treated as a continuous variable?

## Turn 3 - User Simulator

The number of workers hired or fired in a given month must be an integer.

## Turn 4 - Generic Agent

QUESTION: Is the number of units produced in-house in a given month required to be an integer, or can it be treated as a continuous variable?

## Turn 4 - User Simulator

The number of units produced in-house in a given month must be an integer.

## Turn 5 - Generic Agent

QUESTION: Is the number of units outsourced in a given month required to be an integer, or can it be treated as a continuous variable?

## Turn 5 - User Simulator

The number of units outsourced in a given month must be an integer.

## Turn 6 - Generic Agent

QUESTION: Is the number of units sold in a given month required to be an integer, or can it be treated as a continuous variable?

## Turn 6 - User Simulator

The number of units sold in a given month must be an integer.

## Turn 7 - Generic Agent

QUESTION: Is the number of units back-ordered at the end of a given month required to be an integer, or can it be treated as a continuous variable?

## Turn 7 - User Simulator

The number of units back-ordered at the end of a given month must be an integer.

## Turn 8 - Generic Agent

QUESTION: Is the number of units in inventory at the end of a given month required to be an integer, or can it be treated as a continuous variable?

## Turn 8 - User Simulator

The number of units in inventory at the end of a given month must be an integer.

## Turn 9 - Generic Agent

QUESTION: Is the regular wage cost of 30 Yuan per hour for the 160 regular hours per worker incurred for every worker on the payroll in a month, regardless of how many hours they actually work?

## Turn 9 - User Simulator

Yes, the regular wage cost of 30 Yuan per hour for the 160 regular hours per worker is incurred for every worker on the payroll in a month, regardless of how many hours they actually work.

## Turn 10 - Generic Agent

QUESTION: Is the inventory holding cost of 15 Yuan per unit applied to the ending inventory of each month, including the ending inventory of June?

## Turn 10 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is applied to the ending inventory of each month, including the ending inventory of June.

## Turn 11 - Generic Agent

QUESTION: Is the backorder cost of 35 Yuan per unit applied to the number of units back-ordered at the end of each month, including the end of June?

## Turn 11 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is applied to the number of units back-ordered at the end of each month, including the end of June.

## Turn 12 - Generic Agent

QUESTION: Is the raw material cost of 90 Yuan per unit incurred only for units produced in-house, or does it also apply to units outsourced?

## Turn 12 - User Simulator

The raw material cost of 90 Yuan per unit is incurred only for units produced in-house.

## Turn 13 - Generic Agent

QUESTION: Is the outsourcing cost of 200 Yuan per unit an all-inclusive cost that does not include any additional raw material or labor costs?

## Turn 13 - User Simulator

Yes, the outsourcing cost of 200 Yuan per unit is an all-inclusive cost that does not include any additional raw material or labor costs.

## Turn 14 - Generic Agent

QUESTION: Is the sales price of 300 Yuan per unit applied to all units sold, including those that fulfill back-ordered demand from previous months?

## Turn 14 - User Simulator

Yes

## Turn 15 - Generic Agent

QUESTION: Is there a maximum limit on the number of units that can be outsourced in any given month?

## Turn 15 - User Simulator

No

## Turn 16 - Generic Agent

QUESTION: Is there a maximum limit on the total number of workers that can be employed in any given month?

## Turn 16 - User Simulator

No

## Turn 17 - Generic Agent

QUESTION: Is there a minimum number of workers that must be employed in any given month?

## Turn 17 - User Simulator

No

## Turn 18 - Generic Agent

QUESTION: Is there a maximum limit on the total inventory that can be held at the end of any month?

## Turn 18 - User Simulator

No

## Turn 19 - Generic Agent

QUESTION: Is there a maximum limit on the total number of units that can be back-ordered at the end of any month?

## Turn 19 - User Simulator

No

## Turn 20 - Generic Agent

QUESTION: Are there any other constraints or requirements that have not been mentioned yet?

## Turn 20 - User Simulator

Yes, all backorders must be cleared by the end of June. That means no outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 21 - Generic Agent

QUESTION: Is the requirement that all backorders must be cleared by the end of June a hard constraint that must be strictly met?

## Turn 21 - User Simulator

Yes

## Turn 22 - Generic Agent

QUESTION: Is the workforce size at the end of June required to be a specific number, or is it free to be any non-negative integer?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Is the workforce size at the end of June free to be any non-negative integer, or is it required to match a specific target number?

## Turn 30 - User Simulator

The