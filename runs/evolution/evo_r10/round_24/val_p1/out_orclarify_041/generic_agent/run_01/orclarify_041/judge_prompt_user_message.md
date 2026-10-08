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

QUESTION: At the end of Year 3, is the money you want to maximize the total value of all investments that have matured by then (i.e., the sum of the Year-3-maturing returns from products 1 and 4, plus any product-2 proceeds that were reinvested in Year 3), or should any cash that is simply left uninvested at the end of Year 3 also count toward the total?

## Turn 1 - User Simulator

Yes, any cash that is simply left uninvested at the end of Year 3 also counts toward the total. The objective is to maximize your total wealth at the end of Year 3, which includes all matured investment proceeds plus any remaining uninvested cash.

## Turn 2 - Generic Agent

QUESTION: If you invest in product (2) at the beginning of Year 1, the 1.50·I proceeds arrive at the end of Year 2 — can that money be reinvested in product (1) at the beginning of Year 3 (earning 1.20× by end of Year 3), or does it just sit as cash until the end of Year 3?

## Turn 2 - User Simulator

That money can be reinvested in product (1) at the beginning of Year 3.

## Turn 3 - Generic Agent

QUESTION: Product (1) is described as available at the beginning of each year (Years 1–3) — so if you invest in product (1) at the beginning of Year 2, you receive 1.20·I at the end of Year 2, and that money can then be reinvested in product (1) again at the beginning of Year 3, is that correct?

## Turn 3 - User Simulator

Yes, that is correct.

## Turn 4 - Generic Agent

QUESTION: At the beginning of Year 2, you can invest in product (1) (1-year, 1.20×) and product (3) (same-year, 1.60×, capped at 150,000) — is the only constraint on Year-2 investing that the total invested in products (1) and (3) together cannot exceed the cash available at the beginning of Year 2 (i.e., the 1.20× proceeds from Year-1 product-1 investments plus any uninvested Year-1 cash), with no other limit on how much goes into product (1)?

## Turn 4 - User Simulator

Yes, that is correct. The only constraint on Year-2 investing is that the total invested in products (1) and (3) together cannot exceed the cash available at the beginning of Year 2. There is no other limit on how much goes into product (1).

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 3, you can invest in product (1) (1-year, 1.20×, unlimited) and product (4) (1-year, 1.40×, capped at 100,000) — is the only constraint that the total invested in products (1) and (4) together cannot exceed the cash available at the beginning of Year 3 (i.e., the 1.20× proceeds from Year-2 product-1 investments, the 1.60× proceeds from product 3, the 1.50× proceeds from product 2, plus any uninvested earlier cash), with no other limit on how much goes into product (1)?

## Turn 5 - User Simulator

Yes, that is correct.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum investment amount or requirement to invest all available cash at the beginning of each year, or can you choose to leave any amount of cash uninvested in any year?

## Turn 6 - User Simulator

You can choose to leave any amount of cash uninvested in any year. There is no minimum investment amount or requirement to invest all available cash.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in any given year, or is it truly unlimited as stated?

## Turn 7 - User Simulator

It is truly unlimited as stated.

## Turn 8 - Generic Agent

QUESTION: Are there any other constraints or considerations I should know about — for example, transaction fees, taxes, or any requirement that a certain amount of cash must be kept liquid at any point during the three years?

## Turn 8 - User Simulator

No, there are no transaction fees, taxes, or liquidity requirements. The only constraints are the investment caps for products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total wealth at the end of Year 3, which includes all matured investment proceeds plus any uninvested cash.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

1. **Product (1):** 1-year, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at year-end. Unlimited capacity.
2. **Product (2):** 2-year, available only at the beginning of Year 1. Matures at end of Year 2, pays 1.50×I. Capped at 120,000 yuan.
3. **Product (3):** Same-year (1-year), available only at the beginning of Year 2. Matures at end of Year 2, pays 1.60×I. Capped at 150,000 yuan.
4. **Product (4):** 1-year, available only at the beginning of Year 3. Matures at end of Year 3, pays 1.40×I. Capped at 100,000 yuan.

**Cash flow / reinvestment rules:**
- Proceeds from any product maturing at the end of a year are available for reinvestment at the beginning of the next year.
- Product (2) proceeds (end of Year 2) can be reinvested in product (1) at the beginning of Year 3.
- Product (1) Year-1 proceeds (end of Year 1) can be reinvested in products (1) or (3) at the beginning of Year 2.
- Product (1) Year-2 and product (3) proceeds (end of Year 2) can be reinvested in products (1) or (4) at the beginning of Year 3.

**Constraints:**
- Cannot invest more than available cash at the beginning of each year (no borrowing).
- Product (2) ≤ 120,000; Product (3) ≤ 150,000; Product (4) ≤ 100,000.
- Product (1) is unlimited.
- No minimum investment; any amount of cash may be left uninvested in any year.
- No transaction fees, taxes, or liquidity requirements.

**Decision variables (per year where applicable):**
- Amount invested in each product at each point in time it is available.
- Amount of cash left uninvested at each year's beginning.

This is a linear programming problem with a small number of decision variables and linear constraints.