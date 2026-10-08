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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a given month (so total overtime is 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime hours for the month are 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you said it is "paid regardless of utilization" — does this mean the company pays 30 Yuan/hour × 160 hours × (number of workers that month) every month even if those hours are not fully used for production, so the regular labor cost is simply 48,000 Yuan per worker per month no matter how much is actually produced in-house?

## Turn 2 - User Simulator

Yes, that is correct. The regular labor cost is 48,000 Yuan per worker per month, paid regardless of how many hours are actually used for production.

## Turn 3 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does this mean that in each month the total units available to meet that month's demand (plus any backorders carried in) are: beginning inventory + in-house production + outsourcing, and any shortfall becomes a backorder carried to the next month — i.e., there is no limit on how much can be back-ordered in any given month?

## Turn 3 - User Simulator

Yes, that is correct. In each month, the total units available to meet demand (plus any backorders carried in) are beginning inventory plus in-house production plus outsourced units. Any shortfall becomes a backorder carried to the next month, and there is no limit on how much can be back-ordered in any given month.

## Turn 4 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June — does this 10,000 units need to be on hand after fulfilling June's demand (i.e., it is additional to whatever is needed to cover June's 18,500 units of demand), or does it mean the total inventory at the end of June must be at least 10,000 units including whatever is used to satisfy June's demand?

## Turn 4 - User Simulator

The 10,000 units must be on hand after fulfilling June's demand. It is additional to whatever is needed to cover June's 18,500 units of demand.

## Turn 5 - Generic Agent

QUESTION: Regarding hiring and firing — can the workforce change by any integer amount each month (i.e., you can hire or fire any number of workers in any month), and is the workforce at the start of January fixed at 1,000 with no hiring or firing allowed before January production begins?

## Turn 5 - User Simulator

Yes, the workforce can change by any integer amount each month. The workforce at the start of January is fixed at 1,000, and no hiring or firing is allowed before January production begins.

## Turn 6 - Generic Agent

QUESTION: When a worker is hired or fired in a given month, does that change take effect for that same month's production (i.e., the new worker can contribute hours in the month they are hired, and a fired worker is no longer available for that month's production), or does the change take effect starting the next month?

## Turn 6 - User Simulator

The change takes effect for that same month's production. A new worker can contribute hours in the month they are hired, and a fired worker is no longer available for that month's production.

## Turn 7 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit — does this apply only to in-house production, or does it also apply to outsourced units (i.e., is the 200 Yuan outsourcing cost truly all-inclusive with no additional raw material cost on top)?

## Turn 7 - User Simulator

The 90 Yuan raw material cost applies only to in-house production. The 200 Yuan outsourcing cost is all-inclusive, with no additional raw material cost on top.

## Turn 8 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is revenue recognized in the month the unit is actually delivered to the customer (i.e., when the demand is fulfilled, which could be a later month if back-ordered), or is it recognized in the month the demand was originally placed?

## Turn 8 - User Simulator

Revenue is recognized in the month the unit is actually delivered to the customer, which is when the demand is fulfilled. If demand is back-ordered, revenue is recognized in the later month when the unit is delivered.

## Turn 9 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit — is this charged on the ending inventory of each month (i.e., the units remaining after fulfilling that month's demand), and does it also apply to the 10,000 units that must be on hand at the end of June?

## Turn 9 - User Simulator

Yes, the 15 Yuan per unit holding cost is charged on the ending inventory of each month, which is the units remaining after fulfilling that month's demand. This includes the 10,000 units that must be on hand at the end of June.

## Turn 10 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit — is this charged on the number of units that are back-ordered at the end of each month (i.e., the unfulfilled demand carried into the next month), and does this cost apply to all months including June (even though June's backorders would need to be fulfilled in July or later, outside the planning horizon)?

## Turn 10 - User Simulator

Yes, the 35 Yuan per unit backorder cost is charged on the number of units back-ordered at the end of each month. However, all backorders must be cleared by the end of June, so there are no backorders at the end of June.

## Turn 11 - Generic Agent

QUESTION: You mentioned that all backorders must be cleared by the end of June — does this mean that the total units delivered by the end of June must equal the total demand over all six months (20,000 + 40,000 + 42,000 + 35,000 + 19,000 + 18,500 = 174,500 units), in addition to the 10,000 units of ending inventory, so the total units that must be produced or sourced over the six months is at least 184,500 units?

## Turn 11 - User Simulator

Yes, that is correct. The total units delivered by the end of June must equal the total demand over all six months (174,500 units), and the ending inventory at the end of June must be at least 10,000 units. Therefore, the total units that must be produced or sourced over the six months is at least 184,500 units.

## Turn 12 - Generic Agent

QUESTION: Regarding the workforce — is the number of workers in each month required to be an integer (whole number of workers), or can it be treated as a continuous variable in the model?

## Turn 12 - User Simulator

The number of workers in each month must be an integer (whole number of workers).

## Turn 13 - Generic Agent

QUESTION: Regarding the production and outsourcing decisions — must the number of units produced in-house and the number of units outsourced in each month be integers, or can they be treated as continuous variables?

