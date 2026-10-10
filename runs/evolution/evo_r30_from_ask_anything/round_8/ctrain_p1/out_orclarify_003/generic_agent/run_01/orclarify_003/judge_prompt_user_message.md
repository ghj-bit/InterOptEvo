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

QUESTION: Is the 10,000-unit minimum ending inventory requirement for June only, or must the ending inventory be at least 10,000 units at the end of every month from January through June

## Turn 1 - User Simulator

The 10,000-unit minimum ending inventory requirement applies only to the end of June. There is no such minimum inventory requirement for the end of any other month from January through May.

## Turn 2 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work up to 20 overtime hours per month (so total overtime is 20 times the number of workers), or that the sum of all overtime hours across all workers in a month is capped at 20 hours

## Turn 2 - User Simulator

Each individual worker can work up to 20 overtime hours per month. So the total overtime hours for the entire workforce in a given month is 20 times the number of workers employed that month.

## Turn 3 - Generic Agent

QUESTION: When you say "orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," do you mean that backorders from prior months must be fulfilled before any current-month demand is satisfied, or that all units (backorders plus current demand) are treated as a single pool of demand to be met

## Turn 3 - User Simulator

All units—backorders plus current-month demand—are treated as a single pool of demand to be met. There is no requirement that backorders must be fulfilled before current-month demand.

## Turn 4 - Generic Agent

QUESTION: Can the workforce size (number of employees) change from month to month through hiring and firing, or is the workforce fixed at 1,000 employees for all six months

## Turn 4 - User Simulator

The workforce size can change from month to month through hiring and firing. The 1,000 employees is the starting workforce at the beginning of January, not a fixed constraint for all six months.

## Turn 5 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (including regular and overtime hours) in that same month, or do they only become available starting the following month

## Turn 5 - User Simulator

The available business facts do not specify whether a worker hired in a given month is available to work in that same month or only starting the following month. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the purpose of this model, should we assume that a worker hired in a given month is available to work in that same month

## Turn 6 - User Simulator

Yes, for the purpose of this model, assume that a worker hired in a given month is available to work in that same month.

## Turn 7 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (including regular and overtime hours) in that same month, or are they removed from the workforce starting that same month

## Turn 7 - User Simulator

The available business facts do not specify whether a worker fired in a given month is still available to work in that same month or is removed from the workforce starting that same month. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: For the purpose of this model, should we assume that a worker fired in a given month is removed from the workforce and not available to work in that same month

## Turn 8 - User Simulator

Yes, for the purpose of this model, assume that a worker fired in a given month is removed from the workforce and not available to work in that same month.

## Turn 9 - Generic Agent

QUESTION: Is the regular wage of 30 Yuan per hour for 160 hours per worker paid for every worker employed in a month regardless of how many hours they actually work, meaning a worker who works zero hours still incurs the full 4,800 Yuan regular wage

## Turn 9 - User Simulator

Yes, the regular wage of 30 Yuan per hour for 160 hours per worker is paid for every worker employed in a month regardless of how many hours they actually work. A worker who works zero hours still incurs the full 4,800 Yuan regular wage.

## Turn 10 - Generic Agent

QUESTION: Is the inventory holding cost of 15 Yuan per unit applied to the ending inventory of each month from January through June, or only to the ending inventory of months January through May

## Turn 10 - User Simulator

The available business facts do not specify whether the inventory holding cost of 15 Yuan per unit is applied to the ending inventory of each month from January through June, or only to the ending inventory of months January through May. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For the purpose of this model, should we assume that the inventory holding cost of 15 Yuan per unit is applied to the ending inventory of each month from January through June

## Turn 11 - User Simulator

Yes, for the purpose of this model, assume that the inventory holding cost of 15 Yuan per unit is applied to the ending inventory of each month from January through June.

## Turn 12 - Generic Agent

QUESTION: Is the backorder cost of 35 Yuan per unit applied to the number of units backordered at the end of each month from January through May, or is it applied to the cumulative total of all backordered units across all months

## Turn 12 - User Simulator

