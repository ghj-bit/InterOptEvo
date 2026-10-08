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

QUESTION: When you say Process II's weekly production time must be "fully utilized, with potential overtime if necessary," do you mean the model should force exactly 70 hours of Process II usage (with overtime hours allowed to exceed 70 if needed to meet the other requirements), or should it simply require at least 70 hours of Process II usage (i.e., the 70-hour capacity is a minimum that must be met, and any amount above 70 is permitted)?

## Turn 1 - User Simulator

It should simply require at least 70 hours of Process II usage. The 70-hour capacity is a minimum that must be met, and any amount above 70 is permitted.

## Turn 2 - Generic Agent

QUESTION: For Process I, is the 150-hour maximum weekly capacity a hard upper limit that production cannot exceed (i.e., total Process I hours must be at most 150), or is it also a minimum that must be met like Process II?

## Turn 2 - User Simulator

It is a minimum that must be met. The weekly production time for Process I must be exactly 150 hours, not just up to 150.

## Turn 3 - Generic Agent

QUESTION: You said Process I must be exactly 150 hours, but earlier the table listed 150 as a "maximum weekly processing capacity." To be sure I model it correctly: should Process I hours be constrained to be exactly 150 (no more, no less), or at least 150 (150 or more allowed)?

## Turn 3 - User Simulator

Process I hours should be constrained to be exactly 150 (no more, no less).

## Turn 4 - Generic Agent

QUESTION: The table lists 70 hours as the "maximum weekly processing capacity" for Process II, but you said it should be treated as a minimum that must be met with any amount above 70 permitted. To confirm: is there any upper limit on Process II hours at all, or can Process II hours be any value of 70 or more with no ceiling?

## Turn 4 - User Simulator

There is no upper limit on Process II hours. Process II hours can be any value of 70 or more with no ceiling.

## Turn 5 - Generic Agent

QUESTION: Should the number of Model A and Model B units produced per week be whole numbers (integer units), or is it acceptable to treat them as continuous values (e.g., 12.5 units) in the plan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: The brief requires at least 10 units of Model A per week. Is there any minimum production requirement for Model B, or can Model B production be zero if that is optimal?

## Turn 6 - User Simulator

Yes, there is a minimum production requirement for Model B. We have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 7 - Generic Agent

QUESTION: Are there any upper limits on how many units of Model A or Model B can be produced per week (e.g., demand caps or market limits), or is production of each model unlimited above its minimum?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: To confirm the objective: should the plan maximize total weekly profit, calculated as 300 times the number of Model A units plus 450 times the number of Model B units, with no other costs or penalties included?

## Turn 8 - User Simulator

Yes, the goal is to maximize total weekly profit, calculated as 300 times the number of Model A units plus 450 times the number of Model B units, with no other costs or penalties included.

## Turn 9 - Generic Agent

QUESTION: You mentioned earlier that the production plan involves "two types of microcomputers" and "the same two production processes." To confirm: are there exactly two models (A and B) and exactly two processes (I and II), with no additional models, processes, or constraints beyond what is described?

## Turn 9 - User Simulator

Yes, there are exactly two models (A and B) and exactly two processes (I and II), with no additional models or processes.

## Turn 10 - Generic Agent

QUESTION: Earlier you deferred the question of whether Model A and Model B units must be whole numbers (integer) or can be continuous values. To confirm: should the production quantities be restricted to whole units (integer), or is it acceptable to treat them as continuous values in the plan?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Earlier you deferred the question of whether there are upper limits on Model A or Model B production (demand caps or market limits). To confirm: is there any upper limit on how many units of Model A or Model B can be produced per week, or is production of each model unlimited above its minimum?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables:**
- x_A = number of Model A units produced per week
- x_B = number of Model B units produced per week
- (Integrality: deferred by client — I will treat them as continuous non-negative variables, but note that integer restriction is a natural extension if whole units are required.)

**Objective:**
- Maximize total weekly profit = 300·x_A + 450·x_B

**Constraints:**
1. Process I hours exactly 150: 4·x_A + 6·x_B = 150
2. Process II hours at least 70 (no upper limit): 3·x_A + 2·x_B ≥ 70
3. Minimum Model A production: x_A ≥ 10
4. Minimum Model B production (contractual): x_B ≥ 15
5. Non-negativity: x_A ≥ 0, x_B ≥ 0 (redundant given constraints 3 and 4)

**Notes on deferred items:**
- Whether x_A and x_B must be integers: deferred twice; I will model as continuous (LP) and note the integer variant.
- Whether there are upper bounds (demand caps) on x_A or x_B: deferred twice; I will model without upper bounds.

**Model class:** Linear Programming (LP) with two continuous decision variables. If integrality is later confirmed, it becomes a small Integer Linear Program (ILP).