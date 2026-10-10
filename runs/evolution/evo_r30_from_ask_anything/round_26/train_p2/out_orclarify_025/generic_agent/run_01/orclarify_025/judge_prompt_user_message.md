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

QUESTION: Is the goal of the investment plan to maximize the total amount of money available at the end of the three-year horizon?

## Turn 1 - User Simulator

Yes.

## Turn 2 - Generic Agent

QUESTION: For the first investment option, is the 0.7 yuan return a simple interest payment that does not include the original 1 yuan principal, or is it the total amount returned including the principal?

## Turn 2 - User Simulator

The 0.7 yuan is the return on top of the original 1 yuan principal.

## Turn 3 - Generic Agent

QUESTION: For the second investment option, is the 2 yuan return a simple interest payment that does not include the original 1 yuan principal, or is it the total amount returned including the principal?

## Turn 3 - User Simulator

The 2 yuan is the return on top of the original 1 yuan principal.

## Turn 4 - Generic Agent

QUESTION: When the first investment matures after one year, is the total amount (principal plus return) available to be reinvested in either option in the following year?

## Turn 4 - User Simulator

Yes, the total amount (principal plus return) is available to be reinvested in either option in the following year.

## Turn 5 - Generic Agent

QUESTION: When the second investment matures after two years, is the total amount (principal plus return) available to be reinvested in the first investment option for the remaining year of the three-year horizon?

## Turn 5 - User Simulator

Yes, the total amount (principal plus return) is available to be reinvested in the first investment option for the remaining year of the three-year horizon.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan, such as minimum investment amounts, limits on how much can be invested in each option per year, or rules about holding cash uninvested?

## Turn 6 - User Simulator

No, there are no other constraints or requirements beyond the initial capital limit of 100,000 yuan and the rule that the second investment must be held for a multiple of two years.

## Turn 7 - Generic Agent

QUESTION: Is the amount invested in each option in each year required to be a whole number of yuan, or can it be any non-negative real number?

## Turn 7 - User Simulator

It can be any non-negative real number.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total amount of money available at the end of the three-year horizon.
2.  **Time Horizon:** 3 years.
3.  **Initial Capital:** 100,000 yuan.
4.  **Investment Options:**
    *   **Option 1:** 1-year maturity. Return is 0.7 yuan per 1 yuan invested (simple interest). Total return at maturity is 1.7 times the principal.
    *   **Option 2:** 2-year maturity. Return is 2 yuan per 1 yuan invested (simple interest). Total return at maturity is 3 times the principal.
5.  **Reinvestment Rules:**
    *   Proceeds from Option 1 (principal + interest) can be reinvested in either Option 1 or Option 2 in subsequent years.
    *   Proceeds from Option 2 (principal + interest) can be reinvested in Option 1 for the remaining year if it matures in year 2.
6.  **Constraints:**
    *   Total initial investment cannot exceed 100,000 yuan.
    *   Option 2 must be held for a multiple of 2 years (i.e., it matures exactly at the end of year 2 or year 4, etc.; within the 3-year horizon, it effectively matures at the end of year 2).
    *   No other constraints (no minimums, no per-year caps, no requirement to invest all capital).
7.  **Variable Domain:** Investment amounts can be any non-negative real number.

**Assumptions:**
*   Cash not invested is held as cash with 0% return and is available at the end of the horizon.
*   "Held for a multiple of two years" implies that if invested in Year 1, it matures at the end of Year 2. It cannot be invested in Year 2 to mature at the end of Year 4 because the horizon ends at Year 3.