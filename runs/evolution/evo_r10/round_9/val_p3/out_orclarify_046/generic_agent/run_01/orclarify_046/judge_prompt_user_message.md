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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, so the weekly on-duty hours total 70. But the sum of each student's maximum hours across Monday–Friday is only 56, which cannot cover 70 hours. Does the lab also operate on Saturday and Sunday (with the same 8:00 AM–10:00 PM hours and the same per-day maximums), or should the schedule instead cover only Monday–Friday with a different interpretation of the open hours?

## Turn 1 - User Simulator

The schedule covers only Monday through Friday. The lab does not operate on Saturday or Sunday.

## Turn 2 - Generic Agent

QUESTION: Since the lab is open 14 hours each day (8:00 AM–10:00 PM) and exactly one student must be on duty at all times, the weekly on-duty hours total 70, but the sum of all students' maximum hours across Monday–Friday is only 56. Given that the schedule covers only Monday–Friday, should I treat the per-day maximums in Table 5-9 as the binding limits (making the problem infeasible as stated), or is the intended interpretation that the lab is open for fewer hours per day (for example, only the hours that the maximums allow), so that "one and only one student on duty" applies only during the actually-open hours?

## Turn 2 - User Simulator

The per-day maximums in Table 5-9 are the binding limits. The lab is open for fewer hours per day than 8:00 AM to 10:00 PM. The "one and only one student on duty" requirement applies only during the actually-open hours, which are determined by the maximums in the table.

## Turn 3 - Generic Agent

QUESTION: The per-day maximums in Table 5-9 sum to 56 hours over the week, but the minimum requirements (undergraduates at least 8 hours, graduates at least 7 hours) sum to at least 45 hours, so the open hours are not simply the sum of the maximums. How exactly are the actually-open hours per day determined — for example, is the lab open for a fixed number of hours each day that I should treat as a given (and if so, how many hours per day), or are the open hours a decision to be determined as part of the schedule?

## Turn 3 - User Simulator

The lab is open for a fixed number of hours each day. The open hours per day are not a decision variable; they are given. However, the specific number of open hours per day is not provided in the original request or the supplied business facts. This point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the open hours per day are fixed but not yet specified, and the per-day maximums in Table 5-9 are the binding limits, should I treat the lab's open hours on each day as equal to the sum of the maximum hours across all students for that day (i.e., Monday 18, Tuesday 20, Wednesday 23, Thursday 20, Friday 16), or are the open hours a separate given value that you will provide for each day?

## Turn 4 - User Simulator

The open hours are a separate given value for each day. They are not equal to the sum of the maximum hours across all students for that day. The specific open hours for each day still need internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Which students are undergraduates and which are graduate students, since the minimum weekly hours differ (undergraduates at least 8 hours, graduates at least 7 hours)?

## Turn 5 - User Simulator

Students 1, 2, and 3 are undergraduates. Students 4, 5, and 6 are graduate students.

## Turn 6 - Generic Agent

QUESTION: What is the objective of the scheduling plan — is it to minimize the total weekly wage cost of the on-duty hours, or is there another objective (such as maximizing fairness or minimizing total hours)?

## Turn 6 - User Simulator

The objective is to minimize the total weekly wage cost of the on-duty hours.

## Turn 7 - Generic Agent

QUESTION: The open hours per day are fixed but not yet given, and the per-day maximums in Table 5-9 are the binding limits. Since the open hours must be coverable by the students' maximums, should I treat the open hours on each day as a parameter that you will provide (and I should leave as a symbolic input in the model), or should I assume the open hours on each day equal the sum of the maximum hours across all students for that day (Monday 18, Tuesday 20, Wednesday 23, Thursday 20, Friday 16)?

## Turn 7 - User Simulator

The open hours on each day are a parameter that I will provide. You should leave them as a symbolic input in the model. They are not equal to the sum of the maximum hours across all students for that day.

## Turn 8 - Generic Agent

QUESTION: When a student's on-duty hours on a given day are less than that student's maximum for that day, is the unused capacity simply free (i.e., no penalty or requirement to use it), or is there any penalty or conservation requirement on unused capacity?

