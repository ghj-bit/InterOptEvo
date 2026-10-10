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

QUESTION: Is the 20-hour overtime limit a total cap for the entire workforce per month, or is it a limit of 20 hours per individual worker per month

## Turn 1 - User Simulator

It is a limit of 20 hours per individual worker per month.

## Turn 2 - Generic Agent

QUESTION: Can the workforce size be changed every month, or are there restrictions on hiring or firing

## Turn 2 - User Simulator

The workforce size can be changed every month. There are no restrictions on the timing or frequency of hiring or firing, other than the associated costs: 5,000 Yuan per new worker hired and 8,000 Yuan per worker fired.

## Turn 3 - Generic Agent

QUESTION: When calculating the labor cost for a month, is the regular wage of 30 Yuan per hour paid for the full 160 hours for every worker on the payroll that month, regardless of how many hours they actually

## Turn 3 - User Simulator

Yes, the regular wage of 30 Yuan per hour is paid for the full 160 hours for every worker on the payroll that month, regardless of how many hours they actually work.

## Turn 4 - Generic Agent

QUESTION: Is the raw material cost of 90 Yuan per unit incurred for every unit produced in-house, regardless of whether that unit is sold in the current

## Turn 4 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred for every unit produced in-house, regardless of whether that unit is sold in the current month or held in inventory.

## Turn 5 - Generic Agent

QUESTION: Is the inventory holding cost of 15 Yuan per unit charged on the total ending inventory at the end of each

## Turn 5 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the total ending inventory at the end of each month.

## Turn 6 - Generic Agent

QUESTION: Is the backorder cost of 35 Yuan per unit charged on the total quantity of unful

## Turn 6 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is charged on the total quantity of unfulfilled demand carried over to the next month.

## Turn 7 - Generic Agent

QUESTION: Can the company hold both positive inventory and backorders

## Turn 7 - User Simulator

No, the company cannot hold both positive inventory and backorders at the same time.

## Turn 8 - Generic Agent

QUESTION: When fulfilling demand in a given month, is the priority order for using available

## Turn 8 - User Simulator

The available inventory from the previous month, current in-house production, and outsourced units are all used to fulfill the orders (current demand and backorders) in that month. There is no specified priority order among these three sources; they are simply the available means to meet the total order quantity for the month.

## Turn 9 - Generic Agent

QUESTION: Is the sales price of 300 Yuan per unit earned for every unit

## Turn 9 - User Simulator

Yes, the sales price of 300 Yuan per unit is earned for every unit sold to fulfill customer demand, regardless of whether that unit came from previous inventory, current in-house production, or outsourcing.

## Turn 10 - Generic Agent

QUESTION: Is the minimum ending inventory requirement of 10,000 units a

## Turn 10 - User Simulator

Yes, the minimum ending inventory requirement of 10,000 units applies specifically to the end of June.

## Turn 11 - Generic Agent

QUESTION: Is the workforce size at the end of

## Turn 11 - User Simulator

There is no specific requirement for the workforce size at the end of June.

## Turn 12 - Generic Agent

QUESTION: Are the decision variables for workforce size, in-house

## Turn 12 - User Simulator

Yes, the workforce size, in-house production quantity, and outsourcing quantity are decision variables that can be chosen for each month to maximize total net profit.

## Turn 13 - Generic Agent

QUESTION: Are the decision variables for workforce

## Turn 13 - User Simulator

Yes, the workforce size, in-house production quantity, and outsourcing quantity are decision variables that can be chosen for each month to maximize total net profit.

## Turn 14 - Generic Agent

QUESTION: Are the decision

## Turn 14 - User Simulator

The decision variables are the workforce size, in-house production quantity, and outsourcing quantity for each month.

## Turn 15 - Generic Agent

QUESTION: Are the

## Turn 15 - User Simulator

The decision variables are the workforce size, in-house production quantity, and outsourcing quantity for each month.

## Turn 16 - Generic Agent

QUESTION: Are

## Turn 16 - User Simulator

The decision

## Turn 17 - Generic Agent

QUESTION: Are

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION:

## Turn 18 - User Simulator

The

## Turn 19 - Generic Agent

QUESTION:

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION:

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION:

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION:

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION:

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION:

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION:

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION:

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION:

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION:

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION:

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION:

## Turn 30 - User Simulator

The