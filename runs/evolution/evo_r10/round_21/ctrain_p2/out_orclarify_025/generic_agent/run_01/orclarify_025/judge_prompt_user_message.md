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

QUESTION: When you say the second investment "must be held for a period that is a multiple of two years," do you mean it must be held for exactly 2 years (so it matures at the end of year 2), or could it also be held for 4 years (maturing at the end of year 4, i.e., beyond the 3-year horizon)?

## Turn 1 - User Simulator

It must be held for exactly 2 years, so it matures at the end of year 2.

## Turn 2 - Generic Agent

QUESTION: At the end of year 2, when the second investment matures and returns 2 yuan per 1 yuan invested, can that returned amount be reinvested in either option for the remaining year (year 3), or must it simply be held as cash until the end of the 3-year horizon?

## Turn 2 - User Simulator

The returned amount can be reinvested in either option for the remaining year (year 3).

## Turn 3 - Generic Agent

QUESTION: If the second investment's returned amount is reinvested in the second option at the end of year 2, it would mature at the end of year 4, which is beyond the 3-year horizon. Is that allowed (i.e., you can hold it past the horizon and count its value at year 4), or can the year-2 proceeds only be reinvested in the first option (which matures at the end of year 3)?

## Turn 3 - User Simulator

The year-2 proceeds can only be reinvested in the first option, which matures at the end of year 3.

## Turn 4 - Generic Agent

QUESTION: What is the goal of this plan — to maximize the total amount of money you have at the end of year 3, or is there some other objective (such as maximizing returns at a specific earlier point, or minimizing risk)?

## Turn 4 - User Simulator

The goal is to maximize the total amount of money you have at the end of year 3.

## Turn 5 - Generic Agent

QUESTION: The first investment matures at the end of year 1. Can that returned amount be reinvested in either option at the start of year 2 (i.e., in the first option for year 2, or in the second option which would then mature at the end of year 3), or must it be held as cash?

## Turn 5 - User Simulator

The returned amount can be reinvested in either option at the start of year 2.

## Turn 6 - Generic Agent

QUESTION: At the start of year 2, if the year-1 proceeds are reinvested in the second option, it would mature at the end of year 3 (within the horizon). Is that allowed, or can year-1 proceeds only be reinvested in the first option?

## Turn 6 - User Simulator

Yes, that is allowed. Year-1 proceeds can be reinvested in the second option at the start of year 2, maturing at the end of year 3.

## Turn 7 - Generic Agent

QUESTION: The constraint says the total amount invested initially cannot exceed 100,000 yuan. Does this mean the sum of what you put into the first and second options at the start of year 1 must be at most 100,000, and any leftover (100,000 minus that sum) simply sits as cash earning nothing?

## Turn 7 - User Simulator

Yes, the sum of what you put into the first and second options at the start of year 1 must be at most 100,000, and any leftover simply sits as cash earning nothing.

## Turn 8 - Generic Agent

QUESTION: When you reinvest proceeds in later years, is there any limit on how much you can reinvest (for example, must reinvested amounts also stay within the original 100,000 capital), or can you reinvest the full proceeds regardless of the original capital amount?

## Turn 8 - User Simulator

You can reinvest the full proceeds regardless of the original capital amount.

## Turn 9 - Generic Agent

QUESTION: Are the investment amounts required to be whole numbers (e.g., whole yuan), or can you invest any fractional amount?

## Turn 9 - User Simulator

You can invest any fractional amount.

## Turn 10 - Generic Agent

QUESTION: When the first investment matures at the end of year 1 and returns 0.7 yuan per 1 yuan invested, does that mean you get back 0.7 yuan total (i.e., a loss of principal), or do you get back 1.7 yuan total (i.e., 1 yuan principal plus 0.7 yuan return)?

## Turn 10 - User Simulator

You get back 1.7 yuan total (1 yuan principal plus 0.7 yuan return).

## Turn 11 - Generic Agent

QUESTION: Similarly, when the second investment matures at the end of year 2 and returns 2 yuan per 1 yuan invested, do you get back 2 yuan total (a loss of principal), or do you get back 3 yuan total (1 yuan principal plus 2 yuan return)?

## Turn 11 - User Simulator

You get back 3 yuan total (1 yuan principal plus 2 yuan return).

## Turn 12 - Generic Agent

QUESTION: At the end of year 3, the first investment matures and returns 1.7 yuan per 1 yuan invested. Is the total amount you have at the end of year 3 simply the sum of all matured proceeds plus any cash that was never invested, with no further reinvestment possible after year 3?

## Turn 12 - User Simulator

Yes, the total amount you have at the end of year 3 is simply the sum of all matured proceeds plus any cash that was never invested, with no further reinvestment possible after year 3.

## Turn 13 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Horizon and Objective**
- Three-year investment horizon (years 1, 2, 3).
- Goal: maximize total money held at the end of year 3.

**Capital**
- Initial capital: 100,000 yuan.
- At the start of year 1, the sum invested in both options must be ≤ 100,000. Any leftover sits as cash earning nothing.
- Reinvested proceeds in later years are not capped by the original 100,000.

**Investment Options**
- **Option 1:** 1-year maturity. For every 1 yuan invested, you receive 1.7 yuan at maturity (principal + 0.7 return).
- **Option 2:** 2-year maturity (must be held exactly 2 years). For every 1 yuan invested, you receive 3 yuan at maturity (principal + 2 return).

**Reinvestment Rules**
- Year 1: Invest in Option 1 and/or Option 2 (subject to the 100,000 cap).
- End of Year 1: Option 1 investments mature. Proceeds can be reinvested in either Option 1 or Option 2 at the start of year 2.
- End of Year 2: Option 2 investments (from year 1) mature. Proceeds can only be reinvested in Option 1 at the start of year 3 (since Option 2 would mature at year 4, beyond the horizon).
- End of Year 3: All Option 1 investments mature. Total wealth = sum of all matured proceeds + any uninvested cash. No further reinvestment.

**Variable Domains**
- All investment amounts are continuous (fractional yuan allowed).
- All amounts are non-negative.