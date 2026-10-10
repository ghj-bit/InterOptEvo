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

QUESTION: When you say the weekly production time for Process II must be "fully utilized," do you mean the total hours used in Process II must be exactly equal to 70 hours, or that it must be at least 70 hours (allowing for overtime beyond 70)?

## Turn 1 - User Simulator

It must be at least 70 hours, allowing for overtime beyond 70.

## Turn 2 - Generic Agent

QUESTION: Is there a maximum limit on the total weekly hours that can be used for Process II when including overtime, or is the overtime capacity unlimited?

## Turn 2 - User Simulator

The overtime capacity for Process II is unlimited.

## Turn 3 - Generic Agent

QUESTION: Is there a maximum limit on the total weekly hours that can be used for Process I, or is the 150-hour capacity for Process I a hard ceiling that cannot be exceeded?

## Turn 3 - User Simulator

The 150-hour capacity for Process I is a hard ceiling that cannot be exceeded.

## Turn 4 - Generic Agent

QUESTION: Are the production quantities for Model A and Model B required to be whole numbers (integers), or can they be fractional values?

## Turn 4 - User Simulator

The production quantities for Model A and Model B must be whole numbers (integers).

## Turn 5 - Generic Agent

QUESTION: Is there a minimum production requirement for Model B per week, or can the production quantity for Model B be zero?

## Turn 5 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 6 - Generic Agent

QUESTION: Is there a maximum limit on the total weekly production quantity for Model A, or can it be produced in unlimited quantities subject only to the Process I capacity and other constraints?

## Turn 6 - User Simulator

There is no maximum limit on the total weekly production quantity for Model A.

## Turn 7 - Generic Agent

QUESTION: Is there a maximum limit on the total weekly production quantity for Model B, or can it be produced in unlimited quantities subject only to the Process I capacity and other constraints?

## Turn 7 - User Simulator

There is no maximum limit on the total weekly production quantity for Model B.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements for the weekly production plan that are not mentioned in the brief, such as minimum production levels for total output, labor availability, or material limits?

## Turn 8 - User Simulator

Yes, the total weekly profit must be at least $10,000.

## Turn 9 - Generic Agent

QUESTION: Is the $10,000 total weekly profit requirement a hard constraint that must be strictly satisfied, or is it a soft target that can be violated if necessary to maximize profit?

## Turn 9 - User Simulator

The $10,000 total weekly profit requirement is a hard constraint that must be strictly satisfied.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total weekly profit.
    *   Profit per unit: Model A = $300, Model B = $450.
    *   Objective Function: Maximize $300A + 450B$.

2.  **Decision Variables:**
    *   $A$: Number of units of Model A produced per week.
    *   $B$: Number of units of Model B produced per week.
    *   Domain: Both $A$ and $B$ must be non-negative integers ($A, B \in \mathbb{Z}_{\ge 0}$).

3.  **Constraints:**
    *   **Process I Capacity:** The total hours used in Process I cannot exceed 150 hours.
        *   $4A + 6B \le 150$
    *   **Process II Utilization:** The total hours used in Process II must be at least 70 hours (overtime is allowed and unlimited).
        *   $3A + 2B \ge 70$
    *   **Minimum Production Model A:** At least 10 units of Model A must be produced.
        *   $A \ge 10$
    *   **Minimum Production Model B:** At least 15 units of Model B must be produced.
        *   $B \ge 15$
    *   **Minimum Profit:** The total weekly profit must be at least $10,000.
        *   $300A + 450B \ge 10,000$

4.  **Assumptions:**
    *   There are no other hidden constraints (e.g., labor, materials, or total output limits) beyond those explicitly confirmed.
    *   The "unlimited" overtime for Process II means there is no upper bound on the hours used in Process II, only the lower bound of 70 hours.
    *   The profit figures provided are net profits per unit, so the objective function and the profit constraint use the same coefficients.