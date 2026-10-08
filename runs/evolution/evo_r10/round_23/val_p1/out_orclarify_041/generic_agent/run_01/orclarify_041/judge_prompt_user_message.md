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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand from all investments that have matured by then, or should any funds that were not invested (left idle) also count toward that total?

## Turn 1 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes all proceeds from investments that have matured by then, as well as any funds that were not invested and were left idle.

## Turn 2 - Generic Agent

QUESTION: If you invest in the 1-year product (1) at the beginning of Year 2 or Year 3, does it mature at the end of that same year (so Year 2 money is available to invest in Year 3, but Year 3 money is not reinvested before the end of Year 3)?

## Turn 2 - User Simulator

Yes, that is correct. If you invest in product (1) at the beginning of Year 2, it matures at the end of Year 2, and the proceeds are available to invest at the beginning of Year 3. If you invest in product (1) at the beginning of Year 3, it matures at the end of Year 3, and the proceeds count toward the final total wealth at the end of Year 3.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much can be invested in product (1) in any given year, or is it truly unlimited as stated?

## Turn 3 - User Simulator

Product (1) has unlimited capacity. There is no limit on how much can be invested in it in any given year.

## Turn 4 - Generic Agent

QUESTION: Can you invest in product (1) at the beginning of Year 1, Year 2, and Year 3, or is it only available in certain years?

## Turn 4 - User Simulator

Product (1) is available at the beginning of each year, so you can invest in it at the beginning of Year 1, Year 2, and Year 3.

## Turn 5 - Generic Agent

QUESTION: Are there any minimum investment amounts for any of the products, or can you invest any amount (including zero) in each product?

## Turn 5 - User Simulator

There are no minimum investment amounts. You can invest any amount, including zero, in each product.

## Turn 6 - Generic Agent

QUESTION: Are there any transaction costs, fees, or taxes associated with investing in any of the products, or are the returns stated (1.20, 1.50, 1.60, 1.40) the net amounts you actually receive?

## Turn 6 - User Simulator

The returns stated (1.20, 1.50, 1.60, 1.40) are the net amounts you actually receive. There are no transaction costs, fees, or taxes associated with investing in any of the products.

## Turn 7 - Generic Agent

QUESTION: Can you invest in product (2) at the beginning of Year 2 or Year 3, or is it only available at the beginning of Year 1 as stated?

## Turn 7 - User Simulator

Product (2) is only available at the beginning of Year 1.

## Turn 8 - Generic Agent

QUESTION: Can you invest in product (3) at the beginning of Year 1 or Year 3, or is it only available at the beginning of Year 2 as stated?

## Turn 8 - User Simulator

Product (3) is only available at the beginning of Year 2.

## Turn 9 - Generic Agent

QUESTION: Can you invest in product (4) at the beginning of Year 1 or Year 2, or is it only available at the beginning of Year 3 as stated?

## Turn 9 - User Simulator

Product (4) is only available at the beginning of Year 3.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on the total amount you can invest across all products in a single year, or is the only constraint the individual product caps?

## Turn 10 - User Simulator

There is no limit on the total amount you can invest across all products in a single year. The only constraints are the individual product caps and the requirement that you cannot borrow; you can only invest the cash you have available at the beginning of that year.

## Turn 11 - Generic Agent

QUESTION: If you have cash available at the beginning of a year that you do not invest in any product, does it simply carry over to the next year unchanged (i.e., no interest earned on idle cash)?

## Turn 11 - User Simulator

Yes, any cash not invested at the beginning of a year carries over to the next year unchanged. No interest is earned on idle cash.

## Turn 12 - Generic Agent

QUESTION: Is there any requirement that you must invest all available cash at the beginning of each year, or are you free to leave some or all of it idle?

## Turn 12 - User Simulator

You are free to leave some or all of your available cash idle at the beginning of each year. There is no requirement to invest all available cash.

## Turn 13 - Generic Agent

QUESTION: At the end of Year 3, does the final total cash on hand include the proceeds from product (1) invested at the beginning of Year 3, product (4) invested at the beginning of Year 3, and any idle cash carried into Year 3, all combined?

## Turn 13 - User Simulator

Yes, the final total cash on hand at the end of Year 3 includes the proceeds from product (1) invested at the beginning of Year 3, the proceeds from product (4) invested at the beginning of Year 3, and any idle cash carried into Year 3, all combined.

## Turn 14 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of Year 3, which includes proceeds from all investments that mature by then plus any idle cash carried into Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Products:**
- **Product (1):** 1-year, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at year-end. Unlimited capacity.
- **Product (2):** 2-year, available only at the beginning of Year 1. Matures at end of Year 2, returns 1.50×I. Capped at 120,000 yuan.
- **Product (3):** Same-year, available only at the beginning of Year 2. Matures at end of Year 2, returns 1.60×I. Capped at 150,000 yuan.
- **Product (4):** 1-year, available only at the beginning of Year 3. Matures at end of Year 3, returns 1.40×I. Capped at 100,000 yuan.

**Constraints:**
- No borrowing: investments in any year cannot exceed cash available at the beginning of that year.
- Individual product caps as stated (120k, 150k, 100k).
- No minimum investment amounts; zero investment is allowed.
- No transaction costs, fees, or taxes; stated returns are net.
- Idle cash carries over unchanged (no interest).
- No total annual investment limit beyond individual caps and available cash.

**Cash flow structure:**
- Beginning of Year 1: 500,000 available. Can invest in products (1) and (2).
- End of Year 1: Product (1) Year-1 proceeds (1.20×) + idle cash available.
- Beginning of Year 2: Can invest in products (1) and (3).
- End of Year 2: Product (1) Year-2 proceeds (1.20×), product (2) proceeds (1.50×), product (3) proceeds (1.60×), plus idle cash available.
- Beginning of Year 3: Can invest in products (1) and (4).
- End of Year 3: Product (1) Year-3 proceeds (1.20×), product (4) proceeds (1.40×), plus idle cash = final total cash on hand.