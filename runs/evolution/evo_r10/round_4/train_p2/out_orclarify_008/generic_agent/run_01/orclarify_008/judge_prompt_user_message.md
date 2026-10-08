# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U6, U2
I need help creating a work assignment plan where exactly 4 out of the 5 workers must be selected, and each task (A, B, C, D) must be assigned to exactly one worker.

Table of hours required by each worker to complete each task:

| Worker | A | B | C | D |
|--------|---|---|---|---|
| I      | 9 | 4 | 3 | 7 |
| II     | 4 | 6 | 5 | 6 |
| III    | 5 | 4 | 7 | 5 |
| IV     | 7 | 5 | 2 | 3 |
| V      | 10| 6 | 7 | 4 |

## Problem units
- U1 (context): I need help creating a work assignment plan.
- U2 (data): Table of hours required by each worker to complete each task:

| Worker | A | B | C | D |
|--------|---|---|---|---|
| I      | 9 | 4 | 3 | 7 |
| II     | 4 | 6 | 5 | 6 |
| III    | 5 | 4 | 7 | 5 |
| IV     | 7 | 5 | 2 | 3 |
| V      | 10| 6 | 7 | 4 |
- U3 (objective): Total working hours are to be minimized.
- U4 (constraint): Exactly 4 out of the 5 workers must be selected.
- U5 (constraint): Each selected worker is assigned to exactly one of the four tasks.
- U6 (constraint): Each task (A, B, C, D) must be assigned to exactly one worker.

## Hidden slot scoring rules
## H1: missing_minimize_hours_objective
- Severity: P0
- Severity reason: Without the objective, the optimization problem is ill‑posed. The agent cannot formulate a meaningful model, because it does not know what criterion to optimize (minimizing total working hours). Missing this makes the entire modelling attempt impossible or almost certainly wrong.
- Problem unit ID: U3
- Semantic hit rule: The agent’s question must ask about the performance metric to be optimized, explicitly mentioning minimization of total working time or total hours.
- Reference acceptable questions:
  - What is the objective we are trying to optimize?
  - Are we minimizing total working hours or something else like cost or makespan?
- Failure modes:
  - Assumption that total working hours is the objective without confirming.
  - Assumption of a different objective such as minimising the maximum completion time or minimising cost.
  - Inventing an objective that does not match the intended problem.

## H2: worker_at_most_one_task_constraint
- Severity: P1
- Severity reason: Without this constraint, an agent may model a worker handling several tasks simultaneously, leading to a materially different assignment structure (e.g., one worker can be assigned to multiple tasks). The problem would still be coherent but would not reflect the intended business rule that each selected worker is responsible for exactly one task.
- Problem unit ID: U5
- Semantic hit rule: The agent’s question must inquire whether a selected worker can be assigned to multiple tasks, or ask for the exact number of tasks each worker may take.
- Reference acceptable questions:
  - Is each worker limited to exactly one task, or can a single worker perform more than one task?
  - For the four workers we pick, does each worker get exactly one of the four tasks?
- Failure modes:
  - Assuming a worker can be assigned to more than one task (e.g., one worker does two tasks while another does none).
  - Assuming at most one task per worker but not verifying the 'exactly one' part, leaving task assignments ambiguous.
  - Inventing a flexible capacity per worker that is absent from the original problem.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the goal to minimize the total hours worked by the selected workers across all four tasks?

## Turn 1 - User Simulator

Yes, the goal is to minimize the total working hours.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned more than one of the four tasks, or must each task go to a different worker?

## Turn 2 - User Simulator

Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many tasks a single worker can be assigned, or can one worker take multiple tasks?

## Turn 3 - User Simulator

No, each selected worker is assigned to exactly one of the four tasks.

## Turn 4 - Generic Agent

QUESTION: Since 4 workers are selected and each gets exactly one task, does that mean the 4 selected workers each take one of the 4 tasks (so each task is covered by a distinct worker), and the 5th worker is simply left out with no work?

## Turn 4 - User Simulator

Yes, that is correct.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Workers:** 5 workers (I, II, III, IV, V); exactly 4 must be selected, 1 left out with no work.
- **Tasks:** 4 tasks (A, B, C, D); each task assigned to exactly one worker.
- **Assignment rule:** Each selected worker is assigned to exactly one task, and each task is covered by a distinct selected worker (a one-to-one matching between the 4 selected workers and the 4 tasks).
- **Objective:** Minimize the total hours, where the hours for a (worker, task) pair are given by the table:

| Worker | A | B | C | D |
|--------|---|---|---|---|
| I      | 9 | 4 | 3 | 7 |
| II     | 4 | 6 | 5 | 6 |
| III    | 5 | 4 | 7 | 5 |
| IV     | 7 | 5 | 2 | 3 |
| V      | 10| 6 | 7 | 4 |

**Model sketch:** Binary variable x[w,t] = 1 if worker w is assigned task t. Constraints: each task assigned to exactly one worker (sum over w of x[w,t] = 1 for each t); each worker assigned to at most one task (sum over t of x[w,t] ≤ 1 for each w); exactly 4 workers selected (sum over all x = 4). Objective: minimize sum of hours[w,t]·x[w,t].