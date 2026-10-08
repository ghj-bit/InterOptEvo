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

QUESTION: When you say the first investment "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean that 1 yuan invested at the start of a year becomes 1.7 yuan (principal plus 0.7) at the end of that year, or that it becomes 0.7 yuan total (i.e., you lose the principal)?

## Turn 1 - User Simulator

It becomes 1.7 yuan total (principal plus 0.7) at the end of that year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, does 1 yuan invested at the start of a year become 3 yuan total (principal plus 2) at the end of the two-year holding period, or does it become 2 yuan total?

## Turn 2 - User Simulator

It becomes 3 yuan total (principal plus 2) at the end of the two-year holding period.

## Turn 3 - Generic Agent

QUESTION: Can money that matures from an investment be reinvested in either option in later years, or is the initial 100,000 yuan the only money that can ever be invested?

## Turn 3 - User Simulator

Money that matures from an investment can be reinvested in either option in later years.

## Turn 4 - Generic Agent

QUESTION: You mentioned the second investment must be held for a period that is a multiple of two years — does this mean it can be held for 2 years, 4 years, 6 years, etc., or is it simply that it must be held for exactly 2 years (and can only be started in years where it will mature within the 3-year horizon)?

## Turn 4 - User Simulator

It must be held for exactly 2 years.

## Turn 5 - Generic Agent

QUESTION: What is the objective of this investment plan — is it to maximize the total wealth (principal plus returns) at the end of year 3, or is there some other goal such as maximizing returns only, or meeting a specific target amount?

## Turn 5 - User Simulator

The objective is to maximize the total amount of money the investor has at the end of the third year.

## Turn 6 - Generic Agent

QUESTION: Can the investor invest in the first option in year 3 (i.e., at the start of year 3, with the money maturing at the end of year 3), or is the first option only available in years 1 and 2?

## Turn 6 - User Simulator

The first option is available in year 3.

## Turn 7 - Generic Agent

QUESTION: Can the investor invest in the second option in year 2 (i.e., at the start of year 2, with the money maturing at the end of year 3), or is the second option only available in year 1?

## Turn 7 - User Simulator

The second option is available in year 2.

## Turn 8 - Generic Agent

QUESTION: Are there any minimum or maximum investment amounts for either option, or can any amount (including fractional yuan) be invested in each option in each year it is available?

## Turn 8 - User Simulator

There are no minimum or maximum investment amounts for either option. Any amount can be invested in each option in each year it is available.

## Turn 9 - Generic Agent

QUESTION: Is it allowed to leave some money uninvested (i.e., hold it as cash) at any point during the three years, or must all available money be invested in one of the two options each year?

## Turn 9 - User Simulator

It is allowed to leave some money uninvested (i.e., hold it as cash) at any point during the three years.

## Turn 10 - Generic Agent

QUESTION: If money is held as cash, does it earn any interest or return, or is it simply carried forward at face value (1 yuan in = 1 yuan out)?

## Turn 10 - User Simulator

It is simply carried forward at face value (1 yuan in = 1 yuan out).

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total wealth (cash + matured investments) at the end of year 3.

**Initial capital:** 100,000 yuan available at the start of year 1.

**Investment options:**
- **Option 1 (1-year):** Available at the start of years 1, 2, and 3. 1 yuan invested at the start of a year becomes 1.7 yuan at the end of that year.
- **Option 2 (2-year):** Available at the start of years 1 and 2. 1 yuan invested at the start of a year becomes 3 yuan at the end of the two-year holding period. (Not available in year 3 since it would not mature within the horizon.)

**Reinvestment:** Money that matures from either option can be reinvested in either option in subsequent years.

**Cash:** Uninvested money can be held as cash and carries forward at face value (no interest).

**Constraints:**
- Total amount invested at the start of year 1 cannot exceed 100,000 yuan.
- No minimum or maximum per-investment amounts; any non-negative amount can be invested.
- Investments are continuous (fractional yuan allowed).
- The second option must be held for exactly 2 years (no early withdrawal, no extension).

**Decision variables (per year, per option):** How much to allocate to Option 1, Option 2, and cash at the start of each year.

**Timing:** Investments are made at the start of each year; returns are received at the end of the holding period.