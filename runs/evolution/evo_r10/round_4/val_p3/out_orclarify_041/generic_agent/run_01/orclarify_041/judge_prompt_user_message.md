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

QUESTION: Is there any minimum investment amount required for each product, or can you invest any amount (including zero) in each available product?

## Turn 1 - User Simulator

There is no minimum investment amount. You can invest any amount, including zero, in each available product.

## Turn 2 - Generic Agent

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., all matured proceeds from investments that mature at the end of Year 3), or should any uninvested cash also count toward the total?

## Turn 2 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes all matured proceeds from investments that mature at the end of Year 3, as well as any uninvested cash.

## Turn 3 - Generic Agent

QUESTION: Can uninvested cash be carried forward from one year to the next (i.e., cash not invested at the beginning of a year simply rolls over to the beginning of the following year), or must all available cash be invested each year?

## Turn 3 - User Simulator

Uninvested cash can be carried forward from one year to the next. You are not required to invest all available cash each year.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited as stated?

## Turn 4 - User Simulator

Product (1) is truly unlimited. There is no cap on the total amount that can be invested in it across the three years.

## Turn 5 - Generic Agent

QUESTION: Is there any constraint on the total amount that can be invested in a single year (i.e., a per-year budget cap), or is the only limit the initial 500,000 yuan plus whatever cash is available from maturing investments?

## Turn 5 - User Simulator

There is no per-year budget cap. The only limit is the cash available at the beginning of each year, which comes from the initial 500,000 yuan and proceeds from investments that have already matured.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints or rules I should be aware of, such as transaction fees, taxes, or a requirement to maintain a minimum cash reserve at any point in time?

## Turn 6 - User Simulator

No. There are no transaction fees, taxes, or minimum cash reserve requirements. The only constraints are the individual product caps for products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 7 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash on hand at the end of Year 3 (all matured proceeds plus any uninvested cash).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Invest I at the start of a year → receive 1.20·I at that year's end. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, pays 1.50·I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, pays 1.60·I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, pays 1.40·I. Capped at 100,000 yuan.

**Constraints:**
- No minimum investment (zero is allowed).
- No borrowing: investments in any year cannot exceed cash available at the beginning of that year.
- Uninvested cash carries forward to the next year.
- No per-year budget cap beyond available cash.
- No transaction fees, taxes, or minimum cash reserve.
- Product caps: (2) ≤ 120,000; (3) ≤ 150,000; (4) ≤ 100,000.

**Decision variables:** Amount invested in each product at each available time point (continuous, non-negative).

**Cash flow structure:**
- Beginning of Year 1: 500,000 available → allocate to Product (1) Year 1, Product (2), and carry-forward.
- End of Year 1: 1.20 × (Product 1 Year 1 investment) matures.
- Beginning of Year 2: cash from Year 1 maturity + carry-forward → allocate to Product (1) Year 2, Product (3), and carry-forward.
- End of Year 2: 1.20 × (Product 1 Year 2) + 1.50 × (Product 2) + 1.60 × (Product 3) mature.
- Beginning of Year 3: cash from Year 2 maturities + carry-forward → allocate to Product (1) Year 3, Product (4), and carry-forward.
- End of Year 3: 1.20 × (Product 1 Year 3) + 1.40 × (Product 4) + carry-forward = total cash on hand (objective).