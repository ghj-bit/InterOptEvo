## Turn 1 - Generic Agent

QUESTION: When the second investment matures after two years, is the 2 yuan per 1 yuan figure the total amount you receive back (i.e., 1 yuan principal plus 1 yuan profit), or is it 2 yuan of profit on top of the 1 yuan principal (i.e., 3 yuan total returned)?

## Turn 1 - User Simulator

It is 2 yuan of profit on top of the 1 yuan principal, so the total returned is 3 yuan.

## Turn 2 - Generic Agent

QUESTION: For the first investment, is the 0.7 yuan per 1 yuan figure the total amount returned after one year (i.e., 1.7 yuan total), or is it 0.7 yuan of profit on top of the 1 yuan principal (i.e., 1.7 yuan total returned)?

## Turn 2 - User Simulator

It is 0.7 yuan of profit on top of the 1 yuan principal, so the total returned is 1.7 yuan.

## Turn 3 - Generic Agent

QUESTION: When an investment matures, can the returned amount (principal plus profit) be reinvested into either option in the following year, or must it be withdrawn and kept as cash?

## Turn 3 - User Simulator

The returned amount can be reinvested into either option in the following year.

## Turn 4 - Generic Agent

QUESTION: At the end of year 3, is the goal to maximize the total cash on hand (including any matured investments), or is there a different objective such as maximizing profit or meeting a target amount?

## Turn 4 - User Simulator

The goal is to maximize the total cash on hand at the end of year 3, including any matured investments.

## Turn 5 - Generic Agent

QUESTION: Can the second investment be started in year 3 (so it would mature in year 5, after the horizon ends), or can it only be started in years where it will fully mature within the three-year horizon (i.e., only in year 1 or year 2)?

## Turn 5 - User Simulator

The second investment can only be started in years where it will fully mature within the three-year horizon, so it can only be started in year 1 or year 2.

## Turn 6 - Generic Agent

QUESTION: Can the second investment be started in year 2 (maturing at the end of year 4, which is after the three-year horizon ends), or can it only be started in year 1 (maturing at the end of year 2)?

## Turn 6 - User Simulator

The second investment can only be started in year 1, maturing at the end of year 2.

## Turn 7 - Generic Agent

QUESTION: Can the first investment be started in any of the three years (year 1, year 2, or year 3), or are there restrictions on when it can be initiated?

## Turn 7 - User Simulator

The first investment can be started in any of the three years (year 1, year 2, or year 3).

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how much can be invested in each option in a given year, or can any amount (up to available cash) be invested in each option?

## Turn 8 - User Simulator

There is no limit on how much can be invested in each option in a given year, other than the available cash.

## Turn 9 - Generic Agent

QUESTION: Can the investment amounts be any continuous value (e.g., 12,345.67 yuan), or must they be in whole yuan or some other discrete unit?

## Turn 9 - User Simulator

The investment amounts can be any continuous value.

## Turn 10 - Generic Agent

QUESTION: If cash is left uninvested in any year, does it simply carry over to the next year with no interest or return, or does it earn some return while sitting idle?

## Turn 10 - User Simulator

Cash left uninvested simply carries over to the next year with no interest or return.

## Turn 11 - Generic Agent

QUESTION: At the end of year 3, if the first investment started in year 3 has not yet matured (it matures at the end of year 4), is it counted in the total cash on hand at the end of year 3, or only investments that have fully matured by the end of year 3 are counted?

## Turn 11 - User Simulator

Only investments that have fully matured by the end of year 3 are counted in the total cash on hand.

## Turn 12 - Generic Agent

