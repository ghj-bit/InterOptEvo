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

QUESTION: Is there any minimum investment amount required for any of the four products?

## Turn 1 - User Simulator

No, there is no minimum investment amount required for any of the four products.

## Turn 2 - Generic Agent

QUESTION: Can the funds received from a product maturing at the end of a year be immediately reinvested in products available at the beginning of the next year?

## Turn 2 - User Simulator

Yes. The proceeds from investments that mature at the end of a year are available as cash at the beginning of the next year and can be reinvested in products available at that time.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years combined?

## Turn 3 - User Simulator

No, there is no limit on the total amount that can be invested in product (1) across all three years. It has unlimited capacity.

## Turn 4 - Generic Agent

QUESTION: Are there any transaction fees, taxes, or other costs associated with investing in or redeeming any of the four products?

## Turn 4 - User Simulator

No, there are no transaction fees, taxes, or other costs associated with investing in or redeeming any of the four products.

## Turn 5 - Generic Agent

QUESTION: Is the initial capital of 500,000 yuan the only source of funds available for investment, or can additional external funds be injected during the three-year period

## Turn 5 - User Simulator

The initial capital of 500,000 yuan is the only source of funds available for investment. No additional external funds can be injected during the three-year period.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total cash (principal plus interest) at the end of Year 3.
- **Initial capital:** 500,000 yuan at the beginning of Year 1. No additional external funds.
- **Reinvestment:** Proceeds from products maturing at the end of a year are available as cash at the beginning of the next year for reinvestment.
- **No minimums, fees, or taxes** on any product.

**Products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at year-end. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at end of Year 2, pays 1.50×I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at end of Year 2, pays 1.60×I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at end of Year 3, pays 1.40×I. Capped at 100,000 yuan.

**Constraints:**
- Total invested at the beginning of each year cannot exceed available cash.
- Product (2) ≤ 120,000 yuan.
- Product (3) ≤ 150,000 yuan.
- Product (4) ≤ 100,000 yuan.
- All investment amounts ≥ 0.