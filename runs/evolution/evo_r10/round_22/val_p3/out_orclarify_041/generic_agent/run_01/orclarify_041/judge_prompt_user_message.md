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

QUESTION: At the end of Year 3, do you want the objective to count only the cash that has actually matured by then (i.e., money in 1-year products (1) and (4) plus any leftover cash), or should it also include the value of any money still locked in longer-term investments that have not yet matured?

## Turn 1 - User Simulator

The objective should count only the cash that has actually matured by the end of Year 3. This includes proceeds from 1-year products (1) and (4), as well as any leftover cash. It should not include the value of any money still locked in longer-term investments that have not yet matured.

## Turn 2 - Generic Agent

QUESTION: Product (2) is a 2-year product that matures at the end of Year 2, so its proceeds are available at the start of Year 3 — is that correct, meaning the 1.50·I proceeds can be reinvested in Year 3 products (such as product (4) or product (1))?

## Turn 2 - User Simulator

Yes, that is correct. The proceeds from product (2) are available at the start of Year 3 and can be reinvested in Year 3 products, such as product (4) or product (1).

## Turn 3 - Generic Agent

QUESTION: If you hold cash at the end of a year without investing it, does that cash earn any interest (for example, a bank deposit rate), or does it simply carry over to the next year at face value with no return?

## Turn 3 - User Simulator

Cash that is not invested simply carries over to the next year at face value with no return.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum investment amount or divisibility requirement for the products, or can you invest any non-negative amount (including fractional yuan) in each product?

## Turn 4 - User Simulator

There is no minimum investment amount or divisibility requirement. You can invest any non-negative amount, including fractional yuan, in each product.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1), the 1-year product available at the beginning of each year, or is it truly unlimited as stated?

## Turn 5 - User Simulator

Product (1) is truly unlimited. There is no cap on the amount you can invest in it.

## Turn 6 - Generic Agent

QUESTION: Are there any other constraints I should know about, such as a requirement to invest all available cash each year, a maximum total portfolio value, or any other business rules not mentioned in the brief?

## Turn 6 - User Simulator

No, there are no other constraints. You are not required to invest all available cash each year, and there is no maximum total portfolio value limit. The only rules are the individual caps on products (2), (3), and (4), and the no-borrowing rule.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash available at the end of Year 3, counting only matured proceeds (from 1-year products (1) and (4)) plus any leftover uninvested cash. Money still locked in longer-term investments that have not matured by end of Year 3 is excluded.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Products:**
- **(1)** 1-year product, available at the beginning of Years 1, 2, and 3. Invest I at start of year → receive 1.20·I at end of that year. Unlimited capacity.
- **(2)** 2-year product, available only at the beginning of Year 1. Matures at end of Year 2, pays 1.50·I. Cap: 120,000 yuan. Proceeds available at start of Year 3 for reinvestment.
- **(3)** Same-year product, available only at the beginning of Year 2. Matures at end of Year 2, pays 1.60·I. Cap: 150,000 yuan.
- **(4)** 1-year product, available only at the beginning of Year 3. Matures at end of Year 3, pays 1.40·I. Cap: 100,000 yuan.

**Cash flow / reinvestment:**
- Uninvested cash carries over to the next year at face value (no interest).
- Proceeds from maturing products are available for reinvestment in subsequent years.
- No borrowing allowed.

**Constraints:**
- Caps: Product (2) ≤ 120,000; Product (3) ≤ 150,000; Product (4) ≤ 100,000.
- No minimum investment, no divisibility requirement (continuous, non-negative variables).
- No requirement to invest all cash each year.
- No other constraints.