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

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 × number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: Regarding workforce changes, can you hire and fire workers in any month (including January), and is the workforce for a month determined by the number of workers employed during that month (i.e., can you hire at the start of a month and have them work that same month)?

## Turn 2 - User Simulator

Yes, you can hire and fire workers in any month, including January. The workforce for a given month is determined by the number of workers employed during that month, so if you hire at the start of a month, they are available to work that same month.

## Turn 3 - Generic Agent

QUESTION: Regarding the regular wage, you said it's 30 Yuan per hour for the 160 regular hours per worker, paid regardless of utilization. Does this mean each worker costs 160 × 30 = 4,800 Yuan per month in regular wages, even if they work fewer than 160 hours (e.g., if production is low)?

## Turn 3 - User Simulator

Yes, each worker costs 160 × 30 = 4,800 Yuan per month in regular wages, regardless of how many hours they actually work.

## Turn 4 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit for unfulfilled demand carried over to the next month — is this cost charged once per unit per month it remains back-ordered (i.e., if a unit is back-ordered for two months, it incurs 35 × 2 = 70 Yuan in backorder cost), or is it a one-time cost of 35 Yuan per unit regardless of how many months it stays back-ordered?

## Turn 4 - User Simulator

The backorder cost is charged once per unit per month it remains back-ordered. So if a unit is back-ordered for two months, it incurs 35 × 2 = 70 Yuan in backorder cost.

## Turn 5 - Generic Agent

QUESTION: Regarding the inventory holding cost of 15 Yuan per unit for inventory held at the end of a month — does this apply to all units in ending inventory (including units that were back-ordered and then fulfilled), or only to units that were produced and not yet sold?

## Turn 5 - User Simulator

The inventory holding cost of 15 Yuan per unit applies to all units in ending inventory at the end of a month, regardless of how those units were sourced (produced in-house, outsourced, or carried over from prior inventory).

## Turn 6 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is this revenue recognized in the month the unit is actually delivered to the customer (i.e., when the backorder is fulfilled), or is it recognized in the month the demand originally occurred?

## Turn 6 - User Simulator

The revenue of 300 Yuan per unit is recognized in the month the unit is actually delivered to the customer, which is when the backorder is fulfilled.

## Turn 7 - Generic Agent

QUESTION: Regarding the minimum ending inventory requirement of 10,000 units at the end of June — does this 10,000 units need to be in physical inventory (i.e., not back-ordered), meaning that all demand through June must be fully satisfied and there must be at least 10,000 units left over in inventory?

## Turn 7 - User Simulator

Yes, the 10,000 units must be in physical inventory at the end of June. All demand through June must be fully satisfied (no outstanding backorders), and there must be at least 10,000 units remaining in inventory.

## Turn 8 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit for in-house production — is this cost incurred in the month the unit is produced, regardless of when it is eventually sold?

## Turn 8 - User Simulator

Yes, the raw material cost of 90 Yuan per unit is incurred in the month the unit is produced in-house, regardless of when it is eventually sold.

## Turn 9 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit for finished tables — is this cost incurred in the month the outsourced units are received and used to fulfill demand, or in the month they are ordered (which could be a prior month)?

## Turn 9 - User Simulator

The outsourcing cost of 200 Yuan per unit is incurred in the month the outsourced units are received and used to fulfill demand.

## Turn 10 - Generic Agent

QUESTION: Regarding the labor hours constraint — the total labor hours available in a month are (number of workers × 160 regular hours) + (number of workers × 20 overtime hours). Is the in-house production in a month limited by this total available labor hours (i.e., in-house units × 5 ≤ workers × 180), or is there a separate constraint that regular hours must be used before overtime hours can be used?

## Turn 10 - User Simulator

The in-house production in a month is limited by the total available labor hours, which is (number of workers × 160 regular hours) + (number of workers × 20 overtime hours). So the constraint is: in-house units × 5 ≤ workers × 180. There is no separate requirement that regular hours must be used before overtime hours can be used.

## Turn 11 - Generic Agent

QUESTION: Regarding the overtime wage cost — since overtime hours are only paid when actually used (at 40 Yuan per hour), is the overtime cost in a month equal to (actual overtime hours used) × 40, where actual overtime hours used = max(0, in-house units × 5 − workers × 160)?

## Turn 11 - User Simulator

Yes, the overtime cost in a month is equal to (actual overtime hours used) × 40, where actual overtime hours used = max(0, in-house units × 5 − workers × 160).

## Turn 12 - Generic Agent

