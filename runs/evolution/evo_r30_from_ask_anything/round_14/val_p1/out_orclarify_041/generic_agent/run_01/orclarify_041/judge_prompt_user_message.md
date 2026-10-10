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

QUESTION: For the 1-year product (1), is the 1.20 return factor applied to the full amount invested at the start of each year, with no additional fees or taxes reducing the amount available for reinvestment at the end of that year?

## Turn 1 - User Simulator

Yes. The 1.20 return factor is applied to the full amount invested at the start of the year, and the entire amount received at the end of the year is available for reinvestment. There are no additional fees or taxes reducing that amount.

## Turn 2 - Generic Agent

QUESTION: For the 2-year product (2), is the 1.50 return factor applied to the full amount invested at the start of Year 1, with the entire amount received at the end of Year 2 available for reinvestment in Year 3, and no fees or taxes reducing that amount?

## Turn 2 - User Simulator

Yes. The 1.50 return factor is applied to the full amount invested at the start of Year 1, and the entire amount received at the end of Year 2 is available for reinvestment in Year 3. There are no fees or taxes reducing that amount.

## Turn 3 - Generic Agent

QUESTION: For the same-year product (3), is the 1.60 return factor applied to the full amount invested at the start of Year 2, with the entire amount received at the end of Year 2 available for reinvestment in Year 3, and no fees or taxes reducing that amount?

## Turn 3 - User Simulator

Yes. The 1.60 return factor is applied to the full amount invested at the start of Year 2, and the entire amount received at the end of Year 2 is available for reinvestment in Year 3. There are no fees or taxes reducing that amount.

## Turn 4 - Generic Agent

QUESTION: For the 1-year product (4), is the 1.40 return factor applied to the full amount invested at the start of Year 3, with the entire amount received at the end of Year 3 counted toward the final objective, and no fees or taxes reducing that amount?

## Turn 4 - User Simulator

Yes. The 1.40 return factor is applied to the full amount invested at the start of Year 3, and the entire amount received at the end of Year 3 counts toward the final objective. There are no fees or taxes reducing that amount.

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 1, is the entire 500,000 yuan initial capital required to be allocated among the available products (1) and (2), or is it permissible to leave some of the 500,000 yuan uninvested as cash that carries over to later years without earning any return?

## Turn 5 - User Simulator

It is permissible to leave some of the 500,000 yuan uninvested as cash that carries over to later years without earning any return.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 2, is the entire amount available (from Year 1 product (1) returns plus any uninvested cash) required to be allocated among the available products (1) and (3), or is it permissible to leave some of that amount uninvested as cash that carries over to Year 3 without earning any return?

## Turn 6 - User Simulator

It is permissible to leave some of the amount available at the beginning of Year 2 uninvested as cash that carries over to Year 3 without earning any return.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 3, is the entire amount available (from Year 2 product (1) and (3) returns, product (2) maturity, plus any uninvested cash) required to be allocated among the available products (1) and (4), or is it permissible to leave some of that amount uninvested as cash that simply counts toward the final Year 3 total without earning any return?

## Turn 7 - User Simulator

It is permissible to leave some of the amount available at the beginning of Year 3 uninvested as cash that simply counts toward the final Year 3 total without earning any return.

## Turn 8 - Generic Agent

QUESTION: Are the investment amounts in each product required to be whole numbers (integer yuan), or can they be any non-negative real number (continuous amounts)?

## Turn 8 - User Simulator

The investment amounts can be any non-negative real number (continuous amounts).

## Turn 9 - Generic Agent

QUESTION: Are there any additional constraints or requirements beyond the product caps and the initial capital that I should include in the model, such as a minimum investment in any product, a requirement to invest a certain percentage of available funds each year, or any linkage between the products?

## Turn 9 - User Simulator

No. There are no additional constraints or requirements beyond the product caps, the initial capital, and the no-borrowing rule. There is no minimum investment in any product, no requirement to invest a certain percentage of available funds each year, and no linkage between the products.

## Turn 10 - Generic Agent

QUESTION: Is the "no-borrowing rule" you mentioned a formal constraint that the total amount invested at the start of each year cannot exceed the total funds available at that time (i.e., you cannot invest more than you have on hand), or is it simply a descriptive statement that you start with 500,000 yuan and cannot add external funds?

## Turn 10 - User Simulator

It is a formal constraint: the total amount invested at the start of each year cannot exceed the total funds available at that time. You cannot invest more than you have on hand.

## Turn 11 - Generic Agent

QUESTION: Is the objective to maximize the total amount of money (principal plus interest) held at the end of Year 3, which includes both the returns from all matured investments and any uninvested cash carried over, or is it only the sum of the returns from the investments that mature at the end of Year 3?

## Turn 11 - User Simulator

The objective is to maximize the total amount of money (principal plus interest) held at the end of Year 3, which includes both the returns from all matured investments and any uninvested cash carried over.

## Turn 12 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total funds (principal plus interest) at the end of Year 3, including returns from all matured investments and any uninvested cash carried over.

**Decision Variables (all continuous, non-negative):**
- x1_1: Amount invested in product (1) at start of Year 1
- x1_2: Amount invested in product (1) at start of Year 2
- x1_3: Amount invested in product (1) at start of Year 3
- x2: Amount invested in product (2) at start of Year 1
- x3: Amount invested in product (3) at start of Year 2
- x4: Amount invested in product (4) at start of Year 3
- c1: Uninvested cash at start of Year 1 (carries to Year 2)
- c2: Uninvested cash at start of Year 2 (carries to Year 3)
- c3: Uninvested cash at start of Year 3 (counts in final total)

**Constraints:**

1. **Year 1 budget:** x1_1 + x2 + c1 ≤ 500,000
2. **Year 2 budget:** x1_2 + x3 + c2 ≤ 1.20·x1_1 + c1
3. **Year 3 budget:** x1_3 + x4 + c3 ≤ 1.20·x1_2 + 1.60·x3 + 1.50·x2 + c2
4. **Product (2) cap:** x2 ≤ 120,000
5. **Product (3) cap:** x3 ≤ 150,000
6. **Product (4) cap:** x4 ≤ 100,000
7. **Non-negativity:** All variables ≥ 0

**Objective Function:**
Maximize Z = 1.20·x1_3 + 1.40·x4 + c3

**Confirmed Facts:**
- Return factors: 1.20 (product 1), 1.50 (product 2), 1.60 (product 3), 1.40 (product 4) — all applied to full invested amount, no fees/taxes.
- Product (1) available at start of Years 1, 2, 3; unlimited capacity.
- Product (2) available only at start of Year 1; matures end of Year 2.
- Product (3) available only at start of Year 2; matures end of Year 2.
- Product (4) available only at start of Year 3; matures end of Year 3.
- Uninvested cash carries forward with zero return.
- No borrowing: investments in each year cannot exceed funds available.
- No minimum investments, no percentage requirements, no linkages between products.
- Continuous (non-integer) investment amounts.

**Assumptions:** None. All formulation-critical facts were confirmed by the user.