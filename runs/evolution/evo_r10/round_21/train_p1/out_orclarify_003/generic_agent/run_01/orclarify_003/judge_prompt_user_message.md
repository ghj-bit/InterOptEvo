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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker per month (so total workforce overtime is 20 times the number of workers that month), or is it a single aggregate cap of 20 hours for the whole workforce combined per month?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime available in any month is 20 hours multiplied by the number of workers on staff that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can you hire and fire workers in any month (including January), and is the workforce level for a month determined by the starting workforce plus hires minus firings in that same month (i.e., can you hire at the start of January and use them for January production)?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. The workforce level for a given month is the starting workforce for that month plus any hires minus any firings made in that same month. So, if you hire at the start of January, those workers are available for January production.

## Turn 3 - Generic Agent

QUESTION: For the regular wage, you said it is paid "regardless of utilization" — does that mean every worker on staff in a month is paid the full 160 regular hours at 30 Yuan/hour even if the actual regular hours used for production are fewer, so the regular wage cost is simply 160 × 30 × (number of workers that month)?

## Turn 3 - User Simulator

Yes, that is correct. Every worker on staff in a month is paid for the full 160 regular hours at 30 Yuan per hour, regardless of how many hours are actually used for production. So the regular wage cost for a month is 160 × 30 × (number of workers that month).

## Turn 4 - Generic Agent

QUESTION: For the sales price of 300 Yuan per unit — is this revenue earned on every unit that is ultimately delivered to meet demand (including backordered units delivered in a later month), or only on units sold in the month the demand originally occurred?

## Turn 4 - User Simulator

The 300 Yuan sales price is earned on every unit ultimately delivered to meet demand, including backordered units delivered in a later month.

## Turn 5 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit — is it incurred only on units produced in-house, and is it incurred in the month the unit is produced (even if that unit sits in inventory or is used to satisfy a backorder later)?

## Turn 5 - User Simulator

Yes, the 90 Yuan raw material cost is incurred only on units produced in-house, and it is incurred in the month the unit is produced, regardless of whether that unit is sold immediately, held in inventory, or used to satisfy a backorder in a later month.

## Turn 6 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit — is it charged on the ending inventory of each month (i.e., the inventory carried over at the end of that month), and does it apply to all six months including June's ending inventory of at least 10,000 units?

## Turn 6 - User Simulator

Yes, the 15 Yuan inventory holding cost is charged on the ending inventory of each month, and it applies to all six months, including June's ending inventory.

## Turn 7 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit — is it charged on the amount of unfulfilled demand carried over at the end of each month (i.e., the backorder balance at month-end), and can backorders accumulate across multiple months (so a unit of demand unmet in January and still unmet in February incurs the 35 Yuan cost in both January and February)?

## Turn 7 - User Simulator

Yes, the 35 Yuan backorder cost is charged on the backorder balance at the end of each month. Backorders can accumulate across multiple months, so a unit of demand unmet in January and still unmet in February incurs the 35 Yuan cost in both January and February.

## Turn 8 - Generic Agent

QUESTION: For the workforce, is there any minimum or maximum limit on the number of workers you can have in a month (other than the non-negativity constraint), or can the workforce be any non-negative integer from 0 up to some unbounded level?

## Turn 8 - User Simulator

There is no minimum or maximum limit on the number of workers other than the non-negativity constraint. The workforce can be any non-negative integer from 0 up to an unbounded level.

## Turn 9 - Generic Agent

QUESTION: For the production capacity, is the only limit on in-house production the available labor hours (regular 160 hours plus overtime up to 20 hours per worker), or is there any separate machine or facility capacity cap on the number of units that can be produced in-house per month?

## Turn 9 - User Simulator

The only limit on in-house production is the available labor hours (regular 160 hours plus overtime up to 20 hours per worker). There is no separate machine or facility capacity cap on the number of units that can be produced in-house per month.

## Turn 10 - Generic Agent

QUESTION: For the outsourcing, is there any limit on the number of units that can be outsourced per month, or can you outsource any non-negative number of units at 200 Yuan each?

## Turn 10 - User Simulator

There is no limit on the number of units that can be outsourced per month. You can outsource any non-negative number of units at 200 Yuan each.

## Turn 11 - Generic Agent

QUESTION: For the demand fulfillment, you said orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units — does this mean that in each month, the total available supply (beginning inventory + in-house production + outsourcing) must be at least the current month's demand, and any shortfall becomes a backorder carried to the next month?

