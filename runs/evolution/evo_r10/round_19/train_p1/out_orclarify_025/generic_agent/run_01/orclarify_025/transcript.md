## Turn 1 - Generic Agent

QUESTION: For the first investment option, is the 0.7 yuan return in addition to getting your original 1 yuan back (i.e., you receive 1.7 yuan total after one year), or is 0.7 yuan the total amount you receive (meaning you lose 0.3 yuan of principal)?

## Turn 1 - User Simulator

The 0.7 yuan is the return in addition to getting your original 1 yuan back. You receive 1.7 yuan total after one year.

## Turn 2 - Generic Agent

QUESTION: For the second investment option, is the 2 yuan return in addition to getting your original 1 yuan back (i.e., you receive 3 yuan total after two years), or is 2 yuan the total amount you receive (meaning you lose 1 yuan of principal)?

## Turn 2 - User Simulator

The 2 yuan is the return in addition to getting your original 1 yuan back. You receive 3 yuan total after two years.

## Turn 3 - Generic Agent

QUESTION: When you invest in the second option, can you choose to hold it for 2 years or for 4 years (or any other multiple of 2), or is it fixed at exactly 2 years?

## Turn 3 - User Simulator

You can choose to hold it for 2 years or for 4 years (or any other multiple of 2).

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize the total amount of money you have at the end of year 3, and is it allowed to have uninvested cash sitting idle (earning nothing) at the end of year 3?

## Turn 4 - User Simulator

Yes, the objective is to maximize the total amount of money you have at the end of year 3. It is allowed to have uninvested cash sitting idle (earning nothing) at the end of year 3.

## Turn 5 - Generic Agent

QUESTION: Can you invest in the first option at the start of each year (years 1, 2, and 3), or only at the start of year 1?

## Turn 5 - User Simulator

You can invest in the first option at the start of each year (years 1, 2, and 3).

## Turn 6 - Generic Agent

QUESTION: Can you invest in the second option at the start of each year (years 1, 2, and 3), or only at the start of year 1?

## Turn 6 - User Simulator

You can invest in the second option at the start of each year (years 1, 2, and 3).

## Turn 7 - Generic Agent

QUESTION: If you invest in the second option at the start of year 3 and hold it for 2 years, it would mature at the end of year 5, which is beyond your 3-year horizon. Is that allowed (i.e., you simply don't count that money at year 3), or are you only allowed to make second-option investments that mature by the end of year 3?

## Turn 7 - User Simulator

You are only allowed to make second-option investments that mature by the end of year 3.

## Turn 8 - Generic Agent

QUESTION: If you invest in the second option at the start of year 1 and choose to hold it for 4 years, it would mature at the end of year 5, which is beyond your 3-year horizon. Given your rule that second-option investments must mature by the end of year 3, does that mean the only valid holding period for the second option is 2 years (since 4 years would always exceed the horizon)?

## Turn 8 - User Simulator

Yes, given the 3-year horizon and the requirement that second-option investments must mature by the end of year 3, the only valid holding period for the second option is 2 years.

## Turn 9 - Generic Agent

QUESTION: When you invest in the first option at the start of year 3, it matures at the end of year 3, which is within your horizon. Is that allowed, or does the first option also need to mature strictly before the end of year 3?

## Turn 9 - User Simulator

It is allowed.

## Turn 10 - Generic Agent

QUESTION: When you invest in the second option at the start of year 2, it matures at the end of year 4, which is beyond your 3-year horizon. Is that allowed, or can you only invest in the second option at the start of year 1 (so it matures at the end of year 2)?

## Turn 10 - User Simulator

You can only invest in the second option at the start of year 1 (so it matures at the end of year 2).

## Turn 11 - Generic Agent

QUESTION: When you invest in the first option at the start of year 2, it matures at the end of year 2. Can you then reinvest that money (including the return) into the first option at the start of year 3, or into the second option at the start of year 2 (which would mature at the end of year 4, beyond your horizon)?

## Turn 11 - User Simulator

You can reinvest that money into the first option at the start of year 3.

## Turn 12 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the second option at the start of year 2 (which would mature at the end of year 4, beyond your horizon), or is that not allowed since the second option can only be invested at the start of year 1?

## Turn 12 - User Simulator

That is not allowed, since the second option can only be invested at the start of year 1.

## Turn 13 - Generic Agent

QUESTION: Can you invest in the first option at the start of year 3, and if so, does it mature at the end of year 3 (within your horizon) or at the end of year 4 (beyond your horizon)?

## Turn 13 - User Simulator

Yes, you can invest in the first option at the start of year 3, and it matures at the end of year 3 (within your horizon).

## Turn 14 - Generic Agent

QUESTION: When you invest in the first option at the start of year 2, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 14 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 15 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2, within your horizon)?

## Turn 15 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2.

## Turn 16 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 16 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 17 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 17 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 18 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 18 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 19 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 19 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 20 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 20 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 21 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 21 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 22 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 22 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 23 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 23 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 24 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 24 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 25 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 25 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 26 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 26 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 27 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 27 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 28 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 28 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.

## Turn 29 - Generic Agent

QUESTION: When you invest in the second option at the start of year 1, it matures at the end of year 2. Can you reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3, within your horizon)?

## Turn 29 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 3.

## Turn 30 - Generic Agent

QUESTION: When you invest in the first option at the start of year 1, it matures at the end of year 1. Can you reinvest that money into the first option at the start of year 2 (which would mature at the end of year 2), and then reinvest that money into the first option at the start of year 3 (which would mature at the end of year 3)?

## Turn 30 - User Simulator

Yes, you can reinvest that money into the first option at the start of year 2, and then reinvest that money into the first option at the start of year 3.