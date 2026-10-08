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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a given month (so total overtime is bounded by 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at a fixed 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime hours for the month are bounded by 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding the workforce, can the number of workers change from month to month (i.e., can you hire or fire workers in any month, with the 5,000 Yuan hiring cost and 8,000 Yuan firing cost applying to each change), or is the workforce fixed at 1,000 for all six months?

## Turn 2 - User Simulator

The workforce can change from month to month. You can hire or fire workers in any month, with the 5,000 Yuan hiring cost and 8,000 Yuan firing cost applying to each change.

## Turn 3 - Generic Agent

QUESTION: When you say "orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," do you mean that in each month, the total units available to satisfy that month's demand (including any backorders from prior months) come from the sum of: (1) ending inventory carried over from the previous month, (2) in-house production in the current month, and (3) outsourced units in the current month — and any shortfall becomes a new backorder carried to the next month?

## Turn 3 - User Simulator

Yes, that is correct. In each month, the total units available to satisfy that month's demand (including any backorders from prior months) come from the sum of: (1) ending inventory carried over from the previous month, (2) in-house production in the current month, and (3) outsourced units in the current month. Any shortfall becomes a new backorder carried to the next month.

## Turn 4 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit — is this charged on the ending inventory of each month (i.e., the units remaining at the end of January, end of February, etc.), and does it apply to all six months including June?

## Turn 4 - User Simulator

Yes, the 15 Yuan per unit inventory holding cost is charged on the ending inventory of each month, and it applies to all six months, including June.

## Turn 5 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit — is this charged on the number of units that are backordered at the end of each month (i.e., the unfulfilled demand carried from that month to the next), and does it apply to all six months including June (meaning if there is still unfulfilled demand at the end of June, it incurs a cost)?

## Turn 5 - User Simulator

The 35 Yuan per unit backorder cost is charged on the number of units backordered at the end of each month. However, it does not apply to June, because all backorders must be cleared by the end of June. There can be no unfulfilled demand remaining after June.

## Turn 6 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for 160 hours per worker, paid regardless of utilization — does this mean that in each month, every worker on the roster is paid 160 × 30 = 4,800 Yuan in regular wages, even if the total in-house production that month requires fewer labor hours than 160 times the number of workers?

## Turn 6 - User Simulator

Yes, that is correct. In each month, every worker on the roster is paid 160 × 30 = 4,800 Yuan in regular wages, even if the total in-house production that month requires fewer labor hours than 160 times the number of workers.

## Turn 7 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is this revenue earned for every unit that is actually delivered to the customer (i.e., demand that is fulfilled in the month it was due or in a later month via backorder fulfillment), and does it apply to all units sold across all six months?

## Turn 7 - User Simulator

Yes, the 300 Yuan per unit sales price is revenue earned for every unit that is actually delivered to the customer, whether fulfilled in the month it was due or in a later month via backorder fulfillment. It applies to all units sold across all six months.

## Turn 8 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit applicable only to in-house production — does the outsourced unit at 200 Yuan per unit already include all material and labor costs (i.e., no additional raw material cost is incurred for outsourced units), so the only cost for an outsourced unit is the 200 Yuan?

## Turn 8 - User Simulator

Yes, the 200 Yuan per unit outsourcing cost is all-inclusive. No additional raw material cost is incurred for outsourced units. The only cost for an outsourced unit is the 200 Yuan.

## Turn 9 - Generic Agent

QUESTION: Regarding the workforce constraint — is there a minimum number of workers that must be maintained in any month (e.g., you cannot fire all workers), or can the workforce theoretically drop to zero in any month?

## Turn 9 - User Simulator

There is no minimum number of workers that must be maintained in any month. The workforce can theoretically drop to zero in any month.

## Turn 10 - Generic Agent

QUESTION: Regarding the ending inventory requirement of at least 10,000 units at the end of June — does this 10,000 units need to be in physical inventory (i.e., not backordered), meaning that after all demand through June is satisfied, at least 10,000 units must remain in stock?

## Turn 10 - User Simulator

Yes, the 10,000 units must be in physical inventory at the end of June. After all demand through June is satisfied, at least 10,000 units must remain in stock.

## Turn 11 - Generic Agent

QUESTION: Regarding the labor hours constraint — the total in-house production in a month requires 5 hours per unit, and each worker provides 160 regular hours plus up to 20 overtime hours (180 total). Does this mean the total in-house production in a month is limited to (180 × number of workers) / 5 units, or is there a separate constraint that regular hours must be used before overtime hours (i.e., you cannot use overtime hours unless all regular hours are already fully utilized)?

## Turn 11 - User Simulator

The total in-house production in a month is limited to (180 × number of workers) / 5 units. There is no separate constraint requiring that regular hours must be used before overtime hours.

## Turn 12 - Generic Agent

QUESTION: Regarding the workforce transition — when you hire or fire workers in a given month, does the workforce level used for that month's production capacity and wage calculation reflect the workforce after hiring/firing in that same month (i.e., the end-of-month workforce), or does it reflect the workforce at the start of the month (before any hiring/firing that month)?

## Turn 12 - User Simulator

The workforce level used for that month's production capacity and wage calculation reflects the workforce after hiring/firing in that same month (i.e., the end-of-month workforce).

## Turn 13 - Generic Agent

QUESTION: Regarding the backorder cost — you confirmed it is charged on units backordered at the end of each month for January through May. If, for example, 5,000 units are backordered at the end of January and then 3,000 of those are fulfilled in February (leaving 2,000 still backordered at the end of February), is the backorder cost for February based on the 2,000 units still unfulfilled at the end of February, or is it based on the 5,000 units that were originally backordered from January?

## Turn 13 - User Simulator

The backorder cost for February is based on the 2,000 units still unfulfilled at the end of February. The cost is charged on the number of units backordered at the end of each month, not on the original backorder quantity from a prior month.

## Turn 14 - Generic Agent

QUESTION: Regarding the inventory balance — if in a given month, the total available units (beginning inventory + in-house production + outsourced units) exceed the total demand to be fulfilled that month (current demand + prior backorders), the excess becomes ending inventory. Is it possible to have both positive ending inventory and positive backorders in the same month, or must one be zero whenever the other is positive?

## Turn 14 - User Simulator

It is not possible to have both positive ending inventory and positive backorders in the same month. One must be zero whenever the other is positive.

## Turn 15 - Generic Agent

QUESTION: Regarding the demand fulfillment priority — when backorders from prior months exist alongside current month demand, are backorders fulfilled first (before current month demand), or can the company choose to fulfill current month demand first and let backorders wait further?

## Turn 15 - User Simulator

The company can choose to fulfill current month demand first and let backorders wait further. There is no requirement that backorders must be fulfilled before current month demand.

## Turn 16 - Generic Agent

QUESTION: Regarding the net profit objective — is the total net profit calculated as total revenue (300 × total units delivered) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing) over the six-month period, with no other revenue or cost components?

