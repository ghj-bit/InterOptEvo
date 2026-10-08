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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a given month (so total overtime capacity = 20 × number of workers that month), or that the whole workforce combined is capped at a fixed 20 hours of overtime per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime capacity for the month is 20 hours multiplied by the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage of 30 Yuan/hour for the 160 regular hours per worker, is this cost incurred for every worker employed in a month regardless of how many hours they actually work (i.e., a fixed monthly cost of 1,000 Yuan per worker), or is it paid only for the regular hours actually used in production?

## Turn 2 - User Simulator

It is a fixed monthly cost. Each worker is paid for the 160 regular hours regardless of how many hours they actually work in production.

## Turn 3 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) in any month from January through June, or is the workforce fixed at 1,000 for the entire six-month period?

## Turn 3 - User Simulator

The workforce can be changed in any month from January through June. We can hire or fire workers as needed, subject to the hiring cost of 5,000 Yuan per new worker and the firing cost of 8,000 Yuan per worker.

## Turn 4 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month, the demand for that month must be fully satisfied from the combination of beginning inventory (carried over from the prior month), in-house production in that month, and outsourced units in that month, with any shortfall becoming a backorder carried to the next month?

## Turn 4 - User Simulator

Yes, that is correct. In each month, the demand for that month (including any backorders carried over from the prior month) is satisfied from the combination of beginning inventory, current in-house production, and outsourced units. Any shortfall becomes a backorder carried to the next month.

## Turn 5 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit for unfulfilled demand carried over to the next month, is this cost charged once per unit per month it remains backordered (i.e., if a unit is backordered for two months, it incurs 70 Yuan total), or is it a one-time charge of 35 Yuan per unit regardless of how many months it stays backordered?

## Turn 5 - User Simulator

The backorder cost is charged once per unit per month it remains backordered. So if a unit is backordered for two months, it incurs 70 Yuan total.

## Turn 6 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit for inventory held at the end of a month, is this charged on the ending inventory of each month (i.e., the units remaining after satisfying that month's demand), and does it apply to the ending inventory at the end of June as well?

## Turn 6 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including the ending inventory at the end of June.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum limit on the number of workers that can be employed in any given month, or can the workforce grow without bound as long as the hiring cost is paid?

## Turn 7 - User Simulator

There is no maximum limit on the number of workers that can be employed in any given month. The workforce can grow as long as the hiring cost is paid.

## Turn 8 - Generic Agent

QUESTION: Is there a minimum number of workers that must be maintained in any given month, or can the workforce be reduced to zero if that is optimal?

## Turn 8 - User Simulator

There is no minimum number of workers that must be maintained. The workforce can be reduced to zero if that is optimal.

## Turn 9 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold, is this revenue recognized only for units that are actually delivered to customers (i.e., demand satisfied in the month it was due), or is it recognized for all units that eventually get delivered, including those that were backordered and delivered in a later month?

## Turn 9 - User Simulator

The sales price of 300 Yuan per unit is recognized for all units that eventually get delivered, including those that were backordered and delivered in a later month.

## Turn 10 - Generic Agent

QUESTION: Is there a limit on how many months a backorder can be carried before it must be fulfilled, or can backorders be carried indefinitely as long as they are eventually satisfied within the six-month planning horizon?

## Turn 10 - User Simulator

Backorders can be carried for as many months as needed, as long as they are eventually satisfied within the six-month planning horizon. All backorders must be cleared by the end of June.

## Turn 11 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit applicable only to in-house production, is this cost incurred for every in-house unit produced in a month, regardless of whether that unit is used to satisfy current demand, backorders, or added to ending inventory?

## Turn 11 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred for every in-house unit produced in a month, regardless of whether that unit is used to satisfy current demand, backorders, or added to ending inventory.

## Turn 12 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit for finished tables, is this cost incurred for every outsourced unit ordered in a month, regardless of whether that unit is used to satisfy current demand, backorders, or added to ending inventory?

## Turn 12 - User Simulator

Yes, the outsourcing cost of 200 Yuan per unit is incurred for every outsourced unit ordered in a month, regardless of whether that unit is used to satisfy current demand, backorders, or added to ending inventory.

