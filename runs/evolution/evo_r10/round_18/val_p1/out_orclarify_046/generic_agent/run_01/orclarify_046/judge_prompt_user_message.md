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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, so 14 student-hours are needed each day — but the sum of the daily maximum hours in Table 5-9 is only 12 on Monday, 10 on Tuesday, 12 on Wednesday, 12 on Thursday, and 16 on Friday. Since the daily maximums cannot be exceeded, the lab cannot be fully covered on Monday through Thursday as stated. Which reading should I use: (a) the open hours are actually shorter than 8:00–22:00 (if so, how many hours per day), (b) the daily maximums in the table are per-student caps and the lab may be understaffed on some days (i.e., coverage is not required for the full 14 hours), or (c) the objective is to minimize total wage cost subject to the weekly minimums and daily caps, with no requirement that every hour of the day be covered?

## Turn 1 - User Simulator

The open hours are indeed 8:00 AM to 10:00 PM (14 hours), and exactly one student must be on duty during all open hours. Therefore, 14 student-hours are required each day.

The daily maximums in Table 5-9 are per-student caps. The sum of these caps across all students for a given day represents the maximum total hours that can be scheduled for that day. If the sum of the daily maximums is less than 14, it is impossible to cover the full 14 hours with the available students under the given constraints.

Please confirm: Is the data in Table 5-9 correct as provided? If so, the problem as stated is infeasible for Monday through Thursday because the total available hours (sum of individual daily caps) is less than the required 14 hours. There is no option for understaffing or partial coverage; full coverage is mandatory.

## Turn 2 - Generic Agent

QUESTION: You've confirmed the problem is infeasible as stated (daily caps sum to less than 14 on Monday–Thursday). To make it solvable, which correction should I apply: (a) the daily maximums in Table 5-9 are actually the *minimum* hours each student must work that day (so the caps are removed and only the weekly minimums of 8/7 hours plus the 14-hour daily coverage constraint bind), (b) the table values should be read as the maximum hours but the lab's open hours are shorter than 14 (please give the actual daily open hours), or (c) the table is correct and I should treat the daily caps as soft (allowing overtime beyond the cap at a penalty) so full 14-hour coverage is always achievable?

## Turn 2 - User Simulator

The table is correct, and the daily caps are hard constraints. The lab's open hours are 8:00 AM to 10:00 PM (14 hours).

However, I need to correct my previous statement. The constraint is that **no more than 3 students** can be scheduled for duty each day. This is a key constraint I missed in my initial feasibility check.

Let's re-evaluate the feasibility with the "max 3 students per day" constraint:

*   **Monday:** Max hours for top 3 students: Student 1 (6) + Student 4 (5) + Student 3 (4) = 15 hours. (15 >= 14, Feasible)
*   **Tuesday:** Max hours for top 3 students: Student 2 (8) + Student 3 (8) + Student 6 (6) = 22 hours. (22 >= 14, Feasible)
*   **Wednesday:** Max hours for top 3 students: Student 2 (9) + Student 4 (6) + Student 1 (6) = 21 hours. (21 >= 14, Feasible)
*   **Thursday:** Max hours for top 3 students: Student 5 (8) + Student 2 (6) + Student 6 (6) = 20 hours. (20 >= 14, Feasible)
*   **Friday:** Max hours for top 3 students: Student 1 (7) + Student 3 (5) + Student 6 (5) = 17 hours. (17 >= 14, Feasible)

So, the problem is feasible. The daily caps are hard constraints, the open hours are 14 hours, and full coverage is required. The "max 3 students per day" constraint is what makes the problem solvable despite the low individual caps, because it forces the selection of the highest-capacity students for each day.

Please proceed with the original problem statement:
1.  Minimize total gross pay.
2.  One student on duty at all times (14 hours/day).
3.  Undergrads: >= 8 hours/week.
4.  Grad students: >= 7 hours/week.
5.  Max 2 shifts per student per week.
6.  Max 3 students on duty per day.
7.  Daily hours per student <= Table 5-9 caps.

## Turn 3 - Generic Agent

QUESTION: The "max 3 students per day" constraint doesn't actually resolve the infeasibility — the sum of ALL six students' daily caps is still only 12 on Monday, 10 on Tuesday, 12 on Wednesday, and 12 on Thursday, which is below the required 14 hours regardless of how many students work. So the problem remains infeasible on those days. Given that, which correction should I apply to make the problem solvable: (a) the daily caps in Table 5-9 are actually the *minimum* hours each student must work that day (not maximums), (b) the lab's open hours are shorter than 14 hours per day (please specify how many), or (c) the daily caps are soft constraints that can be exceeded at an overtime penalty?

## Turn 3 - User Simulator

The table is correct, and the daily caps are hard constraints. The lab's open hours are 8:00 AM to 10:00 PM (14 hours).

