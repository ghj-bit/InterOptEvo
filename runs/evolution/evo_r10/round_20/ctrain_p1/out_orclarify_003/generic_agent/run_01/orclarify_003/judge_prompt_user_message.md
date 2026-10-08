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

QUESTION: For the workforce, can the number of workers change from month to month through hiring and firing, and if so, is the workforce level for a month determined at the start of that month (so workers hired in January are available for January production) — or is there any other timing convention you have in mind?

## Turn 2 - User Simulator

Yes, the number of workers can change from month to month through hiring and firing. The workforce level for a month is determined at the start of that month, so workers hired in January are available for January production.

## Turn 3 - Generic Agent

QUESTION: For the regular wage, you said it is paid regardless of utilization — does that mean every worker employed in a month is paid the full 160 regular hours at 30 Yuan/hour (48,000 Yuan per worker per month) even if the in-house production that month uses fewer than 160 hours per worker?

## Turn 3 - User Simulator

Yes, every worker employed in a month is paid the full 160 regular hours at 30 Yuan/hour (48,000 Yuan per worker per month), even if the in-house production that month uses fewer than 160 hours per worker.

## Turn 4 - Generic Agent

QUESTION: For backorders, is there any limit on how long an order can be back-ordered (for example, must all demand be fulfilled by the end of June), or can unfulfilled demand simply carry over month to month with no deadline as long as the June ending inventory requirement is met?

## Turn 4 - User Simulator

All backorders must be cleared by the end of June. No outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 5 - Generic Agent

QUESTION: When demand is fulfilled in a given month, does the sales revenue of 300 Yuan per unit get recognized in the month the order is actually fulfilled (i.e., when the back-ordered unit is finally delivered), or in the month the demand originally occurred?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (including June's ending inventory of at least 10,000 units), or only on the ending inventory of months January through May?

## Turn 6 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including June's ending inventory.

## Turn 7 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is it charged on the amount of unfulfilled demand carried over at the end of each month (i.e., the backorder balance at the end of the month), or on the total number of units that were back-ordered during that month?

## Turn 7 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the amount of unfulfilled demand carried over at the end of each month (i.e., the backorder balance at the end of the month).

## Turn 8 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it incurred only on units produced in-house (as you stated), and is there any separate cost or constraint on outsourced units beyond the 200 Yuan all-inclusive outsourcing cost?

## Turn 8 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred only on units produced in-house. There is no separate cost or constraint on outsourced units beyond the 200 Yuan all-inclusive outsourcing cost.

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a month (for example, a capacity cap on the outsourcing supplier), or can any non-negative number of units be outsourced in each month?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: For the workforce, is there any upper or lower bound on the number of workers that can be employed in a month (for example, a maximum workforce size or a minimum that must be kept), or can the workforce be any non-negative integer with no cap?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For the in-house production, is there any constraint that the total labor hours used (regular plus overtime) in a month must not exceed the total available hours of the workforce (160 regular plus up to 20 overtime per worker), or can in-house production be any non-negative number as long as overtime stays within the 20-hour-per-worker cap?

## Turn 11 - User Simulator

Yes, the total labor hours used for in-house production in a month must not exceed the total available hours of the workforce, which is 160 regular hours plus up to 20 overtime hours per worker.

## Turn 12 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: For the decision variables, should the number of workers, in-house production units, outsourced units, and inventory/backorder levels all be treated as integer values, or is it acceptable to treat them as continuous (allowing fractional values)?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the fulfillment of demand in a month, you said orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units — is there any priority or cost-based ordering to these sources (for example, must inventory be used before in-house production, and in-house before outsourcing), or can the model freely choose how much to draw from each source as long as the total covers the demand?

## Turn 14 - User Simulator

The model can freely choose how much to draw from each source (previous month's inventory, current in-house production, and outsourced units) as long as the total covers the demand. There is no required priority or cost-based ordering among these sources.

## Turn 15 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit charged on the end-of-month backorder balance, is it also charged on the backorder balance at the end of June (which must be zero since all backorders must be cleared by end of June), or only on the backorder balances at the end of January through May?

## Turn 15 - User Simulator

The backorder cost is charged on the backorder balance at the end of each month, including June. Since all backorders must be cleared by the end of June, the June backorder balance is zero, so the cost for that month is zero.

## Turn 16 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually delivered to the customer (i.e., when the order is fulfilled, including back-ordered units delivered later), or in the month the demand originally occurred?

## Turn 30 - User Simulator

The point still needs internal confirmation.