## Turn 16 - User Simulator

Yes, the total net profit is calculated as total revenue (300 × total units delivered) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing) over the six-month period, with no other revenue or cost components.

## Turn 17 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total net profit over January–June.

**Net Profit = Total Revenue − Total Costs**
- Revenue: 300 Yuan × total units delivered (all demand fulfilled by end of June).
- Costs: raw materials (90/unit, in-house only), outsourcing (200/unit, all-inclusive), inventory holding (15/unit/month on ending inventory, all 6 months), backorder (35/unit/month on units backordered at end of month, Jan–May only), regular wages (4,800/worker/month, paid regardless of utilization), overtime wages (40/hour), hiring (5,000/worker), firing (8,000/worker).

**Decision Variables (per month t = 1..6):**
- W_t: workforce at end of month t (integer, ≥ 0)
- P_t: in-house production (units, ≥ 0)
- O_t: outsourced units (units, ≥ 0)
- I_t: ending inventory (units, ≥ 0)
- B_t: ending backorders (units, ≥ 0)
- OT_t: total overtime hours used in month t (≥ 0)
- H_t: workers hired in month t (integer, ≥ 0)
- F_t: workers fired in month t (integer, ≥ 0)

**Key Constraints:**
1. **Workforce balance:** W_t = W_{t−1} + H_t − F_t, with W_0 = 1,000.
2. **Production capacity:** 5 × P_t ≤ 160 × W_t + OT_t, and OT_t ≤ 20 × W_t.
3. **Inventory/backorder balance:** I_t = I_{t−1} + P_t + O_t − (D_t + B_{t−1} − B_t), with I_0 = 15,000, B_0 = 0.
4. **Mutual exclusivity:** I_t × B_t = 0 (cannot have both positive inventory and backorders in the same month).
5. **Backorder clearance:** B_6 = 0 (all demand must be fulfilled by end of June).
6. **Ending inventory:** I_6 ≥ 10,000.
7. **No simultaneous inventory and backorders** (enforced via binary or big-M).

**Parameters:**
- Demand: Jan 20,000; Feb 40,000; Mar 42,000; Apr 35,000; May 19,000; Jun 18,500.
- Initial workforce: 1,000; Initial inventory: 15,000.
- Regular hours: 160/worker/month; Max overtime: 20/worker/month.
- Labor: 5 hours/unit in-house.
- Regular wage: 30/hour (4,800/worker/month); Overtime wage: 40/hour.
- Hiring: 5,000/worker; Firing: 8,000/worker.
- Raw material: 90/unit (in-house only); Outsourcing: 200/unit (all-inclusive).
- Holding: 15/unit/month; Backorder: 35/unit/month (Jan–May only).