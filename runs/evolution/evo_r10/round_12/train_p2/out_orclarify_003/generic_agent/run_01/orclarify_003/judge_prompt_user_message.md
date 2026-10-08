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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker per month (so total workforce overtime can be up to 20 × number of workers), or that the sum of overtime hours across all workers combined is capped at 20 hours per month?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime available in a month is 20 times the number of workers on staff that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can you hire and fire workers in any month (including January), and is the workforce level for a month determined by the number of workers on staff during that month (i.e., hires and firings happen at the start of the month and affect that month's production capacity)?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. The workforce level for a month is determined by the number of workers on staff during that month, with hires and firings happening at the start of the month and affecting that month's production capacity.

## Turn 3 - Generic Agent

QUESTION: Regarding the inventory balance, when you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in a given month, the total units available to meet demand (current + backorders) are: ending inventory from the prior month + in-house production that month + outsourced units that month, and any shortfall becomes a new backorder carried to the next month?

## Turn 3 - User Simulator

Yes, that is correct. In a given month, the total units available to meet demand (current demand plus any backorders from the prior month) are the ending inventory from the prior month plus in-house production that month plus outsourced units that month. Any shortfall becomes a new backorder carried to the next month.

## Turn 4 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit, is this charged on the ending inventory of each month (i.e., units remaining at the end of January, end of February, etc.), and does the 10,000-unit minimum ending inventory requirement at the end of June count as part of that ending inventory (so it would also incur the 15 Yuan holding cost)?

## Turn 4 - User Simulator

Yes, the 15 Yuan holding cost is charged on the ending inventory of each month. The 10,000-unit minimum ending inventory requirement at the end of June is part of that ending inventory, so it also incurs the 15 Yuan holding cost.

## Turn 5 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit, is this charged on the number of units that are backordered at the end of each month (i.e., the unfulfilled demand carried into the next month), and is there any limit on how many months a backorder can be carried before it must be fulfilled?

## Turn 5 - User Simulator

Yes, the 35 Yuan backorder cost is charged on the number of units backordered at the end of each month. There is no limit on how many months a backorder can be carried, except that all backorders must be cleared by the end of June.

## Turn 6 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production, is this cost incurred for every unit produced in-house regardless of whether that unit is sold in the same month or held in inventory, and is there any raw material cost associated with outsourced units (or is the 200 Yuan outsourcing cost truly all-inclusive with no additional material cost)?

## Turn 6 - User Simulator

Yes, the 90 Yuan raw material cost is incurred for every unit produced in-house, regardless of whether that unit is sold in the same month or held in inventory. The 200 Yuan outsourcing cost is all-inclusive, with no additional raw material cost associated with outsourced units.

## Turn 7 - Generic Agent

QUESTION: Regarding the sales revenue of 300 Yuan per unit, is this revenue recognized in the month the unit is actually sold (i.e., when demand is fulfilled), meaning that backordered units generate revenue in the month they are eventually delivered rather than the month the demand was originally placed?

## Turn 7 - User Simulator

Yes, the 300 Yuan sales revenue is recognized in the month the unit is actually sold, meaning backordered units generate revenue in the month they are eventually delivered rather than the month the demand was originally placed.

## Turn 8 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for 160 hours per worker, is this a fixed cost of 4,800 Yuan per worker per month (160 × 30) that is paid regardless of how many hours are actually used for production, so that even if a worker is idle, the full 4,800 Yuan is still paid?

## Turn 8 - User Simulator

Yes, the regular wage is a fixed cost of 4,800 Yuan per worker per month (160 hours × 30 Yuan/hour), paid regardless of how many hours are actually used for production. Even if a worker is idle, the full 4,800 Yuan is still paid.

## Turn 9 - Generic Agent

QUESTION: Regarding the workforce, is there any constraint that the workforce must remain non-negative (obviously), and can the workforce drop to zero in any month, or is there a minimum number of workers that must be maintained at all times?

## Turn 9 - User Simulator

The workforce must remain non-negative. There is no minimum number of workers that must be maintained at all times, so the workforce can drop to zero in any month.

## Turn 10 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January, is this inventory available to fulfill January's demand (i.e., it counts as the "ending inventory from the prior month" in the January balance equation), and does it incur a holding cost for January (i.e., is the holding cost charged on the ending inventory of January, which would be the 15,000 minus what was used plus what was produced/outsourced)?

## Turn 10 - User Simulator

Yes, the initial 15,000 units at the start of January are available to fulfill January's demand and count as the "ending inventory from the prior month" in the January balance equation. The holding cost is charged on the ending inventory of January, which is the 15,000 units minus what was used plus what was produced or outsourced during January.

## Turn 11 - Generic Agent

QUESTION: Regarding the initial workforce of 1,000 employees at the start of January, is the regular wage cost of 4,800 Yuan per worker per month applied to the workforce level during January (which would be 1,000 plus any hires minus any firings at the start of January), and is the hiring/firing cost incurred in the same month the change takes effect?

## Turn 11 - User Simulator

Yes, the regular wage cost of 4,800 Yuan per worker per month is applied to the workforce level during January, which is 1,000 plus any hires minus any firings at the start of January. The hiring and firing costs are incurred in the same month the change takes effect.

## Turn 12 - Generic Agent

QUESTION: Regarding the production capacity, is the maximum in-house production in a month limited by the total available labor hours (workforce × 160 regular hours + workforce × 20 overtime hours), with each unit requiring 5 labor hours, so the maximum in-house production is (workforce × 180) / 5 units per month?

## Turn 12 - User Simulator

Yes, the maximum in-house production in a month is limited by the total available labor hours, which is the workforce multiplied by 160 regular hours plus the workforce multiplied by 20 overtime hours. Since each unit requires 5 labor hours, the maximum in-house production is (workforce × 180) / 5 units per month.

## Turn 13 - Generic Agent

QUESTION: Regarding the overtime cost, is the overtime wage of 40 Yuan per hour charged only on the overtime hours actually used for production (i.e., if a worker uses 10 overtime hours, the cost is 10 × 40 = 400 Yuan for that worker), rather than a fixed charge for the full 20 hours of overtime capacity?

## Turn 13 - User Simulator

Yes, the overtime wage of 40 Yuan per hour is charged only on the overtime hours actually used for production. If a worker uses 10 overtime hours, the cost is 10 × 40 = 400 Yuan for that worker. It is not a fixed charge for the full 20 hours of overtime capacity.

## Turn 14 - Generic Agent

QUESTION: Regarding the net profit objective, is it simply total revenue minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing) over the six-month period, with no other revenue or cost components I haven't mentioned?

