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

QUESTION: When you say the total overtime hours per month for the entire workforce cannot exceed 20 hours per worker, do you mean each individual worker can work at most 20 overtime hours in a given month (so total overtime is capped at 20 times the number of workers that month), or that the whole workforce combined can work at most 20 overtime hours total in a month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime hours for the entire workforce in a month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you said it is paid regardless of utilization — does that mean the company pays 30 Yuan/hour for all 160 regular hours of every worker employed in a month (i.e., 48,000 Yuan per worker per month) even if the worker's hours are not fully used for production, or is the regular wage only paid for the hours actually worked up to the 160-hour cap?

## Turn 2 - User Simulator

The company pays 30 Yuan/hour for all 160 regular hours of every worker employed in a month, even if the worker's hours are not fully used for production. So the regular wage cost is 48,000 Yuan per worker per month.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units — is there any limit on how many units can be outsourced in a given month, or can the company outsource an unlimited number of units as long as it pays 200 Yuan per unit?

## Turn 3 - User Simulator

There is no limit on how many units can be outsourced in a given month. The company can outsource an unlimited number of units as long as it pays 200 Yuan per unit.

## Turn 4 - Generic Agent

QUESTION: Regarding the workforce, can the company hire and fire workers in any month from January through June, or are hiring and firing decisions only allowed in certain months?

## Turn 4 - User Simulator

The company can hire and fire workers in any month from January through June.

## Turn 5 - Generic Agent

QUESTION: When a worker is hired or fired in a given month, does that worker count toward the workforce for that same month's production (i.e., a worker hired in January can work in January, and a worker fired in January is not available for January production), or does the change take effect starting the following month?

## Turn 5 - User Simulator

A worker hired in a given month is available for that same month's production, and a worker fired in a given month is not available for that same month's production.

## Turn 6 - Generic Agent

QUESTION: For the inventory balance, when you say ending inventory at the end of June must be at least 10,000 units — does this 10,000-unit requirement apply only to June, or is there a minimum inventory level required at the end of every month?

## Turn 6 - User Simulator

The 10,000-unit minimum inventory requirement applies only to the end of June. There is no minimum inventory level required at the end of any other month.

## Turn 7 - Generic Agent

QUESTION: Regarding backorders — if demand in a month exceeds what can be fulfilled (from prior inventory, in-house production, and outsourcing), the unfulfilled portion is carried as a backorder to the next month. Is there any limit on how many units can be back-ordered in a given month, or can an unlimited amount of demand be deferred?

## Turn 7 - User Simulator

There is no limit on how many units can be back-ordered in a given month. An unlimited amount of demand can be deferred, as long as all backorders are cleared by the end of June.

## Turn 8 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June — does this mean that by the end of June, all demand from January through June (including any previously back-ordered units) must have been fulfilled, so that the ending inventory of 10,000 units is on top of having satisfied all cumulative demand?

## Turn 8 - User Simulator

Yes, that is correct. By the end of June, all demand from January through June, including any previously back-ordered units, must have been fulfilled. The ending inventory of 10,000 units is on top of having satisfied all cumulative demand.

## Turn 9 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit — is revenue recognized only when a unit is actually delivered to the customer (i.e., when demand is fulfilled, whether in the current month or a later month for backorders), or is revenue recognized in the month the demand originally occurred regardless of when it is fulfilled?

## Turn 9 - User Simulator

Revenue is recognized only when a unit is actually delivered to the customer, i.e., when demand is fulfilled, whether in the current month or a later month for backorders.

## Turn 10 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit — is this charged on the ending inventory of each month (i.e., units left over at the end of January, end of February, etc.), and does it also apply to the 10,000 units held at the end of June?

## Turn 10 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including the 10,000 units held at the end of June.

## Turn 11 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit — is this charged on the number of units that are back-ordered at the end of each month (i.e., the unfulfilled demand carried into the next month), and is it charged for each month a unit remains back-ordered?

## Turn 11 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is charged on the number of units that are back-ordered at the end of each month, and it is charged for each month a unit remains back-ordered.

## Turn 12 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production — is this the only material cost, or is there also a material cost associated with outsourced units (i.e., does the 200 Yuan outsourcing cost already include all materials, or does the company also pay 90 Yuan per outsourced unit for materials)?

