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

QUESTION: For the 1-year product (1), is the 1.20 return factor applied to the principal invested at the start of each year, meaning the amount received at the end of that same year is 1.20 times the amount invested at the start of that year?

## Turn 1 - User Simulator

Yes, that is correct. For the 1-year product (1), if you invest an amount at the start of a year, you receive 1.20 times that amount at the end of that same year.

## Turn 2 - Generic Agent

QUESTION: Is the 1-year product (1) available for investment at the beginning of Year 1, Year 2, and Year 3, with each investment maturing at the end of that same year?

## Turn 2 - User Simulator

Yes, the 1-year product (1) is available at the beginning of Years 1, 2, and 3, and each investment matures at the end of that same year.

## Turn 3 - Generic Agent

QUESTION: Is the 2-year product (2) available for investment only at the beginning of Year 1, with the investment maturing and paying 1.50 times the principal at the end of Year 2?

## Turn 3 - User Simulator

Yes, the 2-year product (2) is available only at the beginning of Year 1, and it matures at the end of Year 2, paying 1.50 times the principal invested.

## Turn 4 - Generic Agent

QUESTION: Is the same-year product (3) available for investment only at the beginning of Year 2, with the investment maturing at the end of Year 2 and paying 1.60 times the principal invested?

## Turn 4 - User Simulator

Yes, the same-year product (3) is available only at the beginning of Year 2, matures at the end of Year 2, and pays 1.60 times the principal invested.

## Turn 5 - Generic Agent

QUESTION: Is the 1-year product (4) available for investment only at the beginning of Year 3, with the investment maturing at the end of Year 3 and paying 1.40 times the principal invested?

## Turn 5 - User Simulator

Yes, the 1-year product (4) is available only at the beginning of Year 3, matures at the end of Year 3, and pays 1.40 times the principal invested.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 2, is the available cash for investment equal to the 500,000 yuan initial capital plus the returns from any Year 1 investments that matured at the end of Year 1?

## Turn 6 - User Simulator

No. The available cash at the beginning of Year 2 is not the initial 500,000 yuan plus returns. It is only the proceeds from investments that matured at the end of Year 1. The initial capital was used for investments at the beginning of Year 1, so it is no longer available as cash at the start of Year 2.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 3, is the available cash for investment equal to the proceeds from all investments that matured at the end of Year 2?

## Turn 7 - User Simulator

Yes, the available cash at the beginning of Year 3 is equal to the proceeds from all investments that matured at the end of Year 2.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan, such as a minimum amount that must be invested in any specific product, a requirement to invest all available cash each year, or any restrictions on holding cash without investing it?

## Turn 8 - User Simulator

There are no minimum investment requirements for any product. You are not required to invest all available cash each year, and there are no restrictions on holding cash without investing it.

## Turn 9 - Generic Agent

QUESTION: If you hold cash without investing it in a given year, does that cash carry over to the next year's available cash at the same amount, or does it earn any interest or return?

## Turn 9 - User Simulator

The available business facts do not specify whether uninvested cash earns interest or carries over at the same amount. This point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: If you hold cash without investing it in a given year, does that cash carry over to the next year's available cash at the same amount, or does it earn any interest or return?

## Turn 10 - User Simulator

The available business facts do not specify whether uninvested cash earns interest or carries over at the same amount. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is the objective to maximize the total value of all investments that have matured by the end of Year 3, plus any uninvested cash held at the end of Year 3?

## Turn 11 - User Simulator

Yes, the objective is to maximize the total principal plus interest at the end of Year 3, which includes the value of all investments that have matured by the end of Year 3 plus any uninvested cash held at that time.

## Turn 12 - Generic Agent

QUESTION: Are the investment amounts for each product in each year required to be whole numbers (integers), or can they be any non-negative real numbers?

## Turn 12 - User Simulator

The available business facts do not specify whether investment amounts must be whole numbers or can be any non-negative real numbers. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Are the investment amounts for each product in each year required to be whole numbers (integers), or can they be any non-negative real numbers?

## Turn 13 - User Simulator

The available business facts do not specify whether investment amounts must be whole numbers or can be any non-negative real numbers. This point still needs internal confirmation.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total value (principal plus interest) at the end of Year 3. This includes the proceeds from all investments maturing at the end of Year 3 plus any uninvested cash held at that time.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Cash Flow Dynamics:**
    *   **Start of Year 1:** Available cash is 500,000 yuan.
    *   **Start of Year 2:** Available cash is the sum of proceeds from investments maturing at the end of Year 1 plus any uninvested cash from Year 1.
    *   **Start of Year 3:** Available cash is the sum of proceeds from investments maturing at the end of Year 2 plus any uninvested cash from Year 2.
    *   **End of Year 3:** The objective value is the sum of proceeds from investments maturing at the end of Year 3 plus any uninvested cash from Year 3.
5.  **Investment Products:**
    *   **Product (1):** 1-year product. Available at the beginning of Years 1, 2, and 3. Returns 1.20 times the principal at the end of the same year. Unlimited capacity.
    *   **Product (2):** 2-year product. Available only at the beginning of Year 1. Returns 1.50 times the principal at the end of Year 2. Capacity limit: 120,000 yuan.
    *   **Product (3):** Same-year product. Available only at the beginning of Year 2. Returns 1.60 times the principal at the end of Year 2. Capacity limit: 150,000 yuan.
    *   **Product (4):** 1-year product. Available only at the beginning of Year 3. Returns 1.40 times the principal at the end of Year 3. Capacity limit: 100,000 yuan.
6.  **Constraints:**
    *   Investment in Product (2) $\le$ 120,000 yuan.
    *   Investment in Product (3) $\le$ 150,000 yuan.
    *   Investment in Product (4) $\le$ 100,000 yuan.
    *   No minimum investment requirements.
    *   Not required to invest all available cash each year.
    *   No restrictions on holding cash.

**Explicit Assumptions:**

1.  **Uninvested Cash Return:** It is assumed that uninvested cash carries over to the next year at the same amount (i.e., 0% interest on cash). This assumption was made because the user stated that the facts regarding cash carry-over were unconfirmed, and in the absence of a specified interest rate for cash, the standard conservative assumption is no return.
2.  **Variable Domain:** It is assumed that investment amounts can be any non-negative real numbers (continuous variables). This assumption was made because the user stated that the facts regarding integrality were unconfirmed, and continuous variables are the standard default for financial planning models unless integer constraints are explicitly required.