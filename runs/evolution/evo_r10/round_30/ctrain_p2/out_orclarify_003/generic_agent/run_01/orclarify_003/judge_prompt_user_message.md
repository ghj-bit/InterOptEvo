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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 × number of workers that month), or that the whole workforce combined can work at most 20 overtime hours total in a month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you state it is 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization — does this mean each worker's regular wage is a fixed 4,800 Yuan per month (160 × 30) even if they work fewer than 160 regular hours, or is the regular wage only paid for the regular hours actually worked up to a maximum of 160?

## Turn 2 - User Simulator

Each worker's regular wage is a fixed 4,800 Yuan per month (160 hours × 30 Yuan/hour), paid regardless of how many regular hours are actually utilized.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered (unfulfilled in the current month), is the backorder cost of 35 Yuan per unit charged once for the month the demand is carried over, and then charged again in each subsequent month until the order is finally fulfilled, or is it charged only once total per unit regardless of how many months it is delayed?

## Turn 3 - User Simulator

The backorder cost of 35 Yuan per unit is charged for each month the demand is carried over. So if an order is back-ordered for two months before being fulfilled, the cost is 35 Yuan for the first month and another 35 Yuan for the second month, totaling 70 Yuan for that unit.

## Turn 4 - Generic Agent

QUESTION: When you say orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units — is there any limit on how many units can be outsourced in a given month, or can you outsource an unlimited number of units each month?

## Turn 4 - User Simulator

There is no limit on the number of units that can be outsourced in a given month. You can outsource as many units as needed, subject only to the cost of 200 Yuan per unit.

## Turn 5 - Generic Agent

QUESTION: Can the workforce (number of workers) change from month to month through hiring and firing, or is the workforce fixed at 1,000 workers for all six months?

## Turn 5 - User Simulator

The workforce can change from month to month through hiring and firing. The 1,000 workers is only the starting level at the beginning of January. You may hire or fire workers in any month, incurring the respective costs of 5,000 Yuan per new worker hired and 8,000 Yuan per worker fired.

## Turn 6 - Generic Agent

QUESTION: When workers are hired or fired in a given month, are they available for production (regular and overtime hours) in that same month, or do they only become available starting the following month?

## Turn 6 - User Simulator

Workers hired in a given month are available for production (regular and overtime hours) in that same month. Similarly, workers fired in a given month are not available for production in that month; they are only available through the end of the previous month.

## Turn 7 - Generic Agent

QUESTION: When you say workers fired in a given month are not available for production in that month, does this mean the firing decision is made at the start of the month (so those workers are gone for the entire month), or at the end of the month (so they work the full month and then leave)?

## Turn 7 - User Simulator

The firing decision is made at the start of the month. Workers who are fired in a given month are not available for production in that month; they are gone for the entire month.

## Turn 8 - Generic Agent

QUESTION: When you say workers hired in a given month are available for production in that same month, does this mean the hiring decision is also made at the start of the month, so new workers are available for the full month's production?

## Turn 8 - User Simulator

Yes, the hiring decision is made at the start of the month, so new workers are available for the full month's production.

## Turn 9 - Generic Agent

QUESTION: The raw material cost of 90 Yuan per unit applies only to in-house production. Does outsourced production have any additional raw material cost, or is the 200 Yuan outsourcing cost truly all-inclusive (covering materials, labor, and everything else)?

## Turn 9 - User Simulator

The 200 Yuan outsourcing cost is truly all-inclusive. It covers materials, labor, and everything else. There is no additional raw material cost for outsourced units.

## Turn 10 - Generic Agent

QUESTION: The inventory holding cost of 15 Yuan per unit is charged on inventory held at the end of a month. Does this apply to all units in ending inventory regardless of whether they were produced in-house or outsourced, or only to in-house produced units?

## Turn 10 - User Simulator

The inventory holding cost of 15 Yuan per unit applies to all units in ending inventory, regardless of whether they were produced in-house or outsourced.

## Turn 11 - Generic Agent

QUESTION: The sales price of 300 Yuan per unit is earned when a unit is sold to fulfill demand. If demand is back-ordered and fulfilled in a later month, is the 300 Yuan revenue recognized in the month the demand was originally placed, or in the month the unit is actually delivered?

## Turn 11 - User Simulator

