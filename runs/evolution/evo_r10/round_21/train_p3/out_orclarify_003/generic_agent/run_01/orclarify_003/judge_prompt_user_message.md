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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker (so total overtime = 20 × number of workers that month), or is it a single aggregate cap of 20 hours for the whole workforce combined?

## Turn 1 - User Simulator

It is 20 hours per individual worker. So the total overtime available in any month is 20 hours multiplied by the number of workers on staff that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can you hire and fire workers in any month (including January), and is the workforce level for a month determined before or after that month's production — that is, if you hire in January, can those new workers contribute to January's production?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. If you hire in January, those new workers are available to contribute to January's production.

## Turn 3 - Generic Agent

QUESTION: When you fire a worker in a given month, does that worker still contribute to that month's production (i.e., firing takes effect from the next month), or is the worker removed before that month's production so they contribute nothing?

## Turn 3 - User Simulator

The worker is removed before that month's production, so they contribute nothing to that month.

## Turn 4 - Generic Agent

QUESTION: For the regular wage, you said it's paid regardless of utilization — does that mean each worker on staff in a month is paid the full 160 hours × 30 Yuan = 4,800 Yuan even if their hours aren't fully used, and is the workforce level for a month the number of workers on staff during that month (i.e., after any hiring/firing that month)?

## Turn 4 - User Simulator

Yes, each worker on staff in a month is paid the full 4,800 Yuan regardless of utilization. The workforce level for a month is the number of workers on staff during that month, after any hiring or firing that month.

## Turn 5 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (including June's ending inventory of at least 10,000 units), or only on the ending inventory of months January through May?

## Turn 5 - User Simulator

It is charged on the ending inventory of each month, including June's ending inventory.

## Turn 6 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is it charged on the amount of unfulfilled demand carried over at the end of each month (including any backorders at the end of June, if any), or only on backorders carried from one month to the next during January through May?

## Turn 6 - User Simulator

It is charged on the amount of unfulfilled demand carried over at the end of each month. However, since all backorders must be cleared by the end of June, there should be no backorders at the end of June.

## Turn 7 - Generic Agent

QUESTION: You mentioned that orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units. Does this mean that in any given month, the fulfillment priority is: first use beginning inventory, then in-house production, then outsourcing — or can you choose any combination of these three sources to meet demand in any order?

## Turn 7 - User Simulator

You can choose any combination of these three sources to meet demand in any order. There is no required priority; the plan can allocate fulfillment across beginning inventory, in-house production, and outsourcing as needed.

## Turn 8 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it charged only on units produced in-house (as you stated), and is there any additional cost for outsourced units beyond the 200 Yuan all-inclusive outsourcing cost?

## Turn 8 - User Simulator

Yes, the 90 Yuan raw material cost is charged only on units produced in-house. There is no additional cost for outsourced units beyond the 200 Yuan all-inclusive outsourcing cost.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced in a month, or is outsourcing capacity unlimited?

## Turn 9 - User Simulator

Outsourcing capacity is unlimited.

## Turn 10 - Generic Agent

QUESTION: Is there any minimum or maximum constraint on the workforce size in any month (e.g., a minimum number of workers that must be retained, or a maximum hiring rate per month), or can the workforce be any non-negative integer?

## Turn 10 - User Simulator

There is no minimum or maximum constraint on the workforce size in any month. The workforce can be any non-negative integer.

## Turn 11 - Generic Agent

QUESTION: For the sales price of 300 Yuan per unit sold — is revenue recognized only on units actually delivered to customers (i.e., demand fulfilled in the month it was due, or backorders fulfilled in a later month), or is revenue recognized on all units that were originally demanded, regardless of when they are delivered?

## Turn 11 - User Simulator

Revenue is recognized only on units actually delivered to customers.

## Turn 12 - Generic Agent

QUESTION: Since backorders must be cleared by the end of June, does that mean all demand from January through June must be fully satisfied by the end of June (i.e., total units delivered across all six months equals total demand of 175,500 units), or is it possible to leave some demand unfulfilled at the end of June and simply not count it as revenue?

## Turn 12 - User Simulator

All demand from January through June must be fully satisfied by the end of June. Total units delivered across all six months must equal the total demand of 175,500 units.

## Turn 13 - Generic Agent

