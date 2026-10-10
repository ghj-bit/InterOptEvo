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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment, or can you also draw on external financing or carry over uninvested cash between years?

## Turn 1 - User Simulator

The 500,000 yuan initial capital is the only external source of funds. You cannot borrow money. However, you can carry over uninvested cash between years. At the beginning of each year, you can invest any cash you have available, which includes your initial capital, proceeds from investments that have already matured, and any uninvested cash carried over from previous years.

## Turn 2 - Generic Agent

QUESTION: Can you invest in product (1) more than once during the same year, or is there a limit on the number of times you can purchase it within a single year?

## Turn 2 - User Simulator

There is no limit on the number of times you can purchase product (1) within a single year. It is available at the beginning of each year, and you can invest any amount of your available cash in it.

## Turn 3 - Generic Agent

QUESTION: Is the 120,000 yuan cap on product (2) a total limit across all years, or is it a limit per year?

## Turn 3 - User Simulator

The 120,000 yuan cap on product (2) is a total limit. Since product (2) is only available at the beginning of Year 1, the entire investment in this product must be made at that single time and cannot exceed 120,000 yuan.

## Turn 4 - Generic Agent

QUESTION: Is the 150,000 yuan cap on product (3) a total limit across all years, or is it a limit per year?

## Turn 4 - User Simulator

The 150,000 yuan cap on product (3) is a total limit. Since product (3) is only available at the beginning of Year 2, the entire investment in this product must be made at that single time and cannot exceed 150,000 yuan.

## Turn 5 - Generic Agent

QUESTION: Is the 100,000 yuan cap on product (4) a total limit across all years, or is it a limit per year?

## Turn 5 - User Simulator

The 100,000 yuan cap on product (4) is a total limit. Since product (4) is only available at the beginning of Year 3, the entire investment in this product must be made at that single time and cannot exceed 100,000 yuan.

## Turn 6 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can you invest any positive amount in each?

## Turn 6 - User Simulator

There are no minimum investment amounts required for any of the four products. You can invest any positive amount in each, subject to the available cash and the maximum caps for products (2), (3), and (4).

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about, such as mandatory diversification rules, liquidity requirements, or restrictions on how much cash can be carried over?

## Turn 7 - User Simulator

No, there are no other constraints or requirements. There are no mandatory diversification rules, liquidity requirements, or restrictions on how much cash can be carried over. The only constraints are the maximum investment caps for products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 8 - Generic Agent

QUESTION: Can you invest zero in any of the products, or must you invest a positive amount in each product that is available?

## Turn 8 - User Simulator

You can invest zero in any of the products. There is no requirement to invest a positive amount in each available product.

## Turn 9 - Generic Agent

QUESTION: Is the objective to maximize the total value of all matured investments plus any uninvested cash at the end of Year 3, or only the total value of matured investments?

## Turn 9 - User Simulator

The objective is to maximize the total value of all matured investments plus any uninvested cash at the end of Year 3.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize total wealth at the end of Year 3, which includes the proceeds from all matured investments plus any uninvested cash carried over.

2. **Time Horizon:** Three years (Year 1, Year 2, Year 3).

3. **Initial Capital:** 500,000 yuan available at the beginning of Year 1.

4. **Funding Rules:**
   - No borrowing allowed.
   - Uninvested cash can be carried over between years.
   - At the beginning of each year, available cash includes initial capital, proceeds from matured investments, and carried-over cash.

5. **Investment Products:**
   - **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20× investment at year-end. Unlimited capacity. No minimum investment. Can invest zero.
   - **Product (2):** 2-year product, available only at the beginning of Year 1. Returns 1.50× investment at end of Year 2. Maximum total investment: 120,000 yuan. No minimum investment. Can invest zero.
   - **Product (3):** Same-year product, available only at the beginning of Year 2. Returns 1.60× investment at end of Year 2. Maximum total investment: 150,000 yuan. No minimum investment. Can invest zero.
   - **Product (4):** 1-year product, available only at the beginning of Year 3. Returns 1.40× investment at end of Year 3. Maximum total investment: 100,000 yuan. No minimum investment. Can invest zero.

6. **Constraints:**
   - Investment in Product (2) ≤ 120,000 yuan (total, single purchase at start of Year 1).
   - Investment in Product (3) ≤ 150,000 yuan (total, single purchase at start of Year 2).
   - Investment in Product (4) ≤ 100,000 yuan (total, single purchase at start of Year 3).
   - No borrowing.
   - No other constraints (no diversification rules, no liquidity requirements, no carry-over restrictions).

7. **Decision Variables:**
   - Amount invested in Product (1) at the beginning of Year 1, Year 2, and Year 3.
   - Amount invested in Product (2) at the beginning of Year 1.
   - Amount invested in Product (3) at the beginning of Year 2.
   - Amount invested in Product (4) at the beginning of Year 3.
   - Uninvested cash carried over at the end of each year.

8. **Assumptions:** None. All key facts have been confirmed.