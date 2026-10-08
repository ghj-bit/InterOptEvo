# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U12, U13, U14, U2, U3, U4, U5, U6, U7, U8, U9
I need help creating a production plan for a textile factory where at least 70,000 meters of curtain fabric and 45,000 meters of clothing fabric must be sold per week, while minimizing overtime as much as possible.

The factory produces two types of fabrics: clothing fabric and curtain fabric.

The factory operates two shifts.

Weekly production time is 110 hours.

Production rate for both fabrics: 1000 meters per hour.

Minimum weekly sales of curtain fabric: 70,000 meters.

Profit for curtain fabric: 2.5 yuan per meter.

Minimum weekly sales of clothing fabric: 45,000 meters.

Profit for clothing fabric: 1.5 yuan per meter.

## Problem units
- U1 (context): I need help creating a production plan for a textile factory.
- U2 (data): The factory produces two types of fabrics: clothing fabric and curtain fabric.
- U3 (data): The factory operates two shifts.
- U4 (data): Weekly production time is 110 hours.
- U5 (data): Production rate for both fabrics: 1000 meters per hour.
- U6 (data): Minimum weekly sales of curtain fabric: 70,000 meters.
- U7 (data): Profit for curtain fabric: 2.5 yuan per meter.
- U8 (data): Minimum weekly sales of clothing fabric: 45,000 meters.
- U9 (data): Profit for clothing fabric: 1.5 yuan per meter.
- U10 (constraint): Weekly production time must fully utilize the 110 hours.
- U11 (constraint): Overtime should not exceed 10 hours per week.
- U12 (constraint): At least 70,000 meters of curtain fabric must be sold per week.
- U13 (constraint): At least 45,000 meters of clothing fabric must be sold per week.
- U14 (objective): Minimize overtime as much as possible.

## Hidden slot scoring rules
## H1: unclear_production_time_goal
- Severity: P0
- Severity reason: Without knowing that this is a goal with a specific priority and not a hard equality constraint, the model will incorrectly enforce exactly 110 hours of production time, conflicting with other objectives and missing the preemptive goal-programming structure.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must ask whether the 110-hours utilization is a hard constraint or a soft goal, and/or inquire about its priority relative to the other listed objectives.
- Reference acceptable questions:
  - Is the requirement to fully use 110 hours a strict constraint, or a target that can be over-/under‑achieved?
  - Should the goal of fully utilizing 110 hours be treated as an objective with a certain priority over the other objectives?
- Failure modes:
  - Assuming that weekly production time must equal exactly 110 hours as a rigid constraint.
  - Assuming that fully utilizing 110 hours has higher priority than the overtime-related goals without asking.

## H2: unclear_overtime_limit_goal
- Severity: P0
- Severity reason: Without clarification, the agent may treat the overtime limit as a hard constraint instead of a prioritized goal, leading to a model that cannot correctly trade off overtime against other objectives and misrepresents the real problem structure.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask about the nature of the 10-hour overtime rule (strict constraint vs. soft target) and/or its priority in the overall objective hierarchy.
- Reference acceptable questions:
  - Is the 10-hour overtime limit a strict upper bound, or is it another goal that we try to meet as closely as possible?
  - What is the priority of keeping overtime under 10 hours compared to the other objectives like minimizing overtime?
- Failure modes:
  - Assuming the 10-hour overtime limit is a rigid constraint that cannot be violated under any circumstances.
  - Assuming the overtime limit has equal weight to minimizing overtime without inquiring about preemptive priorities.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: The brief says to minimize overtime "as much as possible" while meeting minimum sales, but it also lists per-meter profits — should the objective be (a) minimize overtime hours only, with the minimum sales as hard constraints and profits unused, (b) maximize total profit subject to a cap on overtime hours, or (c) minimize overtime first and, among plans with equal overtime, maximize profit?

## Turn 1 - User Simulator

The objective is (a): minimize overtime hours only. The minimum sales requirements are hard constraints. The per-meter profit figures are not part of the objective for this plan.

## Turn 2 - Generic Agent

QUESTION: The brief states weekly production time is 110 hours, but doesn't say how much of that is regular time versus overtime — what is the regular (non-overtime) weekly production time in hours, so that overtime is the amount by which total production time exceeds it?

## Turn 2 - User Simulator

The regular weekly production time is 110 hours. Overtime is any production time beyond that 110-hour baseline.

## Turn 3 - Generic Agent

QUESTION: The 110 hours of production time — is it a single shared pool that can be split between the two fabrics (so total hours on both fabrics combined is what counts against the 110-hour baseline), or does each fabric have its own separate 110-hour pool?

## Turn 3 - User Simulator

