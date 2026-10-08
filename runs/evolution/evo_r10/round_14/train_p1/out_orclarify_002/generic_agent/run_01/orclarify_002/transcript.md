## Turn 1 - Generic Agent

QUESTION: What is the exact rule for how many fighter jets each year must be allocated exclusively for pilot training — is it a fixed number, a fraction of that year's production, or some other formula?

## Turn 1 - User Simulator

The rule is not a fixed number, a fraction of that year’s production, or a specific formula. The requirement is simply that some fighter jets each year must be allocated exclusively for pilot training. The exact number to be allocated each year is not predetermined; it is part of what needs to be determined to maximize the total number of trained pilots by the end of year 2.

## Turn 2 - Generic Agent

QUESTION: How many trained pilots does one fighter jet produce per year when it is allocated to pilot training?

## Turn 2 - User Simulator

Each training jet can train 5 pilots per year.

## Turn 3 - Generic Agent

QUESTION: Do the training jets allocated in year 1 remain available for training in year 2 as well, or does each year's training allocation consist only of that year's newly produced jets?

## Turn 3 - User Simulator

The training jets allocated in year 1 remain available for training in year 2 as well.

## Turn 4 - Generic Agent

QUESTION: Are there any limits on how many of the newly produced jets in each year can be allocated to training — for example, must at least some jets be kept for other purposes (combat, reserves), or can all of a year's production be sent to training?

## Turn 4 - User Simulator

There are no limits on how many of the newly produced jets in each year can be allocated to training. All of a year's production can be sent to training.

## Turn 5 - Generic Agent

QUESTION: When a training jet trains pilots, does it train 5 pilots in each year it is in service (so a jet allocated in year 1 trains 5 in year 1 and another 5 in year 2, for 10 total), or does it train 5 pilots only in the year it is first allocated?

## Turn 5 - User Simulator

A training jet trains 5 pilots in each year it is in service. So a jet allocated in year 1 trains 5 pilots in year 1 and another 5 pilots in year 2, for 10 total.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 2 years (year 1 and year 2).
- **Production:** a1 = 10 jets in year 1, a2 = 15 jets in year 2.
- **Decision:** How many of each year's newly produced jets to allocate to pilot training (x1 in year 1, x2 in year 2).
- **Training capacity:** Each training jet trains 5 pilots per year it is in service.
- **Persistence:** Jets allocated to training in year 1 remain in training in year 2 as well (cumulative fleet).
- **No other constraints:** All of a year's production may be allocated to training; no minimum must be reserved for other purposes.
- **Objective:** Maximize the total number of trained pilots available by the end of year 2.

The total trained pilots by end of year 2 = 5·x1 (year 1) + 5·(x1 + x2) (year 2) = 10·x1 + 5·x2, subject to 0 ≤ x1 ≤ 10 and 0 ≤ x2 ≤ 15.