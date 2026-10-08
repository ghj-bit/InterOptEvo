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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can the number of workers change from month to month through hiring and firing, and if so, is the workforce level for a month determined at the start of that month (so it applies to that month's production and overtime)?

## Turn 2 - User Simulator

Yes, the number of workers can change from month to month through hiring and firing. The workforce level for a given month is determined at the start of that month and applies to that month's production and overtime capacity.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using previous-month inventory, current in-house production, and outsourced units, is there any limit on how much can be outsourced in a month, or can any number of units be outsourced as needed?

## Turn 3 - User Simulator

There is no limit on how much can be outsourced in a month. Any number of units can be outsourced as needed.

## Turn 4 - Generic Agent

QUESTION: For the regular wage, you said it is paid regardless of utilization — does that mean the company pays 30 Yuan/hour × 160 hours for every worker employed in a month even if the worker's hours are not fully used for production?

## Turn 4 - User Simulator

Yes, the company pays 30 Yuan/hour × 160 hours for every worker employed in a month, even if the worker's hours are not fully used for production.

## Turn 5 - Generic Agent

QUESTION: For backorders, when unfulfilled demand is carried over to the next month, is the backorder cost of 35 Yuan per unit charged once per month that a unit remains back-ordered (i.e., if a unit is back-ordered for two months, it incurs 35 Yuan in each of those months)?

## Turn 5 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is charged once per month that a unit remains back-ordered. If a unit is back-ordered for two months, it incurs 35 Yuan in each of those months.

## Turn 6 - Generic Agent

QUESTION: For the ending inventory at the end of June, does the 10,000-unit minimum apply to the physical inventory on hand (excluding any backorders), and can there be backorders remaining at the end of June, or must all demand be fully satisfied by the end of June?

## Turn 6 - User Simulator

The 10,000-unit minimum applies to the physical inventory on hand at the end of June. Additionally, all backorders must be cleared by the end of June; no outstanding customer orders can remain after June. Everything must be fulfilled within the six months.

## Turn 7 - Generic Agent

QUESTION: For the sales price of 300 Yuan per unit sold — is this revenue recognized when the unit is actually delivered to the customer (i.e., when the demand is fulfilled, possibly in a later month if back-ordered), or is it recognized in the month the demand originally occurred?

## Turn 7 - User Simulator

The sales price of 300 Yuan per unit is recognized when the unit is actually delivered to the customer, i.e., when the demand is fulfilled, possibly in a later month if back-ordered.

## Turn 8 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit — does this apply only to units produced in-house, and does it NOT apply to outsourced units (since outsourcing is described as all-inclusive at 200 Yuan per finished table)?

## Turn 8 - User Simulator

Yes, the raw material cost of 90 Yuan per unit applies only to units produced in-house. It does not apply to outsourced units, since the outsourcing cost of 200 Yuan per finished table is all-inclusive.

## Turn 9 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit — is this charged on the ending inventory of each month (i.e., the units physically on hand at the end of that month), and does it apply to all six months including June?

## Turn 9 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, meaning the units physically on hand at the end of that month. It applies to all six months, including June.

## Turn 10 - Generic Agent

QUESTION: For the workforce, is there any upper or lower bound on the number of workers the company can have in any month (for example, a maximum workforce size or a minimum of zero), or can the workforce be any non-negative integer?

## Turn 10 - User Simulator

There is no upper or lower bound specified beyond the workforce being a non-negative integer. The company can have any non-negative integer number of workers in any month.

## Turn 11 - Generic Agent

QUESTION: For in-house production, is the number of units produced in a month required to be an integer, or can it be a continuous (fractional) value?

## Turn 11 - User Simulator

The number of units produced in a month must be an integer.

## Turn 12 - Generic Agent

QUESTION: For the outsourced units, must the number of units outsourced in a month also be an integer, or can it be a continuous (fractional) value?

## Turn 12 - User Simulator

The number of units outsourced in a month must also be an integer.

## Turn 13 - Generic Agent

QUESTION: For the backorder quantity carried from one month to the next, must it be an integer, or can it be a continuous (fractional) value?

## Turn 13 - User Simulator

The backorder quantity carried from one month to the next must be an integer.

## Turn 14 - Generic Agent

QUESTION: For the inventory on hand at the end of each month, must it be an integer, or can it be a continuous (fractional) value?

## Turn 14 - User Simulator

The inventory on hand at the end of each month must be an integer.

## Turn 15 - Generic Agent

QUESTION: For the overtime hours used in a month, must the total overtime hours be an integer, or can they be a continuous (fractional) value?

## Turn 15 - User Simulator

The total overtime hours used in a month can be a continuous (fractional) value.

## Turn 16 - Generic Agent

QUESTION: For the regular hours used in a month, must the total regular hours used be an integer, or can they be a continuous (fractional) value?

## Turn 16 - User Simulator

The total regular hours used in a month can be a continuous (fractional) value.

## Turn 17 - Generic Agent

QUESTION: For the workforce, is the number of workers hired or fired in a month required to be an integer, or can it be a continuous (fractional) value?

## Turn 17 - User Simulator

The number of workers hired or fired in a month must be an integer.

## Turn 18 - Generic Agent

QUESTION: For the demand fulfillment in a given month, can the company choose to fulfill only part of the current month's demand and back-order the rest, or must all of the current month's demand be fulfilled in that same month?

## Turn 18 - User Simulator

The company can choose to fulfill only part of the current month's demand and back-order the rest.

## Turn 19 - Generic Agent

QUESTION: For the initial inventory of 15,000 units at the start of January, is this available to fulfill January's demand (i.e., it is part of the supply for January), or is it only available starting from February?

## Turn 19 - User Simulator

The initial inventory of 15,000 units at the start of January is available to fulfill January's demand. It is part of the supply for January.

## Turn 20 - Generic Agent

QUESTION: For the initial workforce of 1,000 employees at the start of January, is this the workforce level for January (i.e., they are available for January's production), or is it only the starting point before any January hiring/firing decisions?

## Turn 20 - User Simulator

The initial workforce of 1,000 employees at the start of January is the starting point before any January hiring/firing decisions. The workforce level for January is determined after any hiring or firing decisions made at the start of January.

## Turn 21 - Generic Agent

QUESTION: For the hiring and firing decisions, are they made at the start of each month (including January), so that the January workforce can differ from the initial 1,000?

## Turn 21 - User Simulator

Yes, hiring and firing decisions are made at the start of each month, including January. The January workforce can differ from the initial 1,000.

## Turn 22 - Generic Agent

QUESTION: For the workforce balance, is the workforce at the start of a month equal to the workforce at the end of the previous month plus hires minus fires, with no other way for the workforce to change?

## Turn 22 - User Simulator

Yes, the workforce at the start of a month is equal to the workforce at the end of the previous month plus hires minus fires, with no other way for the workforce to change.

## Turn 23 - Generic Agent

QUESTION: For the production capacity, is the total in-house production in a month limited by the total available labor hours (regular hours plus overtime hours) divided by 5 hours per unit, or is there any other constraint on in-house production?

## Turn 23 - User Simulator

The total in-house production in a month is limited by the total available labor hours (regular hours plus overtime hours) divided by 5 hours per unit. There are no other constraints on in-house production.

## Turn 24 - Generic Agent

QUESTION: For the inventory balance in a given month, is the ending inventory equal to the beginning inventory plus in-house production plus outsourced units minus the units delivered to fulfill demand in that month, with no other sources or uses of inventory?

## Turn 24 - User Simulator

Yes, the ending inventory in a given month is equal to the beginning inventory plus in-house production plus outsourced units minus the units delivered to fulfill demand in that month, with no other sources or uses of inventory.

## Turn 25 - Generic Agent

QUESTION: For the demand fulfillment, is the total units delivered in a month equal to the current month's demand minus the new backorders created in that month plus the backorders from the previous month that are fulfilled in that month, or is there a different way to track fulfillment?

## Turn 25 - User Simulator

The total units delivered in a month is equal to the current month's demand minus the new backorders created in that month plus the backorders from the previous month that are fulfilled in that month.

## Turn 26 - Generic Agent

QUESTION: For the backorder balance, is the backorder at the end of a month equal to the backorder at the beginning of the month plus the current month's demand minus the total units delivered in that month, with the constraint that this must be non-negative?

## Turn 26 - User Simulator

Yes, the backorder at the end of a month is equal to the backorder at the beginning of the month plus the current month's demand minus the total units delivered in that month, with the constraint that this must be non-negative.

## Turn 27 - Generic Agent

QUESTION: For the net profit objective, is it calculated as total revenue from all units delivered over the six months minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost components?

## Turn 27 - User Simulator

Yes, the net profit is calculated as total revenue from all units delivered over the six months minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost components.

## Turn 28 - Generic Agent

QUESTION: For the regular wage cost, is it simply 30 Yuan/hour × 160 hours × (number of workers in that month), regardless of how many regular hours are actually used for production?

## Turn 28 - User Simulator

Yes, the regular wage cost is simply 30 Yuan/hour × 160 hours × (number of workers in that month), regardless of how many regular hours are actually used for production.

## Turn 29 - Generic Agent

QUESTION: For the overtime wage cost, is it simply 40 Yuan/hour × (total overtime hours used in that month), where the total overtime hours used is a decision variable that can range from 0 to 20 times the number of workers in that month?

## Turn 29 - User Simulator

Yes, the overtime wage cost is simply 40 Yuan/hour × (total overtime hours used in that month), where the total overtime hours used is a decision variable that can range from 0 to 20 times the number of workers in that month.

## Turn 30 - Generic Agent

QUESTION: For the in-house production constraint, is the total labor hours used for in-house production in a month (5 hours per unit × in-house units) equal to the regular hours used plus the overtime hours used, where regular hours used cannot exceed 160 times the number of workers and overtime hours used cannot exceed 20 times the number of workers?

## Turn 30 - User Simulator

Yes, the total labor hours used for in-house production in a month (5 hours per unit × in-house units) is equal to the regular hours used plus the overtime hours used, where regular hours used cannot exceed 160 times the number of workers and overtime hours used cannot exceed 20 times the number of workers.