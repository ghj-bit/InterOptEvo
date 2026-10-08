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

QUESTION: When you say the total overtime hours per month for the entire workforce cannot exceed 20 hours per worker, do you mean the overtime cap is 20 hours per individual worker per month (so total overtime is at most 20 times the number of workers employed that month), or is it a single company-wide cap of 20 total overtime hours per month?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime hours allowed in a given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the workforce, is the number of workers employed in a given month the level at the start of that month (before any hiring/firing that month), and do hiring and firing decisions happen at the start of each month so that the new workers are available for that month's production?

## Turn 2 - User Simulator

Yes, hiring and firing decisions happen at the start of each month, and the resulting workforce level is available for that month's production.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered, is the backorder cost of 35 Yuan per unit charged once for the month the demand is unfulfilled, and then charged again in each subsequent month the units remain unfulfilled until they are finally delivered?

## Turn 3 - User Simulator

Yes, the 35 Yuan per unit backorder cost is charged for each month the units remain unfulfilled until they are finally delivered.

## Turn 4 - Generic Agent

QUESTION: When back-ordered units are finally delivered in a later month, do they still generate the full 300 Yuan sales price per unit, just like units sold in the month their demand originally arose?

## Turn 4 - User Simulator

Yes, back-ordered units generate the full 300 Yuan sales price per unit when they are finally delivered.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how many units can be outsourced in a given month, or can you outsource any non-negative number of finished tables each month?

## Turn 5 - User Simulator

There is no limit on the number of units that can be outsourced in a given month. You can outsource any non-negative number of finished tables each month.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how many workers can be hired or fired in a single month, or can you change the workforce by any non-negative amount each month?

## Turn 6 - User Simulator

There is no limit on how many workers can be hired or fired in a single month. You can change the workforce by any non-negative amount each month.

## Turn 7 - Generic Agent

QUESTION: Is there a minimum number of workers that must be kept on staff at the end of June, or can the workforce be reduced to any non-negative level by then?

## Turn 7 - User Simulator

There is no minimum number of workers that must be kept on staff at the end of June. The workforce can be reduced to any non-negative level by then.

## Turn 8 - Generic Agent

QUESTION: For the 15 Yuan per unit inventory holding cost, is it charged on the ending inventory of each month including June, or only on the ending inventory of January through May (excluding June)?

## Turn 8 - User Simulator

The 15 Yuan per unit inventory holding cost is charged on the ending inventory of each month, including June.

## Turn 9 - Generic Agent

QUESTION: Can the ending inventory at the end of any month be negative, or must inventory always be non-negative with unmet demand tracked separately as backorders?

## Turn 9 - User Simulator

Inventory must always be non-negative. Unmet demand is tracked separately as backorders.

## Turn 10 - Generic Agent

QUESTION: When fulfilling a month's total orders (current demand plus prior backorders), is there any required priority on which source is used first (e.g., must use prior inventory before current production before outsourcing), or can the model freely mix the three sources as long as the total equals the orders fulfilled?

## Turn 10 - User Simulator

There is no required priority. The model can freely mix prior inventory, current in-house production, and outsourced units as long as the total equals the orders fulfilled.

## Turn 11 - Generic Agent

QUESTION: Is the regular wage of 30 Yuan per hour for the 160 regular hours per worker paid for every worker employed in a month regardless of how many hours they actually work, meaning the regular labor cost is simply 30 times 160 times the number of workers each month?

## Turn 11 - User Simulator

Yes, the regular labor cost is simply 30 times 160 times the number of workers employed each month, paid regardless of actual utilization.

## Turn 12 - Generic Agent

QUESTION: Are the workforce levels and production quantities required to be whole numbers (integer units and whole workers), or can they be treated as continuous values?

## Turn 12 - User Simulator

The workforce levels and production quantities can be treated as continuous values.

## Turn 13 - Generic Agent

QUESTION: Is the 90 Yuan raw material cost applied only to in-house produced units, and is there no raw material cost for outsourced units (since outsourcing is all-inclusive at 200 Yuan)?

## Turn 13 - User Simulator

Yes, the 90 Yuan raw material cost applies only to in-house produced units. There is no separate raw material cost for outsourced units, as the 200 Yuan outsourcing cost is all-inclusive.

