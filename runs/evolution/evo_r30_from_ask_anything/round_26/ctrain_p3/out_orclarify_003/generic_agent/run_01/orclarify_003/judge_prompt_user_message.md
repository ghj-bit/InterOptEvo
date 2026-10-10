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

QUESTION: Is the 10,000-unit minimum ending inventory requirement for June only, or must the ending inventory be at least 10,000 units at the end of every month from January through June?

## Turn 1 - User Simulator

It is only for the end of June. The 10,000-unit minimum ending inventory requirement applies specifically to the end of June, not to the end of every month from January through June.

## Turn 2 - Generic Agent

QUESTION: Can the workforce size change from month to month through hiring and firing, or is the workforce fixed at 1,000 employees for the entire six-month period?

## Turn 2 - User Simulator

The workforce size can change from month to month through hiring and firing. It is not fixed at 1,000 employees for the entire period.

## Turn 3 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work up to 20 overtime hours per month, or is there a single aggregate cap of 20 total overtime hours across all workers combined in a month?

## Turn 3 - User Simulator

Each individual worker can work up to 20 overtime hours per month.

## Turn 4 - Generic Agent

QUESTION: Is there a limit on the number of units that can be outsourced in any given month, or is the outsourcing quantity unlimited as long as the 200 Yuan per unit cost is paid?

## Turn 4 - User Simulator

I don't have a specific limit on the number of units that can be outsourced in any given month. The outsourcing quantity is not capped, as long as the 200 Yuan per unit cost is paid.

## Turn 5 - Generic Agent

QUESTION: Is there a maximum number of workers that can be hired or fired in any single month, or are hiring and firing quantities unlimited as long as the per-worker costs are paid?

## Turn 5 - User Simulator

I don't have a specific limit on the number of workers that can be hired or fired in any single month. Hiring and firing quantities are not capped, as long as the per-worker costs are paid.

## Turn 6 - Generic Agent

QUESTION: Are the monthly demand figures (20,000, 40,000, etc.) hard requirements that must be fully satisfied by the end of June, or are they targets where unmet demand can simply be lost without penalty?

## Turn 6 - User Simulator

The monthly demand figures are hard requirements. Unfulfilled demand is back-ordered and must be met in subsequent months. All backorders must be cleared by the end of June, so no demand can be lost without penalty.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum number of units that can be held in inventory at the end of any month, or is inventory capacity unlimited?

## Turn 7 - User Simulator

I don't have a specific limit on the number of units that can be held in inventory at the end of any month. Inventory capacity is not capped.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum number of workers the company can have at the end of any month, or is the workforce size unlimited as long as hiring and firing costs are paid?

## Turn 8 - User Simulator

I don't have a specific limit on the maximum number of workers the company can have at the end of any month. The workforce size is not capped, as long as hiring and firing costs are paid.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about, such as minimum workforce levels, production capacity limits, or restrictions on how many units can be produced in-house per month?

## Turn 9 - User Simulator

No, there are no other constraints or requirements beyond what has already been specified. There are no minimum workforce levels, no production capacity limits beyond the labor hours available (160 regular + up to 20 overtime per worker), and no separate restrictions on how many units can be produced in-house per month other than those labor hour limits.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total net profit over six months (January–June).

**Decision Variables (per month, t = 1 to 6):**
- Workforce size (integer, non-negative)
- Number of workers hired (integer, non-negative)
- Number of workers fired (integer, non-negative)
- In-house production units (continuous or integer, non-negative)
- Outsourced units (continuous or integer, non-negative)
- Ending inventory (continuous or integer, non-negative)
- Backorders carried forward (continuous or integer, non-negative)
- Overtime hours used (continuous, non-negative)

**Parameters (Confirmed):**
- Initial workforce: 1,000 employees
- Initial inventory: 15,000 units
- Sales price: 300 Yuan/unit
- Raw material cost: 90 Yuan/unit (in-house only)
- Outsourcing cost: 200 Yuan/unit (all-inclusive)
- Inventory holding cost: 15 Yuan/unit/month (end-of-month)
- Backorder cost: 35 Yuan/unit/month
- Labor requirement: 5 hours/unit (in-house)
- Regular hours: 160 hours/worker/month
- Regular wage: 30 Yuan/hour (paid regardless of utilization)
- Overtime wage: 40 Yuan/hour
- Max overtime: 20 hours/worker/month
- Hiring cost: 5,000 Yuan/worker
- Firing cost: 8,000 Yuan/worker
- Demand: Jan=20,000; Feb=40,000; Mar=42,000; Apr=35,000; May=19,000; Jun=18,500

**Constraints (Confirmed):**
1. **Workforce balance:** Workforce_t = Workforce_{t-1} + Hires_t - Fires_t
2. **Labor capacity:** 5 × In-house Production_t ≤ 160 × Workforce_t + Overtime_t
3. **Overtime cap:** Overtime_t ≤ 20 × Workforce_t
4. **Inventory/backorder flow:** Inventory_t = Inventory_{t-1} + In-house Production_t + Outsourced_t − Demand_t + Backorders_{t-1} − Backorders_t (equivalently, supply meets demand plus backorder changes)
5. **June ending inventory:** Inventory_6 ≥ 10,000
6. **All backorders cleared by end of June:** Backorders_6 = 0
7. **Non-negativity:** All decision variables ≥ 0
8. **Integrality:** Workforce, hires, fires are integers; production and outsourcing quantities may be continuous (assumed)

**Assumptions (Flagged):**
- Production and outsourcing quantities are treated as continuous (not required to be integer). If integer units are required, this can be adjusted.
- No other hidden constraints exist (confirmed by user).