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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., the sum of all matured proceeds from products 1, 2, 3, and 4), or should any uninvested cash (idle cash) also count toward the total?

## Turn 1 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes both the matured proceeds from the investment products and any uninvested cash (idle cash) that remains.

## Turn 2 - Generic Agent

QUESTION: When you say "uninvested cash (idle cash) that remains" counts toward the total at the end of Year 3, does that idle cash earn any interest, or is it simply carried forward at face value (1.00) with no return?

## Turn 2 - User Simulator

Idle cash is simply carried forward at face value (1.00) with no return.

## Turn 3 - Generic Agent

QUESTION: Product (1) is a 1-year product available at the beginning of each year (Years 1–3). If you invest in product (1) at the beginning of Year 3, it matures at the end of Year 3 and pays 1.20·I. Is this correct, or does product (1) at the beginning of Year 3 mature at the end of Year 4 (i.e., after the planning horizon)?

## Turn 3 - User Simulator

That is correct. If you invest in product (1) at the beginning of Year 3, it matures at the end of Year 3 and pays 1.20·I.

## Turn 4 - Generic Agent

QUESTION: Product (2) is a 2-year product available only at the beginning of Year 1, maturing at the end of Year 2. After it matures at the end of Year 2, can the proceeds (1.50·I) be reinvested in product (1) at the beginning of Year 3 (which matures at the end of Year 3), or are the proceeds simply added to the cash on hand at the end of Year 3?

## Turn 4 - User Simulator

The proceeds from product (2) can be reinvested in product (1) at the beginning of Year 3.

## Turn 5 - Generic Agent

QUESTION: Product (3) is a same-year product available at the beginning of Year 2, maturing at the end of Year 2. After it matures at the end of Year 2, can the proceeds (1.60·I) be reinvested in product (1) at the beginning of Year 3, or are they simply added to the cash on hand at the end of Year 3?

## Turn 5 - User Simulator

The proceeds from product (3) can be reinvested in product (1) at the beginning of Year 3.

## Turn 6 - Generic Agent

QUESTION: Product (4) is a 1-year product available at the beginning of Year 3, maturing at the end of Year 3, paying 1.40·I. Is product (4) an alternative to product (1) at the beginning of Year 3 (i.e., you can invest in both product (1) and product (4) at the beginning of Year 3, subject to their respective caps), or is product (4) the only 1-year option available at the beginning of Year 3?

## Turn 6 - User Simulator

Product (4) is an alternative to product (1) at the beginning of Year 3. You can invest in both product (1) and product (4) at the beginning of Year 3, subject to their respective caps.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 1, you have 500,000 yuan. You can invest in product (1) (1-year, unlimited) and product (2) (2-year, capped at 120,000). Is there any minimum investment requirement for any product, or can you invest any non-negative amount (including zero) in each product?

## Turn 7 - User Simulator

There is no minimum investment requirement. You can invest any non-negative amount, including zero, in each product.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 2, the available products are product (1) (1-year, unlimited) and product (3) (same-year, capped at 150,000). The cash available at the beginning of Year 2 comes from the proceeds of product (1) invested at the beginning of Year 1 (1.20·I) plus any idle cash carried from Year 1. Is this correct, or is there any other source of cash at the beginning of Year 2?

## Turn 8 - User Simulator

That is correct. The cash available at the beginning of Year 2 comes from the proceeds of product (1) invested at the beginning of Year 1 (1.20·I) plus any idle cash carried from Year 1.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 3, the available products are product (1) (1-year, unlimited) and product (4) (1-year, capped at 100,000). The cash available at the beginning of Year 3 comes from the proceeds of product (1) invested at the beginning of Year 2 (1.20·I), the proceeds of product (3) (1.60·I), the proceeds of product (2) (1.50·I), plus any idle cash carried from Year 2. Is this correct, or is there any other source of cash at the beginning of Year 3?

## Turn 9 - User Simulator

That is correct. The cash available at the beginning of Year 3 comes from the proceeds of product (1) invested at the beginning of Year 2 (1.20·I), the proceeds of product (3) (1.60·I), the proceeds of product (2) (1.50·I), plus any idle cash carried from Year 2.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total cash on hand at the end of Year 3, which includes all matured proceeds from investments plus any idle cash carried forward at face value (no interest on idle cash).

**Planning Horizon:** 3 years (Year 1, Year 2, Year 3).

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Investment Products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Pays 1.20·I at the end of the same year. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, pays 1.50·I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, pays 1.60·I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, pays 1.40·I. Capped at 100,000 yuan.

**Cash Flow Structure:**

- **Beginning of Year 1:** 500,000 yuan available. Can invest in Product (1) and Product (2). Idle cash carries to Year 2 at face value.
- **Beginning of Year 2:** Cash = proceeds from Product (1) Year 1 (1.20·I) + idle cash from Year 1. Can invest in Product (1) and Product (3). Idle cash carries to Year 3 at face value.
- **Beginning of Year 3:** Cash = proceeds from Product (1) Year 2 (1.20·I) + proceeds from Product (3) (1.60·I) + proceeds from Product (2) (1.50·I) + idle cash from Year 2. Can invest in Product (1) and Product (4). Idle cash carries to end of Year 3 at face value.
- **End of Year 3:** Total cash = proceeds from Product (1) Year 3 (1.20·I) + proceeds from Product (4) (1.40·I) + idle cash from Year 3.

**Constraints:**
- All investments are non-negative (no minimum investment).
- Product (2) ≤ 120,000 yuan.
- Product (3) ≤ 150,000 yuan.
- Product (4) ≤ 100,000 yuan.
- Cash flow balance at each year boundary (cash available = sum of all incoming proceeds + idle cash from prior period).
- No borrowing (cash available cannot be negative).