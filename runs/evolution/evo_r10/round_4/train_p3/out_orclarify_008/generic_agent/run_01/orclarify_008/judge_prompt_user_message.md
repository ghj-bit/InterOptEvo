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

QUESTION: Is the goal to minimize the total hours worked by the selected workers (i.e., the sum of the hours for the four task assignments), or is there a different objective such as minimizing the maximum hours any single worker works?

## Turn 1 - User Simulator

The goal is to minimize the total hours worked by the selected workers, which is the sum of the hours for the four task assignments.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned more than one of the four tasks, or must each of the four tasks go to a different worker (meaning one selected worker would be left with no task)?

## Turn 2 - User Simulator

Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Since exactly 4 workers are selected and each selected worker gets exactly one task, all 4 tasks are covered and the 5th worker is simply left out with no task and no cost — is that the correct reading, i.e., the unselected worker contributes nothing to the total hours?

## Turn 3 - User Simulator

Yes, that is correct. The unselected worker contributes nothing to the total hours.

## Turn 4 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Workers:** 5 workers (I–V); exactly 4 must be selected, so exactly 1 is left out.
- **Tasks:** 4 tasks (A, B, C, D); each task is assigned to exactly one worker.
- **Assignment rule:** Each selected worker is assigned to exactly one task (a bijection between the 4 selected workers and the 4 tasks). The unselected worker gets no task and contributes nothing.
- **Cost:** The hours table gives the hours a worker needs to complete a task; the objective is to **minimize the total hours** = the sum of the hours of the four (worker, task) assignments.
- **Decision variables:** Binary x[w,t] = 1 if worker w is assigned task t; binary s[w] = 1 if worker w is selected.
- **Constraints:**
  - Each task assigned to exactly one worker: Σ_w x[w,t] = 1 for each t.
  - Each selected worker gets exactly one task: Σ_t x[w,t] = s[w] for each w.
  - Exactly 4 workers selected: Σ_w s[w] = 4.
- **Objective:** Minimize Σ_w Σ_t hours[w,t] · x[w,t].

This is a small assignment/selection problem (equivalently, choose which worker to drop and then solve the 4×4 assignment). I will now formulate the model.