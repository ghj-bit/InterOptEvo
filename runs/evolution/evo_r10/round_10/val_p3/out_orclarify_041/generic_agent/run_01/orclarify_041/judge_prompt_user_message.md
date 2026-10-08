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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash left idle) counted toward the total principal plus interest you want to maximize?

## Turn 1 - User Simulator

Yes. The objective is to maximize your total wealth at the end of Year 3, which includes any cash that remains uninvested at that time.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how much cash can be carried over from one year to the next, or can you freely roll over any uninvested cash into the following year's investments?

## Turn 2 - User Simulator

There is no limit on carrying over cash. You can freely roll over any uninvested cash into the following year's investments, subject only to the rule that you cannot borrow money.

## Turn 3 - Generic Agent

QUESTION: Can you invest in product (1) more than once within the same year, or is there at most one investment in product (1) per year?

## Turn 3 - User Simulator

There is at most one investment in product (1) per year.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any amount down to zero?

## Turn 4 - User Simulator

There is no minimum investment amount. You can invest any amount down to zero in any of the products.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts in each product required to be whole numbers (integer yuan), or can they be any fractional amount?

## Turn 5 - User Simulator

The investment amounts can be any fractional amount; they do not need to be whole numbers.

## Turn 6 - Generic Agent

QUESTION: Is there any other constraint or rule I should know about, such as a requirement to invest all available cash each year, or any other restriction on how funds can be allocated?

## Turn 6 - User Simulator

No. There is no requirement to invest all available cash each year. The only restrictions are the individual caps on products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total wealth (principal + interest + any uninvested cash) at the end of Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Decision variables (all continuous, non-negative):**
- x1: amount invested in product (1) at the start of Year 1
- x2: amount invested in product (1) at the start of Year 2
- x3: amount invested in product (1) at the start of Year 3
- x4: amount invested in product (2) at the start of Year 1
- x5: amount invested in product (3) at the start of Year 2
- x6: amount invested in product (4) at the start of Year 3
- c1: cash carried from end of Year 1 to start of Year 2
- c2: cash carried from end of Year 2 to start of Year 3

**Products and returns:**
- Product (1): 1-year, available at start of Years 1–3, returns 1.20×I at year-end. Unlimited capacity. At most one investment per year.
- Product (2): 2-year, available only at start of Year 1, matures end of Year 2, returns 1.50×I. Cap: 120,000.
- Product (3): Same-year (1-year), available only at start of Year 2, matures end of Year 2, returns 1.60×I. Cap: 150,000.
- Product (4): 1-year, available only at start of Year 3, matures end of Year 3, returns 1.40×I. Cap: 100,000.

**Cash flow / budget constraints (no borrowing):**
- Year 1: x1 + x4 + c1 ≤ 500,000
- Year 2: x2 + x5 + c2 ≤ 1.20·x1 + 1.50·x4 + c1
- Year 3: x3 + x6 ≤ 1.20·x2 + 1.60·x5 + c2

**Caps:**
- x4 ≤ 120,000
- x5 ≤ 150,000
- x6 ≤ 100,000

**Objective function:**
Maximize 1.20·x3 + 1.40·x6 + c2

**Other rules:**
- No minimum investment; any amount from 0 up is allowed.
- No limit on cash carryover.
- No requirement to invest all available cash each year.
- All variables are continuous and non-negative.