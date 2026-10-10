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

QUESTION: Is the 70-hour maximum weekly capacity for Process II a hard limit that cannot be exceeded, or is it a regular-time capacity that can be exceeded through overtime (and if overtime is allowed, what is the overtime cost per hour and is there a maximum overtime limit)?

## Turn 1 - User Simulator

The 70-hour figure is the regular-time capacity. It is not a hard limit; we can exceed it through overtime if necessary.

I do not have the overtime cost per hour or a maximum overtime limit available in the current business facts. That point still needs internal confirmation.

## Turn 2 - Generic Agent

QUESTION: Since the overtime cost and limit are unconfirmed, should I treat the 70-hour Process II capacity as a hard upper bound (no overtime allowed) for now, or should I treat Process II as having no upper bound at all (unlimited overtime at zero cost) for the purpose of the model?

## Turn 2 - User Simulator

Treat the 70-hour Process II capacity as a hard upper bound (no overtime allowed) for now.

## Turn 3 - Generic Agent

QUESTION: Is the 150-hour maximum weekly capacity for Process I also a hard upper bound that cannot be exceeded, or can it also be exceeded through overtime?

## Turn 3 - User Simulator

The 150-hour capacity for Process I is a hard upper bound that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the requirement of at least 10 units of Model A per week a hard minimum constraint that must be satisfied, or is it a target that can be relaxed if it conflicts with other constraints?

## Turn 4 - User Simulator

The requirement of at least 10 units of Model A per week is a hard minimum constraint that must be satisfied.

## Turn 5 - Generic Agent

QUESTION: Should the number of units produced for Model A and Model B be restricted to whole numbers (integers), or can they be treated as continuous values (allowing fractional units) in the model?

## Turn 5 - User Simulator

The number of units produced for Model A and Model B should be restricted to whole numbers (integers).

## Turn 6 - Generic Agent

QUESTION: Should the production quantities for Model A and Model B be allowed to be zero, or is there a minimum production requirement for Model B as well?

## Turn 6 - User Simulator

There is a minimum production requirement for Model B: at least 15 units must be produced per week.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements I should be aware of, such as maximum production limits for either model, or any other resource limitations beyond the two processes?

## Turn 7 - User Simulator

Yes, there are two additional requirements:

1. The total weekly profit must be at least $10,000.
2. The weekly production time for Process I must be exactly 150 hours, not just up to 150.

## Turn 8 - Generic Agent

QUESTION: Is the requirement that weekly production time for Process I must be exactly 150 hours a hard equality constraint that must be satisfied, or is it a target that can be relaxed if it conflicts with other constraints?

## Turn 8 - User Simulator

The requirement that weekly production time for Process I must be exactly 150 hours is a hard equality constraint that must be satisfied.

## Turn 9 - Generic Agent

QUESTION: Is the requirement that total weekly profit must be at least $10,000 a hard constraint that must be satisfied, or is it a target that can be relaxed if it conflicts with other constraints?

## Turn 9 - User Simulator

The requirement that total weekly profit must be at least $10,000 is a hard constraint that must be satisfied.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:**
- Maximize total weekly profit (confirmed)

**Decision Variables:**
- Model A units produced per week (integer, non-negative) (confirmed)
- Model B units produced per week (integer, non-negative) (confirmed)

**Hard Constraints:**
1. Process I capacity: 4A + 6B = 150 hours (hard equality constraint) (confirmed)
2. Process II capacity: 3A + 2B ≤ 70 hours (hard upper bound, no overtime) (confirmed)
3. Minimum Model A production: A ≥ 10 units (hard minimum) (confirmed)
4. Minimum Model B production: B ≥ 15 units (hard minimum) (confirmed)
5. Minimum total profit: 300A + 450B ≥ $10,000 (hard minimum) (confirmed)

**Data:**
- Process I: Model A requires 4 hours/unit, Model B requires 6 hours/unit
- Process II: Model A requires 3 hours/unit, Model B requires 2 hours/unit
- Profit: Model A $300/unit, Model B $450/unit

**Open Assumptions:**
- None. All formulation-critical facts have been confirmed.