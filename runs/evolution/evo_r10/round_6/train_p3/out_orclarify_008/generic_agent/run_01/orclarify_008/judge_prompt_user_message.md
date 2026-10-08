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

QUESTION: Is the goal to minimize the total hours worked by the 4 selected workers, or is there a different objective (such as minimizing the hours of the busiest worker, or meeting a deadline)?

## Turn 1 - User Simulator

The goal is to minimize the total hours worked by the 4 selected workers.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned more than one of the four tasks, or must each selected worker take exactly one task (which would leave one task unassigned since only 4 workers are chosen for 4 tasks)?

## Turn 2 - User Simulator

Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Since 4 workers are selected for 4 tasks and each selected worker takes exactly one task, does that mean each of the four tasks A, B, C, D is assigned to exactly one distinct selected worker (a one-to-one matching), so no task is left unassigned and no worker gets two tasks?

## Turn 3 - User Simulator

Yes, each of the four tasks A, B, C, D is assigned to exactly one distinct selected worker.

## Turn 4 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Workers:** 5 workers (I, II, III, IV, V); **Tasks:** 4 tasks (A, B, C, D).
- **Selection:** Exactly 4 of the 5 workers must be selected (one worker is left out).
- **Assignment:** Each selected worker is assigned to exactly one task, and each of the four tasks A, B, C, D is assigned to exactly one distinct selected worker — i.e., a one-to-one matching between the 4 selected workers and the 4 tasks. No worker gets two tasks; no task is left unassigned.
- **Cost data:** The table gives the hours each worker requires to complete each task:

| Worker | A | B | C | D |
|--------|---|---|---|---|
| I      | 9 | 4 | 3 | 7 |
| II     | 4 | 6 | 5 | 6 |
| III    | 5 | 4 | 7 | 5 |
| IV     | 7 | 5 | 2 | 3 |
| V      | 10| 6 | 7 | 4 |

- **Objective:** Minimize the total hours worked by the 4 selected workers (sum of the hours of the assigned worker–task pairs).

**Model sketch:**
- Binary variable x[w,t] = 1 if worker w is assigned to task t.
- Binary variable s[w] = 1 if worker w is selected.
- Constraints:
  - Each task assigned to exactly one worker: for each t, sum_w x[w,t] = 1.
  - Each worker assigned to at most one task: for each w, sum_t x[w,t] <= 1.
  - Selection consistency: s[w] = sum_t x[w,t] (a worker is selected iff assigned).
  - Exactly 4 workers selected: sum_w s[w] = 4.
- Objective: minimize sum_{w,t} hours[w,t] * x[w,t].

Since 4 workers are selected and each takes exactly one of the 4 tasks, the "at most one task" constraint is automatically tight for selected workers, and the one left-out worker has s=0 and no assignment.