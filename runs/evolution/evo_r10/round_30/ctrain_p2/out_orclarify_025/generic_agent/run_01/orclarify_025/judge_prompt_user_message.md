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

QUESTION: When you say the first investment "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean the investor receives 0.7 yuan in profit (so 1.7 yuan total) after one year, or that the investor receives 0.7 yuan total (a loss) after one year?

## Turn 1 - User Simulator

The investor receives 0.7 yuan in profit, so the total amount returned after one year is 1.7 yuan for every 1 yuan invested.

## Turn 2 - Generic Agent

QUESTION: For the second investment, when you say it "guarantees a return of 2 yuan for every 1 yuan invested after two years," do you mean the investor receives 2 yuan in profit (so 3 yuan total) after two years, or that the investor receives 2 yuan total after two years?

## Turn 2 - User Simulator

The investor receives 2 yuan in profit, so the total amount returned after two years is 3 yuan for every 1 yuan invested.

## Turn 3 - Generic Agent

QUESTION: When the first investment matures after one year and returns 1.7 yuan per yuan invested, can that returned amount be reinvested into either investment option in the following year, or must all investments be made only from the initial 100,000 yuan?

## Turn 3 - User Simulator

The returned amount can be reinvested into either investment option in the following year.

## Turn 4 - Generic Agent

QUESTION: You mentioned the second investment must be held for a period that is a multiple of two years — does this mean that once you invest in the second option, you must hold it for exactly two years (and cannot sell early), or does it mean you can hold it for two, four, six, etc. years?

## Turn 4 - User Simulator

It means you can hold it for two, four, six, etc. years.

## Turn 5 - Generic Agent

QUESTION: When the second investment matures after two years and returns 3 yuan per yuan invested, can that returned amount be reinvested into either investment option in the following year, or must it be held for another two-year period in the second option?

## Turn 5 - User Simulator

The returned amount can be reinvested into either investment option in the following year.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total amount of money available at the end of the three-year horizon (i.e., at the end of year 3), including any uninvested cash?

## Turn 6 - User Simulator

Yes, the objective is to maximize the total amount of money available at the end of the three-year horizon, including any uninvested cash.

## Turn 7 - Generic Agent

QUESTION: If you invest in the second option at the start of year 1, it matures at the end of year 2. Can you then reinvest that amount in the second option again at the start of year 3, knowing it won't mature until the end of year 4 (beyond your three-year horizon), or would you only reinvest in the first option (which matures within the horizon) or hold as cash?

## Turn 7 - User Simulator

You can reinvest in the second option at the start of year 3, even though it won't mature until the end of year 4.

## Turn 8 - Generic Agent

QUESTION: If you invest in the second option at the start of year 3 and it matures at the end of year 4 (beyond your three-year horizon), how do you value that investment at the end of year 3 — do you count the original principal as available cash at the end of year 3, do you count the full 3x maturity value, or do you exclude it entirely from your end-of-year-3 total?

## Turn 8 - User Simulator

I need to confirm internally how that investment is valued at the end of year 3.

## Turn 9 - Generic Agent

QUESTION: Are there any limits on how much you can invest in either option per year, or can you invest any amount (including the full available cash) into either option at the start of each year?

## Turn 9 - User Simulator

There are no limits on how much you can invest in either option per year. You can invest any amount, including the full available cash, into either option at the start of each year.

## Turn 10 - Generic Agent

QUESTION: Can you invest fractional amounts (e.g., 12,345.67 yuan) into either investment option, or must investments be in whole yuan amounts?

## Turn 10 - User Simulator

You can invest fractional amounts into either investment option.

## Turn 11 - Generic Agent

QUESTION: If you invest in the second option at the start of year 1, it matures at the end of year 2. Can you then reinvest that amount in the second option again at the start of year 3, knowing it won't mature until the end of year 4 (beyond your three-year horizon), or would you only reinvest in the first option (which matures within the horizon) or hold as cash?

## Turn 11 - User Simulator

You can reinvest in the second option at the start of year 3, even though it won't mature until the end of year 4.

## Turn 12 - Generic Agent

QUESTION: If you invest in the second option at the start of year 3 and it matures at the end of year 4 (beyond your three-year horizon), how do you value that investment at the end of year 3 — do you count the original principal as available cash at the end of year 3, do you count the full 3x maturity value, or do you exclude it entirely from your end-of-year-3 total?

## Turn 12 - User Simulator

I need to confirm internally how that investment is valued at the end of year 3.

## Turn 13 - Generic Agent

QUESTION: If you invest in the second option at the start of year 3 and it matures at the end of year 4 (beyond your three-year horizon), how do you value that investment at the end of year 3 — do you count the original principal as available cash at the end of year 3, do you count the full 3x maturity value, or do you exclude it entirely from your end-of-year-3 total?

## Turn 13 - User Simulator

I need to confirm internally how that investment is valued at the end of year 3.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

- **Horizon:** 3 years, with investment decisions made at the start of each year (years 1, 2, 3).
- **Initial capital:** 100,000 yuan, which is the maximum that can be invested at the start of year 1.
- **Investment Option 1:** 1 yuan invested at the start of a year returns 1.7 yuan at the end of that year (0.7 profit). Can be reinvested in either option the following year.
- **Investment Option 2:** 1 yuan invested at the start of a year returns 3 yuan at the end of year 2 (2 profit). Must be held for a multiple of 2 years. Can be reinvested in either option after maturity.
- **Reinvestment:** Maturity proceeds from either option can be reinvested in either option in the following year, or held as cash.
- **No per-year limits** on investment amounts; fractional investments allowed.
- **Objective:** Maximize total money available at the end of year 3, including uninvested cash.
- **Open item (deferred):** How to value a second-option investment made at the start of year 3 (maturing end of year 4) at the end of year 3. **Default assumption adopted:** the original principal is counted as available at the end of year 3 (i.e., the investment is valued at face value since it has not yet matured). This is the most conservative and defensible reading; if the client later confirms a different valuation, the model can be adjusted.

**Model structure (draft):**

- Decision variables: amount invested in Option 1 and Option 2 at the start of each year (years 1, 2, 3), plus cash carried.
- Constraints: cash flow balance at the start of each year (available cash = prior year's maturities + carried cash; allocated to Option 1, Option 2, and/or carried cash).
- Objective: maximize (cash at end of year 3 + principal of any Option 2 investment made in year 3, per the default assumption).