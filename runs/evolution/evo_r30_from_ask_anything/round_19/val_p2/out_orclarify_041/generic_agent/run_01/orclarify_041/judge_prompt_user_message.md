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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or can you also invest the proceeds from maturing projects in subsequent years?

## Turn 1 - User Simulator

The 500,000 yuan is the only source of funds at the beginning of Year 1. In subsequent years, you can also invest the proceeds from projects that have already matured.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the investment amount at the beginning of each year a separate decision variable that can be chosen independently for each of the three years, subject only to the available funds at that time?

## Turn 2 - User Simulator

Yes.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four products, or can you invest any non-negative amount up to the stated caps?

## Turn 3 - User Simulator

There are no minimum investment amounts. You can invest any non-negative amount up to the stated caps.

## Turn 4 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integer yuan), or can they be any continuous non-negative value?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is the 1.20 return for product (1) a total multiplier (meaning you receive 1.20 times your investment at year-end, including principal), or is it a 20% interest rate on top of the principal (meaning you receive 1.20 times your investment total)?

## Turn 5 - User Simulator

It is a total multiplier. You receive 1.20 times your investment at year-end, including principal.

## Turn 6 - Generic Agent

QUESTION: Are the returns for products (2), (3), and (4) also total multipliers, meaning you receive 1.50, 1.60, and 1.40 times your investment respectively at maturity, including principal?

## Turn 6 - User Simulator

Yes.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as a requirement to invest all available funds each year, a limit on the total number of products you can hold simultaneously, or any other rules governing how funds flow between years?

## Turn 7 - User Simulator

No. The only constraints are the caps on products (2), (3), and (4), and the rule that you cannot borrow; you can only invest cash available at the beginning of each year from initial capital and matured proceeds.

## Turn 8 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year 3, which includes the proceeds from all investments maturing at that time, or is there a different definition of "total principal plus interest" you have in mind?

## Turn 8 - User Simulator

Yes, the objective is to maximize the total cash available at the end of Year 3, which includes the proceeds from all investments maturing at that time.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize total cash available at the end of Year 3. (Confirmed)
2. **Time Horizon:** 3 years. (Confirmed)
3. **Initial Capital:** 500,000 yuan at the beginning of Year 1. (Confirmed)
4. **Funding Rule:** No borrowing allowed. Investments in any year can only be funded by initial capital (Year 1) or proceeds from investments maturing in prior years. (Confirmed)
5. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Return is a total multiplier of 1.20 (i.e., receive 1.20 × investment at year-end). Unlimited capacity. Investment amount is a separate decision variable for each year. (Confirmed)
6. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2. Return is a total multiplier of 1.50. Maximum investment: 120,000 yuan. (Confirmed)
7. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2. Return is a total multiplier of 1.60. Maximum investment: 150,000 yuan. (Confirmed)
8. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3. Return is a total multiplier of 1.40. Maximum investment: 100,000 yuan. (Confirmed)
9. **Minimum Investments:** None. Any non-negative amount up to the caps is allowed. (Confirmed)
10. **Variable Domain:** Continuous non-negative values. (Assumed – user indicated this point still needs internal confirmation, so I am assuming continuous variables for now.)
11. **Other Constraints:** None beyond the caps and the no-borrowing rule. (Confirmed)

**Open Assumptions:**
- Investment amounts are treated as continuous variables (not restricted to integer yuan). If integer constraints are required, the model would need to be adjusted accordingly.