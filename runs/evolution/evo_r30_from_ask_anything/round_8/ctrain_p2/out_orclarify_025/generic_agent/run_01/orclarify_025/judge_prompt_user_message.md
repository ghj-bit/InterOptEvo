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

QUESTION: When you say the second investment must be held for a period that is a multiple of two years, do you mean it must be held for exactly two years, or could it also be held for four years (which would extend beyond the three-year horizon)?

## Turn 1 - User Simulator

It must be held for exactly two years.

## Turn 2 - Generic Agent

QUESTION: When the first investment matures after one year, is the returned amount (principal plus return) available to be reinvested in either option in the following year, or is it withdrawn and not available for further investment?

## Turn 2 - User Simulator

The returned amount is available to be reinvested in either option in the following year.

## Turn 3 - Generic Agent

QUESTION: Is the objective to maximize the total amount of money available at the end of year three, or is there a different goal such as maximizing the total return earned over the three years?

## Turn 3 - User Simulator

The objective is to maximize the total amount of money available at the end of year three.

## Turn 4 - Generic Agent

QUESTION: When you say the total amount invested initially cannot exceed 100,000 yuan, does this constraint apply only to the investments made at the start of year one, or does it also limit the total amount invested in any subsequent year (e.g., year two) to 100,000 yuan?

## Turn 4 - User Simulator

The constraint applies only to the investments made at the start of year one.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts in each option and each year required to be whole numbers (integer yuan), or can they be any non-negative real number?

## Turn 5 - User Simulator

They can be any non-negative real number.

## Turn 6 - Generic Agent

QUESTION: When the second investment matures at the end of year two, is the returned amount available to be reinvested in the first investment option for year three, or is it withdrawn and not available for further investment?

## Turn 6 - User Simulator

The returned amount is available to be reinvested in the first investment option for year three.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Time Horizon:** Three years (Year 1, Year 2, Year 3).
- **Objective:** Maximize the total amount of money available at the end of Year 3.
- **Initial Capital:** 100,000 yuan available at the start of Year 1.
- **Investment Options:**
  - **Option 1:** 1-year maturity. Return is 0.7 yuan per 1 yuan invested (i.e., 1.7x principal at maturity).
  - **Option 2:** 2-year maturity. Return is 2 yuan per 1 yuan invested (i.e., 3x principal at maturity). Must be held for exactly two years.
- **Reinvestment Rules:**
  - Proceeds from Option 1 maturing at the end of Year 1 are available for reinvestment in Year 2.
  - Proceeds from Option 2 maturing at the end of Year 2 are available for reinvestment in Year 3 (specifically in Option 1, as Option 2 cannot fit in the remaining one year).
- **Constraints:**
  - The total amount invested at the start of Year 1 cannot exceed 100,000 yuan.
  - There are no explicit constraints on the amount invested in Year 2 or Year 3 other than the availability of funds from previous maturities.
- **Variable Domain:** Investment amounts are non-negative real numbers.

**Assumptions:**
- No transaction costs or taxes are applied.
- Funds not invested in a given year are held as cash with zero return until the end of Year 3.
- The "return" figures (0.7 and 2) are in addition to the principal, so the total payout is 1.7x and 3x the invested amount, respectively.