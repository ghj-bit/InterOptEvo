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

QUESTION: Is the goal to minimize total overtime hours (with the 110 hours being regular time and overtime being any additional hours needed), or is the goal to minimize overtime cost, and if so, what is the overtime rate per hour?

## Turn 1 - User Simulator

The goal is to minimize total overtime hours. The 110 hours are the regular production time, and overtime is any additional hours needed beyond that. We do not have a specific overtime cost rate to minimize; the objective is simply to keep the number of overtime hours as low as possible.

## Turn 2 - Generic Agent

QUESTION: Is there a maximum limit on how many overtime hours can be worked per week, or is overtime unlimited as long as it is minimized?

## Turn 2 - User Simulator

There is a maximum limit. Overtime should not exceed 10 hours per week.

## Turn 3 - Generic Agent

QUESTION: The 110 regular hours plus up to 10 overtime hours gives at most 120 hours, which at 1000 meters/hour yields at most 120,000 meters total, but the minimum sales alone require 115,000 meters — so production must be at least 115,000 meters. Is production exactly equal to sales each week (no inventory carried over), or can the factory produce more than it sells and hold the surplus as inventory?

## Turn 3 - User Simulator

Production is exactly equal to sales each week. There is no inventory carried over.

## Turn 4 - Generic Agent

QUESTION: The two shifts — do they affect the model in any way (for example, a per-shift capacity limit, a shift-specific production rate, or a rule that overtime can only be worked on one shift), or are the two shifts just background information and the only relevant capacity is the 110 regular hours plus up to 10 overtime hours?

## Turn 4 - User Simulator

The two shifts are just background information. The only relevant capacity is the 110 regular hours plus up to 10 overtime hours.

## Turn 5 - Generic Agent

QUESTION: The brief lists a profit per meter for each fabric, but the stated goal is to minimize overtime hours. Should profit play any role in the model — for example, as a secondary objective (minimize overtime first, then maximize profit among plans with the same overtime), or as a constraint (e.g., total weekly profit must reach some minimum) — or should profit be ignored entirely and the only objective be minimizing overtime hours?

## Turn 5 - User Simulator

Profit should be ignored entirely. The only objective is minimizing overtime hours.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Weekly production (and sales, which are equal) of curtain fabric (meters) and clothing fabric (meters), plus overtime hours.
- **Demand (minimum sales):** Curtain fabric ≥ 70,000 m/week; clothing fabric ≥ 45,000 m/week.
- **Production = sales:** No inventory; production exactly equals sales each week.
- **Capacity:** 110 regular hours/week + up to 10 overtime hours/week (overtime capped at 10).
- **Production rate:** 1,000 meters per hour for both fabrics (combined).
- **Objective:** Minimize total overtime hours. Profit is ignored entirely.
- **Shifts:** Background only; no per-shift constraints.

Model sketch:
- Minimize OT
- s.t. curtain ≥ 70,000; clothing ≥ 45,000
- (curtain + clothing) / 1000 ≤ 110 + OT
- 0 ≤ OT ≤ 10

Note: minimum sales alone require 115,000 m = 115 hours, so the optimum will use exactly 5 overtime hours (115 − 110), with production split at the minimums (70,000 curtain + 45,000 clothing).