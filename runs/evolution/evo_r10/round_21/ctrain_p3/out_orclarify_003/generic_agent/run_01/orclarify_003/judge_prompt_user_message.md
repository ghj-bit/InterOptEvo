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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: When you say "orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," do you mean that backorders from prior months must be fulfilled before the current month's new demand is satisfied, or that all units (backorders plus current demand) are treated as one combined pool that just needs to be covered by the available supply?

## Turn 2 - User Simulator

All units (backorders plus current demand) are treated as one combined pool that just needs to be covered by the available supply.

## Turn 3 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire workers in any month (January through June), or are hiring/firing decisions only allowed at the start of January?

## Turn 3 - User Simulator

Hiring and firing decisions can be made in any month from January through June.

## Turn 4 - Generic Agent

QUESTION: When you say the regular wage is "paid regardless of utilization," does that mean each worker's 160 regular hours are paid at 30 Yuan/hour (4,800 Yuan per worker per month) even if the actual production workload in that month requires fewer hours, so the regular wage is a fixed cost per worker per month?

## Turn 4 - User Simulator

Yes, each worker's 160 regular hours are paid at 30 Yuan/hour (4,800 Yuan per worker per month) even if the actual production workload in that month requires fewer hours. The regular wage is a fixed cost per worker per month.

## Turn 5 - Generic Agent

QUESTION: For the inventory balance, is the ending inventory at the end of each month (including June) calculated as: beginning inventory + in-house production + outsourcing − total units fulfilled (backorders + current demand), and is the 10,000-unit minimum ending inventory requirement applied only to June or to every month?

## Turn 5 - User Simulator

The ending inventory at the end of each month is calculated as: beginning inventory + in-house production + outsourcing − total units fulfilled (backorders + current demand). The 10,000-unit minimum ending inventory requirement is applied only to June.

## Turn 6 - Generic Agent

QUESTION: Can the ending inventory in any month (January through May) go negative, meaning that if supply is insufficient to cover the combined demand pool, the shortfall becomes a backorder carried to the next month, or must inventory never go below zero in any month?

## Turn 6 - User Simulator

The ending inventory in any month (January through May) can go negative. If supply is insufficient to cover the combined demand pool, the shortfall becomes a backorder carried to the next month.

## Turn 7 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit, is this charged on the total backorder quantity carried from one month to the next (i.e., the cumulative unfulfilled demand at the end of each month), or is it charged only on the new units that become backordered in that specific month?

## Turn 7 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the total backorder quantity carried from one month to the next (i.e., the cumulative unfulfilled demand at the end of each month).

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the number of workers you can hire in a given month, or can you hire an unlimited number of new workers in any month?

## Turn 8 - User Simulator

There is no upper limit on the number of workers you can hire in a given month. You can hire an unlimited number of new workers in any month.

## Turn 9 - Generic Agent

QUESTION: Is there a minimum number of workers that must be employed in any month, or can the workforce drop to zero if it is optimal to fire everyone?

## Turn 9 - User Simulator

There is no minimum number of workers that must be employed in any month. The workforce can drop to zero if it is optimal to fire everyone.

## Turn 10 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is this charged only on positive ending inventory (i.e., when you have surplus units left over), or is it also charged on the absolute value of inventory (meaning it would apply even when inventory is negative, i.e., backorders)?

## Turn 10 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged only on positive ending inventory (i.e., when you have surplus units left over).

## Turn 11 - Generic Agent

QUESTION: When you say the sales price is 300 Yuan per unit sold, does this revenue apply to every unit that is ultimately fulfilled (including backordered units that are delivered in a later month), or only to units fulfilled in the same month the demand was originally placed?

## Turn 11 - User Simulator

The sales price of 300 Yuan per unit applies to every unit that is ultimately fulfilled, including backordered units that are delivered in a later month.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced in a given month, or can you outsource an unlimited number of finished tables in any month?

## Turn 12 - User Simulator

There is no limit on the number of units that can be outsourced in a given month. You can outsource an unlimited number of finished tables in any month.

## Turn 13 - Generic Agent

QUESTION: When a backordered unit is eventually fulfilled in a later month, is the raw material cost of 90 Yuan per unit still incurred if that unit was produced in-house in the later month, or is the raw material cost only associated with the month the demand was originally placed?

## Turn 13 - User Simulator

The raw material cost of 90 Yuan per unit is incurred in the month the unit is actually produced in-house, regardless of when the demand was originally placed.

## Turn 14 - Generic Agent

QUESTION: For the workforce balance, is the number of workers employed in a given month determined by: workers at start of month + hires in that month − fires in that month, and does this workforce level apply to both the regular wage cost and the overtime capacity in that same month?

## Turn 14 - User Simulator

Yes, the number of workers employed in a given month is determined by: workers at start of month + hires in that month − fires in that month. This workforce level applies to both the regular wage cost and the overtime capacity in that same month.

## Turn 15 - Generic Agent

QUESTION: Are all decision variables (units produced in-house, units outsourced, units hired, units fired, units fulfilled, backorders, inventory) required to be non-negative integers, or can they take continuous (fractional) values?

## Turn 15 - User Simulator

All decision variables (units produced in-house, units outsourced, units hired, units fired, units fulfilled, backorders, inventory) are required to be non-negative integers.

## Turn 16 - Generic Agent

