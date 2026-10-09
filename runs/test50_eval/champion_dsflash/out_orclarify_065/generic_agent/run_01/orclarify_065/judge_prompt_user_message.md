# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U8, U9, U2, U3, U4, U5, U6
I need help determining a monthly production plan for a company producing microwave ovens and water heaters in two workshops (A and B), where at least 80 microwave ovens should be sold per month, and the production hours of both workshops A and B should be fully utilized.

Processing requirements per unit: microwave oven requires 2 hours in workshop A and 1 hour in workshop B; water heater requires 1 hour in workshop A and 3 hours in workshop B.

Inspection and sales cost per unit: microwave oven 30 yuan, water heater 50 yuan.

Workshop A: 250 hours available per month, cost 80 yuan per hour.

Workshop B: 150 hours available per month, cost 20 yuan per hour.

Estimated average monthly sales next year: 80 microwave ovens, 50 water heaters.

## Problem units
- U1 (context): I need help determining a monthly production plan for a company producing microwave ovens and water heaters in two workshops (A and B).
- U2 (data): Processing requirements per unit: microwave oven requires 2 hours in workshop A and 1 hour in workshop B; water heater requires 1 hour in workshop A and 3 hours in workshop B.
- U3 (data): Inspection and sales cost per unit: microwave oven 30 yuan, water heater 50 yuan.
- U4 (data): Workshop A: 250 hours available per month, cost 80 yuan per hour.
- U5 (data): Workshop B: 150 hours available per month, cost 20 yuan per hour.
- U6 (data): Estimated average monthly sales next year: 80 microwave ovens, 50 water heaters.
- U7 (constraint): Inspection and sales costs should not exceed 5500 yuan per month.
- U8 (constraint): At least 80 microwave ovens should be sold per month.
- U9 (constraint): The production hours of both workshops A and B should be fully utilized.
- U10 (constraint): Overtime in workshop A should not exceed 20 hours.
- U11 (constraint): At least 50 water heaters should be sold per month.

## Hidden slot scoring rules
## H1: inspection_cost_limit
- Severity: P1
- Severity reason: Without this constraint, the agent could formulate a model that ignores the monthly budget cap on inspection and sales costs, leading to a plan that violates the company's financial limit. It is a critical business rule that materially changes the feasible region.
- Problem unit ID: U7
- Semantic hit rule: The agent's question must ask about the inspection/sales cost budget or confirm the 5500 yuan monthly limit.
- Reference acceptable questions:
  - Do the inspection and sales costs have a monthly budget? The problem mentions it should not exceed 5500 yuan, can you confirm?
  - Is there a limit on the total cost of inspection and sales per month?
- Failure modes:
  - Assuming there is no limit on total inspection and sales costs.
  - Treating the per-unit costs (30/50 yuan) as purely variable expenses without any aggregate cap.

## H2: overtime_limit_workshop_a
- Severity: P1
- Severity reason: Without this constraint, the agent might assume there is no overtime allowed or that overtime is unlimited. The model would then incorrectly treat workshop A's capacity, making the problem either infeasible (if full utilization of regular hours is required without overtime) or unbounded. This is an important clarification for the capacity structure.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must ask about the possibility and/or limit of overtime hours for workshop A.
- Reference acceptable questions:
  - Is overtime allowed in workshop A? If so, up to how many hours?
  - Can workshop A work beyond the 250 regular hours, and what is the overtime limit?
- Failure modes:
  - Assuming workshop A's capacity is fixed at exactly 250 hours with no flexibility.
  - Assuming workshop A can use unlimited overtime hours.

## H3: minimum_water_heater_sales
- Severity: P2
- Severity reason: The problem still yields a coherent production planning model without this lower bound, as the minimum microwave sales (U8) and other constraints are present. The omission would create a valid alternative scenario, but adding this constraint enforces a specific business requirement that slightly restricts the feasible region.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask about a minimum sales requirement for water heaters.
- Reference acceptable questions:
  - Is there a minimum number of water heaters that must be sold each month?
  - Should the plan ensure that at least 50 water heaters are sold?
- Failure modes:
  - Assuming no minimum sales constraint exists for water heaters.
  - Using only the estimated average (50) as a target but not as a hard lower bound.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective you want the production plan to optimize — for example, maximize total profit, minimize total cost, or meet the sales estimates exactly?

## Turn 1 - User Simulator

Minimize total cost.

## Turn 2 - Generic Agent

QUESTION: For the "at least 80 microwave ovens sold per month" requirement, is that a minimum sales floor of 80 microwaves, or must production exactly equal the estimated 80 microwaves and 50 water heaters?

## Turn 2 - User Simulator

