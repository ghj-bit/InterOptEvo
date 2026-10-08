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

It is 20 hours per individual worker per month. So the total overtime hours allowed for the entire workforce in any given month is 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you state it is paid "regardless of utilization" — does this mean each worker's 160 regular hours are paid at 30 Yuan/hour every month even if the actual production uses fewer than 160 hours (i.e., regular labor cost is simply 160 × 30 × number of workers per month, independent of how many units are produced)?

## Turn 2 - User Simulator

Yes, that is correct. Each worker is paid for 160 regular hours at 30 Yuan per hour every month, regardless of how many hours are actually used for production.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered (unfulfilled in the current month and carried to a later month), is the backorder cost of 35 Yuan per unit charged once for the month the demand is unmet, and then charged again in each subsequent month the backorder remains outstanding until it is finally fulfilled?

## Turn 3 - User Simulator

Yes, the 35 Yuan per unit backorder cost is charged for each month the demand remains unfulfilled.

## Turn 4 - Generic Agent

QUESTION: When a backorder is finally fulfilled in a later month, is the sales revenue of 300 Yuan per unit recognized in the month the demand was originally due, or in the month the unit is actually delivered to the customer?

## Turn 4 - User Simulator

The sales revenue of 300 Yuan per unit is recognized in the month the unit is actually delivered to the customer.

## Turn 5 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of each month (i.e., inventory remaining at the end of January, end of February, etc.), and does this include the final ending inventory of 10,000 units at the end of June?

## Turn 5 - User Simulator

Yes, the 15 Yuan per unit inventory holding cost is charged on the ending inventory of each month, including the final ending inventory at the end of June.

## Turn 6 - Generic Agent

QUESTION: Can the workforce be changed (hired or fired) at the start of each month, meaning the number of workers employed during a given month can differ from the previous month, with hiring and firing costs incurred for the net change?

## Turn 6 - User Simulator

Yes, the workforce can be changed at the start of each month. The number of workers employed during a given month can differ from the previous month, and hiring or firing costs are incurred for the net change in workforce size.

## Turn 7 - Generic Agent

QUESTION: When you say hiring and firing costs are incurred for the "net change," do you mean that if the workforce increases by 100 you pay 100 × 5,000, and if it decreases by 100 you pay 100 × 8,000, but you cannot simultaneously hire and fire in the same month (i.e., only the net change matters)?

## Turn 7 - User Simulator

Yes, that is correct. Only the net change matters. If the workforce increases, you pay the hiring cost for the number of new workers. If it decreases, you pay the firing cost for the number of workers let go. You do not simultaneously hire and fire in the same month.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint on the workforce size, such as a minimum or maximum number of workers that must be maintained each month, or can the workforce be reduced to zero if that is optimal?

## Turn 8 - User Simulator

There is no minimum or maximum workforce size constraint. The workforce can be reduced to zero if that is optimal.

## Turn 9 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it incurred only on units produced in-house during that month, and does it apply to units that are produced but end up in ending inventory (not yet sold)?

## Turn 9 - User Simulator

Yes, the 90 Yuan per unit raw material cost is incurred only on units produced in-house during that month. It applies to all in-house units produced, including those that end up in ending inventory and are not yet sold.

## Turn 10 - Generic Agent

QUESTION: When backordered demand is fulfilled in a later month, is the raw material cost of 90 Yuan per unit charged in the month the unit is actually produced (in-house), regardless of which month's demand it fulfills?

## Turn 10 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is charged in the month the unit is actually produced in-house, regardless of which month's demand it fulfills.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on the number of units that can be outsourced per month, or is outsourcing capacity unlimited?

## Turn 11 - User Simulator

Outsourcing capacity is unlimited. There is no limit on the number of units that can be outsourced per month.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint on the total production capacity per month beyond what is determined by the workforce (regular + overtime hours), or can in-house production be any non-negative number as long as the labor hours required (5 hours per unit) do not exceed the available regular and overtime hours?

## Turn 12 - User Simulator

There is no additional constraint on total production capacity beyond the labor hours. In-house production can be any non-negative number as long as the labor hours required (5 hours per unit) do not exceed the available regular and overtime hours for that month.

## Turn 13 - Generic Agent

QUESTION: Can the workforce be changed at the start of January (i.e., can you hire or fire workers before January production begins, relative to the initial 1,000 employees), or is the January workforce fixed at 1,000?

## Turn 13 - User Simulator

The workforce can be changed at the start of January. You can hire or fire workers before January production begins, relative to the initial 1,000 employees.

## Turn 14 - Generic Agent

QUESTION: Is there any constraint that the workforce must be an integer number of workers each month, or can it be treated as a continuous variable?

## Turn 14 - User Simulator

The workforce must be an integer number of workers each month.

## Turn 15 - Generic Agent

QUESTION: Are in-house production units and outsourced units required to be integers, or can they be treated as continuous variables?

## Turn 15 - User Simulator

In-house production units and outsourced units can be treated as continuous variables.

## Turn 16 - Generic Agent

