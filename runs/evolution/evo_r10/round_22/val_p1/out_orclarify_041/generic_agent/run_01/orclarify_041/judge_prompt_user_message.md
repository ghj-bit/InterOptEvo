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

QUESTION: At the end of Year 3, do you want to count only the cash that has actually matured by then (i.e., the proceeds from products 1, 3, and 4, plus any cash you chose not to invest), or should any money still locked in a product that matures after Year 3 also be counted at its expected maturity value?

## Turn 1 - User Simulator

Only count the cash that has actually matured by the end of Year 3. That includes proceeds from products 1, 3, and 4, plus any cash you chose not to invest. Do not count any money still locked in a product that matures after Year 3.

## Turn 2 - Generic Agent

QUESTION: If you invest in product (1) at the beginning of Year 3, it matures at the end of Year 3 and pays 1.20·I — is that proceeds included in the end-of-Year-3 total, or should product (1) be treated as unavailable in Year 3?

## Turn 2 - User Simulator

The proceeds from product (1) invested at the beginning of Year 3 are included in the end-of-Year-3 total. Product (1) is available in Year 3.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum amount you must invest in each product, or can you invest zero in any of them (i.e., are all investments optional with a lower bound of zero)?

## Turn 3 - User Simulator

All investments are optional. You can invest zero in any of the products.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in a given year, or is it truly unlimited as stated?

## Turn 4 - User Simulator

Product (1) is truly unlimited. There is no cap on how much you can invest in it in a given year.

## Turn 5 - Generic Agent

QUESTION: Are there any transaction costs, taxes, or fees associated with investing in any of the products, or are the stated returns (1.20, 1.50, 1.60, 1.40) the net amounts you actually receive?

## Turn 5 - User Simulator

The stated returns (1.20, 1.50, 1.60, 1.40) are the net amounts you actually receive. There are no transaction costs, taxes, or fees.

## Turn 6 - Generic Agent

QUESTION: Can you invest in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1 and Year 3?

## Turn 6 - User Simulator

Yes, you can invest in product (1) at the beginning of Year 2. It is available at the beginning of each year (Years 1–3).

## Turn 7 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you hold cash (uninvested) from one year to the next without penalty?

## Turn 7 - User Simulator

You can hold cash (uninvested) from one year to the next without penalty. There is no requirement to invest all available cash at the beginning of each year.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you hold cash (uninvested) from one year to the next without penalty?

## Turn 8 - User Simulator

You can hold cash (uninvested) from one year to the next without penalty. There is no requirement to invest all available cash at the beginning of each year.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or rules I should be aware of, such as a minimum total investment, a requirement to diversify across products, or any other business rules that would affect the model?

## Turn 9 - User Simulator

No. There are no other constraints or rules. You cannot borrow money, and at the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 10 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash available at the end of Year 3 (proceeds from matured investments plus any uninvested cash).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

| Product | Type | Available | Matures | Return | Cap |
|---------|------|-----------|---------|--------|-----|
| (1) | 1-year | Beginning of Years 1, 2, 3 | End of same year | 1.20·I | Unlimited |
| (2) | 2-year | Beginning of Year 1 only | End of Year 2 | 1.50·I | 120,000 |
| (3) | Same-year | Beginning of Year 2 only | End of Year 2 | 1.60·I | 150,000 |
| (4) | 1-year | Beginning of Year 3 only | End of Year 3 | 1.40·I | 100,000 |

**Key rules confirmed:**
- All investments are optional (lower bound = 0).
- No borrowing; each year's investments are funded only by cash on hand (initial capital + proceeds from previously matured investments).
- Uninvested cash carries over to the next year with no penalty or interest.
- Returns are net (no fees, taxes, or transaction costs).
- Only cash that has actually matured by the end of Year 3 counts toward the objective.
- No other constraints (no minimum investment, no diversification requirement, no other business rules).

**Cash flow structure:**
- **Beginning of Year 1:** 500,000 available. Can invest in products (1) and (2).
- **End of Year 1 / Beginning of Year 2:** Cash = uninvested Year 1 cash + 1.20 × (Year 1 product 1 investment). Can invest in products (1) and (3).
- **End of Year 2 / Beginning of Year 3:** Cash = uninvested Year 2 cash + 1.20 × (Year 2 product 1 investment) + 1.50 × (product 2 investment) + 1.60 × (product 3 investment). Can invest in products (1) and (4).
- **End of Year 3:** Objective = uninvested Year 3 cash + 1.20 × (Year 3 product 1 investment) + 1.40 × (product 4 investment).