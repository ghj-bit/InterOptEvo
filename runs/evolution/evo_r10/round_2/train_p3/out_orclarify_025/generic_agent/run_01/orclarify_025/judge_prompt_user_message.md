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

QUESTION: For the first investment, when you say it "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean the investor receives 1.7 yuan total (principal plus 0.7 profit) after one year, or only 0.7 yuan total (a loss of principal)?

## Turn 1 - User Simulator

The investor receives 1.7 yuan total (principal plus 0.7 profit) after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, when you say it "guarantees a return of 2 yuan for every 1 yuan invested after two years," do you mean the investor receives 3 yuan total (principal plus 2 profit) after two years, or only 2 yuan total (a 1 yuan profit)?

## Turn 2 - User Simulator

The investor receives 3 yuan total (principal plus 2 profit) after two years.

## Turn 3 - Generic Agent

QUESTION: When the first investment matures after one year, can the proceeds (principal plus profit) be reinvested in either option in the following year, or must all investment decisions be made only at the start of year 1 with no reinvestment allowed?

## Turn 3 - User Simulator

The proceeds can be reinvested in either option in the following year.

## Turn 4 - Generic Agent

QUESTION: You mentioned the second investment must be held for a period that is a multiple of two years. Does this mean it can be held for 2 years, 4 years, 6 years, etc., or is it simply that the holding period is exactly 2 years (i.e., it matures after 2 years and can then be reinvested)?

## Turn 4 - User Simulator

It can be held for 2 years, 4 years, 6 years, etc.

## Turn 5 - Generic Agent

QUESTION: If the second investment is held for 4 years (i.e., 2 years plus another 2 years), does the return compound — so 1 yuan invested at the start of year 1 becomes 3 yuan at the end of year 2 and then 9 yuan at the end of year 4 — or does it simply pay 3 yuan total at the end of the full 4-year holding period (i.e., the 2 yuan profit is not reinvested automatically)?

## Turn 5 - User Simulator

The return compounds — so 1 yuan invested at the start of year 1 becomes 3 yuan at the end of year 2 and then 9 yuan at the end of year 4.

## Turn 6 - Generic Agent

QUESTION: What is the objective of this investment plan — is it to maximize the total wealth (principal plus all accumulated profits) at the end of year 3, or is there a different goal such as maximizing the return at a specific intermediate point?

## Turn 6 - User Simulator

The objective is to maximize the total wealth (principal plus all accumulated profits) at the end of year 3.

## Turn 7 - Generic Agent

QUESTION: Since the second investment matures in even years (end of year 2, end of year 4, etc.) and the horizon ends at the end of year 3, can money be invested in the second option at the start of year 3 (so it would mature at the end of year 5, beyond the horizon), or is the second option only available for investments that mature within the three-year horizon?

## Turn 7 - User Simulator

The second option is only available for investments that mature within the three-year horizon.

## Turn 8 - Generic Agent

QUESTION: At the end of year 3, if there is any cash that is not invested in either option (e.g., money that matured from the first investment at the end of year 3), does it simply remain as cash and count toward the final wealth, or must all funds be fully invested at all times?

## Turn 8 - User Simulator

It simply remains as cash and counts toward the final wealth.

## Turn 9 - Generic Agent

QUESTION: Can the first investment be made at the start of each year (years 1, 2, and 3), with proceeds maturing at the end of that same year, or is it only available at the start of year 1?

## Turn 9 - User Simulator

The first investment can be made at the start of each year (years 1, 2, and 3), with proceeds maturing at the end of that same year.

## Turn 10 - Generic Agent

QUESTION: Can the second investment be made at the start of year 1 (maturing at the end of year 2) and at the start of year 2 (maturing at the end of year 4, which is beyond the horizon), or is it only available at the start of year 1 within the three-year horizon?

## Turn 10 - User Simulator

The second investment is only available at the start of year 1 within the three-year horizon.

## Turn 11 - Generic Agent

QUESTION: Are there any minimum or maximum investment amounts for either option, or can any non-negative amount (including fractional yuan) be invested in each option at each eligible time?

## Turn 11 - User Simulator

Any non-negative amount (including fractional yuan) can be invested in each option at each eligible time.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in the second option at the start of year 1, or is the only constraint the initial capital of 100,000 yuan shared across both options?

## Turn 12 - User Simulator

The only constraint is the initial capital of 100,000 yuan shared across both options.

## Turn 13 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total wealth (cash + matured investment proceeds) at the end of year 3.

**Initial capital:** 100,000 yuan available at the start of year 1.

**Investment options:**

1. **Option 1 (1-year):** Can be invested at the start of years 1, 2, and 3. Returns 1.7 yuan per 1 yuan invested (i.e., 70% profit) at the end of that same year.

2. **Option 2 (2-year, compounding):** Can only be invested at the start of year 1 (so it matures at the end of year 2, within the horizon). Returns 3 yuan per 1 yuan invested (i.e., 200% profit) at the end of year 2. If held for 4 years it would compound to 9 yuan, but since the horizon is 3 years, only the 2-year maturity is relevant here.

**Reinvestment:** Proceeds from any maturing investment can be reinvested in either option in subsequent years (subject to availability rules above).

**Constraints:**
- Total invested at the start of year 1 ≤ 100,000 yuan.
- No other investment limits (no minimums, no per-option caps).
- Any non-negative (continuous) amount can be invested.
- Uninvested cash simply carries forward and counts toward final wealth.
- Option 2 is only available at the start of year 1 (maturing end of year 2).
- Option 1 is available at the start of each year (1, 2, 3), maturing at the end of that year.

**Decision variables (continuous, non-negative):**
- Amount invested in Option 1 at the start of each year (years 1, 2, 3).
- Amount invested in Option 2 at the start of year 1.

**Cash flow structure:**
- Start of year 1: Allocate initial 100,000 between Option 1 (year 1), Option 2 (year 1), and cash.
- End of year 1 / Start of year 2: Option 1 (year 1) matures → 1.7× proceeds available. Allocate between Option 1 (year 2), cash.
- End of year 2 / Start of year 3: Option 2 matures → 3× proceeds available; Option 1 (year 2) matures → 1.7× proceeds available. Allocate between Option 1 (year 3) and cash.
- End of year 3: Option 1 (year 3) matures → 1.7× proceeds. All cash + proceeds = final wealth to maximize.