## Turn 13 - Generic Agent

QUESTION: When backorders from a prior month are carried into the current month, are they added to the current month's demand (so the total to be satisfied in the current month is current demand plus prior backorders), or are they tracked separately and can be satisfied independently of the current month's demand?

## Turn 13 - User Simulator

They are added to the current month's demand. The total to be satisfied in the current month is the current month's demand plus any prior backorders carried over.

## Turn 14 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June, does this 10,000 units need to be in physical inventory (i.e., actual units on hand), or can it include units that are in the process of being produced or outsourced in June but not yet delivered?

## Turn 14 - User Simulator

The 10,000 units must be in physical inventory at the end of June. This means actual units on hand after satisfying all demand and backorders for June.

## Turn 15 - Generic Agent

QUESTION: Regarding the workforce transition, if we start January with 1,000 workers and decide to have, say, 1,200 workers in January, does that mean we hire 200 workers at the start of January (incurring 200 × 5,000 Yuan in hiring cost), and the 1,200 workers are all available for production during January?

## Turn 15 - User Simulator

Yes, that is correct. If we start January with 1,000 workers and decide to have 1,200 workers in January, we hire 200 workers at the start of January, incurring 200 × 5,000 Yuan in hiring cost, and all 1,200 workers are available for production during January.

## Turn 16 - Generic Agent

QUESTION: If we have 1,200 workers in January and decide to have 1,000 workers in February, does that mean we fire 200 workers at the start of February (incurring 200 × 8,000 Yuan in firing cost), and the 1,000 workers are all available for production during February?

## Turn 16 - User Simulator

Yes, that is correct. If we have 1,200 workers in January and decide to have 1,000 workers in February, we fire 200 workers at the start of February, incurring 200 × 8,000 Yuan in firing cost, and the 1,000 workers are all available for production during February.

## Turn 17 - Generic Agent

QUESTION: Can we both hire and fire workers in the same month, or is the workforce change in each month either purely hiring or purely firing (i.e., the workforce can only go up or down, not both, in a single month)?

## Turn 17 - User Simulator

The workforce change in each month is either purely hiring or purely firing. The workforce can only go up or down in a single month, not both.

## Turn 18 - Generic Agent

QUESTION: Regarding the in-house production capacity, is the maximum in-house production in a month limited by the total available labor hours (160 regular hours + up to 20 overtime hours per worker, divided by 5 hours per unit), or is there any other constraint on in-house production capacity?

## Turn 18 - User Simulator

The maximum in-house production in a month is limited by the total available labor hours: (160 regular hours + up to 20 overtime hours) per worker, divided by 5 hours per unit. There are no other constraints on in-house production capacity.

## Turn 19 - Generic Agent

QUESTION: Regarding the outsourcing, is there any limit on the number of units that can be outsourced in a given month, or can we outsource an unlimited number of units as long as we pay 200 Yuan per unit?

## Turn 19 - User Simulator

There is no limit on the number of units that can be outsourced in a given month. We can outsource an unlimited number of units as long as we pay 200 Yuan per unit.

## Turn 20 - Generic Agent

QUESTION: Regarding the inventory balance, if we have beginning inventory of 15,000 units at the start of January, and in January we produce 10,000 units in-house and outsource 5,000 units, and the total demand to satisfy in January (including any backorders) is 20,000 units, would the ending inventory for January be 10,000 units (15,000 + 10,000 + 5,000 - 20,000), or is there a different way the inventory balance works?

## Turn 20 - User Simulator

Yes, the ending inventory for January would be 10,000 units (15,000 + 10,000 + 5,000 - 20,000).

## Turn 21 - Generic Agent

QUESTION: If the total available supply (beginning inventory + in-house production + outsourced units) in a month is less than the total demand to satisfy (current demand + prior backorders), the shortfall becomes a backorder. In that case, is the ending inventory for that month zero, or can it be negative (representing the backorder)?

## Turn 21 - User Simulator

The ending inventory for that month is zero. The shortfall is tracked separately as a backorder carried to the next month.

