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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 × number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can you hire and fire workers in any month (including January), and is the workforce level for a month determined before or after that month's hiring/firing decisions — that is, if you hire 100 workers in January, are those 100 available to produce in January itself, or only starting in February?

## Turn 2 - User Simulator

You can hire and fire workers in any month, including January. The workforce level for a month is determined after that month's hiring and firing decisions. So if you hire 100 workers in January, those 100 are available to produce in January itself.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered, is the backorder cost of 35 Yuan per unit charged once for the month the demand is first unfulfilled, or is it charged every month the unit remains unfulfilled until it is finally delivered?

## Turn 3 - User Simulator

The backorder cost of 35 Yuan per unit is charged every month the unit remains unfulfilled until it is finally delivered.

## Turn 4 - Generic Agent

QUESTION: When a backorder is finally fulfilled in a later month, is the sales revenue of 300 Yuan per unit recognized in the month the unit is actually delivered, or in the month the demand originally occurred?

## Turn 4 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the month the unit is actually delivered.

## Turn 5 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (including June's ending inventory of at least 10,000 units), or only on inventory carried over to a subsequent month (i.e., excluding June's final ending inventory)?

## Turn 5 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including June's ending inventory.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many units can be outsourced in a month, or is outsourcing unlimited as long as you pay 200 Yuan per unit?

## Turn 6 - User Simulator

There is no limit on how many units can be outsourced in a month. Outsourcing is unlimited as long as you pay 200 Yuan per unit.

## Turn 7 - Generic Agent

QUESTION: Can the workforce be reduced to zero workers in any month, or is there a minimum number of workers that must be maintained at all times?

## Turn 7 - User Simulator

There is no minimum number of workers that must be maintained. The workforce can be reduced to zero in any month.

## Turn 8 - Generic Agent

QUESTION: Are the number of workers, in-house production units, and outsourced units required to be whole numbers (integers), or can they be treated as continuous values in the model?

## Turn 8 - User Simulator

The number of workers, in-house production units, and outsourced units are required to be whole numbers (integers).

## Turn 9 - Generic Agent

QUESTION: When demand is back-ordered and later fulfilled, is the raw material cost of 90 Yuan per unit still charged if the unit is produced in-house in the later fulfillment month, or is raw material cost only charged in the month the demand originally occurred?

## Turn 9 - User Simulator

The raw material cost of 90 Yuan per unit is charged in the month the unit is actually produced in-house, regardless of when the demand originally occurred.

## Turn 10 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," is there any priority or constraint on the order in which these sources are used — for example, must you use up previous inventory before producing in-house, or before outsourcing — or can you freely mix all three sources in any proportion to meet demand?

## Turn 10 - User Simulator

There is no priority or constraint on the order in which these sources are used. You can freely mix all three sources—previous inventory, current in-house production, and outsourced units—in any proportion to meet demand.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on the total number of workers you can hire in a single month, or is hiring unlimited as long as you pay 5,000 Yuan per new worker?

## Turn 11 - User Simulator

There is no limit on the total number of workers you can hire in a single month. Hiring is unlimited as long as you pay 5,000 Yuan per new worker.

## Turn 12 - Generic Agent

QUESTION: For the regular wage of 30 Yuan per hour for 160 hours per worker, is this cost incurred for every worker employed in a month regardless of how many hours they actually work (i.e., even if they work zero hours), or is it only paid for hours actually worked up to 160?

## Turn 12 - User Simulator

The regular wage of 30 Yuan per hour for 160 hours per worker is incurred for every worker employed in a month regardless of how many hours they actually work. It is paid even if they work zero hours.

## Turn 13 - Generic Agent

QUESTION: If demand in a month exceeds what can be fulfilled (inventory + in-house production + outsourcing), the unfulfilled portion becomes a backorder. Is there any limit on how many units can be back-ordered in a single month, or can any amount of demand be deferred?

## Turn 13 - User Simulator

There is no limit on how many units can be back-ordered in a single month. Any amount of demand can be deferred, as long as all backorders are cleared by the end of June.

## Turn 14 - Generic Agent

QUESTION: You mentioned all backorders must be cleared by the end of June. Does this mean that by the end of June, all demand from January through June must have been fully delivered (i.e., no backorders remaining), in addition to the 10,000-unit ending inventory requirement?

## Turn 14 - User Simulator

Yes, that is correct. By the end of June, all demand from January through June must have been fully delivered, meaning no backorders remain. This is in addition to the requirement that the ending inventory at the end of June must be at least 10,000 units.

## Turn 15 - Generic Agent

QUESTION: For the 10,000-unit minimum ending inventory at the end of June, does this inventory need to be in addition to fulfilling all demand (i.e., total production + outsourcing + initial inventory must cover all 175,500 units of demand plus 10,000 units of ending inventory), or could some of the 10,000 units come from the initial 15,000 inventory if demand is less?

## Turn 15 - User Simulator

The 10,000-unit minimum ending inventory at the end of June is in addition to fulfilling all demand. Total production, outsourcing, and initial inventory must cover all 175,500 units of demand plus the 10,000 units of ending inventory.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house in a month beyond the labor hour limit (i.e., 160 regular + 20 overtime hours per worker), or is in-house production capacity solely determined by available labor hours?

## Turn 16 - User Simulator

In-house production capacity is solely determined by available labor hours. There is no additional constraint on the total number of units that can be produced in-house beyond the labor hour limit of 160 regular plus 20 overtime hours per worker.

## Turn 17 - Generic Agent

QUESTION: Can workers be hired and fired in the same month, and if so, is the hiring cost of 5,000 Yuan and firing cost of 8,000 Yuan both incurred in that month for the respective numbers of workers hired and fired?

