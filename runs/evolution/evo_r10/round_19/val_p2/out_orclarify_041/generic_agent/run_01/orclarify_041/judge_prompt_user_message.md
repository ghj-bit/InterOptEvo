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

QUESTION: At the end of Year 3, should the objective value include only the proceeds from investments that mature at the end of Year 3, or should it also include the value of any capital that was never invested (left idle) plus any proceeds from product (1) that mature at the end of Year 3?

## Turn 1 - User Simulator

The objective value should include all cash available at the end of Year 3. This means it includes:

1.  Proceeds from investments that mature at the end of Year 3 (such as product (1) invested in Year 3 and product (4)).
2.  Any capital that was never invested and was left idle.

It does not include the value of investments that have not yet matured, but since the planning horizon ends at the end of Year 3, all relevant cash flows are realized by that point.

## Turn 2 - Generic Agent

QUESTION: When you say "all cash available at the end of Year 3," does this mean that any capital not invested in a given year simply carries over to the next year as available cash (i.e., it can be invested in later years), or is uninvested capital permanently lost at the end of each year?

## Turn 2 - User Simulator

Uninvested capital carries over to the next year as available cash. It is not lost. At the beginning of each year, you can invest any cash you have, which includes your initial capital, proceeds from matured investments, and any capital left uninvested from previous years.

## Turn 3 - Generic Agent

QUESTION: For product (1), which is available at the beginning of each year and matures at that year's end, can you invest in it in Year 1, Year 2, and Year 3 independently (i.e., separate investment decisions each year), or is there a single total amount invested in product (1) across all three years?

## Turn 3 - User Simulator

You can invest in product (1) independently in Year 1, Year 2, and Year 3. These are separate investment decisions made at the beginning of each year.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can you invest any amount from zero up to the stated cap?

## Turn 4 - User Simulator

There are no minimum investment amounts. You can invest any amount from zero up to the stated cap for each product.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts required to be whole numbers (integer yuan), or can they be any non-negative real number?

## Turn 5 - User Simulator

The investment amounts can be any non-negative real number. They do not need to be whole numbers.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited as stated?

## Turn 6 - User Simulator

Product (1) is truly unlimited. There is no cap on the total amount that can be invested in product (1) across all three years, other than the constraint that you cannot invest more cash than you have available at the beginning of each year.

## Turn 7 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or is it optional to leave some cash uninvested and carry it forward?

## Turn 7 - User Simulator

It is optional to leave some cash uninvested. You are not required to invest all available cash at the beginning of each year; any uninvested cash carries forward to the next year.

## Turn 8 - Generic Agent

QUESTION: Since product (1) is available in all three years with a 20% return, product (3) is only available in Year 2 with a 60% return, and product (4) is only available in Year 3 with a 40% return, is there any additional constraint or business rule I should be aware of that would prevent you from simply investing as much as possible in the highest-return products available each year?

## Turn 8 - User Simulator

No, there are no additional constraints or business rules preventing you from investing as much as possible in the highest-return products available each year, subject to the stated caps and the rule that you cannot borrow. The only limitations are the specific caps for products (2), (3), and (4), and the requirement to use only currently available cash.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash available at the end of Year 3 (proceeds from investments maturing at end of Year 3 plus any uninvested cash carried forward).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Decision variables (all non-negative reals):**
- x1_1, x1_2, x1_3: amounts invested in product (1) at the beginning of Years 1, 2, and 3 respectively (unlimited).
- x2: amount invested in product (2) at the beginning of Year 1 (cap: 120,000).
- x3: amount invested in product (3) at the beginning of Year 2 (cap: 150,000).
- x4: amount invested in product (4) at the beginning of Year 3 (cap: 100,000).
- c1, c2, c3: uninvested cash carried forward from the beginning of Years 1, 2, and 3 respectively.

**Cash flow / balance constraints:**
- Beginning of Year 1: x1_1 + x2 + c1 = 500,000
- Beginning of Year 2: x1_2 + x3 + c2 = 1.20·x1_1 + 1.50·x2 + c1
- Beginning of Year 3: x1_3 + x4 + c3 = 1.20·x1_2 + 1.60·x3 + c2

**Objective function:**
Maximize 1.20·x1_3 + 1.40·x4 + c3

**Caps:**
- x2 ≤ 120,000
- x3 ≤ 150,000
- x4 ≤ 100,000

**Other confirmed facts:**
- No minimum investment amounts.
- No borrowing allowed.
- Uninvested cash carries forward (not lost).
- Product (1) is a separate decision each year, unlimited in capacity.
- All variables are continuous (non-negative reals).
- No other hidden constraints or business rules.