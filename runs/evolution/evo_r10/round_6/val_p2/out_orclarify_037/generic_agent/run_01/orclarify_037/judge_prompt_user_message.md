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

QUESTION: When you say Process II's weekly production time must be "fully utilized, with potential overtime if necessary," do you mean the model should require exactly 70 hours of Process II work (forcing overtime to be paid whenever the natural optimum would use less), or should 70 hours be a minimum that must be met with overtime allowed only as a way to exceed 70 hours when the plan calls for more?

## Turn 1 - User Simulator

It should be a minimum that must be met. The plan must use at least 70 hours of Process II time. Overtime is allowed only if the plan calls for more than 70 hours.

## Turn 2 - Generic Agent

QUESTION: If the plan calls for more than 70 hours of Process II time, is there a maximum overtime limit (in hours) that Process II can exceed its 70-hour capacity, or can overtime be unlimited?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For Process I, is its 150-hour weekly capacity a hard limit that cannot be exceeded (no overtime allowed), or can Process I also run overtime beyond 150 hours?

## Turn 3 - User Simulator

Process I's 150-hour weekly capacity is a hard limit that cannot be exceeded. No overtime is allowed for Process I.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum weekly production quantity (a ceiling) for Model A or Model B, or can the factory produce any non-negative number of each model as long as the process capacities are respected?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or is it acceptable to treat them as continuous values (e.g., 12.5 units) in the plan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: If the plan uses more than 70 hours of Process II (overtime), is there an additional overtime cost per hour that should be subtracted from profit, or is overtime free and only the regular per-unit profits of $300 (A) and $450 (B) count toward the objective?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there any demand or minimum production requirement for Model B, or is Model B free to be zero if the plan prefers it?

## Turn 7 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" a hard minimum that must be met in every week, or is it a target that could be relaxed if doing so would increase profit?

## Turn 8 - User Simulator

It is a hard minimum that must be met every week.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how many units of Model A can be produced per week (a maximum), or is Model A only constrained by the "at least 10" minimum and the process capacities?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: For the overtime on Process II, is there a maximum number of overtime hours allowed per week (e.g., no more than 20 hours of overtime), or is overtime unlimited as long as it's needed?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there an overtime cost per hour for Process II that should be subtracted from the profit objective, or is overtime free (no additional cost) and only the regular per-unit profits count?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional values?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is there a maximum weekly production quantity (a ceiling) for Model B, or is Model B only constrained by the "at least 15" minimum and the process capacities?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any other constraint or requirement I haven't asked about that would affect the production plan, such as a limit on total units produced, a minimum profit target, or a constraint on the ratio of Model A to Model B?

## Turn 14 - User Simulator

Yes, the total weekly profit must be at least $10,000.

## Turn 15 - Generic Agent

QUESTION: Is the $10,000 minimum weekly profit a hard constraint that must be met (making the problem infeasible if it can't be achieved), or is it a target that the plan should aim for but could potentially fall short of?

## Turn 15 - User Simulator

Yes, our goal is that the total weekly profit should not be less than $10,000.

## Turn 16 - Generic Agent

QUESTION: Is the $10,000 minimum profit a hard constraint that must be satisfied (making the plan infeasible if it can't be met), or is it a soft target that the plan should aim for but could potentially fall short of?

## Turn 16 - User Simulator

It is a hard constraint that must be satisfied.

## Turn 17 - Generic Agent

QUESTION: Is there any limit on the total number of units (Model A + Model B) that can be produced per week, or is total output only constrained by the process capacities?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or is overtime unlimited as long as it's needed to meet the production plan?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there an overtime cost per hour for Process II that should be subtracted from the profit objective, or is overtime free (no additional cost) and only the regular per-unit profits of $300 (A) and $450 (B) count toward the $10,000 minimum and the maximization objective?

## Turn 19 - User Simulator

The point

## Turn 20 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional values in the plan?

## Turn 20 - User Simulator

The point still needs

## Turn 21 - Generic Agent

QUESTION: Is there a maximum weekly production quantity (a ceiling) for Model A, or is Model A only constrained by the "at least 10" minimum and the process capacities?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Is there a maximum weekly production quantity (a ceiling) for Model B, or is Model B only constrained by the "at least 15" minimum and the process capacities?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or is overtime unlimited as long as it's needed to meet the production plan?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Is there an overtime cost per hour for Process II that should be subtracted from the profit objective, or is overtime free (no additional cost) and only the regular per-unit profits of $300 (A) and $450 (B) count toward the objective?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional values in the plan?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Is there a maximum weekly production quantity (a ceiling) for Model A, or is Model A only constrained by the "at least 10" minimum and the process capacities?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Is there a maximum weekly production quantity (a ceiling) for Model B, or is Model B only constrained by the "at least 15" minimum and the process capacities?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or is overtime unlimited as long as it's needed to meet the production plan?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is there an overtime cost per hour for Process II that should be subtracted from the profit objective, or is overtime free (no additional cost) and only the regular per-unit profits of $300 (A) and $450 (B) count toward the objective?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Are the production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional values in the plan?

## Turn 30 - User Simulator

The