## Turn 11 - User Simulator

Yes, that is correct. In each month, the total available supply (beginning inventory + in-house production + outsourcing) is used to fulfill the current month's demand plus any backorders carried in from the previous month. If the total available supply is less than the total orders (current demand + incoming backorders), the shortfall becomes a backorder carried to the next month.

## Turn 12 - Generic Agent

QUESTION: For the ending inventory at the end of June, must it be exactly 10,000 units, or at least 10,000 units (i.e., it can be more than 10,000)?

## Turn 12 - User Simulator

It must be at least 10,000 units. The ending inventory at the end of June can be more than 10,000 units.

## Turn 13 - Generic Agent

QUESTION: For the backorders, is there any requirement that all backorders must be cleared by the end of June (i.e., no backorders can remain after June), or is it acceptable to still have unfulfilled demand at the end of June as long as the ending inventory is at least 10,000 units?

## Turn 13 - User Simulator

Yes, all backorders must be cleared by the end of June. No outstanding customer orders can remain after June; everything must be fulfilled within the six months.

## Turn 14 - Generic Agent

QUESTION: For the labor hours, can regular hours be partially used (e.g., only 100 out of 160 regular hours used in a month), or must all 160 regular hours be fully utilized if any production occurs?

## Turn 14 - User Simulator

Regular hours can be partially used. You do not need to fully utilize all 160 regular hours in a month; you can use any amount up to 160 regular hours per worker for production.

## Turn 15 - Generic Agent

QUESTION: For the overtime hours, can they be partially used (e.g., only 10 out of 20 overtime hours per worker), or must overtime be used in full if any overtime is used at all?

## Turn 15 - User Simulator

Overtime hours can be partially used. You can use any amount up to 20 overtime hours per worker per month; there is no requirement to use the full 20 hours if you use any overtime at all.

## Turn 16 - Generic Agent

QUESTION: For the production variables, should in-house production, outsourcing, hires, firings, and workforce levels all be integer-valued (whole units/whole workers), or can they be treated as continuous variables?

## Turn 16 - User Simulator

All of these should be integer-valued: in-house production (whole units), outsourcing (whole units), hires (whole workers), firings (whole workers), and workforce levels (whole workers).

## Turn 17 - Generic Agent

QUESTION: For the inventory and backorder variables, should ending inventory and backorder balances also be integer-valued (whole units), or can they be continuous?

## Turn 17 - User Simulator

Yes, ending inventory and backorder balances should also be integer-valued (whole units).

## Turn 18 - Generic Agent

QUESTION: For the net profit objective, is it simply total revenue (300 per unit delivered) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue or cost components?

## Turn 18 - User Simulator

Yes, the net profit objective is simply total revenue (300 Yuan per unit delivered) minus all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing. There are no other revenue or cost components.

## Turn 19 - Generic Agent

QUESTION: For the workforce flow, is the workforce at the start of each month equal to the workforce at the end of the previous month (i.e., workforce_t = workforce_{t-1} + hires_t - firings_t, where workforce_0 = 1000), and can hires and firings both occur in the same month?

## Turn 19 - User Simulator

Yes, the workforce at the start of each month is equal to the workforce at the end of the previous month, so workforce_t = workforce_{t-1} + hires_t - firings_t, where workforce_0 = 1,000. And yes, hires and firings can both occur in the same month.

## Turn 20 - Generic Agent

QUESTION: For the inventory flow, is the ending inventory of each month equal to the beginning inventory plus in-house production plus outsourcing minus the units actually delivered to meet orders (current demand plus incoming backorders that are fulfilled), and can inventory and backorders both be positive in the same month?

## Turn 20 - User Simulator

Yes, the ending inventory of each month is equal to the beginning inventory plus in-house production plus outsourcing minus the units actually delivered to meet orders (current demand plus incoming backorders that are fulfilled).

And yes, inventory and backorders can both be positive in the same month.

## Turn 21 - Generic Agent

QUESTION: For the inventory and backorder flow, if both inventory and backorders can be positive in the same month, how is the fulfillment priority determined — do you first use available inventory to cover orders, and only if inventory is insufficient do you use current production and outsourcing, with any remaining shortfall becoming a backorder?

## Turn 21 - User Simulator

Yes, the fulfillment priority is: first use available inventory to cover orders, then use current in-house production, then use outsourcing. Any remaining shortfall after all available supply is used becomes a backorder carried to the next month.

## Turn 22 - Generic Agent

