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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash held idle) counted in the final "total principal plus interest" objective, or does the objective only include the proceeds from investments that mature at the end of Year 3?

## Turn 1 - User Simulator

The objective is to maximize your total wealth at the end of Year 3. Therefore, any cash held idle at the end of Year 3 is counted in the final total. It is not limited to only the proceeds from investments that mature at that time.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is it available at the beginning of Year 3 as well (so you can invest at the start of Year 3 and receive 1.20·I at the end of Year 3), or is it only available at the beginnings of Years 1 and 2?

## Turn 2 - User Simulator

Product (1) is available at the beginning of Year 3. You can invest at the start of Year 3 and receive 1.20·I at the end of Year 3.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in any given year, or is it truly unlimited in each of Years 1, 2, and 3?

## Turn 3 - User Simulator

Product (1) has unlimited capacity in each of Years 1, 2, and 3.

## Turn 4 - Generic Agent

QUESTION: Can you invest in product (1) at the beginning of Year 2 using the proceeds from product (1) that matured at the end of Year 1, or are there any restrictions on reinvesting returns from one product into another?

## Turn 4 - User Simulator

Yes, you can invest in product (1) at the beginning of Year 2 using the proceeds from product (1) that matured at the end of Year 1. There are no restrictions on reinvesting returns from one product into another, as long as you only use cash available at that moment and do not borrow.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any non-negative amount (including zero) in each product?

## Turn 5 - User Simulator

There is no minimum investment amount required. You can invest any non-negative amount, including zero, in each product.

## Turn 6 - Generic Agent

QUESTION: Are the investments in each product required to be whole numbers (e.g., whole yuan), or can you invest any continuous (fractional) amount?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Is there any other product or investment option available besides the four products described, or are these the only four investment choices across the three years?

## Turn 7 - User Simulator

These are the only four investment choices available across the three years.

## Turn 8 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax applied when investing in or receiving proceeds from any of the four products, or are the stated returns (1.20, 1.50, 1.60, 1.40) the exact amounts received with no deductions?

## Turn 8 - User Simulator

The stated returns (1.20, 1.50, 1.60, 1.40) are the exact amounts received with no deductions. There are no transaction costs, fees, or taxes applied.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on the total amount you can invest across all products in a single year, or is the only constraint the per-product caps you mentioned (120,000 for product 2, 150,000 for product 3, 100,000 for product 4)?

## Turn 9 - User Simulator

There is no limit on the total amount you can invest across all products in a single year. The only constraints are the per-product caps: 120,000 yuan for product (2), 150,000 yuan for product (3), and 100,000 yuan for product (4).

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total wealth (cash + investment proceeds) at the end of Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**
1. **Product (1):** 1-year, available at the beginning of Years 1, 2, and 3. Returns 1.20·I at year-end. Unlimited capacity.
2. **Product (2):** 2-year, available only at the beginning of Year 1. Matures at end of Year 2, pays 1.50·I. Capped at 120,000 yuan.
3. **Product (3):** Same-year, available only at the beginning of Year 2. Matures at end of Year 2, pays 1.60·I. Capped at 150,000 yuan.
4. **Product (4):** 1-year, available only at the beginning of Year 3. Matures at end of Year 3, pays 1.40·I. Capped at 100,000 yuan.

**Constraints:**
- Per-product caps: Product (2) ≤ 120,000; Product (3) ≤ 150,000; Product (4) ≤ 100,000.
- No borrowing: investments in any period cannot exceed cash available at that time.
- No minimum investment; any non-negative amount allowed.
- No transaction costs, fees, or taxes.
- No total annual investment limit beyond the per-product caps.
- Reinvestment of proceeds is unrestricted.
- Idle cash at end of Year 3 counts toward the objective.

**Deferred (non-load-bearing):** Whether investments must be whole numbers or can be fractional — the client deferred this. I will model with continuous (fractional) variables, which is the standard default and does not change the optimal structure.