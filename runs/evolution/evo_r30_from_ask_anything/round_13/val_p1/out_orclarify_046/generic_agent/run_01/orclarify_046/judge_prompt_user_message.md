# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U5, U6, U9, U2, U3
I need help creating a duty scheduling plan for a university computer lab with undergraduate and graduate student workers, where there must be one and only one student on duty during open hours. Each undergraduate must work at least 8 hours per week, and each graduate student must work at least 7 hours per week. Additionally, for each student, their working hours on a given day cannot exceed the maximum hours specified in Table 5-9.

Table 5-9: Hourly wage and maximum duty hours from Monday to Friday for each student.

| Student ID | Wage (CNY/h) | Monday | Tuesday | Wednesday | Thursday | Friday |
|------------|--------------|--------|---------|-----------|----------|--------|
| 1          | 10.0         | 6      | 0       | 6         | 0        | 7      |
| 2          | 10.0         | 0      | 8       | 9         | 6        | 0      |
| 3          | 9.9          | 4      | 8       | 3         | 0        | 5      |
| 4          | 9.8          | 5      | 5       | 6         | 0        | 4      |
| 5          | 10.8         | 3      | 0       | 5         | 8        | 0      |
| 6          | 11.3         | 0      | 6       | 0         | 6        | 5      |

The lab operates from 8:00 AM to 10:00 PM.

## Problem units
- U1 (context): I need help creating a duty scheduling plan for a university computer lab with undergraduate and graduate student workers.
- U2 (data): Table 5-9: Hourly wage and maximum duty hours from Monday to Friday for each student.

| Student ID | Wage (CNY/h) | Monday | Tuesday | Wednesday | Thursday | Friday |
|------------|--------------|--------|---------|-----------|----------|--------|
| 1          | 10.0         | 6      | 0       | 6         | 0        | 7      |
| 2          | 10.0         | 0      | 8       | 9         | 6        | 0      |
| 3          | 9.9          | 4      | 8       | 3         | 0        | 5      |
| 4          | 9.8          | 5      | 5       | 6         | 0        | 4      |
| 5          | 10.8         | 3      | 0       | 5         | 8        | 0      |
| 6          | 11.3         | 0      | 6       | 0         | 6        | 5      |
- U3 (data): The lab operates from 8:00 AM to 10:00 PM.
- U4 (constraint): There must be one and only one student on duty during open hours.
- U5 (constraint): Each undergraduate must work at least 8 hours per week.
- U6 (constraint): Each graduate student must work at least 7 hours per week.
- U7 (constraint): Each student can work no more than 2 shifts per week.
- U8 (constraint): No more than 3 students can be scheduled for duty each day.
- U9 (constraint): For each student, their working hours on a given day cannot exceed the maximum hours specified in Table 5-9.
- U10 (objective): Minimize total gross pay (sum over all students of hourly wage multiplied by total hours worked during the week).

## Hidden slot scoring rules
## H1: max_shifts_per_week
- Severity: P1
- Severity reason: Without this constraint, the agent can still formulate a valid scheduling model using daily hour limits and coverage constraints, but the model would be under‑constrained and might assign a student to work on more than 2 distinct days, violating the intended business rule. The agent should clarify this before finalizing.
- Problem unit ID: U7
- Semantic hit rule: The Agent's question must ask about a limit on the number of shifts or working days per student per week.
- Reference acceptable questions:
  - Is there a limit on how many different days a student can work?
  - Can a student be scheduled on more than two days of the week?
- Failure modes:
  - Assuming there is no limit on the number of days a student can work, possibly scheduling a student across all 5 days
  - Assuming a 'shift' is the same as a day and not considering distinct time blocks

## H2: max_students_per_day
- Severity: P1
- Severity reason: Missing this constraint leads to a schedule that could assign more than three distinct students on any day, which might be a labor rule the problem intends. The agent can still build a coherent model without it, but the resulting schedule would not comply with the full specification, so clarification is needed for accuracy.
- Problem unit ID: U8
- Semantic hit rule: The Agent's question must inquire about a daily limit on the count of distinct students assigned to duty.
- Reference acceptable questions:
  - Is there a limit on the number of different students who can work on the same day?
  - Can I schedule all six students on a single day if their individual hours allow?
- Failure modes:
  - Assuming any number of students can be used per day as long as only one is on duty at a time
  - Overlooking the distinct-student-per-day cap and scheduling 4 or more students on one day

