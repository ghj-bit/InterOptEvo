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

QUESTION: At the end of Year 3, is any money that has not been invested (i.e., cash left over after all investments are made) counted toward the objective, or must all funds be fully invested in the available products?

## Turn 1 - User Simulator

Yes, any cash left over at the end of Year 3 is counted toward the objective. The goal is to maximize your total wealth at the end of Year 3, which includes both the proceeds from matured investments and any uninvested cash. You are not required to fully invest all funds in the available products.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20·I payout at year-end automatically reinvested, or does it become available cash that can be allocated to other products in the following year (or held as cash)?

## Turn 2 - User Simulator

The 1.20·I payout becomes available cash at the end of the year. It is not automatically reinvested. You can choose to allocate it to other products in the following year or hold it as cash.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much cash can be held uninvested from one year to the next, or is holding cash free with no penalty or cap?

## Turn 3 - User Simulator

Holding cash is free with no penalty or cap. There is no limit on how much cash can be held uninvested from one year to the next.

## Turn 4 - Generic Agent

QUESTION: For product (2), the 2-year product available only at the beginning of Year 1 — is the 1.50·I payout received at the end of Year 2 available as cash that can be invested in Year 3 products, or is it only counted in the final objective at the end of Year 3?

## Turn 4 - User Simulator

The 1.50·I payout is received as cash at the end of Year 2. It is available to be invested in Year 3 products or held as cash. It is not only counted in the final objective at the end of Year 3.

## Turn 5 - Generic Agent

QUESTION: Are there any minimum investment amounts for any of the products, or can you invest any amount (including zero) in each product?

## Turn 5 - User Simulator

There are no minimum investment amounts. You can invest any amount, including zero, in each product.

## Turn 6 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year — is the investment amount in each year independent (i.e., you can invest different amounts in Year 1, Year 2, and Year 3), or is there a single total investment across all three years?

## Turn 6 - User Simulator

The investment amount in each year is independent. You can invest different amounts in Year 1, Year 2, and Year 3.

## Turn 7 - Generic Agent

QUESTION: Is there any constraint that the total investment in a given year cannot exceed the cash available at the beginning of that year (i.e., a budget constraint per year), or can you invest more than what you have available?

## Turn 7 - User Simulator

Yes, there is a constraint that the total investment in a given year cannot exceed the cash available at the beginning of that year. You cannot invest more than what you have available.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 2, the cash available includes the 1.20·I payout from product (1) invested in Year 1 plus any uninvested cash carried over from Year 1 — is that correct, or is there any other source of cash at the beginning of Year 2?

## Turn 8 - User Simulator

Yes, that is correct. At the beginning of Year 2, the cash available includes the 1.20·I payout from product (1) invested in Year 1 plus any uninvested cash carried over from Year 1. There are no other sources of cash at the beginning of Year 2.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 3, the cash available includes the 1.20·I payout from product (1) invested in Year 2, the 1.50·I payout from product (2), the 1.60·I payout from product (3), plus any uninvested cash carried over from Year 2 — is that correct, or is there any other source of cash at the beginning of Year 3?

## Turn 9 - User Simulator

Yes, that is correct. At the beginning of Year 3, the cash available includes the 1.20·I payout from product (1) invested in Year 2, the 1.50·I payout from product (2), the 1.60·I payout from product (3), plus any uninvested cash carried over from Year 2. There are no other sources of cash at the beginning of Year 3.

## Turn 10 - Generic Agent

QUESTION: At the end of Year 3, the final wealth includes the 1.20·I payout from product (1) invested in Year 3, the 1.40·I payout from product (4), plus any uninvested cash carried over from Year 3 — is that correct, or is there any other component of final wealth?

## Turn 10 - User Simulator

Yes, that is correct. At the end of Year 3, the final wealth includes the 1.20·I payout from product (1) invested in Year 3, the 1.40·I payout from product (4), plus any uninvested cash carried over from Year 3. There are no other components of final wealth.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total wealth at the end of Year 3, which equals the sum of all matured investment payouts and any uninvested cash at that time.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Decision variables (all continuous, non-negative, no minimums):**
- x1₁, x1₂, x1₃: amounts invested in product (1) at the beginning of Years 1, 2, and 3 respectively (unlimited capacity).
- x2: amount invested in product (2) at the beginning of Year 1 (cap: 120,000).
- x3: amount invested in product (3) at the beginning of Year 2 (cap: 150,000).
- x4: amount invested in product (4) at the beginning of Year 3 (cap: 100,000).
- c1, c2, c3: uninvested cash carried over at the end of Years 1, 2, and 3 respectively (no cap, no penalty).

**Cash flow / budget constraints:**
- Beginning of Year 1: x1₁ + x2 + c1 ≤ 500,000
- Beginning of Year 2: x1₂ + x3 + c2 ≤ 1.20·x1₁ + c1
- Beginning of Year 3: x1₃ + x4 + c3 ≤ 1.20·x1₂ + 1.50·x2 + 1.60·x3 + c2

**Capacity constraints:**
- x2 ≤ 120,000
- x3 ≤ 150,000
- x4 ≤ 100,000

**Objective function:**
Maximize 1.20·x1₃ + 1.40·x4 + c3

**Key confirmed facts:**
- Payouts become available cash at maturity and can be reinvested or held.
- Holding cash is free (no penalty, no cap).
- Per-year budget constraint: cannot invest more than cash available.
- Product (1) investments in each year are independent.
- No minimum investment amounts.
- All variables are continuous and non-negative.