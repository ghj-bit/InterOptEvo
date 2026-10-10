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

QUESTION: Is the 10,000-unit minimum ending inventory requirement a hard constraint that must be strictly satisfied, or is it a soft target where violations are penalized in the objective function?

## Turn 1 - User Simulator

It is a hard constraint. The ending inventory at the end of June must be at least 10,000 units.

## Turn 2 - Generic Agent

QUESTION: Is the 20-hour overtime limit per worker per month a hard constraint that must be strictly satisfied, or is it a soft target where violations are penalized in the objective function?

## Turn 2 - User Simulator

It is a hard constraint. Total overtime hours per month for the entire workforce cannot exceed 20 hours per worker.

## Turn 3 - Generic Agent

QUESTION: Can the workforce size change every month, or is it fixed at 1,000 employees for the entire six-month period?

## Turn 3 - User Simulator

The workforce size can change every month. We can hire or fire workers, with a hiring cost of 5,000 Yuan per new worker and a firing cost of 8,000 Yuan per worker.

## Turn 4 - Generic Agent

QUESTION: Is the workforce size required to be an integer number of workers, or can it be treated as a continuous variable in the model?

## Turn 4 - User Simulator

The workforce size must be an integer number of workers.

## Turn 5 - Generic Agent

QUESTION: Is the number of units produced in-house each month required to be an integer, or can it be treated as a continuous variable in the model?

## Turn 5 - User Simulator

The number of units produced in-house each month must be an integer.

## Turn 6 - Generic Agent

QUESTION: Is the number of units outsourced each month required to be an integer, or can it be treated as a continuous variable in the model?

## Turn 6 - User Simulator

The number of units outsourced each month must be an integer.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements for the production and workforce plan that have not been mentioned yet?

## Turn 7 - User Simulator

Yes, all backorders must be cleared by the end of June. That means no outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 8 - Generic Agent

QUESTION: Is the requirement that all backorders must be cleared by the end of June a hard constraint that must be strictly satisfied, or is it a soft target where violations are penalized in the objective function?

## Turn 8 - User Simulator

It is a hard constraint. All backorders must be cleared by the end of June; no outstanding customer orders can remain after June.

## Turn 9 - Generic Agent

QUESTION: Is the number of units sold each month required to be an integer, or can it be treated as a continuous variable in the model?

## Turn 9 - User Simulator

The number of units sold each month must be an integer.

## Turn 10 - Generic Agent

QUESTION: Is the number of units held in inventory at the end of each month required to be an integer, or can it be treated as a continuous variable in the model?

## Turn 10 - User Simulator

The number of units held in inventory at the end of each month must be an integer.

## Turn 11 - Generic Agent

QUESTION: Is the number of units backordered at the end of each month required to be an integer, or can it be treated as a continuous variable in the model?

## Turn 11 - User Simulator

The number of units backordered at the end of each month must be an integer.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:**
- Maximize total net profit over the six-month period (January to June).

**Decision Variables (all integer):**
- Workforce size per month (integer)
- Units produced in-house per month (integer)
- Units outsourced per month (integer)
- Units sold per month (integer)
- Ending inventory per month (integer)
- Backorders per month (integer)

**Parameters:**
- Time horizon: 6 months (January to June)
- Initial workforce (start of January): 1,000 employees
- Initial inventory (start of January): 15,000 units
- Sales price: 300 Yuan per unit sold
- Raw material cost: 90 Yuan per unit (in-house production only)
- Outsourcing cost: 200 Yuan per unit (finished tables, all-inclusive)
- Inventory holding cost: 15 Yuan per unit per month (end-of-month inventory)
- Backorder cost: 35 Yuan per unit per month (unfulfilled demand carried over)
- Labor requirement: 5 labor hours per in-house unit
- Regular working hours per worker per month: 160 hours
- Regular wage rate: 30 Yuan per hour (paid for 160 hours regardless of utilization)
- Overtime wage rate: 40 Yuan per hour
- Maximum overtime hours per worker per month: 20 hours (hard constraint)
- Hiring cost: 5,000 Yuan per new worker
- Firing cost: 8,000 Yuan per worker
- Demand forecast: Jan=20,000, Feb=40,000, Mar=42,000, Apr=35,000, May=19,000, Jun=18,500

**Constraints (all hard):**
1. Overtime hours per worker per month ≤ 20 hours
2. Ending inventory at end of June ≥ 10,000 units
3. All backorders must be cleared by end of June (backorders at end of June = 0)
4. Workforce size is integer
5. All production, sales, inventory, and backorder quantities are integer

**Flow Logic:**
- Unfulfilled demand is back-ordered and must be met in subsequent months
- Orders (current demand + backorders) are fulfilled using: previous month's inventory + current in-house production + current outsourced units
- Workforce can change each month with associated hiring/firing costs
- Regular wages are paid for 160 hours per worker regardless of actual utilization