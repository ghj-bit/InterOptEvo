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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., the sum of all matured proceeds from products 1, 2, 3, and 4), or should any uninvested cash that was never put into a product also count toward that total?

## Turn 1 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes both the matured proceeds from any investments and any uninvested cash that remains.

## Turn 2 - Generic Agent

QUESTION: If you invest in product (1) at the beginning of Year 3, it matures at the end of Year 3 and pays 1.20·I — so it is available for the Year 3 objective. But is product (1) also available at the beginning of Year 3 in the sense that you can choose to invest in it then, or is it only available at the beginnings of Years 1 and 2?

## Turn 2 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 3 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of a year, does the invested amount have to come from cash available at that exact moment (i.e., you cannot invest more than you currently hold), or is there any other source of funds (like borrowing) that could finance the investment?

## Turn 3 - User Simulator

The invested amount must come from cash available at that exact moment. You cannot borrow money.

## Turn 4 - Generic Agent

QUESTION: At the end of each year, when a product matures and pays out, does that cash become immediately available for investment at the beginning of the next year, or is there any delay or restriction on using matured proceeds?

## Turn 4 - User Simulator

Matured proceeds become immediately available for investment at the beginning of the next year.

## Turn 5 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the four products, or can you invest any non-negative amount (including zero) in each?

## Turn 5 - User Simulator

There is no minimum investment amount. You can invest any non-negative amount, including zero, in each product.

## Turn 6 - Generic Agent

QUESTION: Are the investment amounts required to be whole yuan amounts (integer), or can they be any continuous non-negative value (e.g., 12,345.67 yuan)?

## Turn 6 - User Simulator

The investment amounts can be any continuous non-negative value.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1), or is it truly unlimited as stated?

## Turn 7 - User Simulator

Product (1) is truly unlimited.

## Turn 8 - Generic Agent

QUESTION: Is there any other constraint or rule I should be aware of that isn't mentioned in the brief — for example, a requirement to invest all available cash each year, a penalty for holding uninvested cash, or any tax on returns?

## Turn 8 - User Simulator

No, there are no other constraints or rules. You are not required to invest all available cash each year, there is no penalty for holding uninvested cash, and there are no taxes on returns.

## Turn 9 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash on hand at the end of Year 3 (sum of all matured proceeds plus any uninvested cash).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Decision variables (continuous, non-negative):**
- x1_1, x1_2, x1_3: amount invested in product (1) at the beginning of Years 1, 2, and 3 respectively (unlimited).
- x2_1: amount invested in product (2) at the beginning of Year 1 (cap: 120,000).
- x3_2: amount invested in product (3) at the beginning of Year 2 (cap: 150,000).
- x4_3: amount invested in product (4) at the beginning of Year 3 (cap: 100,000).

**Cash-flow / budget constraints (no borrowing; invested amount must come from cash on hand at that moment):**
- Beginning of Year 1: x1_1 + x2_1 ≤ 500,000.
- Beginning of Year 2: x1_2 + x3_2 ≤ (cash carried from Year 1) + 1.20·x1_1, where cash carried from Year 1 = 500,000 − x1_1 − x2_1.
- Beginning of Year 3: x1_3 + x4_3 ≤ (cash carried from Year 2) + 1.20·x1_2 + 1.50·x2_1 + 1.60·x3_2, where cash carried from Year 2 = (cash available at start of Year 2) − x1_2 − x3_2.

**Maturities feeding the Year 3 end-of-horizon cash:**
- Product (1) Year 3: 1.20·x1_3 (matures end of Year 3).
- Product (1) Year 2: 1.20·x1_2 (matures end of Year 2, available at start of Year 3).
- Product (2): 1.50·x2_1 (matures end of Year 2, available at start of Year 3).
- Product (3): 1.60·x3_2 (matures end of Year 2, available at start of Year 3).
- Product (4): 1.40·x4_3 (matures end of Year 3).

**Caps:**
- x2_1 ≤ 120,000
- x3_2 ≤ 150,000
- x4_3 ≤ 100,000

**Other confirmed facts:**
- No minimum investment; zero is allowed.
- No borrowing; no taxes; no penalty for idle cash.
- All amounts are continuous non-negative values.
- No other hidden constraints.