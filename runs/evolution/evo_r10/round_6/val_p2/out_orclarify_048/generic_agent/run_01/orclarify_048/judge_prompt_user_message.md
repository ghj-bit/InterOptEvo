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

QUESTION: When some units of Model A or B are processed in overtime in Process II, do those units still consume their full regular Process II time (3 hours for A, 2 hours for B) against the 70-hour regular capacity, or does the overtime portion replace the regular time so that only the non-overtime units count against the 70-hour limit?

## Turn 1 - User Simulator

The overtime portion replaces the regular time. Only the non-overtime units count against the 70-hour regular capacity limit.

## Turn 2 - Generic Agent

QUESTION: For units processed in overtime in Process II, do they still consume their full Process I time (4 hours for A, 6 hours for B) against the 150-hour Process I requirement, or does overtime affect Process I time as well?

## Turn 2 - User Simulator

Overtime only applies to Process II. Units processed in overtime in Process II still consume their full Process I time (4 hours for A, 6 hours for B) against the 150-hour Process I requirement.

## Turn 3 - Generic Agent

QUESTION: The brief says Process I time must be exactly 150 hours per week. Is 150 a hard equality that the plan must hit precisely, or is it a capacity ceiling (at most 150) that the plan may use up to but not exceed?

## Turn 3 - User Simulator

It is a hard equality. The plan must use exactly 150 hours of Process I time per week.

## Turn 4 - Generic Agent

QUESTION: The total weekly profit must be at least 10,000 yuan. Is this a constraint the plan must satisfy (a floor), or is it the objective to maximize?

## Turn 4 - User Simulator

It is a constraint. The plan must achieve a total weekly profit of at least 10,000 yuan.

## Turn 5 - Generic Agent

QUESTION: Since profit is a constraint (at least 10,000) and Process I time is a hard equality (exactly 150), what is the actual objective of the production plan — for example, minimize total production cost, minimize overtime usage, maximize total units produced, or something else?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the overtime units in Process II, is there a maximum number of units (or maximum overtime hours) that can be processed in overtime, or is overtime unlimited as long as the regular 70-hour capacity is respected for the non-overtime units?

## Turn 6 - User Simulator

The overtime on Process II is limited to 30 hours per week.

## Turn 7 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: The overtime profit figures (280 yuan for A, 425 yuan for B) are lower than the regular profit (300 for A, 450 for B). Does this mean overtime units earn only the reduced profit (i.e., the overtime cost is already netted out), or is there an additional overtime cost that should be subtracted separately from the regular profit?

## Turn 8 - User Simulator

The overtime units earn only the reduced profit. The overtime cost is already netted out in those figures.

## Turn 9 - Generic Agent

QUESTION: The overtime on Process II is limited to 30 hours per week. Is this 30 hours a hard ceiling (overtime hours used must be at most 30), or must the plan use exactly 30 hours of overtime?

## Turn 9 - User Simulator

It is a hard ceiling. Overtime hours used must be at most 30 hours per week.

## Turn 10 - Generic Agent

QUESTION: Is there any minimum production requirement for Model A or Model B (e.g., at least X units of each must be produced per week), or can either model's production be zero?

## Turn 10 - User Simulator

Yes, there are minimum production requirements:

- At least 10 units of Model A must be produced each week.
- At least 15 units of Model B must be produced each week.

## Turn 11 - Generic Agent

QUESTION: Are there any maximum production limits for Model A or Model B per week (e.g., demand caps or market limits), or is production of each model unbounded above (subject only to the process constraints)?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: For the overtime units in Process II, how is the 30-hour overtime ceiling measured — is it the total overtime hours consumed (3 hours per overtime unit of A plus 2 hours per overtime unit of B, at most 30), or is it a cap on the number of overtime units?

## Turn 12 - User Simulator

It is the total overtime hours consumed. The sum of 3 hours per overtime unit of A plus 2 hours per overtime unit of B must be at most 30 hours.

## Turn 13 - Generic Agent

QUESTION: The objective is still pending internal confirmation. While waiting, can you confirm: is there any other constraint or business rule I haven't asked about — for example, a limit on total units produced, a requirement to use all available capacity, or a preference for one model over the other?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Since the objective is still pending internal confirmation, may I proceed with the model using "maximize total weekly profit" as a placeholder objective (with the 10,000-yuan floor kept as a constraint), so that the structure is ready and only the objective line needs to be swapped once your team confirms?

## Turn 14 - User Simulator

Yes, that is fine.

## Turn 15 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Products:** Two microcomputer models, A and B, produced weekly.

**Decision variables (per week):**
- Regular (non-overtime) units of A and B processed in Process II: a_r, b_r
- Overtime units of A and B processed in Process II: a_o, b_o
- Total units: A = a_r + a_o, B = b_r + b_o

**Process I (hard equality, exactly 150 hours/week):**
- 4·A + 6·B = 150
- Overtime units still consume full Process I time.

**Process II regular capacity (ceiling, 70 hours/week):**
- Only non-overtime units count: 3·a_r + 2·b_r ≤ 70

**Process II overtime (ceiling, 30 hours/week):**
- 3·a_o + 2·b_o ≤ 30

**Profit (constraint, floor of 10,000 yuan/week):**
- Regular units earn full profit; overtime units earn reduced profit (overtime cost already netted out):
- 300·a_r + 450·b_r + 280·a_o + 425·b_o ≥ 10,000

**Minimum production (floors):**
- A ≥ 10, B ≥ 15

**Objective (placeholder, pending internal confirmation):**
- Maximize total weekly profit: 300·a_r + 450·b_r + 280·a_o + 425·b_o
- (To be swapped once the team confirms the true objective.)

**Parked / pending items:**
- True objective function (placeholder = maximize profit)
- Whether production quantities must be integer (currently modeled as continuous; integrality to be added if confirmed)
- Any maximum production caps on A or B (none assumed)

**No other constraints** were confirmed (no total-unit cap, no full-capacity requirement, no model preference).