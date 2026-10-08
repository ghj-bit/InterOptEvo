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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker per month (i.e., total workforce overtime ≤ 20 × number of workers that month), or is it a single aggregate cap of 20 hours for the whole workforce combined per month?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime hours for the entire workforce in any given month cannot exceed 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: You mentioned that orders are fulfilled using available inventory from the previous month, current in-house production, and outsourced units — but can backorders also be satisfied by outsourcing, or is outsourcing only available for current-month demand?

## Turn 2 - User Simulator

Outsourcing can be used to satisfy both current-month demand and backorders. There is no restriction limiting outsourcing to current-month demand only.

## Turn 3 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire workers in any month (January through June), or are hiring/firing decisions only allowed at the start of January?

## Turn 3 - User Simulator

Hiring and firing decisions can be made in any month from January through June.

## Turn 4 - Generic Agent

QUESTION: When a worker is hired or fired in a given month, does that change take effect immediately within that same month (so the new worker count is used for that month's production capacity and wage calculations), or does it take effect starting the next month?

## Turn 4 - User Simulator

The change takes effect immediately within that same month. The new worker count is used for that month's production capacity and wage calculations.

## Turn 5 - Generic Agent

QUESTION: Is there any upper limit on the number of workers you can hire in a single month, or is the workforce size effectively unbounded above (subject only to the hiring cost)?

## Turn 5 - User Simulator

There is no upper limit on the number of workers that can be hired in a single month. The workforce size is effectively unbounded above, subject only to the hiring cost.

## Turn 6 - Generic Agent

QUESTION: Is there a minimum workforce size that must be maintained in any month, or can the workforce theoretically drop to zero workers in a given month?

## Turn 6 - User Simulator

There is no minimum workforce size that must be maintained. The workforce can theoretically drop to zero workers in a given month.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a single month, or is outsourcing capacity effectively unlimited (subject only to the 200 Yuan per unit cost)?

## Turn 7 - User Simulator

There is no upper limit on the number of units that can be outsourced in a single month. Outsourcing capacity is effectively unlimited, subject only to the 200 Yuan per unit cost.

## Turn 8 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for 160 hours per worker, paid regardless of utilization — does this mean the total regular wage cost each month is simply 30 × 160 × (number of workers that month), even if the workers are not fully utilized for production?

## Turn 8 - User Simulator

Yes, the total regular wage cost each month is simply 30 × 160 × (number of workers that month), even if the workers are not fully utilized for production.

## Turn 9 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit — is this charged on the ending inventory of each month (i.e., the inventory remaining at the end of January, end of February, etc.), and does it also apply to the ending inventory at the end of June (the 10,000+ units required)?

## Turn 9 - User Simulator

Yes, the inventory holding cost of 15 Yuan per unit is charged on the ending inventory of each month, including the ending inventory at the end of June.

## Turn 10 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit — is this charged on the amount of unfulfilled demand carried over from one month to the next (i.e., the backorder balance at the end of each month), and does it apply to all months including June?

## Turn 10 - User Simulator

Yes, the backorder cost of 35 Yuan per unit is charged on the backorder balance at the end of each month. However, because all backorders must be cleared by the end of June, the backorder balance at the end of June is zero, so no backorder cost is incurred for June.

## Turn 11 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June — does this mean that by the end of June, all cumulative demand from January through June must have been fully satisfied (i.e., no backorders remain), or is it acceptable to have some unfulfilled demand at the end of June as long as the ending inventory is at least 10,000 units?

## Turn 11 - User Simulator

Yes, by the end of June, all cumulative demand from January through June must have been fully satisfied. No backorders can remain at the end of June. The ending inventory requirement of at least 10,000 units is a separate condition that must also be met.

## Turn 12 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit — is this cost incurred only for units produced in-house, and is it independent of whether those units are used to satisfy current demand, backorders, or added to inventory?

## Turn 12 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred only for units produced in-house. It applies regardless of whether those units are used to satisfy current demand, backorders, or added to inventory.

## Turn 13 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is revenue recognized in the month the demand is actually fulfilled (i.e., when the unit is delivered to the customer), or is it recognized in the month the demand originally occurred, even if it is backordered and fulfilled later?

## Turn 13 - User Simulator

Revenue is recognized in the month the demand is actually fulfilled, i.e., when the unit is delivered to the customer.

## Turn 14 - Generic Agent

QUESTION: Regarding the labor hours constraint — the total in-house production in a month is limited by (number of workers × 160 regular hours + number of workers × 20 overtime hours) divided by 5 hours per unit. Is this the correct interpretation, meaning each worker can contribute at most 180 hours (160 regular + 20 overtime) per month to in-house production?

## Turn 14 - User Simulator

Yes, that is the correct interpretation. Each worker can contribute at most 180 hours (160 regular + 20 overtime) per month to in-house production.

## Turn 15 - Generic Agent

QUESTION: Regarding the overtime wage of 40 Yuan per hour — is this cost incurred only for the overtime hours actually used for production, or is it paid for all 20 overtime hours per worker regardless of whether they are fully utilized?

## Turn 15 - User Simulator

The overtime wage of 40 Yuan per hour is incurred only for the overtime hours actually used for production. It is not paid for all 20 overtime hours per worker regardless of utilization.

## Turn 16 - Generic Agent

QUESTION: Regarding the inventory balance — can inventory and backorders both be positive in the same month (i.e., can you simultaneously have leftover inventory and unfulfilled demand), or must one be zero whenever the other is positive?

## Turn 16 - User Simulator

Inventory and backorders cannot both be positive in the same month. If there is leftover inventory, backorders must be zero, and if there are backorders, inventory must be zero.

## Turn 17 - Generic Agent

QUESTION: Regarding the inventory and backorder balance equation for each month — the available supply (beginning inventory + in-house production + outsourcing) is used to first satisfy backorders from the previous month, then current demand, with any remainder going to ending inventory (or any shortfall becoming new backorders). Is this the correct priority order for allocating supply?

## Turn 17 - User Simulator

Yes, that is the correct priority order. Available supply (beginning inventory + in-house production + outsourcing) is used to first satisfy backorders from the previous month, then current demand, with any remainder going to ending inventory or any shortfall becoming new backorders.

## Turn 18 - Generic Agent

QUESTION: Regarding the workforce balance — the number of workers at the start of each month equals the number of workers at the end of the previous month, plus hires minus firings in that month. Is this correct, meaning the workforce evolves as: Workers(t) = Workers(t-1) + Hires(t) - Firings(t), where Workers(0) = 1,000?

## Turn 18 - User Simulator

Yes, that is correct. The workforce evolves as: Workers(t) = Workers(t-1) + Hires(t) - Firings(t), where Workers(0) = 1,000.

## Turn 19 - Generic Agent

QUESTION: Regarding the objective function — is the total net profit calculated as total revenue (300 × total units sold over 6 months) minus all costs (raw materials, outsourcing, regular wages, overtime wages, inventory holding, backorder costs, hiring, and firing), with no other revenue or cost components?

## Turn 19 - User Simulator

Yes, the total net profit is calculated as total revenue (300 × total units sold over 6 months) minus all costs (raw materials, outsourcing, regular wages, overtime wages, inventory holding, backorder costs, hiring, and firing), with no other revenue or cost components.

## Turn 20 - Generic Agent

QUESTION: Regarding the in-house production constraint — the total in-house production in a month is limited by the total available labor hours (regular + overtime) divided by 5 hours per unit. Is there any other constraint on in-house production, such as a maximum number of units that can be produced in-house per month regardless of labor availability?

## Turn 20 - User Simulator

No, there is no other constraint on in-house production. The only limit is the total available labor hours (regular + overtime) divided by 5 hours per unit.

## Turn 21 - Generic Agent

QUESTION: Regarding the decision variables — are all quantities (workers, hires, firings, in-house production, outsourcing, inventory, backorders) required to be non-negative, and are workers, hires, and firings required to be integers (whole numbers) while production, outsourcing, inventory, and backorders can be continuous (fractional) values?

## Turn 21 - User Simulator

Yes, all quantities are required to be non-negative. Workers, hires, and firings are required to be integers (whole numbers), while production, outsourcing, inventory, and backorders can be continuous (fractional) values.

## Turn 22 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total net profit over 6 months (January–June).

**Profit = Revenue − Total Costs**
- Revenue: 300 Yuan × total units sold (delivered) over 6 months.
- Costs: raw materials (90/unit in-house), outsourcing (200/unit), regular wages (30×160×workers per month), overtime wages (40×overtime hours actually used), inventory holding (15×ending inventory each month, including June), backorder cost (35×backorder balance at end of each month, Jan–May; June backorder = 0), hiring (5,000/worker), firing (8,000/worker).

**Decision Variables:**
- Workers(t), Hires(t), Firings(t): non-negative integers, t = 1..6.
- In-house production P(t), outsourcing O(t), ending inventory I(t), backorders B(t), overtime hours OT(t): non-negative continuous, t = 1..6.

**Workforce Balance:**
- Workers(t) = Workers(t−1) + Hires(t) − Firings(t), Workers(0) = 1,000.
- No upper or lower bound on workforce size.
- Changes take effect immediately in the same month.

**Production Capacity:**
- In-house production: P(t) ≤ [Workers(t) × 160 + OT(t)] / 5
- Overtime: 0 ≤ OT(t) ≤ 20 × Workers(t)
- Outsourcing: unbounded above.

**Inventory/Backorder Balance (per month t):**
- Supply(t) = I(t−1) + P(t) + O(t), where I(0) = 15,000.
- Demand to satisfy: B(t−1) + D(t), where B(0) = 0.
- If Supply(t) ≥ B(t−1) + D(t): I(t) = Supply(t) − B(t−1) − D(t), B(t) = 0.
- If Supply(t) < B(t−1) + D(t): B(t) = B(t−1) + D(t) − Supply(t), I(t) = 0.
- Inventory and backorders cannot both be positive in the same month.

**Terminal Conditions:**
- B(6) = 0 (all demand fully satisfied by end of June).
- I(6) ≥ 10,000.

**Demand:** Jan=20,000; Feb=40,000; Mar=42,000; Apr=35,000; May=19,000; Jun=18,500.

**Integrality:** Workers, Hires, Firings are integers. All other variables are continuous.