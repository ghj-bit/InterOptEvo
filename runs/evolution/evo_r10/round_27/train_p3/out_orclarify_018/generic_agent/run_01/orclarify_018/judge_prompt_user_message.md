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

QUESTION: The brief says to minimize overtime, but it doesn't define what overtime is — is overtime the number of hours worked beyond the 110 weekly hours (i.e., total production hours minus 110), and is there any upper limit on how much overtime is allowed per week?

## Turn 1 - User Simulator

Yes, overtime is the number of hours worked beyond the 110 weekly hours. There is an upper limit: overtime should not exceed 10 hours per week.

## Turn 2 - Generic Agent

QUESTION: The brief mentions two shifts but doesn't say how the 110 weekly hours are split between them — is the 110-hour weekly capacity simply the total available regular time (with the two shifts being just context), or does each shift have its own separate capacity that I need to track in the model?

## Turn 2 - User Simulator

The 110-hour weekly capacity is simply the total available regular time. The two shifts are just context; you do not need to track separate capacities for each shift in the model.

## Turn 3 - Generic Agent

QUESTION: The brief says at least 70,000 meters of curtain fabric and 45,000 meters of clothing fabric "must be sold" — is production allowed to exceed these minimums (i.e., produce and sell more than 70,000/45,000 meters), or must production be exactly equal to these minimums?

## Turn 3 - User Simulator

Production is allowed to exceed these minimums. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are minimum weekly sales requirements, not exact targets.

## Turn 4 - Generic Agent

QUESTION: The brief gives profit per meter for each fabric but says the goal is to minimize overtime — is profit part of the objective at all (for example, maximize profit subject to minimizing overtime, or a weighted combination), or is profit just background information and the sole objective is to minimize overtime hours?

## Turn 4 - User Simulator

Profit is just background information. The sole objective is to minimize overtime hours.

## Turn 5 - Generic Agent

QUESTION: Since the sole objective is to minimize overtime, and the minimum sales requirements (70,000 + 45,000 = 115,000 meters at 1,000 meters/hour = 115 hours) already exceed the 110 regular hours, the model will always use exactly 5 hours of overtime regardless of how production is split — is that the intended situation, or is there some flexibility I'm missing, such as the sales minimums being per-fabric but production of one fabric being able to substitute for the other?

## Turn 5 - User Simulator

That is the intended situation. The minimum sales requirements are per-fabric and cannot be substituted for one another. Therefore, the model will always require at least 5 hours of overtime to meet the minimums.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Facility**: A textile factory producing two fabric types — curtain fabric and clothing fabric.
- **Decision variables**: Weekly production (and sales) of curtain fabric (meters) and clothing fabric (meters), both continuous and non-negative.
- **Capacity**: Total regular weekly production time is 110 hours. Overtime is the hours worked beyond 110, capped at 10 hours per week (so total production time ≤ 120 hours). The two shifts are context only; no per-shift tracking is needed.
- **Production rate**: 1,000 meters per hour for both fabrics (shared rate, so total production time = (curtain meters + clothing meters) / 1000).
- **Minimum sales requirements**: At least 70,000 meters of curtain fabric and at least 45,000 meters of clothing fabric per week. These are floors, not exact targets — production may exceed them, but the two fabrics cannot substitute for each other.
- **Objective**: Minimize overtime hours = max(0, total production hours − 110). Profit figures (2.5 yuan/m for curtain, 1.5 yuan/m for clothing) are background information only and do not enter the objective.
- **Known consequence**: Meeting the minimums requires 115,000 meters = 115 hours, so the model will always use at least 5 hours of overtime; the optimum is 5 overtime hours with production exactly at the minimums (any extra production only adds overtime).