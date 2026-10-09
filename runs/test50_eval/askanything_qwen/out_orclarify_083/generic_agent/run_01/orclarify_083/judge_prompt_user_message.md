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

QUESTION: How many consecutive hours does a single waiter work in one shift?

## Turn 1 - User Simulator

A single waiter works 8 consecutive hours in one shift.

## Turn 2 - Generic Agent

QUESTION: Can a waiter start a shift at any hour, or are there specific allowed start times?

## Turn 2 - User Simulator

A waiter can start a shift at any hour.

## Turn 3 - Generic Agent

QUESTION: Are waiters allowed to work multiple shifts per day, or is each waiter limited to exactly one 8-hour shift per day?

## Turn 3 - User Simulator

Each waiter is limited to exactly one 8-hour shift per day.

## Turn 4 - Generic Agent

QUESTION: Do you require the number of waiters starting at each hour to be a whole number, or can fractional values be used in the calculation?

## Turn 4 - User Simulator

The number of waiters starting at each hour must be a whole number.

## Turn 5 - Generic Agent

READY_TO_MODEL
I have confirmed the following details for the waiter scheduling problem:
1.  **Objective:** Minimize the total number of waiters employed.
2.  **Operating Hours:** The restaurant operates 24 hours a day.
3.  **Shift Length:** Each waiter works exactly 8 consecutive hours.
4.  **Shift Frequency:** Each waiter works exactly one shift per day.
5.  **Start Times:** Waiters can start a shift at any hour (0 through 23).
6.  **Constraints:** The number of waiters on duty during each 4-hour interval must be at least the minimum specified in Table 1.1:
    *   2:00–6:00: 4 waiters
    *   6:00–10:00: 8 waiters
    *   10:00–14:00: 10 waiters
    *   14:00–18:00: 7 waiters
    *   18:00–22:00: 12 waiters
    *   22:00–2:00: 4 waiters
7.  **Variable Type:** The number of waiters starting at each hour must be a non-negative integer.