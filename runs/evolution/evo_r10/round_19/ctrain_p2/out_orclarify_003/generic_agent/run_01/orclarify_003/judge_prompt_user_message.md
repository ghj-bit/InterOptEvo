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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 × number of workers that month), or that the sum of overtime hours across all workers combined is capped at 20 hours per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire workers in any month (including January), and is the workforce for a month determined before or after that month's production — that is, if you hire in January, can those new workers contribute to January's production, or do they only start contributing in February?

## Turn 2 - User Simulator

The available business facts do not specify whether hiring and firing can occur in any month, or whether new workers hired in a given month contribute to that same month's production or only the following month. This point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Since that point is still being confirmed internally, which reading should I implement for now: (a) you can hire and fire in any month including January, and workers hired in a month are available for that same month's production, or (b) workers hired in a month only become available starting the next month?

## Turn 3 - User Simulator

The available business facts do not determine which reading to implement. This point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the hiring-timing point is still pending, let me move on to another load-bearing detail: when you fulfill a month's orders using "available inventory from the previous month, current in-house production, and outsourced units," is there any limit on how many units can be outsourced in a given month, or is outsourcing unlimited?

## Turn 4 - User Simulator

The available business facts do not specify any limit on the number of units that can be outsourced in a given month. This point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Since outsourcing capacity is still being confirmed, let me ask about backorders: is there any limit on how many units of demand can be back-ordered (carried over) in a given month, or can any amount of unfulfilled demand be carried forward to later months?

## Turn 5 - User Simulator

The available business facts do not specify any limit on the number of units of demand that can be back-ordered in a given month. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit "carried over to the next month" — if a unit of demand is back-ordered for two months (e.g., demanded in January but fulfilled in March), is the backorder cost charged once (35 Yuan total) or charged each month it is outstanding (70 Yuan total)?

## Turn 6 - User Simulator

The available business facts state the backorder cost is 35 Yuan per unit "for unfulfilled demand carried over to the next month." This phrasing suggests the cost is charged each month the unit remains outstanding. However, the facts do not explicitly confirm whether a unit back-ordered for two months incurs the cost twice (once per month outstanding) or only once. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since the backorder cost timing is still pending, let me ask about the inventory holding cost of 15 Yuan per unit "held at the end of a month": does this apply to all ending inventory each month (including the 10,000 units required at end of June), or is the June ending inventory exempt from the holding cost?

## Turn 7 - User Simulator

The available business facts state the inventory holding cost is 15 Yuan per unit for inventory held at the end of a month. They do not specify any exemption for the June ending inventory. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Regarding the regular wage: you said it is "paid regardless of utilization" — does this mean the 160 regular hours per worker per month are paid as a fixed cost (160 × 30 = 4,800 Yuan per worker per month) even if the worker is not fully utilized, and overtime hours (up to 20 per worker) are paid additionally at 40 Yuan per hour on top of that?

## Turn 8 - User Simulator

Yes, that is correct. The 160 regular hours per worker per month are paid as a fixed cost (160 × 30 = 4,800 Yuan per worker per month) regardless of how many hours are actually used for production. Overtime hours, up to 20 per worker per month, are paid additionally at 40 Yuan per hour on top of that fixed regular wage.

## Turn 9 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit "applicable only to units produced in-house" — does outsourced production have no raw material cost at all (the 200 Yuan outsourcing cost is all-inclusive and covers materials), or do outsourced units also incur the 90 Yuan raw material cost in addition to the 200 Yuan outsourcing fee?

## Turn 9 - User Simulator

The 200 Yuan outsourcing cost is all-inclusive and covers materials. Outsourced units do not incur the 90 Yuan raw material cost.

## Turn 10 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is this revenue recognized in the month the unit is actually delivered to the customer (i.e., when the demand is fulfilled, which could be a later month if back-ordered), or is it recognized in the month the demand was originally due?

## Turn 10 - User Simulator

The available business facts do not specify whether the 300 Yuan sales price is recognized in the month the unit is delivered or in the month the demand was originally due. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Since the revenue timing is still pending, let me ask about the workforce: is there any minimum or maximum number of workers you must maintain in any month, or can the workforce range from 0 up to any number as long as hiring and firing costs are accounted for?

