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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean the overtime cap is 20 hours per individual worker per month (so total workforce overtime is 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

It is 20 hours per individual worker per month. So the total overtime hours allowed for the workforce in any given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you said it is paid regardless of utilization — does that mean each worker employed in a month is paid 160 hours × 30 Yuan = 4,800 Yuan for that month even if they work fewer than 160 regular hours (e.g., because production is low)?

## Turn 2 - User Simulator

Yes, that is correct. Each worker employed in a month is paid 160 hours × 30 Yuan = 4,800 Yuan for that month, regardless of how many regular hours they actually work.

## Turn 3 - Generic Agent

QUESTION: When a worker is hired or fired in a given month, does that worker count toward that month's workforce (and thus receive that month's regular wage and can work that month's overtime), or do hires/fires take effect at the start of the following month?

## Turn 3 - User Simulator

I need to confirm this internally. The original request does not specify whether hires and fires take effect in the same month or the following month.

## Turn 4 - Generic Agent

QUESTION: For the backorder cost of 35 Yuan per unit, is it charged on the number of units still unfulfilled at the end of each month (i.e., the backorder balance carried into the next month), or is it charged on the total units that were backordered during the month regardless of when they are eventually fulfilled?

## Turn 4 - User Simulator

It is charged on the number of units still unfulfilled at the end of each month — that is, the backorder balance carried into the next month.

## Turn 5 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory balance at the end of each month (including June), or only on the inventory carried into the next month (i.e., not charged on June's ending inventory)?

## Turn 5 - User Simulator

It is charged on the ending inventory balance at the end of each month, including June.

## Turn 6 - Generic Agent

QUESTION: Can the workforce be reduced below the initial 1,000 workers (i.e., are firings allowed), and is there any minimum workforce level that must be maintained in any month?

## Turn 6 - User Simulator

Yes, firings are allowed, and there is no minimum workforce level that must be maintained in any month.

## Turn 7 - Generic Agent

QUESTION: Can the workforce be increased without limit (i.e., is there any cap on the number of workers that can be hired in a month or on the total workforce size)?

## Turn 7 - User Simulator

No, there is no cap on the number of workers that can be hired in a month or on the total workforce size.

## Turn 8 - Generic Agent

QUESTION: When demand is fulfilled, is there any limit on how much of a month's demand can be satisfied by outsourced units, or can all of a month's demand (current plus backorders) be met by outsourcing if that is cheaper?

## Turn 8 - User Simulator

There is no limit on how much of a month's demand can be satisfied by outsourced units. All of a month's demand (current plus backorders) can be met by outsourcing if that is the chosen approach.

## Turn 9 - Generic Agent

QUESTION: When demand is fulfilled from previous-month inventory, current in-house production, and outsourced units, is there any required priority or order in which these sources must be used (e.g., must inventory be used before production, or production before outsourcing), or can the model freely choose how much to draw from each source?

## Turn 9 - User Simulator

There is no required priority or order. The model can freely choose how much to draw from each source (previous-month inventory, current in-house production, and outsourced units) to fulfill demand.

## Turn 10 - Generic Agent

QUESTION: Can in-house production in a month exceed that month's demand (i.e., produce extra units to build inventory for future months), or must in-house production be limited to the demand being fulfilled in that same month?

## Turn 10 - User Simulator

In-house production can exceed that month's demand. Extra units produced can be added to inventory for future months.

## Turn 11 - Generic Agent

QUESTION: Can outsourced units also be added to inventory for future months (i.e., outsource more than the current month's demand to build inventory), or are outsourced units only allowed to fulfill the current month's demand?

## Turn 11 - User Simulator

Outsourced units can also be added to inventory for future months. There is no restriction limiting outsourcing to only the current month's demand.

## Turn 12 - Generic Agent

QUESTION: Regarding the backorder mechanism: if demand in a month exceeds the total available supply (inventory + in-house production + outsourcing), the shortfall becomes a backorder. Is it possible for the model to choose to backorder units even when there is sufficient supply available (i.e., is backordering a forced consequence of insufficient supply, or is it a decision the model can make even when supply is adequate)?

## Turn 12 - User Simulator

Backordering is a forced consequence of insufficient supply. The model cannot choose to backorder units when there is sufficient supply available to meet demand.

## Turn 13 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold: is revenue recognized only when the demand is actually fulfilled (i.e., when the unit is delivered to the customer, which may be in a later month if backordered), or is revenue recognized in the month the demand originally occurred regardless of when it is fulfilled?

## Turn 13 - User Simulator

Revenue is recognized only when the demand is actually fulfilled — that is, when the unit is delivered to the customer, which may be in a later month if the order was backordered.

## Turn 14 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production: is this cost incurred in the month the unit is produced (even if it sits in inventory for future months), or is it incurred in the month the unit is actually sold/delivered to the customer?

## Turn 14 - User Simulator

The raw material cost is incurred in the month the unit is produced, even if it sits in inventory for future months.

## Turn 15 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit: is this cost incurred in the month the outsourced unit is produced/received (even if it sits in inventory for future months), or is it incurred in the month the unit is actually sold/delivered to the customer?

## Turn 15 - User Simulator

The outsourcing cost is incurred in the month the outsourced unit is produced/received, even if it sits in inventory for future months.

## Turn 16 - Generic Agent

QUESTION: Regarding the workforce timing: since you deferred confirming whether hires and fires take effect in the same month or the following month, could you clarify whether a worker hired in month t is available to work (and receives the regular wage) in month t, or only starting in month t+1?

## Turn 16 - User Simulator

I need to confirm this internally. The original request does not specify whether hires and fires take effect in the same month or the following month.

## Turn 17 - Generic Agent

QUESTION: Since the workforce timing is still being confirmed internally, for the purpose of building the model now, would you prefer I assume that hires and fires take effect immediately in the same month (i.e., a worker hired in month t works and is paid in month t, and a worker fired in month t does not work or get paid in month t), or would you prefer I assume they take effect in the following month?

## Turn 17 - User Simulator

I need to confirm this internally. The original request does not specify whether hires and fires take effect in the same month or the following month.

## Turn 18 - Generic Agent

QUESTION: Regarding the workforce timing, since this is still being confirmed internally, I will proceed with the assumption that hires and fires take effect immediately in the same month (a worker hired in month t works and is paid in month t; a worker fired in month t does not work or get paid in month t). Is there any other aspect of the problem you would like to clarify before I proceed with the model?

## Turn 18 - User Simulator

No, that assumption is fine for now. There are no other aspects I would like to clarify before you proceed with the model.

## Turn 19 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total net profit over 6 months (January–June).

**Decision Variables (per month t = 1..6):**
- Workforce level W_t (integer, ≥ 0)
- Hires H_t (integer, ≥ 0)
- Fires F_t (integer, ≥ 0)
- In-house production P_t (continuous, ≥ 0)
- Outsourcing O_t (continuous, ≥ 0)
- Ending inventory I_t (continuous, ≥ 0)
- Backorder B_t (continuous, ≥ 0)
- Units fulfilled (sold) S_t (continuous, ≥ 0)

**Workforce Dynamics:**
- W_1 = 1,000 + H_1 − F_1 (hires/fires take effect in the same month)
- W_t = W_{t−1} + H_t − F_t for t = 2..6
- H_t, F_t ≥ 0, W_t ≥ 0

**Production Capacity:**
- In-house production: P_t ≤ (160 × W_t + 20 × W_t) / 5 = 36 × W_t (each worker provides 160 regular + up to 20 overtime hours; 5 hours per unit)
- Overtime per worker ≤ 20 hours (already embedded in the 36 units/worker cap)

**Inventory/Backorder Balance:**
- I_t = I_{t−1} + P_t + O_t − S_t, with I_0 = 15,000
- S_t ≤ I_{t−1} + P_t + O_t (cannot sell more than available)
- B_t = B_{t−1} + D_t − S_t, with B_0 = 0
- Backordering is forced: if supply < demand, the shortfall is backordered (S_t = min(supply, B_{t−1} + D_t))

**Constraints:**
- I_6 ≥ 10,000 (minimum ending inventory)
- B_t ≥ 0, I_t ≥ 0 for all t
- P_t, O_t, S_t ≥ 0

**Costs and Revenue (per month t):**
- Revenue: 300 × S_t
- Raw material: 90 × P_t
- Outsourcing: 200 × O_t
- Regular wages: 4,800 × W_t (paid regardless of utilization)
- Overtime wages: 40 × (5 × P_t − 160 × W_t) if P_t > 32 × W_t, else 0 (overtime hours = max(0, 5P_t − 160W_t))
- Hiring: 5,000 × H_t
- Firing: 8,000 × F_t
- Inventory holding: 15 × I_t (including June)
- Backorder: 35 × B_t (including June's ending backorder)

**Demand:**
- Jan: 20,000; Feb: 40,000; Mar: 42,000; Apr: 35,000; May: 19,000; Jun: 18,500

**Key Assumptions Confirmed:**
- Overtime cap: 20 hours per worker per month
- Regular wage paid regardless of utilization
- Hires/fires effective in the same month
- Backorder cost on ending backorder balance each month
- Holding cost on ending inventory each month (including June)
- No minimum workforce, no cap on hiring
- No limit on outsourcing quantity
- No priority among supply sources
- Production and outsourcing can build inventory
- Backordering only when supply is insufficient
- Revenue recognized at fulfillment
- Raw material and outsourcing costs incurred at production/receipt
- No cap on workforce size