QUESTION: Regarding the workforce balance — if you start January with 1,000 workers, hire H workers, and fire F workers, is the workforce for January equal to 1,000 + H − F, and does the workforce for the next month equal the workforce of the current month (i.e., no carry-over of hires/fires beyond the month they occur)?

## Turn 12 - User Simulator

Yes, the workforce for January is 1,000 + H − F. The workforce for the next month equals the workforce of the current month, meaning hires and fires only affect the month in which they occur, and the resulting workforce level carries forward to the next month.

## Turn 13 - Generic Agent

QUESTION: Regarding the inventory balance — in each month, the available units to fulfill demand are: beginning inventory + in-house production + outsourced units. The ending inventory is then: available units − units actually delivered (current demand + prior backorders fulfilled). Can ending inventory be negative (representing backorders), or must it be non-negative with backorders tracked separately?

## Turn 13 - User Simulator

Ending inventory must be non-negative. Backorders are tracked separately. If available units (beginning inventory + in-house production + outsourced units) are less than the total demand to be fulfilled (current demand + prior backorders), the shortfall is recorded as backorders carried to the next month, and ending inventory is zero.

## Turn 14 - Generic Agent

QUESTION: Regarding the objective function — is the total net profit calculated as total revenue (300 × total units delivered over 6 months) minus all costs (raw materials, outsourcing, regular wages, overtime wages, inventory holding, backorder costs, hiring, and firing), with no other revenue or cost components?

## Turn 14 - User Simulator

Yes, total net profit is calculated as total revenue (300 × total units delivered over 6 months) minus all costs: raw materials, outsourcing, regular wages, overtime wages, inventory holding, backorder costs, hiring, and firing. There are no other revenue or cost components.

## Turn 15 - Generic Agent

QUESTION: Regarding the backorder cost — you confirmed it's 35 Yuan per unit per month it remains back-ordered. Does this mean that in each month, the backorder cost is 35 × (number of units in backorder at the end of that month), and this is charged for each month the backorder persists?

## Turn 15 - User Simulator

Yes, in each month, the backorder cost is 35 × (number of units in backorder at the end of that month). This is charged for each month the backorder persists.

## Turn 16 - Generic Agent

QUESTION: Regarding the inventory holding cost — you confirmed it's 15 Yuan per unit for inventory held at the end of a month. Does this mean the holding cost in each month is 15 × (ending inventory of that month), and this applies to all six months including June?

## Turn 16 - User Simulator

Yes, the holding cost in each month is 15 × (ending inventory of that month), and this applies to all six months, including June.

## Turn 17 - Generic Agent

QUESTION: Regarding the workforce — is there a minimum or maximum number of workers that can be employed in any month, or can the workforce theoretically go to zero (if all workers are fired)?

## Turn 17 - User Simulator

There is no minimum or maximum number of workers specified. The workforce can theoretically go to zero if all workers are fired.

## Turn 18 - Generic Agent

QUESTION: Regarding the outsourcing — is there any limit on the number of units that can be outsourced in a month, or can you outsource an unlimited number of units?

## Turn 18 - User Simulator

There is no limit on the number of units that can be outsourced in a month. You can outsource an unlimited number of units.

## Turn 19 - Generic Agent

QUESTION: Regarding the in-house production — is there any limit on the number of units that can be produced in-house in a month other than the labor hours constraint (in-house units × 5 ≤ workers × 180)?

## Turn 19 - User Simulator

No, there is no other limit on in-house production besides the labor hours constraint (in-house units × 5 ≤ workers × 180).

## Turn 20 - Generic Agent

QUESTION: Regarding the demand fulfillment priority — when available units (beginning inventory + in-house production + outsourced units) are used to fulfill demand, is there a specific priority order (e.g., use beginning inventory first, then in-house production, then outsourced units), or does the model simply need to ensure total available units ≥ total demand to be fulfilled, with the specific sourcing mix being a free decision?

## Turn 20 - User Simulator

The model simply needs to ensure total available units (beginning inventory + in-house production + outsourced units) ≥ total demand to be fulfilled (current demand + prior backorders). There is no specific priority order for sourcing; the specific mix is a free decision.

## Turn 21 - Generic Agent

QUESTION: Regarding the backorder tracking — if in a given month, available units exceed the total demand to be fulfilled (current demand + prior backorders), is the excess simply added to ending inventory, and the backorder for the next month is zero? In other words, can backorders only increase (when available < demand) or go to zero (when available ≥ demand), but never partially reduce?

## Turn 21 - User Simulator

No, backorders can be partially reduced. If available units are less than total demand to be fulfilled (current demand + prior backorders), the available units are used to fulfill as much demand as possible, and the remaining unfulfilled amount becomes the backorder for the next month. So the backorder for the next month is max(0, total demand to be fulfilled − available units).

