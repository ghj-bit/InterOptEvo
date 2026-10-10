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

QUESTION: Is the goal to minimize the total hours across all four assigned tasks?

## Turn 1 - User Simulator

Yes, the goal is to minimize the total working hours across all four assigned tasks.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned to more than one of the four tasks?

## Turn 2 - User Simulator

No. Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Are there any additional requirements, such as a worker being unavailable for a specific task or a minimum number of hours a selected worker must work?

## Turn 3 - User Simulator

No, there are no additional requirements like worker unavailability for specific tasks or minimum hours per selected worker.

## Turn 4 - Generic Agent

READY_TO_MODEL
I have gathered all necessary information to formulate the work assignment plan. Here is the summary of the confirmed understanding:

**Objective**
*   **Goal:** Minimize the total working hours across all four assigned tasks.
*   **Status:** Confirmed.

**Decision Variables**
*   **Selection:** Binary variables indicating which 4 out of the 5 workers are selected.
*   **Assignment:** Binary variables indicating which task (A, B, C, D) is assigned to which selected worker.
*   **Status:** Confirmed.

**Constraints**
1.  **Worker Selection:** Exactly 4 out of the 5 workers must be selected.
    *   **Status:** Confirmed.
2.  **Task Assignment:** Each task (A, B, C, D) must be assigned to exactly one worker.
    *   **Status:** Confirmed.
3.  **Worker Load:** Each selected worker is assigned to exactly one task.
    *   **Status:** Confirmed.
4.  **Unselected Workers:** The one unselected worker is assigned to no tasks.
    *   **Status:** Confirmed (implied by "exactly 4 selected" and "each selected worker assigned to exactly one task").
5.  **Additional Restrictions:** There are no worker unavailability constraints, minimum hour requirements, or other hidden constraints.
    *   **Status:** Confirmed.

**Data**
*   **Hours Matrix:**
    *   Worker I: A=9, B=4, C=3, D=7
    *   Worker II: A=4, B=6, C=5, D=6
    *   Worker III: A=5, B=4, C=7, D=5
    *   Worker IV: A=7, B=5, C=2, D=3
    *   Worker V: A=10, B=6, C=7, D=4
    *   **Status:** Confirmed.

**Assumptions**
*   None. All critical facts were explicitly confirmed by the user.