## H3: objective_minimize_gross_pay
- Severity: P0
- Severity reason: Without an explicit objective, the optimization problem is ill‑posed. The agent cannot build a meaningful model without knowing what to minimize or maximize. The objective must be clarified before modeling.
- Problem unit ID: U10
- Semantic hit rule: The Agent's question must explicitly ask about the optimization goal (objective), such as minimizing total cost or gross pay.
- Reference acceptable questions:
  - What is the objective of the optimization? Should we minimize total cost?
  - Are we trying to minimize the total wage payout?
- Failure modes:
  - Assuming the objective is to minimize the number of students used or total hours worked, rather than gross pay
  - Proceeding with a feasibility-only formulation without any objective


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the lab open for the full 14 hours (8:00 AM to 10:00 PM) every day from Monday through Friday, or are there specific open hours on certain days that differ from this range?

## Turn 1 - User Simulator

The lab is open for the full 14 hours, from 8:00 AM to 10:00 PM, every day from Monday through Friday.

## Turn 2 - Generic Agent

QUESTION: Are the maximum duty hours in Table 5-9 (e.g., 6, 8, 9) measured in hours, or do they represent a maximum number of discrete duty slots (e.g., 2-hour blocks) that a student can work on that day?

## Turn 2 - User Simulator

The maximum duty hours in Table 5-9 are measured in hours.

## Turn 3 - Generic Agent

QUESTION: Since the lab is open for 14 hours daily but the maximum daily hours for any single student in Table 5-9 is 9, is it required that the total hours worked by all students on a given day must sum to exactly 14 hours to cover the entire open period?

## Turn 3 - User Simulator

Yes, the total hours worked by all students on a given day must sum to exactly 14 hours to cover the entire open period.

## Turn 4 - Generic Agent

QUESTION: Is the objective of the scheduling plan to minimize the total weekly labor cost (sum of wage rate multiplied by hours worked for each student), or is there a different primary goal such as maximizing fairness or minimizing total hours worked?

## Turn 4 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 5 - Generic Agent

QUESTION: Are the decision variables representing the number of hours each student works on each day continuous (allowing fractional hours like 0.5) or must they be integers?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Should the hours worked by each student on each day be treated as continuous values (allowing fractions like 0.5 hours) or must they be whole numbers (integers)?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements for the schedule, such as limits on the number of days a student can work per week, requirements for consecutive days off, or restrictions on which students can work together?

## Turn 7 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 8 - Generic Agent

QUESTION: Regarding the constraint that each student can work no more than 2 shifts per week, does a "shift" refer to any day on which the student works at least one hour, or does it refer to a specific fixed time block?

## Turn 8 - User Simulator

A "shift" refers to any day on which the student works at least one hour.

## Turn 9 - Generic Agent

QUESTION: Regarding the constraint that no more than 3 students can be scheduled for duty each day, does this mean that on any given day, the number of students with a positive number of hours worked must be 3 or fewer?

## Turn 9 - User Simulator