## Turn 8 - User Simulator

The unused capacity is simply free. There is no penalty or requirement to use it.

## Turn 9 - Generic Agent

QUESTION: Are the on-duty hours for each student on each day continuous (i.e., a student can work any fractional number of hours up to their maximum), or must they be integer hours?

## Turn 9 - User Simulator

The on-duty hours for each student on each day must be integer hours.

## Turn 10 - Generic Agent

QUESTION: The minimum weekly hours (undergraduates at least 8, graduates at least 7) — are these lower bounds that a student's total weekly on-duty hours must meet or exceed, or are they exact targets that must be met precisely?

## Turn 10 - User Simulator

They are lower bounds. A student's total weekly on-duty hours must meet or exceed the minimum.

## Turn 11 - Generic Agent

QUESTION: The per-day maximums in Table 5-9 — are these upper bounds that a student's on-duty hours on that day must not exceed, or are they exact targets that must be met precisely?

## Turn 11 - User Simulator

They are upper bounds. A student's on-duty hours on a given day must not exceed the maximum specified in Table 5-9.

## Turn 12 - Generic Agent

QUESTION: The "one and only one student on duty" requirement — does this mean that at any given hour during the open hours, exactly one student is on duty (so the sum of all students' on-duty hours on a given day equals the open hours for that day), or does it mean that exactly one student is assigned to cover the entire day's open hours (so only one student works on each day)?

## Turn 12 - User Simulator

It means that at any given hour during the open hours, exactly one student is on duty. Therefore, the sum of all students' on-duty hours on a given day equals the open hours for that day.

## Turn 13 - Generic Agent

QUESTION: The open hours per day are a symbolic input that you will provide. For the model to be feasible, the open hours on each day must not exceed the sum of the maximum hours across all students for that day (Monday 18, Tuesday 20, Wednesday 23, Thursday 20, Friday 16). Should I include a constraint in the model that enforces this feasibility condition, or should I assume the open hours you provide will always satisfy this condition?

## Turn 13 - User Simulator

You should assume the open hours I provide will always satisfy this condition.

## Turn 14 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Scope:** Monday through Friday only. No weekend operation.
- **Decision variables:** For each student i (1–6) and each day d (Mon–Fri), the integer number of on-duty hours x(i,d) ≥ 0.
- **Objective:** Minimize total weekly wage cost = Σ_i Σ_d wage_i × x(i,d).
- **Coverage constraint:** For each day d, Σ_i x(i,d) = H_d, where H_d is the given (symbolic) number of open hours on day d. Exactly one student is on duty at every hour, so the sum of all students' hours on a day equals the open hours.
- **Per-day upper bounds:** x(i,d) ≤ M(i,d), where M(i,d) is the maximum from Table 5-9. These are binding upper bounds.
- **Weekly minimums:** Students 1, 2, 3 (undergraduates): Σ_d x(i,d) ≥ 8. Students 4, 5, 6 (graduates): Σ_d x(i,d) ≥ 7. These are lower bounds.
- **Integrality:** All x(i,d) are non-negative integers.
- **Unused capacity:** Free; no penalty or conservation requirement.
- **Feasibility assumption:** The provided H_d values will always satisfy Σ_i M(i,d) ≥ H_d for each day.
- **Wages (CNY/h):** Student 1: 10.0, Student 2: 10.0, Student 3: 9.9, Student 4: 9.8, Student 5: 10.8, Student 6: 11.3.
- **Maximum hours (Table 5-9):**
  - Student 1: Mon 6, Tue 0, Wed 6, Thu 0, Fri 7
  - Student 2: Mon 0, Tue 8, Wed 9, Thu 6, Fri 0
  - Student 3: Mon 4, Tue 8, Wed 3, Thu 0, Fri 5
  - Student 4: Mon 5, Tue 5, Wed 6, Thu 0, Fri 4
  - Student 5: Mon 3, Tue 0, Wed 5, Thu 8, Fri 0
  - Student 6: Mon 0, Tue 6, Wed 0, Thu 6, Fri 5