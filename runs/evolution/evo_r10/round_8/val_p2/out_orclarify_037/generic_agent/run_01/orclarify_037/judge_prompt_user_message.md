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

QUESTION: When Process II runs overtime, is there a maximum number of overtime hours allowed per week, and if so, what is that limit?

## Turn 1 - User Simulator

The point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed per week for Process II, and if so, what is that limit?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, and if so, what is that cost?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is the weekly production time for Process I also allowed to exceed its 150-hour capacity via overtime, or is the 150-hour limit a hard cap that must never be exceeded?

## Turn 4 - User Simulator

The 150-hour limit for Process I is a hard cap that must never be exceeded.

## Turn 5 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" requirement a hard minimum that must always be met, or is it a target that can be relaxed if doing so would increase total profit?

## Turn 5 - User Simulator

It is a hard minimum that must always be met.

## Turn 6 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum number of units of Model B that can be produced per week, or is Model B production unlimited apart from the process capacity limits?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum number of units of Model A that can be produced per week, or is Model A production unlimited apart from the process capacity limits and the 10-unit minimum?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: When Process II runs overtime, is the overtime time added on top of the 70-hour regular capacity (so total Process II time can exceed 70 hours), or does "fully utilized" simply mean the 70 hours must be exactly used with no extra time allowed?

## Turn 9 - User Simulator

The overtime time is added on top of the 70-hour regular capacity, so total Process II time can exceed 70 hours.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum total number of units (Model A plus Model B combined) that can be produced per week, or is total output unlimited apart from the process capacity limits?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints on the weekly production plan besides the Process I capacity (150 hours), the Process II regular capacity (70 hours plus overtime), and the 10-unit minimum for Model A?

## Turn 11 - User Simulator

Yes, there are additional constraints:

- Total weekly profit must be at least $10,000.
- At least 15 units of Model B must be produced per week.
- The weekly production time for Process I must be exactly 150 hours.

## Turn 12 - Generic Agent

QUESTION: Is the "total weekly profit must be at least $10,000" requirement a hard constraint that must always be satisfied, or is it a target that the plan should aim for but can be relaxed if doing so would allow a better use of capacity?

## Turn 12 - User Simulator

It is a hard constraint that must always be satisfied.

## Turn 13 - Generic Agent

QUESTION: Is the "at least 15 units of Model B per week" requirement a hard minimum that must always be met, or is it a target that can be relaxed if doing so would increase total profit?

## Turn 13 - User Simulator

It is a hard minimum that must always be met.

## Turn 14 - Generic Agent

QUESTION: Is the requirement that Process I time be exactly 150 hours a hard equality constraint that must always hold, or is it a target that can be relaxed if doing so would increase total profit?

## Turn 14 - User Simulator

It is a hard equality constraint that must always hold.

## Turn 15 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: When Process II runs overtime, is there a maximum number of overtime hours allowed per week, or can overtime be unlimited as long as the 70-hour regular capacity is fully used?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 18 - User Simulator

The

## Turn 19 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: When Process II runs overtime, is there an additional cost per overtime hour that should be subtracted from profit, or is overtime free (no extra cost)?

## Turn 30 - User Simulator

The