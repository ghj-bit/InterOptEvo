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

QUESTION: For the first investment option, when the 0.7 yuan return is received at the end of year 1, is that 0.7 yuan the profit on top of the original 1 yuan (so you get back 1.7 yuan total), or is it the total amount returned (so you get back only 0.7 yuan and lose principal)?

## Turn 1 - User Simulator

The 0.7 yuan is the profit on top of the original 1 yuan. So, for every 1 yuan invested, you get back 1.7 yuan total at the end of year 1.

## Turn 2 - Generic Agent

QUESTION: For the second investment option, is the 2 yuan return the profit on top of the original 1 yuan (so you get back 3 yuan total after two years), or is it the total amount returned (so you get back only 2 yuan)?

## Turn 2 - User Simulator

The 2 yuan is the profit on top of the original 1 yuan. So, for every 1 yuan invested, you get back 3 yuan total after two years.

## Turn 3 - Generic Agent

QUESTION: At the end of year 1, the proceeds from the first investment (1.7 yuan per yuan invested) become available — can these proceeds be reinvested into either option in year 2, or must all investing be done only from the original 100,000 yuan at the start of year 1?

## Turn 3 - User Simulator

The proceeds from the first investment can be reinvested into either option in year 2.

## Turn 4 - Generic Agent

QUESTION: When you say the second investment "must be held for a period that is a multiple of two years," does that mean each individual investment in option 2 must be held for exactly 2 years (not 4 or 6), or could a single investment in option 2 be held for 4 years (i.e., 2×2) within the three-year horizon?

## Turn 4 - User Simulator

Each individual investment in option 2 must be held for exactly 2 years.

## Turn 5 - Generic Agent

QUESTION: What is the goal of this investment plan — is it to maximize the total amount of money (principal plus profit) available at the end of year 3?

## Turn 5 - User Simulator

Yes, the goal is to maximize the total amount of money available at the end of year 3.

## Turn 6 - Generic Agent

QUESTION: If you invest in option 2 at the start of year 1, it matures at the end of year 2 and you receive 3 yuan per yuan invested — can those proceeds then be reinvested in option 1 for the final year (year 3), or are option 2 proceeds locked and only available at the end of year 3?

## Turn 6 - User Simulator

The proceeds from option 2 can be reinvested in option 1 for the final year (year 3).

## Turn 7 - Generic Agent

QUESTION: At the end of year 3, any money that was not invested (idle cash) simply remains available as part of the final total, correct — there is no penalty or requirement to have everything fully invested?

## Turn 7 - User Simulator

Yes, any money not invested remains available as part of the final total at the end of year 3.

## Turn 8 - Generic Agent

QUESTION: Are there any minimum or maximum investment amounts per option per year (e.g., you must invest at least some amount, or cannot invest more than some cap), or can you invest any amount from 0 up to whatever cash is available?

## Turn 8 - User Simulator

There are no minimum or maximum investment amounts per option per year. You can invest any amount from 0 up to whatever cash is available.

## Turn 9 - Generic Agent

QUESTION: Can you invest in option 2 at the start of year 2 (so it matures at the end of year 3), or is option 2 only available for investment at the start of year 1?

## Turn 9 - User Simulator

Yes, you can invest in option 2 at the start of year 2, so it matures at the end of year 3.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how many times you can invest in option 1 — for example, can you invest in option 1 in all three years (year 1, year 2, and year 3), or is there a restriction on the number of times option 1 can be used?

## Turn 10 - User Simulator

There is no restriction on the number of times option 1 can be used. You can invest in option 1 in all three years.

## Turn 11 - Generic Agent

QUESTION: Is there any restriction on investing in option 2 more than once — for example, could you invest in option 2 at the start of year 1 AND also invest in option 2 at the start of year 2, or is option 2 limited to a single investment over the entire horizon?

## Turn 11 - User Simulator

There is no restriction on investing in option 2 more than once. You could invest in option 2 at the start of year 1 and also invest in option 2 at the start of year 2.

## Turn 12 - Generic Agent

QUESTION: When you say "the total amount invested initially cannot exceed the available capital of 100,000 yuan," does this constraint apply only to the initial investment at the start of year 1, or does it also mean that at any point in time (including reinvestments in years 2 and 3) the total amount currently invested cannot exceed 100,000 yuan?

## Turn 12 - User Simulator

This constraint applies only to the initial investment at the start of year 1.

## Turn 13 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize the total amount of money (principal + profit + any idle cash) available at the end of year 3.

**Initial capital:** 100,000 yuan available at the start of year 1.

**Investment options:**
- **Option 1:** Invest any amount at the start of a year; receive 1.7× the amount invested at the end of that year (0.7 profit per 1 yuan). Can be used in any year (year 1, 2, or 3), any number of times.
- **Option 2:** Invest any amount at the start of a year; receive 3× the amount invested at the end of that 2-year holding period (2 profit per 1 yuan). Must be held for exactly 2 years. Can be initiated at the start of year 1 (matures end of year 2) or at the start of year 2 (matures end of year 3). Can be used more than once.

**Reinvestment rules:**
- Proceeds from option 1 (maturing at end of year 1) can be reinvested in either option 1 or option 2 at the start of year 2.
- Proceeds from option 2 (maturing at end of year 2) can be reinvested in option 1 at the start of year 3.
- Any cash not invested at any point simply carries forward as idle cash.

**Constraints:**
- The total amount invested at the start of year 1 (into option 1 and/or option 2) cannot exceed 100,000 yuan.
- No minimum or maximum per-investment amounts.
- No other constraints on reinvestment amounts in years 2 and 3 (limited only by available cash).

**Decision variables:** Amounts allocated to option 1 and option 2 at the start of each year (year 1, year 2, year 3 as applicable), with cash-flow balance linking years together.