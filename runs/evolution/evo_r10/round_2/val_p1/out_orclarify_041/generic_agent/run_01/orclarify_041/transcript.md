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