## Turn 12 - User Simulator

The 200 Yuan outsourcing cost is all-inclusive and already includes all materials. The company does not pay the 90 Yuan raw material cost for outsourced units.

## Turn 13 - Generic Agent

QUESTION: Regarding the workforce — is there a maximum number of workers the company can employ in any month, or is the workforce size unbounded (limited only by the hiring cost)?

## Turn 13 - User Simulator

The workforce size is unbounded. There is no maximum number of workers the company can employ in any month; it is limited only by the hiring cost.

## Turn 14 - Generic Agent

QUESTION: Regarding the workforce — is there a minimum number of workers the company must maintain in any month, or can the workforce be reduced to zero if that is optimal?

## Turn 14 - User Simulator

There is no minimum number of workers the company must maintain in any month. The workforce can be reduced to zero if that is optimal.

## Turn 15 - Generic Agent

QUESTION: Regarding the in-house production capacity — is the only constraint on in-house production the available labor hours (regular 160 hours plus overtime up to 20 hours per worker), or is there any other capacity limit such as a maximum number of units that can be produced in-house per month regardless of labor hours?

## Turn 15 - User Simulator

The only constraint on in-house production is the available labor hours (regular 160 hours plus overtime up to 20 hours per worker). There is no other capacity limit such as a maximum number of units that can be produced in-house per month regardless of labor hours.

## Turn 16 - Generic Agent

QUESTION: Regarding the inventory balance — when fulfilling demand in a given month, is there a specific priority order for using available sources (e.g., must use prior inventory first, then in-house production, then outsourcing), or can the company freely mix the three sources in any proportion to fulfill demand?

## Turn 16 - User Simulator

The company can freely mix the three sources (prior inventory, in-house production, and outsourcing) in any proportion to fulfill demand. There is no specific priority order required.

## Turn 17 - Generic Agent

QUESTION: Regarding the net profit objective — is the total net profit calculated as total revenue minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other costs or taxes to consider?

## Turn 17 - User Simulator

Yes, the total net profit is calculated as total revenue minus all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing. There are no other costs or taxes to consider.

## Turn 18 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January — is this inventory available to fulfill January demand (and any backorders from before January, though there are none), and does it incur a holding cost if it is not used in January?

## Turn 18 - User Simulator

Yes, the initial inventory of 15,000 units at the start of January is available to fulfill January demand. If any of those units are not used in January, they remain as ending inventory for January and incur the 15 Yuan per unit holding cost.

## Turn 19 - Generic Agent

QUESTION: Regarding the initial workforce of 1,000 employees at the start of January — are these 1,000 workers available for January production (contributing 160 regular hours each plus up to 20 overtime hours each), and does the company pay the regular wage of 48,000 Yuan per worker for January for all 1,000 workers?

## Turn 19 - User Simulator

Yes, the 1,000 workers at the start of January are available for January production, contributing 160 regular hours each plus up to 20 overtime hours each. The company pays the regular wage of 48,000 Yuan per worker for January for all 1,000 workers.

## Turn 20 - Generic Agent

QUESTION: Regarding the hiring and firing costs — is the hiring cost of 5,000 Yuan paid once per worker when they are hired, and the firing cost of 8,000 Yuan paid once per worker when they are fired, with no recurring or additional costs associated with workforce changes?

## Turn 20 - User Simulator

Yes, the hiring cost of 5,000 Yuan is paid once per worker when they are hired, and the firing cost of 8,000 Yuan is paid once per worker when they are fired. There are no recurring or additional costs associated with workforce changes.

## Turn 21 - Generic Agent

QUESTION: Regarding the overtime hours — if a worker works overtime in a given month, is the overtime cost simply 40 Yuan per overtime hour worked, with no additional premium or penalty beyond the 40 Yuan rate, and does the overtime work contribute to in-house production just like regular hours?

## Turn 21 - User Simulator

Yes, the overtime cost is simply 40 Yuan per overtime hour worked, with no additional premium or penalty beyond the 40 Yuan rate. Overtime work contributes to in-house production just like regular hours.

## Turn 22 - Generic Agent

