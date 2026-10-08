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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker is capped at 20 overtime hours per month (so total overtime is at most 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker is capped at 20 overtime hours per month. So the total overtime hours for the entire workforce in a given month is at most 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) in every month from January through June, or is hiring/firing only allowed in certain months?

## Turn 2 - User Simulator

Hiring and firing can occur in every month from January through June.

## Turn 3 - Generic Agent

QUESTION: When a worker is hired in a given month, is that worker available to work (including overtime) in that same month, or only starting the following month?

## Turn 3 - User Simulator

A worker hired in a given month is available to work, including overtime, in that same month.

## Turn 4 - Generic Agent

QUESTION: When a worker is fired in a given month, is that worker still available to work (including overtime) in that same month, or is the worker gone and unavailable starting that month?

## Turn 4 - User Simulator

A worker fired in a given month is still available to work, including overtime, in that same month.

## Turn 5 - Generic Agent

QUESTION: For the regular wage of 30 Yuan per hour for the 160 regular hours per worker, is this cost incurred for every worker employed during the month (i.e., 160 × 30 = 4,800 Yuan per worker per month) regardless of how many hours they actually work, or is it only paid for the hours actually used?

## Turn 5 - User Simulator

The regular wage is paid for every worker employed during the month, regardless of how many hours they actually work. So it is 160 × 30 = 4,800 Yuan per worker per month.

## Turn 6 - Generic Agent

QUESTION: When you say "orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the total units available to satisfy demand (previous month's ending inventory + current month's in-house production + current month's outsourced units) must be at least the current month's demand plus any backorders carried in, with any excess becoming the new ending inventory?

## Turn 6 - User Simulator