## Turn 14 - Generic Agent

QUESTION: For the labor hours constraint, is the total labor hours available in a month equal to 160 times the number of workers plus 20 times the number of workers (i.e., 180 hours per worker max), and must in-house production hours (5 times in-house units) be less than or equal to this total?

## Turn 14 - User Simulator

Yes, the total labor hours available in a month is 160 times the number of workers plus 20 times the number of workers (i.e., 180 hours per worker max). In-house production hours (5 times in-house units) must be less than or equal to this total.

## Turn 15 - Generic Agent

QUESTION: Is the overtime cost of 40 Yuan per hour charged only for the actual overtime hours used (i.e., the portion of in-house production hours that exceeds 160 times the number of workers), or is it charged for all hours up to the 20-hour overtime cap per worker?

## Turn 15 - User Simulator

The overtime cost of 40 Yuan per hour is charged only for the actual overtime hours used, which is the portion of in-house production hours that exceeds 160 times the number of workers.

## Turn 16 - Generic Agent

QUESTION: Is the backorder at the end of June allowed to be non-zero, or must all backorders be cleared by the end of June (i.e., ending backorder in June must be zero)?

## Turn 16 - User Simulator

All backorders must be cleared by the end of June. The ending backorder in June must be zero.

## Turn 17 - Generic Agent

QUESTION: Is the 10,000 unit minimum ending inventory at the end of June in addition to clearing all backorders, meaning both conditions must hold simultaneously (ending inventory at least 10,000 AND ending backorder equals zero)?

## Turn 17 - User Simulator

Yes, both conditions must hold simultaneously: the ending inventory at the end of June must be at least 10,000 units, and the ending backorder must be zero.

## Turn 18 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total net profit over January–June.

**Time horizon:** 6 months (Jan–Jun).

**Decision variables (continuous, non-negative):**
- Workforce level W_t at start of each month t (after hiring/firing that month).
- Hiring H_t and firing F_t each month (W_t = W_{t-1} + H_t - F_t, W_0 = 1000).
- In-house production P_t each month.
- Outsourcing O_t each month (unbounded above).
- Ending inventory I_t each month (I_0 = 15,000).
- Ending backorder B_t each month (B_0 = 0).
- Overtime hours OT_t each month.

**Demand (units):** Jan 20,000; Feb 40,000; Mar 42,000; Apr 35,000; May 19,000; Jun 18,500.

**Flow balance each month t:**
I_{t-1} + P_t + O_t = D_t + (B_t - B_{t-1}) + I_t
i.e., prior inventory + current in-house + outsourced = current demand + change in backorders + ending inventory.
Equivalently: I_t = I_{t-1} + P_t + O_t - D_t - B_t + B_{t-1}, with I_t ≥ 0, B_t ≥ 0.

**Labor constraint each month:**
- Regular hours available: 160 × W_t.
- Overtime hours OT_t ≥ 0, with OT_t ≤ 20 × W_t.
- In-house production hours: 5 × P_t ≤ 160 × W_t + OT_t.

**Workforce:**
- W_0 = 1,000.
- W_t = W_{t-1} + H_t - F_t, H_t, F_t ≥ 0, no per-month cap.
- No minimum workforce at end of June.

**End-of-horizon constraints:**
- I_6 ≥ 10,000.
- B_6 = 0.

**Costs and revenues (per month t):**
- Revenue: 300 × (units delivered in month t) = 300 × (D_t + B_{t-1} - B_t). Back-ordered units earn full 300 when delivered.
- Raw material: 90 × P_t (in-house only).
- Outsourcing: 200 × O_t (all-inclusive, no raw material on top).
- Regular labor: 30 × 160 × W_t = 4,800 × W_t (paid regardless of utilization).
- Overtime labor: 40 × OT_t (only actual overtime hours used).
- Inventory holding: 15 × I_t (each month including June).
- Backorder: 35 × B_t (each month the units remain unfulfilled, including June if any — but B_6 = 0 so no June backorder cost).
- Hiring: 5,000 × H_t.
- Firing: 8,000 × F_t.

**Net profit = Total revenue − Total costs.**

All variables continuous and non-negative. No integrality requirements.