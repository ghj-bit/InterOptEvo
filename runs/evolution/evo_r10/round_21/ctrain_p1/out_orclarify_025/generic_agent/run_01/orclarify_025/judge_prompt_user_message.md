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

QUESTION: For the first investment, when you say it guarantees 0.7 yuan for every 1 yuan invested after one year, do you mean the investor receives 1.7 yuan total (principal plus 0.7 profit) at the end of each year, or only 0.7 yuan total (losing the principal)?

## Turn 1 - User Simulator

The investor receives 1.7 yuan total (principal plus 0.7 profit) at the end of each year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, when you say it guarantees 2 yuan for every 1 yuan invested after two years, do you mean the investor receives 3 yuan total (principal plus 2 profit) at the end of each two-year holding period, or only 2 yuan total (losing the principal)?

## Turn 2 - User Simulator

The investor receives 3 yuan total (principal plus 2 profit) at the end of each two-year holding period.

## Turn 3 - Generic Agent

QUESTION: When the first investment matures at the end of a year, can the proceeds (principal plus profit) be reinvested into either investment option in the following year, or must only the original 100,000 yuan be invested and all proceeds simply accumulate as cash?

## Turn 3 - User Simulator

The proceeds can be reinvested into either investment option in the following year.

## Turn 4 - Generic Agent

QUESTION: At the end of the three-year horizon, is the goal to maximize the total amount of money available (cash plus the value of any investments still being held), or must all money be in cash by the end of year three?

## Turn 4 - User Simulator

The goal is to maximize the total amount of money available (cash plus the value of any investments still being held) at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: Since the second investment must be held for a multiple of two years, can it be started in year three (so it matures in year five, after the horizon ends), or can it only be started in year one (maturing at the end of year two)?

## Turn 5 - User Simulator

It can only be started in year one (maturing at the end of year two).

## Turn 6 - Generic Agent

QUESTION: If the second investment matures at the end of year two, can its proceeds be reinvested in the first investment for year three, or must they remain as cash at the end of the horizon?

## Turn 6 - User Simulator

The proceeds can be reinvested in the first investment for year three.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much can be invested in each option per year, or can any amount up to the available funds be invested in either option?

## Turn 7 - User Simulator

There is no limit on how much can be invested in each option per year, other than the available funds.

## Turn 8 - Generic Agent

QUESTION: At the end of year three, if the first investment started in year three has not yet matured (it matures at the end of year three), is its value counted as the full 1.7 times the amount invested, or is it counted at face value (1 times the amount invested)?

## Turn 8 - User Simulator

It is counted as the full 1.7 times the amount invested.

## Turn 9 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 3 years, with investment decisions made at the start of each year (years 1, 2, 3).
- **Initial capital:** 100,000 yuan, which is the maximum that can be invested initially.
- **Investment Option 1:** 1 yuan invested at the start of a year returns 1.7 yuan at the end of that year (0.7 profit). Can be started in any year (1, 2, or 3).
- **Investment Option 2:** 1 yuan invested at the start of a year returns 3 yuan at the end of the second year (2 profit). Must be held for a multiple of 2 years. Can only be started in year 1 (maturing at the end of year 2).
- **Reinvestment:** Proceeds from any maturing investment can be reinvested in either option in the following year.
- **Objective:** Maximize total wealth (cash plus value of investments) at the end of year 3.
- **Valuation at end of year 3:** The first investment started in year 3 is valued at 1.7 times the amount invested (it matures at the end of year 3).
- **No per-option limits** other than available funds.
- **Cash** can be held idle (no interest) if not invested.