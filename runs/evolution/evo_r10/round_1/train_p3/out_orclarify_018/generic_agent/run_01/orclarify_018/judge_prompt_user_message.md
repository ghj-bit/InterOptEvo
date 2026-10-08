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

QUESTION: The problem says to minimize overtime, but the data only gives a total of 110 weekly production hours and no separate regular-hours limit or overtime cost — so how should overtime be defined and measured in the model?

## Turn 1 - User Simulator

Overtime is any production time beyond the 110 hours of regular weekly production time. We want to keep that overtime under 10 hours per week if possible, and the goal is to minimize it as much as possible.

## Turn 2 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 production hours, which is 5 hours over the 110-hour regular limit — so is producing exactly the minimum sales quantities the intended plan, or should the model also allow producing and selling more than the minimums (using the up-to-10 overtime hours) to earn the stated profits?

## Turn 2 - User Simulator

The minimum sales quantities are the required targets. The model should allow producing and selling more than the minimums, using the up-to-10 overtime hours, to earn the stated profits.

## Turn 3 - Generic Agent

QUESTION: Since the goal is to minimize overtime, how should the model decide how much of the available overtime to actually use — should it use overtime only as much as needed to reach the minimum sales targets (i.e., 5 hours), or should it use all available overtime (up to 10 hours) to produce extra fabric for profit?

## Turn 3 - User Simulator

The model should use overtime only as much as needed to reach the minimum sales targets, which is 5 hours.

## Turn 4 - Generic Agent

QUESTION: You mentioned the factory operates two shifts — does the two-shift structure impose any constraint I should model (such as a per-shift hour limit or a requirement to split production across shifts), or is it just background information and the only time limit is the 110 regular hours plus up to 10 overtime hours?

## Turn 4 - User Simulator

It is just background information. The only time limits are the 110 regular hours plus up to 10 overtime hours.

## Turn 5 - Generic Agent

QUESTION: Since the plan is fixed at exactly the minimum sales quantities (70,000 m curtain + 45,000 m clothing) with 5 hours of overtime, is the profit per meter just informational, or should the model still report total weekly profit as an output?

## Turn 5 - User Simulator

The profit per meter is informational. The model does not need to report total weekly profit as an output.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two fabrics — curtain fabric and clothing fabric.
- **Decision variables:** Weekly production (and sales) quantity of each fabric, in meters.
- **Production rate:** 1000 meters per hour for both fabrics (shared machine/time).
- **Time limits:**
  - Regular weekly production time: 110 hours.
  - Overtime: any production time beyond 110 hours, capped at 10 hours per week.
- **Minimum sales requirements (hard constraints):**
  - Curtain fabric ≥ 70,000 meters/week.
  - Clothing fabric ≥ 45,000 meters/week.
- **Objective:** Minimize overtime hours.
- **Confirmed plan logic:** The minimums require 115,000 m total = 115 production hours, i.e., 5 hours of overtime. The model should use overtime only as much as needed to meet the minimums (5 hours), not use extra overtime to produce beyond the minimums.
- **Two shifts:** Background information only — no per-shift constraints.
- **Profit per meter (2.5 yuan curtain, 1.5 yuan clothing):** Informational only — not part of the objective and not reported as an output.

The model is a small LP: minimize overtime hours subject to the two minimum-production constraints and the total-time constraint (regular + overtime ≤ 120 hours, with overtime = total time − 110).