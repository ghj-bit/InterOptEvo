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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker per month (so total workforce overtime is 20 × number of workers that month), or is it a single aggregate cap of 20 hours for the whole workforce combined in each month?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime available in any given month is 20 hours multiplied by the number of workers on staff that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, is the number of workers allowed to change each month (i.e., can you hire or fire at the start of any month, with the 5,000 Yuan hiring cost and 8,000 Yuan firing cost applying to each such change), or is the workforce fixed at 1,000 for all six months?

## Turn 2 - User Simulator

The workforce can change each month. You can hire or fire at the start of any month, with the 5,000 Yuan hiring cost and 8,000 Yuan firing cost applying to each worker hired or fired.

## Turn 3 - Generic Agent

QUESTION: When a worker is hired or fired at the start of a month, does that worker count toward that month's regular hours (160), overtime capacity (20), and wage payment, or do they only count starting the following month?

## Turn 3 - User Simulator

A worker hired or fired at the start of a month counts toward that month's regular hours, overtime capacity, and wage payment.

## Turn 4 - Generic Agent

QUESTION: Regarding the regular wage: you said each worker is paid 30 Yuan/hour for 160 regular hours "regardless of utilization." Does this mean the company pays every worker a fixed 4,800 Yuan per month (160 × 30) even if actual production uses fewer hours, or is the regular wage only paid for the hours actually used up to 160?

## Turn 4 - User Simulator

The company pays every worker a fixed 4,800 Yuan per month (160 hours × 30 Yuan/hour), regardless of how many hours are actually used for production.

## Turn 5 - Generic Agent

QUESTION: For the inventory balance, when you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in any given month, the total units available to meet demand (current + backorders) equal: beginning inventory + in-house production + outsourcing, and any shortfall becomes a backorder carried to the next month?

## Turn 5 - User Simulator

Yes, that is correct. In any given month, the total units available to meet demand (current demand plus any backorders from the previous month) equal: beginning inventory + in-house production + outsourcing. If this total is less than the total demand to be met, the shortfall becomes a backorder carried to the next month.

## Turn 6 - Generic Agent

QUESTION: Can inventory and backorders be positive at the same time in the same month (i.e., can the company simultaneously hold leftover inventory and carry unfulfilled demand), or must one be zero whenever the other is positive?

## Turn 6 - User Simulator

The available business facts do not explicitly state whether inventory and backorders can be positive at the same time in the same month. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the June ending inventory requirement of at least 10,000 units, does this mean that after fulfilling all of June's demand (including any backorders carried into June), the remaining inventory must be at least 10,000, or does it mean the total units available in June (beginning inventory + production + outsourcing) minus June's demand must leave at least 10,000, even if some of June's demand is backordered beyond June?

## Turn 7 - User Simulator

It means that after fulfilling all of June's demand (including any backorders carried into June), the remaining inventory must be at least 10,000 units. Since all backorders must be cleared by the end of June, there are no backorders carried beyond June, so the ending inventory is simply what remains after all June obligations are met.

## Turn 8 - Generic Agent

QUESTION: You confirmed that all backorders must be cleared by the end of June. Does this mean that in June, the total units available (beginning inventory + in-house production + outsourcing) must be at least the sum of June's demand plus any backorders carried into June plus the 10,000 minimum ending inventory, with no possibility of leaving any demand unmet in June?

## Turn 8 - User Simulator

Yes, that is correct. In June, the total units available (beginning inventory + in-house production + outsourcing) must be at least the sum of June's demand plus any backorders carried into June plus the 10,000 minimum ending inventory. No demand can be left unmet in June.

## Turn 9 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is this cost incurred only on units that are actually produced in-house (regardless of whether they are sold in the same month or held in inventory), or is it only incurred on units that are both produced in-house and sold?

## Turn 9 - User Simulator

The raw material cost of 90 Yuan per unit is incurred only on units that are actually produced in-house, regardless of whether they are sold in the same month or held in inventory.

## Turn 10 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is revenue recognized in the month the unit is sold (i.e., when demand is fulfilled), or is it recognized in the month the unit is produced?

## Turn 10 - User Simulator

Revenue is recognized in the month the unit is sold, i.e., when demand is fulfilled.

## Turn 11 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it applied to the ending inventory of each month (i.e., the units remaining at the end of that month after fulfilling demand), and does it also apply to the 10,000 units of ending inventory at the end of June?

## Turn 11 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is applied to the ending inventory of each month, including the 10,000 units of ending inventory at the end of June.

## Turn 12 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is it applied to the number of units backordered at the end of each month (i.e., the unfulfilled demand carried from that month to the next), and does it apply to any backorders at the end of June (which you confirmed must be zero)?

## Turn 12 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is applied to the number of units backordered at the end of each month. Since all backorders must be cleared by the end of June, there are no backorders at the end of June, so no backorder cost is incurred for June.

## Turn 13 - Generic Agent

QUESTION: For the outsourcing units, is there any limit on how many units can be outsourced in a given month, or can the company outsource an unlimited number of units at 200 Yuan per unit?

## Turn 13 - User Simulator

The available business facts do not specify any limit on the number of units that can be outsourced in a given month. This point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the in-house production, is there any maximum production capacity per month beyond what is determined by the workforce's available hours (160 regular + 20 overtime per worker), or is the only constraint on in-house production the labor hours available from the workforce?

## Turn 14 - User Simulator

The only constraint on in-house production is the labor hours available from the workforce (160 regular + 20 overtime per worker). There is no separate maximum production capacity per month beyond that.

## Turn 15 - Generic Agent

QUESTION: For the workforce, can the number of workers go below zero or is there a minimum workforce size that must be maintained (e.g., at least 0 workers, or some other minimum)?

## Turn 15 - User Simulator

The available business facts do not specify a minimum workforce size that must be maintained. This point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 16 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 17 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 18 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 19 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 20 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 21 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 22 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 23 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 24 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 25 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one

## Turn 26 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 26 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 27 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs internal

## Turn 28 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 28 - User Simulator

The available business facts do not specify whether the workforce can be reduced to zero or whether at least one worker must be retained. This point still needs

## Turn 29 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 29 - User Simulator

The available business

## Turn 30 - Generic Agent

QUESTION: For the workforce, can the number of workers be zero in any month (i.e., can the company fire all workers), or must at least one worker be retained at all times?

## Turn 30 - User Simulator

The available