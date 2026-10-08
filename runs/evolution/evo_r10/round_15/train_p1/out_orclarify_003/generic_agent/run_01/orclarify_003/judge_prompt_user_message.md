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

QUESTION: Regarding workforce changes, can you hire and fire workers in any month (including January), and are hires/fires effective immediately within that same month for production purposes?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. Hires and fires are effective immediately within that same month for production purposes.

## Turn 3 - Generic Agent

QUESTION: Regarding the backorder mechanism, when you say "orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month you must first satisfy all prior backorders before satisfying that month's new demand, or can you fulfill them in any order as long as the total (backorders + current demand) is met by the end of the month?

## Turn 3 - User Simulator

You can fulfill them in any order as long as the total (backorders + current demand) is met by the end of the month.

## Turn 4 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June, does this 10,000 units need to be on hand after fulfilling all of June's demand and any remaining backorders, or is it a separate target that can be met by producing extra units beyond what's needed for demand?

## Turn 4 - User Simulator

The 10,000 units must be on hand at the end of June after fulfilling all of June's demand and any remaining backorders. It is not a separate target; it is the actual ending inventory level after all June obligations are met.

## Turn 5 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold, is revenue recognized only when a unit is actually delivered to the customer (i.e., when demand is fulfilled, whether in the current month or later via backorder fulfillment), or is revenue recognized in the month the demand was originally placed regardless of when it's fulfilled?

## Turn 5 - User Simulator

Revenue is recognized only when a unit is actually delivered to the customer, i.e., when the demand is fulfilled, whether in the current month or later via backorder fulfillment.

## Turn 6 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is this charged on the ending inventory of each month (i.e., units remaining at the end of January, end of February, etc.), and does it apply to all 6 months including June?

## Turn 6 - User Simulator

Yes, the 15 Yuan per unit holding cost is charged on the ending inventory of each month, and it applies to all 6 months, including June.

## Turn 7 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit, is this charged on the number of units that remain unfulfilled at the end of each month (i.e., the backorder balance carried into the next month), and does it apply to all months including June?

## Turn 7 - User Simulator

Yes, the 35 Yuan per unit backorder cost is charged on the number of units that remain unfulfilled at the end of each month (the backorder balance carried into the next month). It applies to all months, including June.

## Turn 8 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for 160 hours per worker, paid regardless of utilization — does this mean each worker costs 1,000 × 30 = 4,800 Yuan per month in regular wages even if they work zero hours, and this cost is incurred for every worker employed during that month?

## Turn 8 - User Simulator

Yes, each worker costs 160 hours × 30 Yuan/hour = 4,800 Yuan per month in regular wages, and this cost is incurred for every worker employed during that month, regardless of how many hours they actually work.

## Turn 9 - Generic Agent

QUESTION: Regarding the workforce level in a given month, if you start the month with W workers, hire H, and fire F, is the workforce available for production that month W + H - F, and is the workforce at the start of the next month also W + H - F?

## Turn 9 - User Simulator

Yes, the workforce available for production that month is W + H - F, and the workforce at the start of the next month is also W + H - F.

## Turn 10 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January, can this inventory be used to fulfill January's demand (and any backorders, though there are none initially), or is it reserved for a different purpose?

## Turn 10 - User Simulator

Yes, the initial inventory of 15,000 units at the start of January can be used to fulfill January's demand.

## Turn 11 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production, is this the only production cost for in-house units (i.e., in-house cost per unit = 90 Yuan raw material + labor hours already accounted for in wages), or is there an additional variable production cost on top of raw materials?

## Turn 11 - User Simulator

The 90 Yuan raw material cost is the only additional variable production cost for in-house units. The labor cost is already accounted for in the regular and overtime wages.

## Turn 12 - Generic Agent

QUESTION: Regarding the outsourced units at 200 Yuan per unit (all-inclusive), do outsourced units also require raw materials (i.e., do they incur the 90 Yuan raw material cost in addition to the 200 Yuan outsourcing cost), or is the 200 Yuan truly all-inclusive with no additional costs?