QUESTION: For the backorder cost, is it charged on the total backorder balance at the end of each month (i.e., all unfulfilled units carried over), or only on the new backorders created in that month (i.e., the shortfall that month, not the cumulative balance)?

## Turn 22 - User Simulator

The backorder cost is charged on the total backorder balance at the end of each month (i.e., all unfulfilled units carried over), not just the new backorders created in that month.

## Turn 23 - Generic Agent

QUESTION: For the sales revenue, since backorders must be cleared by the end of June, does that mean all 175,500 units of total demand (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500) must be delivered by the end of June, and the total revenue is simply 300 × 175,500?

## Turn 23 - User Simulator

Yes, since all backorders must be cleared by the end of June, all 175,500 units of total demand must be delivered by the end of June. The total revenue is simply 300 × 175,500.

## Turn 24 - Generic Agent

QUESTION: For the initial inventory of 15,000 units at the start of January, is there any cost associated with this initial inventory (e.g., a holding cost for January's beginning inventory), or is the holding cost only charged on ending inventory as you confirmed earlier?

## Turn 24 - User Simulator

There is no cost associated with the initial inventory of 15,000 units at the start of January. The holding cost is only charged on ending inventory, as confirmed earlier.

## Turn 25 - Generic Agent

QUESTION: For the overtime wage cost, is it simply 40 Yuan per overtime hour actually used (i.e., 40 × total overtime hours in the month), with no additional premium or surcharge beyond the 40 Yuan rate?

## Turn 25 - User Simulator

Yes, the overtime wage cost is simply 40 Yuan per overtime hour actually used (i.e., 40 × total overtime hours in the month), with no additional premium or surcharge beyond the 40 Yuan rate.

## Turn 26 - Generic Agent

QUESTION: For the hiring and firing costs, are they one-time costs incurred in the month the hire or fire occurs (i.e., 5,000 per worker hired in that month, 8,000 per worker fired in that month), with no recurring or ongoing cost associated with the workforce beyond the regular and overtime wages?

## Turn 26 - User Simulator

Yes, hiring and firing costs are one-time costs incurred in the month the hire or fire occurs (5,000 Yuan per worker hired, 8,000 Yuan per worker fired). There are no recurring or ongoing costs associated with the workforce beyond the regular and overtime wages.

## Turn 27 - Generic Agent

QUESTION: For the in-house production labor hours, is the total labor hours used for in-house production in a month equal to 5 times the number of in-house units produced, and must this total be less than or equal to the total available hours (160 × workforce + overtime hours used)?

## Turn 27 - User Simulator

Yes, the total labor hours used for in-house production in a month is equal to 5 times the number of in-house units produced. This total must be less than or equal to the total available hours, which is (160 × workforce) + overtime hours used.

## Turn 28 - Generic Agent

QUESTION: For the overtime hours, is the total overtime hours used in a month simply a decision variable that can range from 0 to 20 × workforce, and is the overtime cost 40 × (total overtime hours used), with the constraint that total labor hours (regular used + overtime used) must equal 5 × in-house production?

## Turn 28 - User Simulator

Yes, the total overtime hours used in a month is a decision variable that can range from 0 to 20 × workforce. The overtime cost is 40 × (total overtime hours used). And yes, the total labor hours (regular hours used + overtime hours used) must equal 5 × in-house production.

## Turn 29 - Generic Agent

QUESTION: For the regular hours used, is it simply the total labor hours minus overtime hours used, and must it be less than or equal to 160 × workforce (i.e., regular hours used = 5 × in-house production - overtime hours used, with the constraint that regular hours used ≤ 160 × workforce)?

## Turn 29 - User Simulator

Yes, the regular hours used is simply the total labor hours minus overtime hours used. It must be less than or equal to 160 × workforce. So, regular hours used = 5 × in-house production - overtime hours used, with the constraint that regular hours used ≤ 160 × workforce.

## Turn 30 - Generic Agent

QUESTION: For the fulfillment in each month, is the total units delivered in a month equal to the current month's demand plus the incoming backorders from the previous month minus the new backorders created in that month, and is this total delivered units equal to the total available supply (beginning inventory + in-house production + outsourcing) minus the ending inventory?

## Turn 30 - User Simulator

Yes, the total units delivered in a month is equal to the current month's demand plus the incoming backorders from the previous month minus the new backorders created in that month. And yes, this total delivered units is equal to the total available supply (beginning inventory + in-house production + outsourcing) minus the ending inventory.