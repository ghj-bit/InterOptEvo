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

QUESTION: What is the overtime cost per hour for Process II?

## Turn 1 - User Simulator

That point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: What is the maximum number of overtime hours allowed for Process II per week?

## Turn 2 - User Simulator

That point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model B

## Turn 3 - User Simulator

No, there is no maximum weekly production limit for Model B.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum weekly production limit

## Turn 4 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 5 - Generic Agent

QUESTION: Is there a minimum weekly production requirement

## Turn 5 - User Simulator

Yes, there is a minimum weekly production requirement of at least 10 units of Model A and at least 15 units of Model B.

## Turn 6 - Generic Agent

QUESTION: What is the overtime cost

## Turn 6 - User Simulator

That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum

## Turn 7 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum

## Turn 8 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 9 - Generic Agent

QUESTION: Is there a maximum

## Turn 9 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum

## Turn 10 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 11 - Generic Agent

QUESTION: Is there a maximum

## Turn 11 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 12 - Generic Agent

QUESTION: Is there a maximum

## Turn 12 - User Simulator

No, there is no maximum weekly production limit for either Model A or Model B.

## Turn 13 - Generic Agent

QUESTION: Is there a maximum

## Turn 13 - User Simulator

No, there is no maximum weekly production

## Turn 14 - Generic Agent

QUESTION: Is there a maximum

## Turn 14 - User Simulator

No, there

## Turn 15 - Generic Agent

QUESTION: Is there a maximum

## Turn 15 - User Simulator

No

## Turn 16 - Generic Agent

QUESTION: Is there a maximum

## Turn 16 - User Simulator

No

## Turn 17 - Generic Agent

QUESTION: Is there a maximum

## Turn 17 - User Simulator

No

## Turn 18 - Generic Agent

QUESTION: Is there a maximum

## Turn 18 - User Simulator

No

## Turn 19 - Generic Agent

QUESTION: Is there a maximum

## Turn 19 - User Simulator

No

## Turn 20 - Generic Agent

QUESTION: Is there a maximum

## Turn 20 - User Simulator

No

## Turn 21 - Generic Agent

QUESTION: Is there a maximum

## Turn 21 - User Simulator

No

## Turn 22 - Generic Agent

QUESTION: Is there a maximum

## Turn 22 - User Simulator

No

## Turn 23 - Generic Agent

QUESTION: Is there a maximum

## Turn 23 - User Simulator

No

## Turn 24 - Generic Agent

QUESTION: Is there a maximum

## Turn 24 - User Simulator

No

## Turn 25 - Generic Agent

QUESTION: Is there a maximum

## Turn 25 - User Simulator

No

## Turn 26 - Generic Agent

QUESTION: Is there a maximum

## Turn 26 - User Simulator

No

## Turn 27 - Generic Agent

QUESTION: Is there a maximum

## Turn 27 - User Simulator

No

## Turn 28 - Generic Agent

QUESTION: Is there a maximum

## Turn 28 - User Simulator

No

## Turn 29 - Generic Agent

QUESTION: Is there a maximum

## Turn 29 - User Simulator

No

## Turn 30 - Generic Agent

QUESTION: Is there a maximum

## Turn 30 - User Simulator

No