## Turn 12 - User Simulator

The 200 Yuan outsourcing cost is truly all-inclusive. Outsourced units do not incur the 90 Yuan raw material cost or any other additional costs.

## Turn 13 - Generic Agent

QUESTION: Regarding the labor hours constraint, each in-house unit requires 5 labor hours. Is the total labor hours available in a month equal to (number of workers × 160 regular hours) + (number of workers × up to 20 overtime hours), and the total in-house production in a month is limited to total available labor hours divided by 5?

## Turn 13 - User Simulator

Yes, the total labor hours available in a month is (number of workers × 160 regular hours) + (number of workers × up to 20 overtime hours). The total in-house production in a month is limited to the total available labor hours divided by 5.

## Turn 14 - Generic Agent

QUESTION: Regarding the backorder mechanism, can backorders accumulate across multiple months (e.g., if January's demand isn't fully met, the shortfall carries to February, and if February's demand plus the January backorder isn't fully met, the combined shortfall carries to March), or is there a limit on how many months a backorder can be carried?

## Turn 14 - User Simulator

Yes, backorders can accumulate across multiple months. If January's demand isn't fully met, the shortfall carries to February, and if February's demand plus the January backorder isn't fully met, the combined shortfall carries to March. There is no limit on how many months a backorder can be carried, as long as all backorders are cleared by the end of June.

## Turn 15 - Generic Agent

QUESTION: Regarding the constraint that all backorders must be cleared by the end of June, does this mean that by the end of June, the backorder balance must be zero (i.e., all cumulative demand from January through June must be fully fulfilled), in addition to the 10,000 unit ending inventory requirement?

## Turn 15 - User Simulator

Yes, by the end of June, the backorder balance must be zero, meaning all cumulative demand from January through June must be fully fulfilled. This is in addition to the 10,000 unit ending inventory requirement.

## Turn 16 - Generic Agent

QUESTION: Regarding the workforce, is there a maximum or minimum number of workers that can be employed in any month, or can the workforce be any non-negative integer (including zero)?

## Turn 16 - User Simulator

There is no maximum or minimum number of workers specified. The workforce can be any non-negative integer, including zero.

## Turn 17 - Generic Agent

QUESTION: Regarding the decision variables, are the number of workers hired and fired in each month required to be integers, and is the in-house production quantity required to be an integer, or can these be treated as continuous variables?

## Turn 17 - User Simulator

The number of workers hired and fired in each month must be integers. The in-house production quantity can be treated as a continuous variable.

## Turn 18 - Generic Agent

QUESTION: Regarding the outsourcing quantity, must it be an integer or can it be treated as a continuous variable?

## Turn 18 - User Simulator

The outsourcing quantity can be treated as a continuous variable.

## Turn 19 - Generic Agent

QUESTION: Regarding the inventory and backorder variables, can these be treated as continuous variables, or must they be integers?

## Turn 19 - User Simulator

Inventory and backorder variables can be treated as continuous variables.

## Turn 20 - Generic Agent

QUESTION: Regarding the net profit objective, is it simply total revenue (300 Yuan per unit delivered) minus all costs (raw materials, outsourcing, holding, backorder, regular wages, overtime wages, hiring, firing), with no other revenue or cost components?

## Turn 20 - User Simulator

Yes, the net profit objective is simply total revenue (300 Yuan per unit delivered) minus all costs (raw materials, outsourcing, holding, backorder, regular wages, overtime wages, hiring, firing), with no other revenue or cost components.

## Turn 21 - Generic Agent

QUESTION: Regarding the overtime hours, is the overtime hours variable in each month a continuous variable (i.e., workers can work any fractional number of overtime hours up to 20), or must overtime hours be an integer?

## Turn 21 - User Simulator

Overtime hours can be treated as a continuous variable.

## Turn 22 - Generic Agent

