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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours per day), but the maximum daily hours in Table 5-9 are at most 9, so no single student can cover a whole day. Does the day need to be split into fixed time slots (e.g., 2-hour blocks) with exactly one student assigned to each slot, and if so, how many slots per day and what are their start/end times?

## Turn 1 - User Simulator

Yes, the day needs to be split into fixed time slots.

There are 7 slots per day.

The start and end times for the slots are:
1. 8:00 AM – 10:00 AM
2. 10:00 AM – 12:00 PM
3. 12:00 PM – 2:00 PM
4. 2:00 PM – 4:00 PM
5. 4:00 PM – 6:00 PM
6. 6:00 PM – 8:00 PM
7. 8:00 PM – 10:00 PM

## Turn 2 - Generic Agent

QUESTION: The maximum daily hours in Table 5-9 are not all multiples of 2 (e.g., student 1 has 6, 6, 7; student 3 has 4, 8, 3, 5; student 5 has 3, 5, 8), but each slot is 2 hours long. How should I interpret these maximums — are they in hours (so a student can work at most floor(max/2) slots per day, e.g., 7 hours = 3 slots), or should I treat them as a cap on total hours where a student may work a partial slot to hit the exact hour?

## Turn 2 - User Simulator

The maximums are in hours. A student may work a partial slot to hit the exact hour cap.

## Turn 3 - Generic Agent

QUESTION: Since a student may work a partial slot, how is the "exactly one student on duty" requirement enforced when a slot is split between two students — is it that the sum of the two students' hours in that slot must equal exactly 2 hours (so coverage is continuous), and can a single slot be split among at most two students, or any number?

## Turn 3 - User Simulator

The sum of the hours worked by all students in a slot must equal exactly 2 hours. A single slot can be split among any number of students.

## Turn 4 - Generic Agent

