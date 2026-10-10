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

QUESTION: Is the 15,000-unit initial inventory at the start of January available to fulfill January demand, or is it reserved for a different purpose?

## Turn 3 - User Simulator

The 15,000-unit initial inventory is available to fulfill January demand.

## Turn 4 - Generic Agent

QUESTION: Is the 10,000-unit minimum ending inventory requirement a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 4 - User Simulator

It is a hard constraint. The ending inventory at the end of June must be at least 10,000 units.

## Turn 5 - Generic Agent

QUESTION: Is the 200 Yuan outsourcing cost per unit a fixed price regardless of the quantity outsourced, or does it vary based on volume or other factors?

## Turn 5 - User Simulator

It is a fixed price of 200 Yuan per unit, regardless of the quantity outsourced.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum limit on the number of units that can be outsourced per month, or is the outsourcing quantity unlimited?

## Turn 6 - User Simulator

The outsourcing quantity is unlimited.

## Turn 7 - Generic Agent

QUESTION: Is the 5,000 Yuan hiring cost incurred per worker hired in a given month, and is the 8,000 Yuan firing cost incurred per worker fired in a given month?

## Turn 7 - User Simulator

Yes, the 5,000 Yuan hiring cost is incurred per worker hired in a given month, and the 8,000 Yuan firing cost is incurred per worker fired in a given month.

## Turn 8 - Generic Agent

QUESTION: Is the 300 Yuan sales price per unit applied to all units sold, including those fulfilled from backorders in subsequent months?

## Turn 8 - User Simulator

Yes, the 300 Yuan sales price is applied to all units sold, including those fulfilled from backorders in subsequent months.

## Turn 9 - Generic Agent

QUESTION: Is the 35 Yuan backorder cost per unit incurred for each month that a unit remains unfulfilled, or is it a one-time cost when the unit is first backordered?

## Turn 9 - User Simulator

It is incurred for each month that a unit remains unfulfilled.

## Turn 10 - Generic Agent

QUESTION: Is the 15 Yuan inventory holding cost per unit incurred for each month that a unit is held in inventory, or is it a one-time cost when the unit enters inventory?

## Turn 10 - User Simulator

It is incurred for each month that a unit is held in inventory.

## Turn 11 - Generic Agent

QUESTION: Is the 90 Yuan raw material cost per unit incurred only for units produced in-house, or does it also apply to outsourced units?

## Turn 11 - User Simulator

It is incurred only for units produced in-house.

## Turn 12 - Generic Agent

QUESTION: Is the 160 regular working hours per worker per month a fixed capacity that is paid for regardless of how many hours are actually used, or is it a maximum capacity that can be partially utilized?

## Turn 12 - User Simulator

It is a fixed capacity that is paid for regardless of how many hours are actually used.

## Turn 13 - Generic Agent

QUESTION: Is the workforce size at the start of each month determined by the previous month's workforce plus hires minus firings, or is there a different mechanism for determining monthly workforce levels?

## Turn 13 - User Simulator

Yes, the workforce size at the start of each month is determined by the previous month's workforce plus hires minus firings.

## Turn 14 - Generic Agent

QUESTION: Is the 5 labor hours per in-house unit a fixed requirement, or can it vary based on worker skill or other factors?

## Turn 14 - User Simulator

It is a fixed requirement of 5 labor hours per in-house unit.

## Turn 15 - Generic Agent

QUESTION: Is there a minimum number of workers that must be maintained at all times, or can the workforce be reduced to zero?

## Turn 15 - User Simulator

There is no minimum number of workers that must be maintained. The workforce can be reduced to zero.

## Turn 16 - Generic Agent

QUESTION: Is there a maximum number of workers that can be hired or fired in a single month, or are hiring and firing quantities unlimited?

## Turn 16 - User Simulator

Hiring and firing quantities are unlimited.

## Turn 17 - Generic Agent

QUESTION: Is the 15,000-unit initial inventory at the start of January subject to the 15 Yuan per unit per month holding cost for January, or is the holding cost only applied to inventory held at the end of each month?

## Turn 17 - User Simulator

The holding cost is only applied to inventory held at the end of each month.

## Turn 18 - Generic Agent

QUESTION: Is the 35 Yuan backorder cost per unit per month applied to the total number of units backordered at the end of each month, or is it applied to the number of units that were backordered during that month?

## Turn 18 - User Simulator

It is applied to the total number of units backordered at the end of each month.

## Turn 19 - Generic Agent

QUESTION: Is the 15 Yuan inventory holding cost per unit per month applied to the total number of units in inventory at the end of each month, or is it applied to the number of units that entered inventory during that month?

## Turn 19 - User Simulator

It is applied to the total number of units in inventory at the end of each month.

## Turn 20 - Generic Agent

QUESTION: Is the 300 Yuan sales price per unit applied to all units sold in a given month, regardless of whether they were produced in-house, outsourced, or came from inventory?

## Turn 20 - User Simulator

Yes, the 300 Yuan sales price is applied to all units sold in a given month, regardless of whether they were produced in-house, outsourced, or came from inventory.

## Turn 21 - Generic Agent

QUESTION: Is the 90 Yuan raw material cost per unit incurred for all units produced in-house during a month, regardless of whether they are sold in that month or held in inventory?

## Turn 21 - User Simulator

Yes

## Turn 22 - Generic Agent

QUESTION: Is the 200 Yuan outsourcing cost per unit incurred for all units outsourced during a month, regardless of whether they are sold in that month or held in inventory?

## Turn 22 - User Simulator

Yes

## Turn 23 - Generic Agent

QUESTION: Is the 30 Yuan per hour regular wage paid for all 160 regular hours per worker per month, even if the worker is not fully utilized?

## Turn 23 - User Simulator

Yes

## Turn 24 - Generic Agent

QUESTION: Is the 40 Yuan per hour overtime wage paid only for the actual overtime hours worked, up to the 20-hour per worker per month cap?

## Turn 24 - User Simulator

Yes

## Turn 25 - Generic Agent

QUESTION: Is the 5,000 Yuan hiring cost incurred for each new worker hired in a given month, and is the 8,000 Yuan firing cost incurred for each worker fired in a given month?

## Turn 25 - User Simulator

Yes

## Turn 26 - Generic Agent

QUESTION: Is the 15,000-unit initial inventory at the start of January available to fulfill January demand, or is it reserved for a different purpose?

## Turn 26 - User Simulator

The 15,000-unit initial inventory is available to fulfill January demand.

## Turn 27 - Generic Agent

QUESTION: Is the 10,000-unit minimum ending inventory requirement a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 27 - User Simulator

It is a hard constraint.

## Turn 28 - Generic Agent

QUESTION: Is the 20-hour overtime limit per worker per month a hard constraint that must be strictly satisfied, or is it a soft target that can be violated with a penalty?

## Turn 28 - User Simulator

It is a hard constraint.

## Turn 29 - Generic Agent

QUESTION: Is the 160 regular working hours per worker per month a hard constraint that limits the maximum regular hours that can be used, or is it a fixed capacity that is paid for regardless of utilization?

## Turn 29 - User Simulator

It is a fixed capacity that is paid for regardless of utilization.

## Turn 30 - Generic Agent

QUESTION: Is the 5 labor hours per in-house unit a fixed requirement that must be met exactly, or can it vary based on worker skill or other factors

## Turn 30 - User Simulator

It is a fixed requirement that must be met exactly.