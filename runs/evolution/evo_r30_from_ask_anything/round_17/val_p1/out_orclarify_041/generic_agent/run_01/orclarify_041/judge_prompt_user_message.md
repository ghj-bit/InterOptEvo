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

QUESTION: For the 1-year product (1), is the 20% return a simple annual rate applied to the principal invested at the start of that year, with no compounding or reinvestment within the year?

## Turn 1 - User Simulator

Yes. The 20% return is a simple annual rate applied to the principal invested at the start of that year. You receive 1.20 times the amount invested at the end of that year. There is no compounding or reinvestment within the year.

## Turn 2 - Generic Agent

QUESTION: For the 2-year product (2), is the 50% total return a simple return over the full two-year holding period, meaning you receive 1.50 times the principal at the end of Year 2 with no intermediate cash flows?

## Turn 2 - User Simulator

Yes. The 50% total return is a simple return over the full two-year holding period. You invest at the beginning of Year 1 and receive 1.50 times the principal at the end of Year 2, with no intermediate cash flows.

## Turn 3 - Generic Agent

QUESTION: For the same-year product (3), is the 60% return a simple return over the single-year holding period from the beginning of Year 2 to the end of Year 2, meaning you receive 1.60 times the principal at the end of Year 2?

## Turn 3 - User Simulator

Yes. The 60% return is a simple return over the single-year holding period from the beginning of Year 2 to the end of Year 2. You receive 1.60 times the principal at the end of Year 2.

## Turn 4 - Generic Agent

QUESTION: For the 1-year product (4), is the 40% return a simple return over the single-year holding period from the beginning of Year 3 to the end of Year 3, meaning you receive 1.40 times the principal at the end of Year 3?

## Turn 4 - User Simulator

Yes. The 40% return is a simple return over the single-year holding period from the beginning of Year 3 to the end of Year 3. You receive 1.40 times the principal at the end of Year 3.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts for each product and year required to be whole numbers (integer yuan), or can they be any non-negative real number?

## Turn 5 - User Simulator

The business facts do not specify whether investment amounts must be whole numbers or can be any non-negative real number. This point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, with no additional external capital or borrowing allowed during the three-year period?

## Turn 6 - User Simulator

Yes. The 500,000 yuan initial capital is the only source of funds available at the beginning of Year 1. No borrowing is allowed, and no additional external capital is available during the three-year period.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 2, is the total amount available for investment exactly equal to the sum of all cash flows received at the end of Year 1 (from product 1 investments made in Year 1), with no other sources of funds?

## Turn 7 - User Simulator

Yes. At the beginning of Year 2, the total amount available for investment is exactly equal to the sum of all cash flows received at the end of Year 1 from product (1) investments made in Year 1. There are no other sources of funds.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 3, is the total amount available for investment exactly equal to the sum of all cash flows received at the end of Year 2 (from product 1 investments made in Year 2, product 2 investments made in Year 1, and product 3 investments made in Year 2), with no other sources of funds?

## Turn 8 - User Simulator

Yes. At the beginning of Year 3, the total amount available for investment is exactly equal to the sum of all cash flows received at the end of Year 2 from:

- Product (1) investments made in Year 2,
- Product (2) investments made in Year 1, and
- Product (3) investments made in Year 2.

There are no other sources of funds.

## Turn 9 - Generic Agent

QUESTION: Is the objective to maximize the total cash value received at the end of Year 3 from all investments maturing at that time (product 1 investments made in Year 3 and product 4 investments made in Year 3), with no other cash flows or terminal value components?

## Turn 9 - User Simulator

Yes. The objective is to maximize the total cash value received at the end of Year 3 from all investments maturing at that time, which are product (1) investments made in Year 3 and product (4) investments made in Year 3. There are no other cash flows or terminal value components.

## Turn 10 - Generic Agent

QUESTION: Are there any minimum investment requirements for any of the products, or can the investment amount for any product be zero?

## Turn 10 - User Simulator

The business facts do not specify any minimum investment requirements. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as limits on the total amount invested in product (1) across all years, or any rules about how funds must be allocated among the available products in each year?

## Turn 11 - User Simulator

No. There are no other constraints or requirements beyond those already mentioned. There are no limits on the total amount invested in product (1) across all years, and there are no rules requiring a specific allocation among the available products in each year.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total cash value received at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1. No external capital or borrowing.
4.  **Investment Products:**
    *   **Product (1):** 1-year product. Available at the beginning of Years 1, 2, and 3. Return is 1.20x principal at the end of the same year. Unlimited capacity.
    *   **Product (2):** 2-year product. Available only at the beginning of Year 1. Matures at the end of Year 2. Return is 1.50x principal. Capacity capped at 120,000 yuan.
    *   **Product (3):** 1-year product. Available only at the beginning of Year 2. Matures at the end of Year 2. Return is 1.60x principal. Capacity capped at 150,000 yuan.
    *   **Product (4):** 1-year product. Available only at the beginning of Year 3. Matures at the end of Year 3. Return is 1.40x principal. Capacity capped at 100,000 yuan.
5.  **Cash Flow Constraints:**
    *   **Beginning of Year 1:** Total investment in Product (1) Year 1 + Product (2) Year 1 ≤ 500,000.
    *   **Beginning of Year 2:** Total investment in Product (1) Year 2 + Product (3) Year 2 ≤ Cash received at end of Year 1 (which is 1.20 * Investment in Product (1) Year 1).
    *   **Beginning of Year 3:** Total investment in Product (1) Year 3 + Product (4) Year 3 ≤ Cash received at end of Year 2 (which is 1.20 * Investment in Product (1) Year 2 + 1.50 * Investment in Product (2) Year 1 + 1.60 * Investment in Product (3) Year 2).
6.  **Capacity Constraints:**
    *   Investment in Product (2) ≤ 120,000.
    *   Investment in Product (3) ≤ 150,000.
    *   Investment in Product (4) ≤ 100,000.
7.  **Objective Function:** Maximize (1.20 * Investment in Product (1) Year 3) + (1.40 * Investment in Product (4) Year 3).

**Explicit Assumptions:**
1.  **Variable Domain:** Investment amounts are assumed to be non-negative real numbers (continuous), as integrality was not confirmed.
2.  **Minimum Investment:** It is assumed that the minimum investment for any product is 0, as no minimums were confirmed.
3.  **Fund Usage:** It is assumed that it is not necessary to invest all available funds in each period; any uninvested cash is simply not available for future periods (since no interest is earned on cash and no external capital is allowed, holding cash is equivalent to not investing it, but since the objective is to maximize end-of-Year 3 cash, and all products have positive returns > 1.0, the optimal solution will likely invest all available funds in the highest yielding available options subject to constraints). *Correction:* Actually, since all returns are > 1.0, and there are no constraints forcing under-investment other than capacity, the model will naturally invest as much as possible. However, strictly speaking, the constraint is "Investment ≤ Available Cash". If capacity limits prevent full investment, the remaining cash is lost (or held with 0 return). The model formulation will use "≤" for the cash flow constraints.