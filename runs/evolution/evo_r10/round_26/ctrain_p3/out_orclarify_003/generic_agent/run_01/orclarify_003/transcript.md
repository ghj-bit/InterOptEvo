## Turn 1 - Generic Agent

QUESTION: When you say the workforce can be hired or fired, is the number of workers allowed to change at the start of each month (so January's production can already use workers hired in January), and can the workforce size change in every month from January through June?

## Turn 1 - User Simulator

Yes, the workforce can be adjusted at the start of each month, so January’s production can already use workers hired in January. The workforce size can change in every month from January through June.

## Turn 2 - Generic Agent

QUESTION: For the overtime limit, is the 20-hour cap applied per individual worker (so total overtime in a month equals 20 times the number of workers that month), or is it a single company-wide cap of 20 hours total for the whole workforce?

## Turn 2 - User Simulator

The 20-hour cap is applied per individual worker. So the total overtime hours allowed in a month equals 20 times the number of workers that month.

## Turn 3 - Generic Agent

QUESTION: For the regular wage, is the 30 Yuan/hour paid for all 160 regular hours of every worker each month regardless of how many hours are actually used (i.e., a fixed 4,800 Yuan per worker per month), or is it paid only for the regular hours actually consumed by production?

## Turn 3 - User Simulator

The regular wage is paid for all 160 regular hours of every worker each month regardless of how many hours are actually used. So it is a fixed 4,800 Yuan per worker per month.

## Turn 4 - Generic Agent

QUESTION: When demand is back-ordered, is the 35 Yuan backorder cost charged once per unit for the single month it is carried over, or is it charged for each month a unit remains unfulfilled until it is finally delivered?

## Turn 4 - User Simulator

The 35 Yuan backorder cost is charged for each month a unit remains unfulfilled until it is finally delivered.

## Turn 5 - Generic Agent

QUESTION: For the 10,000-unit minimum ending inventory at the end of June, does this inventory need to be on hand after all June demand (including any backorders) has been fulfilled, or is it a separate stock that must exist in addition to meeting June's demand?

## Turn 5 - User Simulator

The 10,000-unit minimum ending inventory must be on hand after all June demand (including any backorders) has been fulfilled.

## Turn 6 - Generic Agent

QUESTION: Can the workforce size ever drop below zero or go negative, and is there any minimum number of workers that must be kept (for example, at least 0 is allowed, meaning the company could fire everyone)?

## Turn 6 - User Simulator

The workforce size cannot drop below zero. There is no stated minimum number of workers that must be kept, so the company could fire everyone, leaving zero workers.

## Turn 7 - Generic Agent

QUESTION: For the 15 Yuan inventory holding cost, is it charged on the ending inventory of every month from January through June (including the June ending inventory that must be at least 10,000 units), or only for the months January through May?

## Turn 7 - User Simulator

The 15 Yuan inventory holding cost is charged on the ending inventory of every month from January through June, including the June ending inventory.

## Turn 8 - Generic Agent

QUESTION: When a unit is back-ordered and later fulfilled in a subsequent month, is the sales price of 300 Yuan still earned for that unit when it is finally delivered, or is the revenue recognized in the month the demand originally occurred?

## Turn 8 - User Simulator

The sales price of 300 Yuan is earned for that unit when it is finally delivered.

## Turn 9 - Generic Agent

QUESTION: For the raw material cost of 90 Yuan per unit, is it incurred only on units produced in-house (as stated), and is there any raw material cost associated with outsourced finished tables, or is the 200 Yuan outsourcing cost fully all-inclusive with no additional material cost?

## Turn 9 - User Simulator

The 90 Yuan raw material cost is incurred only on units produced in-house. The 200 Yuan outsourcing cost is fully all-inclusive with no additional material cost.

## Turn 10 - Generic Agent

QUESTION: Can the company choose to produce more units than the total demand (current plus backorders) in a given month, building up inventory for future months, or must production exactly match the demand being fulfilled each month?

## Turn 10 - User Simulator

The company can choose to produce more units than the total demand (current plus backorders) in a given month, building up inventory for future months.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how many units can be outsourced in a month (a maximum outsourcing capacity), or can the company outsource any number of units it needs?

## Turn 11 - User Simulator

There is no stated limit on how many units can be outsourced in a month. The company can outsource any number of units it needs.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on how many units can be produced in-house in a month beyond what the available labor hours (regular plus overtime) allow, or is the only constraint on in-house production the labor-hour capacity?

## Turn 12 - User Simulator

The only constraint on in-house production is the labor-hour capacity (regular plus overtime). There is no separate limit on the number of units that can be produced in-house beyond what the available labor hours allow.

## Turn 13 - Generic Agent

QUESTION: Can the company choose to leave some demand unfulfilled (back-ordered) even when it has enough inventory, production, and outsourcing capacity to meet it, or must it always fulfill as much demand as possible each month?

## Turn 13 - User Simulator

The company can choose to leave some demand unfulfilled (back-ordered) even when it has enough inventory, production, and outsourcing capacity to meet it.

## Turn 14 - Generic Agent

QUESTION: When a unit is back-ordered and later fulfilled, is the 35 Yuan backorder cost charged for each month it remains unfulfilled, including the month it is finally delivered, or only for the months it is carried over before delivery?

## Turn 14 - User Simulator

The 35 Yuan backorder cost is charged for each month it remains unfulfilled, including the month it is finally delivered.

## Turn 15 - Generic Agent

QUESTION: For the backorder cost, is it charged on the total number of units that are unfulfilled at the end of each month (i.e., the backorder balance carried into the next month), or is it charged on the cumulative total of all units that have ever been back-ordered during the period?

## Turn 15 - User Simulator

The 35 Yuan backorder cost is charged on the total number of units that are unfulfilled at the end of each month (i.e., the backorder balance carried into the next month).

## Turn 16 - Generic Agent

QUESTION: For the backorder cost, is it charged on the backorder balance at the end of every month from January through June, or only for the months January through May (since there is no month after June to carry into)?

## Turn 16 - User Simulator

The 35 Yuan backorder cost is charged on the backorder balance at the end of every month from January through May. Since all backorders must be cleared by the end of June, the June ending backorder balance is zero, so no backorder cost is charged for June.

## Turn 17 - Generic Agent

QUESTION: For the hiring and firing costs, are these one-time costs paid in the month the workforce changes (i.e., hiring cost of 5,000 Yuan per new worker hired in a given month, and firing cost of 8,000 Yuan per worker fired in that same month), or are they spread over multiple months?

## Turn 17 - User Simulator

These are one-time costs paid in the month the workforce changes. The hiring cost of 5,000 Yuan is paid per new worker hired in a given month, and the firing cost of 8,000 Yuan is paid per worker fired in that same month.

## Turn 18 - Generic Agent

QUESTION: For the inventory holding cost, is it charged on the ending inventory balance at the end of each month (i.e., the units physically on hand after that month's demand is fulfilled), or is it charged on the average inventory during the month?

## Turn 18 - User Simulator

The inventory holding cost is charged on the ending inventory balance at the end of each month (i.e., the units physically on hand after that month's demand is fulfilled).

## Turn 19 - Generic Agent

QUESTION: When the company fulfills demand using inventory, in-house production, and outsourced units, is there any priority or restriction on which source is used first (e.g., must use inventory before production, or production before outsourcing), or can the company freely allocate among the three sources in any combination?

## Turn 19 - User Simulator

There is no priority or restriction on which source is used first. The company can freely allocate among inventory, in-house production, and outsourced units in any combination to fulfill demand.

## Turn 20 - Generic Agent

QUESTION: For the labor-hour capacity, is the total available labor in a month equal to (number of workers × 160 regular hours) + (number of workers × 20 overtime hours), meaning each worker can contribute up to 180 hours total, or is the overtime capacity separate and can be used independently of the regular hours?

## Turn 20 - User Simulator

The total available labor in a month is equal to (number of workers × 160 regular hours) + (number of workers × 20 overtime hours), meaning each worker can contribute up to 180 hours total.

## Turn 21 - Generic Agent

QUESTION: For the in-house production, is the 5 labor hours per unit drawn from the regular hours first and then overtime, or can the 5 hours per unit be drawn from any combination of regular and overtime hours as long as the total does not exceed the available capacity?

## Turn 21 - User Simulator

The 5 labor hours per unit can be drawn from any combination of regular and overtime hours, as long as the total does not exceed the available capacity.

## Turn 22 - Generic Agent

QUESTION: For the net profit calculation, is the objective to maximize (total revenue from all units sold) minus (all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other costs or revenues to consider?

## Turn 22 - User Simulator

Yes, the objective is to maximize (total revenue from all units sold) minus (all costs: raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, and firing), with no other costs or revenues to consider.

## Turn 23 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Planning horizon:** 6 months (January through June).

**Objective:** Maximize total net profit = total revenue from all units sold (300 Yuan per unit, earned when delivered) minus all costs (raw materials, outsourcing, inventory holding, backorder, regular wages, overtime wages, hiring, firing).

**Demand:** Jan 20,000; Feb 40,000; Mar 42,000; Apr 35,000; May 19,000; Jun 18,500.

**Backorders:** Unfulfilled demand is carried forward. The 35 Yuan backorder cost is charged on the ending backorder balance for each month January through May. All backorders must be cleared by end of June (June ending backorder = 0).

**Inventory:** Initial inventory = 15,000 units. The 15 Yuan holding cost is charged on the ending inventory balance for each month January through June. Ending inventory at end of June must be at least 10,000 units (after all June demand is fulfilled).

**Workforce:** Initial workforce = 1,000 workers. Workforce can be adjusted at the start of each month (January through June). Workforce cannot go below zero. Hiring cost = 5,000 Yuan per new worker (one-time, in the month hired). Firing cost = 8,000 Yuan per worker fired (one-time, in the month fired).

**Labor:** Each worker provides 160 regular hours + up to 20 overtime hours per month (max 180 total). Regular wage = 30 Yuan/hour × 160 hours = 4,800 Yuan per worker per month (paid regardless of utilization). Overtime wage = 40 Yuan/hour. Total overtime per month ≤ 20 × (number of workers that month).

**In-house production:** Each unit requires 5 labor hours. Labor hours can be drawn from any combination of regular and overtime. No separate capacity limit beyond labor hours. Raw material cost = 90 Yuan per in-house unit.

**Outsourcing:** 200 Yuan per finished unit (all-inclusive, no additional material cost). No limit on outsourcing quantity.

**Fulfillment:** Demand (current + backorders) is fulfilled from a free combination of beginning inventory, in-house production, and outsourced units. No priority or restriction on source allocation. The company may choose to backorder even when capacity exists.

**No other costs or revenues.**