# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U7, U2, U3
I need help creating a production plan for a beverage factory over a four-week horizon, where weekly production cannot exceed the production capacity for that week, and beverages remaining at the end of a week can be stored for use in later weeks, incurring the storage cost.

| Week | Demand (1000 boxes) | Production Capacity (1000 boxes) | Cost per 1000 boxes (1000 yuan) |
|------|---------------------|----------------------------------|----------------------------------|
| 1    | 15                  | 30                               | 5.0                              |
| 2    | 25                  | 40                               | 5.1                              |
| 3    | 35                  | 45                               | 5.4                              |
| 4    | 25                  | 20                               | 5.5                              |
| Total | 100                 | 135                              |                                  |

Storage cost: 0.2 thousand yuan per week per thousand boxes of beverages.

## Problem units
- U1 (context): I need help creating a production plan for a beverage factory over a four-week horizon.
- U2 (data): | Week | Demand (1000 boxes) | Production Capacity (1000 boxes) | Cost per 1000 boxes (1000 yuan) |
|------|---------------------|----------------------------------|----------------------------------|
| 1    | 15                  | 30                               | 5.0                              |
| 2    | 25                  | 40                               | 5.1                              |
| 3    | 35                  | 45                               | 5.4                              |
| 4    | 25                  | 20                               | 5.5                              |
| Total | 100                 | 135                              |                                  |
- U3 (data): Storage cost: 0.2 thousand yuan per week per thousand boxes of beverages.
- U4 (objective): Minimize the total cost (the sum of production cost and storage cost) over the four weeks.
- U5 (constraint): Weekly market demand must be met.
- U6 (constraint): Weekly production cannot exceed the production capacity for that week.
- U7 (assumption): Beverages remaining at the end of a week can be stored for use in later weeks, incurring the storage cost.

## Hidden slot scoring rules
## H1: minimize_total_production_and_storage_cost
- Severity: P0
- Severity reason: Without the objective, the agent has no basis to define what constitutes an optimal plan; the problem is undefined and cannot be formulated.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must explicitly ask about the cost objective, indicating uncertainty about whether storage cost is included or what costs are minimized.
- Reference acceptable questions:
  - What exactly are we trying to minimize? Is it the total production cost plus storage cost over the whole period?
  - Should the objective be to minimize the sum of production and inventory holding costs across all four weeks?
- Failure modes:
  - Assuming the objective is to minimize only production cost
  - Assuming the objective is to maximize profit without a selling price
  - Assuming the objective is to minimize the total number of boxes produced

## H2: demand_must_be_met_each_week
- Severity: P1
- Severity reason: Missing this constraint could lead to a model where demand is not fully satisfied, which would produce a materially invalid business plan, even though the optimization would remain mathematically coherent.
- Problem unit ID: U5
- Semantic hit rule: The agent's question must explicitly ask about demand satisfaction obligations, such as whether demand must be fully met each week or if backlog/unmet demand is allowed.
- Reference acceptable questions:
  - Do we have to satisfy the demand completely each week, or can we backorder or leave some demand unmet?
  - Is it mandatory to meet all weekly demand, or can we have a shortfall and make up later?
- Failure modes:
  - Silently assuming backorders are allowed with a penalty cost
  - Assuming unmet demand is lost and considered acceptable
  - Assuming demand is a soft target that can be partially fulfilled


# Atomic Question Map

Q1 (turn 1): Must the factory satisfy all demand in each week, or can demand be backlogged or left unmet?
Q2 (turn 2): Is there any beverage inventory already available at the beginning of week 1, and if so, how much?
Q3 (turn 3): Can weekly production be any fractional amount in 1000-box units, or must it be a whole number of 1000-box units?
Q4 (turn 4): Is the storage cost charged on the inventory remaining at the end of each week, or on the average inventory held during the week?
Q5 (turn 5): Is there any beverage inventory already available at the beginning of week 1, and if so, how much?
Q6 (turn 6): Must all inventory be used by the end of week 4, or is ending inventory allowed or required?
Q7 (turn 7): Should the plan be built assuming zero initial inventory and zero required ending inventory, with these treated as standard planning assumptions until confirmed otherwise?
Q8 (turn 8): Can weekly production be any fractional amount in 1000-box units, or must it be a whole number of 1000-box units?
Q9 (turn 9): Should the plan be built assuming fractional production in 1000-box units is allowed, with this treated as a standard planning assumption until confirmed otherwise?
Q10 (turn 10): Should the production plan minimize total production cost plus storage cost, or only storage cost?
Q11 (turn 11): Are there any minimum weekly production levels, startup/shutdown requirements, or limits on how much production can change from one week to the next?
Q12 (turn 12): Should the plan be built assuming no minimum weekly production levels, no startup/shutdown requirements, and no limits on week-to-week production changes, with these treated as standard planning assumptions until confirmed otherwise?
Q13 (turn 13): Can beverages produced in earlier weeks be stored and used to meet a later week's demand, or must each week's demand be met entirely by that week's production?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Must the factory satisfy all demand in each week, or can demand be backlogged or left unmet?

