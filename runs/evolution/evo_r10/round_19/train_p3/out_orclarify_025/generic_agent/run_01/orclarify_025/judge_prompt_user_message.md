# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U2, U3, U4
I need help creating an investment plan over a three-year horizon. There are two investment options to consider, and the second investment must be held for a period that is a multiple of two years. Additionally, the total amount invested initially cannot exceed the available capital of 100,000 yuan.

Available initial capital: 100,000 yuan.

First investment option: guarantees a return of 0.7 yuan for every 1 yuan invested after one year.

Second investment option: guarantees a return of 2 yuan for every 1 yuan invested after two years.

## Problem units
- U1 (context): I need help creating an investment plan over a three-year horizon. There are two investment options to consider.
- U2 (data): Available initial capital: 100,000 yuan.
- U3 (data): First investment option: guarantees a return of 0.7 yuan for every 1 yuan invested after one year.
- U4 (data): Second investment option: guarantees a return of 2 yuan for every 1 yuan invested after two years.
- U5 (constraint): The second investment must be held for a period that is a multiple of two years.
- U6 (objective): Maximize the investor's earnings by the end of the third year.
- U7 (constraint): Total amount invested initially cannot exceed the available capital of 100,000 yuan.

## Hidden slot scoring rules
## H1: earnings_definition
- Severity: P2
- Severity reason: Without explicit definition of 'earnings', the agent can still formulate a coherent optimization model because maximizing final wealth or net profit yields identical optimal decisions. Clarification is helpful but not critical.
- Problem unit ID: U6
- Semantic hit rule: The Agent's question must explicitly ask for the definition or calculation basis of 'earnings' (e.g., asking whether it means final wealth, total return, net profit, or specifying what the objective function should measure).
- Reference acceptable questions:
  - What exactly does 'earnings' refer to: total final wealth or net profit after subtracting the initial investment?
  - Should we maximize the total amount of money at the end of year 3, or the profit (final amount minus the initial 100,000 yuan)?
- Failure modes:
  - Silently assuming earnings means total final wealth without confirming
  - Assuming earnings means net profit and subtracting initial capital without checking


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: For the first investment, when you say it "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean the investor receives 1.7 yuan total (principal 1.0 plus 0.7 profit) after one year, or only 0.7 yuan total (i.e., a loss of principal)?

## Turn 1 - User Simulator

The investor receives 1.7 yuan total (principal 1.0 plus 0.7 profit) after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, when you say it "guarantees a return of 2 yuan for every 1 yuan invested after two years," do you mean the investor receives 3 yuan total (principal 1.0 plus 2.0 profit) after two years, or only 2 yuan total?

## Turn 2 - User Simulator

The investor receives 3 yuan total (principal 1.0 plus 2.0 profit) after two years.

## Turn 3 - Generic Agent

QUESTION: At the end of the three-year horizon, is the goal to maximize the total amount of money available (principal plus all profits), or to maximize only the total profit earned over the three years?

## Turn 3 - User Simulator

The goal is to maximize the total amount of money available (principal plus all profits) at the end of the third year.

## Turn 4 - Generic Agent

QUESTION: When the first investment matures after one year, can the full 1.7 yuan per yuan invested be reinvested into either investment option in the following year, or is only the 0.7 yuan profit portion available for reinvestment?

## Turn 4 - User Simulator

The full 1.7 yuan per yuan invested can be reinvested into either investment option in the following year.

## Turn 5 - Generic Agent

QUESTION: When the second investment matures after two years, can the full 3 yuan per yuan invested be reinvested into either investment option in the following year, or is only the 2 yuan profit portion available for reinvestment?

## Turn 5 - User Simulator

The full 3 yuan per yuan invested can be reinvested into either investment option in the following year.

## Turn 6 - Generic Agent

QUESTION: You mentioned the second investment "must be held for a period that is a multiple of two years." Does this mean the second investment can only be started at the beginning of year 1 or the beginning of year 3 (so it matures at the end of year 2 or end of year 4), or can it also be started at the beginning of year 2 (maturing at the end of year 4, after the horizon)?

## Turn 6 - User Simulator

The second investment can only be started at the beginning of year 1 or the beginning of year 3.

## Turn 7 - Generic Agent

QUESTION: If the second investment is started at the beginning of year 3, it would mature at the end of year 5, which is after the three-year horizon. Should this investment be allowed in the plan, with its value counted at the end of year 3 (e.g., as principal only, or at some other valuation), or should the second investment only be allowed if it fully matures within the three-year horizon (i.e., only at the beginning of year 1)?

## Turn 7 - User Simulator

The second investment should only be allowed if it fully matures within the three-year horizon (i.e., only at the beginning of year 1).

## Turn 8 - Generic Agent

QUESTION: Can the first investment be started at the beginning of each of the three years (year 1, year 2, and year 3), with the year-3 investment maturing at the end of year 3 and counted in the final amount?

## Turn 8 - User Simulator

Yes, the first investment can be started at the beginning of each of the three years (year 1, year 2, and year 3), with the year-3 investment maturing at the end of year 3 and counted in the final amount.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how much can be invested in each option in a given year (other than the available funds), or can any amount up to the available funds be invested in each option?

## Turn 9 - User Simulator

There is no limit on how much can be invested in each option in a given year, other than the available funds.

## Turn 10 - Generic Agent

QUESTION: If there is leftover cash at the end of the three-year horizon that was not invested, is it simply added to the final total amount, or is it penalized or excluded from the objective?

## Turn 10 - User Simulator

Leftover cash at the end of the three-year horizon is simply added to the final total amount.

## Turn 11 - Generic Agent

QUESTION: Are the investment amounts required to be whole numbers (integer yuan), or can they be any continuous (fractional) amount?

## Turn 11 - User Simulator

The investment amounts can be any continuous (fractional) amount.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 3 years, with decisions made at the beginning of each year (year 1, year 2, year 3).
- **Initial capital:** 100,000 yuan available at the beginning of year 1.
- **Investment Option 1:** Can be started at the beginning of any year (1, 2, or 3). For every 1 yuan invested, the investor receives 1.7 yuan total at the end of that year (1.0 principal + 0.7 profit). The full 1.7 yuan can be reinvested in subsequent years.
- **Investment Option 2:** Can only be started at the beginning of year 1 (so it matures at the end of year 2, within the horizon). For every 1 yuan invested, the investor receives 3 yuan total at the end of year 2 (1.0 principal + 2.0 profit). The full 3 yuan can be reinvested in year 3.
- **Reinvestment:** Full matured amounts (principal + profit) from either option can be reinvested into either available option in the following year.
- **Objective:** Maximize the total amount of money available (principal + profits + any leftover cash) at the end of year 3.
- **Constraints:**
  - Total invested at the beginning of year 1 ≤ 100,000 yuan.
  - In each subsequent year, total invested ≤ available funds (from matured investments and any leftover cash carried forward).
  - No per-option limits beyond available funds.
  - Investment amounts are continuous (fractional yuan allowed).
  - Leftover cash at the end of year 3 is added to the final total.