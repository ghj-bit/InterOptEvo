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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is 20 times the number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours allowed in a given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage of 30 Yuan per hour paid for 160 hours per worker "regardless of utilization," is the total regular labor cost each month simply 1,000 base workers times 160 hours times 30 Yuan (i.e., 4,800,000 Yuan per month for the initial workforce, scaled by the actual workforce size each month), meaning workers are paid their full 160 hours even if in-house production uses fewer hours?

## Turn 2 - User Simulator

Yes, that is correct. Each worker is paid for the full 160 regular hours each month regardless of how many hours are actually used for production. The total regular labor cost for a month is the number of workers employed that month multiplied by 160 hours multiplied by 30 Yuan per hour.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the total units available to meet that month's demand (plus any backorders from prior months) equal the ending inventory from the prior month plus current in-house production plus current outsourcing, and any shortfall becomes a new backorder carried to the next month?

## Turn 3 - User Simulator

Yes, that is correct. In each month, the total units available to meet that month's demand plus any backorders from prior months equal the ending inventory from the prior month plus current in-house production plus current outsourced units. If the available units are less than the total orders to fulfill, the shortfall becomes a new backorder carried to the next month.

## Turn 4 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire workers in any month from January through June, or are hiring and firing decisions only allowed at the start of January (i.e., the workforce is fixed at 1,000 for all six months)?

## Turn 4 - User Simulator

Hiring and firing decisions can be made in any month from January through June. The workforce is not fixed at 1,000 for all six months; it can change month to month based on your plan.

## Turn 5 - Generic Agent

QUESTION: When workers are hired or fired in a given month, do they count toward that month's workforce for production purposes (i.e., a worker hired in March is available to work in March), or do they only become available starting the following month?

## Turn 5 - User Simulator

A worker hired in a given month is available to work in that same month. Similarly, a worker fired in a given month is no longer available to work in that month.

## Turn 6 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit, is this charged on the number of units that are backordered at the end of each month (i.e., the unfulfilled demand carried into the next month), and is it charged every month the units remain backordered until they are finally fulfilled?

## Turn 6 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is charged on the number of units that are backordered at the end of each month. It is charged every month the units remain backordered until they are finally fulfilled.

## Turn 7 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is this charged on the ending inventory at the end of each month (including June), and does it apply to all units in inventory regardless of whether they were produced in-house or outsourced?

## Turn 7 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory at the end of each month, including June. It applies to all units in inventory regardless of whether they were produced in-house or outsourced.

## Turn 8 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit, is this the only cost associated with in-house production (in addition to labor), or are there other in-house production costs I should account for?

## Turn 8 - User Simulator

The raw material cost of 90 Yuan per unit is the only additional cost associated with in-house production beyond labor. There are no other in-house production costs to account for.

## Turn 9 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit, is revenue recognized only when a unit is actually sold (i.e., when demand is fulfilled, including backordered units that are fulfilled in a later month), or is revenue recognized based on the original demand month regardless of when the unit is actually delivered?

## Turn 9 - User Simulator

Revenue is recognized only when a unit is actually sold, meaning when demand is fulfilled, including backordered units that are fulfilled in a later month.

## Turn 10 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a given month, or can you outsource as many units as needed?

## Turn 10 - User Simulator

There is no upper limit on the number of units that can be outsourced in a given month. You can outsource as many units as needed.

## Turn 11 - Generic Agent

QUESTION: Is there any upper limit on the number of workers that can be hired in a single month, or can you hire an unlimited number of new workers in any given month?

## Turn 11 - User Simulator

There is no upper limit on the number of workers that can be hired in a single month. You can hire an unlimited number of new workers in any given month.

## Turn 12 - Generic Agent

QUESTION: Can the workforce drop below zero workers (i.e., can you fire more workers than you currently have), or is the workforce constrained to be at least zero in every month?

## Turn 12 - User Simulator

The workforce is constrained to be at least zero in every month. You cannot fire more workers than you currently have.

## Turn 13 - Generic Agent

