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

QUESTION: Is the objective to minimize the total hours across all four assigned tasks?

## Turn 1 - User Simulator

Yes, the objective is to minimize the total working hours across all four assigned tasks.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned to more than one of the four tasks?

## Turn 2 - User Simulator

No. Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Are there any additional requirements or restrictions on which workers can be selected or which tasks they can perform that are not listed in the table?

## Turn 3 - User Simulator

No, there are no additional requirements or restrictions beyond what is listed in the table and the stated constraints.

## Turn 4 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize the total working hours across all four assigned tasks.
2.  **Decision Variables:** Binary variables indicating whether a specific worker is assigned to a specific task.
3.  **Worker Selection Constraint:** Exactly 4 out of the 5 workers must be selected.
4.  **Task Assignment Constraint:** Each of the four tasks (A, B, C, D) must be assigned to exactly one worker.
5.  **Worker Capacity Constraint:** Each selected worker is assigned to exactly one task (no worker handles multiple tasks).
6.  **Data:** The hours required for each worker-task pair are as provided in the table.
7.  **No Other Restrictions:** There are no additional constraints or exclusivity rules beyond those stated.

**Model Formulation:**

Let $x_{ij}$ be a binary variable where $i \in \{I, II, III, IV, V\}$ is the worker and $j \in \{A, B, C, D\}$ is the task. $x_{ij} = 1$ if worker $i$ is assigned to task $j$, and 0 otherwise.

**Objective Function:**
$$ \text{Minimize } Z = \sum_{i} \sum_{j} h_{ij} x_{ij} $$
where $h_{ij}$ is the hours required for worker $i$ to complete task $j$.

**Constraints:**

1.  **Each task is assigned to exactly one worker:**
    $$ \sum_{i} x_{ij} = 1 \quad \forall j \in \{A, B, C, D\} $$

2.  **Each worker is assigned to at most one task:**
    $$ \sum_{j} x_{ij} \le 1 \quad \forall i \in \{I, II, III, IV, V\} $$

3.  **Exactly 4 workers are selected:**
    Since each selected worker is assigned to exactly one task, the number of selected workers is equal to the number of assigned tasks. However, to explicitly enforce that exactly 4 distinct workers are used (and thus 1 is left out), we can use the constraint that the sum of all assignments is 4 (which is already implied by the task constraints) and that no worker is assigned more than one task.
    
    Actually, the constraint "Exactly 4 out of 5 workers must be selected" combined with "Each selected worker is assigned to exactly one task" and "Each task is assigned to exactly one worker" implies that 4 workers are used and 1 is not.
    
    Let $y_i$ be a binary variable indicating if worker $i$ is selected.
    $$ \sum_{i} y_i = 4 $$
    $$ \sum_{j} x_{ij} = y_i \quad \forall i $$
    
    This ensures that if a worker is selected ($y_i=1$), they are assigned to exactly one task ($\sum x_{ij}=1$). If not selected ($y_i=0$), they are assigned to no tasks ($\sum x_{ij}=0$).

    Alternatively, without $y_i$:
    The constraint $\sum_{j} x_{ij} \le 1$ for all $i$ and $\sum_{i} x_{ij} = 1$ for all $j$ ensures that 4 workers are assigned to 4 tasks. Since there are 5 workers and 4 tasks, exactly one worker will have $\sum_{j} x_{ij} = 0$. This naturally satisfies the "exactly 4 workers selected" condition.

    So the simplified constraints are:
    1. $\sum_{i} x_{ij} = 1$ for all $j \in \{A, B, C, D\}$
    2. $\sum_{j} x_{ij} \le 1$ for all $i \in \{I, II, III, IV, V\}$
    3. $x_{ij} \in \{0, 1\}$ for all $i, j$