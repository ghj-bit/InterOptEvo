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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours for each individual worker (so total workforce overtime is 20 times the number of workers that month), or is there a single aggregate cap of 20 hours for the whole workforce combined?

## Turn 1 - User Simulator

It is 20 hours for each individual worker. So the total overtime hours allowed in a given month is 20 times the number of workers on staff that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can you hire and fire workers in any month (including January), and is the workforce level for a month determined before or after that month's hiring/firing decisions — that is, if you hire in January, are those new workers available to produce in January itself?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. If you hire in January, those new workers are available to produce in January itself. The workforce level for a month is determined after that month's hiring and firing decisions.

## Turn 3 - Generic Agent

QUESTION: When you say the regular wage of 30 Yuan per hour for the 160 regular hours is "paid regardless of utilization," does that mean each worker's 160 regular hours are paid in full even if the worker is not fully utilized (i.e., total regular labor hours available = 160 × number of workers, and you pay for all of it whether or not it is used)?

## Turn 3 - User Simulator

Yes, that is correct. Each worker's 160 regular hours are paid in full regardless of utilization. You pay for all 160 hours per worker per month, whether or not those hours are actually used for production.

## Turn 4 - Generic Agent

QUESTION: For the sales price of 300 Yuan per unit sold — is revenue recognized on units actually shipped/fulfilled to customers in a given month (i.e., demand that is met that month), or on units that were originally demanded in that month regardless of when they are finally delivered?

## Turn 4 - User Simulator

Revenue is recognized on units actually shipped/fulfilled to customers in a given month. So if demand is back-ordered and fulfilled in a later month, the revenue is recognized in that later month when the unit is delivered.

## Turn 5 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit — is it incurred only on units produced in-house (as stated), and is it incurred at the time of production (when the unit is made) rather than at the time of sale?

## Turn 5 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred only on units produced in-house, and it is incurred at the time of production, not at the time of sale.

## Turn 6 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit — is it charged on the ending inventory of each month (i.e., units left over at the end of that month), and does it apply to all months including June (so the 10,000-unit minimum ending inventory in June also incurs holding cost)?

## Turn 6 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, and it applies to all months including June. So the 10,000-unit minimum ending inventory in June also incurs holding cost.

## Turn 7 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit — is it charged on the number of units that are back-ordered at the end of each month (i.e., unfulfilled demand carried into the next month), and does it apply to all months including June (or is June exempt because the plan ends there)?

## Turn 7 - User Simulator

The backorder cost of 35 Yuan per unit is charged on the number of units back-ordered at the end of each month. However, because all backorders must be cleared by the end of June, there are no backorders at the end of June, so no backorder cost is incurred in June.

## Turn 8 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June — is this a hard requirement (i.e., ending backorders in June must equal zero, so all cumulative demand through June must be fully satisfied by June), or is it just a consequence of the 10,000-unit minimum ending inventory requirement?

## Turn 8 - User Simulator

It is a hard requirement. Ending backorders in June must equal zero, meaning all cumulative demand through June must be fully satisfied by the end of June. This is separate from the 10,000-unit minimum ending inventory requirement.

## Turn 9 - Generic Agent

QUESTION: For the inventory balance, when you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units" — is the inventory balance equation simply: ending inventory = beginning inventory + in-house production + outsourcing − units shipped to meet demand (including backorders), with no other sources or sinks?

## Turn 9 - User Simulator

Yes, that is correct. The inventory balance equation is: ending inventory = beginning inventory + in-house production + outsourcing − units shipped to meet demand (including backorders). There are no other sources or sinks.

## Turn 10 - Generic Agent

QUESTION: For the labor constraint, is the total labor hours used for in-house production in a month limited to (160 × number of workers) + (20 × number of workers) = 180 × number of workers, meaning in-house production is capped at 36 units per worker per month (180 hours ÷ 5 hours per unit)?

## Turn 10 - User Simulator

Yes, that is correct. The total labor hours available for in-house production in a month is (160 × number of workers) + (20 × number of workers) = 180 × number of workers. Since each in-house unit requires 5 labor hours, in-house production is capped at 36 units per worker per month.

## Turn 11 - Generic Agent

QUESTION: For the workforce balance, is the number of workers at the end of each month simply: ending workers = beginning workers + hires − fires, with no other constraints on the workforce (such as a minimum or maximum number of workers)?

## Turn 11 - User Simulator

