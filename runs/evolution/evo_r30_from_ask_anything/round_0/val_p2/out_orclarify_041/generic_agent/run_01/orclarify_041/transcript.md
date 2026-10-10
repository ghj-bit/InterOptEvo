## Turn 1 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the four products?

## Turn 1 - User Simulator

No, there is no minimum investment amount required for any of the four products.

## Turn 2 - Generic Agent

QUESTION: Can the funds received from maturing investments be immediately reinvested in other products available at that same point in time?

## Turn 2 - User Simulator

Yes. At the beginning of each year, you can invest the cash you have at that moment, which includes proceeds from investments that have already matured.

## Turn 3 - Generic Agent

QUESTION: Is it possible to hold uninvested cash (idle funds) from one year to the next without earning any interest?

## Turn 3 - User Simulator

Yes, it is possible to hold uninvested cash from one year to the next without earning any interest.

## Turn 4 - Generic Agent

QUESTION: Are there any transaction fees, taxes, or other costs associated with investing in or redeeming these products?

## Turn 4 - User Simulator

No, there are no transaction fees, taxes, or other costs associated with investing in or redeeming these products.

## Turn 5 - Generic Agent

READY_TO_MODEL

I have a clear understanding of your investment planning problem. Here is a summary of the confirmed details:

**Objective:**
Maximize the total cash (principal plus interest) available at the end of Year 3.

**Initial Capital:**
500,000 yuan at the beginning of Year 1.

**Investment Products:**
1.  **Product 1:** 1-year term. Available at the beginning of Years 1, 2, and 3. Returns 1.20x the investment at the end of that year. No capacity limit.
2.  **Product 2:** 2-year term. Available only at the beginning of Year 1. Matures at the end of Year 2. Returns 1.50x the investment. Capacity limit: 120,000 yuan.
3.  **Product 3:** 1-year term (same-year). Available only at the beginning of Year 2. Matures at the end of Year 2. Returns 1.60x the investment. Capacity limit: 150,000 yuan.
4.  **Product 4:** 1-year term. Available only at the beginning of Year 3. Matures at the end of Year 3. Returns 1.40x the investment. Capacity limit: 100,000 yuan.

**Constraints & Rules:**
*   Investments in Products 2, 3, and 4 are capped at 120,000, 150,000, and 100,000 yuan, respectively.
*   There are no minimum investment amounts.
*   Proceeds from maturing investments can be immediately reinvested in products available at that time.
*   Uninvested cash can be held idle (earning 0% interest) from one period to the next.
*   There are no transaction fees, taxes, or other costs.