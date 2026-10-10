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

QUESTION: For the 1-year product (1), is the 20% return a simple annual interest rate applied to the principal invested at the start of that specific year, or does it represent a compound annual growth rate that applies to the total accumulated balance?

## Turn 2 - User Simulator

The 20% return is a simple annual interest rate applied to the principal invested at the start of that specific year.

## Turn 3 - Generic Agent

QUESTION: Are there any transaction fees, taxes, or other costs associated with investing in or redeeming any of the four products?

## Turn 3 - User Simulator

I don't have information about transaction fees, taxes, or other costs for these products. That point still needs internal confirmation.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can any positive amount be invested in each product?

## Turn 4 - User Simulator

I don't have information about minimum investment amounts for these products. That point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Can the funds received from maturing investments be immediately reinvested in other products available at that same time point, or is there a delay or restriction on reinvestment?

## Turn 5 - User Simulator

Funds received from maturing investments can be immediately reinvested in other products available at that same time point. There is no delay or restriction on reinvestment.

## Turn 6 - Generic Agent

QUESTION: Is there a requirement to maintain a minimum cash balance or liquidity reserve at any point during the three-year period, or can all available funds be fully invested at each decision point?

## Turn 6 - User Simulator

I don't have information about a minimum cash balance or liquidity reserve requirement. That point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any constraints on the total amount that can be invested in product (1) across the three years, or is the only limit on product (1) that it is unlimited in capacity?

## Turn 7 - User Simulator

The only limit on product (1) is that it has unlimited capacity. There are no constraints on the total amount that can be invested in product (1) across the three years.

## Turn 8 - Generic Agent

QUESTION: Is there a requirement to invest all available funds at each decision point, or can some funds be held as cash with zero return?

## Turn 8 - User Simulator

I don't have information about whether funds must be fully invested or can be held as cash with zero return. That point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Are there any other investment products or opportunities available during the three-year period besides the four products listed?

## Turn 9 - User Simulator

No, there are no other investment products or opportunities available during the three-year period besides the four products listed.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**
1.  **Objective:** Maximize total principal plus interest at the end of Year 3.
2.  **Time Horizon:** 3 years (Year 1, Year 2, Year 3).
3.  **Initial Capital:** 500,000 yuan at the beginning of Year 1.
4.  **Funding Source:** The initial 500,000 yuan is the only external source of funds; no additional injections occur.
5.  **Reinvestment:** Funds from maturing investments can be immediately reinvested at the same time point.
6.  **Product (1):** 1-year term, available at the start of Years 1, 2, and 3. Returns 1.20 * I at the end of the year. Unlimited capacity. Simple annual interest.
7.  **Product (2):** 2-year term, available only at the start of Year 1. Matures at the end of Year 2. Returns 1.50 * I. Capacity capped at 120,000 yuan.
8.  **Product (3):** Same-year term (1-year), available only at the start of Year 2. Matures at the end of Year 2. Returns 1.60 * I. Capacity capped at 150,000 yuan.
9.  **Product (4):** 1-year term, available only at the start of Year 3. Matures at the end of Year 3. Returns 1.40 * I. Capacity capped at 100,000 yuan.
10. **Exclusivity:** No other investment products are available.

**Assumptions (due to lack of information):**
1.  **Transaction Costs/Taxes:** It is assumed there are no transaction fees, taxes, or other costs associated with investing or redeeming any product.
2.  **Minimum Investments:** It is assumed there are no minimum investment amounts for any product; any non-negative amount can be invested.
3.  **Liquidity Reserve:** It is assumed there is no requirement to maintain a minimum cash balance or liquidity reserve at any point.
4.  **Cash Holding:** It is assumed that funds can be held as cash with zero return if not invested, although given the positive returns on all products, this is likely suboptimal unless capacity constraints prevent full investment.
5.  **Variable Domain:** Investment amounts are assumed to be continuous non-negative variables.