Yes, that is correct. The workforce balance is: ending workers = beginning workers + hires − fires. There are no minimum or maximum constraints on the number of workers.

## Turn 12 - Generic Agent

QUESTION: For the backorder balance, is the number of backorders at the end of each month simply: ending backorders = beginning backorders + current month's demand − units shipped to meet demand that month, where units shipped can come from beginning inventory, in-house production, and outsourcing?

## Turn 12 - User Simulator

Yes, that is correct. The backorder balance is: ending backorders = beginning backorders + current month's demand − units shipped to meet demand that month, where units shipped can come from beginning inventory, in-house production, and outsourcing.

## Turn 13 - Generic Agent

QUESTION: For the inventory and backorder relationship, can a month have both positive ending inventory and positive ending backorders simultaneously, or must one of them be zero in each month (i.e., you cannot have both leftover inventory and unmet demand at the same time)?

## Turn 13 - User Simulator

A month cannot have both positive ending inventory and positive ending backorders simultaneously. One of them must be zero in each month. If there is leftover inventory, backorders must be zero; if there are backorders, inventory must be zero.

## Turn 14 - Generic Agent

QUESTION: For the outsourcing units — is there any limit on how many units can be outsourced in a given month, or is outsourcing unlimited (you can outsource as many units as needed at 200 Yuan per unit)?

## Turn 14 - User Simulator

Outsourcing is unlimited. You can outsource as many units as needed at 200 Yuan per unit, with no monthly cap.

## Turn 15 - Generic Agent

QUESTION: For the objective function, is total net profit calculated as: total revenue (300 × units shipped) minus total costs (raw materials + outsourcing + inventory holding + backorder + regular wages + overtime wages + hiring + firing), with no other revenue or cost components?

## Turn 15 - User Simulator

Yes, that is correct. Total net profit is calculated as: total revenue (300 × units shipped) minus total costs (raw materials + outsourcing + inventory holding + backorder + regular wages + overtime wages + hiring + firing). There are no other revenue or cost components.

## Turn 16 - Generic Agent

QUESTION: For the overtime wage cost — is it calculated as 40 Yuan per hour × actual overtime hours used (which can be up to 20 per worker), meaning you only pay overtime wages for the overtime hours actually consumed for production, not for all 20 hours per worker?

## Turn 16 - User Simulator

Yes, that is correct. Overtime wage cost is calculated as 40 Yuan per hour × actual overtime hours used. You only pay overtime wages for the overtime hours actually consumed for production, not for all 20 hours per worker.

## Turn 17 - Generic Agent

QUESTION: For the regular wage cost — is it calculated as 30 Yuan per hour × 160 hours × number of workers (i.e., 4,800 Yuan per worker per month), paid in full regardless of how many of those 160 hours are actually used for production?

## Turn 17 - User Simulator

Yes, that is correct. Regular wage cost is calculated as 30 Yuan per hour × 160 hours × number of workers, which equals 4,800 Yuan per worker per month, paid in full regardless of how many of those 160 hours are actually used for production.

## Turn 18 - Generic Agent

QUESTION: For the units shipped to meet demand in a given month — can you choose to ship fewer units than the total available (beginning inventory + in-house production + outsourcing) and leave the rest as ending inventory, or must you ship as much as possible to minimize backorders?

## Turn 18 - User Simulator

You can choose to ship fewer units than the total available and leave the rest as ending inventory. You are not required to ship as much as possible; the decision on how many units to ship each month is part of the optimization.

## Turn 19 - Generic Agent

QUESTION: For the backorder and inventory mutual exclusion constraint — does this apply to the beginning of each month as well (i.e., beginning inventory and beginning backorders cannot both be positive), or only to the ending inventory and ending backorders of each month?

## Turn 19 - User Simulator

It applies to the ending inventory and ending backorders of each month. Since the ending values of one month become the beginning values of the next month, this effectively means beginning inventory and beginning backorders also cannot both be positive.

## Turn 20 - Generic Agent

QUESTION: For the initial conditions — at the start of January, you have 15,000 units of inventory and 1,000 workers, and zero backorders. Is that correct, or could there be any initial backorders at the start of January?

## Turn 20 - User Simulator

That is correct. At the start of January, you have 15,000 units of inventory, 1,000 workers, and zero backorders.

## Turn 21 - Generic Agent

QUESTION: For the in-house production labor constraint — is the total in-house production in a month limited to the total available labor hours (180 × workers) divided by 5 hours per unit, or is there a separate constraint that in-house production cannot exceed the regular hours capacity (160 × workers ÷ 5) plus a separate overtime production variable?

