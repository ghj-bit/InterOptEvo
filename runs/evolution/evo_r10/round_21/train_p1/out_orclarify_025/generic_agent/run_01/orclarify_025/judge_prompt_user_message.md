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

QUESTION: For the first investment, when you say it returns 0.7 yuan per 1 yuan after one year, do you mean the investor receives 0.7 yuan in profit (so 1.7 yuan total) after one year, or 0.7 yuan total (a loss of 0.3 yuan)?

## Turn 1 - User Simulator

It means the investor receives 0.7 yuan in profit, so 1.7 yuan total after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, when you say it returns 2 yuan per 1 yuan after two years, do you mean the investor receives 2 yuan in profit (so 3 yuan total) after two years, or 2 yuan total (a profit of 1 yuan)?

## Turn 2 - User Simulator

It means the investor receives 2 yuan in profit, so 3 yuan total after two years.

## Turn 3 - Generic Agent

QUESTION: The second investment must be held for a period that is a multiple of two years. Does this mean it can only be held for exactly two years, or can it also be held for four years (or longer multiples) if you choose?

## Turn 3 - User Simulator

It can be held for exactly two years or four years (or longer multiples), if chosen.

## Turn 4 - Generic Agent

QUESTION: Since the horizon is three years, a four-year holding of the second investment would extend beyond the horizon. How should that be handled — should the second investment only be allowed to be held for two years (so it matures within the horizon), or should four-year holdings be allowed with the value at year three treated somehow (e.g., marked to value or excluded)?

## Turn 4 - User Simulator

The second investment should only be allowed to be held for two years, so it matures within the three-year horizon.

## Turn 5 - Generic Agent

QUESTION: At the end of each year, can the proceeds from a maturing investment be reinvested into either option for the following year, or must all investment decisions be made only at the start (year 0) with no reinvestment during the horizon?

## Turn 5 - User Simulator

The proceeds from a maturing investment can be reinvested into either option for the following year.

## Turn 6 - Generic Agent

QUESTION: When reinvesting proceeds, can the money be split arbitrarily between the two options (e.g., invest 30,000 in option 1 and 20,000 in option 2), or must each year's available funds be allocated as a whole to a single option?

## Turn 6 - User Simulator

The money can be split arbitrarily between the two options.

## Turn 7 - Generic Agent

QUESTION: Is the goal to maximize the total wealth (principal plus profit) at the end of year three, or is there some other objective such as maximizing profit only or meeting a target amount?

## Turn 7 - User Simulator

The goal is to maximize the total wealth (principal plus profit) at the end of year three.

## Turn 8 - Generic Agent

QUESTION: At the end of year three, if there is money that is still locked in an investment that has not yet matured (for example, money put into the first investment in year three, which would mature in year four), how should that be treated — should it be excluded from the final wealth, or should only investments that have matured by the end of year three count toward the objective?

## Turn 8 - User Simulator

Only investments that have matured by the end of year three count toward the objective.

## Turn 9 - Generic Agent

QUESTION: If there is cash available at the end of year three that is not invested in anything maturing by then, should that uninvested cash count toward the final wealth, or should it be excluded?

## Turn 9 - User Simulator

Uninvested cash at the end of year three counts toward the final wealth.

## Turn 10 - Generic Agent

QUESTION: Are there any minimum or maximum investment amounts per option per year, or can any non-negative amount (including zero) be invested in each option each year?

## Turn 10 - User Simulator

Any non-negative amount, including zero, can be invested in each option each year.

## Turn 11 - Generic Agent

QUESTION: The brief says the total amount invested initially cannot exceed 100,000 yuan. Does this constraint apply only to the initial (year 0) investment, or is there also a limit on how much can be reinvested in later years (for example, a cap on total assets at any point)?

## Turn 11 - User Simulator

The constraint applies only to the initial (year 0) investment. There is no separate cap on reinvestment in later years.

## Turn 12 - Generic Agent

QUESTION: Are the investment amounts required to be in whole yuan (integer amounts), or can they be any fractional amount?

## Turn 12 - User Simulator

The investment amounts can be any fractional amount.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 3 years (years 0, 1, 2, 3).
- **Initial capital:** 100,000 yuan available at year 0.
- **Investment options:**
  - **Option 1:** 1-year maturity. Returns 1.7 yuan total per 1 yuan invested (0.7 profit).
  - **Option 2:** 2-year maturity. Returns 3 yuan total per 1 yuan invested (2 profit). Must be held exactly 2 years (no 4-year holdings within this horizon).
- **Reinvestment:** Proceeds from maturing investments can be reinvested in either option in subsequent years. Amounts can be split arbitrarily between options.
- **Constraints:**
  - Total initial investment at year 0 ≤ 100,000 yuan.
  - No separate cap on reinvestment in later years.
  - Any non-negative (fractional) amount can be invested in each option each year.
- **Objective:** Maximize total wealth at the end of year 3, where:
  - Only investments that have matured by the end of year 3 count.
  - Uninvested cash at the end of year 3 also counts toward final wealth.
  - Investments still locked (e.g., option 1 started in year 3, maturing in year 4) do NOT count.