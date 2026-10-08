## Turn 1 - Generic Agent

QUESTION: How many trained pilots does each fighter jet produce per year when it is allocated to pilot training?

## Turn 1 - User Simulator

Each fighter jet allocated to pilot training produces 5 trained pilots per year.

## Turn 2 - Generic Agent

QUESTION: How many fighter jets must be allocated to pilot training each year?

## Turn 2 - User Simulator

The number of fighter jets that must be allocated to pilot training each year still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Do the fighter jets allocated to pilot training in a given year come from that year's production, or can jets produced in earlier years be carried over and used for training?

## Turn 3 - User Simulator

The fighter jets allocated to pilot training in a given year come from that year's production.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how many of the jets produced in a given year can be allocated to pilot training, or can all of that year's production be used for training?

## Turn 4 - User Simulator

There is no limit on how many of the jets produced in a given year can be allocated to pilot training; all of that year's production can be used for training.

## Turn 5 - Generic Agent

QUESTION: Are the jets allocated to pilot training in a given year dedicated to training for that entire year, or can a jet be used for training in one year and then for other purposes in a later year?

## Turn 5 - User Simulator

The jets allocated to pilot training in a given year are dedicated to training for that entire year.

## Turn 6 - Generic Agent

QUESTION: Do the jets allocated to pilot training in year 1 remain available for training in year 2, or are they consumed/retired after year 1?

## Turn 6 - User Simulator

The jets allocated to pilot training in year 1 remain available for training in year 2.

## Turn 7 - Generic Agent

QUESTION: When you say the jets allocated to pilot training in year 1 remain available for training in year 2, does that mean they automatically continue producing 5 pilots in year 2 as well, or does a separate decision need to be made to keep them in training for year 2?

## Turn 7 - User Simulator

A separate decision needs to be made to keep them in training for year 2.

## Turn 8 - Generic Agent

QUESTION: In year 2, can the jets that were allocated to training in year 1 be re-allocated to non-training purposes, or must they remain in training for the full two years?

## Turn 8 - User Simulator

The jets that were allocated to training in year 1 can be re-allocated to non-training purposes in year 2.

## Turn 9 - Generic Agent

QUESTION: Is the goal to maximize the total number of trained pilots by the end of year 2, or is there a fixed requirement for how many jets must be allocated to training each year?

## Turn 9 - User Simulator

The goal is to maximize the total number of trained pilots by the end of year 2.

## Turn 10 - Generic Agent

QUESTION: Are there any other uses or constraints on the fighter jets besides pilot training, such as a minimum number that must be kept for operational deployment each year?

## Turn 10 - User Simulator

There are no other uses or constraints on the fighter jets besides pilot training; there is no minimum number that must be kept for operational deployment each year.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize the total number of trained pilots available by the end of year 2.
- **Production:** Year 1 produces a1 = 10 fighter jets; Year 2 produces a2 = 15 fighter jets.
- **Training capacity:** Each fighter jet allocated to pilot training in a given year produces 5 trained pilots that year.
- **Source of training jets:** Jets allocated to training in a given year come from that year's production.
- **No upper limit:** All of a year's production can be allocated to training.
- **Dedication:** A jet allocated to training in a given year is dedicated to training for that entire year.
- **Carry-over:** Jets allocated to training in year 1 remain available (not consumed) and can be allocated to training again in year 2, but this requires a separate decision.
- **Re-allocation:** Jets allocated to training in year 1 can be re-allocated to non-training purposes in year 2.
- **No other constraints:** There are no other uses, minimum deployment requirements, or limits on the jets besides pilot training.
- **Horizon:** 2 years.
- **Decision variables:** For each year, the number of jets allocated to pilot training (from that year's production, plus carry-over from prior years where applicable).
- **Output:** The maximum total number of trained pilots by the end of year 2.