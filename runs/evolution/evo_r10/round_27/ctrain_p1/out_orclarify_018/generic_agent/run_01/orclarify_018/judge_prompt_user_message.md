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

QUESTION: What is the maximum number of overtime hours available per week?

## Turn 1 - User Simulator

The maximum overtime available is 10 hours per week.

## Turn 2 - Generic Agent

QUESTION: Is the 110 hours of weekly production time the regular (non-overtime) time, with overtime added on top for a total of up to 120 hours?

## Turn 2 - User Simulator

Yes, the 110 hours is the regular production time, and overtime is added on top of that.

## Turn 3 - Generic Agent

QUESTION: Is the 1000 meters per hour production rate the same for both fabrics regardless of which shift (regular or overtime) is being used?

## Turn 3 - User Simulator

Yes, the production rate is 1000 meters per hour for both fabrics, regardless of the shift.

## Turn 4 - Generic Agent

QUESTION: Can the factory produce more than the minimum sales amounts (70,000 m curtain, 45,000 m clothing) and sell the extra, or must production exactly match the minimum sales?

## Turn 4 - User Simulator

The factory can produce more than the minimum sales amounts and sell the extra.

## Turn 5 - Generic Agent

QUESTION: Since the objective is to minimize overtime, is there any profit or revenue consideration in the objective, or is the sole goal to use as few overtime hours as possible (with the sales minimums as constraints)?

## Turn 5 - User Simulator

The sole goal is to use as few overtime hours as possible. The sales minimums are constraints.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how much total fabric can be produced or sold per week (e.g., a maximum production capacity or demand cap), or is the only upper bound the 120 total hours (110 regular + 10 overtime)?

## Turn 6 - User Simulator

The only upper bound is the 120 total hours (110 regular + 10 overtime).

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints I should be aware of, such as a minimum or maximum production requirement for each fabric type, or any relationship between the two fabrics' production?

## Turn 7 - User Simulator

No, there are no other constraints.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Facility:** A textile factory producing two fabrics: curtain fabric and clothing fabric.
- **Time:** Regular production time is 110 hours/week. Overtime is available up to 10 hours/week, for a maximum total of 120 hours/week.
- **Production rate:** 1000 meters per hour for both fabrics, on both regular and overtime shifts.
- **Decision variables:** How many hours of regular time and overtime time are allocated to each fabric (or equivalently, how many meters of each fabric are produced, subject to the total time cap).
- **Constraints:**
  - Curtain fabric produced/sold ≥ 70,000 meters/week.
  - Clothing fabric produced/sold ≥ 45,000 meters/week.
  - Total production time (regular + overtime) ≤ 120 hours/week.
  - Regular time used ≤ 110 hours/week.
  - Overtime used ≤ 10 hours/week.
  - Production can exceed the minimums (no upper cap beyond the time limit).
- **Objective:** Minimize total overtime hours used.
- **Profit figures** (2.5 yuan/m for curtain, 1.5 yuan/m for clothing) are provided but do not enter the objective, which is purely overtime minimization.
- **No other constraints** (no per-fabric caps, no coupling between fabrics).

The model is a small linear program: allocate regular and overtime hours across the two fabrics to meet the minimum sales while using as little overtime as possible.