QUESTION: For the ending inventory at the end of June (at least 10,000 units), does this inventory represent units that are produced or outsourced in June but not yet sold, and is the 10,000-unit minimum a hard constraint (i.e., the model must have at least 10,000 units in inventory at the end of June, on top of all demand being fulfilled)?

## Turn 13 - User Simulator

Yes, the ending inventory at the end of June represents units that are produced or outsourced in June but not yet sold. The 10,000-unit minimum is a hard constraint: the model must have at least 10,000 units in inventory at the end of June, on top of all demand being fulfilled.

## Turn 14 - Generic Agent

QUESTION: For the labor hours, each in-house unit requires 5 labor hours. Is the total labor hours available in a month equal to (number of workers × 160 regular hours) + (number of workers × 20 overtime hours), and can overtime hours be used for any in-house production in that month without restriction beyond the 20-hour per-worker cap?

## Turn 14 - User Simulator

Yes, the total labor hours available in a month equal (number of workers × 160 regular hours) + (number of workers × 20 overtime hours). Overtime hours can be used for any in-house production in that month without restriction beyond the 20-hour per-worker cap.

## Turn 15 - Generic Agent

QUESTION: For the workforce transition, if you start January with 1,000 workers, hire H workers, and fire F workers in January, is the workforce on staff during January equal to 1,000 + H - F, and does the same logic apply to each subsequent month (workforce in month t = workforce at end of month t-1 + hires in month t - fires in month t)?

## Turn 15 - User Simulator

Yes, the workforce on staff during January is 1,000 + H - F. The same logic applies to each subsequent month: workforce in month t = workforce at end of month t-1 + hires in month t - fires in month t.

## Turn 16 - Generic Agent

QUESTION: For the inventory balance in each month, is the relationship: ending inventory = beginning inventory + in-house production + outsourcing - units delivered to customers that month, where units delivered can come from any combination of beginning inventory, in-house production, and outsourcing?

## Turn 16 - User Simulator

Yes, that is correct. Ending inventory = beginning inventory + in-house production + outsourcing - units delivered to customers that month.

## Turn 17 - Generic Agent

QUESTION: For the backorder mechanism, if demand in a month exceeds the units available (beginning inventory + in-house production + outsourcing), the shortfall becomes a backorder carried to the next month. Is the backorder at the end of month t equal to the cumulative unfulfilled demand up to month t, and does the backorder cost of 35 Yuan apply to the backorder balance at the end of each month (i.e., the amount still unfulfilled at month-end)?

## Turn 17 - User Simulator

Yes, the backorder at the end of month t is the cumulative unfulfilled demand up to month t. The backorder cost of 35 Yuan applies to the backorder balance at the end of each month.

## Turn 18 - Generic Agent

QUESTION: For the net profit objective, is it: total revenue (300 × total units delivered) minus total costs (raw materials + outsourcing + inventory holding + backorder + regular wages + overtime wages + hiring + firing), with no other costs or revenue items?

## Turn 18 - User Simulator

Yes, that is correct. Net profit is total revenue (300 × total units delivered) minus total costs (raw materials + outsourcing + inventory holding + backorder + regular wages + overtime wages + hiring + firing), with no other costs or revenue items.

## Turn 19 - Generic Agent

QUESTION: For the overtime wage cost, is it 40 Yuan per overtime hour actually used (not per available overtime hour), meaning if a worker has 20 overtime hours available but only 10 are used, the overtime cost is 10 × 40 = 400 Yuan for that worker?

## Turn 19 - User Simulator

Yes, the overtime wage cost is 40 Yuan per overtime hour actually used. If a worker has 20 overtime hours available but only 10 are used, the overtime cost is 10 × 40 = 400 Yuan for that worker.

## Turn 20 - Generic Agent

QUESTION: For the regular wage, you confirmed each worker is paid 4,800 Yuan regardless of utilization. Does this mean the regular wage cost is simply 4,800 × (number of workers on staff in that month), and the regular hours (160 per worker) are only a capacity constraint on in-house production (i.e., in-house production × 5 ≤ workers × 160 + overtime hours used)?

## Turn 20 - User Simulator

Yes, the regular wage cost is simply 4,800 × (number of workers on staff in that month). The regular hours (160 per worker) are only a capacity constraint on in-house production, meaning in-house production × 5 ≤ workers × 160 + overtime hours used.

## Turn 21 - Generic Agent

