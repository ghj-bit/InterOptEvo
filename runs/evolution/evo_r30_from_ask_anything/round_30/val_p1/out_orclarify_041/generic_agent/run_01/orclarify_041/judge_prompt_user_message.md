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

QUESTION: When you say "investment in product (2) cannot exceed 120,000 yuan," does this cap apply to the total amount invested in product (2) across all years, or is it a per-year limit (though product 2 is only available in Year 1)?

## Turn 2 - User Simulator

The 120,000 yuan cap applies to the total amount invested in product (2). Since product (2) is only available at the beginning of Year 1, this is effectively the limit for that single investment opportunity.

## Turn 3 - Generic Agent

QUESTION: Does the 150,000 yuan cap for product (3) apply to the total amount invested in that product, or is it a per-year limit (though product 3 is only available in Year 2)?

## Turn 3 - User Simulator

The 150,000 yuan cap applies to the total amount invested in product (3). Since product (3) is only available at the beginning of Year 2, this is effectively the limit for that single investment opportunity.

## Turn 4 - Generic Agent

QUESTION: Does the 100,000 yuan cap for product (4) apply to the total amount invested in that product, or is it a per-year limit (though product 4 is only available in Year 3)?

## Turn 4 - User Simulator

The 100,000 yuan cap applies to the total amount invested in product (4). Since product (4) is only available at the beginning of Year 3, this is effectively the limit for that single investment opportunity.

## Turn 5 - Generic Agent

QUESTION: Are there any minimum investment requirements for any of the four products, or can you invest any non-negative amount up to the stated caps?

## Turn 5 - User Simulator

There are no minimum investment requirements. You can invest any non-negative amount up to the stated caps for each product.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as mandatory diversification rules, liquidity requirements, or restrictions on how funds can be carried over between years?

## Turn 6 - User Simulator

No, there are no other constraints or requirements. The only rules are the investment caps for products (2), (3), and (4), and the fact that you cannot borrow money. You can only invest cash that is currently available from your initial capital and proceeds from matured investments.

## Turn 7 - Generic Agent

QUESTION: When you say "maximize total principal plus interest at the end of Year 3," does this mean the objective is to maximize the total cash value of all matured investments at the end of Year 3, assuming any uninvested cash also carries over to that date?

## Turn 7 - User Simulator

Yes, the objective is to maximize the total cash value at the end of Year 3. This includes the proceeds from all investments that mature by the end of Year 3, plus any uninvested cash carried over to that date.

## Turn 8 - Generic Agent

QUESTION: Is it possible to invest in product (1) at the beginning of Year 2 and Year 3, or is product (1) only available at the beginning of Year 1?

## Turn 8 - User Simulator

Product (1) is available at the beginning of each year (Years 1–3).

## Turn 9 - Generic Agent

QUESTION: Are there any transaction costs, fees, or taxes associated with investing in or redeeming any of the four products?

## Turn 9 - User Simulator

No, there are no transaction costs, fees, or taxes associated with investing in or redeeming any of the four products.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize total cash value at the end of Year 3, including proceeds from all matured investments plus any uninvested cash carried over. (Confirmed)

2. **Initial Capital:** 500,000 yuan available at the beginning of Year 1. No additional external funds will be injected during the three-year period. (Confirmed)

3. **Investment Products:**
   - **Product (1):** 1-year product available at the beginning of Years 1, 2, and 3. Returns 1.20×I at year-end. Unlimited capacity. No minimum investment. (Confirmed)
   - **Product (2):** 2-year product available only at the beginning of Year 1. Matures at end of Year 2, pays 1.50×I. Total investment capped at 120,000 yuan. No minimum investment. (Confirmed)
   - **Product (3):** Same-year product available only at the beginning of Year 2. Matures at end of Year 2, pays 1.60×I. Total investment capped at 150,000 yuan. No minimum investment. (Confirmed)
   - **Product (4):** 1-year product available only at the beginning of Year 3. Matures at end of Year 3, pays 1.40×I. Total investment capped at 100,000 yuan. No minimum investment. (Confirmed)

4. **Constraints:**
   - Investment in Product (2) ≤ 120,000 yuan (total). (Confirmed)
   - Investment in Product (3) ≤ 150,000 yuan (total). (Confirmed)
   - Investment in Product (4) ≤ 100,000 yuan (total). (Confirmed)
   - No borrowing allowed; only currently available cash (initial capital + matured proceeds) can be invested. (Confirmed)
   - No minimum investment requirements for any product. (Confirmed)
   - No transaction costs, fees, or taxes. (Confirmed)
   - No other constraints (diversification, liquidity, etc.). (Confirmed)

5. **Assumptions:**
   - All investments are made at the beginning of the specified year and mature at the end of the specified year. (Confirmed)
   - Cash flows are deterministic; no uncertainty in returns. (Assumed, as no uncertainty was mentioned)
   - Investments can be fractional (continuous variables), not restricted to integer units. (Assumed, as no integrality requirement was mentioned)