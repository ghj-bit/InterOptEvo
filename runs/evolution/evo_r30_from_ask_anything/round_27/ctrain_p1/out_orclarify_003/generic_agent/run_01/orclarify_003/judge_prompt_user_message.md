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

QUESTION: Is the 20-hour overtime limit a total cap for the entire workforce per month, or is it a limit of 20 hours for each individual worker per month?

## Turn 1 - User Simulator

It is a limit of 20 hours for each individual worker per month.

## Turn 2 - Generic Agent

QUESTION: Is the 10,000-unit minimum ending inventory requirement a hard constraint that must be strictly satisfied, or is it a soft target that can be violated if a penalty is paid?

## Turn 2 - User Simulator

It is a hard constraint that must be strictly satisfied.

## Turn 3 - Generic Agent

QUESTION: Is the 15,000-unit initial inventory at the start of January available to fulfill January demand, or is it reserved for other purposes?

## Turn 3 - User Simulator

It is available to fulfill January demand.

## Turn 4 - Generic Agent

QUESTION: Is the 1,000-employee initial workforce at the start of January the number of workers available for production in January, or is it a baseline that can be adjusted before January production begins?

## Turn 4 - User Simulator

It is the number of workers available for production in January.

## Turn 5 - Generic Agent

QUESTION: Is the 300 Yuan sales price per unit applied to all units sold, including those fulfilled from backorders in subsequent months?

## Turn 5 - User Simulator

Yes, the 300 Yuan sales price per unit is applied to all units sold, including those fulfilled from backorders in subsequent months.

## Turn 6 - Generic Agent

QUESTION: Is the 35 Yuan backorder cost per unit charged for each month a unit remains unfulfilled, or is it a one-time charge when the unit is first backordered?

## Turn 6 - User Simulator

It is charged for each month a unit remains unfulfilled.

## Turn 7 - Generic Agent

QUESTION: Is the 15 Yuan inventory holding cost per unit charged for all units in ending inventory, or only for units produced in-house during that month?

## Turn 7 - User Simulator

It is charged for all units in ending inventory.

## Turn 8 - Generic Agent

QUESTION: Is the 90 Yuan raw material cost per unit incurred for all units produced in-house, regardless of whether they are sold immediately or held in inventory?

## Turn 8 - User Simulator

Yes, the 90 Yuan raw material cost per unit is incurred for all units produced in-house, regardless of whether they are sold immediately or held in inventory.

## Turn 9 - Generic Agent

QUESTION: Is the 200 Yuan outsourcing cost per unit incurred for all outsourced units, regardless of whether they are sold immediately or held in inventory?

## Turn 9 - User Simulator

Yes, the 200 Yuan outsourcing cost per unit is incurred for all outsourced units, regardless of whether they are sold immediately or held in inventory.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum limit on the number of units that can be outsourced per month, or is outsourcing capacity unlimited?

## Turn 10 - User Simulator

Outsourcing capacity is unlimited.

## Turn 11 - Generic Agent

QUESTION: Is there a maximum limit on the number of workers that can be hired or fired in any single month, or are hiring and firing quantities unlimited?

## Turn 11 - User Simulator

Hiring and firing quantities are unlimited.

## Turn 12 - Generic Agent

QUESTION: Is the regular wage cost of 30 Yuan per hour for 160 hours per worker paid for all workers on the payroll each month, regardless of how many hours they actually work?

## Turn 12 - User Simulator

Yes, the regular wage cost of 30 Yuan per hour for 160 hours per worker is paid for all workers on the payroll each month, regardless of how many hours they actually work.

## Turn 13 - Generic Agent

QUESTION: Is the 5,000 Yuan hiring cost per new worker a one-time cost incurred when a worker is hired, or is it a recurring monthly cost for each new worker?

## Turn 13 - User Simulator

It is a one-time cost incurred when a worker is hired.

## Turn 14 - Generic Agent