QUESTION: When you say the ending inventory at the end of June must be at least 10,000 units, does this mean the net inventory (beginning inventory + production + outsourcing − total fulfilled) must be at least 10,000, or does it mean the physical inventory on hand must be at least 10,000 (which would be different if there are still backorders outstanding at the end of June)?

## Turn 16 - User Simulator

The ending inventory at the end of June must be at least 10,000 units of physical inventory on hand. Since all backorders must be cleared by the end of June (ending backorders must be zero), the net inventory and the physical inventory on hand are the same at the end of June.

## Turn 17 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June (ending backorders must be zero). Is this a hard requirement that must be satisfied, or is it simply a consequence of the 10,000-unit minimum ending inventory constraint?

## Turn 17 - User Simulator

This is a hard requirement that must be satisfied. All backorders must be cleared by the end of June; no outstanding customer orders can remain after June.

## Turn 18 - Generic Agent

QUESTION: Regarding the overtime hours, can the total in-house production in a month exceed the regular capacity (160 hours × number of workers) by using overtime, up to the maximum of 20 additional hours per worker, meaning the maximum in-house production in a month is (160 + 20) × number of workers ÷ 5 units?

## Turn 18 - User Simulator

Yes, the total in-house production in a month can exceed the regular capacity (160 hours × number of workers) by using overtime, up to the maximum of 20 additional hours per worker. The maximum in-house production in a month is (160 + 20) × number of workers ÷ 5 units.

## Turn 19 - Generic Agent

QUESTION: Is the overtime used in a month determined endogenously (i.e., the model decides how much overtime to use up to the 20-hour-per-worker cap based on production needs), or is overtime a fixed amount that must be fully utilized if any production exceeds regular capacity?

## Turn 19 - User Simulator

The overtime used in a month is determined endogenously. The model decides how much overtime to use, up to the 20-hour-per-worker cap, based on production needs.

## Turn 20 - Generic Agent

QUESTION: When you say the workforce can drop to zero, does that mean you can fire all workers in a month and then hire new workers in the same month, or does the workforce balance work such that you first hire and then fire (or vice versa), and the net effect is what matters for the month's workforce level?

## Turn 20 - User Simulator

The workforce balance works such that the net effect is what matters for the month's workforce level. You can fire all workers in a month and then hire new workers in the same month, or vice versa. The workforce level for that month is determined by: workers at start of month + hires in that month − fires in that month.

## Turn 21 - Generic Agent

QUESTION: Regarding the backorder cost, is it charged on the cumulative backorder at the end of each month (January through May), and is it also charged on the backorder at the end of June (which must be zero)? In other words, is the backorder cost applied for all six months or only for the first five months?

## Turn 21 - User Simulator

The backorder cost is charged on the cumulative backorder at the end of each month (January through May). Since the backorder at the end of June must be zero, no backorder cost is incurred for June.

## Turn 22 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is it charged on the positive ending inventory at the end of each month from January through June, including June?

## Turn 22 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the positive ending inventory at the end of each month from January through June, including June.

## Turn 23 - Generic Agent

QUESTION: When a unit is outsourced, does it require any labor hours from the workforce, or is outsourcing completely independent of the workforce (i.e., no labor hours are consumed for outsourced units)?

## Turn 23 - User Simulator

Outsourcing is completely independent of the workforce. No labor hours are consumed for outsourced units.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that limits the total number of units that can be fulfilled in a given month (e.g., a maximum delivery capacity), or can you fulfill an unlimited number of units in any month as long as supply (beginning inventory + in-house production + outsourcing) is sufficient?

## Turn 24 - User Simulator

There is no constraint that limits the total number of units that can be fulfilled in a given month. You can fulfill an unlimited number of units in any month as long as supply (beginning inventory + in-house production + outsourcing) is sufficient.

## Turn 25 - Generic Agent

QUESTION: Regarding the sales revenue of 300 Yuan per unit, is it recognized in the month the unit is actually fulfilled/delivered to the customer, or is it recognized in the month the demand was originally placed (even if the unit is delivered later as a backorder)?

## Turn 25 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the month the unit is actually fulfilled/delivered to the customer.

## Turn 26 - Generic Agent

QUESTION: Since the objective is to maximize total net profit over the six-month period, and revenue is recognized when units are delivered, does the timing of revenue recognition within the six months matter for the objective (i.e., is there any discounting or time-value-of-money effect), or is the objective simply the sum of all revenues minus all costs over the entire six-month period with no time discounting?

## Turn 26 - User Simulator

The objective is simply the sum of all revenues minus all costs over the entire six-month period with no time discounting. The timing of revenue recognition within the six months does not matter for the objective.

## Turn 27 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire fractional workers (e.g., hire 0.5 workers), or must the number of workers hired and fired in each month be a whole number?

## Turn 27 - User Simulator

The number of workers hired and fired in each month must be a whole number.

## Turn 28 - Generic Agent

QUESTION: Regarding the in-house production, must the number of units produced in-house in each month be a whole number, or can it be fractional (e.g., produce 3.5 units)?

## Turn 28 - User Simulator

The number of units produced in-house in each month must be a whole number.

## Turn 29 - Generic Agent

QUESTION: Regarding the outsourcing, must the number of units outsourced in each month be a whole number, or can it be fractional?

## Turn 29 - User Simulator

The number of units outsourced in each month must be a whole number.

## Turn 30 - Generic Agent

QUESTION: Regarding the units fulfilled in each month, must the number of units fulfilled (delivered to customers) be a whole number, or can it be fractional?

## Turn 30 - User Simulator

The number of units fulfilled in each month must be a whole number.