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

QUESTION: When you say "minimizing overtime as much as possible," is overtime a cost to be minimized in the objective (with a per-hour overtime cost), or is it a hard constraint that overtime must be zero (i.e., all production must fit within the 110 regular hours)?

## Turn 1 - User Simulator

It is a cost to be minimized in the objective. We do not require overtime to be zero; we simply want to keep it as low as possible, ideally under 10 hours per week.

## Turn 2 - Generic Agent

QUESTION: What is the overtime cost per hour that should be used in the objective function?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: The brief says weekly production time is 110 hours and the factory operates two shifts — is 110 hours the total regular (non-overtime) capacity available per week, with any production beyond 110 hours counted as overtime?

## Turn 3 - User Simulator

Yes, 110 hours is the total regular (non-overtime) capacity available per week. Any production beyond 110 hours is counted as overtime.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum limit on how many overtime hours per week the factory is allowed to work (a hard cap), or is overtime unlimited and only penalized by its cost in the objective?

## Turn 4 - User Simulator

There is a hard cap: overtime should not exceed 10 hours per week.

## Turn 5 - Generic Agent

QUESTION: The minimum sales are 70,000 m of curtain and 45,000 m of clothing, which together need 115,000 m of production (115 hours at 1000 m/hour) — more than the 110 regular hours. So the sales minimums must be treated as production minimums that force at least 5 hours of overtime. Is that the intended reading: produce at least these amounts, and any production above the minimums is allowed and earns profit?

## Turn 5 - User Simulator

Yes, that is the intended reading. The minimum sales figures are production minimums. Since 115,000 meters requires 115 hours, this forces at least 5 hours of overtime. Production above these minimums is allowed and earns profit.

## Turn 6 - Generic Agent

QUESTION: Since producing more than the minimums earns profit but also consumes capacity (and possibly more overtime), is there any upper limit on total weekly production or on the production of each fabric, or can the factory produce unlimited amounts as long as total hours stay within 110 regular plus 10 overtime hours?

## Turn 6 - User Simulator

There is no upper limit on total weekly production or on the production of each fabric. The factory can produce unlimited amounts as long as total hours stay within 110 regular plus 10 overtime hours.

## Turn 7 - Generic Agent

QUESTION: Is the production rate of 1000 meters per hour the same for both fabrics regardless of which shift they are produced on, or does the rate differ between the two shifts?

## Turn 7 - User Simulator

The production rate of 1000 meters per hour is the same for both fabrics regardless of which shift they are produced on.

## Turn 8 - Generic Agent

QUESTION: The brief mentions two shifts — does the shift structure affect the model in any way (for example, different costs, different capacities, or a requirement to split production across shifts), or is it just background information and the model only needs to track total hours (regular vs. overtime)?

## Turn 8 - User Simulator

It is just background information. The model only needs to track total hours (regular vs. overtime).

## Turn 9 - Generic Agent

QUESTION: The overtime cost per hour still needs internal confirmation — for now, should I treat it as a parameter (a variable to be filled in later) in the model, or would you like me to proceed with a placeholder value?

## Turn 9 - User Simulator

Please treat it as a parameter to be filled in later.

## Turn 10 - Generic Agent

QUESTION: The objective is to minimize overtime cost, but producing above the minimums earns profit — should the objective be purely minimizing overtime cost (ignoring profit), or should it be maximizing net profit (profit from all production minus overtime cost)?

## Turn 10 - User Simulator

The objective is purely minimizing overtime cost.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Facility:** A textile factory producing two fabrics — curtain fabric and clothing fabric.
- **Capacity:** 110 hours of regular (non-overtime) production time per week. Overtime is allowed up to a hard cap of 10 hours per week. Total available time: up to 120 hours.
- **Production rate:** 1,000 meters per hour for both fabrics, same on both shifts. Shifts are background only; the model tracks total hours (regular vs. overtime).
- **Decision variables:**
  - Curtain fabric produced (meters), ≥ 70,000
  - Clothing fabric produced (meters), ≥ 45,000
  - Overtime hours used, 0 ≤ overtime ≤ 10
- **Capacity constraint:** (Curtain meters + Clothing meters) / 1000 ≤ 110 + overtime hours
- **Objective:** Minimize overtime cost = (overtime cost per hour, a parameter to be filled in later) × overtime hours. Profit figures (2.5 yuan/m curtain, 1.5 yuan/m clothing) are noted but do not enter the objective.
- **No upper bounds** on production of either fabric beyond the capacity constraint.
- **Note:** The minimums (70,000 + 45,000 = 115,000 m = 115 hours) exceed the 110 regular hours, so at least 5 hours of overtime is forced.