## Turn 1 - User Simulator

All demand must be met each week. There is no option to postpone or leave demand unmet.

## Turn 2 - Generic Agent

QUESTION: Is there any beverage inventory already available at the beginning of week 1, and if so, how much?

## Turn 2 - User Simulator

That point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Can weekly production be any fractional amount in 1000-box units, or must it be a whole number of 1000-box units?

## Turn 3 - User Simulator

That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the storage cost charged on the inventory remaining at the end of each week, or on the average inventory held during the week?

## Turn 4 - User Simulator

The storage cost is charged on the beverages remaining at the end of a week that are stored for use in later weeks.

## Turn 5 - Generic Agent

QUESTION: Is there any beverage inventory already available at the beginning of week 1, and if so, how much?

## Turn 5 - User Simulator

That point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Must all inventory be used by the end of week 4, or is ending inventory allowed or required?

## Turn 6 - User Simulator

That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Should the plan be built assuming zero initial inventory and zero required ending inventory, with these treated as standard planning assumptions until confirmed otherwise?

## Turn 7 - User Simulator

Yes, that is fine as a standard planning assumption until confirmed otherwise.

## Turn 8 - Generic Agent

QUESTION: Can weekly production be any fractional amount in 1000-box units, or must it be a whole number of 1000-box units?

## Turn 8 - User Simulator

That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Should the plan be built assuming fractional production in 1000-box units is allowed, with this treated as a standard planning assumption until confirmed otherwise?

## Turn 9 - User Simulator

Yes, that is fine as a standard planning assumption until confirmed otherwise.

## Turn 10 - Generic Agent

QUESTION: Should the production plan minimize total production cost plus storage cost, or only storage cost?

## Turn 10 - User Simulator

It should minimize total production cost plus storage cost.

## Turn 11 - Generic Agent

QUESTION: Are there any minimum weekly production levels, startup/shutdown requirements, or limits on how much production can change from one week to the next?

## Turn 11 - User Simulator

That point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Should the plan be built assuming no minimum weekly production levels, no startup/shutdown requirements, and no limits on week-to-week production changes, with these treated as standard planning assumptions until confirmed otherwise?

## Turn 12 - User Simulator

Yes, that is fine as a standard planning assumption until confirmed otherwise.

## Turn 13 - Generic Agent

QUESTION: Can beverages produced in earlier weeks be stored and used to meet a later week's demand, or must each week's demand be met entirely by that week's production?

## Turn 13 - User Simulator

Beverages produced in earlier weeks can be stored and used to meet a later week's demand.

## Turn 14 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.850

Confidence rationale: All structural elements are now settled: demand must be met each week, inventory can be carried forward to meet later demand, storage cost is charged on end-of-week inventory, the objective minimizes production plus storage cost, and weekly capacity is a hard limit. The only remaining gap is production integrality, which the user has repeatedly deferred and which we have agreed to treat as a standard planning assumption (fractional production allowed) until confirmed otherwise. This assumption is explicitly flagged, so a unique linear formulation can proceed.

Summary: Four-week beverage production planning model. Decision variables: production quantity and end-of-week inventory for each week. Objective: minimize total production cost (weekly cost per 1000 boxes times production) plus storage cost (0.2 thousand yuan per 1000 boxes per week on end-of-week inventory). Constraints: weekly production cannot exceed weekly capacity; each week's demand must be fully met from that week's production plus carried-over inventory; inventory balance links weeks. Assumptions (pending internal confirmation): zero initial inventory, zero required ending inventory, fractional production in 1000-box units allowed, and no minimum production levels, startup/shutdown requirements, or week-to-week change limits.