I must correct my previous error. I incorrectly summed the top 3 students' caps. The sum of **all** students' caps is indeed:
*   Monday: 6+0+4+5+3+0 = 18 hours.
*   Tuesday: 0+8+8+5+0+6 = 27 hours.
*   Wednesday: 6+9+3+6+5+0 = 29 hours.
*   Thursday: 0+6+0+0+8+6 = 20 hours.
*   Friday: 7+0+5+4+0+5 = 21 hours.

Wait, let me re-read the table carefully.

| Student ID | Monday | Tuesday | Wednesday | Thursday | Friday |
|------------|--------|---------|-----------|----------|--------|
| 1          | 6      | 0       | 6         | 0        | 7      |
| 2          | 0      | 8       | 9         | 6        | 0      |
| 3          | 4      | 8       | 3         | 0        | 5      |
| 4          | 5      | 5       | 6         | 0        | 4      |
| 5          | 3      | 0       | 5         | 8        | 0      |
| 6          | 0      | 6       | 0         | 6        | 5      |

Sum of all caps:
*   Monday: 6+0+4+5+3+0 = 18
*   Tuesday: 0+8+8+5+0+6 = 27
*   Wednesday: 6+9+3+6+5+0 = 29
*   Thursday: 0+6+0+0+8+6 = 20
*   Friday: 7+0+5+4+0+5 = 21

All sums are >= 14. The problem is feasible. The previous assistant's claim that the sum was 12, 10, 12, 12 was incorrect.

Therefore, no correction is needed. The problem is solvable as stated. Please proceed with the original constraints.

## Turn 4 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, since the weekly minimums differ (8 hours for undergrads, 7 hours for grads)?

## Turn 4 - User Simulator

Students 1, 2, 3, and 4 are undergraduates. Students 5 and 6 are graduate students.

## Turn 5 - Generic Agent

QUESTION: You mentioned a "max 2 shifts per student per week" constraint — does this mean each student can work on at most 2 different days per week (i.e., if a student works Monday and Wednesday, that's 2 shifts and they cannot work any other day)?

## Turn 5 - User Simulator

Yes, that is correct. Each student can work on at most 2 different days per week.

## Turn 6 - Generic Agent

QUESTION: Is the "max 3 students on duty per day" constraint a hard requirement (i.e., at most 3 students can be scheduled to work on any given day), or was it just a feasibility-check heuristic you used and not an actual constraint of the problem?

## Turn 6 - User Simulator

It is a hard requirement. No more than 3 students can be scheduled for duty on any given day.

## Turn 7 - Generic Agent

QUESTION: Since exactly one student is on duty at all times and each student works a single continuous block of hours per day (up to their daily cap), is the objective simply to minimize total weekly wage cost (sum of hours worked × hourly wage for each student), with no other costs or preferences to consider?

## Turn 7 - User Simulator

Yes, the objective is simply to minimize the total weekly wage cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week. There are no other costs or preferences to consider.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Setting:** A university computer lab open 8:00 AM to 10:00 PM (14 hours) Monday through Friday. Exactly one student must be on duty at all times, so 14 student-hours are required each day.

- **Students:** 6 students total.
  - Undergraduates: Students 1, 2, 3, 4 (minimum 8 hours/week each).
  - Graduates: Students 5, 6 (minimum 7 hours/week each).

- **Decision variables:** For each student and each day (Mon–Fri), the number of hours that student works (continuous, non-negative).

- **Constraints:**
  1. **Daily coverage:** For each day, the sum of hours worked by all students equals exactly 14.
  2. **Daily caps:** Each student's hours on a given day ≤ the value in Table 5-9 (hard constraint).
  3. **Weekly minimums:** Undergrads (1–4) work ≥ 8 hours total per week; Graduates (5–6) work ≥ 7 hours total per week.
  4. **Max days per student:** Each student works on at most 2 different days per week (i.e., at most 2 of the 5 daily hour-variables can be positive for each student).
  5. **Max students per day:** At most 3 students are scheduled (i.e., have positive hours) on any given day.

- **Objective:** Minimize total weekly wage cost = Σ (student's hourly wage × total hours worked that week).

- **Wages (CNY/h):** S1=10.0, S2=10.0, S3=9.9, S4=9.8, S5=10.8, S6=11.3.

- **Daily caps (hours):**

| Student | Mon | Tue | Wed | Thu | Fri |
|---------|-----|-----|-----|-----|-----|
| 1       | 6   | 0   | 6   | 0   | 7   |
| 2       | 0   | 8   | 9   | 6   | 0   |
| 3       | 4   | 8   | 3   | 0   | 5   |
| 4       | 5   | 5   | 6   | 0   | 4   |
| 5       | 3   | 0   | 5   | 8   | 0   |
| 6       | 0   | 6   | 0   | 6   | 5   |

- **Model type:** Mixed-integer linear program (binary variables to enforce the "at most 2 days" and "at most 3 students per day" constraints, continuous variables for hours).