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

QUESTION: What is the objective of the scheduling plan — is it to minimize the total weekly labor cost (sum of wage × hours for all students), or is there another goal such as maximizing fairness or minimizing total hours worked?

## Turn 1 - User Simulator

The objective is to minimize the total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 2 - Generic Agent

QUESTION: The lab is open from 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times — does this mean the 14 hours are divided into 14 one-hour slots, and each student's daily hours must be an integer number of those slots (i.e., a student works whole consecutive or non-consecutive hours, but never a fraction of an hour)?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: For the "one and only one student on duty" requirement, is it sufficient that the sum of all students' hours on any given day equals exactly 14 (the total open hours), or must the schedule also specify which particular hours each student covers (i.e., a full hour-by-hour assignment)?

## Turn 3 - User Simulator

The point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: The table shows maximum hours per day for each student — for example, Student 1 has 0 on Tuesday and Thursday. Does a value of 0 mean that student is completely unavailable on that day (cannot work any hours), or does it simply mean their maximum is 0 so they happen to work nothing that day?

## Turn 4 - User Simulator

A value of 0 means that student is completely unavailable on that day and cannot work any hours.

## Turn 5 - Generic Agent

QUESTION: The minimum weekly hours are "at least 8" for undergraduates and "at least 7" for graduates — are all six students in the table undergraduates, or are some of them graduate students (and if so, which IDs are graduates)?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the graduate/undergraduate split is still being confirmed internally, may I proceed by treating all six students as undergraduates (each requiring at least 8 hours per week) for now, and you can correct me later if some are actually graduates?

## Turn 6 - User Simulator

Yes, you may proceed by treating all six students as undergraduates (each requiring at least 8 hours per week) for now.

## Turn 7 - Generic Agent

QUESTION: The two open items about the hour-by-hour structure (whether hours are whole 1-hour slots, and whether we need to assign specific hours or just daily totals) are still pending internal confirmation — may I proceed by modeling daily hours as non-negative integers (whole hours) and only requiring that the sum of all students' hours each day equals 14, without specifying which particular hours each student covers?

## Turn 7 - User Simulator

Yes, you may proceed by modeling daily hours as non-negative integers and only requiring that the sum of all students' hours each day equals 14, without specifying which particular hours each student covers.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints I should be aware of, such as a maximum number of days per week a student can work, a requirement that a student's daily hours be consecutive, or a cap on total weekly hours per student beyond the daily maximums?

## Turn 8 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 different students can be scheduled for duty on any single day.

## Turn 9 - Generic Agent

QUESTION: Regarding the "no more than 2 shifts per week" constraint — does a "shift" mean a day on which the student works at least 1 hour (i.e., each student can be on duty on at most 2 of the 5 days), or does it mean something else such as a fixed block of hours?

## Turn 9 - User Simulator

A "shift" means a day on which the student works at least 1 hour. So each student can be on duty on at most 2 of the 5 days.

## Turn 10 - Generic Agent

QUESTION: With each student limited to at most 2 days per week and at most 3 students per day, the maximum total hours per day is 3 × (max daily hours of the 3 chosen students). For example, on Monday the available students and their max hours are: Student 1 (6), Student 3 (4), Student 4 (5), Student 5 (3) — Student 2 and 6 are unavailable. The top 3 by max hours are Students 1, 4, 5 giving 6+5+3=14, which just meets the 14-hour requirement. Are you aware that this makes the schedule very tight on some days, and should I treat the 14-hour daily coverage as a hard requirement (the model must find a feasible solution or report infeasibility) rather than a soft target?

## Turn 10 - User Simulator

Yes, the 14-hour daily coverage is a hard requirement. The model must find a feasible solution that covers all 14 hours each day, or report infeasibility if no such schedule exists.

## Turn 11 - Generic Agent

QUESTION: For the "no more than 3 different students can be scheduled for duty on any single day" constraint — does this mean at most 3 students can have positive hours on a given day, or does it mean at most 3 students can be assigned to the lab that day regardless of whether they actually work?

## Turn 11 - User Simulator

It means at most 3 students can have positive hours on a given day.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint on the total number of hours a student can work in a single week beyond the daily maximums and the minimum of 8 hours — for example, a weekly cap like "no more than 20 hours per week" — or is the only weekly constraint the minimum of 8 hours?

## Turn 12 - User Simulator

The only weekly constraint is the minimum of 8 hours per week. There is no additional weekly cap beyond the daily maximums and the 2-shift limit.

## Turn 13 - Generic Agent

QUESTION: Are there any other constraints or preferences I should incorporate, such as a preference for spreading shifts evenly across the week, a requirement that a student cannot work on consecutive days, or any other business rules not yet mentioned?

## Turn 13 - User Simulator

No, there are no other constraints or preferences beyond what has already been discussed.

## Turn 14 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Minimize total weekly labor cost = sum over all students of (hourly wage × total hours worked that week).

**Decision variables:** For each student i (1–6) and each day d (Mon–Fri), let x(i,d) = number of hours student i works on day d. Variables are non-negative integers.

**Parameters (from Table 5-9):**
- Wage: Student 1: 10.0, Student 2: 10.0, Student 3: 9.9, Student 4: 9.8, Student 5: 10.8, Student 6: 11.3 (CNY/h)
- Daily max hours (0 = unavailable that day):
  - Student 1: Mon 6, Tue 0, Wed 6, Thu 0, Fri 7
  - Student 2: Mon 0, Tue 8, Wed 9, Thu 6, Fri 0
  - Student 3: Mon 4, Tue 8, Wed 3, Thu 0, Fri 5
  - Student 4: Mon 5, Tue 5, Wed 6, Thu 0, Fri 4
  - Student 5: Mon 3, Tue 0, Wed 5, Thu 8, Fri 0
  - Student 6: Mon 0, Tue 6, Wed 0, Thu 6, Fri 5

**Constraints:**
1. **Daily coverage (hard):** For each day d, the sum of x(i,d) over all students i equals exactly 14.
2. **Daily maximum:** x(i,d) ≤ max_hours(i,d) for all i, d. If max_hours(i,d) = 0, then x(i,d) = 0 (student unavailable).
3. **Weekly minimum:** For each student i, the sum of x(i,d) over all days d ≥ 8 (all treated as undergraduates).
4. **Shift limit:** For each student i, the number of days d on which x(i,d) ≥ 1 is at most 2.
5. **Daily student cap:** For each day d, the number of students i with x(i,d) ≥ 1 is at most 3.
6. **Integrality:** All x(i,d) are non-negative integers.

**Modeling notes:**
- Constraints 4 and 5 require binary auxiliary variables (e.g., y(i,d) = 1 if student i works on day d) to count active students per day and active days per student.
- The model is a mixed-integer linear program (MILP).
- If no feasible solution exists, the model should report infeasibility.