## Turn 13 - User Simulator

The number of units produced in-house and the number of units outsourced in each month must be integers.

## Turn 14 - Generic Agent

QUESTION: Regarding the backorder variable — must the number of units back-ordered at the end of each month be an integer, or can it be treated as a continuous variable?

## Turn 14 - User Simulator

The number of units back-ordered at the end of each month must be an integer.

## Turn 15 - Generic Agent

QUESTION: Regarding the inventory variable — must the ending inventory at the end of each month be an integer, or can it be treated as a continuous variable?

## Turn 15 - User Simulator

The ending inventory at the end of each month must be an integer.

## Turn 16 - Generic Agent

QUESTION: Regarding the overtime hours — must the total overtime hours used in each month be an integer, or can they be treated as a continuous variable (since hours can be fractional)?

## Turn 16 - User Simulator

The total overtime hours used in each month can be treated as a continuous variable, since hours can be fractional.

## Turn 17 - Generic Agent

QUESTION: Regarding the regular hours used for production — must the total regular hours used in each month be an integer, or can they also be treated as a continuous variable?

## Turn 17 - User Simulator

The total regular hours used in each month can be treated as a continuous variable, since hours can be fractional.

## Turn 18 - Generic Agent

QUESTION: Regarding the objective function — is the total net profit calculated as total revenue minus all costs (raw materials, outsourcing, regular wages, overtime wages, inventory holding, backorder costs, hiring, and firing) over the six-month period, with no other costs or constraints I haven't covered?

## Turn 18 - User Simulator

Yes, the total net profit is calculated as total revenue minus all costs (raw materials, outsourcing, regular wages, overtime wages, inventory holding, backorder costs, hiring, and firing) over the six-month period. There are no other costs or constraints beyond what has been covered.

## Turn 19 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Planning Horizon:** 6 months (January through June).

**Objective:** Maximize total net profit over the 6 months = Total Revenue − (Raw Material Cost + Outsourcing Cost + Regular Wage Cost + Overtime Wage Cost + Inventory Holding Cost + Backorder Cost + Hiring Cost + Firing Cost).

**Decision Variables (per month t = 1..6):**
- W_t: number of workers (integer, ≥ 0)
- P_t: units produced in-house (integer, ≥ 0)
- O_t: units outsourced (integer, ≥ 0)
- I_t: ending inventory (integer, ≥ 0)
- B_t: ending backorders (integer, ≥ 0)
- H_t: number of workers hired (integer, ≥ 0)
- F_t: number of workers fired (integer, ≥ 0)
- OT_t: total overtime hours used (continuous, ≥ 0)
- RH_t: total regular hours used (continuous, ≥ 0)

**Key Parameters:**
- Initial workforce (start of Jan): 1,000
- Initial inventory (start of Jan): 15,000
- Sales price: 300 Yuan/unit (revenue recognized in month of delivery)
- Raw material cost: 90 Yuan/unit (in-house only)
- Outsourcing cost: 200 Yuan/unit (all-inclusive)
- Inventory holding cost: 15 Yuan/unit/month (on ending inventory)
- Backorder cost: 35 Yuan/unit/month (on ending backorders)
- Labor per in-house unit: 5 hours
- Regular hours per worker per month: 160
- Regular wage: 30 Yuan/hour → 48,000 Yuan/worker/month (paid regardless of utilization)
- Overtime wage: 40 Yuan/hour
- Max overtime per worker per month: 20 hours
- Hiring cost: 5,000 Yuan/worker
- Firing cost: 8,000 Yuan/worker
- Demand: Jan=20,000; Feb=40,000; Mar=42,000; Apr=35,000; May=19,000; Jun=18,500

**Key Constraints:**
1. **Workforce balance:** W_t = W_{t−1} + H_t − F_t, with W_0 = 1,000. H_t and F_t cannot both be positive in the same month (or equivalently, W_t ≥ 0 and the model handles it naturally).
2. **Production capacity:** 5 × P_t ≤ RH_t + OT_t, where RH_t ≤ 160 × W_t and OT_t ≤ 20 × W_t.
3. **Inventory/backorder balance:** I_t = I_{t−1} + P_t + O_t − (D_t + B_{t−1}) + B_t, with I_0 = 15,000 and B_0 = 0. Equivalently: I_t + B_{t−1} + P_t + O_t = D_t + B_t + I_t.
4. **No backorders at end of June:** B_6 = 0.
5. **Ending inventory:** I_6 ≥ 10,000.
6. **Non-negativity and integrality** as specified above.

**Cost Structure per month:**
- Regular wages: 48,000 × W_t
- Overtime wages: 40 × OT_t
- Raw materials: 90 × P_t
- Outsourcing: 200 × O_t
- Holding: 15 × I_t
- Backorder: 35 × B_t
- Hiring: 5,000 × H_t
- Firing: 8,000 × F_t

**Revenue per month:** 300 × (D_t + B_{t−1}) [units delivered in month t = current demand + prior backorders fulfilled]

This gives a complete mixed-integer linear program (MILP) formulation.