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

QUESTION: Is the 70-hour capacity for Process II a hard upper limit that cannot be exceeded, or is it a baseline capacity that can be extended through overtime (and if overtime is allowed, what is the maximum additional overtime hours permitted per week)?

## Turn 1 - User Simulator

The 70-hour capacity for Process II is a baseline capacity that can be extended through overtime. There is no maximum additional overtime hours permitted per week; overtime is allowed as necessary to fully utilize the process.

## Turn 2 - Generic Agent

QUESTION: When you say Process II must be "fully utilized," do you mean the total hours used (including any overtime) must be at least 70, or do you mean the total hours used must be at least 70 plus whatever overtime is added, making the constraint effectively that Process II hours are never below 70?

## Turn 2 - User Simulator

The constraint is that the total hours used for Process II must be at least 70.

## Turn 3 - Generic Agent

QUESTION: Is the 150-hour capacity for Process I a hard upper limit that cannot be exceeded, or can it also be extended through overtime?

## Turn 3 - User Simulator

The 150-hour capacity for Process I is a hard upper limit that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the requirement of at least 10 units of Model A per week a hard minimum that must be met, or is it a soft target that can be relaxed if it conflicts with other constraints?

## Turn 4 - User Simulator

The requirement of at least 10 units of Model A per week is a hard minimum that must be met.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities for Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values in the plan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Should the production quantities for Model A and Model B be treated as non-negative values, meaning zero production of either model is allowed as long as the other constraints are satisfied?

## Turn 6 - User Simulator

No, zero production of either model is not allowed. There are hard minimums: at least 10 units of Model A and at least 15 units of Model B must be produced each week.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model A or Model B, or is the only upper bound on each model's quantity determined by the process capacity constraints?

## Turn 7 - User Simulator

There is no separate maximum weekly production limit for Model A or Model B. The only upper bounds on each model's quantity are determined by the process capacity constraints.

## Turn 8 - Generic Agent

QUESTION: Are the profit figures of $300 per unit for Model A and $450 per unit for Model B the total weekly profit contribution per unit, or are they per-unit values that need to be multiplied by the number of units produced to get total profit?

## Turn 8 - User Simulator

They are per-unit values that need to be multiplied by the number of units produced to get total profit.

## Turn 9 - Generic Agent

QUESTION: Are there any additional constraints or requirements not yet mentioned, such as conditional linkages between the two models, minimum quantities tied to a decision being active, or dependencies between the two production processes?

## Turn 9 - User Simulator

No, there are no additional constraints or requirements beyond those already mentioned.

## Turn 10 - Generic Agent

QUESTION: Should the production quantities for Model A and Model B be treated as whole numbers (integer units), or can they be treated as continuous values in the plan?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model A or Model B, or is the only upper bound on each model's quantity determined by the process capacity constraints?

## Turn 11 - User Simulator

There is no separate maximum weekly production limit for Model A or Model B. The only upper bounds on each model's quantity are determined by the process capacity constraints.

## Turn 12 - Generic Agent

QUESTION: Are the profit figures of $300 per unit for Model A and $450 per unit for Model B the total weekly profit contribution per unit, or are they per-unit values that need to be multiplied by the number of units produced to get total profit?

## Turn 12 - User Simulator

They are per-unit values that need to be multiplied by the number of units produced to get total profit.

## Turn 13 - Generic Agent

QUESTION: Are there any additional constraints or requirements not yet mentioned, such as conditional linkages between the two models, minimum quantities tied to a decision being active, or dependencies between the two production processes?

## Turn 13 - User Simulator

No, there are no additional constraints or requirements beyond those already mentioned.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Maximize total weekly profit, calculated as 300 × (units of Model A) + 450 × (units of Model B).
- **Decision Variables:** Weekly production quantities for Model A and Model B.
- **Variable Domain:** Non-negative continuous values (integrality is unconfirmed and assumed continuous for now).
- **Constraints:**
  - Process I: 4 × (Model A) + 6 × (Model B) ≤ 150 hours (hard upper limit).
  - Process II: 3 × (Model A) + 2 × (Model B) ≥ 70 hours (hard lower limit; overtime allowed with no upper cap).
  - Model A minimum: Model A ≥ 10 units (hard minimum).
  - Model B minimum: Model B ≥ 15 units (hard minimum).
- **No other constraints** exist beyond those listed.

**Open Assumptions:**
- Production quantities are treated as continuous (not required to be integers). If integer production is required, the model would need to be reformulated as an integer program.