QUESTION: Regarding the minimum ending inventory of 10,000 units at the end of June, does this 10,000 units need to be in physical inventory (i.e., not backordered), meaning that all demand through June must be fully satisfied and there must be at least 10,000 units left over in inventory?

## Turn 13 - User Simulator

Yes, the 10,000 units must be in physical inventory at the end of June. All demand through June must be fully satisfied (no backorders remaining), and there must be at least 10,000 units left over in inventory.

## Turn 14 - Generic Agent

QUESTION: Regarding the backorder cost, is it charged only on the net backorder at the end of each month (i.e., the cumulative unfulfilled demand minus any units that were fulfilled from that backorder in the same month), or is it charged on the total original demand that was not met in its original month regardless of when it gets fulfilled?

## Turn 14 - User Simulator

The backorder cost is charged on the net backorder at the end of each month. That is the cumulative unfulfilled demand minus any units that were fulfilled from that backorder in the same month.

## Turn 15 - Generic Agent

QUESTION: Regarding the in-house production capacity, is the only constraint on in-house production the available labor hours (regular 160 hours plus overtime up to 20 hours per worker), or are there other capacity limits such as a maximum number of units that can be produced in-house per month regardless of labor availability?

## Turn 15 - User Simulator

The only constraint on in-house production is the available labor hours (regular 160 hours plus overtime up to 20 hours per worker). There are no other capacity limits on in-house production.

## Turn 16 - Generic Agent

QUESTION: Regarding the workforce, can you both hire and fire workers in the same month (i.e., net workforce change could involve simultaneous hiring and firing), or is the workforce change in each month simply a net adjustment where you either hire or fire but not both?

## Turn 16 - User Simulator

The workforce change in each month is simply a net adjustment. You either hire or fire, but not both in the same month.

## Turn 17 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January, is there any holding cost charged on this initial inventory for January (i.e., is the 15,000 units considered as inventory held at the end of December and thus subject to a holding cost in January), or is the holding cost only charged on the ending inventory of each month from January through June?

## Turn 17 - User Simulator

The holding cost is only charged on the ending inventory of each month from January through June. The initial 15,000 units at the start of January do not incur a holding cost for January.

## Turn 18 - Generic Agent

QUESTION: Regarding the net profit objective, is the total net profit calculated as total revenue (300 Yuan per unit sold) minus all costs (raw materials, outsourcing, regular labor, overtime labor, inventory holding, backorder, hiring, and firing), with no other revenue or cost items to consider?

## Turn 18 - User Simulator

Yes, the total net profit is calculated as total revenue (300 Yuan per unit sold) minus all costs: raw materials, outsourcing, regular labor, overtime labor, inventory holding, backorder, hiring, and firing. There are no other revenue or cost items to consider.

## Turn 19 - Generic Agent

QUESTION: Regarding the backorder at the end of June, since all demand through June must be fully satisfied and there must be at least 10,000 units in physical inventory, does this mean the backorder at the end of June must be exactly zero (no backorders remaining)?

## Turn 19 - User Simulator

Yes, the backorder at the end of June must be exactly zero. No backorders can remain after June; all customer orders must be fulfilled within the six months.

## Turn 20 - Generic Agent

QUESTION: Regarding the workforce in January, the initial workforce is 1,000 at the start of January. If you hire or fire workers in January, does the 1,000 represent the workforce before any January hiring/firing decision, meaning the January workforce equals 1,000 plus January hires minus January fires?

## Turn 20 - User Simulator

Yes, the 1,000 represents the workforce before any January hiring or firing decision. The January workforce equals 1,000 plus January hires minus January fires.

## Turn 21 - Generic Agent

QUESTION: Regarding the overtime hours, is the overtime used in a month simply the total labor hours needed for in-house production minus the regular hours available (160 times the workforce), capped at 20 times the workforce, or can you choose to use fewer overtime hours than the maximum even if you have the capacity?

## Turn 21 - User Simulator

Yes, overtime used in a month is the total labor hours needed for in-house production minus the regular hours available (160 times the workforce), capped at 20 times the workforce. You can also choose to use fewer overtime hours than the maximum even if you have the capacity.

## Turn 22 - Generic Agent

