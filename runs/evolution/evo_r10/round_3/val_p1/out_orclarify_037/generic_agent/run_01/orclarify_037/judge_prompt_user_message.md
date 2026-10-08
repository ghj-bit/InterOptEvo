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

QUESTION: When you say Process II must be "fully utilized, with potential overtime if necessary," do you mean the 70-hour capacity is a hard limit that can be exceeded only by paying an overtime premium (and if so, what is the overtime rate and any overtime cap), or do you mean the plan must use exactly 70 hours of Process II time with no overtime allowed at all?

## Turn 1 - User Simulator

The 70-hour capacity is a hard limit that can be exceeded only by paying an overtime premium.

## Turn 2 - Generic Agent

QUESTION: What is the overtime premium rate for Process II (e.g., an extra $ per overtime hour), and is there a maximum number of overtime hours allowed per week?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" a hard minimum that must always be met, or is it a target that may be relaxed if doing so would increase total weekly profit?

## Turn 3 - User Simulator

It is a hard minimum that must always be met.

## Turn 4 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or is it acceptable to treat them as continuous values in the plan?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is Process I's 150-hour capacity a hard limit that cannot be exceeded (no overtime possible on Process I), or can it also be exceeded with overtime?

## Turn 5 - User Simulator

Process I's 150-hour capacity is a hard limit that cannot be exceeded.

## Turn 6 - Generic Agent

QUESTION: Since the overtime premium rate and any overtime cap for Process II are still pending internal confirmation, should I proceed by modeling Process II with a 70-hour regular limit plus an overtime variable that is only allowed when the 70 hours are fully used, and leave the overtime cost as a parameter to be filled in later?

## Turn 6 - User Simulator

Yes, that approach is acceptable.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products/decisions:** Weekly production quantities of Model A and Model B. Integrality is pending internal confirmation, so I will treat them as continuous non-negative variables (and note that integer versions can be enforced if confirmed).
- **Objective:** Maximize total weekly profit = 300·A + 450·B, minus any overtime premium cost on Process II (overtime cost is a parameter to be filled in later, per your approval).
- **Process I:** 4·A + 6·B ≤ 150 (hard limit, no overtime).
- **Process II:** Regular capacity 70 hours, hard limit; overtime is allowed only after the 70 regular hours are fully used. I will model this with a regular-time variable capped at 70 and an overtime variable, with the constraint that overtime can be positive only when regular time equals 70 (i.e., 3·A + 2·B = 70 + OT, 0 ≤ regular ≤ 70, and OT > 0 implies regular = 70). The overtime premium rate and any overtime cap are left as parameters pending internal confirmation.
- **Model A minimum:** A ≥ 10 (hard minimum, always enforced).
- **Non-negativity:** A, B ≥ 0.

I will now formulate the model accordingly.