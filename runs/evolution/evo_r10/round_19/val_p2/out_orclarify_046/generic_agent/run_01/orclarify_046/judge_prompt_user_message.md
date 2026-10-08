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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, but the daily maximum hours in Table 5-9 sum to at most 13 hours across all six students on some days (e.g., Monday: 6+0+4+5+3+0 = 18, but Tuesday: 0+8+8+5+0+6 = 27, while Wednesday: 6+9+3+6+5+0 = 29, Thursday: 0+6+0+0+8+6 = 20, Friday: 7+0+5+4+0+5 = 21) — so the table values are not the binding constraint on total coverage; could you confirm that the daily maximums in Table 5-9 are per-student caps (i.e., each student i can work at most that many hours on that day), and that the 14-hour daily coverage requirement is the hard constraint that must be met by splitting the day among students?

## Turn 1 - User Simulator

Yes, that is correct. The values in Table 5-9 are per-student maximum daily hours. The 14-hour daily coverage requirement is the hard constraint that must be met by splitting the day among the students.

## Turn 2 - Generic Agent

QUESTION: The objective is to minimize total weekly labor cost (sum of wage × hours worked), correct?

## Turn 2 - User Simulator

Yes, the objective is to minimize total weekly labor cost, which is the sum of each student's hourly wage multiplied by their total hours worked that week.

## Turn 3 - Generic Agent

QUESTION: The minimum weekly hours (8 for undergraduates, 7 for graduates) are hard lower bounds that must be satisfied, and the per-day maximums in Table 5-9 are hard upper bounds — so a feasible schedule must meet both, correct?

## Turn 3 - User Simulator

Yes, that is correct. The minimum weekly hours (8 for undergraduates, 7 for graduates) are hard lower bounds, and the per-day maximums in Table 5-9 are hard upper bounds. A feasible schedule must satisfy both.

## Turn 4 - Generic Agent

QUESTION: Which students are undergraduates and which are graduates?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Since the undergraduate/graduate split is still being confirmed internally, could you tell me whether the minimum weekly hours (8 vs 7) are the only place the distinction matters, so I can model it as a parameter you'll fill in later?

## Turn 5 - User Simulator

Yes, the undergraduate/graduate distinction only matters for the minimum weekly hours requirement (8 hours for undergraduates, 7 hours for graduates).

## Turn 6 - Generic Agent

QUESTION: Can a student's hours on a given day be any non-negative real number (e.g., 3.5 hours), or must they be whole hours?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: For the daily coverage, is it acceptable for a student to work a partial day (e.g., 3.5 hours on Monday), or must each student's daily shift be a whole number of hours?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is there any rule about how a student's hours on a given day must be arranged — for example, must a student's hours on a day form one contiguous block (a single shift), or can they be split into multiple separate blocks within the day?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how many students can be on duty at the same time, or is it simply that exactly one student is on duty at every moment from 8:00 AM to 10:00 PM?

## Turn 9 - User Simulator

It is simply that exactly one student is on duty at every moment from 8:00 AM to 10:00 PM.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or preferences I should be aware of, such as a student not working on consecutive days, a maximum number of days per week a student can work, or any other business rules?

## Turn 10 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 11 - Generic Agent

QUESTION: When you say "each student can work no more than 2 shifts per week," does a "shift" mean a day on which the student works at least one hour (i.e., a student can work on at most 2 of the 5 days), or does it mean something else?

## Turn 11 - User Simulator

A "shift" means a day on which the student works at least one hour. So each student can work on at most 2 of the 5 days.

## Turn 12 - Generic Agent

QUESTION: The constraint "no more than 3 students can be scheduled for duty each day" — does this mean that on any given day, at most 3 different students can have non-zero hours, or does it mean something else?

## Turn 12 - User Simulator

Yes, it means that on any given day, at most 3 different students can have non-zero hours.

## Turn 13 - Generic Agent

QUESTION: Since each student can work at most 2 days per week and at most 3 students can work each day, the maximum total coverage per day is 3 students × their daily max hours. For Monday, the top 3 daily maxes are Student 1 (6), Student 4 (5), Student 3 (4) = 15 hours, which is enough for 14. But for Tuesday, the top 3 are Student 2 (8), Student 3 (8), Student 4 (5) = 21, also enough. Could you confirm that the problem is guaranteed to be feasible under these constraints, or should I treat infeasibility as something to detect and report?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: For the "at most 3 students per day" constraint, is this a hard constraint (the schedule must satisfy it) or a soft preference (it can be violated if necessary to meet coverage)?

## Turn 14 - User Simulator

It is a hard constraint.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints, preferences, or business rules I should be aware of before I finalize the model?

## Turn 15 - User Simulator

No, there are no other constraints, preferences, or business rules beyond what has already been discussed.

## Turn 16 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the duty scheduling problem:

**Setting:**
- A university computer lab is open Monday through Friday, 8:00 AM to 10:00 PM (14 hours per day).
- Exactly one student must be on duty at every moment during open hours.
- Six students (IDs 1–6) are available, each with an hourly wage and per-day maximum hours as given in Table 5-9.

**Decision variables:**
- For each student *i* and each day *d* (Mon–Fri), the number of hours *x(i,d)* that student works on that day.
- The undergraduate/graduate classification of each student is a parameter to be filled in (it only affects the minimum weekly hours: 8 for undergrads, 7 for grads).
- Whether hours must be integral or can be fractional is pending internal confirmation; I will model hours as continuous (non-negative reals) as the default, which is the more general formulation.

**Objective:**
- Minimize total weekly labor cost = Σᵢ Σ_d wage(i) × x(i,d).

**Constraints:**
1. **Daily coverage (hard):** For each day *d*, Σᵢ x(i,d) = 14.
2. **Per-student daily maximum (hard):** For each student *i* and day *d*, x(i,d) ≤ max_hours(i,d) from Table 5-9.
3. **Minimum weekly hours (hard):** For each student *i*, Σ_d x(i,d) ≥ min_weekly(i), where min_weekly is 8 if *i* is an undergraduate and 7 if *i* is a graduate (classification to be confirmed).
4. **Maximum shifts per week (hard):** Each student works on at most 2 of the 5 days. This is modeled with binary variables y(i,d) ∈ {0,1} indicating whether student *i* works on day *d*, with x(i,d) ≤ M·y(i,d) (where M is the daily max for that student-day) and Σ_d y(i,d) ≤ 2.
5. **Maximum students per day (hard):** On each day *d*, at most 3 students have non-zero hours: Σᵢ y(i,d) ≤ 3.
6. **Non-negativity:** x(i,d) ≥ 0 for all i, d.

**Pending items (to be filled in as parameters):**
- Undergraduate vs. graduate classification for each student (affects constraint 3).
- Whether hours are integral or continuous (affects variable domains).
- Feasibility guarantee (the problem may or may not be feasible under all constraints; the model will detect infeasibility if it arises).