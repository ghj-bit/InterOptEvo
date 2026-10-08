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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a month (so total overtime is bounded by 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is bounded by 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce, can the number of workers change from month to month through hiring and firing, and if so, is the workforce level for a month determined at the start of that month (so workers hired in January are available for January production), or at the end of the month?

## Turn 2 - User Simulator

Yes, the number of workers can change from month to month through hiring and firing. The workforce level for a month is determined at the start of that month, so workers hired in January are available for January production.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered, is the backorder cost of 35 Yuan per unit charged only once (for the month the demand first goes unmet), or is it charged every month the backorder remains outstanding until it is finally fulfilled?

## Turn 3 - User Simulator

The backorder cost of 35 Yuan per unit is charged every month the backorder remains outstanding until it is finally fulfilled.

## Turn 4 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (including June's ending inventory of at least 10,000 units), or only on the ending inventory of months January through May?

## Turn 4 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including June's ending inventory.

## Turn 5 - Generic Agent

QUESTION: When orders are fulfilled using available inventory, current in-house production, and outsourced units, is there any limit on how many units can be outsourced in a month, or can any number of units be outsourced as needed?

## Turn 5 - User Simulator

There is no limit on how many units can be outsourced in a month. Any number of units can be outsourced as needed.

## Turn 6 - Generic Agent

QUESTION: Is the sales price of 300 Yuan per unit earned for every unit of demand that is eventually fulfilled (including back-ordered demand fulfilled in a later month), or only for units fulfilled in the month the demand originally occurred?

## Turn 6 - User Simulator

The sales price of 300 Yuan per unit is earned for every unit of demand that is eventually fulfilled, including back-ordered demand fulfilled in a later month.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum number of workers the company can employ in any month, or is the workforce size only bounded by the hiring/firing costs and the initial 1,000 workers?

## Turn 7 - User Simulator

There is no maximum number of workers the company can employ in any month. The workforce size is only bounded by the hiring/firing costs and the initial 1,000 workers.

## Turn 8 - Generic Agent

QUESTION: For the regular wage of 30 Yuan per hour for 160 hours per worker, is this cost incurred for every worker employed in a month regardless of how many hours they actually work (i.e., 4,800 Yuan per worker per month as a fixed cost), or is it only paid for the hours actually used in production?

## Turn 8 - User Simulator

The regular wage is a fixed cost of 4,800 Yuan per worker per month (30 Yuan/hour × 160 hours), incurred for every worker employed in that month regardless of how many hours they actually work in production.

## Turn 9 - Generic Agent

QUESTION: Can the workforce be reduced below zero workers, or is the minimum workforce in any month zero (i.e., the company could fire all workers if it chose to)?

## Turn 9 - User Simulator

The minimum workforce in any month is zero. The company could fire all workers if it chose to.

## Turn 10 - Generic Agent

QUESTION: Is there a minimum number of workers that must be employed in any month, or can the workforce be zero in a month where the company relies entirely on outsourcing and inventory?

## Turn 10 - User Simulator

There is no minimum number of workers that must be employed in any month. The workforce can be zero in a month where the company relies entirely on outsourcing and inventory.

## Turn 11 - Generic Agent

QUESTION: When back-ordered demand is fulfilled in a later month, does the raw material cost of 90 Yuan per unit apply to in-house production of those units in the later month, or is the raw material cost only associated with the month the demand originally occurred?

## Turn 11 - User Simulator

The raw material cost of 90 Yuan per unit applies to in-house production of those units in the later month when they are actually produced.

## Turn 12 - Generic Agent

QUESTION: Is there a maximum capacity for in-house production in a month beyond what is determined by the available labor hours (regular + overtime), or is in-house production capacity solely limited by the total available labor hours divided by 5 hours per unit?

## Turn 12 - User Simulator

In-house production capacity is solely limited by the total available labor hours (regular + overtime) divided by 5 hours per unit. There is no additional maximum capacity beyond that.

## Turn 13 - Generic Agent

QUESTION: Can the workforce be fractional (e.g., 1,250.5 workers), or must the number of workers in each month be a whole number?

## Turn 13 - User Simulator

The number of workers in each month must be a whole number.

## Turn 14 - Generic Agent

QUESTION: Can the number of units produced in-house, outsourced, and the ending inventory in each month be fractional, or must they all be whole numbers?

## Turn 14 - User Simulator

The number of units produced in-house, outsourced, and the ending inventory in each month must all be whole numbers.

## Turn 15 - Generic Agent

QUESTION: When demand is back-ordered and fulfilled in a later month, is the backorder cost of 35 Yuan per unit charged for each month the backorder is outstanding, including the month it is finally fulfilled, or only for the months before it is fulfilled?

## Turn 15 - User Simulator

The backorder cost of 35 Yuan per unit is charged for each month the backorder is outstanding, including the month it is finally fulfilled.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house plus outsourced in a month, or is the only production constraint the labor-hour limit for in-house production?

## Turn 16 - User Simulator

There is no constraint on the total number of units that can be produced in-house plus outsourced in a month. The only production constraint is the labor-hour limit for in-house production.

## Turn 17 - Generic Agent

QUESTION: When the company fulfills demand using inventory, in-house production, and outsourced units, is there a priority order (e.g., use inventory first, then in-house, then outsource), or can the company choose any combination of these three sources to meet demand?

## Turn 17 - User Simulator

There is no priority order. The company can choose any combination of inventory, in-house production, and outsourced units to meet demand.

## Turn 18 - Generic Agent

QUESTION: Is the sales revenue of 300 Yuan per unit recognized in the month the demand is fulfilled, or is it recognized in the month the demand originally occurred?

## Turn 18 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the month the demand is fulfilled.

## Turn 19 - Generic Agent

QUESTION: When a backorder is fulfilled in a later month, is the sales revenue of 300 Yuan per unit recognized in that later month when the unit is actually delivered, or is it recognized in the original month when the demand occurred?

## Turn 19 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the later month when the unit is actually delivered.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be held in inventory at the end of any month, or is the only inventory constraint the minimum of 10,000 units at the end of June?

## Turn 20 - User Simulator

There is no maximum constraint on the total number of units that can be held in inventory at the end of any month. The only inventory constraint is the minimum of 10,000 units at the end of June.

## Turn 21 - Generic Agent

QUESTION: When the company has both inventory and backorders at the start of a month, must it use inventory to fulfill backorders before using inventory for current demand, or can it allocate inventory to current demand while leaving backorders outstanding?

## Turn 21 - User Simulator

The company can allocate inventory to current demand while leaving backorders outstanding. There is no requirement to use inventory to fulfill backorders before using it for current demand.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be back-ordered at the end of any month, or can any amount of demand be back-ordered as long as it is eventually fulfilled by the end of June?

## Turn 22 - User Simulator

There is no constraint on the total number of units that can be back-ordered at the end of any month. Any amount of demand can be back-ordered as long as it is eventually fulfilled by the end of June.

## Turn 23 - Generic Agent

QUESTION: Must all demand from January through June be fulfilled by the end of June, or can some demand remain unfulfilled (back-ordered) after June?

## Turn 23 - User Simulator

All demand from January through June must be fulfilled by the end of June. No demand can remain unfulfilled (back-ordered) after June.

## Turn 24 - Generic Agent

QUESTION: When the company produces units in-house, is the raw material cost of 90 Yuan per unit incurred for all units produced, or only for units that are actually sold (fulfilling demand)?

## Turn 24 - User Simulator

The raw material cost of 90 Yuan per unit is incurred for all units produced in-house, regardless of whether they are sold immediately or held in inventory.

## Turn 25 - Generic Agent

QUESTION: When the company outsources units, is the outsourcing cost of 200 Yuan per unit incurred for all units outsourced, or only for units that are actually sold (fulfilling demand)?

## Turn 25 - User Simulator

The outsourcing cost of 200 Yuan per unit is incurred for all units outsourced, regardless of whether they are sold immediately or held in inventory.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor-hour limit, such as a machine capacity or a maximum production rate?

## Turn 26 - User Simulator

There is no constraint on the total number of units that can be produced in-house in a month beyond the labor-hour limit.

## Turn 27 - Generic Agent

QUESTION: When the company has inventory at the start of a month and also produces units in-house and outsources units in that same month, is there any constraint on the total units available to fulfill demand (inventory + in-house production + outsourced units), or is the only constraint that demand must be met?

## Turn 27 - User Simulator

There is no constraint on the total units available to fulfill demand (inventory + in-house production + outsourced units). The only constraint is that demand must be met, with any unfulfilled portion carried forward as backorders.

## Turn 28 - Generic Agent

QUESTION: When the company has backorders at the start of a month, must those backorders be fulfilled before any current demand in that month can be fulfilled, or can the company fulfill current demand while leaving backorders outstanding?

## Turn 28 - User Simulator

The company can fulfill current demand while leaving backorders outstanding. There is no requirement to fulfill backorders before current demand.

## Turn 29 - Generic Agent

QUESTION: When the company has both inventory and backorders at the start of a month, can it choose to use inventory to fulfill current demand while leaving backorders outstanding, or must it use inventory to reduce backorders first?

## Turn 29 - User Simulator

The company can choose to use inventory to fulfill current demand while leaving backorders outstanding. There is no requirement to use inventory to reduce backorders first.

## Turn 30 - Generic Agent

QUESTION: When the company has backorders at the start of a month and also has inventory, can it choose to use the inventory to fulfill current demand while leaving the backorders outstanding, or must it use the inventory to reduce the backorders first?

## Turn 30 - User Simulator

The company can choose to use the inventory to fulfill current demand while leaving the backorders outstanding. There is no requirement to use the inventory to reduce the backorders first.