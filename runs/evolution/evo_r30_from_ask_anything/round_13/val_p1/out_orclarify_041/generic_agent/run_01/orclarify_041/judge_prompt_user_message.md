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

QUESTION: Is the 500,000 yuan initial capital the only source of funds, or can you also invest money received from maturing projects in subsequent years?

## Turn 1 - User Simulator

The 500,000 yuan is not the only source of funds. You can also invest money received from maturing projects in subsequent years. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20·I payout at year-end the total amount received (principal plus interest), or is it just the interest earned on top of the principal?

## Turn 2 - User Simulator

The 1.20·I payout is the total amount received, meaning it includes both the principal and the interest.

## Turn 3 - Generic Agent

QUESTION: Are the 1.50·I, 1.60·I, and 1.40·I payouts for products (2), (3), and (4) also total amounts received including principal, or are they just the interest portion?

## Turn 3 - User Simulator

The 1.50·I, 1.60·I, and 1.40·I payouts for products (2), (3), and (4) are also total amounts received, including both principal and interest.

## Turn 4 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as minimum investment amounts, mandatory allocations, or restrictions on how many products you can hold simultaneously?

## Turn 4 - User Simulator

No, there are no other constraints or requirements. The only restrictions are the maximum investment caps for products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 5 - Generic Agent

QUESTION: Can you invest in product (1) multiple times within the same year, or is there only one opportunity to invest in product (1) at the beginning of each year?

## Turn 5 - User Simulator

There is only one opportunity to invest in product (1) at the beginning of each year.

## Turn 6 - Generic Agent

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand, which includes both the proceeds from maturing investments and any uninvested cash remaining?

## Turn 6 - User Simulator

Yes, the objective is to maximize the total cash on hand at the end of Year 3, which includes both the proceeds from maturing investments and any uninvested cash remaining.

## Turn 7 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total cash on hand at the end of Year 3. This includes proceeds from all investments maturing at the end of Year 3 plus any uninvested cash remaining.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Cash Flow Rule:** At the beginning of each year, available cash equals the initial capital (Year 1 only) plus proceeds from investments that matured in the previous year(s). You cannot borrow money. Uninvested cash carries over to the next year.
5.  **Investment Products:**
    *   **Product (1):** 1-year term. Available at the beginning of Years 1, 2, and 3. Returns 1.20 * I (total payout including principal) at the end of the investment year. Unlimited capacity. One investment opportunity per year.
    *   **Product (2):** 2-year term. Available only at the beginning of Year 1. Matures at the end of Year 2. Returns 1.50 * I (total payout including principal). Maximum investment: 120,000 yuan.
    *   **Product (3):** Same-year term. Available only at the beginning of Year 2. Matures at the end of Year 2. Returns 1.60 * I (total payout including principal). Maximum investment: 150,000 yuan.
    *   **Product (4):** 1-year term. Available only at the beginning of Year 3. Matures at the end of Year 3. Returns 1.40 * I (total payout including principal). Maximum investment: 100,000 yuan.
6.  **Constraints:**
    *   Investment in Product (2) ≤ 120,000 yuan.
    *   Investment in Product (3) ≤ 150,000 yuan.
    *   Investment in Product (4) ≤ 100,000 yuan.
    *   No borrowing allowed.
    *   No minimum investment amounts.
    *   No mutual exclusivity or other hidden constraints.
7.  **Variable Domains:** All investment amounts are non-negative continuous variables.