QUESTION: For the inventory and backorder relationship, can a month have both positive ending inventory and positive backorders simultaneously, or must one be zero if the other is positive (i.e., you cannot have both unsold inventory and unfulfilled demand in the same month)?

## Turn 21 - User Simulator

A month cannot have both positive ending inventory and positive backorders simultaneously. If there is unfulfilled demand (backorders), ending inventory must be zero. If there is ending inventory, backorders must be zero.

## Turn 22 - Generic Agent

QUESTION: For the beginning inventory in January, you stated it is 15,000 units. Is this inventory available to fulfill January's demand of 20,000 units, meaning January's available supply is 15,000 (beginning inventory) + in-house production + outsourcing, and if this is less than 20,000, the shortfall becomes a backorder?

## Turn 22 - User Simulator

Yes, the 15,000 units of beginning inventory in January are available to fulfill January's demand. January's available supply is 15,000 + in-house production + outsourcing. If this is less than 20,000, the shortfall becomes a backorder.

## Turn 23 - Generic Agent

QUESTION: For the workforce, is there any constraint that the number of workers fired in a month cannot exceed the number of workers on staff at the beginning of that month (i.e., you cannot fire more workers than you have), and is the workforce always a non-negative integer?

## Turn 23 - User Simulator

Yes, the number of workers fired in a month cannot exceed the number of workers on staff at the beginning of that month. The workforce is always a non-negative integer.

## Turn 24 - Generic Agent

QUESTION: For the in-house production capacity, is the constraint that in-house production in a month × 5 labor hours ≤ (workers on staff that month × 160 regular hours) + (overtime hours used that month), where overtime hours used ≤ workers on staff that month × 20?

## Turn 24 - User Simulator

Yes, that is correct.

## Turn 25 - Generic Agent

QUESTION: For the backorder and inventory mutual exclusivity, is this enforced as a hard constraint in the model (i.e., ending inventory × backorders = 0 for each month), or is it a natural consequence of the optimization (i.e., the model would never choose to have both because it would be suboptimal)?

## Turn 25 - User Simulator

It is a natural consequence of the optimization. The model would never choose to have both positive ending inventory and positive backorders because it would be suboptimal.

## Turn 26 - Generic Agent

QUESTION: For the demand fulfillment, when backorders from previous months are carried into a later month, are they fulfilled in the same way as current demand (i.e., using any combination of beginning inventory, in-house production, and outsourcing), and does the revenue of 300 Yuan per unit apply to backorder units when they are eventually delivered?

## Turn 26 - User Simulator

Yes, backorders from previous months are fulfilled in the same way as current demand, using any combination of beginning inventory, in-house production, and outsourcing. The revenue of 300 Yuan per unit applies to backorder units when they are eventually delivered.

## Turn 27 - Generic Agent

QUESTION: For the inventory holding cost, is it charged on the ending inventory of each month (January through June), where ending inventory is the physical units on hand at month-end (which is zero if there are backorders that month)?

## Turn 27 - User Simulator

Yes, the inventory holding cost is charged on the ending inventory of each month (January through June), where ending inventory is the physical units on hand at month-end (which is zero if there are backorders that month).

## Turn 28 - Generic Agent

QUESTION: For the backorder cost, is it charged on the backorder balance at the end of each month (January through May, since June must have zero backorders), where the backorder balance is the cumulative unfulfilled demand at that month-end?

## Turn 28 - User Simulator

Yes, the backorder cost is charged on the backorder balance at the end of each month (January through May, since June must have zero backorders), where the backorder balance is the cumulative unfulfilled demand at that month-end.

## Turn 29 - Generic Agent

QUESTION: For the workforce, is there any constraint on the number of workers that can be hired in a single month (e.g., a maximum hiring rate), or can any non-negative integer number of workers be hired in any month?

## Turn 29 - User Simulator

There is no constraint on the number of workers that can be hired in a single month. Any non-negative integer number of workers can be hired in any month.

## Turn 30 - Generic Agent

QUESTION: For the workforce, is there any constraint on the number of workers that can be fired in a single month (e.g., a maximum firing rate), or can any non-negative integer number of workers be fired in any month (up to the workforce on staff at the beginning of that month)?

## Turn 30 - User Simulator

There is no constraint on the number of workers that can be fired in a single month, other than that it cannot exceed the workforce on staff at the beginning of that month.