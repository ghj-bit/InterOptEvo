## Turn 1 - Generic Agent

QUESTION: When you say "total overtime hours per month for the entire workforce cannot exceed 20 hours per worker," do you mean each individual worker can work at most 20 overtime hours in a month (so total overtime is capped at 20 × number of workers that month), or that the whole workforce combined can work at most 20 overtime hours in total per month?

## Turn 1 - User Simulator

Each individual worker can work at most 20 overtime hours in a month. So the total overtime hours for the entire workforce in a given month is capped at 20 times the number of workers employed that month.

## Turn 2 - Generic Agent

QUESTION: For the regular wage, you said each worker is paid 30 Yuan/hour for 160 regular hours per month regardless of utilization — does that mean the company pays every employed worker a fixed 4,800 Yuan per month (160 × 30) even if they work fewer hours, or is the 30 Yuan/hour only paid for the regular hours actually worked (up to 160)?

## Turn 2 - User Simulator

The company pays every employed worker a fixed 4,800 Yuan per month (160 hours × 30 Yuan/hour), regardless of how many regular hours they actually work.

## Turn 3 - Generic Agent

QUESTION: When demand is back-ordered (unfulfilled in the current month), is the backorder cost of 35 Yuan per unit charged once for the month the demand is first unmet, or is it charged every month the unit remains unfulfilled until it is finally delivered?

## Turn 3 - User Simulator

The backorder cost of 35 Yuan per unit is charged every month the unit remains unfulfilled until it is finally delivered.

## Turn 4 - Generic Agent

QUESTION: For the inventory holding cost of 15 Yuan per unit, is it charged on the ending inventory of every month (including June), or only on the ending inventory of months January through May (excluding June)?

## Turn 4 - User Simulator

The inventory holding cost of 15 Yuan per unit is charged on the ending inventory of every month, including June.

## Turn 5 - Generic Agent

QUESTION: When you say orders are fulfilled using "available inventory from the previous month, current in-house production, and outsourced units," does the company have a choice about which source to use first (e.g., it could choose to use outsourced units instead of drawing down inventory), or is there a fixed priority order (e.g., must use inventory first, then in-house production, then outsourcing)?

## Turn 5 - User Simulator

The company has a choice about which source to use. There is no fixed priority order; it can use any combination of available inventory from the previous month, current in-house production, and outsourced units to fulfill orders.

## Turn 6 - Generic Agent

QUESTION: Can the workforce size (number of workers) change from month to month through hiring and firing, or is the workforce fixed at 1,000 workers for all six months?

## Turn 6 - User Simulator

The workforce size can change from month to month through hiring and firing.

## Turn 7 - Generic Agent

QUESTION: When a worker is hired in a given month, are they available to work (regular and overtime hours) in that same month, or do they only become available starting the following month?

## Turn 7 - User Simulator

A worker hired in a given month is available to work (regular and overtime hours) in that same month.

## Turn 8 - Generic Agent

QUESTION: When a worker is fired in a given month, are they still available to work (regular and overtime hours) in that same month, or are they no longer available starting from that month?

## Turn 8 - User Simulator

A worker fired in a given month is no longer available to work (regular and overtime hours) starting from that month.

## Turn 9 - Generic Agent

QUESTION: Is there a minimum or maximum number of workers the company must maintain in any month, or can the workforce theoretically go to zero or grow without bound?

## Turn 9 - User Simulator

There is no minimum or maximum number of workers the company must maintain in any month. The workforce can theoretically go to zero or grow without bound.

## Turn 10 - Generic Agent

QUESTION: Is there a limit on how many units can be outsourced in a given month, or can the company outsource any number of units it needs?

## Turn 10 - User Simulator

There is no limit on how many units can be outsourced in a given month. The company can outsource any number of units it needs.

## Turn 11 - Generic Agent

QUESTION: Is there a limit on how many units can be produced in-house in a given month beyond what the workforce's available hours (regular + overtime) allow, or is in-house production capacity solely determined by the total available labor hours (160 regular + up to 20 overtime per worker) divided by 5 hours per unit?

## Turn 11 - User Simulator

In-house production capacity is solely determined by the total available labor hours (160 regular + up to 20 overtime per worker) divided by 5 hours per unit. There is no additional limit beyond the workforce's available hours.

## Turn 12 - Generic Agent

QUESTION: The sales price is 300 Yuan per unit sold — is this revenue recognized in the month the unit is actually delivered to the customer (i.e., when the demand is fulfilled, including backorders fulfilled in a later month), or is it recognized in the month the demand originally occurred?

## Turn 12 - User Simulator

The revenue of 300 Yuan per unit is recognized in the month the unit is actually delivered to the customer, i.e., when the demand is fulfilled, including backorders fulfilled in a later month.

## Turn 13 - Generic Agent

QUESTION: The raw material cost of 90 Yuan per unit applies only to in-house production — does this cost also apply to units that are produced in-house but end up in ending inventory (not sold in that month), or only to units that are both produced in-house and sold in the same month?

## Turn 13 - User Simulator

The raw material cost of 90 Yuan per unit applies to all units produced in-house, regardless of whether they are sold in that month or end up in ending inventory.

## Turn 14 - Generic Agent

QUESTION: The outsourcing cost of 200 Yuan per unit is for finished tables — does this cost also apply to outsourced units that end up in ending inventory (not sold in that month), or only to outsourced units that are sold in the same month?

## Turn 14 - User Simulator

The outsourcing cost of 200 Yuan per unit applies to all outsourced units, regardless of whether they are sold in that month or end up in ending inventory.

