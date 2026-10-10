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

QUESTION: For the 1-year product (1) that is available at the beginning of each year, is the 120,000 yuan cap on product (2) a limit on the total amount invested in product (2) over the entire three-year horizon, or is it a limit on the amount that can be invested in any single year

## Turn 1 - User Simulator

The 120,000 yuan cap applies to the total amount invested in product (2) over the entire three-year horizon. Since product (2) is only available at the beginning of Year 1, this means the maximum you can invest in it is 120,000 yuan at the start of Year 1.

## Turn 2 - Generic Agent

QUESTION: Is the 150,000 yuan cap on product (3) a limit on the total amount invested in product (3) over the entire three-year

## Turn 2 - User Simulator

The 150,000 yuan cap is a limit on the total amount invested in product (3) over the entire three-year horizon. Since product (3) is only available at the beginning of Year 2, this means the maximum you can invest in it is 150,000 yuan at the start of Year 2.

## Turn 3 - Generic Agent

QUESTION: Is the 100,000 yuan cap on product (4) a limit on the total amount invested in product (4)

## Turn 3 - User Simulator

The 100,000 yuan cap is a limit on the total amount invested in product (4) over the entire three-year horizon. Since product (4) is only available at the beginning of Year 3, this means the maximum you can invest in it is 100,000 yuan at the start of Year 3.

## Turn 4 - Generic Agent

QUESTION: When funds from a maturing investment are received at the end of a year, are they immediately available to be invested in products available at the

## Turn 4 - User Simulator

Yes, funds from a maturing investment received at the end of a year are immediately available to be invested in products available at the beginning of the next year.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product

## Turn 5 - User Simulator

No, there is no limit on the total amount that can be invested in product (1). It has unlimited capacity.

## Turn 6 - Generic Agent

QUESTION: Are there any transaction costs, fees, or taxes associated

## Turn 6 - User Simulator

The business facts provided do not mention any transaction costs, fees, or taxes. This point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Since transaction costs, fees, and taxes are not confirmed, should I assume that all investment returns are net of any such costs and that the stated multipliers (1.20, 1.50, 1.60, 1.40) represent the final amount

## Turn 7 - User Simulator

The business facts do not specify whether the stated multipliers are net of costs or taxes. This point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Are the investment amounts required to be whole numbers

## Turn 8 - User Simulator

The business facts do not specify whether investment amounts must be whole numbers. This point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Can you invest in multiple different

## Turn 9 - User Simulator

Yes, you can invest in multiple different products at the beginning of a year, as long as the total amount invested does not exceed the cash available at that time and each product's individual cap is respected.

## Turn 10 - Generic Agent

QUESTION: Is it allowed to leave some cash un

## Turn 10 - User Simulator

The business facts do not specify whether it is allowed to leave some cash uninvested. This point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: If cash is left un

## Turn 11 - User Simulator

The business facts do not specify what happens to cash left uninvested. This point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there a minimum

## Turn 12 - User Simulator

The business facts do not specify any minimum investment amount for any product. This point still needs internal confirmation.

## Turn 13 - Generic Agent

QUESTION: Are there any

## Turn 13 - User Simulator

The business facts do not provide information about any other constraints or conditions. This point still needs internal confirmation.

## Turn 14 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize total principal plus interest at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Decision Variables:**
    *   $I_{1,t}$: Amount invested in Product 1 at the beginning of Year $t$ (for $t=1, 2, 3$).
    *   $I_{2,1}$: Amount invested in Product 2 at the beginning of Year 1.
    *   $I_{3,2}$: Amount invested in Product 3 at the beginning of Year 2.
    *   $I_{4,3}$: Amount invested in Product 4 at the beginning of Year 3.
    *   $C_t$: Cash available at the beginning of Year $t$ (for $t=1, 2, 3$).
5.  **Product Details & Constraints:**
    *   **Product 1:** 1-year term, available at start of Years 1, 2, 3. Return: $1.20 \times I$. Capacity: Unlimited.
    *   **Product 2:** 2-year term, available only at start of Year 1. Matures end of Year 2. Return: $1.50 \times I$. Capacity: $\le 120,000$ yuan.
    *   **Product 3:** Same-year term (1-year), available only at start of Year 2. Matures end of Year 2. Return: $1.60 \times I$. Capacity: $\le 150,000$ yuan.
    *   **Product 4:** 1-year term, available only at start of Year 3. Matures end of Year 3. Return: $1.40 \times I$. Capacity: $\le 100,000$ yuan.
6.  **Cash Flow Rules:**
    *   Funds from investments maturing at the end of Year $t$ are available for investment at the beginning of Year $t+1$.
    *   Multiple products can be invested in simultaneously at the beginning of a year.
    *   Total investment at the beginning of any year cannot exceed the cash available at that time.
7.  **Open Assumptions (Flagged as Unconfirmed):**
    *   **Transaction Costs/Taxes:** It is assumed that the stated return multipliers (1.20, 1.50, 1.60, 1.40) are net of all costs and taxes, and no additional deductions apply.
    *   **Integrality:** It is assumed that investment amounts can be continuous (fractional yuan is allowed).
    *   **Uninvested Cash:** It is assumed that any cash not invested at the beginning of a year carries over to the next year with zero interest (i.e., it remains as cash available for future investment).
    *   **Minimum Investment:** It is assumed there are no minimum investment amounts for any product.
    *   **Other Constraints:** It is assumed there are no other hidden constraints or conditions.