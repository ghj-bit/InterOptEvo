# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U5, U8, U9, U2
I need help creating a weekly production plan for two types of microcomputers in a factory, where both types require the same two production processes. The goal is to maximize total weekly profit, subject to at least 10 units of Model A being produced per week and the weekly production time for Process II being fully utilized, with potential overtime if necessary.

| Process | Model A (hours/unit) | Model B (hours/unit) | Maximum Weekly Processing Capacity (hours) |
| :---: | :---: | :---: | :---: |
| I | 4 | 6 | 150 |
| II | 3 | 2 | 70 |
| Profit ($ per unit) | 300 | 450 |  |

## Problem units
- U1 (context): I need help creating a weekly production plan for two types of microcomputers in a factory.
- U2 (data): | Process | Model A (hours/unit) | Model B (hours/unit) | Maximum Weekly Processing Capacity (hours) |
| :---: | :---: | :---: | :---: |
| I | 4 | 6 | 150 |
| II | 3 | 2 | 70 |
| Profit ($ per unit) | 300 | 450 |  |
- U3 (objective): Maximize total weekly profit.
- U4 (constraint): Total weekly profit must be at least $10,000.
- U5 (constraint): At least 10 units of Model A must be produced per week.
- U6 (constraint): At least 15 units of Model B must be produced per week.
- U7 (constraint): The weekly production time for Process I must be exactly 150 hours.
- U8 (constraint): The weekly production time for Process II should be fully utilized, with potential overtime if necessary.
- U9 (assumption): Both types of microcomputers require the same two production processes.

## Hidden slot scoring rules
## H1: minimum_profit_target
- Severity: P2
- Severity reason: The omission leaves the model as a still‑coherent pure profit maximization problem; the lower bound is a business target, not a structural necessity.
- Problem unit ID: U4
- Semantic hit rule: The Agent’s question must explicitly ask about a minimum profit requirement or a lower bound of $10,000 on weekly profit.
- Reference acceptable questions:
  - Is there a requirement that the total weekly profit must be at least $10,000?
  - Do we have a minimum profit target of $10,000 per week that must be met?
- Failure modes:
  - Assuming no minimum profit constraint is required
  - Assuming the objective is only to maximize profit without a lower bound

## H2: min_production_model_B
- Severity: P2
- Severity reason: Without this detail the model remains a valid production planning problem; the minimum quantity for Model B is a contractual preference, not a formulation‑critical gap.
- Problem unit ID: U6
- Semantic hit rule: The Agent’s question must ask about the minimum production quantity of Model B, specifically at least 15 units per week.
- Reference acceptable questions:
  - Do we have to produce at least 15 units of Model B every week?
  - Is there a contractual requirement for a minimum of 15 units of Model B per week?
- Failure modes:
  - Assuming that there is no minimum production requirement for Model B
  - Forgetting the contractual obligation for Model B

## H3: exact_process_I_time
- Severity: P2
- Severity reason: The model still works with a ≤150 capacity constraint; the exact‑150 requirement is an extra operational target, not a fatal modeling defect.
- Problem unit ID: U7
- Semantic hit rule: The Agent’s question must ask whether Process I time must be exactly 150 hours (i.e., an equality), not merely a capacity upper bound.
- Reference acceptable questions:
  - Must we use exactly 150 hours of Process I each week, not just up to 150?
  - Is it a hard requirement that Process I time equals 150 hours every week?
- Failure modes:
  - Assuming that Process I time is limited to at most 150 hours, not exactly 150
  - Treating the requirement as a simple capacity constraint


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When you say Process II must be "fully utilized, with potential overtime if necessary," do you mean (a) the base 70 hours must be completely used and any extra hours beyond 70 are allowed as overtime (with some overtime cost or limit I should know about), or (b) the 70-hour capacity is a hard ceiling and "fully utilized" simply means the constraint should be binding at the optimum?

## Turn 1 - User Simulator

It is (a). The base 70 hours must be completely used, and any extra hours beyond 70 are allowed as overtime.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how much overtime can be worked on Process II, or is overtime unlimited?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is there an overtime cost per hour on Process II that should be subtracted from profit, or is overtime free (no additional cost)?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: For Process I, is the 150-hour capacity a hard ceiling that cannot be exceeded, or can Process I also run overtime like Process II?

## Turn 4 - User Simulator

The 150-hour capacity for Process I is a hard ceiling that cannot be exceeded.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" a hard minimum that must always be met, or is it a target that could be relaxed if doing so increases profit?

## Turn 6 - User Simulator

It is a hard minimum that must always be met.

## Turn 7 - Generic Agent

QUESTION: Is there any minimum production requirement for Model B, or can Model B production be zero if that maximizes profit?

## Turn 7 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the weekly production of Model A or Model B (for example, a maximum number of units per week), or is the only upper bound the process capacities?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there any demand cap on how many units of Model A or Model B can be sold per week, or can the factory produce and sell as many as the processes allow?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints I should know about, such as a total weekly production limit, a labor-hour cap across both processes combined, or a budget constraint?

## Turn 10 - User Simulator

Yes, the total weekly profit must be at least $10,000.

## Turn 11 - Generic Agent

QUESTION: Is the $10,000 minimum weekly profit a hard constraint that must always be satisfied, or is it a target that the plan should aim for but could be missed if infeasible?

## Turn 11 - User Simulator

It is a hard constraint that must always be satisfied.

## Turn 12 - Generic Agent

QUESTION: Is there any fixed weekly cost (such as setup, overhead, or labor) that should be subtracted from the unit profits when computing the total weekly profit for the $10,000 minimum?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: When you say the base 70 hours of Process II must be "completely used," does that mean the model must use exactly 70 hours of regular time plus any overtime on top, or does it simply mean total Process II time (regular plus overtime combined) must be at least 70 hours?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any other information or constraint you can confirm now, or should I proceed with the model using the confirmed facts and reasonable assumptions for the unconfirmed items?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Products:** Two microcomputer models, A and B, both processed through Process I and Process II.
- **Objective:** Maximize total weekly profit = 300·A + 450·B.
- **Process I:** 4 hrs/unit for A, 6 hrs/unit for B; hard ceiling of 150 hours (no overtime).
- **Process II:** 3 hrs/unit for A, 2 hrs/unit for B; base capacity 70 hours must be fully utilized; overtime beyond 70 hours is permitted (overtime limit and overtime cost are unconfirmed — I will model overtime as unbounded and cost-free, i.e., total Process II time ≥ 70).
- **Minimum production:** Model A ≥ 10 units/week (hard); Model B ≥ 15 units/week (hard, contractual).
- **Minimum profit:** Total weekly profit ≥ $10,000 (hard constraint).
- **No other constraints** (no demand caps, no upper production limits, no fixed costs, no combined labor cap) were confirmed.
- **Unconfirmed items** (to be treated as assumptions in the model):
  - Overtime limit on Process II: assumed unbounded.
  - Overtime cost on Process II: assumed zero (no deduction from profit).
  - Integrality: assumed continuous (fractional units allowed).
  - Upper bounds on A and B: none.
  - Fixed weekly costs: none.
  - "Fully utilized" for Process II: interpreted as total Process II time ≥ 70 hours.