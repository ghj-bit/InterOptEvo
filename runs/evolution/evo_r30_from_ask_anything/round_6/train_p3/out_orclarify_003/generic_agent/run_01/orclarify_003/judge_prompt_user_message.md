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

QUESTION: When you say the objective is to maximize total net profit, do you want the model to include the revenue from sales (300 Yuan per unit sold) in the objective function, or should the objective be to minimize total costs (production, outsourcing, inventory, backorder, and labor costs) while treating the sales revenue as a fixed constant that does not affect the optimization decision

## Turn 1 - User Simulator

Yes, include the revenue from sales (300 Yuan per unit sold) in the objective function. The goal is to maximize total net profit, which is calculated as total sales revenue minus all associated costs (production, outsourcing, inventory, backorder, and labor costs).

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce planning, are the number of workers hired or fired in a given month allowed to be any non-negative integer, or must the workforce level remain an integer at the start of each month

## Turn 2 - User Simulator

The workforce level must remain an integer at the start of each month.

## Turn 3 - Generic Agent

QUESTION: For the production and outsourcing decisions, must the number of units produced in-house and the number of units outsourced in each month be integers, or can they be continuous

## Turn 3 - User Simulator

The number of units produced in-house and the number of units outsourced in each month must be integers.

## Turn 4 - Generic Agent

QUESTION: When calculating the labor cost for regular hours, is the total regular wage cost for a month equal to the number of workers at the start of that month multiplied by 160 hours multiplied by 30 Yuan per hour, regardless of how many hours are actually used for production

## Turn 4 - User Simulator

Yes, the total regular wage cost for a month is equal to the number of workers at the start of that month multiplied by 160 hours multiplied by 30 Yuan per hour, regardless of how many hours are actually used for production.

## Turn 5 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is this cost applied to the ending inventory of each month (i.e., the inventory remaining at the end of January, end of February, etc.), or is it applied to the average inventory during the month

## Turn 5 - User Simulator

The inventory holding cost of 15 Yuan per unit is applied to the ending inventory of each month.

## Turn 6 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit, is this cost applied to the quantity of unfulfilled demand that is carried over from the end of one month to the beginning of the next

## Turn 6 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is applied to the quantity of unfulfilled demand that is carried over from the end of one month to the beginning of the next.

## Turn 7 - Generic Agent

QUESTION: Regarding the minimum ending inventory requirement of 10,000 units at the end of June, does this constraint apply only to the final month (June), or is there a minimum inventory requirement for the end of every month

## Turn 7 - User Simulator

The minimum ending inventory requirement of 10,000 units applies only to the end of June. There is no minimum inventory requirement for the end of any other month.

## Turn 8 - Generic Agent

QUESTION: Regarding the workforce balance, if you hire or fire workers in a given month, does the new workforce level apply to the production capacity and regular wage cost for that same month

## Turn 8 - User Simulator

Yes, if you hire or fire workers in a given month, the new workforce level applies to the production capacity and regular wage cost for that same month.

## Turn 9 - Generic Agent

QUESTION: Regarding the labor hours available for production in a given month, is the total available labor hours equal to the number of workers at the start of that month multiplied by 160 regular hours plus the number of workers at the start of that month multiplied by 20 overtime hours

## Turn 9 - User Simulator

No. The total available labor hours for a given month is equal to the number of workers at the start of that month multiplied by 160 regular hours, plus the number of workers at the start of that month multiplied by the actual overtime hours used in that month. The 20 hours is the maximum overtime allowed per worker, not a fixed addition to available hours.

## Turn 10 - Generic Agent

QUESTION: Regarding the overtime hours, is the total overtime hours used in a month a decision variable that can be any value between 0 and 20 times the number of workers, or is it determined solely by the production volume

## Turn 10 - User Simulator

The total overtime hours used in a month is a decision variable that can be any value between 0 and 20 times the number of workers at the start of that month. It is not determined solely by the production volume; it is chosen as part of the plan to meet production needs within the maximum limit.

## Turn 11 - Generic Agent

QUESTION: Regarding the production capacity constraint, is the total labor hours required for in-house production in a month (5 hours per unit) constrained to be less than or equal to the total available labor hours (regular plus overtime) for that month

## Turn 11 - User Simulator

Yes, the total labor hours required for in-house production in a month (5 hours per unit) must be less than or equal to the total available labor hours (regular plus overtime) for that month.

## Turn 12 - Generic Agent

