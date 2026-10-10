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

QUESTION: Is the goal to minimize the total number of hours worked across all four assigned tasks

## Turn 1 - User Simulator

Yes, the goal is to minimize the total number of hours worked across all four assigned tasks.

## Turn 2 - Generic Agent

QUESTION: Can a single selected worker be assigned to more than one

## Turn 2 - User Simulator

No. Each selected worker is assigned to exactly one of the four tasks.

## Turn 3 - Generic Agent

QUESTION: Is the "exactly 4 out of 5 workers must be selected" constraint a hard requirement that must be

## Turn 3 - User Simulator

Yes, it is a hard requirement.

## Turn 4 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize the total number of hours worked across all four tasks.
2.  **Decision Variables:** Binary variables $x_{ij}$ indicating whether worker $i$ is assigned to task $j$.
3.  **Workers:** 5 workers (I, V).
4.  **Tasks:** 4 tasks (A, B, C, D).
5.  **Selection Constraint:** Exactly 4 out of the 5 workers must be selected (i.e., exactly one worker is left unassigned).
6.  **Assignment Constraints:**
    *   Each task (A, B, C, D) must be assigned to exactly one worker.
    *   Each selected worker is assigned to exactly one task.
    *   The unselected worker is assigned to no tasks.
7.  **Costs:** The hours required for each worker-task pair are as given in the table:
    *   Worker I: A=9, B=4, C=3, D=7
    *   Worker II: A=4, B=6, C=5, D=6
    *   Worker III: A=5, B=4, C=7, D=5
    *   Worker IV: A=7, B=5, C=2, D=3
    *   Worker V: A=10, B=6, C=7, D=4

**Model Formulation:**

Let $x_{ij} \in \{0, 1\}$ be 1 if worker $i$ is assigned to task $j$, and 0 otherwise.

**Objective Function:**
$$ \text{Minimize } Z = \sum_{i=1}^{5} \sum_{j \in \{A,B,C,D\}} c_{ij} x_{ij} $$
where $c_{ij}$ is the hours required by worker $i$ for task $j$.

**Constraints:**

1.  **Each task is assigned to exactly one worker:**
    $$ \sum_{i=1}^{5} x_{ij} = 1 \quad \forall j \in \{A, B, C, D\} $$

2.  **Each worker is assigned to at most one task:**
    $$ \sum_{j \in \{A,B,C,D\}} x_{ij} \le 1 \quad \forall i \in \{I, II, III, IV, V\} $$

3.  **Exactly 4 workers are selected (assigned to a task):**
    $$ \sum_{i=1}^{5} \sum_{j \in \{A,B,C,D\}} x_{ij} = 4 $$

Note: Constraint 3 combined with Constraint 2 ensures that exactly 4 workers have a sum of 1 (selected) and one worker has a sum of 0 (unselected). Since there are 4 tasks and each task is assigned to exactly one worker, the total number of assignments is 4. If each worker can take at most one task, then exactly 4 workers must be used. Thus, Constraint 3 is actually redundant given Constraints 1 and 2, but it explicitly states the business requirement.