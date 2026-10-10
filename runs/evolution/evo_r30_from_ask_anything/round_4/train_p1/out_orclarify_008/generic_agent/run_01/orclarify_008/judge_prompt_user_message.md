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

QUESTION: Is the goal to minimize the total number of hours worked across all four assigned tasks, or is there a different objective such as minimizing the maximum hours for any single worker?

## Turn 1 - User Simulator

The goal is to minimize the total number of hours worked across all four assigned tasks.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned to more than one of the four tasks, or must each selected worker be assigned to exactly one task?

## Turn 2 - User Simulator

Each selected worker must be assigned to exactly one task.

## Turn 3 - Generic Agent

QUESTION: Since 4 workers are selected and each is assigned to exactly one task, does this mean that exactly 4 of the 5 workers are used, each handling one distinct task, leaving one worker unassigned?

## Turn 3 - User Simulator

Yes, exactly 4 of the 5 workers are used, each handling one distinct task, leaving one worker unassigned.

## Turn 4 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize the total number of hours worked across all four tasks.
2.  **Decision Variables:** Binary variables indicating which worker is assigned to which task.
3.  **Worker Selection:** Exactly 4 out of the 5 workers (I, II, III, IV, V) must be selected.
4.  **Task Assignment:** Each of the 4 tasks (A, B, C, D) must be assigned to exactly one worker.
5.  **Worker Load:** Each selected worker is assigned to exactly one task.
6.  **Unassigned Worker:** Exactly one worker is left unassigned.
7.  **Data:** The hours required for each worker-task pair are as provided in the table.

**Model Structure:**
-   Let $x_{ij}$ be a binary variable where $x_{ij} = 1$ if worker $i$ is assigned to task $j$, and 0 otherwise.
-   **Objective Function:** $\min \sum_{i=1}^{5} \sum_{j=1}^{4} h_{ij} x_{ij}$
-   **Constraints:**
    -   Each task is assigned to exactly one worker: $\sum_{i=1}^{5} x_{ij} = 1$ for all $j \in \{A, B, C, D\}$.
    -   Each worker is assigned to at most one task: $\sum_{j=1}^{4} x_{ij} \le 1$ for all $i \in \{I, II, III, IV, V\}$.
    -   Exactly 4 workers are selected: $\sum_{i=1}^{5} \sum_{j=1}^{4} x_{ij} = 4$. (Note: Given the previous two constraints, this is automatically satisfied if we ensure no worker takes multiple tasks and all tasks are covered, but it explicitly enforces the "4 out of 5" selection logic).