Yes, on any given day, the number of students with a positive number of hours worked must be 3 or fewer.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total weekly labor cost (sum of hourly wage $\times$ hours worked for each student).
2.  **Time Horizon:** Monday through Friday.
3.  **Lab Hours:** 14 hours per day (8:00 AM – 10:00 PM).
4.  **Coverage Constraint:** The sum of hours worked by all students on each day must equal exactly 14 hours.
5.  **Student Minimums:**
    *   Undergraduate students (IDs 1, 2, 3, 4, 5, 6 - *Note: The prompt implies all are students, but typically "undergraduate" and "graduate" are distinct groups. The prompt says "undergraduate and graduate student workers" but doesn't explicitly map IDs to groups. However, the minimums are different: Undergrads $\ge$ 8 hrs/week, Graduates $\ge$ 7 hrs/week. **Assumption:** I need to know which IDs are undergrads and which are graduates. Let me check the prompt again. "undergraduate and graduate student workers... Each undergraduate must work at least 8 hours... each graduate student must work at least 7 hours." The table lists IDs 1-6. It does not specify which are which. This is a critical missing fact. I will flag this as an assumption or ask. Wait, I am in the "Ready to Model" phase. I should have asked this. Let me re-read the prompt. "I need help creating a duty scheduling plan for a university computer lab with undergraduate and graduate student workers...". It does not map IDs to types. I will assume for the summary that I need to clarify this, but since I am declaring readiness, I must list it as an assumption or I should have asked. Let's look at the "Stop Rule". "Declare readiness only when... every ambiguous stated quantity has a confirmed interpretation". The mapping of IDs to Undergrad/Grad is ambiguous. I should probably ask one more question or flag it. However, the prompt says "When you are ready to stop interviewing... start your response with READY_TO_MODEL". If I am not ready, I should ask. I am not fully ready because I don't know which students are undergrads and which are graduates.
    
    *Correction:* I should ask one more question about the student classification.

QUESTION: Which student IDs (1 through 6) are classified as undergraduates and which are classified as graduate students?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Since the classification of students as undergraduate or graduate is unconfirmed, should I assume all six students are undergraduates (requiring at least 8 hours per week each) for the purpose of this model?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Minimize total weekly labor cost (sum of hourly wage $\times$ hours worked for each student).
2.  **Time Horizon:** Monday through Friday.
3.  **Lab Hours:** 14 hours per day (8:00 AM – 10:00 PM).
4.  **Coverage Constraint:** The sum of hours worked by all students on each day must equal exactly 14 hours.
5.  **Student Minimums:**
    *   Undergraduate students: At least 8 hours per week.
    *   Graduate students: At least 7 hours per week.
    *   *Note: The specific classification of Student IDs 1-6 as undergraduate or graduate is unconfirmed.*
6.  **Daily Maximums:** Each student's hours on a given day cannot exceed the values in Table 5-9.
7.  **Shift Limit:** Each student can work on no more than 2 days per week (a "shift" is any day with > 0 hours).
8.  **Daily Headcount Limit:** On any given day, no more than 3 students can have positive hours worked.
9.  **Wages:** As specified in Table 5-9 (Student 1: 10.0, Student 2: 10.0, Student 3: 9.9, Student 4: 9.8, Student 5: 10.8, Student 6: 11.3 CNY/h).

**Explicit Assumptions:**

1.  **Student Classification:** Since the mapping of Student IDs to undergraduate/graduate status is unconfirmed, I will assume **all six students are undergraduates** for the formulation. This means each student must work at least 8 hours per week. If any are graduates, their minimum would be 7 hours, which is a looser constraint, so this assumption is conservative (harder to satisfy) and safe for feasibility, though it might slightly impact optimality if a graduate could work fewer hours.
2.  **Variable Domain:** Since the integrality of hours was unconfirmed, I will assume **continuous variables** (hours can be fractional, e.g., 0.5 hours). This is standard for time-based scheduling unless strict integer blocks are required.
3.  **Non-negativity:** All hours worked must be non-negative.
4.  **Binary Variables for Shifts:** To enforce the "max 2 shifts" and "max 3 students per day" constraints, binary variables will be used to indicate if a student works on a specific day.

**Model Structure:**

*   **Decision Variables:**
    *   $x_{i,d}$: Hours worked by student $i$ on day $d$ (continuous, $\ge 0$).
    *   $y_{i,d}$: Binary variable, 1 if student $i$ works on day $d$ ($x_{i,d} > 0$), 0 otherwise.

*   **Objective Function:**
    $$ \text{Minimize } Z = \sum_{i=1}^{6} \sum_{d=1}^{5} w_i \cdot x_{i,d} $$
    Where $w_i$ is the wage for student $i$.

*   **Constraints:**
    1.  **Daily Coverage:** For each day $d \in \{1..5\}$:
        $$ \sum_{i=1}^{6} x_{i,d} = 14 $$
    2.  **Daily Max Hours:** For each student $i$ and day $d$:
        $$ x_{i,d} \le M_{i,d} \cdot y_{i,d} $$
        Where $M_{i,d}$ is the max hours from Table 5-9. (This also links $x$ and $y$).
        Also, $x_{i,d} \le M_{i,d}$ is implied if $y=1$, but the big-M constraint handles the zero case.
    3.  **Weekly Minimum Hours:** For each student $i$:
        $$ \sum_{d=1}^{5} x_{i,d} \ge 8 $$
        *(Assumption: All are undergrads)*
    4.  **Max Shifts per Week:** For each student $i$:
        $$ \sum_{d=1}^{5} y_{i,d} \le 2 $$
    5.  **Max Students per Day:** For each day $d$:
        $$ \sum_{i=1}^{6} y_{i,d} \le 3 $$
    6.  **Non-negativity:** $x_{i,d} \ge 0$.
    7.  **Binary:** $y_{i,d} \in \{0, 1\}$.