Yes, that is correct. In each month, the total units available (previous month's ending inventory + current month's in-house production + current month's outsourced units) must be at least the current month's demand plus any backorders carried in. Any excess becomes the new ending inventory.

## Turn 7 - Generic Agent

QUESTION: Can backorders accumulate over multiple months (i.e., if demand is not fully met in January, the unmet portion carries to February, and if February also cannot fully meet it, the remaining unmet portion carries to March, and so on), or must all backorders be cleared within the very next month?

## Turn 7 - User Simulator

Yes, backorders can accumulate over multiple months. If demand is not fully met in a month, the unmet portion carries to the next month, and if that month also cannot fully meet it, the remaining unmet portion carries forward again, and so on.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced in a given month, or is outsourcing unlimited?

## Turn 8 - User Simulator

There is no limit on the number of units that can be outsourced in a given month. Outsourcing is unlimited.

## Turn 9 - Generic Agent

QUESTION: Is there a minimum number of workers that must be employed at the end of June, or can the workforce be reduced to zero by the end of the planning horizon?

## Turn 9 - User Simulator

There is no minimum number of workers that must be employed at the end of June. The workforce can be reduced to zero by the end of the planning horizon.

## Turn 10 - Generic Agent

QUESTION: Is there any upper limit on the number of workers that can be hired in a single month, or is hiring unlimited?

## Turn 10 - User Simulator

There is no upper limit on the number of workers that can be hired in a single month. Hiring is unlimited.

## Turn 11 - Generic Agent

QUESTION: The backorder cost of 35 Yuan per unit is charged on the number of units backordered at the end of each month (i.e., the unmet demand carried into the next month), correct?

## Turn 11 - User Simulator

Yes, that is correct. The backorder cost of 35 Yuan per unit is charged on the number of units backordered at the end of each month, i.e., the unmet demand carried into the next month.

## Turn 12 - Generic Agent

QUESTION: The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month (i.e., the units in stock at the end of that month), correct?

## Turn 12 - User Simulator

Yes, that is correct. The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, i.e., the units in stock at the end of that month.

## Turn 13 - Generic Agent

QUESTION: Is the sales revenue of 300 Yuan per unit earned only on units actually delivered to customers (i.e., demand satisfied in the month it was due or in a later month when backorders are cleared), or is it recognized on all units produced/outsourced regardless of when they are delivered?

## Turn 13 - User Simulator

The sales revenue of 300 Yuan per unit is earned only on units actually delivered to customers. This includes demand satisfied in the month it was due and backorders cleared in a later month.

## Turn 14 - Generic Agent

QUESTION: Is the raw material cost of 90 Yuan per unit applied only to in-house produced units, or does it also apply to outsourced units?

## Turn 14 - User Simulator

The raw material cost of 90 Yuan per unit applies only to in-house produced units. It does not apply to outsourced units.

## Turn 15 - Generic Agent

QUESTION: Can the workforce be fractional (e.g., 1,000.5 workers), or must the number of workers be an integer in every month?

## Turn 15 - User Simulator

The number of workers must be an integer in every month.

## Turn 16 - Generic Agent

QUESTION: Can in-house production and outsourcing quantities be fractional, or must they be integers?

## Turn 16 - User Simulator

In-house production and outsourcing quantities must be integers.

## Turn 17 - Generic Agent

QUESTION: Can inventory and backorder quantities be fractional, or must they be integers?

## Turn 17 - User Simulator

Inventory and backorder quantities must be integers.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that prevents both inventory and backorders from being positive in the same month (i.e., can you simultaneously have unsold stock and unmet demand)?

## Turn 18 - User Simulator

There is no explicit constraint that prevents both inventory and backorders from being positive in the same month. However, in practice, it would not be optimal to have both simultaneously, as you would be paying holding costs on inventory while also paying backorder costs on unmet demand.

## Turn 19 - Generic Agent

QUESTION: For the June ending inventory requirement of at least 10,000 units, does this apply to the physical inventory at the end of June (after satisfying June's demand and any backorders carried into June), meaning that if there are still backorders at the end of June, the 10,000-unit minimum applies to the net inventory (physical stock minus backorders), or does it apply to physical stock only regardless of any remaining backorders?

## Turn 19 - User Simulator

The 10,000-unit minimum applies to the physical inventory at the end of June, after satisfying June's demand and any backorders carried into June. Since all backorders must be cleared by the end of June, there are no remaining backorders to subtract. The requirement is simply that the physical stock on hand at the end of June is at least 10,000 units.

## Turn 20 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June. Is this an explicit constraint (i.e., backorders at the end of June must equal zero), or is it simply implied by the 10,000-unit minimum inventory requirement?

## Turn 20 - User Simulator

Yes, it is an explicit constraint. All backorders must be cleared by the end of June, meaning backorders at the end of June must equal zero.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the workforce at the start of January must be exactly 1,000 (i.e., you cannot hire or fire before January begins), or can you adjust the workforce before the planning period starts?

## Turn 21 - User Simulator

The workforce at the start of January must be exactly 1,000. You cannot hire or fire before January begins.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the initial inventory at the start of January must be exactly 15,000 units (i.e., you cannot adjust it before the planning period starts)?

## Turn 22 - User Simulator

Yes, the initial inventory at the start of January must be exactly 15,000 units. It cannot be adjusted before the planning period starts.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint on the workforce at the end of June (e.g., a minimum or maximum number of workers that must remain employed after the planning period), or is the end-of-June workforce free to be any non-negative integer?

## Turn 23 - User Simulator

There is no constraint on the workforce at the end of June. The end-of-June workforce is free to be any non-negative integer.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the workforce cannot go below zero (i.e., you cannot fire more workers than you currently have), or is that implicitly understood?

## Turn 24 - User Simulator

Yes, the workforce cannot go below zero. You cannot fire more workers than you currently have.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the workforce must be non-decreasing or non-increasing over the six months, or can it fluctuate freely (hiring in some months and firing in others)?

## Turn 25 - User Simulator

The workforce can fluctuate freely over the six months. You can hire in some months and fire in others, with no requirement that the workforce be non-decreasing or non-increasing.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of a month (after hiring/firing) must be the same as the workforce available to work in that month, or is there a distinction between the workforce used for production in a month and the workforce carried into the next month?

## Turn 26 - User Simulator

The workforce at the end of a month (after hiring/firing) is the same as the workforce available to work in that month. There is no distinction between the workforce used for production in a month and the workforce carried into the next month.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the workforce at the start of a month (before hiring/firing) must equal the workforce at the end of the previous month, or can there be a gap?

## Turn 27 - User Simulator

The workforce at the start of a month (before hiring/firing) must equal the workforce at the end of the previous month. There is no gap.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the workforce at the start of January (1,000) is the workforce available to work in January, or is there a separate hiring/firing decision at the start of January before production begins?

## Turn 28 - User Simulator

The workforce at the start of January (1,000) is the workforce available to work in January. There is no separate hiring/firing decision at the start of January before production begins.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of June must equal the workforce at the start of July (i.e., the workforce after June's hiring/firing is carried into July), or is the planning horizon strictly January through June with no carry-over consideration?

## Turn 29 - User Simulator

The planning horizon is strictly January through June with no carry-over consideration. There is no constraint that the workforce at the end of June must equal the workforce at the start of July.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of a month (after hiring/firing) must be at least the number of workers needed to produce the in-house units in that month, or can the workforce be reduced below what is needed for production within the same month?

## Turn 30 - User Simulator

There is no such constraint. The workforce at the end of a month (after hiring/firing) does not need to be at least the number of workers needed to produce the in-house units in that month. The workforce available to work in a month is determined by the hiring/firing decisions made in that month, and production is based on that available workforce.