It is a single shared pool. The total hours spent producing both fabrics combined count against the 110-hour baseline.

## Turn 4 - Generic Agent

QUESTION: The brief says the fabrics "must be sold" at minimum 70,000 and 45,000 meters per week — is production exactly equal to sales each week (no inventory carried over), so the production quantities must meet those minimums?

## Turn 4 - User Simulator

Yes, production is exactly equal to sales each week with no inventory carried over. Therefore, the production quantities must meet those minimums.

## Turn 5 - Generic Agent

QUESTION: The two shifts — do they affect the model at all (for example, a per-shift capacity limit or a rule that overtime can only occur on one shift), or are the two shifts just background detail and the only thing that matters is the total weekly hours?

## Turn 5 - User Simulator

The two shifts are just background detail. The only thing that matters is the total weekly hours.

## Turn 6 - Generic Agent

QUESTION: Is there any upper limit on how much overtime hours the factory is allowed to work per week (a maximum overtime cap), or can overtime be unlimited as long as it is minimized?

## Turn 6 - User Simulator

There is a maximum overtime cap of 10 hours per week.

## Turn 7 - Generic Agent

QUESTION: The production rate is 1000 meters per hour for both fabrics — is that rate per machine (so the two shifts or multiple machines could multiply it), or is it the factory's total combined output rate, meaning 110 hours of total time yields at most 110,000 meters across both fabrics combined?

## Turn 7 - User Simulator

It is the factory's total combined output rate. 110 hours of total time yields at most 110,000 meters across both fabrics combined.

## Turn 8 - Generic Agent

QUESTION: Since the minimums (70,000 + 45,000 = 115,000 meters) exceed the 110,000 meters producible in 110 regular hours, the plan will need overtime — is it acceptable for the model to use up to the full 10-hour overtime cap (i.e., up to 120,000 meters) to meet the minimums, or should the model instead report infeasibility if the minimums cannot be met within regular hours alone?

## Turn 8 - User Simulator

It is acceptable for the model to use up to the full 10-hour overtime cap to meet the minimums. The model should not report infeasibility if the minimums cannot be met within regular hours alone, as long as the overtime stays within the 10-hour limit.

## Turn 9 - Generic Agent

QUESTION: Can the factory produce more than the minimum sales quantities (e.g., produce 80,000 meters of curtain fabric instead of exactly 70,000), or must production be exactly at the minimums with no extra production allowed?

## Turn 9 - User Simulator

The factory can produce more than the minimum sales quantities. Production is not restricted to exactly the minimums.

## Turn 10 - Generic Agent

QUESTION: Since production can exceed the minimums, is there any upper limit on how much of each fabric can be produced per week (a maximum production cap per fabric), or is production only bounded by the total available hours (regular plus overtime)?

## Turn 10 - User Simulator

There is no upper limit on how much of each fabric can be produced per week. Production is only bounded by the total available hours (regular plus overtime).

## Turn 11 - Generic Agent

QUESTION: Since overtime is minimized and producing extra fabric beyond the minimums only adds hours, the optimal plan will produce exactly the minimums — is that the intended behavior, i.e., the factory should produce exactly 70,000 meters of curtain fabric and 45,000 meters of clothing fabric (the minimums), with no incentive to produce more?

## Turn 11 - User Simulator

Yes, that is the intended behavior. Since the objective is to minimize overtime and producing extra fabric only adds hours, the optimal plan will produce exactly 70,000 meters of curtain fabric and 45,000 meters of clothing fabric.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize overtime hours only. Per-meter profits (2.5 yuan/m curtain, 1.5 yuan/m clothing) are NOT part of the objective.
- **Decision variables:** Production quantity of curtain fabric (meters/week) and production quantity of clothing fabric (meters/week).
- **Production rate:** 1000 meters per hour, factory-wide combined (single shared pool).
- **Regular time:** 110 hours/week (baseline).
- **Overtime:** Any total production hours beyond 110 hours. Capped at 10 hours/week maximum.
- **Constraints:**
  - Curtain fabric production ≥ 70,000 meters/week (hard minimum).
  - Clothing fabric production ≥ 45,000 meters/week (hard minimum).
  - Total production hours = (curtain meters + clothing meters) / 1000 ≤ 110 + 10 = 120 hours.
  - Overtime hours = max(0, total hours − 110) ≤ 10.
- **No inventory:** Production equals sales each week.
- **No per-fabric upper cap:** Only bounded by total available hours.
- **Two shifts:** Background detail only; no per-shift constraints.
- **Expected optimal solution:** Produce exactly 70,000 m curtain + 45,000 m clothing = 115,000 m total → 115 hours → 5 hours overtime (the minimum feasible overtime).