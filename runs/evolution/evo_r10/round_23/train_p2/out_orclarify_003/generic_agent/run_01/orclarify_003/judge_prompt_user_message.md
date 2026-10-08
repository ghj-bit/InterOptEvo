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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime = 20 × number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours available in a given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you said it's paid regardless of utilization — does that mean the company pays 1,000 workers × 160 hours × 30 Yuan every month even if they produce nothing, or is the regular wage paid only for the hours actually used (up to 160 per worker)?

## Turn 2 - User Simulator

The company pays the regular wage for all 160 hours per worker every month, regardless of how many hours are actually used for production. So if there are 1,000 workers in a month, the regular wage cost is 1,000 × 160 × 30 Yuan for that month, even if they produce nothing.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does the fulfillment order matter for cost purposes — that is, must the model use up previous-month inventory first, then in-house production, then outsourcing — or can any combination of the three sources be used in any order as long as the total meets demand?

## Turn 3 - User Simulator

The fulfillment order does not matter for cost purposes. Any combination of the three sources—previous-month inventory, current in-house production, and outsourced units—can be used in any order, as long as the total quantity meets the demand (current plus any backorders).

## Turn 4 - Generic Agent

QUESTION: Can the workforce (number of workers) change from month to month, meaning the company can hire or fire workers in any of the six months, or is the workforce fixed at 1,000 workers for the entire January–June period?

## Turn 4 - User Simulator

The workforce can change from month to month. The company can hire or fire workers in any of the six months.

## Turn 5 - Generic Agent

QUESTION: When workers are hired or fired in a given month, are they available for production in that same month (i.e., the workforce level used for that month's production capacity is the level after hiring/firing), or do they only become available starting the next month?

## Turn 5 - User Simulator

Workers hired or fired in a given month are available for production in that same month. The workforce level used for that month's production capacity is the level after hiring and firing decisions for that month.

## Turn 6 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit — is this charged on the total quantity of unfulfilled demand carried over at the end of each month (i.e., the ending backorder level), or is it charged on the flow of units that become backordered during that month?

## Turn 6 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the ending backorder level at the end of each month.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how many units can be backordered (i.e., can all unmet demand be carried forward indefinitely), or is there a maximum backorder level or a requirement that all backorders must be cleared by a certain month?

## Turn 7 - User Simulator

There is no maximum backorder level, but all backorders must be cleared by the end of June. No outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many units can be outsourced in a given month, or can the company outsource an unlimited number of units per month?

## Turn 8 - User Simulator

There is no limit on how many units can be outsourced in a given month. The company can outsource an unlimited number of units per month.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how many workers can be hired or fired in a single month, or can the workforce change by any amount in any month?

## Turn 9 - User Simulator

There is no limit on how many workers can be hired or fired in a single month. The workforce can change by any amount in any month.

## Turn 10 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June — does this 10,000 units need to be in addition to fulfilling all demand and backorders through June, or does it mean the net inventory position (after all sales and backorder fulfillment) must be at least 10,000?

## Turn 10 - User Simulator

It means the net inventory position at the end of June, after fulfilling all demand and backorders through June, must be at least 10,000 units.

## Turn 11 - Generic Agent

QUESTION: Is there a minimum number of workers the company must maintain in any month (for example, at least 0, or some positive floor), or can the workforce theoretically drop to zero in a month?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit — is this charged on the ending inventory level at the end of each month (including June), or only on the ending inventory for months January through May (excluding June)?

## Turn 12 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory level at the end of each month, including June.

## Turn 13 - Generic Agent

QUESTION: When the company produces units in-house, does the raw material cost of 90 Yuan per unit apply to all in-house units produced that month (regardless of whether they are sold, held in inventory, or used to fulfill backorders), or only to units that are actually sold?

## Turn 13 - User Simulator

The raw material cost of 90 Yuan per unit applies to all in-house units produced that month, regardless of whether they are sold, held in inventory, or used to fulfill backorders.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June — for example, must the company end with a specific number of workers, or can the workforce at the end of June be any non-negative number?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Can the workforce level in any month be a fractional number of workers (e.g., 1,050.5 workers), or must the number of workers always be a whole number?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit — is this revenue earned only when a unit is actually sold to a customer (i.e., when demand or backorder is fulfilled), or is it recognized at the time of production?

## Turn 16 - User Simulator

The sales revenue of 300 Yuan per unit is earned only when a unit is actually sold to a customer, meaning when demand or a backorder is fulfilled.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the workforce at the start of January must be exactly 1,000 (i.e., no hiring or firing allowed before January begins), or can the company adjust the workforce before the planning horizon starts?

## Turn 17 - User Simulator

The workforce at the start of January is fixed at 1,000 employees. No hiring or firing is allowed before January begins.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June — for example, must the company end with a specific number of workers, or can the workforce at the end of June be any non-negative number?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Can the number of workers in any month be a fractional value (e.g., 1,050.5 workers), or must it always be a whole number?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there any minimum number of workers the company must maintain in any month, or can the workforce theoretically drop to zero?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June — for example, must the company end with a specific number of workers, or can the workforce at the end of June be any non-negative number?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Can the number of workers in any month be a fractional value (e.g., 1,050.5 workers), or must it always be a whole number?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Is there any minimum number of workers the company must maintain in any month, or can the workforce theoretically drop to zero?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June — for example, must the company end with a specific number of workers, or can the workforce at the end of June be any non-negative number?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Can the number of workers in any month be a fractional value (e.g., 1,050.5 workers), or must it always be a whole number?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Is there any minimum number of workers the company must maintain in any month, or can the workforce theoretically drop to zero?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June — for example, must the company end with a specific number of workers, or can the workforce at the end of June be any non-negative number?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Can the number of workers in any month be a fractional value (e.g., 1,050.5 workers), or must it always be a whole number?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is there any minimum number of workers the company must maintain in any month, or can the workforce theoretically drop to zero?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June — for example, must the company end with a specific number of workers, or can the workforce at the end of June be any non-negative number?

## Turn 30 - User Simulator

The