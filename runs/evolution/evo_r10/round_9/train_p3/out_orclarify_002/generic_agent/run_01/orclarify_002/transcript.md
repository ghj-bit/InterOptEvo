## Turn 1 - Generic Agent

QUESTION: What is the exact rule for how many trained pilots a single fighter jet produces when it is allocated to training in a given year (for example, a fixed number of pilots per jet per year, or a rate that depends on something else)?

## Turn 1 - User Simulator

Each training jet can train 5 pilots per year.

## Turn 2 - Generic Agent

QUESTION: When a jet is allocated to training in a year, does it train 5 pilots in that same year only, or does it continue training pilots in subsequent years as well (i.e., is the allocation a per-year flow or a standing assignment)?

## Turn 2 - User Simulator

The allocation is a per-year flow. A jet allocated to training in a given year trains 5 pilots in that same year only.

## Turn 3 - Generic Agent

QUESTION: Are the jets produced in a given year available to be allocated to training in that same year, or do they only become available starting the following year?

## Turn 3 - User Simulator

The jets produced in a given year are available to be allocated to training in that same year.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a year can be allocated to training (for example, a maximum fraction or number), or can all jets produced in a year be allocated to training if that is optimal?

## Turn 4 - User Simulator

There is no stated limit on how many of the jets produced in a year can be allocated to training. All jets produced in a year can be allocated to training if that is optimal.

## Turn 5 - Generic Agent

QUESTION: Is there any requirement that some jets must be kept for other purposes (e.g., operational/combat use), or is the only goal to maximize the total number of trained pilots by the end of year 2 with no other constraints?

## Turn 5 - User Simulator

The only goal is to maximize the total number of trained pilots by the end of year 2. There is no requirement that some jets must be kept for other purposes.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Production:** 10 jets produced in year 1 (a1 = 10), 15 jets produced in year 2 (a2 = 15).
- **Availability:** Jets produced in a given year are available for allocation in that same year.
- **Training rule:** Each jet allocated to training in a given year trains exactly 5 pilots in that same year only (per-year flow, no carryover effect).
- **Allocation variable:** For each year, a non-negative integer (or continuous, since 5×integer is linear) number of jets allocated to training, bounded above by that year's production.
- **No other constraints:** No minimum operational reserve, no cap on training allocation, no other uses for jets.
- **Horizon:** 2 years.

The model is straightforward: allocate all 10 jets in year 1 and all 15 jets in year 2 to training, yielding 10×5 + 15×5 = 50 + 75 = **125 trained pilots** by the end of year 2.