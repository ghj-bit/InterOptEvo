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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment, or can you also invest the returns (principal plus interest) received from maturing products in subsequent years

## Turn 1 - User Simulator

The 500,000 yuan is not the only source of funds. You can also invest the returns (principal plus interest) received from maturing products in subsequent years. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the investment amount at the beginning of Year 1, Year 2, and Year 3 treated as three separate decision variables that can each be different amounts

## Turn 2 - User Simulator

Yes, the investment amount in product (1) at the beginning of Year 1, Year 2, and Year 3 are three separate decisions that can each be different amounts.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum investment requirements for any of the four products

## Turn 3 - User Simulator

No, there are no minimum investment requirements for any of the four products.

## Turn 4 - Generic Agent

QUESTION: Are the investment amounts for all four products required to be non

## Turn 4 - User Simulator

Yes, investment amounts for all four products must be non-negative.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts required to be integer values

## Turn 5 - User Simulator

No, the investment amounts are not required to be integer values.

## Turn 6 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year 3

## Turn 6 - User Simulator

Yes, the objective is to maximize the total principal plus interest at the end of Year 3.

## Turn 7 - Generic Agent

QUESTION: Is the 120,000 yuan cap for product (2) a total limit across all years

## Turn 7 - User Simulator

Yes, the 120,000 yuan cap for product (2) is a total limit. Since product (2) is only available at the beginning of Year 1, the entire investment in this product must not exceed 120,000 yuan.

## Turn 8 - Generic Agent

QUESTION: Is the 150,000 yuan cap for product (3) a

## Turn 8 - User Simulator

Yes, the 150,000 yuan cap for product (3) is a total limit. Since product (3) is only available at the beginning of Year 2, the entire investment in this product must not exceed 150,000 yuan.

## Turn 9 - Generic Agent

QUESTION: Is the 100,000 yuan cap for product (4)

## Turn 9 - User Simulator

Yes, the 100,000 yuan cap for product (4) is a total limit. Since product (4) is only available at the beginning of Year 3, the entire investment in this product must not exceed 100,000 yuan.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total cash (principal plus interest) available at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan available at the beginning of Year 1.
4.  **Cash Flow Rule:** At the beginning of each year, available cash consists of the initial capital (Year 1 only) plus proceeds from investments that matured at the end of the previous year. All available cash must be allocated to investments or held as cash (though holding cash yields 0, so it will likely be invested if profitable options exist).
5.  **Decision Variables:**
    *   $I_{1,1}$: Amount invested in Product 1 at the beginning of Year 1.
    *   $I_{1,2}$: Amount invested in Product 1 at the beginning of Year 2.
    *   $I_{1,3}$: Amount invested in Product 1 at the beginning of Year 3.
    *   $I_{2,1}$: Amount invested in Product 2 at the beginning of Year 1.
    *   $I_{3,2}$: Amount invested in Product 3 at the beginning of Year 2.
    *   $I_{4,3}$: Amount invested in Product 4 at the beginning of Year 3.
6.  **Variable Domains:** All decision variables are continuous and non-negative.
7.  **Investment Products & Returns:**
    *   **Product 1 (1-year):** Available at start of Years 1, 2, 3. Returns 1.20x investment at year-end. Unlimited capacity.
    *   **Product 2 (2-year):** Available only at start of Year 1. Returns 1.50x investment at end of Year 2.
    *   **Product 3 (Same-year/1-year):** Available only at start of Year 2. Returns 1.60x investment at end of Year 2.
    *   **Product 4 (1-year):** Available only at start of Year 3. Returns 1.40x investment at end of Year 3.
8.  **Constraints:**
    *   **Year 1 Budget:** $I_{1,1} + I_{2,1} \le 500,000$.
    *   **Year 2 Budget:** $I_{1,2} + I_{3,2} \le 1.20 \cdot I_{1,1}$. (Cash available is proceeds from Product 1 invested in Year 1).
    *   **Year 3 Budget:** $I_{1,3} + I_{4,3} \le 1.20 \cdot I_{1,2} + 1.50 \cdot I_{2,1} + 1.60 \cdot I_{3,2}$. (Cash available is proceeds from Product 1 invested in Year 2, Product 2 invested in Year 1, and Product 3 invested in Year 2).
    *   **Product 2 Cap:** $I_{2,1} \le 120,000$.
    *   **Product 3 Cap:** $I_{3,2} \le 150,000$.
    *   **Product 4 Cap:** $I_{4,3} \le 100,000$.
    *   **Non-negativity:** All $I \ge 0$.
9.  **Objective Function:** Maximize $Z = 1.20 \cdot I_{1,3} + 1.40 \cdot I_{4,3}$. (Only investments maturing at the end of Year 3 contribute to the final cash balance. Note: Product 1 invested in Year 3 matures at end of Year 3. Product 4 invested in Year 3 matures at end of Year 3. Products maturing in Year 2 have already been reinvested in Year 3).

**Assumptions:**
*   None. All critical facts were confirmed.