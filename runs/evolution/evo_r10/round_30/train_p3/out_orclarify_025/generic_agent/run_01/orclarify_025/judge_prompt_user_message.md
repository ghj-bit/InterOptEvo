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

QUESTION: When you say the first investment "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean that 1 yuan invested at the start of a year becomes 1.7 yuan at the end of that year (i.e., 0.7 is the profit on top of the principal), or that it becomes 0.7 yuan total (i.e., you lose the principal)?

## Turn 1 - User Simulator

It means 1 yuan invested at the start of a year becomes 1.7 yuan at the end of that year. The 0.7 yuan is the profit on top of the principal.

## Turn 2 - Generic Agent

QUESTION: For the second investment, does "2 yuan for every 1 yuan invested after two years" mean that 1 yuan invested at the start of a two-year holding period becomes 3 yuan at the end (2 yuan profit on top of the 1 yuan principal), or that it becomes 2 yuan total?

## Turn 2 - User Simulator

It means 1 yuan invested at the start of a two-year holding period becomes 3 yuan at the end. The 2 yuan is the profit on top of the 1 yuan principal.

## Turn 3 - Generic Agent

QUESTION: Can money be reinvested in either option at the end of a holding period (for example, proceeds from the first investment at the end of year 1 reinvested in year 2, or proceeds from the second investment at the end of year 2 reinvested in year 3), or is the plan limited to a single initial allocation of the 100,000 yuan at the start of year 1?

## Turn 3 - User Simulator

Money can be reinvested in either option at the end of a holding period.

## Turn 4 - Generic Agent

QUESTION: What is the goal of the plan — to maximize the total amount of money available at the end of year 3, or to maximize total profit earned over the three years?

## Turn 4 - User Simulator

The goal is to maximize the total amount of money available at the end of year 3.

## Turn 5 - Generic Agent

QUESTION: The second investment must be held for a multiple of two years. Within the three-year horizon, does that mean it can only be held for exactly two years (so it can be started at the beginning of year 1 or the beginning of year 2), or could it be held for four years and simply extend beyond the horizon?

## Turn 5 - User Simulator

It can only be held for exactly two years within the three-year horizon.

## Turn 6 - Generic Agent

QUESTION: At the end of year 3, can money that is still locked in an investment (for example, money put into the first investment at the start of year 3 that matures at the end of year 3) be counted in the final total, or does only cash that is free and available at the end of year 3 count?

## Turn 6 - User Simulator

Money that matures at the end of year 3 can be counted in the final total.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much can be invested in either option in a given period (for example, a maximum amount per investment), or can any amount up to the available cash be invested in each option?

## Turn 7 - User Simulator

There is no limit on how much can be invested in either option in a given period, other than the available cash.

## Turn 8 - Generic Agent

QUESTION: Can money be left idle (not invested) in any period, or must all available cash be invested in one of the two options at the start of each year?

## Turn 8 - User Simulator

Money can be left idle (not invested) in any period.

## Turn 9 - Generic Agent

QUESTION: Can the second investment be started at the beginning of year 2 (so it matures at the end of year 3), or can it only be started at the beginning of year 1 (maturing at the end of year 2)?

## Turn 9 - User Simulator

The second investment can be started at the beginning of year 2, so it matures at the end of year 3.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 3 years, with decision points at the start of each year (years 1, 2, 3).
- **Initial capital:** 100,000 yuan available at the start of year 1.
- **Investment Option 1:** 1 yuan invested at the start of a year becomes 1.7 yuan at the end of that year (1-year holding period, 70% profit).
- **Investment Option 2:** 1 yuan invested at the start of a two-year holding period becomes 3 yuan at the end (2-year holding period, 200% profit). It can be started at the beginning of year 1 (matures end of year 2) or the beginning of year 2 (matures end of year 3). It cannot be started at the beginning of year 3 because it would not mature within the horizon.
- **Reinvestment:** Proceeds from any maturing investment can be reinvested in either option at the start of the next period, or left idle.
- **Idle cash:** Money can be left uninvested in any period; it carries over unchanged.
- **No per-period limits** other than available cash.
- **Objective:** Maximize the total amount of money available at the end of year 3 (including proceeds from investments that mature at the end of year 3).