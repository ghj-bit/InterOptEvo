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

QUESTION: For the 1-year product (1), is the 1.20 return a total payout (meaning you receive 1.20 times the invested amount, which includes the original principal plus 20% interest) or is it a pure interest rate (meaning you receive the original principal plus an additional 20% interest)?

## Turn 1 - User Simulator

It is a total payout. You receive 1.20 times the invested amount, which includes the original principal plus 20% interest.

## Turn 2 - Generic Agent

QUESTION: For the 2-year product (2), is the 1.50 return a total payout (meaning you receive 1.50 times the invested amount at the end of Year 2, which includes the original principal plus 50% total interest) or is it a pure interest rate (meaning you receive the original principal plus an additional 50% interest)?

## Turn 2 - User Simulator

It is a total payout. You receive 1.50 times the invested amount at the end of Year 2, which includes the original principal plus 50% total interest.

## Turn 3 - Generic Agent

QUESTION: For the same-year product (3), is the 1.60 return a total payout (meaning you receive 1.60 times the invested amount at the end of Year 2, which includes the original principal plus 60% interest) or is it a pure interest rate (meaning you receive the original principal plus an additional 60% interest)?

## Turn 3 - User Simulator

It is a total payout. You receive 1.60 times the invested amount at the end of Year 2, which includes the original principal plus 60% interest.

## Turn 4 - Generic Agent

QUESTION: For the 1-year product (4), is the 1.40 return a total payout (meaning you receive 1.40 times the invested amount at the end of Year 3, which includes the original principal plus 40% interest) or is it a pure interest rate (meaning you receive the original principal plus an additional 40% interest)?

## Turn 4 - User Simulator

It is a total payout. You receive 1.40 times the invested amount at the end of Year 3, which includes the original principal plus 40% interest.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan, such as a minimum amount that must be invested in any specific product, a requirement to invest all available capital each year, or any restrictions on how funds can be carried over between years?

## Turn 5 - User Simulator

No. There are no minimum investment requirements, no requirement to invest all available capital each year, and no restrictions on carrying over funds between years. The only constraints are the maximum investment caps for products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 6 - Generic Agent

QUESTION: When you say you cannot borrow money, does this mean that the total amount invested in any given year cannot exceed the total funds available at the beginning of that year (including initial capital and returns from maturing investments), or is there a specific rule about how uninvested cash is handled?

## Turn 6 - User Simulator

Yes, the total amount invested in any given year cannot exceed the total funds available at the beginning of that year, which includes initial capital and returns from maturing investments.

## Turn 7 - Generic Agent

QUESTION: Is there any interest earned on uninvested cash that is carried over from one year to the next, or does uninvested cash simply remain as principal without any return?

## Turn 7 - User Simulator

I need to confirm this internally.

## Turn 8 - Generic Agent

QUESTION: If uninvested cash does not earn any interest and simply remains as principal, would that be the correct assumption for this model?

## Turn 8 - User Simulator

Yes, that is the correct assumption.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total wealth (principal plus interest) at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Investment Products:**
    *   **Product (1):** 1-year term. Available at the beginning of Years 1, 2, and 3.
        *   Return: Total payout of 1.20 * Investment (includes principal + 20% interest).
        *   Capacity: Unlimited.
    *   **Product (2):** 2-year term. Available only at the beginning of Year 1. Matures at the end of Year 2.
        *   Return: Total payout of 1.50 * Investment (includes principal + 50% total interest).
        *   Capacity: Maximum 120,000 yuan.
    *   **Product (3):** Same-year term. Available only at the beginning of Year 2. Matures at the end of Year 2.
        *   Return: Total payout of 1.60 * Investment (includes principal + 60% interest).
        *   Capacity: Maximum 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the beginning of Year 3. Matures at the end of Year 3.
        *   Return: Total payout of 1.40 * Investment (includes principal + 40% interest).
        *   Capacity: Maximum 100,000 yuan.
5.  **Constraints:**
    *   **Budget Constraint:** Total investment in any year cannot exceed the funds available at the beginning of that year.
    *   **No Borrowing:** Funds available are limited to initial capital plus returns from maturing investments.
    *   **Caps:**
        *   Product (2) $\le$ 120,000 yuan.
        *   Product (3) $\le$ 150,000 yuan.
        *   Product (4) $\le$ 100,000 yuan.
    *   **Uninvested Cash:** Carries over to the next year with **zero** interest (no return on idle cash).
    *   **Non-negativity:** All investment amounts must be non-negative.
6.  **Assumptions:**
    *   Investments are continuous variables (can invest any fractional amount, not just integers).
    *   Returns are received exactly at the end of the stated maturity period and are immediately available for investment at the beginning of the following year (if applicable).
    *   Product (2) funds are locked for 2 years and cannot be accessed before the end of Year 2.