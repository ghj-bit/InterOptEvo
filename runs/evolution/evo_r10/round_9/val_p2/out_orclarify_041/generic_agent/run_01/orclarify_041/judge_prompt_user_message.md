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

QUESTION: Is there any minimum investment amount required for each product, or can you invest any amount down to zero in each available product?

## Turn 1 - User Simulator

There is no minimum investment amount. You can invest any amount down to zero in each available product.

## Turn 2 - Generic Agent

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (principal plus interest) from all investments that have matured by then, or should any uninvested cash (idle money) also be counted as part of the final amount?

## Turn 2 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes both the proceeds from all investments that have matured by then and any uninvested cash (idle money) remaining.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much cash can be held idle (uninvested) at the end of each year, or can any amount of cash simply carry over to the next year without restriction?

## Turn 3 - User Simulator

There is no limit on how much cash can be held idle. Any amount of cash can simply carry over to the next year without restriction.

## Turn 4 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of a year, does the 1.20·I return become available for reinvestment at the beginning of the next year, or is it only available at the end of the next year?

## Turn 4 - User Simulator

The 1.20·I return becomes available at the end of the year in which you invested. Therefore, if you invest in product (1) at the beginning of Year 1, the return is available at the end of Year 1, which is the same time as the beginning of Year 2, making it available for reinvestment at the beginning of Year 2.

## Turn 5 - Generic Agent

QUESTION: For product (2), which is a 2-year product available only at the beginning of Year 1 and matures at the end of Year 2, is the 1.50·I return available at the end of Year 2 (i.e., the beginning of Year 3) for reinvestment, or is it only available at the end of Year 3?

## Turn 5 - User Simulator

The 1.50·I return is available at the end of Year 2, which is the beginning of Year 3, for reinvestment.

## Turn 6 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available cash at the beginning of each year, or can you choose to hold some cash idle and invest only a portion of it?

## Turn 6 - User Simulator

There is no constraint requiring you to invest all available cash. You can choose to hold some cash idle and invest only a portion of it.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or rules I should be aware of, such as a maximum total investment per year, a requirement to invest in at least one product per year, or any other restrictions beyond what has been described?

## Turn 7 - User Simulator

No, there are no other constraints or rules. The only restrictions are the individual caps on products (2), (3), and (4), and the rule that you cannot borrow money.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total cash on hand at the end of Year 3 (proceeds from all matured investments + any idle cash).

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Decision Variables (all continuous, non-negative, no minimums):**
- x₁₁, x₁₂, x₁₃: Amount invested in product (1) at the beginning of Years 1, 2, and 3 respectively.
- x₂: Amount invested in product (2) at the beginning of Year 1.
- x₃: Amount invested in product (3) at the beginning of Year 2.
- x₄: Amount invested in product (4) at the beginning of Year 3.
- Idle cash carried between periods (unrestricted, non-negative).

**Products and Returns:**
- Product (1): 1-year, available at the beginning of Years 1–3, returns 1.20·I at the end of that year (available for reinvestment at the beginning of the next year). Unlimited capacity.
- Product (2): 2-year, available only at the beginning of Year 1, returns 1.50·I at the end of Year 2 (available for reinvestment at the beginning of Year 3). Cap: 120,000 yuan.
- Product (3): Same-year, available only at the beginning of Year 2, returns 1.60·I at the end of Year 2. Cap: 150,000 yuan.
- Product (4): 1-year, available only at the beginning of Year 3, returns 1.40·I at the end of Year 3. Cap: 100,000 yuan.

**Constraints:**
- Cash flow balance at each decision point (beginning of Year 1, beginning of Year 2, beginning of Year 3): total investments + idle cash ≤ available cash.
- No borrowing (cash cannot go negative).
- x₂ ≤ 120,000
- x₃ ≤ 150,000
- x₄ ≤ 100,000
- No minimum investment amounts.
- No other constraints.

**Timing Convention:** End of Year N = Beginning of Year N+1. Returns are available for reinvestment at that point.