QUESTION: Since the first investment started in year 3 matures at the end of year 4 (after the horizon), and only matured investments count at the end of year 3, does that mean investing in the first option in year 3 is pointless (since it won't mature in time), or is there some other way to count it?

## Turn 12 - User Simulator

Investing in the first option in year 3 is pointless for the purpose of maximizing cash on hand at the end of year 3, since it will not mature within the horizon.

## Turn 13 - Generic Agent

QUESTION: Can the second investment be started in year 2 (maturing at the end of year 4, after the horizon), or is it restricted to only year 1 as you previously stated?

## Turn 13 - User Simulator

It is restricted to only year 1.

## Turn 14 - Generic Agent

QUESTION: Is there any minimum or maximum number of times the first investment can be started across the three years, or can it be started zero, one, two, or three times (once per year) as needed?

## Turn 14 - User Simulator

The first investment can be started zero, one, two, or three times (once per year) as needed.

## Turn 15 - Generic Agent

QUESTION: When the second investment matures at the end of year 2, can the returned amount (3 yuan per 1 yuan invested) be reinvested in the first investment in year 3, or must it be held as cash?

## Turn 15 - User Simulator

The returned amount can be reinvested in the first investment in year 3.

## Turn 16 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment again in year 2 (maturing at end of year 3)?

## Turn 16 - User Simulator

Yes, the returned amount from the first investment started in year 1 can be reinvested in the first investment again in year 2.

## Turn 17 - Generic Agent

QUESTION: Can the first investment started in year 2 (maturing at end of year 3) have its returned amount counted in the total cash on hand at the end of year 3?

## Turn 17 - User Simulator

Yes, the returned amount from the first investment started in year 2 is counted in the total cash on hand at the end of year 3.

## Turn 18 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 18 - User Simulator

Yes, the returned amount from the first investment started in year 1 can be reinvested in the first investment in year 3.

## Turn 19 - Generic Agent

QUESTION: Can the first investment started in year 2 (maturing at end of year 3) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 19 - User Simulator

No, the first investment started in year 2 matures at the end of year 3, so its returned amount is available at the end of year 3 and cannot be reinvested in year 3.

## Turn 20 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 2 (maturing at end of year 3), and then that year-2 investment's returned amount also reinvested in the first investment in year 3 (maturing at end of year 4)?

## Turn 20 - User Simulator

No. The first investment started in year 1 matures at the end of year 2, so its returned amount can be reinvested in year 2. However, the year-2 investment matures at the end of year 3, so its returned amount is available at the end of year 3 and cannot be reinvested in year 3.

## Turn 21 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 21 - User Simulator

Yes, the returned amount from the first investment started in year 1 can be reinvested in the first investment in year 3.

## Turn 22 - Generic Agent

QUESTION: Can the first investment started in year 2 (maturing at end of year 3) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 22 - User Simulator

No, the first investment started in year 2 matures at the end of year 3, so its returned amount is available at the end of year 3 and cannot be reinvested in year 3.

## Turn 23 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 2 (maturing at end of year 3), and then that year-2 investment's returned amount be counted in the total cash on hand at the end of year 3?

## Turn 23 - User Simulator

Yes, the returned amount from the first investment started in year 1 can be reinvested in the first investment in year 2, and that year-2 investment's returned amount is counted in the total cash on hand at the end of year 3.

## Turn 24 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon), and then that year-3 investment's returned amount be counted in the total cash on hand at the end of year 3?

## Turn 24 - User Simulator

No, the first investment started in year 3 matures at the end of year 4, so its returned amount is not counted in the total cash on hand at the end of year 3.

## Turn 25 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 2 (maturing at end of year 3), and then that year-2 investment's returned amount be reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 25 - User Simulator

No. The first investment started in year 2 matures at the end of year 3, so its returned amount is available at the end of year 3 and cannot be reinvested in year 3.

## Turn 26 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon), and then that year-3 investment's returned amount be counted in the total cash on hand at the end of year 4?

## Turn 26 - User Simulator

The three-year horizon ends at the end of year 3, so the total cash on hand at the end of year 4 is not part of the objective.

## Turn 27 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 27 - User Simulator

Yes, the returned amount from the first investment started in year 1 can be reinvested in the first investment in year 3.

## Turn 28 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 2 (maturing at end of year 3), and then that year-2 investment's returned amount be reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon)?

## Turn 28 - User Simulator

No. The first investment started in year 2 matures at the end of year 3, so its returned amount is available at the end of year 3 and cannot be reinvested in year 3.

## Turn 29 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 3 (maturing at end of year 4, after the horizon), and then that year-3 investment's returned amount be counted in the total cash on hand at the end of year 3?

## Turn 29 - User Simulator

No, the first investment started in year 3 matures at the end of year 4, so its returned amount is not counted in the total cash on hand at the end of year 3.

## Turn 30 - Generic Agent

QUESTION: Can the first investment started in year 1 (maturing at end of year 2) have its returned amount reinvested in the first investment in year 2 (maturing at end of year 3), and then that year-2 investment's returned amount be counted in the total cash on hand at the end of year 3?

## Turn 30 - User Simulator

Yes, the returned amount from the first investment started in year 1 can be reinvested in the first investment in year 2, and that year-2 investment's returned amount is counted in the total cash on hand at the end of year 3.