## Turn 22 - Generic Agent

QUESTION: Regarding the backorder tracking, if in January we have a backorder of 5,000 units carried to February, and in February the total demand to satisfy is 40,000 (current) + 5,000 (backorder) = 45,000 units, and we only satisfy 40,000 units, would the backorder carried to March be 5,000 units (the unsatisfied portion of the 45,000), or would it be 10,000 units (the original 5,000 plus the 5,000 unsatisfied from the current 40,000)?

## Turn 22 - User Simulator

The backorder carried to March would be 5,000 units. It is the unsatisfied portion of the total 45,000 units that needed to be satisfied in February.

## Turn 23 - Generic Agent

QUESTION: Regarding the sales revenue, if a unit is backordered in January and delivered in February, is the 300 Yuan revenue recognized in February (when it is delivered), or is it recognized in January (when the demand originally occurred)?

## Turn 23 - User Simulator

The 300 Yuan revenue is recognized in February, when the unit is delivered.

## Turn 24 - Generic Agent

QUESTION: Regarding the backorder cost, if a unit is backordered in January (unsatisfied in January) and delivered in February, is the 35 Yuan backorder cost charged in January (for the month it was backordered), or in February (when it is finally delivered)?

## Turn 24 - User Simulator

The 35 Yuan backorder cost is charged in January, for the month it was backordered.

## Turn 25 - Generic Agent

QUESTION: Regarding the inventory holding cost, if we have 10,000 units in ending inventory at the end of January, is the 15 Yuan per unit holding cost charged in January (for holding those units at the end of January), or in February (for holding them during February)?

## Turn 25 - User Simulator

The 15 Yuan per unit holding cost is charged in January, for holding those units at the end of January.

## Turn 26 - Generic Agent

QUESTION: Regarding the workforce and production in a given month, if we have 1,000 workers in January, the total regular hours available are 1,000 × 160 = 160,000 hours, and the total overtime hours available are 1,000 × 20 = 20,000 hours. The maximum in-house production would be (160,000 + 20,000) / 5 = 38,000 units. Is this correct, or is there a different way to calculate the production capacity?

## Turn 26 - User Simulator

Yes, that is correct. The maximum in-house production would be (160,000 + 20,000) / 5 = 38,000 units.

## Turn 27 - Generic Agent

QUESTION: Regarding the regular wage cost, if we have 1,000 workers in January, the regular wage cost for January is 1,000 × 160 × 30 = 4,800,000 Yuan, regardless of how many hours are actually used in production. Is this correct?

## Turn 27 - User Simulator

Yes, that is correct. The regular wage cost for January is 1,000 × 160 × 30 = 4,800,000 Yuan, regardless of how many hours are actually used in production.

## Turn 28 - Generic Agent

QUESTION: Regarding the overtime wage cost, if we use 10,000 overtime hours in January, the overtime wage cost for January is 10,000 × 40 = 400,000 Yuan. Is this correct, or is there a different way to calculate the overtime cost?

## Turn 28 - User Simulator

Yes, that is correct. The overtime wage cost for January is 10,000 × 40 = 400,000 Yuan.

## Turn 29 - Generic Agent

QUESTION: Regarding the net profit calculation, is the total net profit equal to total revenue (300 Yuan per unit delivered) minus all costs (raw material, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), summed over the six-month period?

## Turn 29 - User Simulator

Yes, the total net profit is equal to total revenue (300 Yuan per unit delivered) minus all costs (raw material, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), summed over the six-month period.

## Turn 30 - Generic Agent

QUESTION: Regarding the backorder constraint, you mentioned that all backorders must be cleared by the end of June. Does this mean that the ending backorder at the end of June must be zero, and therefore the total supply in June (beginning inventory + in-house production + outsourced units) must be at least the total demand in June (current demand + any backorders carried into June)?

## Turn 30 - User Simulator

Yes, that is correct. The ending backorder at the end of June must be zero, and therefore the total supply in June (beginning inventory + in-house production + outsourced units) must be at least the total demand in June (current demand + any backorders carried into June).