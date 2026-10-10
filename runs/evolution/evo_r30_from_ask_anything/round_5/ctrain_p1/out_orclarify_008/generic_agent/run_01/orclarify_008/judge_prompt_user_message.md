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

QUESTION: Is the goal to minimize the total hours worked across all four assigned tasks, or is there a different objective (such as minimizing the maximum hours for any single worker, or meeting a specific deadline)?

## Turn 1 - User Simulator

The goal is to minimize the total hours worked across all four assigned tasks.

## Turn 2 - Generic Agent

QUESTION: When assigning the four tasks to the four selected workers, is each worker allowed to perform at most one task, or can a single worker be assigned multiple tasks?

## Turn 2 - User Simulator

Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Are there any constraints on which specific worker can perform which specific task, or is any of the 5 workers allowed to perform any of the 4 tasks?

## Turn 3 - User Simulator

Any of the 5 workers is allowed to perform any of the 4 tasks.

## Turn 4 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize the total hours worked across all four tasks.
2.  **Workers:** There are 5 workers (I, V). Exactly 4 must be selected.
3.  **Tasks:** There are 4 tasks (A, B, C, D). Each task must be assigned to exactly one worker.
4.  **Assignment Rule:** Each of the 4 selected workers is assigned to exactly one task. This implies a one-to-one mapping between the 4 selected workers and the 4 tasks.
5.  **Eligibility:** Any worker can perform any task.
6.  **Data:** The hours required for each worker-task pair are provided in the table.

**Model Formulation:**

Let $x_{ij}$ be a binary variable where $x_{ij} = 1$ if worker $i$ is assigned to task $j$, and $0$ otherwise.
Let $y_i$ be a binary variable where $y_i = 1$ if worker $i$ is selected, and $0$ otherwise.

**Indices:**
*   $i \in \{I, II, III, IV, V\}$ (Workers)
*   $j \in \{A, B, C, D\}$ (Tasks)

**Objective Function:**
$$ \text{Minimize } Z = \sum_{i \in \text{Workers}} \sum_{j \in \text{Tasks}} h_{ij} x_{ij} $$
where $h_{ij}$ is the hours required for worker $i$ to complete task $j$.

**Constraints:**

1.  **Each task is assigned to exactly one worker:**
    $$ \sum_{i \in \text{Workers}} x_{ij} = 1 \quad \forall j \in \{A, B, C, D\} $$

2.  **Each selected worker is assigned to exactly one task:**
    $$ \sum_{j \in \text{Tasks}} x_{ij} = y_i \quad \forall i \in \{I, II, III, IV, V\} $$
    *(Note: If a worker is not selected, $y_i=0$, so they are assigned to no tasks. If selected, $y_i=1$, so they are assigned to exactly one task.)*

3.  **Exactly 4 workers are selected:**
    $$ \sum_{i \in \text{Workers}} y_i = 4 $$

4.  **Binary constraints:**
    $$ x_{ij} \in \{0, 1\} \quad \forall i, j $$
    $$ y_i \in \{0, 1\} \quad \forall i $$

This is a standard assignment problem variant with a cardinality constraint on the workers.