## Turn 21 - User Simulator

The total in-house production in a month is limited to the total available labor hours (180 × workers) divided by 5 hours per unit. There is no separate constraint splitting regular and overtime production; the single cap is 36 units per worker per month.

## Turn 22 - Generic Agent

QUESTION: For the overtime hours used — is the actual overtime hours used in a month simply the total labor hours consumed for in-house production minus the regular hours available (160 × workers), floored at zero, or is it a separate decision variable that you choose independently?

## Turn 22 - User Simulator

The actual overtime hours used in a month is simply the total labor hours consumed for in-house production minus the regular hours available (160 × workers), floored at zero. It is not a separate decision variable chosen independently; it is determined by how much in-house production is performed.

## Turn 23 - Generic Agent

QUESTION: For the units shipped in a given month — can you ship units to satisfy both the current month's demand and any existing backorders, or must you satisfy backorders first before addressing the current month's new demand?

## Turn 23 - User Simulator

You can ship units to satisfy both the current month's demand and any existing backorders. There is no requirement to satisfy backorders first before addressing the current month's new demand; the allocation of shipped units between backorders and current demand is part of the optimization decision.

## Turn 24 - Generic Agent

QUESTION: For the backorder balance equation — since you can allocate shipped units between backorders and current demand freely, is the backorder balance simply: ending backorders = beginning backorders + current demand − total units shipped that month, where total units shipped is a single aggregate number (not split between backorders and current demand)?

## Turn 24 - User Simulator

Yes, that is correct. The backorder balance is simply: ending backorders = beginning backorders + current demand − total units shipped that month, where total units shipped is a single aggregate number.

## Turn 25 - Generic Agent

QUESTION: For the inventory balance equation — is it simply: ending inventory = beginning inventory + in-house production + outsourcing − total units shipped that month, where total units shipped is the same aggregate number used in the backorder balance?

## Turn 25 - User Simulator

Yes, that is correct. The inventory balance is simply: ending inventory = beginning inventory + in-house production + outsourcing − total units shipped that month, where total units shipped is the same aggregate number used in the backorder balance.

## Turn 26 - Generic Agent

QUESTION: For the mutual exclusion constraint between ending inventory and ending backorders — since both are determined by the same "total units shipped" variable, does this constraint simply mean that in each month, either ending inventory ≥ 0 and ending backorders = 0, or ending inventory = 0 and ending backorders ≥ 0 (i.e., you cannot have both positive)?

## Turn 26 - User Simulator

Yes, that is correct. In each month, either ending inventory ≥ 0 and ending backorders = 0, or ending inventory = 0 and ending backorders ≥ 0. You cannot have both positive simultaneously.

## Turn 27 - Generic Agent

QUESTION: For the June ending conditions — you need ending inventory ≥ 10,000 units AND ending backorders = 0. Does this mean that in June, the ending inventory must be at least 10,000 and there can be no backorders, so effectively the ending inventory is simply ≥ 10,000 (since backorders must be zero)?

## Turn 27 - User Simulator

Yes, that is correct. In June, the ending inventory must be at least 10,000 units and ending backorders must be zero. Since backorders must be zero, the ending inventory is simply ≥ 10,000.

## Turn 28 - Generic Agent

QUESTION: For the hiring and firing decisions — can you hire and fire in the same month (i.e., both hires and fires can be positive in the same month), or must you choose one or the other each month?

## Turn 28 - User Simulator

You can hire and fire in the same month. Both hires and fires can be positive in the same month.

## Turn 29 - Generic Agent

QUESTION: For the workforce and production timing — if you fire workers in a given month, are those fired workers still available to produce in that same month (i.e., production uses the beginning-of-month workforce), or are they only available up to the point of firing (i.e., production uses the end-of-month workforce after hiring/firing)?

## Turn 29 - User Simulator

Production uses the end-of-month workforce after hiring and firing decisions. So if you fire workers in a given month, those fired workers are not available to produce in that same month.

## Turn 30 - Generic Agent

QUESTION: For the regular wage cost — is it based on the end-of-month workforce (after hiring and firing), meaning you pay 4,800 Yuan per worker for each worker on staff at the end of that month?

## Turn 30 - User Simulator

Yes, that is correct. The regular wage cost is based on the end-of-month workforce after hiring and firing. You pay 4,800 Yuan per worker for each worker on staff at the end of that month.