The backorder cost of 35 Yuan per unit is applied to the number of units backordered at the end of each month from January through May.

## Turn 13 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a given month, or is outsourcing capacity unlimited

## Turn 13 - User Simulator

The available business facts do not specify any upper limit on the number of units that can be outsourced in a given month. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the purpose of this model, should we assume that outsourcing capacity is unlimited in each month

## Turn 14 - User Simulator

Yes, for the purpose of this model, assume that outsourcing capacity is unlimited in each month.

## Turn 15 - Generic Agent

QUESTION: Is there any upper limit on the number of workers that can be hired in a given month, or is hiring capacity unlimited

## Turn 15 - User Simulator

The available business facts do not specify any upper limit on the number of workers that can be hired in a given month. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the purpose of this model, should we assume that hiring capacity is unlimited in each month

## Turn 16 - User Simulator

Yes, for the purpose of this model, assume that hiring capacity is unlimited in each month.

## Turn 17 - Generic Agent

QUESTION: Is there any upper limit on the number of workers that can be fired in a given month, or is firing capacity unlimited

## Turn 17 - User Simulator

The available business facts do not specify any upper limit on the number of workers that can be fired in a given month. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: For the purpose of this model, should we assume that firing capacity is unlimited in each month

## Turn 18 - User Simulator

Yes, for the purpose of this model, assume that firing capacity is unlimited in each month.

## Turn 19 - Generic Agent

QUESTION: Is the raw material cost of 90 Yuan per unit applied only to units produced in-house, or does it also apply to outsourced units

## Turn 19 - User Simulator

The raw material cost of 90 Yuan per unit applies only to units produced in-house. It does not apply to outsourced units.

## Turn 20 - Generic Agent

QUESTION: Is the sales price of 300 Yuan per unit applied to all units sold, including those that fulfill backorders from prior months

## Turn 20 - User Simulator

Yes, the sales price of 300 Yuan per unit is applied to all units sold, including those that fulfill backorders from prior months.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the workforce size at the end of June must be at least some minimum number, or can the workforce be reduced to zero

## Turn 21 - User Simulator

The available business facts do not specify any minimum workforce size requirement at the end of June. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: For the purpose of this model, should we assume that there is no minimum workforce size requirement at the end of June

## Turn 22 - User Simulator

Yes, for the purpose of this model, assume that there is no minimum workforce size requirement at the end of June.

## Turn 23 - Generic Agent

QUESTION: Is the workforce size required to be an integer number of workers in each month

## Turn 23 - User Simulator

The available business facts do not explicitly state whether the workforce size must be an integer number of workers in each month. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: For the purpose of this model, should we assume that the workforce size must be an integer number of workers in each month

## Turn 24 - User Simulator

Yes, for the purpose of this model, assume that the workforce size must be an integer number of workers in each month.

## Turn 25 - Generic Agent

QUESTION: Is the number of units produced in-house required to be an integer in each month

## Turn 25 - User Simulator

The available business facts do not explicitly state whether the number of units produced in-house must be an integer in each month. This point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: For the purpose of this model, should we assume that the number of units produced in-house must be an integer in each month

## Turn 26 - User Simulator

Yes, for the purpose of this model, assume that the number of units produced in-house must be an integer in each month.

## Turn 27 - Generic Agent

QUESTION: Is the number of units outsourced required to be an integer in each month

## Turn 27 - User Simulator

The available business facts do not explicitly state whether the number of units outsourced must be an integer in each month. This point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: For the purpose of this model, should we assume that the number of units outsourced must be an integer in each month

## Turn 28 - User Simulator

Yes, for the purpose of this model, assume that the number of units outsourced must be an integer in each month.

## Turn 29 - Generic Agent

QUESTION: Is the ending inventory at the end of each month required to be an integer number of units

## Turn 29 - User Simulator

The available business facts do not explicitly state whether the ending inventory at the end of each month must be an integer number of units. This point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: For the purpose of this model, should we assume that the ending inventory at the end of each month must be an integer number of units

## Turn 30 - User Simulator

Yes, for the purpose of this model, assume that the ending inventory at the end of each month must be an integer number of units.