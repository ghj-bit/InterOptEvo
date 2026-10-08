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

QUESTION: When you say the first investment "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean you get back your original 1 yuan plus 0.7 yuan (i.e., 1.7 yuan total) after one year, or do you get back only the 0.7 yuan (losing your principal)?

## Turn 1 - User Simulator

You get back your original 1 yuan plus 0.7 yuan, so the total is 1.7 yuan after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, when you say it "guarantees a return of 2 yuan for every 1 yuan invested after two years," do you mean you get back your original 1 yuan plus 2 yuan (i.e., 3 yuan total) after two years, or do you get back only the 2 yuan (losing your principal)?

## Turn 2 - User Simulator

You get back your original 1 yuan plus 2 yuan, so the total is 3 yuan after two years.

## Turn 3 - Generic Agent

QUESTION: Can you reinvest the money you receive from maturing investments into either option in later years, or is the 100,000 yuan the only money you can ever invest?

## Turn 3 - User Simulator

Yes, you can reinvest the money received from maturing investments into either option in later years.

## Turn 4 - Generic Agent

QUESTION: You mentioned the second investment must be held for a period that is a multiple of two years. Does this mean you can hold it for 2 years, 4 years, 6 years, etc., and the 3x return applies for each 2-year holding period (so holding 4 years would give 3x of 3x = 9x), or does it simply mean you can only start the second investment in years where it will mature within the 3-year horizon (i.e., only at year 0 or year 1)?

## Turn 4 - User Simulator

It simply means you can only start the second investment in years where it will mature within the 3-year horizon (i.e., only at year 0 or year 1).

## Turn 5 - Generic Agent

QUESTION: What is the goal of this investment plan — do you want to maximize the total amount of money you have at the end of year 3, or is there some other objective such as maximizing returns at a specific intermediate point?

## Turn 5 - User Simulator

The goal is to maximize the total amount of money you have at the end of year 3.

## Turn 6 - Generic Agent

QUESTION: If you have money available at the end of year 3 that was not invested (for example, money from a first-investment that matured at the end of year 3), does it simply count toward your final total, or is there any penalty or requirement to invest all available funds at each decision point?

## Turn 6 - User Simulator

It simply counts toward your final total.

## Turn 7 - Generic Agent

QUESTION: At each decision point (start of year 1, start of year 2, start of year 3), can you split your available money arbitrarily between the two investment options, or must you invest in whole units (e.g., whole yuan amounts)?

## Turn 7 - User Simulator

You can split your available money arbitrarily between the two investment options.

## Turn 8 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 3 (i.e., in the final year), even though it would mature at the end of year 3 and you would receive the 1.7x return right at the end of the horizon?

## Turn 8 - User Simulator

Yes, you can invest in the first option at the start of year 3.

## Turn 9 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 3, even though it would not mature until the end of year 5 (beyond your 3-year horizon)?

## Turn 9 - User Simulator

No, you cannot invest in the second option at the start of year 3.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how much you can invest in either option at any given time, or is the only constraint the total available capital at each decision point?

## Turn 10 - User Simulator

The only constraint is the total available capital at each decision point.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Horizon:** 3 years, with decision points at the start of year 1, year 2, and year 3.

**Objective:** Maximize total wealth at the end of year 3.

**Initial capital:** 100,000 yuan available at the start of year 1.

**Investment options:**

1. **Option 1 (1-year):** Invest at the start of any year (1, 2, or 3). At the end of that year, you receive back 1.7× the amount invested.

2. **Option 2 (2-year):** Invest only at the start of year 1 or year 2 (so it matures within the 3-year horizon). At the end of the second year, you receive back 3× the amount invested.

**Reinvestment:** Money received from maturing investments can be reinvested in either option at the next decision point.

**Constraints:**
- At each decision point, the total amount allocated to investments cannot exceed the available capital at that point.
- You may split funds arbitrarily (continuous amounts) between the two options.
- You may leave money uninvested; it simply carries forward and counts toward the final total.
- No other per-option limits.

**Key timing details:**
- Option 1 invested at start of year 3 matures at end of year 3 (within horizon).
- Option 2 cannot be invested at start of year 3 (would mature at end of year 5, beyond horizon).
- Uninvested cash at end of year 3 counts toward the final total.