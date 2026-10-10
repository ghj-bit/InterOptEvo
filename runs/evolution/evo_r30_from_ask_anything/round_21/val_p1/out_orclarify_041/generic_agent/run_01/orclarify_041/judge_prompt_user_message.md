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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or will additional external funds be injected during the three-year period?

## Turn 1 - User Simulator

The 500,000 yuan initial capital is the only source of funds available at the beginning of Year 1. No additional external funds will be injected during the three-year period.

## Turn 2 - Generic Agent

QUESTION: When you invest in the 1-year product (1) at the beginning of a year, is the entire amount invested locked up until the end of that year, meaning no portion of it is available for other investments during that same year?

## Turn 2 - User Simulator

Yes, the entire amount invested in product (1) is locked up until the end of that year. It is not available for other investments during that same year.

## Turn 3 - Generic Agent

QUESTION: At the end of each year, when investments mature and return principal plus interest, is that returned amount immediately available to be reinvested in products available at the beginning of the next year?

## Turn 3 - User Simulator

Yes, the returned amount is immediately available to be reinvested in products available at the beginning of the next year.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can you invest any non-negative amount in each product?

## Turn 4 - User Simulator

There are no minimum investment amounts required. You can invest any non-negative amount in each product, subject to the stated maximum caps for products (2), (3), and (4).

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integers), or can they be any continuous non-negative value?

## Turn 5 - User Simulator

The investment amounts can be any continuous non-negative value. They are not required to be whole numbers.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year 3, which includes both the matured proceeds from investments and any uninvested cash held at that time?

## Turn 6 - User Simulator

Yes, the objective is to maximize the total cash available at the end of Year 3, which includes both the matured proceeds from investments and any uninvested cash held at that time.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan that have not been mentioned yet, such as limits on the total amount invested in any single year, requirements to maintain a minimum cash reserve, or restrictions on how many different products can be invested in simultaneously?

## Turn 7 - User Simulator

No, there are no other constraints or requirements. The only constraints are the maximum investment caps for products (2), (3), and (4), and the rule that no borrowing is allowed.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total cash available at the end of Year 3 (matured proceeds + uninvested cash).
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Funding Source:** Only the initial capital and reinvested returns from previous periods. No external funds, no borrowing.
5.  **Decision Variables:** Continuous, non-negative investment amounts for each product in each period it is available.
6.  **Products & Returns:**
    *   **Product (1):** 1-year term. Available at the start of Years 1, 2, and 3. Returns 1.20 * I at the end of that year. Unlimited capacity.
    *   **Product (2):** 2-year term. Available only at the start of Year 1. Returns 1.50 * I at the end of Year 2. Max investment: 120,000 yuan.
    *   **Product (3):** 1-year term (same-year). Available only at the start of Year 2. Returns 1.60 * I at the end of Year 2. Max investment: 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the start of Year 3. Returns 1.40 * I at the end of Year 3. Max investment: 100,000 yuan.
7.  **Constraints:**
    *   **Budget Constraints:** For each year, the sum of investments made at the beginning of that year cannot exceed the cash available at the beginning of that year.
    *   **Cash Flow Linkage:** Cash available at the beginning of Year *t* equals the cash available at the end of Year *t-1* (which is the sum of returns from investments maturing at the end of Year *t-1* plus any uninvested cash carried over).
    *   **Product Caps:**
        *   Investment in Product (2) ≤ 120,000.
        *   Investment in Product (3) ≤ 150,000.
        *   Investment in Product (4) ≤ 100,000.
    *   **Non-negativity:** All investment variables ≥ 0.
8.  **Assumptions:**
    *   Uninvested cash carries over to the next period with no interest or penalty.
    *   Investments are locked for their full term (confirmed).
    *   Returns are received at the end of the term and are immediately available for the next period's investments (confirmed).