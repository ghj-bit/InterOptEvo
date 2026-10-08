## Turn 1 - Generic Agent

QUESTION: For the first investment option, is the 0.7 yuan return a simple interest paid at the end of year 1 (so 1 yuan becomes 1.7 yuan), or is it a compound rate applied each year?

## Turn 1 - User Simulator

It is a simple return paid at the end of year 1. So, 1 yuan invested becomes 1.7 yuan after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment option, is the 2 yuan return a simple return paid at the end of year 2 (so 1 yuan becomes 3 yuan), or is it a compound rate applied each year?

## Turn 2 - User Simulator

It is a simple return paid at the end of year 2. So, 1 yuan invested becomes 3 yuan after two years.

## Turn 3 - Generic Agent

QUESTION: When you say the second investment must be held for a period that is a multiple of two years, does that mean you can only invest in it at the start of year 1 (held 2 years, maturing at end of year 2) and at the start of year 3 (held 2 years, maturing at end of year 4), or can you also invest at the start of year 2 (held 2 years, maturing at end of year 4)?

## Turn 3 - User Simulator

You can invest in the second option at the start of year 1 (maturing at end of year 2) and at the start of year 2 (maturing at end of year 4).

## Turn 4 - Generic Agent

QUESTION: Since the second investment can mature at the end of year 4, which is beyond the three-year horizon, should the objective be to maximize the total wealth at the end of year 3 (counting any second-investment funds still locked in as their face value), or should we instead maximize wealth at the end of year 4 when all investments have matured?

## Turn 4 - User Simulator

The objective is to maximize the total amount of money the investor has at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: At the end of year 3, any second-investment funds still locked in (invested at the start of year 2, maturing at end of year 4) — should these be counted in the objective at their original face value (1 yuan per 1 yuan invested), or at some other value?

## Turn 5 - User Simulator

They should be counted at their original face value.

## Turn 6 - Generic Agent

QUESTION: Can money that matures from an investment be reinvested in either option in subsequent years, or is the initial 100,000 yuan the only capital that can be invested?

## Turn 6 - User Simulator

Money that matures from an investment can be reinvested in either option in subsequent years.

## Turn 7 - Generic Agent

QUESTION: Can money be left uninvested (i.e., held as cash) between years, or must all available funds be invested in one of the two options at the start of each year?

## Turn 7 - User Simulator

Money can be left uninvested and held as cash between years.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on the amount that can be invested in either option in a given year, or can any amount (up to available funds) be invested in each option?

## Turn 8 - User Simulator

There is no limit on the amount that can be invested in either option in a given year, other than the available funds.