It is a minimum sales floor of 80 microwave ovens.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum requirement for water heaters, or can the plan produce any number of water heaters (including zero)?

## Turn 3 - User Simulator

Yes, the plan must ensure that at least 50 water heaters are sold each month.

## Turn 4 - Generic Agent

QUESTION: You said both workshops' production hours should be fully utilized — does that mean workshop A must use exactly 250 hours and workshop B exactly 150 hours each month?

## Turn 4 - User Simulator

Workshop A can have overtime, but it should not exceed 20 hours per month.

## Turn 5 - Generic Agent

QUESTION: Does workshop B also have an overtime allowance, or must workshop B use exactly 150 hours with no overtime?

## Turn 5 - User Simulator

Workshop B must use exactly 150 hours with no overtime.

## Turn 6 - Generic Agent

QUESTION: For workshop A, is the 250 hours a minimum that must be used (with up to 20 extra overtime hours allowed), or can workshop A use fewer than 250 hours?

## Turn 6 - User Simulator

The 250 hours is a minimum that must be used, with up to 20 extra overtime hours allowed.

## Turn 7 - Generic Agent

QUESTION: Is the overtime hour cost in workshop A the same 80 yuan per hour as regular hours, or is there a different overtime rate?

## Turn 7 - User Simulator

The overtime hour cost in workshop A is the same 80 yuan per hour as regular hours.

## Turn 8 - Generic Agent

QUESTION: Are the inspection and sales costs (30 yuan per microwave, 50 yuan per water heater) incurred per unit sold, and is there any upper limit on how many units can be sold?

## Turn 8 - User Simulator

Yes, the inspection and sales costs are incurred per unit sold. There is no upper limit on how many units can be sold, but the total monthly inspection and sales cost should not exceed 5500 yuan.

## Turn 9 - Generic Agent

QUESTION: Since there is no upper limit on sales but a 5500 yuan cap on total inspection and sales cost, should the model treat the 80 microwaves and 50 water heaters as minimums only, with extra production allowed as long as the 5500 yuan inspection cost cap holds?

## Turn 9 - User Simulator

Yes, the 80 microwaves and 50 water heaters are minimums only, with extra production allowed as long as the 5500 yuan inspection cost cap holds.

## Turn 10 - Generic Agent

QUESTION: Should production quantities be whole numbers of units, or can the plan use fractional units?

## Turn 10 - User Simulator

Production quantities should be whole numbers of units. The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints I should know about, such as a maximum production capacity per workshop beyond the hours, or any limit on total units produced?

## Turn 11 - User Simulator

No, there are no other constraints beyond the hours available (250 regular + up to 20 overtime for workshop A, 150 for workshop B), the minimum sales floors (80 microwaves, 50 water heaters), and the 5500 yuan inspection and sales cost cap.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** microwave ovens (M) and water heaters (W).
- **Objective:** minimize total cost.
- **Costs:**
  - Workshop A labor: 80 yuan/hour (same rate for regular and overtime).
  - Workshop B labor: 20 yuan/hour.
  - Inspection/sales: 30 yuan per microwave, 50 yuan per water heater, incurred per unit sold.
- **Processing hours per unit:**
  - Microwave: 2 h in A, 1 h in B.
  - Water heater: 1 h in A, 3 h in B.
- **Workshop A hours:** at least 250 regular hours must be used, plus up to 20 overtime hours allowed (max 270 total).
- **Workshop B hours:** exactly 150 hours, no overtime.
- **Sales floors:** at least 80 microwaves and at least 50 water heaters per month.
- **Sales cap:** total inspection/sales cost ≤ 5500 yuan (i.e., 30·M + 50·W ≤ 5500).
- **No other constraints:** no upper capacity limits beyond hours, no total-unit limit.
- **Integrality:** production quantities should be whole numbers (pending internal confirmation).

Model formulation (integer program):

Let M, W = integer units produced/sold per month.

Minimize:
  80·(2M + 1W) + 20·(1M + 3W) + 30M + 50W
= (160 + 20 + 30)M + (80 + 60 + 50)W
= 210M + 190W

Subject to:
- Workshop A hours: 2M + 1W ≥ 250 and 2M + 1W ≤ 270.
- Workshop B hours: 1M + 3W = 150.
- Sales floors: M ≥ 80, W ≥ 50.
- Inspection cost cap: 30M + 50W ≤ 5500.
- M, W ≥ 0 integers.

Note: Workshop B's exact 150-hour requirement (M + 3W = 150) combined with the floors M ≥ 80 and W ≥ 50 is tight — M = 80, W = 50 gives 80 + 150 = 230 ≠ 150, so the floors and the exact B-hours constraint may be jointly infeasible; this will be checked and reported in the final model.