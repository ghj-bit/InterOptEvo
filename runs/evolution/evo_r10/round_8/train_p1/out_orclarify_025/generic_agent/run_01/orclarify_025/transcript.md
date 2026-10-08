## Turn 1 - Generic Agent

QUESTION: When you say the first investment "guarantees a return of 0.7 yuan for every 1 yuan invested after one year," do you mean that after one year you receive back 1.7 yuan total (your 1 yuan principal plus 0.7 yuan profit), or that you receive only 0.7 yuan total (losing 0.3 yuan of principal)?

## Turn 1 - User Simulator

I mean that after one year you receive back 1.7 yuan total (your 1 yuan principal plus 0.7 yuan profit).

## Turn 2 - Generic Agent

QUESTION: For the second investment, does "a return of 2 yuan for every 1 yuan invested after two years" mean that after two years you receive back 3 yuan total (your 1 yuan principal plus 2 yuan profit), consistent with how you described the first investment?

## Turn 2 - User Simulator

Yes, after two years you receive back 3 yuan total (your 1 yuan principal plus 2 yuan profit).

## Turn 3 - Generic Agent

QUESTION: At the end of year 3, is the goal to maximize the total amount of money you have (principal plus all profits), or to maximize only the total profit earned over the three years?

## Turn 3 - User Simulator

The goal is to maximize the total amount of money you have (principal plus all profits) at the end of year 3.

## Turn 4 - Generic Agent

QUESTION: When the first investment matures after one year and you receive 1.7 yuan per yuan invested, can you reinvest that money into either investment option in the following year, or must it be held as cash?

## Turn 4 - User Simulator

You can reinvest that money into either investment option in the following year.

## Turn 5 - Generic Agent

QUESTION: Can you invest in the second option in year 2 (so it matures at the end of year 4, after the three-year horizon ends), or can you only invest in it in year 1 (so it matures at the end of year 2, within the horizon)?

## Turn 5 - User Simulator

You can only invest in the second option in year 1, so it matures at the end of year 2, within the horizon.

## Turn 6 - Generic Agent

QUESTION: If you hold cash (uninvested money) at the end of year 3, does it count toward your total amount of money, or must all money be invested by the end of the horizon?

## Turn 6 - User Simulator

Cash held at the end of year 3 counts toward your total amount of money.

## Turn 7 - Generic Agent

QUESTION: Can you invest in the first option in year 2 (so it matures at the end of year 3, within the horizon), or is the first option only available in year 1?

## Turn 7 - User Simulator

You can invest in the first option in year 2, so it matures at the end of year 3, within the horizon.

## Turn 8 - Generic Agent

QUESTION: Can you invest in the first option in year 3 (so it would mature at the end of year 4, after the horizon ends), or is the first option only available in years 1 and 2?

## Turn 8 - User Simulator

The first option is only available in years 1 and 2.

## Turn 9 - Generic Agent

QUESTION: Can you invest in the first option multiple times within the same year (for example, split your money into several first-option investments in year 1), or is each investment option limited to one investment per year?

## Turn 9 - User Simulator

You can invest in the first option multiple times within the same year.

## Turn 10 - Generic Agent

QUESTION: Are the investment amounts continuous (you can invest any fractional amount of yuan), or must they be in whole yuan amounts?

## Turn 10 - User Simulator

The investment amounts are continuous; you can invest any fractional amount of yuan.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how much you can invest in the second option in year 1, other than the total initial capital constraint of 100,000 yuan?

## Turn 11 - User Simulator

No, there is no limit on how much you can invest in the second option in year 1, other than the total initial capital constraint of 100,000 yuan.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on how much you can invest in the first option in year 2, other than the amount of money you have available at the start of year 2?

## Turn 12 - User Simulator

No, there is no limit on how much you can invest in the first option in year 2, other than the amount of money you have available at the start of year 2.

## Turn 13 - Generic Agent

QUESTION: Can you invest in the second option in year 2 as well (so it would mature at the end of year 4, after the horizon), or is the second option only available in year 1?

## Turn 13 - User Simulator

The second option is only available in year 1.

## Turn 14 - Generic Agent

QUESTION: When you reinvest money from the first option's year-1 maturity into the first option in year 2, does that year-2 investment also mature at the end of year 3 and count toward your final total?

## Turn 14 - User Simulator

Yes, that year-2 investment matures at the end of year 3 and counts toward your final total.

