## Turn 1 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean that each individual worker can work at most 20 overtime hours in a given month (so total overtime is capped at 20 times the number of workers that month), or that the sum of overtime hours across all workers in a month is capped at 20 hours total?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a given month. So the total overtime hours for the entire workforce in a month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: When you say "orders (current demand and backorders) are fulfilled using available inventory from the previous month, current in-house production, and outsourced units," do you mean that backorders from prior months must be fulfilled before any of the current month's new demand is satisfied, or that all units (backorders plus current demand) are treated as a single pool of demand that can be met in any combination from inventory, in-house production, and outsourcing?

## Turn 2 - User Simulator

All units (backorders plus current demand) are treated as a single pool of demand that can be met in any combination from inventory, in-house production, and outsourcing.

## Turn 3 - Generic Agent

QUESTION: Regarding the workforce, can you hire and fire workers in any month (January through June), or are hiring/firing decisions only allowed in certain months?

## Turn 3 - User Simulator

Hiring and firing decisions can be made in any month from January through June.

## Turn 4 - Generic Agent

QUESTION: Regarding the regular wage of 30 Yuan per hour for 160 hours per worker, paid regardless of utilization — does this mean each worker costs 1,000 × 30 = 4,800 Yuan per month in regular wages even if they work zero hours, and this cost is incurred for every worker employed during that month?

## Turn 4 - User Simulator

Yes, each worker costs 160 hours × 30 Yuan per hour = 4,800 Yuan per month in regular wages, and this cost is incurred for every worker employed during that month, regardless of how many hours they actually work.

## Turn 5 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (and accrue the 4,800 Yuan regular wage) starting in that same month, or do they only become available the following month?

## Turn 5 - User Simulator

Workers hired in a given month are available to work starting in that same month and accrue the 4,800 Yuan regular wage for that month.

## Turn 6 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (and accrue the 4,800 Yuan regular wage) in that same month, or are they removed and do not accrue any cost for that month?

## Turn 6 - User Simulator

Workers fired in a given month are still available to work in that same month and accrue the 4,800 Yuan regular wage for that month.

## Turn 7 - Generic Agent

QUESTION: Regarding the ending inventory at the end of June being at least 10,000 units — does this inventory also incur the 15 Yuan per unit holding cost for June, or is the holding cost only applied to inventory held at the end of months January through May?

## Turn 7 - User Simulator

The 15 Yuan per unit holding cost is applied to inventory held at the end of every month, including June.

## Turn 8 - Generic Agent

QUESTION: Regarding the backorder cost of 35 Yuan per unit for unfulfilled demand carried over to the next month — is this cost incurred for each month a unit remains back-ordered (i.e., if a unit is back-ordered from January to March, it incurs 35 Yuan in January and another 35 Yuan in February, totaling 70 Yuan), or is it a one-time cost of 35 Yuan regardless of how many months the unit is delayed?

## Turn 8 - User Simulator

The 35 Yuan per unit backorder cost is incurred for each month a unit remains back-ordered. So if a unit is back-ordered from January to March, it incurs 35 Yuan in January and another 35 Yuan in February, totaling 70 Yuan.

## Turn 9 - Generic Agent

QUESTION: Regarding the raw material cost of 90 Yuan per unit applicable only to in-house production — is this cost incurred for every in-house unit produced in a month, regardless of whether that unit is sold in the same month or held in inventory for later months?

## Turn 9 - User Simulator

Yes, the 90 Yuan raw material cost is incurred for every in-house unit produced in a month, regardless of whether that unit is sold in the same month or held in inventory for later months.

## Turn 10 - Generic Agent

QUESTION: Regarding the sales price of 300 Yuan per unit sold — is revenue recognized in the month the unit is actually delivered to the customer (i.e., when the backorder is fulfilled), or is it recognized in the month the demand originally occurred?

## Turn 10 - User Simulator

Revenue is recognized in the month the unit is actually delivered to the customer, i.e., when the backorder is fulfilled.

## Turn 11 - Generic Agent