## Turn 17 - User Simulator

Yes, workers can be hired and fired in the same month. The hiring cost of 5,000 Yuan is incurred for each worker hired, and the firing cost of 8,000 Yuan is incurred for each worker fired, both in that month.

## Turn 18 - Generic Agent

QUESTION: For the workforce balance, if you start a month with W workers, hire H workers, and fire F workers, is the workforce for that month W + H - F, and must W + H - F be non-negative (i.e., you cannot fire more workers than you have)?

## Turn 18 - User Simulator

Yes, the workforce for that month is W + H - F, and it must be non-negative. You cannot fire more workers than you have.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of June must be at least some minimum number, or can the workforce be reduced to zero by the end of June?

## Turn 19 - User Simulator

There is no constraint that the workforce at the end of June must be at least some minimum number. The workforce can be reduced to zero by the end of June.

## Turn 20 - Generic Agent

QUESTION: For the overtime hours, if a worker works overtime, is the overtime production (units produced using overtime hours) subject to the same 5 labor hours per unit requirement as regular production, meaning overtime hours can only be used to produce additional units beyond what regular hours produce?

## Turn 20 - User Simulator

Yes, overtime hours are subject to the same 5 labor hours per unit requirement. Overtime hours can only be used to produce additional units beyond what regular hours produce.

## Turn 21 - Generic Agent

QUESTION: When you say "orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," does the initial inventory of 15,000 units at the start of January count as "available inventory from the previous month" for fulfilling January's demand?

## Turn 21 - User Simulator

Yes, the initial inventory of 15,000 units at the start of January counts as "available inventory from the previous month" for fulfilling January's demand.

## Turn 22 - Generic Agent

QUESTION: For the inventory balance, is the ending inventory of a month calculated as: beginning inventory + in-house production + outsourcing - units delivered (current demand fulfilled + backorders from previous months fulfilled), and can this ending inventory be negative (representing backorders) or must it be non-negative with backorders tracked separately?

## Turn 22 - User Simulator

The ending inventory of a month is calculated as: beginning inventory + in-house production + outsourcing - units delivered (current demand fulfilled + backorders from previous months fulfilled). The ending inventory must be non-negative, with backorders tracked separately.

## Turn 23 - Generic Agent

QUESTION: If ending inventory must be non-negative and backorders are tracked separately, does that mean in any month you cannot use more inventory + production + outsourcing than the total demand (current + prior backorders) to be fulfilled that month, and any shortfall becomes a new backorder carried to the next month?

## Turn 23 - User Simulator

Yes, that is correct. In any month, you cannot use more inventory + production + outsourcing than the total demand (current + prior backorders) to be fulfilled that month. Any shortfall becomes a new backorder carried to the next month.

## Turn 24 - Generic Agent

QUESTION: For the backorder tracking, if there are 5,000 units of backorder from January and in February you can only fulfill 3,000 units of total demand (February's 40,000 + January's 5,000), is the remaining 7,000 units all carried as backorder to March, with the backorder cost of 35 Yuan charged on all 7,000 units for February?

## Turn 24 - User Simulator

Yes, that is correct. If there are 5,000 units of backorder from January and in February you can only fulfill 3,000 units of total demand (February's 40,000 + January's 5,000), the remaining 42,000 units are carried as backorder to March, with the backorder cost of 35 Yuan charged on all 42,000 units for February.

## Turn 25 - Generic Agent

QUESTION: For the backorder cost, is it charged on the total backorder balance carried at the end of each month (i.e., the cumulative unfulfilled units from all prior months plus any new shortfall), or only on the new shortfall created in that specific month?

## Turn 25 - User Simulator

The backorder cost is charged on the total backorder balance carried at the end of each month, which includes the cumulative unfulfilled units from all prior months plus any new shortfall created in that specific month.

## Turn 26 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month from January through June, meaning June's ending inventory of at least 10,000 units also incurs the 15 Yuan per unit holding cost?

## Turn 26 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month from January through June, including June's ending inventory of at least 10,000 units.

## Turn 27 - Generic Agent

QUESTION: For the sales revenue of 300 Yuan per unit, is it recognized only when a unit is actually delivered to the customer (i.e., when demand or a backorder is fulfilled), and not on units that remain in inventory at the end of June?

## Turn 27 - User Simulator

Yes, the sales revenue of 300 Yuan per unit is recognized only when a unit is actually delivered to the customer (i.e., when demand or a backorder is fulfilled). It is not recognized on units that remain in inventory at the end of June.

## Turn 28 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it charged only on units produced in-house, and not on outsourced units (which already have the 200 Yuan all-inclusive outsourcing cost)?

## Turn 28 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is charged only on units produced in-house. It is not charged on outsourced units, which already have the 200 Yuan all-inclusive outsourcing cost.

## Turn 29 - Generic Agent

QUESTION: For the workforce, if you have W workers in a month, the total regular hours available are 160 × W and total overtime hours available are 20 × W. Is the total in-house production in that month limited to (160 × W + 20 × W) / 5 units, or can you choose to use fewer than the maximum available hours?

## Turn 29 - User Simulator

The total in-house production in that month is limited to (160 × W + 20 × W) / 5 units. You can choose to use fewer than the maximum available hours, but you cannot exceed that limit.

## Turn 30 - Generic Agent

QUESTION: For the overtime wage of 40 Yuan per hour, is it charged only on the overtime hours actually used for production, or is it charged on all 20 overtime hours per worker regardless of whether they are used?

## Turn 30 - User Simulator

The overtime wage of 40 Yuan per hour is charged only on the overtime hours actually used for production. It is not charged on all 20 overtime hours per worker regardless of whether they are used.