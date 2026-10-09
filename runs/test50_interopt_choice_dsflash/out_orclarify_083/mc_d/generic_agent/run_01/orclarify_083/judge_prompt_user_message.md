# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U5, U2
I need help scheduling waiters for a restaurant that operates 24 hours a day, aiming to minimize the total number of waiters employed, while ensuring that at each time interval, the number of waiters on duty is at least the minimum number of waiters needed as shown in Table 1.1.

Table 1.1

| Time        | Minimum Number of Waiters Needed | Time        | Minimum Number of Waiters Needed |
|:-----------:|:-------------------------------:|:-----------:|:-------------------------------:|
| $2 \sim 6$  | 4                                | $14 \sim 18$| 7                                |
| $6 \sim 10$ | 8                                | $18 \sim 22$| 12                               |
| $10 \sim 14$| 10                               | $22 \sim 2$ | 4                                |

## Problem units
- U1 (context): I need help scheduling waiters for a restaurant that operates 24 hours a day.
- U2 (data): Table 1.1

| Time        | Minimum Number of Waiters Needed | Time        | Minimum Number of Waiters Needed |
|:-----------:|:-------------------------------:|:-----------:|:-------------------------------:|
| $2 \sim 6$  | 4                                | $14 \sim 18$| 7                                |
| $6 \sim 10$ | 8                                | $18 \sim 22$| 12                               |
| $10 \sim 14$| 10                               | $22 \sim 2$ | 4                                |
- U3 (objective): Minimize the total number of waiters employed.
- U4 (constraint): Each waiter works continuously for 8 hours a day.
- U5 (constraint): At each time interval, the number of waiters on duty must be at least the minimum number of waiters needed as shown in Table 1.1.

## Hidden slot scoring rules
## H1: continuous_8hour_shift
- Severity: P0
- Severity reason: Without knowing that each waiter works exactly 8 continuous hours, it's impossible to define shift start times and coverage constraints; any model built without this assumption would be structurally invalid for the restaurant scheduling problem.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must explicitly ask about the length of a waiter's daily working hours and whether those hours are consecutive.
- Reference acceptable questions:
  - How many hours does each waiter work per day, and are these hours consecutive?
  - Do the waiters work in 8-hour continuous shifts?
- Failure modes:
  - Assuming waiters can work any number of hours as long as the minimum staffing is met
  - Assuming that shifts can be split into non-contiguous blocks (e.g., two 4-hour periods)
  - Assuming each waiter works for the entire 24-hour day


# Full Transcript

## Turn 1 - Generic Agent

```json
{
  "action": "ASK",
  "question": "What shift structure should the schedule use for waiters?",
  "options": [
    {
      "id": "A",
      "text": "Waiters work fixed-length shifts that start at the beginning of one of the listed time intervals."
    },
    {
      "id": "B",
      "text": "Waiters can be assigned to any consecutive block of time intervals, with no fixed shift length."
    },
    {
      "id": "C",
      "text": "Waiters work standard shifts such as 8 hours, but start times can be chosen freely."
    }
  ],
  "allow_other": true
}
```

Question:
What shift structure should the schedule use for waiters?

Options:
A. Waiters work fixed-length shifts that start at the beginning of one of the listed time intervals.
B. Waiters can be assigned to any consecutive block of time intervals, with no fixed shift length.
C. Waiters work standard shifts such as 8 hours, but start times can be chosen freely.
D. None of the above — I'd like to explain in my own words.

## Turn 1 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 2 - Generic Agent

```json
{
  "action": "ASK",
  "question": "How long is each waiter's fixed shift?",
  "options": [
    {
      "id": "A",
      "text": "Each shift lasts 4 hours, covering exactly one of the listed time intervals."
    },
    {
      "id": "B",
      "text": "Each shift lasts 8 hours, covering two consecutive listed time intervals."
    },
    {
      "id": "C",
      "text": "Each shift lasts 12 hours, covering three consecutive listed time intervals."
    }
  ],
  "allow_other": true
}
```

Question:
How long is each waiter's fixed shift?

