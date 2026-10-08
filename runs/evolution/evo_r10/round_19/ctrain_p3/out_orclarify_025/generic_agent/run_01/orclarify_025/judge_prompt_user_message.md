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

QUESTION: For the first investment option, is the 0.7 yuan return a simple interest (so 1 yuan invested becomes 1.7 yuan after one year, and the original 1 yuan is returned), or is it a net gain on top of the principal?

## Turn 1 - User Simulator

The 0.7 yuan is a net gain on top of the principal. So, 1 yuan invested becomes 1.7 yuan after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment option, is the 2 yuan return a net gain on top of the principal (so 1 yuan invested becomes 3 yuan after two years), or is it the total amount returned (so 1 yuan invested becomes 2 yuan after two years)?

## Turn 2 - User Simulator

The 2 yuan is a net gain on top of the principal. So, 1 yuan invested becomes 3 yuan after two years.

## Turn 3 - Generic Agent

QUESTION: When you say the second investment "must be held for a period that is a multiple of two years," does that mean the only allowed holding periods are exactly 2 years (since the horizon is 3 years, a 4-year hold would exceed it), or could an investor also choose to hold it for 1 year and exit early?

## Turn 3 - User Simulator

The only allowed holding period is exactly 2 years.

## Turn 4 - Generic Agent

QUESTION: At the end of each year, can money that has matured (or was not invested) be reinvested into either option in the following year, or is the initial 100,000 yuan the only capital that can ever be invested?

## Turn 4 - User Simulator

Money that has matured or was not invested can be reinvested into either option in the following year.

## Turn 5 - Generic Agent

QUESTION: Is the goal to maximize the total amount of money available at the end of year 3, or is there some other objective such as maximizing returns at a specific intermediate point?

## Turn 5 - User Simulator

The goal is to maximize the total amount of money available at the end of year 3.

## Turn 6 - Generic Agent

QUESTION: If money is not invested in a given year, does it simply carry over to the next year with no interest or growth, or does it earn some return while idle?

## Turn 6 - User Simulator

Money that is not invested simply carries over to the next year with no interest or growth.

## Turn 7 - Generic Agent

QUESTION: Can the first investment option be invested in during year 2 (maturing at the end of year 3), or is it only available for investment at the start of year 1?

## Turn 7 - User Simulator

The first investment option can be invested in during year 2, maturing at the end of year 3.

## Turn 8 - Generic Agent

QUESTION: Can the second investment option be invested in during year 2 (maturing at the end of year 4, which is beyond the 3-year horizon), or is it only available for investment at the start of year 1 (maturing at the end of year 2)?

## Turn 8 - User Simulator

The second investment option is only available for investment at the start of year 1, maturing at the end of year 2.

## Turn 9 - Generic Agent

QUESTION: Are there any minimum or maximum investment amounts for either option, or can any non-negative amount (including fractional yuan) be invested in each?

## Turn 9 - User Simulator

There are no minimum or maximum investment amounts for either option. Any non-negative amount, including fractional yuan, can be invested in each.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how much can be invested in the second option at the start of year 1, other than the total 100,000 yuan capital constraint?

## Turn 10 - User Simulator

No, there is no limit on how much can be invested in the second option at the start of year 1, other than the total 100,000 yuan capital constraint.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how much can be invested in the first option during year 2, other than the amount of money available at that time?

## Turn 11 - User Simulator

No, there is no limit on how much can be invested in the first option during year 2, other than the amount of money available at that time.

## Turn 12 - Generic Agent

QUESTION: At the end of year 3, does the total amount of money available include both the principal and the net gains from all matured investments, or only the net gains?

## Turn 12 - User Simulator

The total amount of money available at the end of year 3 includes both the principal and the net gains from all matured investments.

## Turn 13 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Horizon and Objective**
- Three-year investment horizon (years 1, 2, 3).
- Goal: maximize total money available at the end of year 3 (principal + net gains from all matured investments).

**Capital**
- Initial capital: 100,000 yuan.
- Total invested at the start of year 1 cannot exceed 100,000 yuan.
- Uninvested money carries over to the next year with no interest or growth.
- Matured money can be reinvested in subsequent years.

**Investment Options**

1. **Option 1 (1-year maturity):**
   - Available for investment at the start of year 1 and at the start of year 2.
   - Net gain: 0.7 yuan per 1 yuan invested (so 1 yuan becomes 1.7 yuan after one year).
   - If invested at start of year 1, matures at end of year 1.
   - If invested at start of year 2, matures at end of year 2.
   - No minimum or maximum investment amount; any non-negative fractional amount allowed.

2. **Option 2 (2-year maturity, must be held exactly 2 years):**
   - Available for investment only at the start of year 1.
   - Matures at the end of year 2.
   - Net gain: 2 yuan per 1 yuan invested (so 1 yuan becomes 3 yuan after two years).
   - No minimum or maximum investment amount; any non-negative fractional amount allowed.

**Constraints**
- Total invested at start of year 1 ≤ 100,000 yuan.
- Total invested at start of year 2 ≤ money available at start of year 2 (from uninvested year-1 capital + matured year-1 Option 1 returns + matured Option 2 returns).
- All investment amounts are non-negative and continuous (fractional yuan allowed).