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

QUESTION: For the 1-year product (1), is the 1.20·I payout at year-end automatically reinvestable at the beginning of the next year, or does it require a separate explicit decision to reinvest?

## Turn 2 - User Simulator

It requires a separate explicit decision to reinvest. At the beginning of each year, you decide how to allocate the cash available at that moment, which includes proceeds from investments that have just matured.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum investment amount or divisibility requirement for any of the products, or can you invest any non-negative continuous amount (including zero) in each product at each time it is available?

## Turn 3 - User Simulator

You can invest any non-negative continuous amount (including zero) in each product at each time it is available. There are no minimum investment amounts or divisibility requirements.

## Turn 4 - Generic Agent

QUESTION: Is there any constraint that the total amount invested at the beginning of a year cannot exceed the cash available at that moment (i.e., no borrowing or leverage allowed)?

## Turn 4 - User Simulator

Yes, there is a constraint that the total amount invested at the beginning of a year cannot exceed the cash available at that moment. No borrowing or leverage is allowed.

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 1, the 500,000 yuan can be allocated among product (1) Year 1, product (2), and left as idle cash. Is there any reason to leave cash idle at the beginning of Year 1 (e.g., a penalty or restriction), or is idle cash simply carried forward to the beginning of Year 2 with no return?

## Turn 5 - User Simulator

Idle cash is simply carried forward to the beginning of Year 2 with no return. There is no penalty or restriction for leaving cash idle.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 2, the available cash can be allocated among product (1) Year 2, product (3), and left as idle cash. Is there any reason to leave cash idle at the beginning of Year 2, or is idle cash simply carried forward to the beginning of Year 3 with no return?

## Turn 6 - User Simulator

Idle cash is simply carried forward to the beginning of Year 3 with no return. There is no penalty or restriction for leaving cash idle.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 3, the available cash can be allocated among product (1) Year 3, product (4), and left as idle cash. Is there any reason to leave cash idle at the beginning of Year 3, or is idle cash simply counted in the final wealth at the end of Year 3 with no return?

## Turn 7 - User Simulator

Idle cash is simply counted in the final wealth at the end of Year 3 with no return. There is no penalty or restriction for leaving cash idle.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total wealth (principal + interest) at the end of Year 3, including any uninvested cash.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Decision variables (all continuous, non-negative):**
- x1_1: amount invested in product (1) at beginning of Year 1
- x1_2: amount invested in product (1) at beginning of Year 2
- x1_3: amount invested in product (1) at beginning of Year 3
- x2: amount invested in product (2) at beginning of Year 1
- x3: amount invested in product (3) at beginning of Year 2
- x4: amount invested in product (4) at beginning of Year 3
- c1: idle cash carried from beginning of Year 1 to beginning of Year 2
- c2: idle cash carried from beginning of Year 2 to beginning of Year 3
- c3: idle cash at end of Year 3 (counted in objective)

**Returns:**
- Product (1): 1.20×I at end of the same year (available Years 1–3, unlimited capacity)
- Product (2): 1.50×I at end of Year 2 (available only at beginning of Year 1, cap 120,000)
- Product (3): 1.60×I at end of Year 2 (available only at beginning of Year 2, cap 150,000)
- Product (4): 1.40×I at end of Year 3 (available only at beginning of Year 3, cap 100,000)

**Cash flow constraints (no borrowing):**
- Beginning of Year 1: x1_1 + x2 + c1 ≤ 500,000
- Beginning of Year 2: x1_2 + x3 + c2 ≤ 1.20·x1_1 + 1.50·x2 + c1
- Beginning of Year 3: x1_3 + x4 + c3 ≤ 1.20·x1_2 + 1.60·x3 + c2

**Capacity constraints:**
- x2 ≤ 120,000
- x3 ≤ 150,000
- x4 ≤ 100,000

**Objective function:**
Maximize 1.20·x1_3 + c3

(All other investments mature before end of Year 3 and their proceeds are already captured in the Year 3 cash flow constraint.)