## Turn 14 - User Simulator

Yes, the net profit objective is simply total revenue minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing) over the six-month period, with no other revenue or cost components.

## Turn 15 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total net profit over January–June.

**Net profit = Total revenue − Total costs**, where:
- Revenue: 300 Yuan per unit sold (recognized in the month the unit is delivered, including backordered units).
- Costs: raw materials (90/unit in-house), outsourcing (200/unit all-inclusive), inventory holding (15/unit on ending inventory each month), backorder (35/unit on units backordered at end of each month), regular wages (4,800/worker/month fixed), overtime wages (40/hour on overtime hours actually used), hiring (5,000/worker), firing (8,000/worker).

**Decision variables (per month t = 1..6):**
- Workforce level W_t (integer, ≥ 0)
- Hires H_t (integer, ≥ 0)
- Firings F_t (integer, ≥ 0)
- In-house production P_t (continuous or integer, ≥ 0)
- Outsourced units O_t (continuous or integer, ≥ 0)
- Ending inventory I_t (≥ 0)
- Backorders B_t (≥ 0)
- Overtime hours used OT_t (≥ 0)

**Workforce balance:** W_t = W_{t−1} + H_t − F_t, with W_0 = 1,000.

**Inventory/demand balance:** I_{t−1} + P_t + O_t = D_t + B_t − B_{t−1} + I_t, where I_0 = 15,000, B_0 = 0, and B_6 = 0 (all backorders cleared by end of June).

**Production capacity:** 5 × P_t ≤ 160 × W_t + OT_t, with OT_t ≤ 20 × W_t.

**Ending inventory constraint:** I_6 ≥ 10,000.

**Demand:** Jan 20,000; Feb 40,000; Mar 42,000; Apr 35,000; May 19,000; Jun 18,500.

**Key confirmed details:**
- Overtime cap is 20 hours per individual worker per month.
- Hires/firings at start of month affect that month's capacity and wage cost.
- Regular wage is fixed at 4,800/worker/month regardless of utilization.
- Overtime cost is variable, charged only on hours actually used.
- Raw material cost applies to all in-house units produced (whether sold or inventoried).
- Outsourcing cost is all-inclusive (no additional material cost).
- Holding cost on ending inventory each month (including the 10,000 minimum in June).
- Backorder cost on units carried at end of each month; no limit on carry duration except all must be cleared by end of June.
- Workforce can drop to zero; no minimum workforce.
- Initial 15,000 inventory available for January demand.