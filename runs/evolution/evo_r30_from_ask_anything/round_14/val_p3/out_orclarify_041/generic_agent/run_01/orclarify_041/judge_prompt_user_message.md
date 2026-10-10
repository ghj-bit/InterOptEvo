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

QUESTION: For the 1-year product (1), is the 20% return a simple annual rate applied only to the original principal, or does it compound such that interest earned in one year can be reinvested in the same product in the following year?

## Turn 1 - User Simulator

It is a simple annual rate applied only to the original principal. However, the proceeds (principal plus interest) received at the end of the year become available cash at the beginning of the next year, and you can choose to reinvest that full amount into product (1) again if it is available.

## Turn 2 - Generic Agent

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment, or are there additional cash inflows (such as salary or external deposits) entering the portfolio at the beginning of Year 2 or Year 3?

## Turn 2 - User Simulator

The 500,000 yuan initial capital is the only source of funds. There are no additional cash inflows like salary or external deposits entering the portfolio at the beginning of Year 2 or Year 3.

## Turn 3 - Generic Agent

QUESTION: At the end of Year 3, is the objective to maximize the total cash value of all matured investments, or is there a requirement to hold a specific amount of liquid cash separate from the investment proceeds?

## Turn 3 - User Simulator

The objective is to maximize the total cash value of all matured investments at the end of Year 3. There is no requirement to hold a specific amount of liquid cash separate from the investment proceeds.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum investment requirements for any of the four products, or can the investment amount in any product be zero?

## Turn 4 - User Simulator

There are no minimum investment requirements. The investment amount in any product can be zero.

## Turn 5 - Generic Agent

QUESTION: Can the investment amounts in the products be any continuous real number, or must they be rounded to specific discrete units such as whole yuan or thousands of yuan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or rules governing the investment plan, such as limits on the total amount invested in a single year or requirements to diversify across a minimum number of products?

## Turn 6 - User Simulator

No. The only constraints are the individual caps on products (2), (3), and (4), and the rule that you cannot borrow money. You can only invest the cash you have available at the beginning of each year. There are no limits on the total amount invested in a single year, and there are no requirements to diversify across a minimum number of products.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total cash value of all matured investments at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Cash Flow Rule:** No external inflows. Cash available at the beginning of a year consists of the initial capital (Year 1) or the proceeds from investments maturing at the end of the previous year. You cannot borrow money (cash flow must be non-negative).
5.  **Investment Products:**
    *   **Product (1):** 1-year term. Available at the beginning of Years 1, 2, and 3. Return is 1.20 * I (simple interest on principal). Unlimited capacity.
    *   **Product (2):** 2-year term. Available only at the beginning of Year 1. Matures at the end of Year 2. Return is 1.50 * I. Capacity cap: 120,000 yuan.
    *   **Product (3):** Same-year term. Available only at the beginning of Year 2. Matures at the end of Year 2. Return is 1.60 * I. Capacity cap: 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the beginning of Year 3. Matures at the end of Year 3. Return is 1.40 * I. Capacity cap: 100,000 yuan.
6.  **Constraints:**
    *   Investment in Product (2) $\le$ 120,000.
    *   Investment in Product (3) $\le$ 150,000.
    *   Investment in Product (4) $\le$ 100,000.
    *   No minimum investment requirements (investments can be zero).
    *   No borrowing allowed.
    *   No other constraints (no diversification requirements, no annual total investment limits).
7.  **Variable Domain:** Continuous real numbers (assumed, as the user indicated this point needs internal confirmation but did not specify discrete units).

**Assumptions:**
*   Investment amounts are continuous variables (not restricted to integer or discrete units).