The 300 Yuan revenue is recognized in the month the unit is actually delivered to fulfill the demand, not in the month the demand was originally placed.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint on the number of workers that can be hired or fired in a single month, or can you hire or fire any number of workers in any month without limit?

## Turn 12 - User Simulator

There is no limit on the number of workers that can be hired or fired in a single month. You can hire or fire any number of workers in any month, subject only to the respective costs of 5,000 Yuan per new worker hired and 8,000 Yuan per worker fired.

## Turn 13 - Generic Agent

QUESTION: The ending inventory at the end of June must be at least 10,000 units. Does this 10,000-unit requirement include any back-ordered units that are still unfulfilled at the end of June, or must all demand through June be fully satisfied (zero backorders) in addition to having 10,000 units of physical inventory?

## Turn 13 - User Simulator

All demand through June must be fully satisfied, meaning zero backorders at the end of June. In addition to that, the physical inventory at the end of June must be at least 10,000 units.

## Turn 14 - Generic Agent

QUESTION: Can the number of workers ever go to zero in any month, or is there a minimum workforce level that must be maintained at all times?

## Turn 14 - User Simulator

There is no minimum workforce level that must be maintained. The number of workers can go to zero in any month if desired, subject only to the hiring and firing costs.

## Turn 15 - Generic Agent

QUESTION: The 15,000 units of initial inventory at the start of January — are these units available to fulfill January's demand, or are they reserved and cannot be used until February?

## Turn 15 - User Simulator

The 15,000 units of initial inventory at the start of January are available to fulfill January's demand.

## Turn 16 - Generic Agent

QUESTION: When fulfilling demand in a given month, is there any priority or constraint on the order in which you use previous month's inventory, current in-house production, and outsourced units, or can you freely mix all three sources in any proportion to meet demand?

## Turn 16 - User Simulator

You can freely mix all three sources—previous month's inventory, current in-house production, and outsourced units—in any proportion to meet demand. There is no required priority or constraint on the order in which they are used.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint on the total production capacity per month beyond what the workforce (regular + overtime hours) allows, such as a maximum number of units that can be produced in-house per month regardless of labor hours available?

## Turn 17 - User Simulator

There is no additional constraint on total in-house production capacity beyond what the workforce's available labor hours (regular plus overtime) allow. The only limit on in-house production is the total labor hours available from the workforce in that month.

## Turn 18 - Generic Agent

QUESTION: The demand figures you provided (20,000, 40,000, 42,000, 35,000, 19,000, 18,500) — are these exact quantities that must be fulfilled, or are they forecasts that could be exceeded (i.e., is there any possibility of selling more than the forecasted demand in any month)?

## Turn 18 - User Simulator

These are exact quantities that must be fulfilled. There is no possibility of selling more than the forecasted demand in any month.

## Turn 19 - Generic Agent

QUESTION: When a unit is produced in-house, does it require 5 labor hours from the regular hours first, and only then from overtime hours, or can the 5 labor hours per unit be drawn from any combination of regular and overtime hours freely?

## Turn 19 - User Simulator

The 5 labor hours per unit can be drawn from any combination of regular and overtime hours freely. There is no requirement to use regular hours before overtime hours.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint that the number of workers must be a whole number (integer), or can you treat the workforce as a continuous variable (e.g., 1,000.5 workers)?

## Turn 20 - User Simulator

The number of workers must be a whole number (integer).

## Turn 21 - Generic Agent

QUESTION: Are the production quantities (in-house units produced and outsourced units per month) required to be whole numbers, or can they be treated as continuous variables?

## Turn 21 - User Simulator

The production quantities (in-house units produced and outsourced units per month) can be treated as continuous variables.

## Turn 22 - Generic Agent

QUESTION: The backorder cost of 35 Yuan per unit per month — is this charged on the total number of units that are back-ordered at the end of each month (i.e., the cumulative unfulfilled demand carried into the next month), or is it charged only on the new demand that becomes back-ordered in that specific month?

## Turn 22 - User Simulator

The backorder cost of 35 Yuan per unit per month is charged on the total number of units that are back-ordered at the end of each month (i.e., the cumulative unfulfilled demand carried into the next month).

## Turn 23 - Generic Agent

