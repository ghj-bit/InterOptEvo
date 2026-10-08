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

QUESTION: The brief says to minimize overtime, but it doesn't define what overtime is or how it relates to the 110 weekly production hours — is the 110 hours the regular (non-overtime) capacity, with any production beyond it counted as overtime hours to be minimized, or is 110 hours the total available time and "overtime" refers to something else (e.g., a second shift beyond the first)?

## Turn 1 - User Simulator

The 110 hours is the regular (non-overtime) capacity. Any production time beyond those 110 hours is counted as overtime, and that overtime is what we want to minimize.

## Turn 2 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 hours at 1,000 m/h, which already exceeds the 110 regular hours — so is the objective purely to minimize overtime hours (with the sales minimums as hard constraints, meaning at least 5 hours of overtime is unavoidable), or should the model also be allowed to produce and sell more than the minimums if that somehow reduces overtime?

## Turn 2 - User Simulator

The sales minimums are hard constraints. The objective is purely to minimize overtime hours. Producing more than the minimums would not reduce overtime, so the model should focus on meeting the minimums with the least amount of overtime.

## Turn 3 - Generic Agent

QUESTION: The brief mentions two shifts, but doesn't say how the 110 regular hours are split between them or whether that split matters — is the 110 hours simply a single total regular capacity that can be used for either fabric in any mix, or are there per-shift hour limits (e.g., a fixed number of hours per shift) that constrain how much of each fabric can be produced?

## Turn 3 - User Simulator

The 110 hours is a single total regular capacity that can be used for either fabric in any mix. There are no per-shift hour limits that constrain the production of each fabric.

## Turn 4 - Generic Agent

QUESTION: Is there any upper limit on how much overtime hours the factory can use per week, or is overtime unlimited as long as it is minimized?

## Turn 4 - User Simulator

There is an upper limit. Overtime should not exceed 10 hours per week.

## Turn 5 - Generic Agent

QUESTION: The brief lists profit per meter for both fabrics, but the stated objective is to minimize overtime — is profit completely irrelevant to the model, or should it play some role (e.g., as a secondary objective to maximize among plans with equal overtime, or as a constraint on minimum weekly profit)?

## Turn 5 - User Simulator

Profit is completely irrelevant to the model. The sole objective is to minimize overtime.

## Turn 6 - Generic Agent

QUESTION: Since the production rate is the same for both fabrics (1,000 m/h) and the only constraints are the two sales minimums plus the 110 regular hours and 10 overtime cap, the total production time is fixed at 115 hours regardless of the mix — is there any constraint that ties the split of production time between the two fabrics (e.g., a maximum or minimum share of time for one fabric), or is the split between curtain and clothing production completely free as long as each fabric's minimum is met?

## Turn 6 - User Simulator

The split between curtain and clothing production is completely free as long as each fabric's minimum is met. There are no constraints tying the split of production time between the two fabrics.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Production rate:** 1,000 meters per hour for both fabrics (same rate).
- **Regular capacity:** 110 hours per week, usable for either fabric in any mix (no per-shift or per-fabric hour limits; the two shifts are irrelevant to the model).
- **Overtime:** Any production time beyond the 110 regular hours is overtime; overtime is capped at 10 hours per week.
- **Sales minimums (hard constraints):** At least 70,000 m of curtain fabric and at least 45,000 m of clothing fabric must be produced/sold per week.
- **Production split:** Completely free between the two fabrics as long as each minimum is met; no constraint ties the time split.
- **Objective:** Minimize overtime hours. Profit figures (2.5 and 1.5 yuan/m) are irrelevant and excluded from the model.
- **Implication:** Total required production is 115,000 m = 115 hours, so at least 5 hours of overtime is unavoidable; the model will confirm the minimum overtime is 5 hours (within the 10-hour cap).