QUESTION: Regarding the workforce variable, is the number of workers employed in each month (the workforce level) required to be an integer, or can it be continuous?

## Turn 22 - User Simulator

The number of workers employed in each month must be an integer.

## Turn 23 - Generic Agent

QUESTION: Regarding the initial workforce of 1,000 employees at the start of January, is this the workforce level before any January hiring or firing, meaning the January workforce available for production is 1,000 + H_jan - F_jan?

## Turn 23 - User Simulator

Yes, the initial workforce of 1,000 employees is the workforce level before any January hiring or firing. The January workforce available for production is 1,000 + H_jan - F_jan.

## Turn 24 - Generic Agent

QUESTION: Regarding the revenue recognition, since revenue is recognized when a unit is delivered, and backorders can be fulfilled in later months, does this mean that if, say, 5,000 units of January's demand are backordered and fulfilled in February, the revenue for those 5,000 units is counted in February's revenue (not January's)?

## Turn 24 - User Simulator

Yes, if 5,000 units of January's demand are backordered and fulfilled in February, the revenue for those 5,000 units is counted in February's revenue, not January's.

## Turn 25 - Generic Agent

QUESTION: Regarding the total demand over six months (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500 = 174,500 units), and the initial inventory of 15,000 units, plus the requirement of 10,000 units ending inventory in June, does this mean total production (in-house + outsourced) over six months must be at least 174,500 + 10,000 - 15,000 = 169,500 units?

## Turn 25 - User Simulator

Yes, total production (in-house + outsourced) over six months must be at least 169,500 units.

## Turn 26 - Generic Agent

QUESTION: Regarding the overtime wage cost, is the overtime cost calculated as (total overtime hours in the month) × 40 Yuan per hour, where total overtime hours is the sum across all workers in that month?

## Turn 26 - User Simulator

Yes, the overtime cost is calculated as (total overtime hours in the month) × 40 Yuan per hour, where total overtime hours is the sum across all workers in that month.

## Turn 27 - Generic Agent

QUESTION: Regarding the regular wage cost, is it calculated as (number of workers employed in the month) × 4,800 Yuan, where the number of workers is the workforce level during that month (i.e., after hiring and firing for that month)?

## Turn 27 - User Simulator

Yes, the regular wage cost is calculated as (number of workers employed in the month) × 4,800 Yuan, where the number of workers is the workforce level during that month (i.e., after hiring and firing for that month).

## Turn 28 - Generic Agent

QUESTION: Regarding the hiring and firing costs, is the hiring cost 5,000 Yuan per worker hired in a given month, and the firing cost 8,000 Yuan per worker fired in a given month, with these costs incurred in the month the hire or fire occurs?

## Turn 28 - User Simulator

Yes, the hiring cost is 5,000 Yuan per worker hired in a given month, and the firing cost is 8,000 Yuan per worker fired in a given month, with these costs incurred in the month the hire or fire occurs.

## Turn 29 - Generic Agent

QUESTION: Regarding the inventory balance equation, is the ending inventory of month t equal to (beginning inventory of month t) + (in-house production in month t) + (outsourced units in month t) - (units delivered in month t), where units delivered in month t equals the total demand fulfilled in that month (including any backorders from prior months)?

## Turn 29 - User Simulator

Yes, the ending inventory of month t equals (beginning inventory of month t) + (in-house production in month t) + (outsourced units in month t) - (units delivered in month t), where units delivered in month t equals the total demand fulfilled in that month (including any backorders from prior months).

## Turn 30 - Generic Agent

QUESTION: Regarding the backorder balance equation, is the ending backorder of month t equal to (beginning backorder of month t) + (demand in month t) - (units delivered in month t), where units delivered in month t is the same quantity used in the inventory balance equation?

## Turn 30 - User Simulator

Yes, the ending backorder of month t equals (beginning backorder of month t) + (demand in month t) - (units delivered in month t), where units delivered in month t is the same quantity used in the inventory balance equation.