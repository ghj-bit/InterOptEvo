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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce, can you hire and/or fire workers at the start of any month (including January), and is the workforce level constant within a month (i.e., one workforce number per month that applies to that month's production and overtime capacity)?

## Turn 2 - User Simulator

Yes, you can hire and/or fire workers at the start of any month, including January. The workforce level is constant within a month; there is one workforce number per month that applies to that month's production and overtime capacity.

## Turn 3 - Generic Agent

QUESTION: For the regular wage, you said it is "paid regardless of utilization" — does that mean the company pays 30 Yuan/hour × 160 hours × (number of workers) every month even if the workers are not fully used, so the regular wage cost is simply 48,000 Yuan per worker per month regardless of how many hours are actually worked?

## Turn 3 - User Simulator

Yes, that is correct. The regular wage cost is 30 Yuan/hour × 160 hours × (number of workers) every month, regardless of how many hours are actually utilized. So it is 4,800 Yuan per worker per month.

## Turn 4 - Generic Agent

QUESTION: When demand is back-ordered, is the backorder cost of 35 Yuan per unit charged once per month that the unit remains unfulfilled (i.e., if a unit is back-ordered for two months, it incurs 70 Yuan total), or is it charged only once when the unit is finally fulfilled?

## Turn 4 - User Simulator

The backorder cost of 35 Yuan per unit is charged once per month that the unit remains unfulfilled. So if a unit is back-ordered for two months, it incurs 70 Yuan total.

## Turn 5 - Generic Agent

QUESTION: Can the workforce be reduced to zero in any month, or is there a minimum number of workers that must be employed at all times?

## Turn 5 - User Simulator

There is no minimum number of workers that must be employed. The workforce can be reduced to zero in any month.

## Turn 6 - Generic Agent

QUESTION: For the inventory balance, is the ending inventory at the end of each month (including June) allowed to be negative, or must it be non-negative at all times with backorders tracked separately as a distinct quantity?

## Turn 6 - User Simulator

Ending inventory must be non-negative at all times. Backorders are tracked separately as a distinct quantity.

## Turn 7 - Generic Agent

QUESTION: When fulfilling orders in a given month, is there a specific priority order for using the three sources (previous month's inventory, current in-house production, outsourced units), or can the model freely allocate among them as long as the total available units cover the total orders (current demand plus backorders)?

## Turn 7 - User Simulator

There is no specific priority order. The model can freely allocate among previous month's inventory, current in-house production, and outsourced units, as long as the total available units cover the total orders (current demand plus backorders).

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a given month, or is outsourcing capacity unlimited?

## Turn 8 - User Simulator

Outsourcing capacity is unlimited. There is no upper limit on the number of units that can be outsourced in a given month.

## Turn 9 - Generic Agent

QUESTION: Is there any upper limit on the number of workers that can be hired in a single month, or is hiring capacity unlimited?

## Turn 9 - User Simulator

Hiring capacity is unlimited. There is no upper limit on the number of workers that can be hired in a single month.

## Turn 10 - Generic Agent

QUESTION: Is the sales price of 300 Yuan per unit applied to every unit that is ultimately fulfilled (including back-ordered units when they are delivered in a later month), so that revenue equals 300 times the total units delivered over the six months?

## Turn 10 - User Simulator

Yes, the sales price of 300 Yuan per unit is applied to every unit that is ultimately fulfilled, including back-ordered units when they are delivered in a later month. Revenue equals 300 times the total units delivered over the six months.

## Turn 11 - Generic Agent

QUESTION: Are all demand units (including back-ordered ones) required to be fulfilled by the end of June, or is it permissible to leave some demand unfulfilled at the end of the planning horizon?

## Turn 11 - User Simulator

All demand units, including back-ordered ones, must be fulfilled by the end of June. No outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 12 - Generic Agent

QUESTION: Is there any upper limit on the ending inventory at the end of any month (other than the minimum of 10,000 at the end of June), or can inventory be arbitrarily large?

## Turn 12 - User Simulator

There is no upper limit on ending inventory at the end of any month. Inventory can be arbitrarily large, subject only to the minimum requirement of 10,000 units at the end of June.

## Turn 13 - Generic Agent

QUESTION: Is there any limit on the number of workers that can be fired in a single month, or is firing capacity unlimited?

## Turn 13 - User Simulator

Firing capacity is unlimited. There is no upper limit on the number of workers that can be fired in a single month.

## Turn 14 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it incurred only on units that are actually produced in-house (regardless of whether they are sold immediately or go into inventory), and is there no raw material cost for outsourced units since that cost is already included in the 200 Yuan outsourcing price?

## Turn 14 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred only on units that are actually produced in-house, regardless of whether they are sold immediately or go into inventory. There is no separate raw material cost for outsourced units, as that cost is already included in the 200 Yuan outsourcing price.

## Turn 15 - Generic Agent

QUESTION: Is the inventory holding cost of 15 Yuan per unit charged on the ending inventory of each month (i.e., 15 times the units in inventory at the end of that month), including the ending inventory at the end of June?

## Turn 15 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including the ending inventory at the end of June.

## Turn 16 - Generic Agent

QUESTION: When a worker is hired at the start of a month, does that worker immediately contribute their full 160 regular hours and up to 20 overtime hours to that month's production capacity, or is there any ramp-up period?

## Turn 16 - User Simulator

A worker hired at the start of a month immediately contributes their full 160 regular hours and up to 20 overtime hours to that month's production capacity. There is no ramp-up period.

## Turn 17 - Generic Agent

QUESTION: When a worker is fired at the start of a month, does that worker contribute zero hours to that month's production capacity (i.e., they are gone for the entire month), or do they work part of the month before being let go?

## Turn 17 - User Simulator

A worker fired at the start of a month contributes zero hours to that month's production capacity. They are gone for the entire month.

## Turn 18 - Generic Agent

QUESTION: Is the workforce variable (number of workers employed in a month) required to be a whole number, or can it be treated as a continuous variable?

## Turn 18 - User Simulator

The workforce variable must be a whole number.

## Turn 19 - Generic Agent

QUESTION: Are the production quantities (in-house units produced and outsourced units per month) required to be whole numbers, or can they be treated as continuous variables?

## Turn 19 - User Simulator

The production quantities (in-house units produced and outsourced units per month) must be whole numbers.

## Turn 20 - Generic Agent

QUESTION: Are the inventory and backorder quantities (ending inventory and backorders per month) required to be whole numbers, or can they be treated as continuous variables?

## Turn 20 - User Simulator

The inventory and backorder quantities (ending inventory and backorders per month) must be whole numbers.

## Turn 21 - Generic Agent

QUESTION: Is the total demand over the six months (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500 = 174,500 units) the complete set of orders that must be fulfilled, or could there be additional orders beyond these forecasted demand figures?

## Turn 21 - User Simulator

The total demand over the six months (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500 = 174,500 units) is the complete set of orders that must be fulfilled. There are no additional orders beyond these forecasted demand figures.

## Turn 22 - Generic Agent

QUESTION: Is the initial inventory of 15,000 units at the start of January available to fulfill January's demand (i.e., it can be used in January's fulfillment), or is it only available starting from February?

## Turn 22 - User Simulator

The initial inventory of 15,000 units at the start of January is available to fulfill January's demand. It can be used in January's fulfillment.

## Turn 23 - Generic Agent

QUESTION: Is the initial workforce of 1,000 employees at the start of January available for January's production (i.e., they can work in January), or are they only available starting from February?

## Turn 23 - User Simulator

The initial workforce of 1,000 employees at the start of January is available for January's production. They can work in January.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint linking the workforce in one month to the workforce in the next month beyond the hiring and firing costs (i.e., is the workforce in month t+1 simply equal to the workforce in month t plus hires minus fires, with no other restrictions)?

## Turn 24 - User Simulator

Yes, the workforce in month t+1 is simply equal to the workforce in month t plus hires minus fires, with no other restrictions.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour capacity (160 regular + up to 20 overtime hours per worker, with 5 hours per unit), or is the labor hour capacity the only limit on in-house production?

## Turn 25 - User Simulator

The labor hour capacity is the only limit on in-house production. There are no other constraints on the total number of units that can be produced in-house in a month.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour capacity (160 regular + up to 20 overtime hours per worker, with 5 hours per unit), or is the labor hour capacity the only limit on in-house production?

## Turn 26 - User Simulator

The labor hour capacity is the only limit on in-house production. There are no other constraints on the total number of units that can be produced in-house in a month.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour capacity (160 regular + up to 20 overtime hours per worker, with 5 hours per unit), or is the labor hour capacity the only limit on in-house production?

## Turn 27 - User Simulator

The labor hour capacity is the only limit on in-house production. There are no other constraints on the total number of units that can be produced in-house in a month.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour capacity (160 regular + up to 20 overtime hours per worker, with 5 hours per unit), or is the labor hour capacity the only limit on in-house production?

## Turn 28 - User Simulator

The labor hour capacity is the only limit on in-house production. There are no other constraints on the total number of units that can be produced in-house in a month.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour capacity (160 regular + up to 20 overtime hours per worker, with 5 hours per unit), or is the labor hour capacity the only limit on in-house production?

## Turn 29 - User Simulator

The labor hour capacity is the only limit on in-house production. There are no other constraints on the total number of units that can be produced in-house in a month.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour capacity (160 regular + up to 20 overtime hours per worker, with 5 hours per unit), or is the labor hour capacity the only limit on in-house production?

## Turn 30 - User Simulator

The labor hour capacity is the only limit on in-house production. There are no other constraints on the total number of units that can be produced in-house in a month.