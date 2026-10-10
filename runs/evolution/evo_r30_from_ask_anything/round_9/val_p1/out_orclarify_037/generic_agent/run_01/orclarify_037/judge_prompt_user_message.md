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

QUESTION: Is the 70-hour capacity for Process II a hard upper limit that cannot be exceeded even with overtime, or is it a baseline that can be extended by paying for additional overtime hours?

## Turn 1 - User Simulator

It is a baseline that can be extended by paying for additional overtime hours.

## Turn 2 - Generic Agent

QUESTION: What is the cost per hour for overtime on Process II, and is there a maximum number of overtime hours allowed per week?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the 10-unit minimum for Model A a hard constraint that must be met in every week, or is it a soft target that can be violated if doing so increases total profit

## Turn 3 - User Simulator

It is a hard constraint that must be met in every week.

## Turn 4 - Generic Agent

QUESTION: Is the 150-hour capacity for Process I a hard upper limit that cannot be exceeded, or is it also a baseline that can be extended with

## Turn 4 - User Simulator

The 150-hour capacity for Process I is a hard upper limit that cannot be exceeded.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the 70-hour baseline for Process II a minimum requirement that must be met, or is it simply the standard capacity that can

## Turn 6 - User Simulator

It is simply the standard capacity that can be extended with overtime if necessary.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum limit on the total number of overtime hours allowed

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements for the production plan

## Turn 8 - User Simulator

Yes, there are two additional requirements:

1. The total weekly profit must be at least $10,000.
2. At least 15 units of Model B must be produced per week.

## Turn 9 - Generic Agent

QUESTION: Is the $10,000 minimum weekly profit a hard constraint that must be met

## Turn 9 - User Simulator

Yes, the $10,000 minimum weekly profit is a hard constraint that must be met.

## Turn 10 - Generic Agent

QUESTION: Is the requirement to produce at least 15 units of Model B per week a hard

## Turn 10 - User Simulator

Yes, the requirement to produce at least 15 units of Model B per week is a hard constraint.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total weekly profit.
2.  **Decision Variables:** Weekly production quantities for Model A ($x_A$) and Model B ($x_B$).
3.  **Profit Coefficients:** Model A = $300/unit, Model B = $450/unit.
4.  **Process I Constraint:** Hard upper limit of 150 hours. Usage: $4x_A + 6x_B \le 150$.
5.  **Process II Constraint:** Baseline capacity of 70 hours, extendable via overtime. The brief states it must be "fully utilized," which is interpreted as the standard capacity being used, with overtime available to handle excess demand if necessary to meet other constraints. *Note: Since the overtime cost and limit are unconfirmed, this is treated as a flexible resource where the base 70 hours are available, and any additional hours are permitted subject to the other hard constraints.*
6.  **Model A Minimum:** Hard constraint, $x_A \ge 10$.
7.  **Model B Minimum:** Hard constraint, $x_B \ge 15$.
8.  **Total Profit Minimum:** Hard constraint, $300x_A + 450x_B \ge 10,000$.
9.  **Non-negativity:** $x_A, x_B \ge 0$.

**Explicit Assumptions (Unconfirmed):**
1.  **Integrality:** It is assumed that production quantities $x_A$ and $x_B$ can be continuous (fractional units are allowed). If whole numbers are required, the model would need to be an Integer Linear Program.
2.  **Overtime Cost/Limit:** It is assumed there is no specific cost penalty for overtime in the objective function (i.e., profit is calculated purely on unit sales) and no upper bound on overtime hours, other than the implicit bounds set by the other constraints. The "fully utilized" phrasing for Process II is interpreted as the standard 70 hours being the base capacity, with overtime allowing the constraint to be relaxed if necessary to satisfy the minimum production and profit targets.
3.  **Process II Direction:** It is assumed the Process II constraint is an upper bound on available time (standard + overtime), i.e., $3x_A + 2x_B \le 70 + \text{overtime}$. Since overtime is unlimited (assumed), this constraint may not be binding if the other constraints allow for higher production, but it defines the base resource availability.