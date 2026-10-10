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

QUESTION: Is the goal to minimize the total hours across all four assigned tasks, or is there a different objective such as minimizing the maximum hours for any single worker?

## Turn 1 - User Simulator

The goal is to minimize the total hours across all four assigned tasks.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned to more than one of the four tasks, or is each worker limited to at most one task?

## Turn 2 - User Simulator

Each selected worker is limited to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Since exactly 4 workers are selected and each selected worker does exactly one task, does this mean the 4th task is assigned to the 4th selected worker, leaving exactly one worker unselected and unassigned?

## Turn 3 - User Simulator

Yes, exactly one worker is unselected and unassigned.

## Turn 4 - Generic Agent

QUESTION: Are there any additional constraints or requirements beyond the ones stated, such as a worker being unavailable for a specific task, a minimum or maximum number of hours for a particular task, or any other restrictions?

## Turn 4 - User Simulator

No, there are no additional constraints or requirements beyond the ones stated.

## Turn 5 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of your work assignment plan:

**Objective:**
*   Minimize the total hours required to complete all four tasks (A, B, C, D).

**Decision Variables:**
*   Binary variables indicating which worker is assigned to which task.
*   Binary variables indicating which worker is selected (or equivalently, which worker is left unassigned).

**Constraints:**
1.  **Task Assignment:** Each of the four tasks (A, B, C, D) must be assigned to exactly one worker.
2.  **Worker Selection:** Exactly 4 out of the 5 workers must be selected.
3.  **Worker Load:** Each selected worker is assigned to exactly one task.
4.  **Unassigned Worker:** Exactly one worker is unselected and performs no tasks.
5.  **No Other Restrictions:** There are no additional constraints regarding worker availability, task-specific limits, or other requirements.

**Data:**
*   The hours required for each worker to complete each task are as provided in the table:
    *   Worker I: A=9, B=4, C=3, D=7
    *   Worker II: A=4, B=6, C=5, D=6
    *   Worker III: A=5, B=4, C=7, D=5
    *   Worker IV: A=7, B=5, C=2, D=3
    *   Worker V: A=10, B=6, C=7, D=4

This is a standard assignment problem variant where we select a subset of workers to form a one-to-one mapping with the tasks, minimizing the total cost (hours).