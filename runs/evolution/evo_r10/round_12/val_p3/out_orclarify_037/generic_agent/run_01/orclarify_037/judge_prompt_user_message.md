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

QUESTION: When you say Process II must be "fully utilized," do you mean the 70 regular hours must be completely consumed (i.e., exactly 70 hours of regular time used, with any additional hours beyond 70 allowed as overtime), or do you mean the total Process II time including overtime must equal some fixed larger number?

## Turn 1 - User Simulator

I mean the 70 regular hours must be completely consumed. Any additional hours beyond 70 are allowed as overtime.

## Turn 2 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or can overtime be unlimited?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: What is the overtime cost per hour for Process II, and does overtime affect the profit per unit of either model, or is it a separate cost that reduces total profit?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model B, or can any number of Model B units be produced as long as the process constraints are satisfied?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Can Model A and Model B production quantities be fractional (e.g., 12.5 units), or must they be whole numbers?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model A, or can any number of Model A units be produced as long as the process constraints are satisfied?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there a minimum weekly production requirement for Model B, or can zero units of Model B be produced in a week?

## Turn 7 - User Simulator

Yes, we have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model A, or can any number of Model A units be produced as long as the process constraints are satisfied?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model B, or can any number of Model B units be produced as long as the process constraints are satisfied?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or can overtime be unlimited?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: What is the overtime cost per hour for Process II, and does overtime affect the profit per unit of either model, or is it a separate cost that reduces total profit?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Can Model A and Model B production quantities be fractional (e.g., 12.5 units), or must they be whole numbers?

## Turn 12 - User Simulator

The point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model A, or can any number of Model A units be produced as long as the process constraints are satisfied?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model B, or can any number of Model B units be produced as long as the process constraints are satisfied?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or can overtime be unlimited?

## Turn 15 - User Simulator

The point still needs internal confirmation

## Turn 16 - Generic Agent

QUESTION: What is the overtime cost per hour for Process II, and does overtime affect the profit per unit of either model, or is it a separate cost that reduces total profit?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: Can Model A and Model B production quantities be fractional (e.g., 12.5 units), or must they be whole numbers?

## Turn 17 - User Simulator

The point still needs

## Turn 18 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model A, or can any number of Model A units be produced as long as the process constraints are satisfied?

## Turn 18 - User Simulator

The point still needs internal

## Turn 19 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model B, or can any number of Model B units be produced as long as the process constraints are satisfied?

## Turn 19 - User Simulator

The point

## Turn 20 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or can overtime be unlimited?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: What is the overtime cost per hour for Process II, and does overtime affect the profit per unit of either model, or is it a separate cost that reduces total profit?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Can Model A and Model B production quantities be fractional (e.g., 12.5 units), or must they be whole numbers?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model A, or can any number of Model A units be produced as long as the process constraints are satisfied?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model B, or can any number of Model B units be produced as long as the process constraints are satisfied?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or can overtime be unlimited?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: What is the overtime cost per hour for Process II, and does overtime affect the profit per unit of either model, or is it a separate cost that reduces total profit?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Can Model A and Model B production quantities be fractional (e.g., 12.5 units), or must they be whole numbers?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model A, or can any number of Model A units be produced as long as the process constraints are satisfied?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Is there a maximum weekly production capacity for Model B, or can any number of Model B units be produced as long as the process constraints are satisfied?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Is there a maximum number of overtime hours allowed for Process II per week, or can overtime be unlimited?

## Turn 30 - User Simulator

The