## Turn 15 - Generic Agent

QUESTION: When backordered demand is fulfilled in a later month, does the raw material cost (for in-house units) or outsourcing cost (for outsourced units) get charged in the month the unit is produced/outsourced, or in the month the unit is delivered to the customer?

## Turn 15 - User Simulator

The raw material cost (for in-house units) or outsourcing cost (for outsourced units) is charged in the month the unit is produced or outsourced, not in the month the unit is delivered to the customer.

## Turn 16 - Generic Agent

QUESTION: Can the company both hire and fire workers in the same month, or is it restricted to only one of the two actions per month?

## Turn 16 - User Simulator

The company can both hire and fire workers in the same month.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint on the number of units that can be back-ordered in a single month, or can any amount of demand remain unfulfilled and carry over to the next month?

## Turn 17 - User Simulator

There is no constraint on the number of units that can be back-ordered in a single month. Any amount of demand can remain unfulfilled and carry over to the next month.

## Turn 18 - Generic Agent

QUESTION: The ending inventory at the end of June must be at least 10,000 units — does this 10,000-unit requirement apply only to June, or is there also a minimum inventory requirement at the end of any other month?

## Turn 18 - User Simulator

The 10,000-unit minimum inventory requirement applies only to the end of June. There is no minimum inventory requirement at the end of any other month.

## Turn 19 - Generic Agent

QUESTION: Can the ending inventory in any month (January through May) be zero, or is there a constraint that inventory must remain non-negative (i.e., you cannot have negative inventory, but zero is allowed)?

## Turn 19 - User Simulator

Inventory must remain non-negative. Zero ending inventory is allowed in any month (January through May).

## Turn 20 - Generic Agent

QUESTION: When backordered demand from a previous month is fulfilled in the current month, is the 300 Yuan revenue recognized in the current month (when delivered), and is the backorder cost of 35 Yuan charged for each month the unit was unfulfilled (including the month it was finally delivered)?

## Turn 20 - User Simulator

Yes, the 300 Yuan revenue is recognized in the current month when the backordered unit is delivered. The backorder cost of 35 Yuan is charged for each month the unit was unfulfilled, including the month it was finally delivered.

## Turn 21 - Generic Agent

QUESTION: When a worker is fired in a given month, is the firing cost of 8,000 Yuan charged in that same month, and is the worker's fixed 4,800 Yuan monthly wage still paid for that month even though they are no longer available to work?

## Turn 21 - User Simulator

The firing cost of 8,000 Yuan is charged in the month the worker is fired. The worker's fixed 4,800 Yuan monthly wage is not paid for that month, since the worker is no longer available to work starting from that month.

## Turn 22 - Generic Agent

QUESTION: When a worker is hired in a given month, is the hiring cost of 5,000 Yuan charged in that same month, and is the worker's fixed 4,800 Yuan monthly wage also paid for that same month (since they are available to work)?

## Turn 22 - User Simulator

Yes, the hiring cost of 5,000 Yuan is charged in the month the worker is hired, and the worker's fixed 4,800 Yuan monthly wage is also paid for that same month since they are available to work.

## Turn 23 - Generic Agent

QUESTION: The initial inventory of 15,000 units at the start of January — is this inventory available to fulfill January's demand, or is it only available starting from February?

## Turn 23 - User Simulator

The initial inventory of 15,000 units at the start of January is available to fulfill January's demand.

## Turn 24 - Generic Agent

QUESTION: The initial workforce of 1,000 employees at the start of January — are these workers available to work (regular and overtime hours) in January, and is their fixed 4,800 Yuan monthly wage paid for January?

## Turn 24 - User Simulator

Yes, the initial workforce of 1,000 employees at the start of January is available to work (regular and overtime hours) in January, and their fixed 4,800 Yuan monthly wage is paid for January.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of June must be at least some minimum number, or can the company fire all workers by the end of June?

## Turn 25 - User Simulator

There is no constraint that the workforce at the end of June must be at least some minimum number. The company can fire all workers by the end of June.

## Turn 26 - Generic Agent

QUESTION: When backordered demand is fulfilled in a later month, is the raw material cost (90 Yuan for in-house) or outsourcing cost (200 Yuan) charged in the month the unit is produced/outsourced, even if the unit is only delivered to the customer in a subsequent month?

## Turn 26 - User Simulator

Yes, the raw material cost (90 Yuan for in-house) or outsourcing cost (200 Yuan) is charged in the month the unit is produced or outsourced, even if the unit is only delivered to the customer in a subsequent month.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint on the total number of units that can be produced in-house plus outsourced in a single month, or is the only limit on in-house production the available labor hours and outsourcing is unlimited?

## Turn 27 - User Simulator

The only limit on in-house production is the available labor hours (160 regular + up to 20 overtime per worker) divided by 5 hours per unit. Outsourcing is unlimited. There is no additional constraint on the total number of units that can be produced in-house plus outsourced in a single month.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the workforce at the end of each month must be an integer number of workers, or can the workforce be fractional (e.g., 1,050.5 workers)?

## Turn 28 - User Simulator

The workforce at the end of each month must be an integer number of workers.

## Turn 29 - Generic Agent

QUESTION: Are the production quantities (in-house units produced and outsourced units) required to be integers, or can they be fractional?

## Turn 29 - User Simulator

The production quantities (in-house units produced and outsourced units) are required to be integers.

## Turn 30 - Generic Agent

QUESTION: Are the inventory and backorder quantities required to be integers, or can they be fractional?

## Turn 30 - User Simulator

The inventory and backorder quantities are required to be integers.