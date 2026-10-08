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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash held idle) counted toward the objective, or must all funds be invested in products that mature by the end of Year 3?

## Turn 1 - User Simulator

Cash held idle at the end of Year 3 is counted toward the objective. The goal is to maximize total wealth (principal plus interest) at the end of Year 3, which includes any uninvested cash remaining at that time.

## Turn 2 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year, can the proceeds from a product that matures at the end of a year be reinvested in product (1) at the beginning of the next year (i.e., is there no friction or delay between maturity and reinvestment)?

## Turn 2 - User Simulator

Yes, proceeds from a product that matures at the end of a year can be reinvested in product (1) at the beginning of the next year. There is no friction or delay; the cash is available for investment at the start of the following year.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum investment amount or granularity requirement for any of the products, or can any non-negative amount be invested in each product?

## Turn 3 - User Simulator

There is no minimum investment amount or granularity requirement. Any non-negative amount can be invested in each product, subject to the stated maximum caps for products (2), (3), and (4).

## Turn 4 - Generic Agent

QUESTION: Is there any constraint that requires a minimum amount of cash to be kept liquid (uninvested) at the beginning of any year, or can 100% of available cash be invested each year?

## Turn 4 - User Simulator

There is no constraint requiring a minimum amount of cash to be kept liquid. 100% of available cash can be invested at the beginning of any year, subject to the product availability and capacity limits.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited in each year it is available?

## Turn 5 - User Simulator

Product (1) is truly unlimited in each year it is available. There is no cap on the total amount that can be invested in product (1) across all three years.

## Turn 6 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total wealth (principal + interest + any idle cash) at the end of Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Products and their parameters:**

| Product | Type | Available | Matures | Return | Cap |
|---------|------|-----------|---------|--------|-----|
| (1) | 1-year | Beginning of Years 1, 2, 3 | End of same year | 1.20 × I | Unlimited |
| (2) | 2-year | Beginning of Year 1 only | End of Year 2 | 1.50 × I | 120,000 |
| (3) | Same-year | Beginning of Year 2 only | End of Year 2 | 1.60 × I | 150,000 |
| (4) | 1-year | Beginning of Year 3 only | End of Year 3 | 1.40 × I | 100,000 |

**Key rules confirmed:**
- Proceeds from maturing products are immediately available for reinvestment at the beginning of the next year (no friction or delay).
- Any non-negative amount can be invested (no minimums or granularity).
- 100% of available cash may be invested each year (no liquidity reserve requirement).
- Product (1) has no capacity limit in any year.
- Idle cash at the end of Year 3 counts toward the objective.
- The only constraints are the per-product caps on (2), (3), and (4), and the cash-flow balance at each year boundary.

**Decision variables (continuous, non-negative):**
- x₁, x₂, x₃: amounts invested in product (1) at the beginning of Years 1, 2, 3 respectively.
- x₄: amount invested in product (2) at the beginning of Year 1.
- x₅: amount invested in product (3) at the beginning of Year 2.
- x₆: amount invested in product (4) at the beginning of Year 3.

**Cash-flow constraints:**
- Beginning of Year 1: x₁ + x₄ ≤ 500,000
- Beginning of Year 2: x₂ + x₅ ≤ 1.20·x₁ + 1.50·x₄ (proceeds from Year 1 product (1) and product (2))
- Beginning of Year 3: x₃ + x₆ ≤ 1.20·x₂ + 1.60·x₅ (proceeds from Year 2 product (1) and product (3))

**Capacity constraints:**
- x₄ ≤ 120,000
- x₅ ≤ 150,000
- x₆ ≤ 100,000

**Objective (end of Year 3 wealth):**
Maximize 1.20·x₃ + 1.40·x₆ + (any idle cash at end of Year 3)

where idle cash at end of Year 3 = (1.20·x₂ + 1.60·x₅) − x₃ − x₆ (if positive).

This is a linear program with 6 continuous non-negative variables.