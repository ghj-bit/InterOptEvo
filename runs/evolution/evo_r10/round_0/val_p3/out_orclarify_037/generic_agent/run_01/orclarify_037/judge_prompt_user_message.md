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

QUESTION: When you say Process II's weekly production time must be "fully utilized," do you mean the total hours used on Process II must be exactly 70 (i.e., 3x_A + 2x_B = 70), or at least 70 (i.e., 3x_A + 2x_B ≥ 70, with overtime allowed beyond 70)?

## Turn 1 - User Simulator

It means at least 70 hours. The base capacity is 70 hours, but we are willing to use overtime if necessary, so the total hours used on Process II can exceed 70.

## Turn 2 - Generic Agent

QUESTION: If overtime is used on Process II, is there any limit on how many overtime hours can be added beyond the 70-hour base capacity, or is overtime unlimited?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Since the overtime limit is still being confirmed internally, for now should I model Process II's overtime as unlimited (i.e., 3x_A + 2x_B ≥ 70 with no upper bound on Process II hours), or would you prefer I treat Process II as having a hard cap of 70 hours (3x_A + 2x_B ≤ 70) until the overtime limit is confirmed?

## Turn 3 - User Simulator

Please model Process II's overtime as unlimited for now (i.e., 3x_A + 2x_B ≥ 70 with no upper bound on Process II hours).

## Turn 4 - Generic Agent

QUESTION: Should the number of units of Model A and Model B produced per week be restricted to whole numbers (integer units), or is it acceptable to treat them as continuous quantities (e.g., 12.5 units)?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: While that's being confirmed, should I treat the production quantities as continuous (allowing fractional units) for now, or as integers (whole units only)?

## Turn 5 - User Simulator

Please treat the production quantities as continuous (allowing fractional units) for now.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum production requirement for Model B per week, or can Model B production be zero?

## Turn 6 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 7 - Generic Agent

QUESTION: Is there any maximum limit on the weekly production of Model A or Model B (other than the process capacity constraints), or are the only upper bounds the Process I and Process II capacities?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: While that's being confirmed, should I assume there are no additional upper bounds on Model A or Model B production beyond the Process I capacity (4x_A + 6x_B ≤ 150) and the Process II minimum (3x_A + 2x_B ≥ 70), or is there a known cap I should include?

## Turn 8 - User Simulator

Please assume there are no additional upper bounds on Model A or Model B production beyond the Process I capacity (4x_A + 6x_B ≤ 150) and the Process II minimum (3x_A + 2x_B ≥ 70).

## Turn 9 - Generic Agent

QUESTION: Is Process I's 150-hour capacity a hard upper limit (i.e., 4x_A + 6x_B ≤ 150), or can Process I also use overtime beyond 150 hours?

## Turn 9 - User Simulator

Process I's 150-hour capacity is a hard upper limit.

## Turn 10 - Generic Agent

QUESTION: Is there any cost associated with overtime on Process II that should be subtracted from the profit in the objective function, or is the overtime simply free (i.e., the $300 and $450 per-unit profits remain unchanged regardless of how many Process II hours are used)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: While that's being confirmed, should I assume the per-unit profits of $300 (Model A) and $450 (Model B) remain unchanged regardless of overtime usage on Process II, or is there a known overtime cost per hour I should subtract?

## Turn 11 - User Simulator

Please assume the per-unit profits of $300 (Model A) and $450 (Model B) remain unchanged regardless of overtime usage on Process II.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Decision variables:** x_A = weekly units of Model A, x_B = weekly units of Model B (continuous, non-negative).
- **Objective:** Maximize total weekly profit = 300·x_A + 450·x_B.
- **Constraints:**
  1. Process I capacity (hard upper limit): 4·x_A + 6·x_B ≤ 150.
  2. Process II minimum utilization (overtime allowed, no upper bound): 3·x_A + 2·x_B ≥ 70.
  3. Minimum Model A production: x_A ≥ 10.
  4. Minimum Model B production (contractual): x_B ≥ 15.
  5. Non-negativity: x_A ≥ 0, x_B ≥ 0 (redundant given constraints 3 and 4).
- **No other upper bounds** on x_A or x_B beyond Process I capacity.
- **No overtime cost** on Process II; per-unit profits are fixed at $300 and $450.
- **Quantities are continuous** (fractional units allowed).