QUESTION: Is the 8,000 Yuan firing cost per worker a one-time cost incurred when a worker is fired, or is it a recurring monthly cost for each fired worker?

## Turn 14 - User Simulator

It is a one-time cost incurred when a worker is fired.

## Turn 15 - Generic Agent

QUESTION: Is there a minimum number of workers that must be maintained on the payroll at all times, or can the workforce be reduced to zero if needed?

## Turn 15 - User Simulator

There is no minimum number of workers that must be maintained; the workforce can be reduced to zero if needed.

## Turn 16 - Generic Agent

QUESTION: Is there a maximum number of workers that can be employed at any time, or is the workforce size unlimited?

## Turn 16 - User Simulator

The workforce size is unlimited.

## Turn 17 - Generic Agent

QUESTION: Is the 160 regular working hours per worker per month a fixed capacity that cannot be exceeded, or can workers work more than 160 regular hours if needed?

## Turn 17 - User Simulator

It is a fixed capacity that cannot be exceeded.

## Turn 18 - Generic Agent

QUESTION: Is the 5 labor hours per in-house unit a fixed requirement that cannot be varied, or can it be adjusted based on worker skill or other factors?

## Turn 18 - User Simulator

It is a fixed requirement that cannot be varied.

## Turn 19 - Generic Agent

QUESTION: Are the demand forecast figures for each month exact requirements that must be met, or are they estimates that can be exceeded or underfilled?

## Turn 19 - User Simulator

They are exact requirements that must be met.

## Turn 20 - Generic Agent

QUESTION: Is there any other constraint or cost not mentioned in the brief that affects the production and workforce plan?

## Turn 20 - User Simulator

No, there are no other constraints or costs not mentioned in the brief.

## Turn 21 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total net profit over six months (January to June).

**Decision Variables:**
- Number of workers hired and fired each month
- Number of units produced in-house each month
- Number of units outsourced each month
- Ending inventory each month
- Backorders carried over each month

**Parameters:**
- Initial workforce: 1,000 workers (January)
- Initial inventory: 15,000 units (January)
- Sales price: 300 Yuan per unit sold (all units, including backorder fulfillment)
- Raw material cost: 90 Yuan per unit (in-house production only)
- Outsourcing cost: 200 Yuan per unit (finished tables)
- Inventory holding cost: 15 Yuan per unit (all ending inventory)
- Backorder cost: 35 Yuan per unit per month (charged each month a unit remains unfulfilled)
- Labor requirement: 5 hours per in-house unit
- Regular working hours: 160 hours per worker per month
- Regular wage rate: 30 Yuan per hour (paid for all 160 hours regardless of utilization)
- Overtime wage rate: 40 Yuan per hour
- Maximum overtime: 20 hours per worker per month
- Hiring cost: 5,000 Yuan per worker (one-time)
- Firing cost: 8,000 Yuan per worker (one-time)
- Demand forecast: Jan 20,000; Feb 40,000; Mar 42,000; Apr 35,000; May 19,000; Jun 18,500 units
- Minimum ending inventory (June): 10,000 units (hard constraint)

**Constraints:**
- Workforce balance: Workers available each month = previous month workers + hires - fires
- Production capacity: In-house production ≤ (workers × 160 + workers × 20) / 5 hours per unit
- Inventory balance: Ending inventory = beginning inventory + in-house production + outsourcing - units sold
- Backorder balance: Backorders carried = previous backorders + demand - units sold
- June ending inventory ≥ 10,000 units
- All variables non-negative
- Workforce can be reduced to zero; no minimum workforce
- Outsourcing capacity unlimited
- Hiring and firing quantities unlimited
- Regular hours fixed at 160 per worker per month
- Overtime limited to 20 hours per worker per month
- Labor hours per unit fixed at 5 hours
- Demand figures are exact requirements that must be met

**Assumptions:**
- None; all key facts confirmed.