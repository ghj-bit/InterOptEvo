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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a given month (so total overtime is bounded by 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at a fixed total of 20 hours?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime hours for the month are bounded by 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization — does this mean every worker employed in a month incurs a fixed cost of 160 × 30 = 4,800 Yuan for that month, even if they work fewer than 160 regular hours (e.g., because production is low)?

## Turn 2 - User Simulator

Yes, every worker employed in a month incurs a fixed cost of 160 × 30 = 4,800 Yuan for that month, regardless of how many regular hours they actually work.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units — does this mean that in any given month, the fulfillment of that month's demand (plus any backorders) can draw from beginning inventory, in-house production, and outsourcing in any combination, with no restriction on the order or priority in which these sources are used?

## Turn 3 - User Simulator

Yes, in any given month, the fulfillment of that month's demand plus any backorders can draw from beginning inventory, current in-house production, and outsourced units in any combination, with no restriction on the order or priority in which these sources are used.

## Turn 4 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit for unfulfilled demand carried over to the next month — is this cost incurred once per unit per month it remains backordered (i.e., if a unit is backordered for 2 months, the cost is 70 Yuan), or is it a one-time cost of 35 Yuan per unit regardless of how many months it stays backordered?

## Turn 4 - User Simulator

The backorder cost of 35 Yuan per unit is incurred once per unit per month it remains backordered. So if a unit is backordered for 2 months, the total backorder cost for that unit is 70 Yuan.

## Turn 5 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit for inventory held at the end of a month — does this apply to all units in ending inventory, or only to units that were produced in-house (since raw material cost is only for in-house production)?

## Turn 5 - User Simulator

The inventory holding cost of 15 Yuan per unit applies to all units in ending inventory, regardless of whether they were produced in-house or outsourced.

## Turn 6 - Generic Agent

QUESTION: Regarding the minimum ending inventory requirement of 10,000 units at the end of June — does this 10,000 units need to be on hand after fulfilling all of June's demand (and any backorders carried into June), meaning it is additional to what is needed to meet June's demand?

## Turn 6 - User Simulator

Yes, the 10,000 units must be on hand at the end of June after fulfilling all of June's demand and any backorders carried into June. It is additional to what is needed to meet June's demand.

## Turn 7 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is this revenue recognized in the month the unit is actually delivered to the customer (i.e., when the backorder is fulfilled), or is it recognized in the month the demand originally occurred?

## Turn 7 - User Simulator

The sales price of 300 Yuan per unit is recognized in the month the unit is actually delivered to the customer, i.e., when the backorder is fulfilled.

## Turn 8 - Generic Agent

QUESTION: Regarding the workforce — can the number of workers change from month to month through hiring and firing, and is there any constraint on the timing (e.g., can you hire and fire within the same month, or must hiring happen at the start of the month and firing at the end)?

## Turn 8 - User Simulator

Yes, the number of workers can change from month to month through hiring and firing. There is no specific constraint on the timing within a month; hiring and firing can occur as needed to adjust the workforce for that month.

## Turn 9 - Generic Agent

QUESTION: Regarding the workforce — is there any upper or lower bound on the number of workers that can be employed in any given month (e.g., a maximum workforce size or a minimum number of workers that must be retained)?

## Turn 9 - User Simulator

There is no upper or lower bound on the number of workers that can be employed in any given month, other than the initial workforce of 1,000 employees at the start of January.

## Turn 10 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit applicable only to in-house production — is this cost incurred for every in-house unit produced in a month, regardless of whether that unit is sold in the same month or held in inventory?

## Turn 10 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred for every in-house unit produced in a month, regardless of whether that unit is sold in the same month or held in inventory.

## Turn 11 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit for finished tables — is this cost incurred for every outsourced unit in the month it is produced/received, regardless of whether it is sold in that same month or held in inventory?

## Turn 11 - User Simulator

Yes, the outsourcing cost of 200 Yuan per unit is incurred for every outsourced unit in the month it is produced/received, regardless of whether it is sold in that same month or held in inventory.

## Turn 12 - Generic Agent

QUESTION: Regarding the labor hours — the 5 labor hours per in-house unit can be drawn from both regular hours (up to 160 per worker) and overtime hours (up to 20 per worker), correct? In other words, total in-house production in a month is limited by (number of workers × 160 + number of workers × 20) / 5 units, with the regular portion always available and the overtime portion incurring the 40 Yuan/hour rate?

## Turn 12 - User Simulator

Yes, the 5 labor hours per in-house unit can be drawn from both regular hours (up to 160 per worker) and overtime hours (up to 20 per worker). Total in-house production in a month is limited by (number of workers × 160 + number of workers × 20) / 5 units, with the regular portion always available and the overtime portion incurring the 40 Yuan/hour rate.

## Turn 13 - Generic Agent

QUESTION: Regarding the overtime cost — since regular hours are paid at a fixed 4,800 Yuan per worker regardless of utilization, is the overtime cost simply 40 Yuan per overtime hour used (i.e., 40 × 5 = 200 Yuan per in-house unit produced beyond the regular capacity of 160/5 = 32 units per worker), with no additional regular-hour cost for those overtime-produced units?

## Turn 13 - User Simulator

Yes, the overtime cost is simply 40 Yuan per overtime hour used. Since regular hours are already paid as a fixed 4,800 Yuan per worker regardless of utilization, there is no additional regular-hour cost for units produced using overtime hours.

## Turn 14 - Generic Agent

QUESTION: Regarding the net profit objective — is the total net profit calculated as total revenue (300 Yuan per unit delivered) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other costs or taxes to consider?

## Turn 14 - User Simulator

Yes, the total net profit is calculated as total revenue (300 Yuan per unit delivered) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other costs or taxes to consider.

## Turn 15 - Generic Agent

QUESTION: Regarding the backorder — can backorders accumulate across multiple months (i.e., if demand in month 2 exceeds available supply, the unmet portion carries to month 3, and if month 3 also can't fully cover it, the remaining unmet portion carries to month 4, etc.), or is there a limit on how many months a backorder can persist?

## Turn 15 - User Simulator

Yes, backorders can accumulate across multiple months. If demand in a month exceeds available supply, the unmet portion carries to the next month, and if that month also cannot fully cover it, the remaining unmet portion carries forward, and so on. The only requirement is that all backorders must be cleared by the end of June.

## Turn 16 - Generic Agent

QUESTION: Regarding the requirement that all backorders must be cleared by the end of June — does this mean that by the end of June, there can be no outstanding backorders (i.e., all cumulative demand from January through June must have been fulfilled by the end of June), in addition to the 10,000-unit minimum ending inventory requirement?

## Turn 16 - User Simulator

Yes, by the end of June, there can be no outstanding backorders. All cumulative demand from January through June must have been fulfilled by the end of June, in addition to the 10,000-unit minimum ending inventory requirement.

## Turn 17 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January — is this inventory available to fulfill January's demand (and any prior backorders, though there are none since January is the first month), and does it incur the 15 Yuan per unit holding cost if it remains in inventory at the end of January?

## Turn 17 - User Simulator

Yes, the initial inventory of 15,000 units at the start of January is available to fulfill January's demand. If any of those units remain in inventory at the end of January, they incur the 15 Yuan per unit holding cost.

## Turn 18 - Generic Agent

QUESTION: Regarding the hiring and firing costs — is the hiring cost of 5,000 Yuan per new worker incurred in the month the worker is hired, and the firing cost of 8,000 Yuan per worker incurred in the month the worker is fired, with no additional costs (such as severance or training) beyond these?

## Turn 18 - User Simulator

Yes, the hiring cost of 5,000 Yuan per new worker is incurred in the month the worker is hired, and the firing cost of 8,000 Yuan per worker is incurred in the month the worker is fired, with no additional costs beyond these.

## Turn 19 - Generic Agent

QUESTION: Regarding the workforce in a given month — if a worker is hired in month t, do they contribute their full 160 regular hours and up to 20 overtime hours in that same month t, or do they only start contributing from month t+1?

## Turn 19 - User Simulator

If a worker is hired in month t, they contribute their full 160 regular hours and up to 20 overtime hours in that same month t.

## Turn 20 - Generic Agent

QUESTION: Regarding the workforce in a given month — if a worker is fired in month t, do they still contribute their full 160 regular hours and up to 20 overtime hours in that same month t (i.e., they work the full month before being let go), or do they not contribute any hours in the month they are fired?

## Turn 20 - User Simulator

If a worker is fired in month t, they still contribute their full 160 regular hours and up to 20 overtime hours in that same month t.

## Turn 21 - Generic Agent

QUESTION: Regarding the workforce in a given month — if a worker is both hired and fired in the same month t, do they still contribute their full 160 regular hours and up to 20 overtime hours in that month, or would such a situation be disallowed?

## Turn 21 - User Simulator

A worker who is both hired and fired in the same month t would still contribute their full 160 regular hours and up to 20 overtime hours in that month.

## Turn 22 - Generic Agent

QUESTION: Regarding the regular wage cost — if a worker is hired and fired in the same month t, do they still incur the full 4,800 Yuan regular wage cost for that month, or is the wage prorated?

## Turn 22 - User Simulator

Yes, if a worker is hired and fired in the same month t, they still incur the full 4,800 Yuan regular wage cost for that month.

## Turn 23 - Generic Agent

QUESTION: Regarding the inventory balance — in each month, is the ending inventory calculated as: beginning inventory + in-house production + outsourcing − units delivered (to fulfill current demand and any backorders), with the constraint that ending inventory must be non-negative (i.e., you cannot have negative inventory, only backorders)?

## Turn 23 - User Simulator

Yes, in each month, the ending inventory is calculated as: beginning inventory + in-house production + outsourcing − units delivered (to fulfill current demand and any backorders), with the constraint that ending inventory must be non-negative.

## Turn 24 - Generic Agent

QUESTION: Regarding the backorder balance — in each month, is the ending backorder calculated as: beginning backorder + current month's demand − units delivered, with the constraint that ending backorder must be non-negative (i.e., you cannot have negative backorders, only inventory)?

## Turn 24 - User Simulator

Yes, in each month, the ending backorder is calculated as: beginning backorder + current month's demand − units delivered, with the constraint that ending backorder must be non-negative.

## Turn 25 - Generic Agent

QUESTION: Regarding the relationship between inventory and backorders — can a month have both positive ending inventory and positive ending backorders simultaneously, or must one of them be zero in each month (i.e., you cannot have both surplus inventory and unmet demand at the same time)?

## Turn 25 - User Simulator

A month cannot have both positive ending inventory and positive ending backorders simultaneously. One of them must be zero in each month.

## Turn 26 - Generic Agent

QUESTION: Regarding the units delivered in a month — is the total units delivered in month t equal to the sum of units used to fulfill month t's current demand plus units used to clear backorders from prior months, and is this total bounded above by (beginning inventory + in-house production + outsourcing) in that month?

## Turn 26 - User Simulator

Yes, the total units delivered in month t is equal to the sum of units used to fulfill month t's current demand plus units used to clear backorders from prior months, and this total is bounded above by (beginning inventory + in-house production + outsourcing) in that month.

## Turn 27 - Generic Agent

QUESTION: Regarding the revenue recognition — since sales revenue is recognized when the unit is delivered, and a unit delivered in month t to fulfill a backorder from month s (where s < t) generates 300 Yuan in month t, does this mean the 300 Yuan revenue is simply counted in month t's contribution to total profit, with no discounting or time-value adjustment?

## Turn 27 - User Simulator

Yes, the 300 Yuan revenue is simply counted in month t's contribution to total profit, with no discounting or time-value adjustment.

## Turn 28 - Generic Agent

QUESTION: Regarding the in-house production capacity — the total in-house production in month t is limited by (number of workers in month t × 180) / 5 units, where 180 = 160 regular + 20 overtime hours per worker. Is there any other constraint on in-house production (such as a maximum number of units that can be produced in-house per month regardless of workforce size)?

## Turn 28 - User Simulator

No, there is no other constraint on in-house production beyond the labor-hour limit of (number of workers in month t × 180) / 5 units.

## Turn 29 - Generic Agent

QUESTION: Regarding outsourcing — is there any upper limit on the number of units that can be outsourced in a given month, or can you outsource any number of units as needed?

## Turn 29 - User Simulator

There is no upper limit on the number of units that can be outsourced in a given month. You can outsource any number of units as needed.

## Turn 30 - Generic Agent

QUESTION: Regarding the workforce balance — is the number of workers at the end of month t equal to: number of workers at the start of month t + hires in month t − fires in month t, with the constraint that the number of workers at the start of January is 1,000 and the number of workers must be non-negative in all months?

## Turn 30 - User Simulator

Yes, the number of workers at the end of month t is equal to: number of workers at the start of month t + hires in month t − fires in month t, with the constraint that the number of workers at the start of January is 1,000 and the number of workers must be non-negative in all months.