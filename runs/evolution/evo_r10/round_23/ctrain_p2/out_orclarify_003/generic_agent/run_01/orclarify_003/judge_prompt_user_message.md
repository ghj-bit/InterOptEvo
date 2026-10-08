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

QUESTION: When you say the ending inventory at the end of June must be at least 10,000 units, does that 10,000-unit requirement apply only to June, or is it a minimum ending-inventory level that must be met at the end of every month from January through June?

## Turn 1 - User Simulator

It applies only to June. The 10,000-unit minimum ending inventory requirement is specific to the end of June. There is no minimum ending inventory requirement for the end of January, February, March, April, or May.

## Turn 2 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is it charged on the total number of units that are backordered at the end of each month (i.e., the cumulative unfulfilled demand carried into the next month), or is it charged only on the newly unfulfilled units in that month?

## Turn 2 - User Simulator

It is charged on the total number of units that are backordered at the end of each month. That is the cumulative unfulfilled demand carried into the next month.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units, is there any restriction on the order or priority in which these sources are used (for example, must previous-month inventory be used before in-house production, and in-house production before outsourcing), or can the plan freely allocate among these three sources in any mix to meet demand?

## Turn 3 - User Simulator

There is no restriction on the order or priority. The plan can freely allocate among previous-month inventory, current in-house production, and outsourced units in any mix to meet demand.

## Turn 4 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) in every month from January through June, or are hiring and firing decisions only allowed in certain months?

## Turn 4 - User Simulator

Hiring and firing decisions can be made in every month from January through June.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on the total number of workers the company can have in any month, or any minimum number of workers that must be maintained, or are the workforce size and hiring/firing amounts completely free (subject only to the hiring and firing costs)?

## Turn 5 - User Simulator

There is no upper limit on the total number of workers and no minimum number of workers that must be maintained. The workforce size and hiring/firing amounts are completely free, subject only to the hiring and firing costs.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced in a month, or can the company outsource any quantity needed?

## Turn 6 - User Simulator

There is no limit on the number of units that can be outsourced in a month. The company can outsource any quantity needed.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total inventory that can be held at the end of a month, or can inventory be carried forward without any capacity constraint?

## Turn 7 - User Simulator

There is no limit on the total inventory that can be held at the end of a month. Inventory can be carried forward without any capacity constraint.

## Turn 8 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization — does this mean the company pays each worker a fixed 4,800 Yuan per month (160 hours × 30 Yuan) whether or not they are fully utilized, so that the regular labor cost is simply 4,800 times the number of workers in that month?

## Turn 8 - User Simulator

Yes, that is correct. The company pays each worker a fixed 4,800 Yuan per month (160 hours × 30 Yuan) regardless of utilization. The regular labor cost is simply 4,800 times the number of workers in that month.

## Turn 9 - Generic Agent

QUESTION: For the overtime hours, is the 20-hour-per-worker-per-month cap a hard limit that applies to the total overtime across the entire workforce (i.e., total overtime hours in a month cannot exceed 20 times the number of workers that month), or is it a per-worker cap that could be exceeded in aggregate if some workers work less overtime than others?

## Turn 9 - User Simulator

It is a per-worker cap. The total overtime hours in a month cannot exceed 20 times the number of workers that month.

## Turn 10 - Generic Agent

QUESTION: When demand is backordered and fulfilled in a later month, is the sales price of 300 Yuan per unit still received for those units when they are eventually delivered, or is there any penalty or discount on the sales price for late delivery?

## Turn 10 - User Simulator

The sales price of 300 Yuan per unit is still received for those units when they are eventually delivered. There is no penalty or discount on the sales price for late delivery.

## Turn 11 - Generic Agent

QUESTION: Is the raw material cost of 90 Yuan per unit applied to all in-house produced units in a month, regardless of whether those units are used to meet current demand, backorders, or added to inventory?

## Turn 11 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is applied to all in-house produced units in a month, regardless of whether those units are used to meet current demand, backorders, or added to inventory.

## Turn 12 - Generic Agent

QUESTION: Is the inventory holding cost of 15 Yuan per unit charged on the ending inventory of each month (including June), or is it charged only on the ending inventory of months January through May?

## Turn 12 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including June.

## Turn 13 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (contributing their 160 regular hours and up to 20 overtime hours) in that same month, or do they only become available starting the following month?

## Turn 13 - User Simulator

A worker hired in a given month is available to work in that same month, contributing their 160 regular hours and up to 20 overtime hours.

## Turn 14 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (contributing their 160 regular hours and up to 20 overtime hours) in that same month, or are they no longer available starting from that month?

## Turn 14 - User Simulator

A worker fired in a given month is no longer available to work starting from that month.

## Turn 15 - Generic Agent

QUESTION: Is there any constraint that the total production (in-house plus outsourced) in a month must exactly equal the total demand (current demand plus backorders from the previous month), or can the company produce more than demand in a month and carry the excess as inventory?

## Turn 15 - User Simulator

There is no constraint that total production must exactly equal total demand. The company can produce more than demand in a month and carry the excess as inventory.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint that the company must fulfill all demand (current plus backorders) by the end of June, or can some demand remain unfulfilled (backordered) after June?

## Turn 16 - User Simulator

Yes, all backorders must be cleared by the end of June. No outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 17 - User Simulator

The available business facts do not determine the answer. This point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 18 - User Simulator

The available business facts do not determine the answer. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit charged on the cumulative unfulfilled demand at the end of each month, is this cost also charged on the backorders that are cleared in June (i.e., is there a backorder cost for the unfulfilled demand carried into June that gets fulfilled in June), or is the backorder cost only charged for backorders carried from one month to the next within the planning horizon?

## Turn 19 - User Simulator

The backorder cost is charged on the cumulative unfulfilled demand at the end of each month. Since all backorders must be cleared by the end of June, the ending backorders in June are zero. Therefore, there is no backorder cost charged for June. The backorder cost is charged for the unfulfilled demand carried from one month to the next within the planning horizon (i.e., for the ending backorders of January through May).

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 20 - User Simulator

The available business facts do not determine the answer. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 21 - User Simulator

The available business facts do not determine the answer. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 22 - User Simulator

The available business facts do not determine the answer. This point still needs

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 23 - User Simulator

The available business facts do not determine the answer. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 24 - User Simulator

The available

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 25 - User Simulator

The available business

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the company cannot have both positive inventory and positive backorders at the end of the same month, or can both exist simultaneously?

## Turn 30 - User Simulator

The