QUESTION: Regarding the outsourcing cost of 200 Yuan per unit for finished tables — is this cost incurred in the month the outsourced units are produced/delivered to your facility, or in the month they are actually sold to the customer?

## Turn 11 - User Simulator

The 200 Yuan outsourcing cost is incurred in the month the outsourced units are produced/delivered to your facility.

## Turn 12 - Generic Agent

QUESTION: Is there any upper limit on the number of units that can be outsourced in a given month, or can you outsource an unlimited number of units?

## Turn 12 - User Simulator

There is no upper limit on the number of units that can be outsourced in a given month.

## Turn 13 - Generic Agent

QUESTION: Is there any upper limit on the number of workers you can hire in a given month, or can you hire an unlimited number of new workers?

## Turn 13 - User Simulator

There is no upper limit on the number of workers that can be hired in a given month.

## Turn 14 - Generic Agent

QUESTION: Regarding the workforce at the end of June — is there any requirement or cost associated with the number of workers employed at the end of June (for example, a target workforce size or a penalty for having too many or too few workers), or is the workforce level at the end of June free with no additional cost or constraint?

## Turn 14 - User Simulator

The workforce level at the end of June is free with no additional cost or constraint.

## Turn 15 - Generic Agent

QUESTION: Regarding the initial inventory of 15,000 units at the start of January — does this inventory incur the 15 Yuan per unit holding cost if it is still on hand at the end of January, or is it "free" inventory that only starts incurring holding cost from February onward?

## Turn 15 - User Simulator

The initial inventory of 15,000 units incurs the 15 Yuan per unit holding cost if it is still on hand at the end of January, just like any other inventory.

## Turn 16 - Generic Agent

QUESTION: Regarding the in-house production capacity — is the only constraint on in-house production the available labor hours (regular 160 hours plus overtime up to 20 hours per worker), or is there any additional machine capacity or production line limit that caps the number of in-house units per month?

## Turn 16 - User Simulator

The only constraint on in-house production is the available labor hours (regular 160 hours plus overtime up to 20 hours per worker). There is no additional machine capacity or production line limit.

## Turn 17 - Generic Agent

QUESTION: Regarding the net profit objective — is it simply total revenue minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other revenue streams or cost items I haven't mentioned?

## Turn 17 - User Simulator

Yes, net profit is simply total revenue minus all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing. There are no other revenue streams or cost items.

## Turn 18 - Generic Agent

QUESTION: Regarding the overtime hours — can a worker work fewer than 160 regular hours in a month (i.e., are regular hours a maximum capacity rather than a fixed commitment), and can overtime hours be any value from 0 up to 20 hours per worker, or must overtime be used in whole-hour increments?

## Turn 18 - User Simulator

Regular hours are a maximum capacity, not a fixed commitment. A worker can work fewer than 160 regular hours in a month. Overtime hours can be any value from 0 up to 20 hours per worker, with no requirement for whole-hour increments.

## Turn 19 - Generic Agent

QUESTION: Regarding the workforce variable — is the number of workers in each month a continuous variable (you can have fractional workers) or must it be an integer (whole number of workers)?

## Turn 19 - User Simulator

The number of workers in each month must be an integer (whole number of workers).

## Turn 20 - Generic Agent

QUESTION: Regarding the production and outsourcing variables — must the number of in-house units produced and the number of outsourced units in each month be integers, or can they be continuous (fractional units)?

## Turn 20 - User Simulator

The number of in-house units produced and the number of outsourced units in each month must be integers.

## Turn 21 - Generic Agent

QUESTION: Regarding the inventory and backorder variables — must the ending inventory and backorder quantities in each month be integers, or can they be continuous (fractional units)?

## Turn 21 - User Simulator

The ending inventory and backorder quantities in each month must be integers.

## Turn 22 - Generic Agent

QUESTION: Regarding the overtime hours variable — must the total overtime hours used in a month be an integer, or can it be a continuous value (e.g., 12.5 hours of overtime across the workforce)?

## Turn 22 - User Simulator

The total overtime hours used in a month can be a continuous value.

## Turn 23 - Generic Agent

