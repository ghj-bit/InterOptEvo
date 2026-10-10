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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment, or can you also invest money received from maturing products in subsequent years?

## Turn 1 - User Simulator

The 500,000 yuan is not the only source of funds. You can also invest money received from maturing products in subsequent years. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 2 - Generic Agent

QUESTION: Is the investment in product (2) a single lump-sum decision made only at the beginning of Year 1, or can you invest in it at the beginning of Year 2 as well?

## Turn 2 - User Simulator

The investment in product (2) is a single lump-sum decision made only at the beginning of Year 1.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can you invest any amount from zero up to the stated maximums?

## Turn 3 - User Simulator

There are no minimum investment amounts required. You can invest any amount from zero up to the stated maximums.

## Turn 4 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integers), or can they be any continuous value?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as limits on total investment per year, mandatory diversification rules, or restrictions on how proceeds from one product can be allocated to others?

## Turn 5 - User Simulator

There are no other constraints or requirements. The only rules are:
- No borrowing allowed.
- Decisions are made at the beginnings of Years 1–3 using only currently available cash (initial capital and proceeds from matured investments).
- Investment in product (2) cannot exceed 120,000 yuan.
- Investment in product (3) cannot exceed 150,000 yuan.
- Investment in product (4) cannot exceed 100,000 yuan.

## Turn 6 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total cash (principal plus interest) at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Cash Flow Rule:** No borrowing. At the beginning of each year, only currently available cash (initial capital plus proceeds from investments that have already matured) can be invested. Uninvested cash carries over to the next year.
5.  **Investment Products:**
    *   **Product (1):** 1-year term. Available at the beginning of Years 1, 2, and 3. Return is 1.20 times the investment at the end of that year. Unlimited capacity.
    *   **Product (2):** 2-year term. Available only at the beginning of Year 1. Matures at the end of Year 2. Return is 1.50 times the investment. Maximum investment: 120,000 yuan.
    *   **Product (3):** 1-year term (same-year). Available only at the beginning of Year 2. Matures at the end of Year 2. Return is 1.60 times the investment. Maximum investment: 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the beginning of Year 3. Matures at the end of Year 3. Return is 1.40 times the investment. Maximum investment: 100,000 yuan.
6.  **Constraints:**
    *   Investment in Product (2) ≤ 120,000 yuan.
    *   Investment in Product (3) ≤ 150,000 yuan.
    *   Investment in Product (4) ≤ 100,000 yuan.
    *   No minimum investment amounts (investments can be zero).
    *   No other constraints (e.g., no diversification requirements, no annual total investment caps beyond the product-specific caps).

**Assumptions:**

1.  **Variable Domain:** Investment amounts are treated as continuous variables (not restricted to integers), as the user could not confirm integrality requirements.
2.  **Uninvested Cash:** Cash not invested in a given year remains available for investment in subsequent years (standard cash flow carry-over).