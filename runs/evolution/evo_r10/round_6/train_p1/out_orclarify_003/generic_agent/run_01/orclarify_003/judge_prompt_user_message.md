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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a given month (so total overtime capacity = 20 × number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime capacity for the month is 20 hours multiplied by the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage of 30 Yuan/hour for 160 hours per worker, is this a fixed monthly cost of 4,800 Yuan per worker regardless of how many hours are actually used, or is it paid only for the hours actually worked (up to 160)?

## Turn 2 - User Simulator

It is a fixed monthly cost of 4,800 Yuan per worker, paid regardless of how many hours are actually used.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the demand for that month must be satisfied by the sum of (beginning inventory + current in-house production + current outsourcing), or can you also use inventory that was already available in earlier months (i.e., inventory carries forward and can be used in any later month)?

## Turn 3 - User Simulator

Inventory carries forward. In each month, the demand for that month (plus any backorders from prior months) is satisfied by the sum of beginning inventory (which includes any unused inventory from earlier months), current in-house production, and current outsourcing.

## Turn 4 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire workers in any month from January through June, or are hiring/firing decisions only allowed at the start of January?

## Turn 4 - User Simulator

Hiring and firing decisions can be made in any month from January through June.

## Turn 5 - Generic Agent

QUESTION: When a worker is hired in a given month, do they immediately contribute their full 160 regular hours (and up to 20 overtime hours) in that same month, or do they only start contributing from the following month?

## Turn 5 - User Simulator

A worker hired in a given month immediately contributes their full 160 regular hours (and up to 20 overtime hours) in that same month.

## Turn 6 - Generic Agent

QUESTION: When a worker is fired in a given month, do they still contribute their full 160 regular hours (and up to 20 overtime hours) in that same month, or are they removed and do not contribute in the month they are fired?

## Turn 6 - User Simulator

A worker fired in a given month does not contribute in that same month. They are removed and do not provide any regular or overtime hours in the month they are fired.

## Turn 7 - Generic Agent

QUESTION: Can a worker be both hired and fired in the same month, or is the workforce change in each month either hiring only or firing only (or neither)?

## Turn 7 - User Simulator

The workforce change in each month is either hiring only, firing only, or neither. A worker cannot be both hired and fired in the same month.

## Turn 8 - Generic Agent

QUESTION: Is there a minimum or maximum workforce size that must be maintained in any month, or can the workforce go as low as zero workers if that is optimal?

## Turn 8 - User Simulator

There is no minimum or maximum workforce size that must be maintained in any month. The workforce can go as low as zero workers if that is optimal.

## Turn 9 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit, is this charged on the total number of units backordered at the end of each month (i.e., the cumulative unfulfilled demand carried into the next month), or is it charged only on the newly unfulfilled units in that specific month?

## Turn 9 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the total number of units backordered at the end of each month (i.e., the cumulative unfulfilled demand carried into the next month).

## Turn 10 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is this charged on the ending inventory at the end of each month (including June), or only on the ending inventory for months January through May (excluding June)?

## Turn 10 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory at the end of each month, including June.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced in a given month, or is outsourcing capacity unlimited?

## Turn 11 - User Simulator

Outsourcing capacity is unlimited.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on the number of units that can be produced in-house in a given month beyond what the available labor hours (regular + overtime) allow, or is in-house production capacity solely determined by the labor hours available?

## Turn 12 - User Simulator

In-house production capacity is solely determined by the available labor hours (regular + overtime).

## Turn 13 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold, is this revenue earned for every unit that fulfills demand (including backordered units fulfilled in a later month), or only for units sold in the month the demand originally occurred?

## Turn 13 - User Simulator

The sales price of 300 Yuan per unit is earned for every unit that fulfills demand, including backordered units fulfilled in a later month.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be backordered (i.e., a maximum backorder level), or can backorders accumulate without limit as long as they are eventually fulfilled?

## Turn 14 - User Simulator

There is no maximum backorder level. Backorders can accumulate without limit as long as they are eventually fulfilled.

## Turn 15 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production, is this cost incurred only when a unit is actually produced in-house, regardless of whether it is sold immediately or held in inventory?

## Turn 15 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred only when a unit is actually produced in-house, regardless of whether it is sold immediately or held in inventory.

## Turn 16 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit, is this the only cost associated with outsourced units (i.e., no additional raw material cost is incurred for outsourced units), or is the 90 Yuan raw material cost also applied to outsourced units on top of the 200 Yuan outsourcing cost?

## Turn 16 - User Simulator

The 200 Yuan outsourcing cost is the only cost associated with outsourced units. No additional raw material cost is incurred for outsourced units.

## Turn 17 - Generic Agent

QUESTION: Regarding the workforce, is the number of workers in each month required to be an integer, or can it be treated as a continuous variable?

## Turn 17 - User Simulator

The number of workers in each month must be an integer.

## Turn 18 - Generic Agent

QUESTION: Regarding the production and outsourcing quantities, must the number of units produced in-house and the number of units outsourced in each month be integers, or can they be treated as continuous variables?

## Turn 18 - User Simulator

The number of units produced in-house and the number of units outsourced in each month must be integers.

## Turn 19 - Generic Agent

QUESTION: Regarding the inventory and backorder quantities, must the ending inventory and backorder levels in each month be integers, or can they be treated as continuous variables?

## Turn 19 - User Simulator

The ending inventory and backorder levels in each month must be integers.

## Turn 20 - Generic Agent

QUESTION: Regarding the overtime hours, must the total overtime hours used in each month be an integer, or can they be treated as a continuous variable (e.g., 10.5 hours)?

## Turn 20 - User Simulator

The total overtime hours used in each month can be treated as a continuous variable.

## Turn 21 - Generic Agent

QUESTION: Regarding the regular hours, must the total regular hours used in each month be an integer, or can they be treated as a continuous variable?

## Turn 21 - User Simulator

The total regular hours used in each month can be treated as a continuous variable.

## Turn 22 - Generic Agent

QUESTION: Regarding the workforce, if a worker is fired in a given month, is the firing cost of 8,000 Yuan charged per worker fired in that month, and if a worker is hired in a given month, is the hiring cost of 5,000 Yuan charged per worker hired in that month?

## Turn 22 - User Simulator

Yes, the firing cost of 8,000 Yuan is charged per worker fired in that month, and the hiring cost of 5,000 Yuan is charged per worker hired in that month.

## Turn 23 - Generic Agent

QUESTION: Regarding the workforce, is the number of workers at the start of each month (before any hiring or firing in that month) equal to the number of workers at the end of the previous month, or is there any other convention for how the workforce carries over between months?

## Turn 23 - User Simulator

The number of workers at the start of each month (before any hiring or firing in that month) is equal to the number of workers at the end of the previous month.

## Turn 24 - Generic Agent

QUESTION: Regarding the workforce, when you say a worker fired in a given month does not contribute in that same month, does this mean the firing decision is made at the beginning of the month (so the worker is removed before any production occurs that month), or at the end of the month (so the worker is present for the month but removed after)?

## Turn 24 - User Simulator

The firing decision is made at the beginning of the month, so the worker is removed before any production occurs that month.

## Turn 25 - Generic Agent

QUESTION: Regarding the workforce, when you say a worker hired in a given month immediately contributes in that same month, does this mean the hiring decision is made at the beginning of the month (so the worker is present for the full month's production)?

## Turn 25 - User Simulator

Yes, the hiring decision is made at the beginning of the month, so the worker is present for the full month's production.

## Turn 26 - Generic Agent

QUESTION: Regarding the workforce, if both hiring and firing could theoretically occur in the same month (which you said is not allowed), but in practice the workforce can only go up or down in a given month, does this mean the workforce in month t is determined by: workforce in month t = workforce at end of month t-1 + hires in month t - fires in month t, where hires and fires are non-negative integers and at most one of them is non-zero in any given month?

## Turn 26 - User Simulator

Yes, that is correct. The workforce in month t is determined by: workforce in month t = workforce at end of month t-1 + hires in month t - fires in month t, where hires and fires are non-negative integers and at most one of them is non-zero in any given month.

## Turn 27 - Generic Agent

QUESTION: Regarding the demand fulfillment, in each month, the total units available to fulfill demand (beginning inventory + in-house production + outsourcing) must be at least equal to the demand for that month plus any backorders from prior months. If the available units exceed the total demand, the excess becomes ending inventory. If the available units are less than the total demand, the shortfall becomes the new backorder level. Is this correct?

## Turn 27 - User Simulator

Yes, that is correct.

## Turn 28 - Generic Agent

QUESTION: Regarding the objective function, is the total net profit calculated as: total revenue (300 × total units sold over 6 months) minus total costs (raw material + outsourcing + inventory holding + backorder + regular wages + overtime wages + hiring + firing), with no other revenue or cost components?

## Turn 28 - User Simulator

Yes, that is correct.

## Turn 29 - Generic Agent

QUESTION: Regarding the "total units sold over 6 months," does this equal the total demand over all 6 months (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500 = 174,500 units), since all demand must eventually be fulfilled (including backorders), or could some demand remain unfulfilled at the end of June?

## Turn 29 - User Simulator

Yes, the total units sold over 6 months equals the total demand over all 6 months (174,500 units), since all demand must be fulfilled by the end of June. No demand can remain unfulfilled.

## Turn 30 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June, does this mean that after fulfilling all demand (including any backorders) in June, the remaining inventory must be at least 10,000 units?

## Turn 30 - User Simulator

Yes, that is correct. After fulfilling all demand (including any backorders) in June, the remaining inventory must be at least 10,000 units.