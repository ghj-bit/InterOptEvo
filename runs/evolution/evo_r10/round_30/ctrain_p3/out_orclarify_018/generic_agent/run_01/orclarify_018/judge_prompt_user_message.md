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

QUESTION: The brief says to minimize overtime "as much as possible" while also giving per-meter profits — should the objective be purely minimizing overtime hours (with the 70,000 m and 45,000 m sales treated as hard minimums), or should it be maximizing total weekly profit subject to some overtime limit, or a weighted combination of both?

## Turn 1 - User Simulator

The objective is purely to minimize overtime hours. The 70,000 meters of curtain fabric and 45,000 meters of clothing fabric are hard minimums that must be met. The per-meter profits are not part of the optimization objective.

## Turn 2 - Generic Agent

QUESTION: The brief states weekly production time is 110 hours, but the minimum sales alone (70,000 + 45,000 = 115,000 meters at 1,000 m/hour) require 115 hours — so at least 5 hours of overtime is unavoidable. Is 110 hours the regular (non-overtime) time available per week, with overtime being any hours beyond it, or does 110 hours already include some overtime?

## Turn 2 - User Simulator

The 110 hours is the regular (non-overtime) time available per week. Overtime is any hours beyond that 110-hour limit.

## Turn 3 - Generic Agent

QUESTION: The brief mentions the factory operates two shifts — does this two-shift structure impose any constraint on the model (for example, a per-shift hour limit, or a requirement that production be split across the two shifts), or is it just background information and the only time constraint is the 110 regular hours plus overtime?

## Turn 3 - User Simulator

The two-shift structure is just background information. It does not impose any additional constraints on the model. The only time constraints are the 110 regular hours and the overtime limit.

## Turn 4 - Generic Agent

QUESTION: You mentioned an "overtime limit" — is there a maximum number of overtime hours allowed per week (a hard cap), or is overtime unlimited and the model simply minimizes how much is used?

## Turn 4 - User Simulator

There is a maximum of 10 overtime hours allowed per week. This is a hard cap.

## Turn 5 - Generic Agent

QUESTION: The minimum sales (115,000 m) require 115 hours, which fits within 110 regular + 10 overtime = 120 hours. If the factory can produce more than the minimums, is there any upper limit on how much of each fabric can be produced or sold per week, or can production exceed the minimums freely as long as total hours stay within 120?

## Turn 5 - User Simulator

There is no upper limit on how much of each fabric can be produced or sold per week. Production can exceed the minimums freely as long as total hours stay within the 120-hour limit (110 regular + 10 overtime).

## Turn 6 - Generic Agent

QUESTION: Since the minimums alone (115,000 m) require 115 hours, the model will always use at least 5 overtime hours. If the factory produces exactly the minimums, overtime is 5 hours. Is there any reason the factory would want to produce MORE than the minimums (which would use more overtime), or should the model simply produce exactly the minimums and accept the 5 overtime hours as the unavoidable minimum?

## Turn 6 - User Simulator

The model should simply produce exactly the minimums and accept the 5 overtime hours as the unavoidable minimum. There is no reason to produce more than the minimums, as that would only increase overtime.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Minimize overtime hours per week.
- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Production rate:** 1,000 meters per hour for both fabrics (shared machine/time).
- **Regular time available:** 110 hours per week.
- **Overtime:** Any hours beyond 110; hard cap of 10 overtime hours (so max total = 120 hours).
- **Hard minimums (sales/production):**
  - Curtain fabric: ≥ 70,000 meters/week
  - Clothing fabric: ≥ 45,000 meters/week
- **No upper bounds** on production beyond the total time limit.
- **Two-shift structure:** Background only; no additional constraints.
- **Profits (2.5 and 1.5 yuan/m):** Not part of the objective; informational only.
- **Key insight:** Minimums require 115,000 m → 115 hours → 5 hours overtime is unavoidable. Producing more would only increase overtime, so the optimal solution produces exactly the minimums with 5 overtime hours.

The model is straightforward:
- Decision variables: hours allocated to curtain fabric (h_c) and clothing fabric (h_l).
- Constraints:
  - 1000·h_c ≥ 70,000 (curtain minimum)
  - 1000·h_l ≥ 45,000 (clothing minimum)
  - h_c + h_l ≤ 120 (total time cap)
  - Overtime = max(0, h_c + h_l − 110)
- Objective: Minimize overtime.
- Optimal: h_c = 70, h_l = 45, total = 115, overtime = 5 hours.