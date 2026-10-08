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

QUESTION: Can the workforce size change from month to month (i.e., can you hire or fire workers in any month, not just January), and if so, is there any limit on how many workers can be hired or fired in a single month?

## Turn 2 - User Simulator

Yes, the workforce size can change from month to month. We can hire or fire workers in any month. There is no limit on how many workers can be hired or fired in a single month.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the total units available to meet that month's demand (current demand plus any backorders from prior months) must come from the sum of: (1) ending inventory from the previous month, (2) in-house production in the current month, and (3) outsourced units in the current month — and any shortfall becomes a new backorder carried to the next month?

## Turn 3 - User Simulator

Yes, that is correct. In each month, the total units available to meet that month's demand (current demand plus any backorders from prior months) come from the sum of: (1) ending inventory from the previous month, (2) in-house production in the current month, and (3) outsourced units in the current month. Any shortfall becomes a new backorder carried to the next month.

## Turn 4 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a given month, or is outsourcing unlimited?

## Turn 4 - User Simulator

There is no upper limit on the number of units that can be outsourced in a given month. Outsourcing is unlimited.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be produced in-house in a given month, other than the labor-hour constraint (i.e., total available regular and overtime hours divided by 5 hours per unit)?

## Turn 5 - User Simulator

No, there is no other upper limit on in-house production. The only constraint on in-house production is the labor-hour constraint: total available regular and overtime hours divided by 5 hours per unit.

## Turn 6 - Generic Agent

QUESTION: Regarding the regular wage: you stated it is 30 Yuan per hour for 160 regular hours per worker, paid regardless of utilization. Does this mean each worker costs 1,000 Yuan per month in regular wages (160 × 30) even if they are not fully utilized, and this cost is incurred for every worker employed in that month?

## Turn 6 - User Simulator

Yes, that is correct. Each worker costs 1,000 Yuan per month in regular wages (160 hours × 30 Yuan per hour), and this cost is incurred for every worker employed in that month, regardless of whether they are fully utilized.

## Turn 7 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and contribute their 160 regular hours and up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 7 - User Simulator

I need to confirm this internally. The original request does not specify whether newly hired workers are available in the same month they are hired or only starting the following month.

## Turn 8 - Generic Agent

QUESTION: For the purpose of modeling, should I assume that newly hired workers are available to work in the same month they are hired (i.e., they contribute their 160 regular hours and up to 20 overtime hours in the hiring month)?

## Turn 8 - User Simulator

Yes, for the purpose of modeling, assume that newly hired workers are available to work in the same month they are hired. They contribute their 160 regular hours and up to 20 overtime hours in the hiring month.

## Turn 9 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (contributing regular and overtime hours) in that same month, or are they removed and only available up to the end of the previous month?

## Turn 9 - User Simulator

I need to confirm this internally. The original request does not specify whether fired workers are still available to work in the month they are fired or are removed immediately.

## Turn 10 - Generic Agent

QUESTION: For the purpose of modeling, should I assume that fired workers are no longer available to work in the month they are fired (i.e., they only contribute hours up to the end of the previous month, and the firing cost is incurred in the month they leave)?

## Turn 10 - User Simulator

Yes, for the purpose of modeling, assume that fired workers are no longer available to work in the month they are fired. They only contribute hours up to the end of the previous month, and the firing cost is incurred in the month they leave.

## Turn 11 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit: is this cost incurred for each unit of unfulfilled demand that is carried over from one month to the next (i.e., it is a per-unit-per-month holding cost on the backorder balance at the end of each month), or is it a one-time cost charged only once per unit when it is first backordered?

## Turn 11 - User Simulator

It is a per-unit-per-month cost. The 35 Yuan is incurred for each unit of unfulfilled demand that is carried over from one month to the next, based on the backorder balance at the end of each month.

## Turn 12 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit: is this cost incurred on the ending inventory balance at the end of each month (i.e., 15 Yuan times the number of units in inventory at the end of that month), and does it apply to all six months including June?

## Turn 12 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is incurred on the ending inventory balance at the end of each month, and it applies to all six months, including June.

## Turn 13 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit: is revenue recognized in the month the unit is actually sold (i.e., when the demand is fulfilled, which could be a later month if backordered), or is it recognized in the month the demand originally occurred?

## Turn 13 - User Simulator

Revenue is recognized in the month the unit is actually sold, i.e., when the demand is fulfilled. If demand is backordered and fulfilled in a later month, the revenue is recognized in that later month.

## Turn 14 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit: is this cost incurred in the month the in-house production takes place, regardless of when the unit is eventually sold?

## Turn 14 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred in the month the in-house production takes place, regardless of when the unit is eventually sold.

## Turn 15 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit: is this cost incurred in the month the outsourced units are used to fulfill demand, or in the month they are ordered/produced externally (which could be a different month)?

## Turn 15 - User Simulator

The outsourcing cost of 200 Yuan per unit is incurred in the month the outsourced units are used to fulfill demand.

## Turn 16 - Generic Agent

QUESTION: Can the workforce size ever go below zero or below some minimum level, or is the only constraint that it starts at 1,000 and can be adjusted by hiring and firing in any month?

## Turn 16 - User Simulator

The only constraint is that the workforce starts at 1,000 employees and can be adjusted by hiring and firing in any month. There is no minimum workforce level specified other than it cannot go below zero.

