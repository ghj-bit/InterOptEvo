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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or can you also invest funds generated from the maturing of investments in subsequent years?

## Turn 1 - User Simulator

The 500,000 yuan is the only source of funds available at the beginning of Year 1. Funds generated from maturing investments become available in later years and can be invested at the beginning of those subsequent years.

## Turn 2 - Generic Agent

QUESTION: Is the investment amount in each product required to be a whole number of yuan, or can it be any non-negative real number?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: Is the investment in product (2) a single lump sum made only at the beginning of Year 1, or can it be split across multiple periods?

## Turn 3 - User Simulator

It is a single lump sum made only at the beginning of Year 1.

## Turn 4 - Generic Agent

QUESTION: Is the investment in product (3) a single lump sum made only at the beginning of Year 2, or can it be split across multiple periods?

## Turn 4 - User Simulator

It is a single lump sum made only at the beginning of Year 2.

## Turn 5 - Generic Agent

QUESTION: Is the investment in product (4) a single lump sum made only at the beginning of Year 3, or can it be split across multiple periods?

## Turn 5 - User Simulator

It is a single lump sum made only at the beginning of Year 3.

## Turn 6 - Generic Agent

QUESTION: Is the investment in product (1) made as a single lump sum at the beginning of each year, or can it be split into multiple tranches within the same year?

## Turn 6 - User Simulator

It is a single lump sum at the beginning of each year.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as minimum investment amounts, exclusivity rules between products, or mandatory allocation to specific products?

## Turn 7 - User Simulator

No, there are no other constraints or requirements.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total value of principal plus interest at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Cash Flow Rule:** Funds from maturing investments become available at the beginning of the subsequent year and can be reinvested.
5.  **Investment Products:**
    *   **Product (1):** 1-year term. Available at the beginning of Years 1, 2, and 3. Returns 1.20x investment at year-end. Unlimited capacity. Single lump sum per year.
    *   **Product (2):** 2-year term. Available only at the beginning of Year 1. Returns 1.50x investment at the end of Year 2. Capacity capped at 120,000 yuan. Single lump sum.
    *   **Product (3):** Same-year term. Available only at the beginning of Year 2. Returns 1.60x investment at the end of Year 2. Capacity capped at 150,000 yuan. Single lump sum.
    *   **Product (4):** 1-year term. Available only at the beginning of Year 3. Returns 1.40x investment at the end of Year 3. Capacity capped at 100,000 yuan. Single lump sum.
6.  **Constraints:**
    *   Investment in Product (2) $\le$ 120,000 yuan.
    *   Investment in Product (3) $\le$ 150,000 yuan.
    *   Investment in Product (4) $\le$ 100,000 yuan.
    *   No other constraints (no minimums, no exclusivity, no mandatory allocations).
7.  **Variable Domain:**
    *   **Assumed:** Investment amounts are continuous non-negative real numbers (integrality was not confirmed and is treated as an assumption).