QUESTION: Regarding the demand forecast — is the demand for each month a fixed, known quantity that must be fulfilled (i.e., the company cannot choose to sell fewer than the forecasted demand), or is the demand a maximum that the company can choose to partially fulfill?

## Turn 22 - User Simulator

The demand for each month is a fixed, known quantity that must be fulfilled. The company cannot choose to sell fewer than the forecasted demand.

## Turn 23 - Generic Agent

QUESTION: Regarding the workforce in a given month — if the company both hires and fires workers in the same month, is the workforce available for production that month equal to the starting workforce plus hires minus firings, and are the hiring and firing costs simply the sum of 5,000 times the number hired plus 8,000 times the number fired?

## Turn 23 - User Simulator

Yes, the workforce available for production in a given month is equal to the starting workforce plus hires minus firings. The hiring and firing costs are simply the sum of 5,000 times the number hired plus 8,000 times the number fired.

## Turn 24 - Generic Agent

QUESTION: Regarding the inventory and backorder balance in a given month — is the ending inventory for that month equal to the beginning inventory plus in-house production plus outsourcing minus the units delivered to fulfill that month's demand (including any backorders from prior months), and is the backorder for that month equal to the total unfulfilled demand (current plus prior backorders) minus the units delivered?

## Turn 24 - User Simulator

Yes, the ending inventory for a given month is equal to the beginning inventory plus in-house production plus outsourcing minus the units delivered to fulfill that month's demand (including any backorders from prior months). The backorder for that month is equal to the total unfulfilled demand (current plus prior backorders) minus the units delivered.

## Turn 25 - Generic Agent

QUESTION: Regarding the relationship between ending inventory and backorders in a given month — can both ending inventory and backorders be positive in the same month, or must one of them be zero (i.e., if there is leftover inventory, all backorders must be cleared, and vice versa)?

## Turn 25 - User Simulator

Both ending inventory and backorders can be positive in the same month. There is no requirement that one of them must be zero.

## Turn 26 - Generic Agent

QUESTION: Regarding the workforce and labor hours — if the company has, say, 1,000 workers in a month, the total available regular hours are 160,000 and the total available overtime hours are up to 20,000. Is the in-house production in that month limited to (160,000 + overtime hours used) divided by 5 units, where overtime hours used can be any value from 0 to 20,000?

## Turn 26 - User Simulator

Yes, the in-house production in that month is limited to (160,000 + overtime hours used) divided by 5 units, where overtime hours used can be any value from 0 to 20,000.

## Turn 27 - Generic Agent

QUESTION: Regarding the net profit objective — since revenue is recognized when units are delivered, and all demand must be fulfilled by the end of June, does this mean total revenue is simply 300 Yuan times the total demand over six months (175,500 units), making it a constant, and the optimization is effectively minimizing total costs?

## Turn 27 - User Simulator

Yes, since all demand must be fulfilled by the end of June, total revenue is simply 300 Yuan times the total demand over six months (175,500 units), making it a constant. The optimization is effectively minimizing total costs.

## Turn 28 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units — is this inventory already paid for (i.e., it is a sunk cost and does not appear in the objective function), or does the company need to account for the cost of this initial inventory in the net profit calculation?

## Turn 28 - User Simulator

The initial inventory of 15,000 units is already paid for. It is a sunk cost and does not appear in the objective function.

## Turn 29 - Generic Agent

QUESTION: Regarding the initial workforce of 1,000 workers — is the cost of these 1,000 workers (their regular wages) already accounted for as a sunk cost, or does the company pay their regular wages of 48,000 Yuan per worker per month as part of the optimization's cost structure?

## Turn 29 - User Simulator

The company pays the regular wages of 48,000 Yuan per worker per month for the initial 1,000 workers as part of the optimization's cost structure. It is not a sunk cost.

## Turn 30 - Generic Agent

QUESTION: Regarding the workforce in a given month — if the company has W workers available for production that month, is the total regular wage cost for that month simply 48,000 times W, regardless of how many regular hours are actually used for production?

## Turn 30 - User Simulator

Yes, the total regular wage cost for that month is simply 48,000 times W, regardless of how many regular hours are actually used for production.