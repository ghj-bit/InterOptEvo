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

QUESTION: At the end of Year 3, is any money that was not invested in a product (i.e., left as idle cash) still available and counted toward the total principal plus interest you want to maximize?

## Turn 1 - User Simulator

Yes. Any cash that is not invested at the end of Year 3 remains available and is counted toward the total principal plus interest you want to maximize.

## Turn 2 - Generic Agent

QUESTION: If you invest in product (1) at the beginning of Year 3, it matures at the end of Year 3 and pays 1.20·I — is that 1.20·I received at the end of Year 3 and therefore counted in the final total, or does product (1) in Year 3 actually mature at the end of Year 4 and thus not count toward the Year 3 total?

## Turn 2 - User Simulator

The 1.20·I is received at the end of Year 3 and is counted in the final total.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in any given year, or is it truly unlimited as stated?

## Turn 3 - User Simulator

Product (1) is truly unlimited; there is no cap on how much you can invest in it in any given year.

## Turn 4 - Generic Agent

QUESTION: Can you invest in product (1) in Year 2 and Year 3 as well, or is product (1) only available at the beginning of Year 1?

## Turn 4 - User Simulator

Product (1) is available at the beginning of each year, including Year 2 and Year 3.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any non-negative amount (including zero) in each product?

## Turn 5 - User Simulator

There is no minimum investment amount. You can invest any non-negative amount, including zero, in each product.

## Turn 6 - Generic Agent

QUESTION: Is this a linear programming problem where you can split your investment across multiple products in the same year (e.g., invest some in product 1 and some in product 3 at the beginning of Year 2), or must you choose only one product per year?

## Turn 6 - User Simulator

You can split your investment across multiple products in the same year. For example, at the beginning of Year 2, you can invest some amount in product (1) and some amount in product (3), as long as the total does not exceed the cash available at that time.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 2, the cash available to invest equals the proceeds from product (1) invested in Year 1 plus any uninvested cash from Year 1 — is that correct, or are there other sources of cash at the beginning of Year 2?

## Turn 7 - User Simulator

That is correct. At the beginning of Year 2, the cash available to invest equals the proceeds from product (1) invested in Year 1 plus any uninvested cash from Year 1.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 3, the cash available to invest equals the proceeds from product (1) invested in Year 2 plus the proceeds from product (2) (which matures at the end of Year 2) plus the proceeds from product (3) (which matures at the end of Year 2) plus any uninvested cash from Year 2 — is that correct?

## Turn 8 - User Simulator

Yes, that is correct.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you choose to leave some cash uninvested and carry it forward to the next year?

## Turn 9 - User Simulator

You can choose to leave some cash uninvested and carry it forward to the next year. There is no requirement to invest all available cash at the beginning of each year.

## Turn 10 - Generic Agent

QUESTION: Is this a linear programming problem (continuous variables), or do you expect the investment amounts to be integer values (e.g., whole yuan)?

## Turn 10 - User Simulator

This is a linear programming problem with continuous variables. The investment amounts do not need to be integer values.

## Turn 11 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash (principal + interest) at the end of Year 3.

**Decision variables (all continuous, non-negative):**
- x1_1, x1_2, x1_3: amount invested in product (1) at the beginning of Years 1, 2, 3 respectively (unlimited).
- x2_1: amount invested in product (2) at the beginning of Year 1 (cap: 120,000).
- x3_2: amount invested in product (3) at the beginning of Year 2 (cap: 150,000).
- x4_3: amount invested in product (4) at the beginning of Year 3 (cap: 100,000).
- c1, c2, c3: uninvested cash carried forward at the end of Years 1, 2, 3 respectively.

**Cash flow constraints:**
- Beginning of Year 1: x1_1 + x2_1 + c1 = 500,000
- Beginning of Year 2: x1_2 + x3_2 + c2 = 1.20·x1_1 + c1
- Beginning of Year 3: x1_3 + x4_3 + c3 = 1.20·x1_2 + 1.50·x2_1 + 1.60·x3_2 + c2

**Objective function:**
Maximize: 1.20·x1_3 + 1.40·x4_3 + c3

**Upper bounds:**
- x2_1 ≤ 120,000
- x3_2 ≤ 150,000
- x4_3 ≤ 100,000

**All variables ≥ 0.**

This is a linear programming problem.