QUESTION: What is the objective of the scheduling plan — is it to minimize the total weekly labor cost (sum of wage × hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 4 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 5 - Generic Agent

QUESTION: The weekly minimums are "at least 8 hours" for undergraduates and "at least 7 hours" for graduates. Are these minimums hard constraints (the schedule must satisfy them, and if infeasible the problem has no solution), or are they soft targets that can be violated at some penalty?

## Turn 5 - User Simulator

These minimums are hard constraints.

## Turn 6 - Generic Agent

QUESTION: Which students are undergraduates and which are graduates? The table lists students 1–6 but doesn't specify their level, and the minimum hours differ by level (8 vs 7).

## Turn 6 - User Simulator

Students 1, 2, and 3 are undergraduates. Students 4, 5, and 6 are graduates.

## Turn 7 - Generic Agent

QUESTION: The daily maximums in Table 5-9 are given only for Monday through Friday. Does the lab operate only Monday–Friday (5 days), or does it also operate on weekends (Saturday/Sunday), and if so, what are the maximum daily hours for students on those days?

## Turn 7 - User Simulator

The lab operates only Monday through Friday.

## Turn 8 - Generic Agent

QUESTION: A student's daily hours are capped by the Table 5-9 maximum for that day. Is there any additional constraint that a student cannot work two consecutive slots (i.e., must have a break between slots), or can a student work any combination of slots within their daily cap, including back-to-back slots?

## Turn 8 - User Simulator

A student can work any combination of slots within their daily cap, including back-to-back slots.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how many days per week a single student can work (e.g., a student must have at least one day off), or can a student work all five days as long as their daily hours stay within the Table 5-9 caps and their weekly total meets the minimum?

## Turn 9 - User Simulator

There is a limit. Each student cannot work more than 2 shifts in a week.

## Turn 10 - Generic Agent

QUESTION: You mentioned each student cannot work more than 2 shifts in a week. Does "shift" mean a single day on which the student works at least one slot (so a student can work at most 2 of the 5 days), or does it mean something else like a contiguous block of slots?

## Turn 10 - User Simulator

"Shift" means a single day on which the student works at least one slot. A student can work at most 2 of the 5 days.

## Turn 11 - Generic Agent

QUESTION: Let me verify feasibility before I finalize. With each student working at most 2 days, the maximum weekly hours are: student 1 = 13, student 2 = 17, student 3 = 13, student 4 = 11, student 5 = 13, student 6 = 11, totaling 78 hours. But the lab needs 70 hours of coverage (5 days × 7 slots × 2 hours). The minimums require at least 39 hours (3×8 + 3×7). So 70 hours of coverage must come from a total capacity of 78, leaving only 8 hours of slack. Is this correct, or did I misread any of the constraints?

## Turn 11 - User Simulator

Your calculation is correct. The total maximum weekly capacity is 78 hours, and the required coverage is 70 hours, leaving 8 hours of slack.

## Turn 12 - Generic Agent

QUESTION: Since the problem is very tight (78 max capacity vs 70 required), I want to confirm the daily maximums are hard caps that cannot be exceeded under any circumstances — i.e., a student's hours on a given day must be strictly ≤ the Table 5-9 value for that day, with no overtime or exceptions allowed?

## Turn 12 - User Simulator

Yes, the daily maximums in Table 5-9 are hard caps. A student's hours on a given day must be strictly less than or equal to the Table 5-9 value for that day.

## Turn 13 - Generic Agent

QUESTION: One final check on the slot-splitting rule: when a slot is split among multiple students, is there any minimum number of hours a student must work in a slot to count (e.g., at least 0.5 hours), or can a student work any positive fraction of a slot (e.g., 0.1 hours) as long as the sum across all students in that slot equals exactly 2 hours?

## Turn 13 - User Simulator

A student can work any positive fraction of a slot, such as 0.1 hours, as long as the sum across all students in that slot equals exactly 2 hours.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Setting:**
- A university computer lab open Monday–Friday, 8:00 AM to 10:00 PM (14 hours/day).
- Each day is divided into 7 fixed 2-hour slots: 8–10, 10–12, 12–14, 14–16, 16–18, 18–20, 20–22.
- 6 student workers: students 1, 2, 3 are undergraduates; students 4, 5, 6 are graduates.

**Decision variables:**
- For each student *i*, day *d*, and slot *s*: the number of hours *x_{i,d,s}* that student *i* works in slot *s* on day *d* (continuous, ≥ 0).

**Objective:**
- Minimize total weekly labor cost = Σ (wage_i × total hours worked by student i over the week).

**Constraints:**
1. **Coverage:** For every day *d* and slot *s*, the sum of hours across all 6 students equals exactly 2 hours.
2. **Daily cap:** For each student *i* and day *d*, the sum of hours across all 7 slots ≤ the Table 5-9 maximum for that student and day.
3. **Weekly minimum:** Students 1, 2, 3 (undergrads) each work ≥ 8 hours total over the week; students 4, 5, 6 (grads) each work ≥ 7 hours total over the week.
4. **Max days worked:** Each student works on at most 2 of the 5 days (a day counts as "worked" if the student works at least one positive hour in any slot that day).
5. **Non-negativity:** All *x_{i,d,s}* ≥ 0. A student may work any positive fraction of a slot; a slot may be split among any number of students.

**Parameters (Table 5-9):**

| Student | Wage (CNY/h) | Mon | Tue | Wed | Thu | Fri |
|---------|-------------|-----|-----|-----|-----|-----|
| 1 (UG)  | 10.0        | 6   | 0   | 6   | 0   | 7   |
| 2 (UG)  | 10.0        | 0   | 8   | 9   | 6   | 0   |
| 3 (UG)  | 9.9         | 4   | 8   | 3   | 0   | 5   |
| 4 (G)   | 9.8         | 5   | 5   | 6   | 0   | 4   |
| 5 (G)   | 10.8        | 3   | 0   | 5   | 8   | 0   |
| 6 (G)   | 11.3        | 0   | 6   | 0   | 6   | 5   |

**Feasibility note:** Total maximum weekly capacity is 78 hours; required coverage is 70 hours, leaving 8 hours of slack. The problem is tight but feasible.