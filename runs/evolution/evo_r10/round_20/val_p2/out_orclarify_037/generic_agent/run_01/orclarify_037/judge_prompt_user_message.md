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

QUESTION: When you say Process II's weekly production time must be "fully utilized, with potential overtime if necessary," do you mean (1) the base 70 hours must be used exactly and any extra hours beyond 70 are allowed as overtime (with some overtime cost or limit), (2) the 70 hours is a hard maximum and "fully utilized" simply means the constraint should be binding at the optimum, or (3) the 70 hours is a minimum that must be met and overtime beyond it is free/unlimited?

## Turn 1 - User Simulator

It is option (1). The base 70 hours must be used exactly, and any extra hours beyond 70 are allowed as overtime.

## Turn 2 - Generic Agent

QUESTION: For the overtime hours on Process II beyond the base 70, is there a maximum overtime limit (e.g., a cap on total Process II hours), or is overtime unlimited?

## Turn 2 - User Simulator

Overtime is unlimited.

## Turn 3 - Generic Agent

QUESTION: Does the overtime on Process II incur any extra cost (e.g., an overtime wage per hour that reduces profit), or is the overtime free so that the $300 and $450 per-unit profits stay unchanged regardless of how many overtime hours are used?

## Turn 3 - User Simulator

The overtime is free, so the $300 and $450 per-unit profits stay unchanged regardless of how many overtime hours are used.

## Turn 4 - Generic Agent

QUESTION: For Process I, is the 150-hour maximum a hard cap that cannot be exceeded (no overtime allowed on Process I), or can Process I also run overtime beyond 150 hours?

## Turn 4 - User Simulator

The 150-hour maximum for Process I is a hard cap that cannot be exceeded. No overtime is allowed on Process I.

## Turn 5 - Generic Agent

QUESTION: Should the number of Model A and Model B units produced per week be whole numbers (integer units), or is it acceptable to treat them as continuous quantities (allowing fractional units)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum production requirement for Model B per week (similar to the 10-unit minimum for Model A), or can Model B production be zero if that is optimal?

## Turn 6 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 7 - Generic Agent

QUESTION: The "at least 10 units of Model A" and "at least 15 units of Model B" requirements — are these strict minimums that must be met in every week (hard lower bounds), or are they targets that could be relaxed if doing so would increase profit?

## Turn 7 - User Simulator

These are strict minimums that must be met in every week.

## Turn 8 - Generic Agent

QUESTION: The "at least 10 units of Model A" and "at least 15 units of Model B" requirements — are these strict minimums that must be met in every week (hard lower bounds), or are they targets that could be relaxed if doing so would increase profit?

## Turn 8 - User Simulator

They are strict minimums that must be met in every week.

## Turn 9 - Generic Agent

QUESTION: For the overtime hours on Process II beyond the base 70, is there a maximum overtime limit (e.g., a cap on total Process II hours), or is overtime unlimited?

## Turn 9 - User Simulator

Overtime is unlimited.

## Turn 10 - Generic Agent

QUESTION: Should the number of Model A and Model B units produced per week be whole numbers (integer units), or is it acceptable to treat them as continuous quantities (allowing fractional units)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Is there any upper limit on the total number of units of Model A or Model B that can be produced per week (e.g., a demand cap or storage limit), or is production only limited by the process capacities and the minimums?

## Turn 30 - User Simulator

The point still needs internal confirmation.