## Turn 15 - Generic Agent

QUESTION: When the second option matures at the end of year 2 and you receive 3 yuan per yuan invested, can you reinvest that money into the first option in year 3, or is the first option not available in year 3?

## Turn 15 - User Simulator

The first option is not available in year 3.

## Turn 16 - Generic Agent

QUESTION: When the second option matures at the end of year 2, can you reinvest that money into the first option in year 2 (so it matures at the end of year 3), or does the year-2 reinvestment window close before the second option's proceeds arrive?

## Turn 16 - User Simulator

You can reinvest that money into the first option in year 2, so it matures at the end of year 3.

## Turn 17 - Generic Agent

QUESTION: If you hold cash at the end of year 2 (money not reinvested into the first option in year 2), does that cash simply carry over to the end of year 3 and count toward your final total?

## Turn 17 - User Simulator

Yes, that cash simply carries over to the end of year 3 and counts toward your final total.

## Turn 18 - Generic Agent

QUESTION: Can you invest in the first option in year 1 and also in year 2 with the same initial capital, or does the year-1 investment lock up that capital until it matures at the end of year 1?

## Turn 18 - User Simulator

The year-1 investment locks up that capital until it matures at the end of year 1.

## Turn 19 - Generic Agent

QUESTION: When you invest in the first option in year 1, does the capital lock up for exactly one year (maturing at the end of year 1), or could you invest in the first option at different points within year 1 with different maturity dates?

## Turn 19 - User Simulator

The capital locks up for exactly one year, maturing at the end of year 1.

## Turn 20 - Generic Agent

QUESTION: When you invest in the second option in year 1, does the capital lock up for exactly two years (maturing at the end of year 2), or could you invest at different points within year 1 with different maturity dates?

## Turn 20 - User Simulator

The capital locks up for exactly two years, maturing at the end of year 2.

## Turn 21 - Generic Agent

QUESTION: When you invest in the first option in year 2, does the capital lock up for exactly one year (maturing at the end of year 3), or could you invest at different points within year 2 with different maturity dates?

## Turn 21 - User Simulator

The capital locks up for exactly one year, maturing at the end of year 3.

## Turn 22 - Generic Agent

QUESTION: Can you invest in the first option in year 1 and also in the second option in year 1 simultaneously, splitting your initial capital between them?

## Turn 22 - User Simulator

Yes, you can invest in the first option in year 1 and also in the second option in year 1 simultaneously, splitting your initial capital between them.

## Turn 23 - Generic Agent

QUESTION: Can you invest in the first option in year 2 and also hold cash in year 2 simultaneously, splitting your available year-2 funds between them?

## Turn 23 - User Simulator

Yes, you can invest in the first option in year 2 and also hold cash in year 2 simultaneously, splitting your available year-2 funds between them.

## Turn 24 - Generic Agent

QUESTION: Is there any minimum investment amount for either option, or can you invest any positive fractional amount?

## Turn 24 - User Simulator

There is no minimum investment amount; you can invest any positive fractional amount.

## Turn 25 - Generic Agent

QUESTION: Can you invest zero in an option (i.e., choose not to invest in it at all in a given year), or must you invest at least some positive amount in each available option each year?

## Turn 25 - User Simulator

You can invest zero in an option; you are not required to invest in each available option each year.

## Turn 26 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax associated with making an investment or receiving a return?

## Turn 26 - User Simulator

No, there are no transaction costs, fees, or taxes associated with making an investment or receiving a return.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint on the total amount you can have at the end of year 3, or is the only constraint the initial capital limit of 100,000 yuan?

## Turn 27 - User Simulator

The only constraint is the initial capital limit of 100,000 yuan.

## Turn 28 - Generic Agent

QUESTION: Can you borrow money or take on debt to invest beyond your available capital at any point during the three years?

## Turn 28 - User Simulator

No, you cannot borrow money or take on debt to invest beyond your available capital at any point during the three years.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint on the total amount you can invest in the first option across both year 1 and year 2 combined, or is the only constraint the available capital at each point in time?

## Turn 29 - User Simulator

The only constraint is the available capital at each point in time.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint on the total amount you can invest in the second option in year 1, other than the initial capital limit of 100,000 yuan?

## Turn 30 - User Simulator

No, there is no constraint on the total amount you can invest in the second option in year 1, other than the initial capital limit of 100,000 yuan.