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

QUESTION: The lab is open 8:00 AM to 10:00 PM (14 hours) and exactly one student must be on duty at all times, so 14 person-hours are needed each day. But the sum of the daily maximum hours in Table 5-9 is only 12 on Monday, 18 on Tuesday, 14 on Wednesday, 12 on Thursday, and 21 on Friday. Since Monday and Thursday cannot reach 14 hours, how should the model handle those days — for example, should the requirement be relaxed to "cover as many of the 14 hours as possible" (minimizing uncovered hours), or should the lab's open hours be shortened on those days to match what the students can supply?

## Turn 1 - User Simulator

The lab’s open hours must remain 8:00 AM to 10:00 PM every day. The requirement is to cover all 14 hours each day with exactly one student on duty at all times. If the available student capacity on a given day is insufficient to cover the full 14 hours, that is a feasibility issue that needs to be resolved by adjusting the student roster or their availability, not by relaxing the coverage requirement or shortening the lab’s open hours.

## Turn 2 - Generic Agent

QUESTION: The lab must be covered for all 14 hours each day, but the sum of the daily maximum hours in Table 5-9 is only 12 on Monday and 12 on Thursday, so those two days are infeasible as stated. To make the model solvable, should I treat the Monday and Thursday maximum-hour entries in Table 5-9 as adjustable (i.e., the students can actually work more than the listed maximum on those two days, so I should drop the upper bound for Monday and Thursday and keep the weekly minimums and the other days' caps), or should I keep every cap in Table 5-9 exactly as given and instead add extra student capacity (for example, allow hiring additional students or overtime beyond the table) to close the 2-hour gap on Monday and Thursday?

## Turn 2 - User Simulator

The maximum-hour entries in Table 5-9 are fixed and cannot be adjusted. The model must keep every cap in Table 5-9 exactly as given. To close the 2-hour gap on Monday and Thursday, additional student capacity should be added (for example, by allowing hiring of additional students or overtime beyond the table).

## Turn 3 - Generic Agent

QUESTION: To close the 2-hour gap on Monday and Thursday, should I model the extra capacity as a single generic "additional worker" resource with a fixed hourly wage (which you would specify) that can be scheduled up to 14 hours on any day, or should I instead allow the existing six students to work overtime beyond their Table 5-9 caps on Monday and Thursday only (with the same wage as their listed rate), and if so, what is the maximum overtime hours allowed per student per day?

## Turn 3 - User Simulator

The extra capacity should be modeled as a single generic "additional worker" resource with a fixed hourly wage that can be scheduled up to 14 hours on any day. The specific hourly wage for this additional worker still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Since the additional worker's hourly wage is still pending internal confirmation, should I build the model with the additional worker's wage as a named parameter (e.g., w_add) that you can plug in later, or would you prefer I use a placeholder value now (for example, 10.0 CNY/h) so the model is fully runnable, with the understanding that you will substitute the confirmed wage before final use?

## Turn 4 - User Simulator

Please build the model with the additional worker's wage as a named parameter (e.g., w_add) that can be plugged in later.

## Turn 5 - Generic Agent

QUESTION: What should the model optimize — should it minimize the total weekly labor cost (sum of each student's hours times their wage, plus the additional worker's hours times w_add), subject to all the coverage, minimum-hour, and maximum-hour constraints?

## Turn 5 - User Simulator

Yes, the model should minimize the total weekly labor cost, which is the sum of each student's hours times their wage, plus the additional worker's hours times w_add, subject to all the coverage, minimum-hour, and maximum-hour constraints.

## Turn 6 - Generic Agent

QUESTION: For the six named students, should the weekly minimum-hour requirement (at least 8 hours for undergraduates, at least 7 hours for graduates) be a hard constraint that must be satisfied, or should it be a soft target that can be relaxed if needed (for example, by paying a penalty for each hour below the minimum)?

## Turn 6 - User Simulator

The weekly minimum-hour requirement should be a hard constraint that must be satisfied.

## Turn 7 - Generic Agent

QUESTION: Which of the six students are undergraduates (minimum 8 hours/week) and which are graduates (minimum 7 hours/week)?

## Turn 7 - User Simulator

The specific classification of which students are undergraduates and which are graduates still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Since the undergraduate/graduate classification is still pending, should I model each student's weekly minimum as a named parameter (e.g., min_hours[i], set to 8 for undergraduates and 7 for graduates) that you can assign per student later, rather than hard-coding a specific split now?

## Turn 8 - User Simulator

Yes, please model each student's weekly minimum as a named parameter (e.g., min_hours[i]) that can be assigned per student later.

## Turn 9 - Generic Agent

QUESTION: For the additional worker, is there any minimum number of hours they must work per week, or can they be scheduled for zero hours if the six named students can cover all 14 hours on a given day?

## Turn 9 - User Simulator

The additional worker can be scheduled for zero hours if the six named students can cover all 14 hours on a given day.

## Turn 10 - Generic Agent

QUESTION: Can a single student work multiple separate blocks within the same day (for example, 3 hours in the morning and 3 hours in the evening), or must each student's hours on a given day form one continuous block?

## Turn 10 - User Simulator

The available business facts do not determine whether a student's hours on a given day must form one continuous block or can be split into multiple separate blocks. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Since the continuity requirement is still pending, should I model each student's daily hours as a single continuous block (which would require additional scheduling logic to enforce), or should I treat daily hours as a simple total that can be split across the day freely (i.e., only the total hours per student per day matters, not their placement within the 14-hour window)?

## Turn 11 - User Simulator

Please treat daily hours as a simple total that can be split across the day freely, so only the total hours per student per day matters, not their placement within the 14-hour window.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on how many hours the additional worker can work per week in total, or is the only limit the 14 hours per day cap you already specified?

## Turn 12 - User Simulator

The only limit on the additional worker is the 14 hours per day cap.

## Turn 13 - Generic Agent

QUESTION: Are there any other constraints or preferences I should include in the model — for example, a maximum number of days per week any student can work, a preference to minimize the number of students used, or a cap on total weekly labor cost?

## Turn 13 - User Simulator

Yes, there are two additional constraints:

1. Each student can work no more than 2 shifts per week.
2. No more than 3 students can be scheduled for duty each day.

## Turn 14 - Generic Agent

QUESTION: When you say each student can work no more than 2 shifts per week, does "shift" mean a day on which the student works at least one hour (i.e., a student can work on at most 2 of the 5 days), or does it mean something else such as a fixed-length block of hours?

## Turn 14 - User Simulator

A "shift" means a day on which the student works at least one hour. So each student can work on at most 2 of the 5 days.

## Turn 15 - Generic Agent

QUESTION: For the constraint that no more than 3 students can be scheduled for duty each day, does this count include the additional worker (so at most 3 total workers including the additional worker per day), or does it apply only to the six named students (so up to 3 named students plus the additional worker per day)?

## Turn 15 - User Simulator

The constraint applies only to the six named students. So up to 3 named students can be scheduled for duty each day, plus the additional worker.

## Turn 16 - Generic Agent

QUESTION: Is there any constraint on the additional worker's number of days per week, or can the additional worker work on all 5 days if needed?

## Turn 16 - User Simulator

The additional worker can work on all 5 days if needed.

## Turn 17 - Generic Agent

QUESTION: Are there any other constraints, preferences, or business rules I should include in the model that we have not yet discussed?

## Turn 17 - User Simulator

No, there are no other constraints, preferences, or business rules to include.

## Turn 18 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Setting:** A university computer lab is open 8:00 AM to 10:00 PM (14 hours) every day Monday through Friday. Exactly one worker must be on duty at all times, so 14 person-hours of coverage are required each day.

- **Workers:** Six named students (IDs 1–6) with hourly wages and per-day maximum hours as given in Table 5-9, plus one generic "additional worker" with a named wage parameter `w_add` (to be plugged in later).

- **Decision variables:** For each named student *i* and each day *d*, the number of hours *x[i,d]* that student works (a non-negative continuous quantity, splittable freely within the day). For the additional worker and each day *d*, the number of hours *a[d]* worked.

- **Objective:** Minimize total weekly labor cost = Σᵢ Σ_d wage[i]·x[i,d] + Σ_d w_add·a[d].

- **Constraints:**
  1. **Daily coverage:** For each day *d*, Σᵢ x[i,d] + a[d] = 14.
  2. **Daily maximum hours (named students):** x[i,d] ≤ cap[i,d] for every (i,d) in Table 5-9 (fixed, not adjustable).
  3. **Weekly minimum hours (named students):** Σ_d x[i,d] ≥ min_hours[i] for each student *i*, where min_hours[i] is a named parameter (8 for undergraduates, 7 for graduates; assignment pending).
  4. **Maximum days per week (named students):** Each student works on at most 2 of the 5 days (a binary indicator y[i,d] = 1 if x[i,d] > 0; Σ_d y[i,d] ≤ 2; x[i,d] ≤ cap[i,d]·y[i,d]).
  5. **Maximum named students per day:** For each day *d*, at most 3 of the six named students are scheduled (Σᵢ y[i,d] ≤ 3).
  6. **Additional worker daily cap:** a[d] ≤ 14 for each day *d*; no weekly cap; no minimum; can work on all 5 days.
  7. **Non-negativity:** x[i,d] ≥ 0, a[d] ≥ 0.

- **Parameters pending internal confirmation (named in the model):**
  - `w_add`: hourly wage of the additional worker.
  - `min_hours[i]`: weekly minimum for each student (8 or 7, depending on undergraduate/graduate classification).

- **No other constraints or preferences.**