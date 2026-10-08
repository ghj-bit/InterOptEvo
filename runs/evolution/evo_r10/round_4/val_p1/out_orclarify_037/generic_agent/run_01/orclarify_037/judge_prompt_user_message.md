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

QUESTION: When you say Process II's weekly production time must be "fully utilized," do you mean the total hours used on Process II must be exactly 70 (i.e., 3A + 2B = 70), or that it must be at least 70 with overtime allowed to cover any excess (i.e., 3A + 2B ≥ 70, with overtime hours beyond 70 permitted and presumably charged at some cost)?

## Turn 1 - User Simulator

It must be at least 70, with overtime allowed to cover any excess.

## Turn 2 - Generic Agent

QUESTION: You mentioned overtime is allowed for Process II if necessary — is there any overtime cost (e.g., an extra $ per overtime hour) that should be subtracted from profit, or is overtime free and the only limit is that Process II has no hard cap beyond regular capacity?

## Turn 2 - User Simulator

I need to check with our finance team to confirm whether there is a specific overtime cost per hour that should be subtracted from profit.

## Turn 3 - Generic Agent

QUESTION: For Process I, is the 150-hour maximum a hard cap (no overtime allowed, so 4A + 6B ≤ 150), or can Process I also run overtime beyond 150 hours if needed?

## Turn 3 - User Simulator

The 150 hours for Process I is a hard cap. No overtime is allowed for Process I.

## Turn 4 - Generic Agent

QUESTION: For the "at least 10 units of Model A per week" requirement — is 10 a strict minimum floor (A ≥ 10, with no upper limit on A other than the process capacities), or is there also a maximum number of Model A units that can be produced per week?

## Turn 4 - User Simulator

10 is a strict minimum floor. There is no upper limit on Model A units other than the process capacities.

## Turn 5 - Generic Agent

QUESTION: Should the number of units produced for each model (A and B) be whole numbers (integer units), or is it acceptable to treat them as continuous quantities (e.g., 12.5 units) for planning purposes?

## Turn 5 - User Simulator

The number of units produced for each model must be whole numbers.

## Turn 6 - Generic Agent

QUESTION: Since overtime on Process II is allowed to cover hours beyond 70, is there any upper limit on how many overtime hours Process II can run (e.g., a maximum total of regular + overtime hours), or can Process II run for as many hours as needed with no cap?

## Turn 6 - User Simulator

I need to check with our operations team to confirm whether there is an upper limit on total overtime hours for Process II.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints I should be aware of — for example, a minimum production requirement for Model B, a maximum total number of units of either model, or any demand limits on how many units of A or B can actually be sold per week?

## Turn 7 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is there also a maximum number of Model B units that can be produced per week (a demand or sales cap), or is 15 simply a floor with no upper limit on B other than the process capacities?

## Turn 8 - User Simulator

15 is simply a floor. There is no upper limit on Model B units other than the process capacities.

## Turn 9 - Generic Agent

QUESTION: Regarding the overtime cost for Process II that you're still confirming with finance — for now, should I model overtime as having zero additional cost (i.e., overtime hours are free, and the only effect is that Process II has no hard cap beyond 70 hours), or would you prefer I include a placeholder overtime cost variable that you can fill in once finance confirms the rate?

## Turn 9 - User Simulator

I need to check with our finance team to confirm whether there is a specific overtime cost per hour that should be subtracted from profit.

## Turn 10 - Generic Agent

QUESTION: You mentioned Process II must be "fully utilized" with at least 70 hours — does this mean the constraint is simply 3A + 2B ≥ 70 (i.e., you must use at least 70 hours of Process II time), or does it mean Process II must be used for exactly 70 hours of regular time plus any overtime, so the total Process II hours used equals 70 + overtime hours (which is effectively the same as 3A + 2B ≥ 70)? Just confirming that 3A + 2B ≥ 70 is the correct formulation.

## Turn 10 - User Simulator

Yes, 3A + 2B ≥ 70 is the correct formulation.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision Variables:**
- A = number of Model A units produced per week (integer, ≥ 0)
- B = number of Model B units produced per week (integer, ≥ 0)

**Objective:**
- Maximize total weekly profit: 300A + 450B

**Constraints:**
1. Process I capacity (hard cap, no overtime): 4A + 6B ≤ 150
2. Process II minimum utilization (overtime allowed beyond 70, no confirmed upper cap): 3A + 2B ≥ 70
3. Model A minimum production: A ≥ 10
4. Model B minimum production: B ≥ 15
5. Integrality: A and B must be non-negative integers

**Parked items (pending confirmation):**
- Overtime cost for Process II: The client is still confirming with finance whether there is a per-hour overtime cost to subtract from profit. I will model overtime as having zero additional cost for now (i.e., Process II simply has no hard cap beyond 70 hours). If a cost is later confirmed, it can be added as a deduction in the objective.
- Upper limit on Process II overtime hours: The client is still confirming with operations. I will assume no upper cap on total Process II hours for now.

**Summary of the model:**
- Maximize: 300A + 450B
- Subject to:
  - 4A + 6B ≤ 150
  - 3A + 2B ≥ 70
  - A ≥ 10
  - B ≥ 15
  - A, B ∈ ℤ₊