## Turn 17 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June: does this mean the inventory balance (units in stock, not counting backorders) must be at least 10,000, and can backorders exist at the end of June as long as the inventory is at least 10,000?

## Turn 17 - User Simulator

The ending inventory requirement of at least 10,000 units at the end of June refers to the inventory balance (units in stock, not counting backorders). However, backorders cannot exist at the end of June. All backorders must be cleared by the end of June, meaning no outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 18 - Generic Agent

QUESTION: Regarding the backorder and inventory variables: can both inventory and backorders be positive in the same month (i.e., can you simultaneously have units in stock and unfulfilled demand), or must one of them be zero in each month?

## Turn 18 - User Simulator

I need to confirm this internally. The original request does not specify whether inventory and backorders can both be positive in the same month or if one must be zero.

## Turn 19 - Generic Agent

QUESTION: For the purpose of modeling, should I assume that inventory and backorders cannot both be positive in the same month (i.e., they are mutually exclusive, so if there is unfulfilled demand, inventory must be zero, and vice versa)?

## Turn 19 - User Simulator

Yes, for the purpose of modeling, assume that inventory and backorders cannot both be positive in the same month. They are mutually exclusive: if there is unfulfilled demand (backorders), inventory must be zero, and vice versa.

## Turn 20 - Generic Agent

QUESTION: Regarding the workforce: is the number of workers required to be a whole number (integer), or can it be treated as a continuous variable in the model?

## Turn 20 - User Simulator

The number of workers must be a whole number (integer).

## Turn 21 - Generic Agent

QUESTION: Regarding in-house production: must the number of units produced in-house in each month be a whole number (integer), or can it be treated as a continuous variable?

## Turn 21 - User Simulator

The number of units produced in-house in each month must be a whole number (integer).

## Turn 22 - Generic Agent

QUESTION: Regarding outsourced units: must the number of units outsourced in each month be a whole number (integer), or can it be treated as a continuous variable?

## Turn 22 - User Simulator

The number of units outsourced in each month must be a whole number (integer).

## Turn 23 - Generic Agent

QUESTION: Regarding the overtime hours: must the total overtime hours used in a month be a whole number, or can they be a continuous (fractional) value as long as they do not exceed 20 times the number of workers?

## Turn 23 - User Simulator

The total overtime hours used in a month can be a continuous (fractional) value, as long as they do not exceed 20 times the number of workers.

## Turn 24 - Generic Agent

QUESTION: Regarding the inventory and backorder quantities: must the ending inventory and backorder balance in each month be whole numbers (integers), or can they be continuous variables?

## Turn 24 - User Simulator

The ending inventory and backorder balance in each month must be whole numbers (integers).

## Turn 25 - Generic Agent

QUESTION: Regarding the labor-hour constraint: the total hours available in a month are (number of workers × 160) regular hours plus (number of workers × 20) overtime hours. The in-house production in that month requires 5 hours per unit. Is the constraint simply that 5 × (in-house production) ≤ (number of workers × 160) + (overtime hours used), where overtime hours used ≤ 20 × (number of workers)?

## Turn 25 - User Simulator

Yes, that is correct. The constraint is that 5 × (in-house production) ≤ (number of workers × 160) + (overtime hours used), where overtime hours used ≤ 20 × (number of workers).

## Turn 26 - Generic Agent

QUESTION: Regarding the net profit objective: is it simply total revenue (300 × total units sold over six months) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost components?

## Turn 26 - User Simulator

Yes, that is correct. The net profit objective is total revenue (300 × total units sold over six months) minus all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing. There are no other revenue or cost components.

## Turn 27 - Generic Agent

QUESTION: Regarding the total units sold over six months: since all backorders must be cleared by the end of June, does this mean the total units sold over six months equals the total demand over six months (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500 = 174,500 units), making total revenue a fixed constant of 300 × 174,500 = 52,350,000 Yuan?

## Turn 27 - User Simulator

Yes, that is correct. Since all backorders must be cleared by the end of June, the total units sold over six months equals the total demand over six months (174,500 units). Therefore, total revenue is a fixed constant of 300 × 174,500 = 52,350,000 Yuan.

## Turn 28 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January: is there any cost associated with this initial inventory (e.g., a purchase cost already sunk), or is it simply available to use with no additional cost beyond the holding cost if it remains at the end of January?

## Turn 28 - User Simulator

The initial inventory of 15,000 units is simply available to use with no additional cost beyond the holding cost if it remains at the end of January. There is no additional purchase cost associated with it in the model.

## Turn 29 - Generic Agent

QUESTION: Regarding the initial workforce of 1,000 employees at the start of January: is there any cost associated with this initial workforce beyond the regular wages (1,000 × 1,000 Yuan per month) they incur in January, or is there a one-time setup cost?

## Turn 29 - User Simulator

There is no one-time setup cost associated with the initial workforce of 1,000 employees. The only cost is the regular wages they incur in January (1,000 × 1,000 Yuan).

## Turn 30 - Generic Agent

QUESTION: Regarding the workforce transition: if you start January with 1,000 workers, hire H workers, and fire F workers in January, is the workforce available for production in January equal to 1,000 + H - F, and is the workforce entering February equal to 1,000 + H - F (i.e., the end-of-January workforce carries into February)?

## Turn 30 - User Simulator

Yes, that is correct. If you start January with 1,000 workers, hire H workers, and fire F workers in January, the workforce available for production in January is 1,000 + H - F, and the workforce entering February is also 1,000 + H - F.