QUESTION: Regarding the in-house production, can you choose to produce fewer in-house units than what the available labor hours (regular plus overtime) would allow, meaning in-house production is a decision variable that can be any non-negative value up to the labor-hour capacity?

## Turn 22 - User Simulator

Yes, in-house production is a decision variable that can be any non-negative value up to the labor-hour capacity (regular plus overtime hours available).

## Turn 23 - Generic Agent

QUESTION: Regarding the inventory balance, if in a given month the available units (prior ending inventory plus in-house production plus outsourcing) exceed the total orders to fulfill (current demand plus prior backorders), does the excess automatically become the ending inventory for that month, or can you choose to discard or not carry over some of the excess?

## Turn 23 - User Simulator

The excess automatically becomes the ending inventory for that month. You cannot choose to discard or not carry over some of the excess.

## Turn 24 - Generic Agent

QUESTION: Regarding the backorder, if in a given month the available units are less than the total orders to fulfill, is the backorder at the end of that month simply the difference (total orders minus available units), and does this backorder carry forward to the next month to be added to the next month's demand?

## Turn 24 - User Simulator

Yes, if in a given month the available units are less than the total orders to fulfill, the backorder at the end of that month is simply the difference (total orders minus available units). This backorder carries forward to the next month to be added to the next month's demand.

## Turn 25 - Generic Agent

QUESTION: Regarding the inventory and backorder, can both ending inventory and backorder be positive in the same month, or is it always the case that one of them is zero (i.e., you either have leftover inventory or unfulfilled demand, but not both)?

## Turn 25 - User Simulator

It is always the case that one of them is zero. You either have leftover inventory or unfulfilled demand in a given month, but not both.

## Turn 26 - Generic Agent

QUESTION: Regarding the workforce, is there a minimum number of workers that must be employed in any month (e.g., you cannot reduce the workforce below a certain level), or can the workforce go down to zero if that is optimal?

## Turn 26 - User Simulator

There is no minimum number of workers that must be employed in any month. The workforce can go down to zero if that is optimal.

## Turn 27 - Generic Agent

QUESTION: Regarding the outsourcing, is there any constraint on outsourcing related to the workforce or labor hours, or is outsourcing completely independent of the workforce (i.e., you can outsource any number of units regardless of how many workers you have)?

## Turn 27 - User Simulator

Outsourcing is completely independent of the workforce. You can outsource any number of units regardless of how many workers you have.

## Turn 28 - Generic Agent

QUESTION: Regarding the regular labor cost, since each worker is paid for 160 hours regardless of utilization, if the workforce in a month is, say, 500 workers, the regular labor cost is 500 times 160 times 30 Yuan, even if the in-house production only requires, say, 10,000 labor hours (which is less than 500 times 160 = 80,000 hours). Is that correct?

## Turn 28 - User Simulator

Yes, that is correct. If the workforce in a month is 500 workers, the regular labor cost is 500 times 160 times 30 Yuan, even if the in-house production only requires 10,000 labor hours.

## Turn 29 - Generic Agent

QUESTION: Regarding the overtime, if the in-house production in a month requires more than 160 times the workforce hours, the overtime used is the excess hours, and the overtime cost is that excess times 40 Yuan per hour. But if the in-house production requires fewer than 160 times the workforce hours, there is no overtime and no overtime cost. Is that correct?

## Turn 29 - User Simulator

Yes, that is correct. If the in-house production in a month requires more than 160 times the workforce hours, the overtime used is the excess hours (capped at 20 times the workforce), and the overtime cost is that excess times 40 Yuan per hour. If the in-house production requires fewer than 160 times the workforce hours, there is no overtime and no overtime cost.

## Turn 30 - Generic Agent

QUESTION: Regarding the in-house production capacity constraint, the maximum in-house production in a month is limited by (160 + 20) times the workforce divided by 5 (since each unit requires 5 labor hours). So the maximum in-house production is 180 times the workforce divided by 5, which equals 36 times the workforce. Is that correct?

## Turn 30 - User Simulator

Yes, that is correct. The maximum in-house production in a month is 36 times the workforce.