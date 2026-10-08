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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., the sum of all matured proceeds from products 1, 3, and 4, plus any uninvested cash carried over), or should the plan be required to invest all available funds each year so that no cash is left idle?

## Turn 1 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes the sum of all matured proceeds from products 1, 3, and 4, plus any uninvested cash carried over. There is no requirement to invest all available funds each year; cash may be left idle if that leads to a higher total at the end of Year 3.

## Turn 2 - Generic Agent

QUESTION: If cash is left uninvested (idle) in a given year, does it earn any interest or return, or does it simply carry over at face value (1.00) to the next year?

## Turn 2 - User Simulator

Idle cash simply carries over at face value (1.00) to the next year. It does not earn any interest or return.

## Turn 3 - Generic Agent

QUESTION: Product (2) is a 2-year product available only at the beginning of Year 1 and maturing at the end of Year 2. When it matures at the end of Year 2, can the proceeds (1.50·I) be reinvested in product (1) at the beginning of Year 3, or do they simply add to the cash on hand at the end of Year 3?

## Turn 3 - User Simulator

The proceeds from product (2) mature at the end of Year 2. They can be reinvested in product (1) at the beginning of Year 3, or they can be left as idle cash. If reinvested in product (1) at the beginning of Year 3, they will mature at the end of Year 3 and contribute to the final cash on hand. If not reinvested, they simply carry over at face value to the end of Year 3.

## Turn 4 - Generic Agent

QUESTION: Product (3) is available at the beginning of Year 2 and matures at the end of Year 2. When it matures at the end of Year 2, can its proceeds (1.60·I) be reinvested in product (1) at the beginning of Year 3, or do they simply carry over at face value to the end of Year 3?

## Turn 4 - User Simulator

The proceeds from product (3) mature at the end of Year 2. They can be reinvested in product (1) at the beginning of Year 3, or they can be left as idle cash. If reinvested in product (1) at the beginning of Year 3, they will mature at the end of Year 3 and contribute to the final cash on hand. If not reinvested, they simply carry over at face value to the end of Year 3.

## Turn 5 - Generic Agent

QUESTION: Product (1) is available at the beginning of each year (Years 1–3) and matures at that year's end. If you invest in product (1) at the beginning of Year 1, the proceeds (1.20·I) mature at the end of Year 1. Can those proceeds be reinvested in product (1) again at the beginning of Year 2, or in product (3) at the beginning of Year 2, or do they simply carry over as idle cash?

## Turn 5 - User Simulator

The proceeds from product (1) invested at the beginning of Year 1 mature at the end of Year 1. At the beginning of Year 2, they can be reinvested in product (1), reinvested in product (3), or left as idle cash.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 2, the available cash includes the initial capital that was not invested in Year 1, plus the proceeds from product (1) invested at the beginning of Year 1. Is there any restriction on which specific source of cash can be used to fund investments in Year 2, or can all available cash at the beginning of Year 2 be freely allocated among product (1), product (3), and idle cash?

## Turn 6 - User Simulator

There is no restriction on which specific source of cash can be used. All available cash at the beginning of Year 2 can be freely allocated among product (1), product (3), and idle cash.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 3, the available cash includes the proceeds from product (1) invested at the beginning of Year 2, the proceeds from product (2) (if any), the proceeds from product (3) (if any), and any idle cash carried over from Year 2. Can all of this available cash be freely allocated among product (1), product (4), and idle cash at the beginning of Year 3, with no restrictions on which source funds which investment?

## Turn 7 - User Simulator

Yes. All available cash at the beginning of Year 3 can be freely allocated among product (1), product (4), and idle cash, with no restrictions on which source funds which investment.

## Turn 8 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any non-negative amount (including zero) in each product?

## Turn 8 - User Simulator

There is no minimum investment amount required. You can invest any non-negative amount, including zero, in each product.

## Turn 9 - Generic Agent

QUESTION: Are the investment amounts required to be in whole yuan (integer values), or can they be any non-negative real number?

## Turn 9 - User Simulator

The investment amounts can be any non-negative real number. They do not need to be in whole yuan.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited as stated?

## Turn 10 - User Simulator

Product (1) is truly unlimited. There is no limit on the total amount that can be invested in product (1) across all three years.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint that the total investment in a given year cannot exceed the available cash at the beginning of that year, or is it possible to borrow or use external funds to invest more than what is available?

## Turn 11 - User Simulator

There is a constraint that the total investment in a given year cannot exceed the available cash at the beginning of that year. No borrowing or use of external funds is allowed.

## Turn 12 - Generic Agent

QUESTION: At the end of Year 3, the final cash on hand includes proceeds from product (1) invested at the beginning of Year 3, proceeds from product (4) (if any), and any idle cash carried over from Year 3. Is there any other source of cash that could contribute to the final amount at the end of Year 3?

## Turn 12 - User Simulator

No. The final cash on hand at the end of Year 3 consists only of:
- Proceeds from product (1) invested at the beginning of Year 3,
- Proceeds from product (4) (if any),
- Any idle cash carried over from Year 3.

No other source of cash contributes to the final amount at the end of Year 3.

## Turn 13 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Maximize total cash on hand at the end of Year 3.
- **Initial capital:** 500,000 yuan at the beginning of Year 1.
- **Products:**
  - **(1)** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20·I at year-end. Unlimited capacity.
  - **(2)** 2-year product, available only at the beginning of Year 1. Returns 1.50·I at the end of Year 2. Capped at 120,000 yuan.
  - **(3)** Same-year product, available only at the beginning of Year 2. Returns 1.60·I at the end of Year 2. Capped at 150,000 yuan.
  - **(4)** 1-year product, available only at the beginning of Year 3. Returns 1.40·I at the end of Year 3. Capped at 100,000 yuan.
- **Cash flow rules:**
  - Idle cash carries over at face value (1.00) to the next year.
  - Proceeds from any product that matures at the end of a year can be freely allocated at the beginning of the next year among available products and idle cash.
  - No borrowing or external funds allowed; total investment in a year cannot exceed available cash at the beginning of that year.
  - No minimum investment; any non-negative real amount is allowed.
  - No restriction on which source of cash funds which investment.
- **Final cash at end of Year 3** = proceeds from product (1) invested in Year 3 + proceeds from product (4) + idle cash carried over from Year 3.