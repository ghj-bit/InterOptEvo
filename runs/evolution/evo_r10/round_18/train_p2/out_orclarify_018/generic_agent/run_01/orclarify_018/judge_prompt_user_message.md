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

QUESTION: You mention minimizing overtime, but the brief only states a fixed 110 hours of weekly production time and no overtime rate, cost, or cap — could you clarify what overtime means here (e.g., hours beyond 110, at what cost or rate) and whether the 110 hours is a hard limit or a baseline that can be exceeded?

## Turn 1 - User Simulator

The 110 hours is a baseline that can be exceeded. Overtime refers to any production hours beyond those 110 hours. We want to keep overtime under 10 hours per week if possible.

## Turn 2 - Generic Agent

QUESTION: You want to keep overtime under 10 hours "if possible" — is the 10-hour cap a hard limit that must never be exceeded, or is it a soft target where exceeding it is allowed but penalized in the objective?

## Turn 2 - User Simulator

The 10-hour cap is a hard limit that must not be exceeded.

## Turn 3 - Generic Agent

QUESTION: The minimum sales (70,000 m curtain + 45,000 m clothing = 115,000 m) require 115 production hours at 1000 m/h, which already exceeds the 110-hour baseline by 5 hours — so overtime is unavoidable. Given that, is the objective purely to minimize overtime hours (i.e., produce exactly the minimums and no more), or should the plan also consider profit (e.g., produce extra fabric when it doesn't add overtime, or trade off profit against overtime)?

## Turn 3 - User Simulator

The objective is purely to minimize overtime hours. We do not need to consider profit in the production plan.

## Turn 4 - Generic Agent

QUESTION: Since the minimum sales alone (115,000 m) require 115 hours — already 5 hours of overtime — is the plan simply to produce exactly the minimum amounts (70,000 m curtain, 45,000 m clothing) and nothing more, or could the factory produce extra fabric beyond the minimums (e.g., to use up available hours) as long as overtime stays within the 10-hour cap?

## Turn 4 - User Simulator

The plan should produce exactly the minimum amounts (70,000 m curtain, 45,000 m clothing) and nothing more.

## Turn 5 - Generic Agent

QUESTION: You mentioned the factory operates two shifts — does the 110-hour baseline split evenly across the two shifts (55 hours each), and is there any per-shift limit on how much overtime can be assigned, or is overtime just a single weekly total that must stay under 10 hours regardless of how it's distributed across shifts?

## Turn 5 - User Simulator

I need to check internally how the 110 hours are split between the two shifts and whether there are per-shift overtime limits.

## Turn 6 - Generic Agent

QUESTION: While you check the shift split, here's a structural point to confirm: since the plan is fixed at exactly 70,000 m curtain and 45,000 m clothing (115 hours total, 5 hours overtime), does the model need to decide *how* to allocate production across the two shifts, or is the shift structure just background information and the plan only needs to report total weekly production and total overtime?

## Turn 6 - User Simulator

The shift structure is just background information. The plan only needs to report total weekly production and total overtime.

## Turn 7 - Generic Agent

QUESTION: Just to confirm the final structure: the model's decision is simply how many meters of each fabric to produce (with the constraint that each meets its minimum sales requirement), the objective is to minimize total overtime hours (total production hours minus 110, capped at 10), and since producing exactly the minimums already minimizes overtime, the optimal solution is 70,000 m curtain + 45,000 m clothing = 115 hours = 5 hours overtime — is that the complete picture, or is there any additional constraint or decision I'm missing?

## Turn 7 - User Simulator

That is the complete picture.

## Turn 8 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Problem:** Production plan for a textile factory producing two fabrics (curtain and clothing).

**Decision variables:**
- x₁ = meters of curtain fabric produced per week (continuous, non-negative)
- x₂ = meters of clothing fabric produced per week (continuous, non-negative)

**Parameters:**
- Production rate: 1,000 meters per hour (both fabrics)
- Baseline weekly production time: 110 hours
- Overtime cap: 10 hours (hard limit)
- Minimum curtain fabric sales: 70,000 meters/week
- Minimum clothing fabric sales: 45,000 meters/week

**Objective:** Minimize total overtime hours = (total production hours − 110), subject to overtime ≤ 10.

**Constraints:**
1. x₁ ≥ 70,000 (minimum curtain fabric)
2. x₂ ≥ 45,000 (minimum clothing fabric)
3. (x₁ + x₂) / 1000 − 110 ≤ 10 (overtime cap, i.e., total production hours ≤ 120)
4. x₁, x₂ ≥ 0

**Key facts confirmed:**
- The 110 hours is a baseline that can be exceeded; overtime = hours beyond 110.
- The 10-hour overtime cap is a hard limit.
- Profit is not part of the objective; the sole goal is minimizing overtime.
- The plan produces exactly the minimums and nothing more.
- Shift structure is background only; the plan reports total weekly production and total overtime.
- No per-shift constraints are needed.

**Expected optimal solution:** x₁ = 70,000 m, x₂ = 45,000 m → 115 production hours → 5 hours overtime (the minimum possible, since 115,000 m ÷ 1,000 m/h = 115 h > 110 h baseline).