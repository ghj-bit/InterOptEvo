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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or are there additional external funds that can be injected during the three-year period?

## Turn 1 - User Simulator

The 500,000 yuan initial capital is the only source of funds available at the beginning of Year 1. There are no additional external funds injected during the three-year period.

## Turn 2 - Generic Agent

QUESTION: When you say "investment in product (2) cannot exceed 120,000 yuan," does this cap apply to the single investment made at the beginning of Year 1, or is it a cumulative limit across all periods (though product 2 is only available in Year 1)?

## Turn 2 - User Simulator

The cap applies to the single investment made at the beginning of Year 1.

## Turn 3 - Generic Agent

QUESTION: When you say "investment in product (3) cannot exceed 150,000 yuan," does this cap apply to the single investment made at the beginning of Year 2, or is it a cumulative limit across all periods (though product 3 is only available in Year 2)?

## Turn 3 - User Simulator

The cap applies to the single investment made at the beginning of Year 2.

## Turn 4 - Generic Agent

QUESTION: When you say "investment in product (4) cannot exceed 100,000 yuan," does this cap apply to the single investment made at the beginning of Year 3, or is it a cumulative limit across all periods (though product 4 is only available in Year 3)?

## Turn 4 - User Simulator

The cap applies to the single investment made at the beginning of Year 3.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integer yuan), or can they be any non-negative real number?

## Turn 5 - User Simulator

I need to confirm this internally.

## Turn 6 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integer yuan), or can they be any non-negative real number?

## Turn 6 - User Simulator

The investment amounts can be any non-negative real number.

## Turn 7 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the products, or can you invest zero in any product?

## Turn 7 - User Simulator

You can invest zero in any product.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan that have not been mentioned, such as liquidity needs, risk limits, or mandatory allocations?

## Turn 8 - User Simulator

No, there are no other constraints or requirements.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total principal plus interest at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Funding Source:** The initial 500,000 yuan is the only external source of funds; no additional injections occur during the 3-year period.
5.  **Investment Products:**
    *   **Product 1:** 1-year term. Available at the beginning of Years 1, 2, and 3. Return is 1.20 times the investment amount at the end of that year. No capacity limit.
    *   **Product 2:** 2-year term. Available only at the beginning of Year 1. Matures at the end of Year 2. Return is 1.50 times the investment amount. Capacity limit: 120,000 yuan (applies to the single investment in Year 1).
    *   **Product 3:** Same-year term (1-year). Available only at the beginning of Year 2. Matures at the end of Year 2. Return is 1.60 times the investment amount. Capacity limit: 150,000 yuan (applies to the single investment in Year 2).
    *   **Product 4:** 1-year term. Available only at the beginning of Year 3. Matures at the end of Year 3. Return is 1.40 times the investment amount. Capacity limit: 100,000 yuan (applies to the single investment in Year 3).
6.  **Variable Domain:** Investment amounts are non-negative real numbers.
7.  **Minimums:** No minimum investment amounts; zero investment is allowed for any product.
8.  **Other Constraints:** No other constraints (e.g., liquidity, risk, mandatory allocations) exist.
9.  **Cash Flow Logic:** Funds not invested in a given year are assumed to be available for investment in subsequent years (standard carry-over of uninvested cash). Specifically, cash available at the beginning of Year 2 consists of uninvested Year 1 capital plus returns from Year 1 investments. Cash available at the beginning of Year 3 consists of uninvested Year 2 capital plus returns from Year 2 investments.