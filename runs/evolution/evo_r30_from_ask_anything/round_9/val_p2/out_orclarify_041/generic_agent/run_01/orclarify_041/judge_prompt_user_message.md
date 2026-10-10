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

QUESTION: For the 1-year product (1), is the 20% return a simple annual rate applied to the principal invested at the start of that year, or does it represent a total return that already includes compounding effects from prior periods?

## Turn 1 - User Simulator

It is a simple annual rate applied to the principal invested at the start of that year. You invest an amount at the beginning of the year, and you receive 1.20 times that amount at the end of that same year. There is no compounding from prior periods built into that 20% figure.

## Turn 2 - Generic Agent

QUESTION: For the 2-year product (2), is the 50% return a total return over the two-year holding period, meaning you invest I at the start of Year 1 and receive 1.50·I at the end of Year 2 with no intermediate cash flows?

## Turn 2 - User Simulator

Yes, that is correct. You invest an amount at the beginning of Year 1, and you receive 1.50 times that amount at the end of Year 2. There are no intermediate cash flows during the two-year holding period.

## Turn 3 - Generic Agent

QUESTION: For the same-year product (3), is the 60% return a total return for that single year, meaning you invest I at the start of Year 2 and receive 1.60·I at the end of Year 2?

## Turn 3 - User Simulator

Yes, that is correct. You invest an amount at the beginning of Year 2, and you receive 1.60 times that amount at the end of Year 2.

## Turn 4 - Generic Agent

QUESTION: For the 1-year product (4), is the 40% return a total return for that single year, meaning you invest I at the start of Year 3 and receive 1.40·I at the end of Year 3

## Turn 4 - User Simulator

Yes, that is correct. You invest an amount at the beginning of Year 3, and you receive 1.40 times that amount at the end of Year 3.

## Turn 5 - Generic Agent

QUESTION: Are there any additional requirements or constraints beyond the stated investment caps, such as minimum investment amounts for any product, mandatory diversification rules, or restrictions on how funds can be rolled over between years

## Turn 5 - User Simulator

No, there are no minimum investment amounts, mandatory diversification rules, or specific restrictions on rolling over funds between years. The only constraints are the maximum investment caps for products (2), (3), and (4), and the rule that you cannot borrow money. You can only invest the cash you have available at the beginning of each year.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year 3, which includes both the principal and all interest earned from all investments maturing at that time

## Turn 6 - User Simulator

Yes, the objective is to maximize the total cash available at the end of Year 3, which includes both the principal and all interest earned from all investments maturing at that time.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total cash available at the end of Year 3 (principal plus interest from all investments maturing at that time).

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Investment Products:**

1.  **Product (1):** 1-year product available at the beginning of Years 1, 2, and 3.
    *   Return: 20% simple annual rate. Invest $I$ at start of year, receive $1.20 \cdot I$ at end of that same year.
    *   Capacity: Unlimited.
    *   Cash Flow: No intermediate cash flows.

2.  **Product (2):** 2-year product available only at the beginning of Year 1.
    *   Return: 50% total return over the two-year holding period. Invest $I$ at start of Year 1, receive $1.50 \cdot I$ at end of Year 2.
    *   Capacity: Capped at 120,000 yuan.
    *   Cash Flow: No intermediate cash flows.

3.  **Product (3):** Same-year product available only at the beginning of Year 2.
    *   Return: 60% total return for that single year. Invest $I$ at start of Year 2, receive $1.60 \cdot I$ at end of Year 2.
    *   Capacity: Capped at 150,000 yuan.
    *   Cash Flow: No intermediate cash flows.

4.  **Product (4):** 1-year product available only at the beginning of Year 3.
    *   Return: 40% total return for that single year. Invest $I$ at start of Year 3, receive $1.40 \cdot I$ at end of Year 3.
    *   Capacity: Capped at 100,000 yuan.
    *   Cash Flow: No intermediate cash flows.

**Constraints:**
*   **Budget Constraints:** At the beginning of each year, the sum of investments in products available in that year cannot exceed the cash available at the start of that year.
    *   Year 1 Start: Cash available = 500,000. Investments in Product (1) Year 1 + Product (2) $\le$ 500,000.
    *   Year 2 Start: Cash available = Proceeds from Product (1) Year 1 + Proceeds from Product (2). Investments in Product (1) Year 2 + Product (3) $\le$ Cash available at start of Year 2.
    *   Year 3 Start: Cash available = Proceeds from Product (1) Year 2 + Proceeds from Product (3). Investments in Product (1) Year 3 + Product (4) $\le$ Cash available at start of Year 3.
*   **Capacity Constraints:**
    *   Product (2) investment $\le$ 120,000.
    *   Product (3) investment $\le$ 150,000.
    *   Product (4) investment $\le$ 100,000.
*   **Non-negativity:** All investment amounts must be non-negative.
*   **No Borrowing:** Cannot invest more than available cash.

**Assumptions:**
*   None. All critical facts were confirmed by the user.