Options:
A. Each shift lasts 4 hours, covering exactly one of the listed time intervals.
B. Each shift lasts 8 hours, covering two consecutive listed time intervals.
C. Each shift lasts 12 hours, covering three consecutive listed time intervals.
D. None of the above — I'd like to explain in my own words.

## Turn 2 - User Simulator

```json
{
  "choice": "B"
}
```

Business user selected option B.

## Turn 3 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Can a waiter be assigned to more than one shift in the schedule?",
  "options": [
    {
      "id": "A",
      "text": "Each waiter works exactly one shift."
    },
    {
      "id": "B",
      "text": "A waiter can work multiple shifts, and the total number of waiters employed counts each person once."
    },
    {
      "id": "C",
      "text": "A waiter can work multiple shifts, but each shift assignment counts as a separate employment."
    }
  ],
  "allow_other": true
}
```

Question:
Can a waiter be assigned to more than one shift in the schedule?

Options:
A. Each waiter works exactly one shift.
B. A waiter can work multiple shifts, and the total number of waiters employed counts each person once.
C. A waiter can work multiple shifts, but each shift assignment counts as a separate employment.
D. None of the above — I'd like to explain in my own words.

## Turn 3 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 4 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Which start times are allowed for the 8-hour shifts?",
  "options": [
    {
      "id": "A",
      "text": "Shifts can start at the beginning of any of the six listed time intervals, including 22:00."
    },
    {
      "id": "B",
      "text": "Shifts can start only at 6:00, 10:00, 14:00, and 18:00."
    },
    {
      "id": "C",
      "text": "Shifts can start only at 2:00, 6:00, 10:00, and 14:00."
    }
  ],
  "allow_other": true
}
```

Question:
Which start times are allowed for the 8-hour shifts?

Options:
A. Shifts can start at the beginning of any of the six listed time intervals, including 22:00.
B. Shifts can start only at 6:00, 10:00, 14:00, and 18:00.
C. Shifts can start only at 2:00, 6:00, 10:00, and 14:00.
D. None of the above — I'd like to explain in my own words.

## Turn 4 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 5 - Generic Agent

```json
{
  "action": "ASK",
  "question": "Are waiters interchangeable across all shifts, or do some have restrictions?",
  "options": [
    {
      "id": "A",
      "text": "All waiters are interchangeable and can be assigned to any shift."
    },
    {
      "id": "B",
      "text": "Some waiters have availability restrictions that limit which shifts they can work."
    },
    {
      "id": "C",
      "text": "Some waiters have skill or role restrictions that limit which shifts they can work."
    }
  ],
  "allow_other": true
}
```

Question:
Are waiters interchangeable across all shifts, or do some have restrictions?

Options:
A. All waiters are interchangeable and can be assigned to any shift.
B. Some waiters have availability restrictions that limit which shifts they can work.
C. Some waiters have skill or role restrictions that limit which shifts they can work.
D. None of the above — I'd like to explain in my own words.

## Turn 5 - User Simulator

```json
{
  "choice": "A"
}
```

Business user selected option A.

## Turn 6 - Generic Agent

```json
{
  "action": "READY_TO_MODEL",
  "summary": "The restaurant operates 24 hours a day, divided into six 4-hour intervals: 2-6, 6-10, 10-14, 14-18, 18-22, and 22-2. Each waiter works exactly one 8-hour shift, covering two consecutive intervals, and shifts may start at the beginning of any of the six intervals. All waiters are interchangeable. The goal is to minimize the total number of waiters employed while meeting the minimum staffing requirements in each interval: 4, 8, 10, 7, 12, and 4 respectively. No important unresolved business assumptions remain."
}
```

The restaurant operates 24 hours a day, divided into six 4-hour intervals: 2-6, 6-10, 10-14, 14-18, 18-22, and 22-2. Each waiter works exactly one 8-hour shift, covering two consecutive intervals, and shifts may start at the beginning of any of the six intervals. All waiters are interchangeable. The goal is to minimize the total number of waiters employed while meeting the minimum staffing requirements in each interval: 4, 8, 10, 7, 12, and 4 respectively. No important unresolved business assumptions remain.