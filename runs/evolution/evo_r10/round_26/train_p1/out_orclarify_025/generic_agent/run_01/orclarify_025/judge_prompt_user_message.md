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

QUESTION: For the first investment option, when the 0.7 yuan return is received at the end of year 1, is that 0.7 yuan the total amount you get back (i.e., 1.7 yuan total per 1 yuan invested, a 70% gain), or is it the profit on top of your original 1 yuan (i.e., 1.7 yuan total per 1 yuan invested, a 70% gain)?

## Turn 1 - User Simulator

The 0.7 yuan is the profit on top of your original 1 yuan. So, for every 1 yuan invested, you get back 1.7 yuan total at the end of year 1.

## Turn 2 - Generic Agent

QUESTION: For the second investment option, is the 2 yuan return the profit on top of your original 1 yuan (so you get back 3 yuan total per 1 yuan invested at the end of year 2), or is it the total amount you get back (so you get back 2 yuan total per 1 yuan invested, a 100% gain)?

## Turn 2 - User Simulator

The 2 yuan is the profit on top of your original 1 yuan. So, for every 1 yuan invested, you get back 3 yuan total at the end of year 2.

## Turn 3 - Generic Agent

QUESTION: Can money that becomes available at the end of year 1 (from the first investment maturing) be reinvested into either option at the start of year 2, or is the only investment decision made once at the start of year 1 with no reinvestment allowed?

## Turn 3 - User Simulator

Money that becomes available at the end of year 1 can be reinvested into either option at the start of year 2.

## Turn 4 - Generic Agent

QUESTION: Can money that becomes available at the end of year 2 (from the second investment maturing) be reinvested into the first option for the year 3 period, or does the second investment's "multiple of two years" holding rule mean it must be held for the full three years (i.e., 2+1 is not allowed, only 2 or 4)?

## Turn 4 - User Simulator

Money that becomes available at the end of year 2 can be reinvested into the first option for the year 3 period.

## Turn 5 - Generic Agent

QUESTION: When you say the second investment "must be held for a period that is a multiple of two years," does that mean each individual investment in the second option must be held for exactly 2 years (so you can invest in it at the start of year 1 and again at the start of year 2, each held for 2 years), or does it mean the total time you are exposed to the second option across the whole plan must be a multiple of 2 years?

## Turn 5 - User Simulator

Each individual investment in the second option must be held for exactly 2 years.

## Turn 6 - Generic Agent

QUESTION: What is the objective of the investment plan — is it to maximize the total amount of money you have at the end of year 3 (i.e., maximize final wealth), or is there some other goal such as maximizing returns above the initial 100,000 yuan, or minimizing risk?

## Turn 6 - User Simulator

The objective is to maximize the total amount of money you have at the end of year 3.

## Turn 7 - Generic Agent

QUESTION: At the end of year 3, if you have money that was invested in the first option at the start of year 3, it matures at the end of year 3 and is available. But what about money that was invested in the second option at the start of year 2 — it matures at the end of year 4, which is beyond the three-year horizon. Is that money simply not counted in the final wealth at the end of year 3, or is there some other treatment (e.g., it is liquidated early at face value, or it is excluded from the plan entirely)?

## Turn 7 - User Simulator

That money is excluded from the plan entirely.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how much can be invested in either option at any given time, or can you invest any amount (up to the available cash) in each option at each decision point?

## Turn 8 - User Simulator

There is no limit on how much can be invested in either option at any given time, other than the available cash.

## Turn 9 - Generic Agent

QUESTION: Can you invest in both options simultaneously at the same decision point (e.g., split your available cash between the first and second options at the start of year 1), or must you choose only one option at each decision point?

## Turn 9 - User Simulator

You can invest in both options simultaneously at the same decision point.

## Turn 10 - Generic Agent

QUESTION: Is there any requirement that all available cash must be invested at each decision point, or is it allowed to hold some cash idle (earning no return) at any point during the three years?

## Turn 10 - User Simulator

It is allowed to hold some cash idle (earning no return) at any point during the three years.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the investment plan:

**Horizon:** 3 years, with decision points at the start of year 1, start of year 2, and start of year 3.

**Initial capital:** 100,000 yuan available at the start of year 1.

**Investment options:**
- **Option 1 (1-year):** Invest any amount at the start of a year; at the end of that year, receive back 1.7 yuan per 1 yuan invested (70% profit).
- **Option 2 (2-year):** Invest any amount at the start of a year; at the end of the second year, receive back 3 yuan per 1 yuan invested (200% profit). Each individual investment must be held for exactly 2 years.

**Reinvestment rules:**
- Money maturing at the end of year 1 (from Option 1 invested at start of year 1) is available at the start of year 2 and can be reinvested in either option.
- Money maturing at the end of year 2 (from Option 2 invested at start of year 1) is available at the start of year 3 and can be reinvested in Option 1 for the year 3 period.
- Option 2 investments made at the start of year 2 would mature at the end of year 4, which is beyond the horizon, so they are excluded from the plan entirely.

**Constraints:**
- Total initial investment at the start of year 1 cannot exceed 100,000 yuan.
- At each decision point, you can invest in both options simultaneously, split arbitrarily, or hold cash idle (earning no return).
- No per-option investment limits beyond available cash.

**Objective:** Maximize total wealth (cash + matured investments) at the end of year 3.

**Decision variables (at each decision point):**
- Amount allocated to Option 1
- Amount allocated to Option 2 (only at start of year 1, since Option 2 at start of year 2 is excluded)
- Amount held as idle cash

The model will track cash flows across the three years and maximize the final amount at the end of year 3.