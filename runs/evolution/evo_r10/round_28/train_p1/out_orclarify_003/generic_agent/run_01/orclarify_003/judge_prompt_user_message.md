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

QUESTION: When you say the workforce can be hired or fired, is the number of workers allowed to change at the start of each month (so January's production can use a workforce different from the initial 1,000), and can workers be both hired and fired within the same month, or only one direction per month?

## Turn 1 - User Simulator

Yes, the workforce can change at the start of each month, so January’s production can use a workforce different from the initial 1,000.

Workers can be both hired and fired within the same month. There is no restriction limiting changes to only one direction per month.

## Turn 2 - Generic Agent

QUESTION: For the overtime limit, is the 20 hours per worker per month a cap on the total overtime hours worked by that worker in a month (so a worker can work up to 180 hours total), and is overtime available to all workers in the workforce each month?

## Turn 2 - User Simulator

Yes, the 20 hours per worker per month is a cap on the total overtime hours worked by that worker in a month, so a worker can work up to 180 hours total. Overtime is available to all workers in the workforce each month.

## Turn 3 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is this charged on the total number of units backordered at the end of each month (i.e., the cumulative unfulfilled demand carried into the next month), or is it charged only on the newly unfulfilled units in that month?

## Turn 3 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the total number of units backordered at the end of each month, which is the cumulative unfulfilled demand carried into the next month.

## Turn 4 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is this charged on the ending inventory at the end of each month (including June), or only on the ending inventory for months January through May (excluding June)?

## Turn 4 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory at the end of each month, including June.

## Turn 5 - Generic Agent

QUESTION: When you say orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units, is there a priority or cost-based ordering to these sources (e.g., use inventory first, then in-house, then outsource), or can the model freely choose how much to draw from each source as long as the total meets demand?

## Turn 5 - User Simulator

The model can freely choose how much to draw from each source (previous month's inventory, current in-house production, and outsourced units) as long as the total meets demand. There is no required priority or cost-based ordering to these sources.

## Turn 6 - Generic Agent

QUESTION: For the sales price of 300 Yuan per unit sold, is this revenue recognized when the unit is actually delivered to the customer (i.e., when demand is fulfilled, including backordered units delivered in a later month), or is it recognized in the month the demand originally occurred?

## Turn 6 - User Simulator

The sales price of 300 Yuan per unit is recognized when the unit is actually delivered to the customer, meaning when demand is fulfilled, including backordered units delivered in a later month.

## Turn 7 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is this applied only to units produced in-house, and does it also apply to units that are produced in-house but end up in inventory (not immediately sold), or only to units that are both produced in-house and sold?

## Turn 7 - User Simulator

The raw material cost of 90 Yuan per unit is applied only to units produced in-house. It applies to all units produced in-house, including those that end up in inventory and are not immediately sold.

## Turn 8 - Generic Agent

QUESTION: For the outsourcing cost of 200 Yuan per unit, is this the only cost associated with outsourced units (i.e., no additional raw material or labor cost on top of the 200 Yuan), and does outsourcing have any capacity limit or is it unlimited?

## Turn 8 - User Simulator

Yes, the 200 Yuan per unit is the only cost associated with outsourced units; there are no additional raw material or labor costs on top of that. Outsourcing has no capacity limit and is unlimited.

## Turn 9 - Generic Agent

QUESTION: For the regular wage of 30 Yuan per hour for 160 hours per worker, is this a fixed monthly cost of 4,800 Yuan per worker (160 × 30) that is paid regardless of how many hours are actually used, meaning the total labor cost is simply 4,800 times the number of workers plus 40 times the total overtime hours?

## Turn 9 - User Simulator

Yes, the regular wage is a fixed monthly cost of 4,800 Yuan per worker (160 hours × 30 Yuan/hour) that is paid regardless of how many hours are actually used. The total labor cost is simply 4,800 times the number of workers plus 40 times the total overtime hours.

## Turn 10 - Generic Agent

QUESTION: For the minimum ending inventory requirement of 10,000 units at the end of June, does this 10,000 units need to be on hand after fulfilling all of June's demand (including any backorders from prior months that are fulfilled in June), or is it a separate requirement that must be met in addition to fulfilling June's demand?

## Turn 10 - User Simulator

The 10,000 units must be on hand after fulfilling all of June's demand, including any backorders from prior months that are fulfilled in June. It is not a separate requirement in addition to fulfilling June's demand; it is the remaining inventory after all June obligations are met.

## Turn 11 - Generic Agent

QUESTION: For the backorder mechanism, can backorders accumulate across multiple months (i.e., if demand in February is not fully met, the unmet portion carries into March and can be added to March's own unmet demand), or must each month's demand be fully met by the end of that month?

## Turn 11 - User Simulator

Backorders can accumulate across multiple months. If demand in February is not fully met, the unmet portion carries into March and can be added to March's own unmet demand.

## Turn 12 - Generic Agent

QUESTION: For the workforce, is there any minimum or maximum number of workers that must be maintained at any point during the six months, or can the workforce be reduced to zero if that is optimal?

## Turn 12 - User Simulator

There is no minimum or maximum number of workers that must be maintained at any point during the six months. The workforce can be reduced to zero if that is optimal.

## Turn 13 - Generic Agent

QUESTION: For the hiring and firing costs, are these one-time costs incurred when the workforce changes at the start of a month (i.e., 5,000 Yuan per worker hired and 8,000 Yuan per worker fired in that month), and are they independent of how long the worker stays or how many hours they work?

## Turn 13 - User Simulator

Yes, these are one-time costs incurred when the workforce changes at the start of a month: 5,000 Yuan per worker hired and 8,000 Yuan per worker fired in that month. They are independent of how long the worker stays or how many hours they work.

## Turn 14 - Generic Agent

QUESTION: For the in-house production, is the total in-house production in a month limited by the total available labor hours (regular plus overtime) divided by 5 hours per unit, or is there any other capacity constraint on in-house production?

## Turn 14 - User Simulator

The total in-house production in a month is limited by the total available labor hours (regular plus overtime) divided by 5 hours per unit. There are no other capacity constraints on in-house production.

## Turn 15 - Generic Agent

QUESTION: For the inventory balance, is the ending inventory at the end of each month calculated as: beginning inventory + in-house production + outsourced units - units delivered to meet demand (current month's demand plus any prior backorders fulfilled that month), and can this ending inventory be negative (representing backorders) or must it be non-negative with backorders tracked separately?

## Turn 15 - User Simulator

The ending inventory at the end of each month is calculated as: beginning inventory + in-house production + outsourced units - units delivered to meet demand (current month's demand plus any prior backorders fulfilled that month). This ending inventory must be non-negative, with backorders tracked separately.

## Turn 16 - Generic Agent

QUESTION: For the backorder tracking, is the backorder at the end of each month calculated as: beginning backorder + current month's demand - units delivered that month, where units delivered can come from beginning inventory, in-house production, and outsourced units, and the backorder must be non-negative?

## Turn 16 - User Simulator

Yes, the backorder at the end of each month is calculated as: beginning backorder + current month's demand - units delivered that month, where units delivered can come from beginning inventory, in-house production, and outsourced units. The backorder must be non-negative.

## Turn 17 - Generic Agent

QUESTION: For the relationship between inventory and backorders, can a month have both positive ending inventory and positive ending backorders simultaneously, or must one of them be zero in each month?

## Turn 17 - User Simulator

A month cannot have both positive ending inventory and positive ending backorders simultaneously. One of them must be zero in each month.

## Turn 18 - Generic Agent

QUESTION: For the net profit calculation, is the total net profit simply: total revenue from all units delivered over the six months minus all costs (raw material, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost items?

## Turn 18 - User Simulator

Yes, the total net profit is simply: total revenue from all units delivered over the six months minus all costs (raw material, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost items.

## Turn 19 - Generic Agent

QUESTION: For the initial inventory of 15,000 units at the start of January, is this inventory available to fulfill January's demand (20,000 units) along with January's in-house production and outsourced units, and does the 15,000 units incur any holding cost in January or is it only the ending inventory that incurs holding cost?

## Turn 19 - User Simulator

Yes, the initial inventory of 15,000 units at the start of January is available to fulfill January's demand along with January's in-house production and outsourced units. The 15,000 units do not incur any holding cost in January; only the ending inventory at the end of each month incurs holding cost.

## Turn 20 - Generic Agent

QUESTION: For the workforce at the start of January, is the initial 1,000 workers available for January's production, and can hiring or firing occur at the start of January (before January's production) in addition to the initial 1,000?

## Turn 20 - User Simulator

Yes, the initial 1,000 workers are available for January's production. Hiring or firing can occur at the start of January, before January's production, in addition to the initial 1,000.

## Turn 21 - Generic Agent

QUESTION: For the workforce balance, is the workforce at the start of each month calculated as: previous month's workforce + workers hired at the start of this month - workers fired at the start of this month, and is the workforce used for production in that month the workforce at the start of that month (after any hiring/firing)?

## Turn 21 - User Simulator

Yes, the workforce at the start of each month is calculated as: previous month's workforce + workers hired at the start of this month - workers fired at the start of this month. The workforce used for production in that month is the workforce at the start of that month, after any hiring or firing.

## Turn 22 - Generic Agent

QUESTION: For the overtime hours, is the total overtime hours in a month limited to 20 times the number of workers in that month, and is the total in-house production limited by (160 × workers + overtime hours) / 5, where overtime hours can be any value from 0 to 20 × workers?

## Turn 22 - User Simulator

Yes, the total overtime hours in a month are limited to 20 times the number of workers in that month. The total in-house production is limited by (160 × workers + overtime hours) / 5, where overtime hours can be any value from 0 to 20 × workers.

## Turn 23 - Generic Agent

QUESTION: For the units delivered in a month, is the total units delivered limited by the total available units (beginning inventory + in-house production + outsourced units), and can the model choose to deliver fewer units than available (leaving some in inventory) even if there is unmet demand, or must all available units be used to fulfill demand first before any inventory is carried forward?

## Turn 23 - User Simulator

The total units delivered in a month is limited by the total available units (beginning inventory + in-house production + outsourced units). The model can choose to deliver fewer units than available, leaving some in inventory, even if there is unmet demand. There is no requirement that all available units must be used to fulfill demand first before any inventory is carried forward.

## Turn 24 - Generic Agent

QUESTION: For the backorder and inventory mutual exclusivity constraint (one must be zero in each month), does this apply to the ending values at the end of each month, and is this a hard constraint that must be satisfied in the model formulation?

## Turn 24 - User Simulator

Yes, the mutual exclusivity constraint applies to the ending values at the end of each month. It is a hard constraint that must be satisfied in the model formulation.

## Turn 25 - Generic Agent

QUESTION: For the demand fulfillment, is the total demand to be fulfilled in a month equal to the current month's forecast demand plus any backorders carried in from the previous month, and is the total units delivered in that month used to satisfy this combined demand?

## Turn 25 - User Simulator

Yes, the total demand to be fulfilled in a month is equal to the current month's forecast demand plus any backorders carried in from the previous month. The total units delivered in that month are used to satisfy this combined demand.

## Turn 26 - Generic Agent

QUESTION: For the backorder at the end of June, is there any requirement that all backorders must be cleared by the end of June (i.e., ending backorder in June must be zero), or can backorders remain at the end of June?

## Turn 26 - User Simulator

Yes, all backorders must be cleared by the end of June. The ending backorder in June must be zero; no outstanding customer orders can remain after June.

## Turn 27 - Generic Agent

QUESTION: For the workforce, are the number of workers hired and fired in each month required to be integer values, or can they be fractional?

## Turn 27 - User Simulator

The number of workers hired and fired in each month must be integer values.

## Turn 28 - Generic Agent

QUESTION: For the in-house production and outsourced units, are these required to be integer values, or can they be fractional?

## Turn 28 - User Simulator

The in-house production and outsourced units can be fractional values.

## Turn 29 - Generic Agent

QUESTION: For the units delivered in each month, is this required to be an integer value, or can it be fractional?

## Turn 29 - User Simulator

The units delivered in each month can be fractional.

## Turn 30 - Generic Agent

QUESTION: For the inventory and backorder values, are these required to be integer values, or can they be fractional?

## Turn 30 - User Simulator

The inventory and backorder values can be fractional.