## Turn 22 - Generic Agent

QUESTION: Regarding the ending inventory calculation — if available units exceed total demand to be fulfilled, the ending inventory is (available units − total demand to be fulfilled). If available units are less than total demand to be fulfilled, the ending inventory is zero and the backorder is (total demand to be fulfilled − available units). Is this correct?

## Turn 22 - User Simulator

Yes, that is correct. If available units exceed total demand to be fulfilled, ending inventory is (available units − total demand to be fulfilled) and backorder is zero. If available units are less than total demand to be fulfilled, ending inventory is zero and backorder is (total demand to be fulfilled − available units).

## Turn 23 - Generic Agent

QUESTION: Regarding the revenue recognition — you confirmed revenue is recognized when the unit is delivered. So in each month, revenue is 300 × (units actually delivered that month), where units delivered = min(available units, total demand to be fulfilled). Is this correct?

## Turn 23 - User Simulator

Yes, that is correct. In each month, revenue is 300 × (units actually delivered that month), where units delivered = min(available units, total demand to be fulfilled).

## Turn 24 - Generic Agent

QUESTION: Regarding the workforce and labor hours — you confirmed the constraint is in-house units × 5 ≤ workers × 180. But the overtime cost is based on actual overtime hours used = max(0, in-house units × 5 − workers × 160). Does this mean that if in-house units × 5 is less than workers × 160, no overtime is used and no overtime cost is incurred, but the workers still get paid their full 160 × 30 = 4,800 Yuan regular wage?

## Turn 24 - User Simulator

Yes, that is correct. If in-house units × 5 is less than workers × 160, no overtime is used and no overtime cost is incurred, but the workers still get paid their full 160 × 30 = 4,800 Yuan regular wage.

## Turn 25 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January — is this inventory available to fulfill January's demand (i.e., it's part of January's available units), and does it incur a holding cost at the end of January if it's still in inventory?

## Turn 25 - User Simulator

Yes, the initial inventory of 15,000 units is available to fulfill January's demand as part of January's available units. If any of it remains in inventory at the end of January, it incurs the holding cost of 15 Yuan per unit at the end of January.

## Turn 26 - Generic Agent

QUESTION: Regarding the initial workforce of 1,000 employees at the start of January — do these 1,000 workers incur the regular wage cost of 4,800 Yuan each in January (i.e., 1,000 × 4,800 = 4,800,000 Yuan), even if no hiring or firing occurs in January?

## Turn 26 - User Simulator

Yes, the 1,000 workers at the start of January incur the regular wage cost of 4,800 Yuan each in January, totaling 1,000 × 4,800 = 4,800,000 Yuan, even if no hiring or firing occurs in January.

## Turn 27 - Generic Agent

QUESTION: Regarding the hiring and firing costs — if you hire H workers in a month, the hiring cost is 5,000 × H for that month. If you fire F workers in a month, the firing cost is 8,000 × F for that month. Can you both hire and fire in the same month, and are these costs independent of each other?

## Turn 27 - User Simulator

Yes, you can both hire and fire in the same month. The hiring cost is 5,000 × H and the firing cost is 8,000 × F, and these costs are independent of each other.

## Turn 28 - Generic Agent

QUESTION: Regarding the workforce balance — if you start a month with W workers, hire H, and fire F, the workforce for that month is W + H − F. The workforce for the next month starts at W + H − F. Is it possible to fire more workers than you have (i.e., can F exceed W + H, making the workforce negative)?

## Turn 28 - User Simulator

No, it is not possible to fire more workers than you have. The workforce cannot be negative, so F cannot exceed W + H.

## Turn 29 - Generic Agent

QUESTION: Regarding the backorder at the end of June — you confirmed that all demand through June must be fully satisfied (no outstanding backorders) and there must be at least 10,000 units in physical inventory. Does this mean the backorder at the end of June must be exactly zero, and the ending inventory at the end of June must be at least 10,000?

## Turn 29 - User Simulator

Yes, the backorder at the end of June must be exactly zero, and the ending inventory at the end of June must be at least 10,000 units.

## Turn 30 - Generic Agent

QUESTION: Regarding the demand forecast — the demand for each month is a fixed, known quantity that must be fulfilled (either in that month or back-ordered to a later month). Is there any possibility of lost sales (i.e., demand that is never fulfilled), or must all demand eventually be satisfied?

## Turn 30 - User Simulator

There is no possibility of lost sales. All demand must eventually be satisfied within the six-month period.