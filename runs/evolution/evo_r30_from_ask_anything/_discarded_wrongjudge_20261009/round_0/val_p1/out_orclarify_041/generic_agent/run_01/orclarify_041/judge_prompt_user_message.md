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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment, or can you also use funds received from maturing investments in subsequent years to make new investments

## Turn 1 - User Simulator

You can use funds received from maturing investments in subsequent years to make new investments. The 500,000 yuan is the starting capital, but as investments mature, the proceeds become available cash that can be reinvested in the following years.

## Turn 2 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four

## Turn 2 - User Simulator

No, there are no minimum investment amounts required for any of the four products.

## Turn 3 - Generic Agent

QUESTION: Can the investment amounts for each product be any real number (continuous), or

## Turn 3 - User Simulator

The investment amounts can be any real number (continuous).

## Turn 4 - Generic Agent

QUESTION: Are there any transaction

## Turn 4 - User Simulator

No, there are no transaction fees or costs associated with investing in any of the four products.

## Turn 5 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year 3, assuming that any funds not invested in a product simply remain as cash

## Turn 5 - User Simulator

Yes, the objective is to maximize the total cash available at the end of Year 3. Any funds not invested in a product simply remain as cash and count toward that total.

## Turn 6 - Generic Agent

READY_TO_MODEL

Here is the confirmed understanding of your investment planning problem:

**Objective:** Maximize total cash available at the end of Year 3.

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Investment Products:**
1.  **Product 1:** 1-year term, available at the start of Years 1, 2, and 3. Returns 1.20x principal at year-end. Unlimited capacity.
2.  **Product 2:** 2-year term, available only at the start of Year 1. Returns 1.50x principal at the end of Year 2. Capacity capped at 120,000 yuan.
3.  **Product 3:** Same-year term (start to end of Year 2), available only at the start of Year 2. Returns 1.60x principal at the end of Year 2. Capacity capped at 150,000 yuan.
4.  **Product 4:** 1-year term, available only at the start of Year 3. Returns 1.40x principal at the end of Year 3. Capacity capped at 100,000 yuan.

**Constraints & Rules:**
*   **Reinvestment:** Proceeds from maturing investments are immediately available for reinvestment in subsequent years.
*   **Cash Holding:** Uninvested funds remain as cash and count toward the final total.
*   **No Fees:** No transaction costs or fees.
*   **No Minimums:** No minimum investment amounts.
*   **Continuous Variables:** Investment amounts can be any real number.
*   **Capacity Limits:**
    *   Product 2: ≤ 120,000 yuan
    *   Product 3: ≤ 150,000 yuan
    *   Product 4: ≤ 100,000 yuan
    *   Product 1: Unlimited