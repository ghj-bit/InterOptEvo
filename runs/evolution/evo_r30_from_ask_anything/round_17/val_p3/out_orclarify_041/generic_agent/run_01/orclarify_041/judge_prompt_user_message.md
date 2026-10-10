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

QUESTION: For the 1-year product (1), is the 20% return a simple annual rate applied only to the principal invested at the start of that year, or does it compound on any funds that remain invested from prior periods?

## Turn 1 - User Simulator

It is a simple annual rate applied only to the principal invested at the start of that year. It does not compound on funds from prior periods.

## Turn 2 - Generic Agent

QUESTION: For the 2-year product (2), is the 50% total return a simple return applied only to the principal invested at the start of Year 1, or does it compound on any funds that remain invested from prior periods?

## Turn 2 - User Simulator

It is a simple return applied only to the principal invested at the start of Year 1.

## Turn 3 - Generic Agent

QUESTION: For the same-year product (3), is the 60% return a simple return applied only to the principal invested at the start of Year 2, or does it compound on any funds that remain invested from prior periods?

## Turn 3 - User Simulator

It is a simple return applied only to the principal invested at the start of Year 2.

## Turn 4 - Generic Agent

QUESTION: For the 1-year product (4), is the 40% return a simple annual rate applied only to the principal invested at the start of Year 3, or does it compound on any funds that remain invested from prior periods?

## Turn 4 - User Simulator

It is a simple annual rate applied only to the principal invested at the start of Year 3.

## Turn 5 - Generic Agent

QUESTION: At the end of Year 1, can funds from maturing investments be immediately reinvested into product (1) at the start of Year 2, or is there a delay or restriction on reinvestment?

## Turn 5 - User Simulator

Funds from maturing investments can be immediately reinvested into product (1) at the start of Year 2. There is no delay or restriction on reinvestment.

## Turn 6 - Generic Agent

QUESTION: At the end of Year 2, can funds from maturing investments be immediately reinvested into product (1) at the start of Year 3, or is there a delay or restriction on reinvestment?

## Turn 6 - User Simulator

Funds from maturing investments can be immediately reinvested into product (1) at the start of Year 3. There is no delay or restriction on reinvestment.

## Turn 7 - Generic Agent

QUESTION: Are there any other investment products or cash-holding options available at the beginning of each year besides the four products listed, or must all available funds be allocated to one of these four products?

## Turn 7 - User Simulator

There are no other investment products or cash-holding options available. All available funds must be allocated to one of the four listed products.

## Turn 8 - Generic Agent

QUESTION: Is there a minimum investment amount required for any of the four products, or can you invest any non-negative amount down to zero?

## Turn 8 - User Simulator

There is no minimum investment amount required. You can invest any non-negative amount down to zero for any of the four products.

## Turn 9 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integer yuan), or can they be any continuous non-negative value?

## Turn 9 - User Simulator

The investment amounts can be any continuous non-negative value.

## Turn 10 - Generic Agent

QUESTION: Is there a maximum total investment limit across all products combined in any given year, or are the only limits the individual caps specified for products (2), (3), and (4)?

## Turn 10 - User Simulator

There is no maximum total investment limit across all products combined in any given year. The only limits are the individual caps specified for products (2), (3), and (4).

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as conditional linkages between investments, minimum quantities tied to a decision being active, or dependencies between activities?

## Turn 11 - User Simulator

No, there are no other constraints or requirements. The only constraints are the individual caps for products (2), (3), and (4), and the rule that no borrowing is allowed.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total principal plus interest at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Decision Variables:** Continuous, non-negative investment amounts for each product at each available time period.
5.  **Products and Returns:**
    *   **Product (1):** 1-year term. Available at the start of Years 1, 2, and 3. Return is 1.20 * I (simple interest, 20% annual rate). Unlimited capacity.
    *   **Product (2):** 2-year term. Available only at the start of Year 1. Matures at end of Year 2. Return is 1.50 * I (simple return, 50% total). Cap: 120,000 yuan.
    *   **Product (3):** Same-year term. Available only at the start of Year 2. Matures at end of Year 2. Return is 1.60 * I (simple return, 60% total). Cap: 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the start of Year 3. Matures at end of Year 3. Return is 1.40 * I (simple interest, 40% annual rate). Cap: 100,000 yuan.
6.  **Cash Flow and Reinvestment:**
    *   Funds from maturing investments are immediately available for reinvestment at the start of the next period.
    *   No borrowing is allowed.
    *   All available funds must be allocated to one of the four products (no cash holding option).
7.  **Constraints:**
    *   Investment in Product (2) ≤ 120,000 yuan.
    *   Investment in Product (3) ≤ 150,000 yuan.
    *   Investment in Product (4) ≤ 100,000 yuan.
    *   No other aggregate or conditional constraints.
8.  **Assumptions:**
    *   None. All critical facts were confirmed by the user.