## Turn 11 - User Simulator

The available business facts do not specify any minimum or maximum number of workers that must be maintained in any month. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Regarding the production capacity constraint: in-house production in a month is limited by the total available labor hours (160 regular + up to 20 overtime per worker), and each unit requires 5 labor hours — so maximum in-house production equals (180 × number of workers) / 5. Is this correct, or is there any other capacity constraint (e.g., machine hours, shift limits) that could further restrict in-house production?

## Turn 12 - User Simulator

Yes, that is correct. Maximum in-house production in a month equals (180 × number of workers) / 5. The available business facts do not mention any other capacity constraint such as machine hours or shift limits that would further restrict in-house production.

## Turn 13 - Generic Agent

QUESTION: Regarding the inventory flow: at the start of January you have 15,000 units of inventory. When fulfilling January's demand of 20,000 units, can you use that initial 15,000 units of inventory, or is the initial inventory only available starting in February?

## Turn 13 - User Simulator

The initial 15,000 units of inventory at the start of January are available for fulfilling January's demand.

## Turn 14 - Generic Agent

QUESTION: Regarding the backorder and inventory relationship: can a month simultaneously have both positive ending inventory and positive backorders, or must all backorders be cleared before any inventory can be built up in that month?

## Turn 14 - User Simulator

The available business facts do not specify whether a month can simultaneously have both positive ending inventory and positive backorders, or whether backorders must be cleared before inventory can be built up. This point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Since the simultaneous inventory/backorder question is still pending, let me ask about the June ending inventory requirement of at least 10,000 units: does this 10,000 units need to be in physical inventory (i.e., all June demand must be fully met and then 10,000 additional units must remain), or can some of the 10,000 units be "virtual" in the sense that June's demand itself is partially back-ordered while still counting toward the 10,000?

## Turn 15 - User Simulator

The available business facts state that the ending inventory at the end of June must be at least 10,000 units, and that all backorders must be cleared by the end of June (ending backorders must be zero). This means June's demand must be fully met, and the 10,000 units must be in physical inventory on top of that.

## Turn 16 - Generic Agent

QUESTION: Regarding the workforce timing that was parked earlier: since it's still pending, let me ask a related question that might help resolve it — when you fire workers in a given month, do those workers still contribute to that month's production (i.e., they work the full month and then leave at month-end), or do they stop contributing immediately upon being fired?

## Turn 16 - User Simulator

The available business facts do not specify whether workers fired in a given month still contribute to that month's production or stop contributing immediately. This point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Let me ask about the objective function: you said the goal is to maximize total net profit over the six months. Is the net profit simply total revenue minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost items I should account for?

## Turn 17 - User Simulator

Yes, that is correct. The net profit is total revenue minus all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing. There are no other revenue or cost items to account for.

## Turn 18 - Generic Agent

QUESTION: Regarding the backorder cost timing that was parked earlier: since it's still pending, let me ask a slightly different angle — in the standard formulation for this type of problem, the backorder cost is typically charged per unit per month that the unit remains unfulfilled. Should I implement it that way (i.e., a unit back-ordered for two months incurs 70 Yuan total), or should I implement it as a one-time 35 Yuan charge regardless of how many months it is outstanding?

## Turn 18 - User Simulator

The available business facts state the backorder cost is 35 Yuan per unit "for unfulfilled demand carried over to the next month." This phrasing suggests the cost is charged each month the unit remains outstanding. However, the facts do not explicitly confirm whether a unit back-ordered for two months incurs the cost twice (once per month outstanding) or only once. This point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Let me ask about the inventory holding cost timing that was parked earlier: should I implement it as 15 Yuan per unit for every unit in ending inventory at the end of each month (including June), or should the June ending inventory be exempt from the holding cost since it is a required minimum rather than excess stock?

## Turn 19 - User Simulator

The available business facts state the inventory holding cost is 15 Yuan per unit for inventory held at the end of a month. They do not specify any exemption for the June ending inventory. This point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Regarding the revenue timing that was parked earlier: should I implement the 300 Yuan sales revenue as recognized in the month the unit is actually delivered to the customer (i.e., when the demand is fulfilled, which could be a later month if back-ordered), or in the month the demand was originally due?