QUESTION: The inventory holding cost of 15 Yuan per unit is charged on ending inventory at the end of each month. Does this also apply to the end of June (i.e., is there a holding cost on the 10,000+ units of ending inventory at the end of June), or is the holding cost only charged for months January through May?

## Turn 23 - User Simulator

The inventory holding cost of 15 Yuan per unit applies to the ending inventory at the end of each month, including the end of June. So there is a holding cost on the 10,000+ units of ending inventory at the end of June.

## Turn 24 - Generic Agent

QUESTION: The regular wage of 4,800 Yuan per worker per month is paid regardless of utilization. Does this mean that even if a worker's available hours (160 regular + up to 20 overtime) are not fully used, the 4,800 Yuan is still paid, and overtime pay of 40 Yuan per hour is only paid for overtime hours actually worked?

## Turn 24 - User Simulator

Yes. The 4,800 Yuan regular wage is paid to each worker regardless of how many of their available hours are actually used. Overtime pay of 40 Yuan per hour is only paid for overtime hours actually worked.

## Turn 25 - Generic Agent

QUESTION: When you say the workforce can change month to month, is the workforce level at the start of each month determined by the previous month's workforce plus hires minus fires in that month, meaning the workforce for month t equals workforce at end of month t-1 plus hires in month t minus fires in month t?

## Turn 25 - User Simulator

Yes. The workforce level at the start of each month is determined by the previous month's workforce plus hires minus fires in that month. So the workforce for month t equals the workforce at the end of month t-1 plus hires in month t minus fires in month t.

## Turn 26 - Generic Agent

QUESTION: The workforce at the end of June — is there any requirement or cost associated with the workforce level at the end of June, or is the workforce level at the end of June simply whatever it is after June's hiring and firing decisions with no additional constraint or cost?

## Turn 26 - User Simulator

There is no additional requirement or cost associated with the workforce level at the end of June. The workforce level at the end of June is simply whatever it is after June's hiring and firing decisions, with no additional constraint or cost.

## Turn 27 - Generic Agent

QUESTION: The net profit objective — is it simply total revenue minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, firing), with no other revenue or cost components I haven't mentioned?

## Turn 27 - User Simulator

Yes. The net profit is simply total revenue (300 Yuan per unit sold) minus all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing. There are no other revenue or cost components.

## Turn 28 - Generic Agent

QUESTION: The 160 regular hours per worker per month — is this a fixed capacity that is always available (i.e., the worker is paid for 160 hours whether or not they are used), or is it a maximum that can be used, meaning the worker could work fewer than 160 regular hours in a month if production needs are lower?

## Turn 28 - User Simulator

The 160 regular hours per worker per month is a maximum that can be used. The worker is paid the fixed 4,800 Yuan regular wage regardless of how many of those 160 hours are actually used. If production needs are lower, the worker can work fewer than 160 regular hours in a month.

## Turn 29 - Generic Agent

QUESTION: The total labor hours available for in-house production in a given month is the sum of regular hours used (up to 160 per worker) plus overtime hours used (up to 20 per worker). Is the constraint that total in-house production × 5 hours ≤ (160 × workers + overtime hours used), where overtime hours used ≤ 20 × workers, or is there a separate constraint that regular hours used must be ≤ 160 × workers AND overtime hours used must be ≤ 20 × workers, with total in-house production × 5 ≤ regular hours used + overtime hours used?

## Turn 29 - User Simulator

The constraint is that total in-house production × 5 hours ≤ (160 × workers + overtime hours used), where overtime hours used ≤ 20 × workers. There is no separate constraint that regular hours used must be ≤ 160 × workers AND overtime hours used must be ≤ 20 × workers, with total in-house production × 5 ≤ regular hours used + overtime hours used.

## Turn 30 - Generic Agent

QUESTION: Since the regular wage is fixed at 4,800 Yuan per worker regardless of utilization, and overtime is only paid for hours actually worked, does this mean the model only needs to track total in-house production (which determines total labor hours needed) and total overtime hours used, without separately tracking regular vs. overtime hours used for each worker?

## Turn 30 - User Simulator

Yes. Since the regular wage is fixed at 4,800 Yuan per worker regardless of utilization, and overtime is only paid for hours actually worked, the model only needs to track total in-house production (which determines total labor hours needed) and total overtime hours used, without separately tracking regular vs. overtime hours used for each worker.