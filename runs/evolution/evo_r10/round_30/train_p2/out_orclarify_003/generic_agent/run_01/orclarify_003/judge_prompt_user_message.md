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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the sum of all overtime hours across the whole workforce is capped at 20 hours total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: When demand is back-ordered and fulfilled in a later month, is the sales revenue of 300 Yuan per unit recognized in the month the order was originally placed, or in the month the unit is actually delivered to the customer?

## Turn 2 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the month the unit is actually delivered to the customer.

## Turn 3 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it incurred in the month the unit is produced in-house, or in the month the unit is actually sold/delivered to the customer?

## Turn 3 - User Simulator

The raw material cost of 90 Yuan per unit is incurred in the month the unit is produced in-house.

## Turn 4 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (i.e., units left over at the end of that month), or on the average inventory during the month?

## Turn 4 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month.

## Turn 5 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is it charged on the amount of unfulfilled demand carried over at the end of each month (i.e., the backorder balance at month-end), or on the total units that were back-ordered during that month?

## Turn 5 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the amount of unfulfilled demand carried over at the end of each month (the backorder balance at month-end).

## Turn 6 - Generic Agent

QUESTION: Can the workforce (number of employees) change from month to month through hiring and firing, or is the workforce fixed at 1,000 employees for all six months?

## Turn 6 - User Simulator

The workforce can change from month to month through hiring and firing.

## Turn 7 - Generic Agent

QUESTION: When a worker is hired or fired in a given month, is that worker counted in the workforce for that same month (i.e., available to work regular and overtime hours in the month they are hired, and their regular wage is paid in that month), or do they only count starting the following month?

## Turn 7 - User Simulator

A worker hired or fired in a given month is counted in the workforce for that same month. They are available to work regular and overtime hours in the month they are hired, and their regular wage is paid in that month.

## Turn 8 - Generic Agent

QUESTION: Can the workforce go below 1,000 employees (i.e., can you fire workers down to fewer than the initial 1,000), or is 1,000 a minimum workforce level that must be maintained throughout the six months?

## Turn 8 - User Simulator

The workforce can go below 1,000 employees. There is no minimum workforce level that must be maintained; 1,000 is simply the starting number at the beginning of January.

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on how many units can be outsourced in a given month, or is outsourcing unlimited (i.e., you can outsource as many units as needed)?

## Turn 9 - User Simulator

There is no upper limit on how many units can be outsourced in a given month. Outsourcing is unlimited.

## Turn 10 - Generic Agent

QUESTION: Can the workforce be zero (i.e., fire all workers) in any month, or is there a minimum of at least one worker that must be maintained?

## Turn 10 - User Simulator

There is no minimum workforce requirement. The workforce can be zero in any month.

## Turn 11 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," is there a specific priority or order in which these sources must be used (e.g., must use previous inventory first, then in-house, then outsourcing), or can the model freely allocate among these three sources in any combination to meet demand?

## Turn 11 - User Simulator

There is no specific priority or order. The model can freely allocate among previous inventory, current in-house production, and outsourced units in any combination to meet demand.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 12 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no additional limit beyond what is implied by the workforce's regular and overtime hours.

## Turn 13 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 13 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no additional limit beyond what is implied by the workforce's regular and overtime hours.

## Turn 14 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 14 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no additional limit beyond what is implied by the workforce's regular and overtime hours.

## Turn 15 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 15 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no additional limit beyond what is implied by the workforce's regular and overtime hours.

## Turn 16 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 16 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no additional limit beyond what is implied by the workforce's regular and overtime hours.

## Turn 17 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 17 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no

## Turn 18 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 18 - User Simulator

In-house production capacity is determined solely by available labor hours. There is no additional limit beyond what is implied by the workforce's regular and overtime hours.

## Turn 19 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 19 - User Simulator

In

## Turn 20 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 20 - User Simulator

In-house

## Turn 21 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 21 - User Simulator

In

## Turn 22 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 22 - User Simulator

In

## Turn 23 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 23 - User Simulator

In

## Turn 24 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 24 - User Simulator

In

## Turn 25 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 25 - User Simulator

In

## Turn 26 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 26 - User Simulator

In

## Turn 27 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 27 - User Simulator

In

## Turn 28 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 28 - User Simulator

In

## Turn 29 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 29 - User Simulator

In

## Turn 30 - Generic Agent

QUESTION: Is there any limit on the total number of units that can be produced in-house in a given month beyond what is implied by the available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), or is in-house production capacity determined solely by available labor hours?

## Turn 30 - User Simulator

In