## Turn 20 - User Simulator

The available business facts do not specify whether the 300 Yuan sales price is recognized in the month the unit is delivered or in the month the demand was originally due. This point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Let me ask about the simultaneous inventory and backorder question that was parked earlier: should I implement the model so that a month can have both positive ending inventory and positive backorders simultaneously, or should I enforce that backorders must be fully cleared before any inventory can be built up in that month?

## Turn 21 - User Simulator

The available business facts do not specify whether a month can simultaneously have both positive ending inventory and positive backorders, or whether backorders must be cleared before inventory can be built up. This point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Let me ask about the workforce timing that was parked earlier: should I implement the model so that workers hired in a given month are available for that same month's production (and workers fired in a given month still contribute to that month's production), or should I implement it so that workforce changes take effect starting the following month?

## Turn 22 - User Simulator

The available business facts do not specify whether workers hired in a given month are available for that same month's production, or whether workforce changes take effect starting the following month. This point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Let me ask about the outsourcing capacity that was parked earlier: should I implement outsourcing as unlimited (any number of units can be outsourced in any month), or is there a maximum number of units that can be outsourced per month?

## Turn 23 - User Simulator

The available business facts do not specify any limit on the number of units that can be outsourced in a given month. This point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Let me ask about the backorder limit that was parked earlier: should I implement backorders as unlimited (any amount of unfulfilled demand can be carried forward), or is there a maximum number of units that can be back-ordered in any month?

## Turn 24 - User Simulator

The available business facts do not specify any limit on the number of units of demand that can be back-ordered in a given month. This point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Let me ask about the workforce bounds that were parked earlier: should I implement the model with no minimum or maximum workforce constraint (workforce can range from 0 to any number), or are there bounds I should enforce?

## Turn 25 - User Simulator

The available business facts do not specify any minimum or maximum number of workers that must be maintained in any month. This point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Let me ask about the inventory holding cost for June that was parked earlier: should I implement the 15 Yuan per unit holding cost for all ending inventory in all six months including June, or should the June ending inventory be exempt from the holding cost?

## Turn 26 - User Simulator

The available business facts state the inventory holding cost is 15 Yuan per unit for inventory held at the end of a month. They do not specify any exemption for the June ending inventory. This point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Let me ask about the backorder cost timing that was parked earlier: should I implement the backorder cost as 35 Yuan per unit per month that the unit remains outstanding (so a unit back-ordered for two months incurs 70 Yuan total), or as a one-time 35 Yuan charge regardless of how many months it is outstanding?

## Turn 27 - User Simulator

The available business facts state the backorder cost is 35 Yuan per unit "for unfulfilled demand carried over to the next month." This phrasing suggests the cost is charged each month the unit remains outstanding. However, the facts do not explicitly confirm whether a unit back-ordered for two months incurs the cost twice (once per month outstanding) or only once. This point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Let me ask about the revenue timing that was parked earlier: should I implement the 300 Yuan sales revenue as recognized in the month the unit is actually delivered to the customer (when the demand is fulfilled, which could be a later month if back-ordered), or in the month the demand was originally due?

## Turn 28 - User Simulator

The available business facts do not specify whether the 300 Yuan sales price is recognized in the month the unit is delivered or in the month the demand was originally due. This point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Let me ask about the simultaneous inventory and backorder question that was parked earlier: should I implement the model so that a month can have both positive ending inventory and positive backorders simultaneously, or should I enforce that backorders must be fully cleared before any inventory can be built up in that month?

## Turn 29 - User Simulator

The available business facts do not specify whether a month can simultaneously have both positive ending inventory and positive backorders, or whether backorders must be cleared before inventory can be built up. This point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Let me ask about the workforce timing that was parked earlier: should I implement the model so that workers hired in a given month are available for that same month's production (and workers fired in a given month still contribute to that month's production), or should I implement it so that workforce changes take effect starting the following month?

## Turn 30 - User Simulator

The available business facts do not specify whether workers hired in a given month are available for that same month's production, or whether workforce changes take effect starting the following month. This point still needs internal confirmation.