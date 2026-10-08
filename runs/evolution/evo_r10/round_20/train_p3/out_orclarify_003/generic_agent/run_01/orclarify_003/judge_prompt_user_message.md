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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a given month (so total overtime = 20 × number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime hours available in a month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, can you hire and fire workers in any month (including January), and is the workforce level for a month determined at the start of that month (so January's production capacity uses January's workforce, which equals the initial 1,000 plus any January hires minus any January fires)?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. The workforce level for a month is determined at the start of that month, so January's production capacity uses the workforce available at the start of January (initial 1,000 plus any January hires minus any January fires).

## Turn 3 - Generic Agent

QUESTION: For the inventory/backorder flow, is the standard balance equation "ending inventory minus ending backorders equals beginning inventory plus in-house production plus outsourcing minus demand" (so a month can end with either inventory or backorders, but not both), and is the 15 Yuan holding cost charged on ending inventory while the 35 Yuan backorder cost is charged on ending backorders?

## Turn 3 - User Simulator

Yes, that is correct. The standard balance equation applies: ending inventory minus ending backorders equals beginning inventory plus in-house production plus outsourcing minus demand. A month can end with either inventory or backorders, but not both. The 15 Yuan holding cost is charged on ending inventory, and the 35 Yuan backorder cost is charged on ending backorders.

## Turn 4 - Generic Agent

QUESTION: Is in-house production limited only by available labor hours (regular 160 plus overtime up to 20 per worker), with no separate machine or capacity cap, and is outsourcing unlimited in quantity?

## Turn 4 - User Simulator

Yes, in-house production is limited only by available labor hours (160 regular hours plus up to 20 overtime hours per worker), with no separate machine or capacity cap. Outsourcing is unlimited in quantity.

## Turn 5 - Generic Agent

QUESTION: Is the 10,000-unit minimum ending inventory requirement for June a hard constraint (the plan must end June with at least 10,000 units of inventory, with no backorders), or is it a soft target that can be violated at some penalty?

## Turn 5 - User Simulator

It is a hard constraint. The plan must end June with at least 10,000 units of inventory, and all backorders must be cleared by the end of June.

## Turn 6 - Generic Agent

QUESTION: For the objective, is total net profit calculated as total sales revenue (300 per unit sold) minus all costs (raw material, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), where "units sold" means units actually delivered to meet demand (including backorders fulfilled in later months)?

## Turn 6 - User Simulator

Yes, that is correct. Total net profit is calculated as total sales revenue (300 per unit sold) minus all costs (raw material, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing). "Units sold" means units actually delivered to meet demand, including backorders fulfilled in later months.

## Turn 7 - Generic Agent

QUESTION: Since all demand must eventually be fulfilled (backorders cleared by end of June), total units sold is fixed at the sum of all demand (175,500 units), making total revenue a constant. So the objective effectively reduces to minimizing total costs. Is that the correct interpretation, or should I still write the objective as revenue minus costs explicitly?

## Turn 7 - User Simulator

Yes, that is the correct interpretation. Since all demand must be fulfilled by the end of June, total units sold is fixed at 175,500 units, making total revenue a constant. The objective effectively reduces to minimizing total costs. You can write the objective as revenue minus costs explicitly, but since revenue is constant, minimizing total costs is equivalent.

## Turn 8 - Generic Agent

QUESTION: For the regular wage cost, is it simply 30 × 160 × (number of workers employed that month) = 4,800 per worker per month, paid regardless of how many hours are actually used, and is the overtime cost 40 × (actual overtime hours used that month)?

## Turn 8 - User Simulator

Yes, that is correct. The regular wage cost is 30 × 160 × (number of workers employed that month) = 4,800 per worker per month, paid regardless of how many hours are actually used. The overtime cost is 40 × (actual overtime hours used that month).

## Turn 9 - Generic Agent

QUESTION: For the inventory holding cost, is the 15 Yuan per unit charged on the ending inventory of each month (including June's ending inventory of at least 10,000 units), or is it charged only on inventory held at the end of months January through May (excluding June)?

## Turn 9 - User Simulator

The 15 Yuan per unit is charged on the ending inventory of each month, including June's ending inventory.

## Turn 10 - Generic Agent

QUESTION: For the backorder cost, is the 35 Yuan per unit charged on the ending backorders of each month (i.e., units of demand that are unfulfilled at the end of that month and carried to the next), so if a unit is backordered for two months it incurs the 35 Yuan cost in each of those two months?

## Turn 10 - User Simulator

Yes, that is correct. The 35 Yuan per unit is charged on the ending backorders of each month. If a unit is backordered for two months, it incurs the 35 Yuan cost in each of those two months.

## Turn 11 - Generic Agent

QUESTION: Are all decision variables (workforce, production, outsourcing, inventory, backorders) required to be non-negative, and do you need integer values for any of them, or can they all be continuous?

## Turn 11 - User Simulator

All decision variables (workforce, production, outsourcing, inventory, backorders) are required to be non-negative. They can all be continuous; integer values are not required.

## Turn 12 - Generic Agent

QUESTION: For the workforce balance, is the workforce at the start of month t+1 equal to the workforce at the start of month t plus hires in month t minus fires in month t, with no other constraints on workforce (e.g., no minimum workforce level, no maximum workforce level)?

## Turn 12 - User Simulator

Yes, that is correct. The workforce at the start of month t+1 equals the workforce at the start of month t plus hires in month t minus fires in month t. There are no other constraints on workforce, such as a minimum or maximum workforce level.

## Turn 13 - Generic Agent

QUESTION: For the in-house production constraint, is the total labor hours used for in-house production in a month (5 × in-house units) required to be less than or equal to the total available hours (160 × workers + overtime hours used), where overtime hours used is a separate decision variable bounded above by 20 × workers?

## Turn 13 - User Simulator

Yes, that is correct. The total labor hours used for in-house production in a month (5 × in-house units) must be less than or equal to the total available hours (160 × workers + overtime hours used), where overtime hours used is a separate decision variable bounded above by 20 × workers.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that limits the total units that can be fulfilled in a month (i.e., the sum of units drawn from beginning inventory, in-house production, and outsourcing to meet that month's demand plus prior backorders), or is fulfillment limited only by the inventory balance equation and the production capacity constraint?

## Turn 14 - User Simulator

There is no separate constraint limiting the total units that can be fulfilled in a month. Fulfillment is limited only by the inventory balance equation and the production capacity constraint.

## Turn 15 - Generic Agent

QUESTION: For the initial conditions, is the beginning inventory of January 15,000 units and the beginning workforce of January 1,000 workers, with no beginning backorders in January (i.e., backorders at the start of January are zero)?

## Turn 15 - User Simulator

Yes, that is correct. The beginning inventory of January is 15,000 units, the beginning workforce of January is 1,000 workers, and there are no beginning backorders in January (backorders at the start of January are zero).

## Turn 16 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Problem:** Production and workforce planning for a foldable tables company over 6 months (January–June), maximizing net profit (equivalently, minimizing total costs since revenue is fixed at 300 × 175,500 = 52,650,000 Yuan).

**Decision Variables (all continuous, non-negative):**
- W_t: workforce at start of month t (t = 1..6)
- H_t: hires in month t
- F_t: fires in month t
- P_t: in-house production units in month t
- O_t: outsourced units in month t
- OT_t: overtime hours used in month t
- I_t: ending inventory at end of month t
- B_t: ending backorders at end of month t

**Parameters:**
- Initial workforce: W_1 = 1,000
- Initial inventory: I_0 = 15,000; B_0 = 0
- Demand: [20,000; 40,000; 42,000; 35,000; 19,000; 18,500]
- Sales price: 300/unit (constant revenue)
- Raw material cost: 90/unit (in-house only)
- Outsourcing cost: 200/unit
- Holding cost: 15/unit/month (on ending inventory, all 6 months)
- Backorder cost: 35/unit/month (on ending backorders, all 6 months)
- Labor: 5 hours/unit in-house
- Regular hours: 160/worker/month; wage: 30/hr → 4,800/worker/month
- Overtime: max 20 hrs/worker/month; wage: 40/hr
- Hiring cost: 5,000/worker
- Firing cost: 8,000/worker

**Constraints:**
1. Workforce balance: W_{t+1} = W_t + H_t − F_t (t = 1..5)
2. Production capacity: 5·P_t ≤ 160·W_t + OT_t (t = 1..6)
3. Overtime cap: OT_t ≤ 20·W_t (t = 1..6)
4. Inventory balance: I_t − B_t = I_{t−1} + P_t + O_t − D_t (t = 1..6)
5. Non-negativity: I_t ≥ 0, B_t ≥ 0 (mutually exclusive by balance equation)
6. June ending inventory: I_6 ≥ 10,000
7. June backorders cleared: B_6 = 0

**Objective (minimize total cost):**
Σ_t [90·P_t + 200·O_t + 15·I_t + 35·B_t + 4,800·W_t + 40·OT_t + 5,000·H_t + 8,000·F_t]

(Equivalently: maximize 52,650,000 − total cost.)