QUESTION: Regarding the regular hours used per worker — since regular hours are a maximum capacity and can be less than 160, is the total regular hours used in a month a continuous variable (e.g., 159.5 hours per worker), or must it be an integer?

## Turn 23 - User Simulator

The total regular hours used in a month can be a continuous value.

## Turn 24 - Generic Agent

QUESTION: Regarding the workforce transition — if you have W_t workers at the start of month t, hire H_t workers, and fire F_t workers, is the workforce at the start of month t+1 equal to W_t + H_t - F_t, and is there any constraint that the workforce cannot go below zero (i.e., you cannot fire more workers than you have)?

## Turn 24 - User Simulator

Yes, the workforce at the start of month t+1 is equal to W_t + H_t - F_t. And yes, there is a constraint that the workforce cannot go below zero; you cannot fire more workers than you have.

## Turn 25 - Generic Agent

QUESTION: Regarding the inventory balance — if you have I_{t-1} units of inventory at the start of month t, produce P_t units in-house, outsource O_t units, and fulfill D_t units of total demand (backorders plus current demand), is the ending inventory I_t = I_{t-1} + P_t + O_t - D_t, and can I_t be negative (representing backorders) or must I_t be non-negative with backorders tracked as a separate non-negative variable?

## Turn 25 - User Simulator

I_t must be non-negative, and backorders are tracked as a separate non-negative variable.

## Turn 26 - Generic Agent

QUESTION: Regarding the demand fulfillment in a given month — the total units available to fulfill demand in month t are I_{t-1} + P_t + O_t. If this total is less than the total demand (backorders from prior months plus current month demand), the shortfall becomes the new backorder. If this total is greater than or equal to total demand, all demand is met and the surplus becomes ending inventory. Is this correct, and can both ending inventory and backorders be positive in the same month, or must at least one of them be zero?

## Turn 26 - User Simulator

Yes, that is correct. And at least one of ending inventory or backorders must be zero in any given month; they cannot both be positive simultaneously.

## Turn 27 - Generic Agent

QUESTION: Regarding the backorder balance — if B_{t-1} is the backorder carried into month t and D_t is the current month's new demand, is the total demand to fulfill in month t equal to B_{t-1} + D_t, and is the new backorder B_t equal to max(0, B_{t-1} + D_t - (I_{t-1} + P_t + O_t))?

## Turn 27 - User Simulator

Yes, the total demand to fulfill in month t is B_{t-1} + D_t, and the new backorder B_t is equal to max(0, B_{t-1} + D_t - (I_{t-1} + P_t + O_t)).

## Turn 28 - Generic Agent

QUESTION: Regarding the revenue — is the 300 Yuan per unit revenue earned for every unit of demand that is eventually fulfilled (including backorders fulfilled in later months), so that total revenue over the six months equals 300 times the total units delivered to customers across all six months?

## Turn 28 - User Simulator

Yes, the 300 Yuan per unit revenue is earned for every unit of demand that is eventually fulfilled, including backorders fulfilled in later months. Total revenue over the six months equals 300 times the total units delivered to customers across all six months.

## Turn 29 - Generic Agent

QUESTION: Regarding the backorder at the end of June — must all backorders be fully cleared by the end of June (i.e., B_6 must equal zero), or is it acceptable to have unfulfilled demand remaining at the end of June?

## Turn 29 - User Simulator

All backorders must be fully cleared by the end of June. B_6 must equal zero.

## Turn 30 - Generic Agent

QUESTION: Regarding the labor hours constraint — the total labor hours available in month t is (W_t × 160) regular hours plus (W_t × 20) overtime hours, where W_t is the number of workers employed in month t. The in-house production P_t requires 5 × P_t labor hours. Is the constraint simply 5 × P_t ≤ W_t × 160 + W_t × 20, or is there a separate constraint that regular hours used cannot exceed W_t × 160 and overtime hours used cannot exceed W_t × 20, with the total being the sum of both?

## Turn 30 - User Simulator

There is a separate constraint that regular hours used cannot exceed W_t × 160 and overtime hours used cannot exceed W_t × 20, with the total being the sum of both.