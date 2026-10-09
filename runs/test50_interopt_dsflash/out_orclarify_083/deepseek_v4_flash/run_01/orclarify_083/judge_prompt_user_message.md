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


# Atomic Question Map

Q1 (turn 1): What shift lengths and start times are allowed for waiters (for example, fixed 8-hour shifts starting at specific times, or flexible start times)?
Q2 (turn 2): Does each waiter work exactly one 8-hour shift per day?
Q3 (turn 2): Should the objective count the number of waiters hired rather than the number of shifts scheduled?
Q4 (turn 3): Should waiter start times and coverage be modeled in continuous time or in discrete time intervals (for example, hourly), and if discrete, what interval length should be used?
Q5 (turn 4): If the exact time granularity is not yet confirmed, should we proceed with a standard discrete hourly model as a working assumption until the internal decision is finalized?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What shift lengths and start times are allowed for waiters (for example, fixed 8-hour shifts starting at specific times, or flexible start times)?

## Turn 1 - User Simulator

Each waiter works a single continuous 8-hour shift per day. The start times are flexible—they can begin at any time, not just at fixed clock times.

## Turn 2 - Generic Agent

QUESTION: Does each waiter work exactly one 8-hour shift per day, and should the objective count the number of waiters hired rather than the number of shifts scheduled?

## Turn 2 - User Simulator

Yes, each waiter works exactly one continuous 8-hour shift per day. The objective is to minimize the total number of waiters employed.

## Turn 3 - Generic Agent

QUESTION: Should waiter start times and coverage be modeled in continuous time or in discrete time intervals (for example, hourly), and if discrete, what interval length should be used?

## Turn 3 - User Simulator

That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: If the exact time granularity is not yet confirmed, should we proceed with a standard discrete hourly model as a working assumption until the internal decision is finalized?

## Turn 4 - User Simulator

Yes, please proceed with a standard discrete hourly model as a working assumption until the internal decision is finalized.

## Turn 5 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.820

Confidence rationale: The core formulation is now specified: 24-hour coverage, minimum staffing per interval from Table 1.1, each waiter works exactly one continuous 8-hour shift, and the objective is to minimize the total number of waiters employed. The user has approved a standard discrete hourly model as a working assumption, which resolves the remaining granularity ambiguity sufficiently to formulate. The only residual uncertainty is that the hourly granularity is provisional and may later be replaced by continuous start times, which could change the optimal objective value but not the model structure.

Summary: Model a 24-hour waiter scheduling problem with discrete hourly intervals. Decision variables represent the number of waiters starting an 8-hour shift at each hourly start time. The objective minimizes the total number of waiters employed (equivalently, total shifts, since each waiter works exactly one shift per day). Coverage constraints require that for every hour of the day, the number of waiters on duty from overlapping 8-hour shifts meets or exceeds the minimum shown in Table 1.1: 4 for 02:00-06:00, 8 for 06:00-10:00, 10 for 10:00-14:00, 7 for 14:00-18:00, 12 for 18:00-22:00, and 4 for 22:00-02:00. Shifts may cross midnight and the schedule is cyclic over the 24-hour day. Start-time granularity is provisionally hourly, pending internal confirmation.