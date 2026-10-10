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

QUESTION: For the 1-year product (1), is the 20% return a simple annual rate applied to the principal invested at the start of that year, with no compounding within the year?

## Turn 1 - User Simulator

Yes. The 20% return is a simple annual rate applied to the principal invested at the start of that year, with no compounding within the year.

## Turn 2 - Generic Agent

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or are there additional cash inflows (such as salary or external deposits) during the three years?

## Turn 2 - User Simulator

The 500,000 yuan initial capital is the only source of funds available for investment at the beginning of Year 1. There are no additional cash inflows during the three years.

## Turn 3 - Generic Agent

QUESTION: When the 2-year product (2) matures at the end of Year 2, can the returned funds be reinvested in the 1-year product (1) at the beginning of Year 3?

## Turn 3 - User Simulator

Yes, the funds returned from the 2-year product (2) at the end of Year 2 can be reinvested in the 1-year product (1) at the beginning of Year 3.

## Turn 4 - Generic Agent

QUESTION: Can the funds returned from the 1-year product (1) at the end of Year 1 be reinvested in the 1-year product (1) at the beginning of Year 2?

## Turn 4 - User Simulator

Yes, the funds returned from the 1-year product (1) at the end of Year 1 can be reinvested in the 1-year product (1) at the beginning of Year 2.

## Turn 5 - Generic Agent

QUESTION: Can the funds returned from the 1-year product (1) at the end of Year 2 be reinvested in the 1-year product (1) at the beginning of Year 3?

## Turn 5 - User Simulator

Yes, the funds returned from the 1-year product (1) at the end of Year 2 can be reinvested in the 1-year product (1) at the beginning of Year 3.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can you invest any non-negative amount up to the stated caps?

## Turn 6 - User Simulator

There are no minimum investment amounts required for any of the four products. You can invest any non-negative amount up to the stated caps.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan, such as a minimum amount that must remain in cash at the end of Year 3, or any restrictions on how funds can be allocated across the products?

## Turn 7 - User Simulator

No, there are no other constraints or requirements. There is no minimum amount that must remain in cash at the end of Year 3, and there are no restrictions on how funds can be allocated across the products beyond the stated caps and the no-borrowing rule.

## Turn 8 - Generic Agent

QUESTION: Is the "no-borrowing rule" a formal constraint that means you cannot invest more than the total funds available at the beginning of each year, or is it just a descriptive statement of how the funds flow?

## Turn 8 - User Simulator

It is a formal constraint. You cannot invest more than the total funds available at the beginning of each year.

## Turn 9 - Generic Agent

QUESTION: Is the objective to maximize the total value of all investments that have matured by the end of Year 3, including any cash that was not invested?

## Turn 9 - User Simulator

Yes, the objective is to maximize the total value of all investments that have matured by the end of Year 3, including any cash that was not invested.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total principal plus interest at the end of Year 3. This includes the value of all matured investments and any uninvested cash.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Cash Flow Rule:** No external inflows or outflows. Funds from matured investments can be reinvested in subsequent years.
5.  **No Borrowing Constraint:** At the beginning of each year, the sum of investments made cannot exceed the total funds available (initial capital plus returns from previous investments).
6.  **Investment Products:**
    *   **Product (1):** 1-year term. Available at the start of Years 1, 2, and 3. Return: 1.20 * I. Capacity: Unlimited.
    *   **Product (2):** 2-year term. Available only at the start of Year 1. Matures at end of Year 2. Return: 1.50 * I. Capacity: Max 120,000 yuan.
    *   **Product (3):** Same-year term. Available only at the start of Year 2. Matures at end of Year 2. Return: 1.60 * I. Capacity: Max 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the start of Year 3. Matures at end of Year 3. Return: 1.40 * I. Capacity: Max 100,000 yuan.
7.  **Variable Domains:** All investment amounts are continuous and non-negative.
8.  **Other Constraints:** No minimum investment amounts. No other restrictions.