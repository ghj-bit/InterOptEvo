# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U7, U8, U2, U3
I need help creating a production plan for two microcomputer models, A and B, where the total weekly profit must be at least 10,000 yuan, the processing time for Process I must be exactly 150 hours per week, and the regular processing time for Process II must not exceed its maximum weekly capacity of 70 hours.

| Process | Model A | Model B | Maximum Weekly Processing Capacity |
|---------|---------|---------|------------------------------------|
| I (hours/unit) | 4 | 6 | 150 |
| II (hours/unit) | 3 | 2 | 70 |
| Profit (yuan/unit) | 300 | 450 | |

Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan.

## Problem units
- U1 (context): I need help creating a production plan for two microcomputer models, A and B.
- U2 (data): | Process | Model A | Model B | Maximum Weekly Processing Capacity |
|---------|---------|---------|------------------------------------|
| I (hours/unit) | 4 | 6 | 150 |
| II (hours/unit) | 3 | 2 | 70 |
| Profit (yuan/unit) | 300 | 450 | |
- U3 (data): Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan.
- U4 (constraint): Total weekly profit must be at least 10,000 yuan.
- U5 (constraint): At least 10 units of model A must be produced each week.
- U6 (constraint): At least 15 units of model B must be produced each week.
- U7 (constraint): The processing time for Process I must be exactly 150 hours per week.
- U8 (constraint): The regular processing time for Process II must not exceed its maximum weekly capacity of 70 hours.
- U9 (constraint): The overtime processing for Process II must not exceed 30 hours per week.

## Hidden slot scoring rules
## H1: min_weekly_production_A
- Severity: P1
- Severity reason: Without this constraint, the model could produce fewer than 10 units of model A, violating a contractual obligation and making the solution business-invalid.
- Problem unit ID: U5
- Semantic hit rule: The Agent's question must inquire about a minimum or lower bound on the weekly production quantity of model A, or ask if there is any requirement to produce at least a certain number of A.
- Reference acceptable questions:
  - What is the minimum number of model A microcomputers we must produce each week?
  - Are there any minimum production requirements for model A?
- Failure modes:
  - Assuming no minimum production requirement for model A (production can be zero)
  - Assuming a different arbitrary lower bound

## H2: min_weekly_production_B
- Severity: P1
- Severity reason: Missing this constraint would allow the model to produce fewer than 15 units of model B, violating a contract and leading to a business-invalid solution.
- Problem unit ID: U6
- Semantic hit rule: The Agent's question asks for the minimum required weekly output of model B or whether there is a lower bound on B production.
- Reference acceptable questions:
  - How many model B microcomputers do we need to produce at minimum each week?
  - Is there a lower bound on the weekly production of model B?
- Failure modes:
  - Assuming no minimum production requirement for model B
  - Assuming an incorrect lower limit for B

## H3: max_overtime_process_II
- Severity: P1
- Severity reason: Without this limit, the model could treat overtime as unbounded, which would completely distort the feasible region and profit calculations, or could omit overtime entirely.
- Problem unit ID: U9
- Semantic hit rule: The Agent's question must explicitly ask for the upper limit or cap on overtime hours for Process II.
- Reference acceptable questions:
  - What is the maximum allowed overtime for Process II?
  - How many hours of overtime per week are permitted for Process II?
- Failure modes:
  - Assuming unlimited overtime for Process II
  - Assuming no overtime is allowed for Process II
  - Assuming a different arbitrary overtime cap


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When production exceeds the 70-hour regular capacity of Process II, is the overtime portion limited to some maximum number of hours per week, or can it be any non-negative amount?

## Turn 1 - User Simulator

The overtime portion is limited to a maximum of 30 hours per week.

## Turn 2 - Generic Agent

QUESTION: For units whose Process II time falls in the overtime portion, is the profit per unit the overtime figure (280 for A, 425 for B) regardless of which specific hours are used, or does the overtime profit apply only to the units that actually consume the overtime hours?

## Turn 2 - User Simulator

The overtime profit applies only to the units that actually consume the overtime hours.

## Turn 3 - Generic Agent

QUESTION: When Process II's total time exceeds 70 hours, how should the units be assigned to regular versus overtime hours — for example, is it free to choose which units count as overtime, or is there a fixed priority (such as all of Model A first, then Model B)?

## Turn 3 - User Simulator

It is free to choose which units count as overtime.

## Turn 4 - Generic Agent

QUESTION: The brief says Process I's time must be exactly 150 hours per week — is that a hard requirement that the plan must use all 150 hours, or is 150 just the capacity ceiling and using less is allowed?

## Turn 4 - User Simulator

It is a hard requirement that the plan must use all 150 hours.

## Turn 5 - Generic Agent

QUESTION: What is the objective of the plan — for example, minimize total production cost, minimize total overtime hours, minimize total units produced, or something else?

## Turn 5 - User Simulator

The objective is to minimize total overtime hours.

## Turn 6 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be fractional?

## Turn 6 - User Simulator

The weekly production quantities must be whole numbers.

## Turn 7 - Generic Agent

QUESTION: The overtime profit figures (280 for A, 425 for B) are lower than the regular profits (300, 450) — is the "at least 10,000 yuan" weekly profit computed using the regular profit for every unit, or using the actual profit (regular or overtime) for each unit depending on which hours it consumed?

## Turn 7 - User Simulator

The "at least 10,000 yuan" weekly profit is computed using the actual profit (regular or overtime) for each unit depending on which hours it consumed.

## Turn 8 - Generic Agent

QUESTION: If no production plan can satisfy all the requirements together (profit at least 10,000, Process I exactly 150 hours, Process II regular at most 70 hours, overtime at most 30 hours), what should happen — should the model simply report infeasibility, or should some requirement be relaxed?

## Turn 8 - User Simulator

The model should simply report infeasibility.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Products:** Two microcomputer models, A and B, produced in whole (integer, non-negative) units per week.
- **Process I:** 4 h/unit for A, 6 h/unit for B; total must be **exactly 150 hours** per week (hard equality).
- **Process II:** 3 h/unit for A, 2 h/unit for B; regular capacity is **70 hours/week** (ceiling). Overtime is allowed up to **30 hours/week** (ceiling), so total Process II time can be at most 100 hours.
- **Overtime assignment:** It is free to choose which units' Process II time counts as regular vs. overtime; overtime profit applies only to the units that actually consume overtime hours.
- **Profit:** Regular: A = 300 yuan/unit, B = 450 yuan/unit. Overtime: A = 280 yuan/unit, B = 425 yuan/unit. Total weekly profit (using each unit's actual regular/overtime profit) must be **at least 10,000 yuan**.
- **Objective:** **Minimize total overtime hours** in Process II.
- **Feasibility:** If no plan satisfies all requirements, the model should report infeasibility (no relaxation).

Model class: integer linear program (binary/integer variables to split each model's units into regular and overtime portions, with the overtime hours minimized).