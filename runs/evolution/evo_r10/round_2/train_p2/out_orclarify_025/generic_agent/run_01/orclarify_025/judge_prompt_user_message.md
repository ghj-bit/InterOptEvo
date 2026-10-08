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

QUESTION: When you say the first investment "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean that 1 yuan invested at the start of a year becomes 1.7 yuan (principal plus 0.7 profit) at the end of that year, or that it becomes 0.7 yuan total (i.e., a loss of principal)?

## Turn 1 - User Simulator

It becomes 1.7 yuan total (principal plus 0.7 profit) at the end of that year.

## Turn 2 - Generic Agent

QUESTION: For the second investment, does 1 yuan invested at the start of a year become 3 yuan total (principal plus 2 profit) at the end of two years, or does it become 2 yuan total?

## Turn 2 - User Simulator

It becomes 3 yuan total (principal plus 2 profit) at the end of two years.

## Turn 3 - Generic Agent

QUESTION: Can money that matures from an investment be reinvested in either option in later years, or is the 100,000 yuan the only money that can ever be invested (i.e., no reinvestment of returns)?

## Turn 3 - User Simulator

Money that matures from an investment can be reinvested in either option in later years.

## Turn 4 - Generic Agent

QUESTION: The second investment must be held for a period that is a multiple of two years — does this mean it can be held for exactly 2 years, or could it also be held for 4 years (or more) within the three-year horizon?

## Turn 4 - User Simulator

It can be held for exactly 2 years.

## Turn 5 - Generic Agent

QUESTION: Is the goal to maximize the total amount of money available at the end of year 3, and is any money that has not matured by the end of year 3 (for example, money still locked in a two-year investment that started in year 2) simply lost or not counted?

## Turn 5 - User Simulator

Yes, the goal is to maximize the total amount of money available at the end of year 3. Money that has not matured by the end of year 3 is not counted.

## Turn 6 - Generic Agent

QUESTION: Can the first investment be made in any of the three years (year 1, year 2, or year 3), or is it only available in year 1?

## Turn 6 - User Simulator

The first investment can be made in any of the three years (year 1, year 2, or year 3).

## Turn 7 - Generic Agent

QUESTION: Can the second investment be started in year 1 or year 2 (maturing at the end of year 2 or year 3 respectively), or is it only available in year 1?

## Turn 7 - User Simulator

The second investment can be started in year 1 or year 2.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how much can be invested in either option in a given year, other than the available cash on hand at that time?

## Turn 8 - User Simulator

No, there is no limit on how much can be invested in either option in a given year, other than the available cash on hand at that time.

## Turn 9 - Generic Agent

QUESTION: Is it allowed to hold cash (i.e., not invest all available money) in any year, or must all available cash be fully invested each year?

## Turn 9 - User Simulator

It is allowed to hold cash (i.e., not invest all available money) in any year.

## Turn 10 - Generic Agent

QUESTION: Does cash that is held (not invested) earn any interest or return, or does it remain at face value until it is invested or the horizon ends?

## Turn 10 - User Simulator

Cash that is held (not invested) remains at face value until it is invested or the horizon ends.

## Turn 11 - Generic Agent

QUESTION: At the end of year 3, does money from a first investment made in year 3 (which matures at the end of year 3) count toward the final total, or does "end of year 3" mean only money that has matured by the end of year 2?

## Turn 11 - User Simulator

Money from a first investment made in year 3 (which matures at the end of year 3) counts toward the final total.

## Turn 12 - Generic Agent

QUESTION: Is there any minimum or maximum investment amount per transaction, or can any continuous (fractional) amount be invested in either option?

## Turn 12 - User Simulator

Any continuous (fractional) amount can be invested in either option.

## Turn 13 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Horizon:** 3 years (year 1, year 2, year 3).
- **Initial capital:** 100,000 yuan at the start of year 1.
- **Investment Option 1:** Can be made in any year (1, 2, or 3). 1 yuan invested at the start of a year becomes 1.7 yuan at the end of that year (70% return).
- **Investment Option 2:** Can be started in year 1 or year 2 only. 1 yuan invested at the start of a year becomes 3 yuan at the end of two years (200% return over 2 years). Must be held for exactly 2 years.
- **Reinvestment:** Money that matures can be reinvested in either option in subsequent years.
- **Cash holding:** Allowed; cash earns no interest (stays at face value).
- **No per-transaction limits** other than available cash.
- **Continuous (fractional) amounts** can be invested.
- **Objective:** Maximize total money available at the end of year 3.
- **End-of-year-3 counting:** Money from Option 1 started in year 3 (maturing end of year 3) counts. Money from Option 2 started in year 2 (maturing end of year 3) counts. Money from Option 2 started in year 1 (maturing end of year 2) counts if reinvested or held as cash. Any money still locked in an investment that has not matured by end of year 3 does not count (but given the available start times, all investments started in years 1 or 2 will have matured by end of year 3).