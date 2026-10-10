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

QUESTION: Is the 70-hour weekly capacity for Process II a hard ceiling that must not be exceeded, or is it a baseline that can be exceeded through overtime at an additional cost that should be included in the profit calculation?

## Turn 1 - User Simulator

The 70-hour weekly capacity for Process II is a baseline that can be exceeded through overtime.

## Turn 2 - Generic Agent

QUESTION: What is the additional cost per hour for overtime on Process II, and is there a maximum limit on how many overtime hours can be used per week?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the 150-hour weekly capacity for Process I a hard ceiling that cannot be exceeded, or can it also be extended through overtime?

## Turn 3 - User Simulator

The 150-hour weekly capacity for Process I is a hard ceiling that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Is the requirement to produce at least 10 units of Model A per week a hard constraint that must be strictly satisfied, or is it a soft target where producing fewer units is allowed if it leads to a higher overall profit?

## Turn 4 - User Simulator

The requirement to produce at least 10 units of Model A per week is a hard constraint that must be strictly satisfied.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers (integers), or can they be fractional values?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum weekly production limit for Model B, or can it be produced in unlimited quantities as long as the process capacities are not exceeded?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there a minimum weekly production requirement for Model B, or can the production quantity for Model B be zero?

## Turn 7 - User Simulator

Yes, there is a minimum weekly production requirement for Model B. We have a contractual requirement to produce at least 15 units of Model B each week.

## Turn 8 - Generic Agent

QUESTION: Is the 15-unit minimum for Model B a hard constraint that must be strictly satisfied, or is it a soft target that can be violated if necessary to maximize profit?

## Turn 8 - User Simulator

The 15-unit minimum for Model B is a hard constraint that must be strictly satisfied.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as maximum production limits for Model A, dependencies between the two models, or additional resource limitations?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Is the profit per unit for Model A ($300) and Model B ($450) a net profit after all costs, or does it require subtracting additional costs like overtime pay or material costs?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total weekly profit.
2.  **Decision Variables:** Weekly production quantity of Model A ($x_A$) and Model B ($x_B$).
3.  **Process I Constraint:** $4x_A + 6x_B \le 150$ (Hard ceiling, no overtime).
4.  **Process II Constraint:** $3x_A + 2x_B \ge 70$ (Baseline capacity must be fully utilized; overtime allowed to exceed 70 hours).
5.  **Model A Minimum:** $x_A \ge 10$ (Hard constraint).
6.  **Model B Minimum:** $x_B \ge 15$ (Hard constraint).
7.  **Profit Coefficients:** $300 per unit for Model A, $450 per unit for Model B.

**Explicit Assumptions (Unconfirmed):**
1.  **Overtime Cost:** The cost per hour for overtime on Process II is unknown. It is assumed to be zero or negligible for the purpose of this formulation, meaning the objective function uses the stated unit profits without deduction for overtime. If overtime has a significant cost, the objective function or the Process II constraint structure would need adjustment.
2.  **Integrality:** It is assumed that production quantities $x_A$ and $x_B$ can be continuous (fractional) values. If integer production is required, the model would need to be an Integer Linear Program.
3.  **Maximum Limits:** It is assumed there are no maximum production limits for Model A or Model B other than those imposed by the process capacities.
4.  **Profit Definition:** It is assumed the stated profits ($300 and $450) are net profits that do not require further adjustment for material costs or other variable costs not explicitly listed.
5.  **Other Constraints:** It is assumed there are no other hidden constraints (e.g., labor limits, storage limits, or dependencies) beyond those specified.