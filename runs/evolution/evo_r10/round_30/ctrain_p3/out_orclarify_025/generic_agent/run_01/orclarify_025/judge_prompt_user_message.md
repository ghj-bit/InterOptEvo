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

QUESTION: For the first investment, when the 0.7 yuan return is received at the end of year 1, is that amount available to be reinvested in either option in year 2 (and again in year 3), or is it simply added to your final wealth and cannot be reinvested?

## Turn 1 - User Simulator

The 0.7 yuan return received at the end of year 1 is available to be reinvested in either option in year 2.

## Turn 2 - Generic Agent

QUESTION: When you invest in the second option, is the original 1 yuan principal returned together with the 2 yuan return at the end of the two-year holding period, or do you only receive the 2 yuan and the principal is consumed?

## Turn 2 - User Simulator

The original 1 yuan principal is returned together with the 2 yuan return at the end of the two-year holding period.

## Turn 3 - Generic Agent

QUESTION: For the first investment, is the original 1 yuan principal also returned together with the 0.7 yuan return at the end of the one-year period, or do you only receive the 0.7 yuan and the principal is consumed?

## Turn 3 - User Simulator

The original 1 yuan principal is returned together with the 0.7 yuan return at the end of the one-year period.

## Turn 4 - Generic Agent

QUESTION: At the end of year 3, is the goal to maximize the total wealth you hold (principal plus returns), or to maximize only the profit earned over the three years?

## Turn 4 - User Simulator

The goal is to maximize the total wealth you hold (principal plus returns) at the end of year 3.

## Turn 5 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 2, so that it matures at the end of year 3 (a two-year holding period that fits within the horizon)?

## Turn 5 - User Simulator

Yes, you can invest in the second option at the start of year 2, so that it matures at the end of year 3.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on how much you can invest in each option at each point in time, or can you invest any amount (up to your available cash) in either option?

## Turn 6 - User Simulator

There is no limit on how much you can invest in each option at each point in time, other than the available cash.

## Turn 7 - Generic Agent

QUESTION: If you have cash available at the start of year 3, can you invest it in the first option for one year so it matures at the end of year 3, or is the first option only available at the start of year 1?

## Turn 7 - User Simulator

Yes, you can invest in the first option at the start of year 3, so it matures at the end of year 3.

## Turn 8 - Generic Agent

QUESTION: If you have cash left over at the end of year 3 that was not invested, does it simply count toward your final wealth at its face value (1 yuan = 1 yuan), or is there any penalty or bonus applied to uninvested cash?

## Turn 8 - User Simulator

Uninvested cash counts toward your final wealth at its face value (1 yuan = 1 yuan).

## Turn 9 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 1, so that it matures at the end of year 2, and then reinvest the proceeds at the start of year 3?

## Turn 9 - User Simulator

Yes, you can invest in the second option at the start of year 1, so that it matures at the end of year 2, and then reinvest the proceeds at the start of year 3.

## Turn 10 - Generic Agent

QUESTION: Are the investment amounts required to be whole yuan amounts, or can you invest any fractional amount (continuous values)?

## Turn 10 - User Simulator

You can invest any fractional amount (continuous values).

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 3 years, with investment decisions at the start of each year (years 1, 2, 3).
- **Initial capital:** 100,000 yuan available at the start of year 1.
- **Investment Option 1:** 1-year holding period. For every 1 yuan invested, you receive 1.7 yuan (principal + 0.7 return) at the end of the year. Available at the start of any year (1, 2, or 3).
- **Investment Option 2:** 2-year holding period (must be a multiple of 2 years). For every 1 yuan invested, you receive 3 yuan (principal + 2 return) at the end of the two-year period. Available at the start of year 1 (matures end of year 2) or start of year 2 (matures end of year 3).
- **Reinvestment:** Proceeds from maturing investments are available to be reinvested in either option in subsequent years.
- **Objective:** Maximize total wealth (principal + returns + uninvested cash) at the end of year 3.
- **Constraints:** Total invested at any point cannot exceed available cash. No per-option limits. Continuous investment amounts. Uninvested cash carries forward at face value.