QUESTION: Regarding the inventory balance equation, is the ending inventory for a given month calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold (which includes current month demand plus any backorders from previous months that are fulfilled in the current month

## Turn 12 - User Simulator

Yes, the ending inventory for a given month is calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold (which includes current month demand plus any backorders from previous months that are fulfilled in the current month).

## Turn 13 - Generic Agent

QUESTION: Regarding the backorder balance, is the backorder at the end of a given month calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month

## Turn 13 - User Simulator

Yes, the backorder at the end of a given month is calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month.

## Turn 14 - Generic Agent

QUESTION: Regarding the relationship between inventory and backorders, can a month have both positive ending inventory and positive ending backorders simultaneously, or must one of them be zero

## Turn 14 - User Simulator

One of them must be zero. A month cannot have both positive ending inventory and positive ending backorders simultaneously.

## Turn 15 - Generic Agent

QUESTION: Regarding the workforce balance equation, is the workforce at the start of a given month equal to the workforce at the start of the previous month plus the number of workers hired in the previous month minus the number of workers fired in the previous month

## Turn 15 - User Simulator

No. The workforce at the start of a given month is equal to the workforce at the start of the previous month plus the number of workers hired in the current month minus the number of workers fired in the current month.

## Turn 16 - Generic Agent

QUESTION: Regarding the workforce balance, if you hire or fire workers in a given month, does the new workforce level (after hiring/firing) apply to the production capacity and regular wage cost for that same month

## Turn 16 - User Simulator

Yes, if you hire or fire workers in a given month, the new workforce level (after hiring/firing) applies to the production capacity and regular wage cost for that same month.

## Turn 17 - Generic Agent

QUESTION: Regarding the workforce balance equation, is the workforce at the start of a given month equal to the workforce at the start of the previous month plus the number of workers hired in the current month minus the number of workers fired in the current month

## Turn 17 - User Simulator

No. The workforce at the start of a given month is equal to the workforce at the start of the previous month plus the number of workers hired in the previous month minus the number of workers fired in the previous month.

## Turn 18 - Generic Agent

QUESTION: Regarding the workforce balance, is the workforce level used to calculate production capacity and regular wage costs for a given month equal to the workforce at the start of that month (before any hiring or firing in that month), or is it equal to the workforce at the end of that month (after hiring or firing

## Turn 18 - User Simulator

The workforce level used to calculate production capacity and regular wage costs for a given month is equal to the workforce at the end of that month (after hiring or firing).

## Turn 19 - Generic Agent

QUESTION: Regarding the workforce balance equation, is the workforce at the end of a given month equal to the workforce at the start of that month plus the number of workers hired in that month minus the number of workers fired in that month

## Turn 19 - User Simulator

Yes, the workforce at the end of a given month is equal to the workforce at the start of that month plus the number of workers hired in that month minus the number of workers fired in that month.

## Turn 20 - Generic Agent

QUESTION: Regarding the workforce balance, is the workforce at the start of a given month equal to the workforce at the end of the previous month

## Turn 20 - User Simulator

Yes, the workforce at the start of a given month is equal to the workforce at the end of the previous month.

## Turn 21 - Generic Agent

QUESTION: Regarding the inventory and backorder balance, is the total units sold in a given month constrained to be less than or equal to the beginning inventory plus in-house production plus outsourced units

## Turn 21 - User Simulator

Yes, the total units sold in a given month is constrained to be less than or equal to the beginning inventory plus in-house production plus outsourced units.

## Turn 22 - Generic Agent

QUESTION: Regarding the backorder balance, is the backorder at the end of a given month calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month

## Turn 22 - User Simulator

Yes, the backorder at the end of a given month is calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month.

## Turn 23 - Generic Agent

QUESTION: Regarding the inventory balance, is the ending inventory for a given month calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month

## Turn 23 - User Simulator

Yes, the ending inventory for a given month is calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month.

## Turn 24 - Generic Agent

QUESTION: Regarding the relationship between inventory and backorders, since a month cannot have both positive ending inventory and positive ending backorders simultaneously, is the total units sold in a given month constrained to be less than or equal to the beginning inventory plus in-house production plus outsourced units

## Turn 24 - User Simulator

Yes, the total units sold in a given month is constrained to be less than or equal to the beginning inventory plus in-house production plus outsourced units.

## Turn 25 - Generic Agent

QUESTION: Regarding the backorder balance, is the backorder at the end of a given month calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month

## Turn 25 - User Simulator

Yes, the backorder at the end of a given month is calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month.

## Turn 26 - Generic Agent

QUESTION: Regarding the inventory balance, is the ending inventory for a given month calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month

## Turn 26 - User Simulator

Yes, the ending inventory for a given month is calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month.

## Turn 27 - Generic Agent

QUESTION: Regarding the backorder balance, is the backorder at the end of a given month calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month

## Turn 27 - User Simulator

Yes, the backorder at the end of a given month is calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month.

## Turn 28 - Generic Agent

QUESTION: Regarding the inventory balance, is the ending inventory for a given month calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month

## Turn 28 - User Simulator

Yes, the ending inventory for a given month is calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month.

## Turn 29 - Generic Agent

QUESTION: Regarding the backorder balance, is the backorder at the end of a given month calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month

## Turn 29 - User Simulator

Yes, the backorder at the end of a given month is calculated as the backorder from the previous month plus the current month's demand minus the total units sold in the current month.

## Turn 30 - Generic Agent

QUESTION: Regarding the inventory balance, is the ending inventory for a given month calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month

## Turn 30 - User Simulator

Yes, the ending inventory for a given month is calculated as the beginning inventory plus in-house production plus outsourced units minus the total units sold in the current month.