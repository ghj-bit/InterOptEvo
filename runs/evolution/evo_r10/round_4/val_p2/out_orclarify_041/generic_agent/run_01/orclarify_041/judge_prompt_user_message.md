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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (principal plus interest from all matured investments), and are there any investments that do not mature by the end of Year 3 that should be excluded from this total?

## Turn 2 - User Simulator

Yes, the objective is to maximize the total cash on hand at the end of Year 3. All available investments mature by the end of Year 3, so none are excluded.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited as stated?

## Turn 3 - User Simulator

Product (1) is truly unlimited. There is no cap on the total amount invested in it across the three years.

## Turn 4 - Generic Agent

QUESTION: Can you invest in product (1) at the beginning of Year 3, and if so, does it mature at the end of Year 3 (i.e., is it available in all three years as stated)?

## Turn 4 - User Simulator

Yes, product (1) is available at the beginning of Year 3 and matures at the end of Year 3. It is available in all three years as stated.

## Turn 5 - Generic Agent

QUESTION: Are there any transaction costs, fees, or taxes associated with investing in any of the products, or are the stated returns (1.20, 1.50, 1.60, 1.40) the net returns after all costs?

## Turn 5 - User Simulator

The stated returns are the net returns after all costs. There are no additional transaction costs, fees, or taxes.

## Turn 6 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you hold cash (uninvested) from one year to the next?

## Turn 6 - User Simulator

You can hold cash uninvested from one year to the next. There is no requirement to invest all available cash at the beginning of each year.

## Turn 7 - Generic Agent

QUESTION: If you hold cash uninvested from one year to the next, does that cash earn any interest or return, or does it remain at face value (i.e., 1 yuan held becomes 1 yuan the next year)?

## Turn 7 - User Simulator

Cash held uninvested remains at face value. It does not earn any interest or return.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint that limits the total amount you can invest across all products in a given year, or is the only limit the individual product caps?

## Turn 8 - User Simulator

The only limits are the individual product caps. There is no separate constraint limiting the total amount invested across all products in a given year, other than the cash available at that time.

## Turn 9 - Generic Agent

QUESTION: Is there any requirement that the initial 500,000 yuan must be fully invested at the beginning of Year 1, or can some of it be held as cash and invested in later years?

## Turn 9 - User Simulator

There is no requirement to fully invest the initial 500,000 yuan at the beginning of Year 1. You can hold some of it as cash and invest it in later years.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or requirements I should be aware of, such as a minimum amount that must remain as cash at the end of Year 3, or any other business rules that would affect the investment plan?

## Turn 10 - User Simulator

No, there are no other constraints or requirements. There is no minimum cash requirement at the end of Year 3, and no other business rules affect the plan.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the investment planning problem:

**Objective:** Maximize total cash on hand at the end of Year 3 (principal plus interest from all matured investments).

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Investment Products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at the end of the same year. Unlimited capacity. No minimum investment.

2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, paying 1.50×I. Capped at 120,000 yuan. No minimum investment.

3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, paying 1.60×I. Capped at 150,000 yuan. No minimum investment.

4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, paying 1.40×I. Capped at 100,000 yuan. No minimum investment.

**Key Rules:**
- Cash can be held uninvested from one year to the next at face value (no interest).
- There is no requirement to invest all available cash in any given year.
- The only investment limits are the individual product caps (120,000 for product 2; 150,000 for product 3; 100,000 for product 4).
- There are no transaction costs, fees, or taxes; stated returns are net.
- There is no minimum cash requirement at the end of Year 3.
- All investments mature by the end of Year 3.
- No other constraints or business rules apply.