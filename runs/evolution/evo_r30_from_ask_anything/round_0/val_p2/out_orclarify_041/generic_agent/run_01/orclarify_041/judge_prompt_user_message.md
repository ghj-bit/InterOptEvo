# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U9, U11, U2, U3, U4, U6, U8
I need help creating an investment plan over the next three years, with the objective to maximize total principal plus interest at the end of Year 3. However, investment in product (2) cannot exceed 120,000 yuan, investment in product (3) cannot exceed 150,000 yuan, and investment in product (4) cannot exceed 100,000 yuan.

Initial capital at beginning of Year 1: 500,000 yuan.

Investment projects:
(1) A 1-year product available at the beginning of each year (Years 1–3). If you invest I at the start of a year, you receive 1.20·I at that year’s end. Unlimited capacity.
(2) A 2-year product available only at the beginning of Year 1; it matures at the end of Year 2 and pays 1.50·I. Investment in this product is capped at 120,000 yuan.
(3) A same-year product available at the beginning of Year 2, maturing at the end of Year 2, and paying 1.60·I. Investment is capped at 150,000 yuan.
(4) A 1-year product available at the beginning of Year 3, maturing at the end of Year 3, and paying 1.40·I. Investment is capped at 100,000 yuan.

Maximum allowable investment for project (2): 120,000 yuan.

Maximum allowable investment for project (3): 150,000 yuan.

Maximum allowable investment for project (4): 100,000 yuan.

## Problem units
- U1 (context): I need help creating an investment plan over the next three years that maximizes my total wealth at the end.
- U2 (data): Initial capital at beginning of Year 1: 500,000 yuan.
- U3 (data): Investment projects:
(1) A 1-year product available at the beginning of each year (Years 1–3). If you invest I at the start of a year, you receive 1.20·I at that year’s end. Unlimited capacity.
(2) A 2-year product available only at the beginning of Year 1; it matures at the end of Year 2 and pays 1.50·I. Investment in this product is capped at 120,000 yuan.
(3) A same-year product available at the beginning of Year 2, maturing at the end of Year 2, and paying 1.60·I. Investment is capped at 150,000 yuan.
(4) A 1-year product available at the beginning of Year 3, maturing at the end of Year 3, and paying 1.40·I. Investment is capped at 100,000 yuan.
- U4 (data): Maximum allowable investment for project (2): 120,000 yuan.
- U5 (constraint): Investment in product (2) cannot exceed 120,000 yuan.
- U6 (data): Maximum allowable investment for project (3): 150,000 yuan.
- U7 (constraint): Investment in product (3) cannot exceed 150,000 yuan.
- U8 (data): Maximum allowable investment for project (4): 100,000 yuan.
- U9 (constraint): Investment in product (4) cannot exceed 100,000 yuan.
- U10 (constraint): No borrowing allowed; decisions are made at the beginnings of Years 1–3 using only currently available cash (initial capital and proceeds from matured investments).
- U11 (objective): Maximize total principal plus interest at the end of Year 3.

## Hidden slot scoring rules
## H1: no_borrowing_cash_only
- Severity: P1
- Severity reason: Without this constraint, the agent may assume borrowing is allowed, leading to a materially incorrect cash-flow model that overestimates available funds and yields an investment plan different from the intended problem.
- Problem unit ID: U10
- Semantic hit rule: The agent's question must explicitly ask about whether borrowing is allowed, or about the restriction that only cash on hand (initial capital and matured proceeds) can be used for investments.
- Reference acceptable questions:
  - Is borrowing allowed, or can we only use the cash we already have?
  - Are we permitted to take out loans, or must we invest strictly from the initial capital and any returns we receive?
- Failure modes:
  - Assuming unlimited borrowing is possible at zero interest
  - Assuming the agent can carry a negative cash balance to invest more


# Full Transcript

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