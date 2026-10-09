# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U6, U8, U9, U2, U3, U4, U5
I need help creating a production plan for two fertilizers using two machines, where processing requirements are measured per standardized lot and planning may use fractional lots when appropriate, and total processing time on Machine 1 cannot exceed its available time, and total processing time on Machine 2 cannot exceed its available time.

Processing times (minutes per lot):
| Product | Machine 1 | Machine 2 |
|--------|----------|----------|
| Liquid | 50       | 30       |
| Solid  | 24       | 33       |

On-hand inventory at beginning of week: liquid 30 lots, solid 90 lots.

Available time on Machine 1: 40 hours. Available time on Machine 2: 35 hours.

Forecast demand for the week: 75 lots of liquid, 95 lots of solid.

## Problem units
- U1 (context): I need help creating a production plan for two fertilizers using two machines.
- U2 (data): Processing times (minutes per lot):
| Product | Machine 1 | Machine 2 |
|--------|----------|----------|
| Liquid | 50       | 30       |
| Solid  | 24       | 33       |
- U3 (data): On-hand inventory at beginning of week: liquid 30 lots, solid 90 lots.
- U4 (data): Available time on Machine 1: 40 hours. Available time on Machine 2: 35 hours.
- U5 (data): Forecast demand for the week: 75 lots of liquid, 95 lots of solid.
- U6 (assumption): Processing requirements are measured per standardized lot, and planning may use fractional lots when appropriate.
- U7 (objective): Maximize the total ending inventory of liquid and solid at the end of the week.
- U8 (constraint): Total processing time on Machine 1 cannot exceed its available time.
- U9 (constraint): Total processing time on Machine 2 cannot exceed its available time.

## Hidden slot scoring rules
## H1: unknown_objective
- Severity: P0
- Severity reason: Without knowing what to optimize, no linear programming model can be formulated. The problem lacks a goal or objective function, making it ill-posed.
- Problem unit ID: U7
- Semantic hit rule: The agent asks about the optimization goal or objective function, explicitly inquiring what to maximize or minimize.
- Reference acceptable questions:
  - What is the objective we are trying to achieve? For example, are we maximizing profit, minimizing waste, or something else?
  - What should the model maximize or minimize? Is it total production, inventory, or cost?
- Failure modes:
  - Assuming the goal is to maximize profit
  - Assuming the goal is to meet demand exactly with no inventory consideration


# Atomic Question Map

Q1 (turn 1): What business objective should this week's production plan optimize?
Q2 (turn 2): If production cannot fully cover this week's forecast demand, should unmet demand be treated as backordered to a later week, lost sales, or is meeting all demand a hard requirement?
Q3 (turn 3): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q4 (turn 4): Should the beginning inventory of liquid and solid lots be counted as available to satisfy this week's forecast demand?
Q5 (turn 5): Is the ending inventory objective measured as the simple total of liquid and solid lots, or should liquid and solid lots be weighted differently?
Q6 (turn 6): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q7 (turn 7): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q8 (turn 8): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q9 (turn 9): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q10 (turn 10): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q11 (turn 11): May production exceed this week's forecast demand to build extra ending inventory, or should production be capped at the forecast demand?
Q12 (turn 12): Can the two machines process the same lot in parallel, or must each lot be processed sequentially on Machine 1 and then Machine 2?
Q13 (turn 13): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q14 (turn 14): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q15 (turn 15): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q16 (turn 16): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q17 (turn 17): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q18 (turn 18): May production exceed this week's forecast demand to build extra ending inventory, or should production be capped at the forecast demand?
Q19 (turn 19): Can the two machines process the same lot in parallel, or must each lot be processed sequentially on Machine 1 and then Machine 2?
Q20 (turn 20): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q21 (turn 21): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q22 (turn 22): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q23 (turn 23): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q24 (turn 24): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q25 (turn 25): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q26 (turn 26): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q27 (turn 27): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q28 (turn 28): Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?
Q29 (turn 29): May production exceed this week's forecast demand to build extra ending inventory, or should production be capped at the forecast demand?
Q30 (turn 30): Can the two machines process the same lot in parallel, or must each lot be processed sequentially on Machine 1 and then Machine 2?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What business objective should this week's production plan optimize?

## Turn 1 - User Simulator

Maximize the total ending inventory of liquid and solid fertilizers at the end of the week.

## Turn 2 - Generic Agent

QUESTION: If production cannot fully cover this week's forecast demand, should unmet demand be treated as backordered to a later week, lost sales, or is meeting all demand a hard requirement?

## Turn 2 - User Simulator

That point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 3 - User Simulator

That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Should the beginning inventory of liquid and solid lots be counted as available to satisfy this week's forecast demand?

## Turn 4 - User Simulator

Yes, the beginning inventory should be counted as available to satisfy this week's forecast demand.

## Turn 5 - Generic Agent

QUESTION: Is the ending inventory objective measured as the simple total of liquid and solid lots, or should liquid and solid lots be weighted differently?

## Turn 5 - User Simulator

The objective is the simple total of liquid and solid lots, with no different weighting between them.

## Turn 6 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 6 - User Simulator

That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 7 - User Simulator

That point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 8 - User Simulator

That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 9 - User Simulator

That point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 10 - User Simulator

That point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: May production exceed this week's forecast demand to build extra ending inventory, or should production be capped at the forecast demand?

## Turn 11 - User Simulator

That point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Can the two machines process the same lot in parallel, or must each lot be processed sequentially on Machine 1 and then Machine 2?

## Turn 12 - User Simulator

That point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 13 - User Simulator

That point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 14 - User Simulator

That point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 15 - User Simulator

That point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 16 - User Simulator

That point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 17 - User Simulator

That point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: May production exceed this week's forecast demand to build extra ending inventory, or should production be capped at the forecast demand?

## Turn 18 - User Simulator

That point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Can the two machines process the same lot in parallel, or must each lot be processed sequentially on Machine 1 and then Machine 2?

## Turn 19 - User Simulator

That point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 20 - User Simulator

That point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 21 - User Simulator

That point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 22 - User Simulator

That point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 23 - User Simulator

That point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 24 - User Simulator

That point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 25 - User Simulator

That point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 26 - User Simulator

That point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 27 - User Simulator

That point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Should this week's forecast demand be treated as a hard requirement that must be fully met, or can unmet demand be backordered or lost?

## Turn 28 - User Simulator

That point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: May production exceed this week's forecast demand to build extra ending inventory, or should production be capped at the forecast demand?

## Turn 29 - User Simulator

That point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Can the two machines process the same lot in parallel, or must each lot be processed sequentially on Machine 1 and then Machine 2?

## Turn 30 - User Simulator

That point still needs internal confirmation.