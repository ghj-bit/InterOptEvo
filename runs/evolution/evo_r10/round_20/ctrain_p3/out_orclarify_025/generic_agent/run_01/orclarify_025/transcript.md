## Turn 1 - Generic Agent

QUESTION: When the second investment matures after two years, is the 2 yuan per 1 yuan the total amount you receive back (i.e., 1 yuan principal plus 1 yuan profit), or is it 2 yuan of profit on top of the 1 yuan principal (i.e., 3 yuan total returned)?

## Turn 1 - User Simulator

It is 2 yuan of profit on top of the 1 yuan principal, so the total returned is 3 yuan.

## Turn 2 - Generic Agent

QUESTION: For the first investment, when it matures after one year and returns 0.7 yuan per 1 yuan invested, is that 0.7 yuan the total amount returned (i.e., you get 0.7 yuan back and lose your principal), or is it 0.7 yuan of profit on top of the 1 yuan principal (i.e., you get 1.7 yuan back)?

## Turn 2 - User Simulator

It is 0.7 yuan of profit on top of the 1 yuan principal, so you get 1.7 yuan back.

## Turn 3 - Generic Agent

QUESTION: At the end of the three-year horizon, what exactly are you trying to maximize — the total cash you have on hand at the end of year 3 (counting any matured investments plus any cash you never invested), or something else such as total profit earned over the three years?

## Turn 3 - User Simulator

I am trying to maximize the total amount of money the investor has at the end of the third year.

## Turn 4 - Generic Agent

QUESTION: When an investment matures and returns cash, can that returned cash be reinvested into either option at that point in time (for example, money returned at the end of year 1 reinvested in year 2, or money returned at the end of year 2 reinvested in year 3)?

## Turn 4 - User Simulator

Yes, returned cash can be reinvested into either option at that point in time.

## Turn 5 - Generic Agent

QUESTION: The second investment must be held for a period that is a multiple of two years. Does this mean it can be held for 2 years, 4 years, 6 years, etc. (with the return compounding or repeating for each 2-year block), or does it simply mean it must be held for exactly 2 years (the only multiple of 2 that fits within the 3-year horizon)?

## Turn 5 - User Simulator

It simply means it must be held for exactly 2 years, as that is the only multiple of 2 that fits within the 3-year horizon.

## Turn 6 - Generic Agent

QUESTION: Can the investment amounts be any continuous (fractional) values, or must they be whole yuan amounts (integers)?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: At the end of year 3, if you have cash that was not invested (or cash returned from an investment that matures exactly at the end of year 3), does that cash count toward your final total, or must all money be locked in an investment at the end of year 3?

## Turn 7 - User Simulator

Yes, that cash counts toward the final total.

## Turn 8 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 2 (i.e., at the end of year 1), so that it matures at the end of year 3?

## Turn 8 - User Simulator

Yes, you can invest in the second option at the start of year 2, so that it matures at the end of year 3.

## Turn 9 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 3 (i.e., at the end of year 2), so that it matures at the end of year 3?

## Turn 9 - User Simulator

Yes, you can invest in the first option at the start of year 3, so that it matures at the end of year 3.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how much you can invest in each option at any given time, or is the only constraint the total cash available at that point in time?

## Turn 10 - User Simulator

The only constraint is the total cash available at that point in time.

## Turn 11 - Generic Agent

QUESTION: Are there any transaction costs, minimum investment amounts, or other fees associated with either investment option?

## Turn 11 - User Simulator

No, there are no transaction costs, minimum investment amounts, or other fees associated with either investment option.

## Turn 12 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (i.e., at time 0), so that it matures at the end of year 1?

## Turn 12 - User Simulator

Yes, you can invest in the first option at the start of year 1, so that it matures at the end of year 1.

## Turn 13 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 1 (i.e., at time 0), so that it matures at the end of year 2?

## Turn 13 - User Simulator

Yes, you can invest in the second option at the start of year 1, so that it matures at the end of year 2.

## Turn 14 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 2 (i.e., at the end of year 1), so that it matures at the end of year 2?

## Turn 14 - User Simulator

Yes, you can invest in the first option at the start of year 2, so that it matures at the end of year 2.

## Turn 15 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (time 0) and, when it matures at the end of year 1, reinvest that returned cash into the first option again at the start of year 2?

## Turn 15 - User Simulator

Yes

## Turn 16 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 2 (end of year 1) and, when it matures at the end of year 2, reinvest that returned cash into the first option again at the start of year 3?

## Turn 16 - User Simulator

Yes

## Turn 17 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 1 (time 0), and when it matures at the end of year 2, reinvest that returned cash into the second option again at the start of year 3?

## Turn 17 - User Simulator

No

## Turn 18 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 1 (time 0), and when it matures at the end of year 2, reinvest that returned cash into the first option at the start of year 3?

## Turn 18 - User Simulator

Yes

## Turn 19 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 2 (end of year 1), and when it matures at the end of year 3, reinvest that returned cash into the first option at the start of year 3?

## Turn 19 - User Simulator

No

## Turn 20 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 2 (end of year 1), and when it matures at the end of year 3, reinvest that returned cash into the second option again at the start of year 3?

## Turn 20 - User Simulator

No

## Turn 21 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (time 0), and when it matures at the end of year 1, reinvest that returned cash into the second option at the start of year 2?

## Turn 21 - User Simulator

Yes

## Turn 22 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 2 (end of year 1), and when it matures at the end of year 2, reinvest that returned cash into the second option at the start of year 3?

## Turn 22 - User Simulator

No

## Turn 23 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 3 (end of year 2), and when it matures at the end of year 3, reinvest that returned cash into the first option again at the start of year 3?

## Turn 23 - User Simulator

No

## Turn 24 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 3 (end of year 2), and when it matures at the end of year 3, reinvest that returned cash into the second option at the start of year 3?

## Turn 24 - User Simulator

No

## Turn 25 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 2 (end of year 1), and when it matures at the end of year 3, reinvest that returned cash into the first option at the start of year 3?

## Turn 25 - User Simulator

No

## Turn 26 - Generic Agent

QUESTION: Can you invest in the second option at the start of year 2 (end of year 1), and when it matures at the end of year 3, reinvest that returned cash into the second option at the start of year 3?

## Turn 26 - User Simulator

No

## Turn 27 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (time 0), and when it matures at the end of year 1, reinvest that returned cash into the first option at the start of year 2, and then when that matures at the end of year 2, reinvest into the first option at the start of year 3?

## Turn 27 - User Simulator

Yes

## Turn 28 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (time 0), and when it matures at the end of year 1, reinvest that returned cash into the second option at the start of year 2, and then when that matures at the end of year 3, reinvest into the first option at the start of year 3?

## Turn 28 - User Simulator

No

## Turn 29 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (time 0), and when it matures at the end of year 1, reinvest that returned cash into the second option at the start of year 2, and then when that matures at the end of year 3, reinvest into the second option at the start of year 3?

## Turn 29 - User Simulator

No

## Turn 30 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 1 (time 0), and when it matures at the end of year 1, reinvest that returned cash into the first option at the start of year 2, and then when that matures at the end of year 2, reinvest into the second option at the start of year 3?

## Turn 30 - User Simulator

No