QUESTION: When demand is back-ordered and fulfilled in a later month, is the backorder cost of 35 Yuan per unit charged for each month the demand remains unfulfilled, including the month it is finally fulfilled?

## Turn 16 - User Simulator

No, the backorder cost of 35 Yuan per unit is charged for each month the demand remains unfulfilled, but it is not charged in the month it is finally fulfilled.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of June must be at least some minimum level, or can it be reduced to zero by the end of June if that is optimal?

## Turn 17 - User Simulator

There is no minimum workforce requirement at the end of June. The workforce can be reduced to zero by the end of June if that is optimal.

## Turn 18 - Generic Agent

QUESTION: Is there any constraint that the workforce must be non-negative (i.e., you cannot have a negative number of workers), or is there any other lower bound on the workforce besides zero?

## Turn 18 - User Simulator

The workforce must be non-negative. You cannot have a negative number of workers. There is no other lower bound on the workforce besides zero.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the ending inventory at the end of each month (other than June) must be non-negative, or can inventory go negative (which would represent backorders)?

## Turn 19 - User Simulator

Inventory cannot go negative. The ending inventory at the end of each month must be non-negative. Backorders are tracked separately from inventory.

## Turn 20 - Generic Agent

QUESTION: When you say backorders are tracked separately from inventory, does that mean the inventory balance equation is: ending inventory = beginning inventory + in-house production + outsourcing - units delivered to customers (from current demand and backorders), and the backorder balance is: ending backorder = beginning backorder + current demand - units delivered to customers, with the constraint that you cannot deliver more units than you have available (beginning inventory + in-house production + outsourcing)?

## Turn 20 - User Simulator

Yes, that is correct. The inventory balance is: ending inventory = beginning inventory + in-house production + outsourcing - units delivered to customers. The backorder balance is: ending backorder = beginning backorder + current demand - units delivered to customers. You cannot deliver more units than you have available (beginning inventory + in-house production + outsourcing).

## Turn 21 - Generic Agent

QUESTION: When you say "units delivered to customers" in both the inventory and backorder balance equations, does this mean the same quantity appears in both equations (i.e., the total units delivered in a month is split between fulfilling current demand and fulfilling backorders, and this total is subtracted from both the inventory and backorder balances)?

## Turn 21 - User Simulator

No, that is not correct. The total units delivered in a month is split between fulfilling current demand and fulfilling backorders. The units delivered to fulfill current demand are subtracted from the inventory balance. The units delivered to fulfill backorders are subtracted from the backorder balance. They are not the same quantity appearing in both equations.

## Turn 22 - Generic Agent

QUESTION: So the inventory balance equation is: ending inventory = beginning inventory + in-house production + outsourcing - units delivered to fulfill current demand, and the backorder balance equation is: ending backorder = beginning backorder + current demand - units delivered to fulfill backorders, with the constraint that total units delivered (current demand fulfilled + backorders fulfilled) cannot exceed available supply (beginning inventory + in-house production + outsourcing)?

## Turn 22 - User Simulator

Yes, that is correct.

## Turn 23 - Generic Agent

QUESTION: When units are delivered to fulfill current demand, are they drawn from beginning inventory first, then from in-house production, then from outsourcing, or can they be drawn from any combination of these sources in any proportion?

## Turn 23 - User Simulator

Units can be drawn from any combination of beginning inventory, in-house production, and outsourcing in any proportion.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the total units delivered to fulfill current demand plus the total units delivered to fulfill backorders in a given month cannot exceed the total available supply (beginning inventory + in-house production + outsourcing), or are these two delivery streams independent?

## Turn 24 - User Simulator

Yes, there is a constraint that the total units delivered to fulfill current demand plus the total units delivered to fulfill backorders in a given month cannot exceed the total available supply (beginning inventory + in-house production + outsourcing).

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the total units delivered to fulfill current demand in a given month cannot exceed the current month's demand, or can you deliver more than the current month's demand (which would reduce future backorders)?

## Turn 25 - User Simulator

The total units delivered to fulfill current demand in a given month cannot exceed the current month's demand.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the total units delivered to fulfill backorders in a given month cannot exceed the beginning backorder balance for that month, or can you deliver more than the beginning backorder balance?

## Turn 26 - User Simulator

The total units delivered to fulfill backorders in a given month cannot exceed the beginning backorder balance for that month.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the workforce must be an integer number of workers each month, or can it be treated as a continuous variable?

## Turn 27 - User Simulator

The workforce must be an integer number of workers each month.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the number of units delivered to fulfill current demand and the number of units delivered to fulfill backorders must be integers, or can they be treated as continuous variables?

## Turn 28 - User Simulator

The number of units delivered to fulfill current demand and the number of units delivered to fulfill backorders can be treated as continuous variables.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the ending inventory and ending backorder must be non-negative, or can they be negative?

## Turn 29 - User Simulator

Both ending inventory and ending backorder must be non-negative.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the in-house production and outsourcing must be non-negative, or can they be negative?

## Turn 30 - User Simulator

Both in-house production and outsourcing must be non-negative.