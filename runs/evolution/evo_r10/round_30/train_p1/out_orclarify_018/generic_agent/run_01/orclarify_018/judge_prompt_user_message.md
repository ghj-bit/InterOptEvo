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

QUESTION: The brief says to minimize overtime "as much as possible" while also giving per-meter profits — should the objective be (a) minimize overtime hours first, with profit only a tie-breaker, (b) maximize profit first, with overtime only a tie-breaker, or (c) a single weighted objective that trades the two off (e.g., profit minus a cost per overtime hour)?

## Turn 1 - User Simulator

The objective is (a): minimize overtime hours first, with profit only a tie-breaker.

## Turn 2 - Generic Agent

QUESTION: The 110 weekly production hours — is that the regular (non-overtime) capacity, with any production beyond 110 hours counting as overtime, or is 110 hours the total available time including any overtime?

## Turn 2 - User Simulator

The 110 hours is the regular (non-overtime) capacity. Any production beyond 110 hours counts as overtime.

## Turn 3 - Generic Agent

QUESTION: The two shifts — do they affect the model at all (e.g., a per-shift limit on hours or on overtime), or is the only thing that matters the total weekly hours of 110 regular plus any overtime?

## Turn 3 - User Simulator

The two shifts do not affect the model. The only thing that matters is the total weekly hours of 110 regular plus any overtime.

## Turn 4 - Generic Agent

QUESTION: Is there any upper limit on how many overtime hours can be worked in a week, or can overtime be as large as needed to meet the sales minimums?

## Turn 4 - User Simulator

There is an upper limit: overtime should not exceed 10 hours per week.

## Turn 5 - Generic Agent

QUESTION: The 1000 meters per hour rate — is that the combined rate when both fabrics are produced (i.e., total meters of both fabrics per hour of machine time), or does each fabric have its own 1000 m/h line so they can be produced simultaneously?

## Turn 5 - User Simulator

The 1000 meters per hour is the combined rate. It represents the total meters of both fabrics produced per hour of machine time.

## Turn 6 - Generic Agent

QUESTION: The 70,000 and 45,000 meter figures are minimums that must be sold — can the factory produce and sell more than these minimums (with the extra counted in profit), or must production be exactly at these minimums?

## Turn 6 - User Simulator

The factory can produce and sell more than these minimums. The 70,000 and 45,000 meter figures are minimums, not exact targets.

## Turn 7 - Generic Agent

QUESTION: Since production can exceed the minimums, is there any upper limit on how much of each fabric can be produced or sold per week (e.g., a demand ceiling), or is the only cap the total available machine hours (110 regular + up to 10 overtime)?

## Turn 7 - User Simulator

There is no upper limit on how much of each fabric can be produced or sold per week. The only cap is the total available machine hours (110 regular + up to 10 overtime).

## Turn 8 - Generic Agent

QUESTION: If two production plans use the same minimum overtime hours, the tie-breaker is profit — should that tie-breaker maximize total profit (2.5 yuan per meter of curtain fabric plus 1.5 yuan per meter of clothing fabric), or is there a different profit measure you want used?

## Turn 8 - User Simulator

The tie-breaker should maximize total profit, calculated as 2.5 yuan per meter of curtain fabric plus 1.5 yuan per meter of clothing fabric.

## Turn 9 - Generic Agent

QUESTION: Is all fabric produced in a week assumed to be sold in that same week (no inventory carried over), so that production quantity equals sales quantity for each fabric?

## Turn 9 - User Simulator

Yes, all fabric produced in a week is assumed to be sold in that same week. Production quantity equals sales quantity for each fabric.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Weekly production (and thus sales) quantity of each fabric, in meters. Both are continuous and non-negative.
- **Machine capacity:** 110 regular hours per week, plus up to 10 overtime hours (overtime capped at 10). Combined production rate is 1000 meters per hour of machine time (both fabrics share the same machine time).
- **Minimum sales (floors):** Curtain fabric ≥ 70,000 m/week; clothing fabric ≥ 45,000 m/week. Production may exceed these minimums; there is no upper limit on production or sales of either fabric.
- **No inventory:** Production equals sales within the week.
- **Two shifts:** Irrelevant to the model; only total weekly hours matter.
- **Objective (lexicographic):**
  1. **Primary:** Minimize overtime hours (overtime = machine hours used beyond 110, capped at 10).
  2. **Tie-breaker:** Maximize total profit = 2.5 yuan/meter (curtain) + 1.5 yuan/meter (clothing).

Note on feasibility: minimums require (70,000 + 45,000)/1000 = 115 hours, which exceeds the 110 regular hours, so at least 5 overtime hours are unavoidable; the model will find the minimum overtime (5 hours) and, among all plans using exactly 5 overtime hours, the one with maximum profit.