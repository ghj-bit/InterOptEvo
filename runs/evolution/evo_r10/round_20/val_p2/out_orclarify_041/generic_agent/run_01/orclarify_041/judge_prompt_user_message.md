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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash held idle) counted at its full face value toward the objective, or must all funds be placed in an investment to count?

## Turn 1 - User Simulator

Cash held idle at the end of Year 3 counts at its full face value toward the objective.

## Turn 2 - Generic Agent

QUESTION: Can funds be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 2 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 3 - Generic Agent

QUESTION: Can funds that mature at the end of Year 2 (from products 1, 2, or 3) be reinvested at the beginning of Year 3, or do they simply sit as cash until the end of Year 3?

## Turn 3 - User Simulator

Funds that mature at the end of Year 2 can be reinvested at the beginning of Year 3.

## Turn 4 - Generic Agent

QUESTION: Can funds that mature at the end of Year 1 (from product 1 invested at the start of Year 1) be reinvested at the beginning of Year 2, or do they simply sit as cash until the end of Year 2?

## Turn 4 - User Simulator

Funds that mature at the end of Year 1 can be reinvested at the beginning of Year 2.

## Turn 5 - Generic Agent

QUESTION: Are there any minimum investment amounts for any of the four products, or can any non-negative amount (including zero) be invested in each?

## Turn 5 - User Simulator

There are no minimum investment amounts. Any non-negative amount, including zero, can be invested in each product.

## Turn 6 - Generic Agent

QUESTION: Can the investment amounts in each product be any continuous (fractional) value, or must they be whole yuan amounts (integers)?

## Turn 6 - User Simulator

The investment amounts can be any continuous (fractional) value.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited as stated?

## Turn 7 - User Simulator

Product (1) is truly unlimited.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 2, can funds be invested in both product (1) and product (3) simultaneously, or is there any restriction on combining investments in the same year?

## Turn 8 - User Simulator

Funds can be invested in both product (1) and product (3) simultaneously at the beginning of Year 2.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 3, can funds be invested in both product (1) and product (4) simultaneously, or is there any restriction on combining investments in the same year?

## Turn 9 - User Simulator

Funds can be invested in both product (1) and product (4) simultaneously at the beginning of Year 3.

## Turn 10 - Generic Agent

QUESTION: Is there any requirement that all available funds must be invested at the beginning of each year, or is it permissible to hold some funds as cash (uninvested) during a year?

## Turn 10 - User Simulator

It is permissible to hold some funds as cash (uninvested) during a year.

## Turn 11 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax associated with investing in or redeeming any of the four products, or are the stated returns (1.20, 1.50, 1.60, 1.40) the exact net multipliers?

## Turn 11 - User Simulator

The stated returns (1.20, 1.50, 1.60, 1.40) are the exact net multipliers.

## Turn 12 - Generic Agent

QUESTION: Is there any requirement that the initial 500,000 yuan must be fully allocated at the beginning of Year 1, or can some of it be held as cash and invested in later years?

## Turn 12 - User Simulator

Some of the initial 500,000 yuan can be held as cash and invested in later years.

## Turn 13 - Generic Agent

QUESTION: Is there any restriction on the total amount of cash that can be held at any point in time, or can any amount of cash be carried forward from one year to the next?

## Turn 13 - User Simulator

There is no restriction on the total amount of cash that can be held. Any amount of cash can be carried forward from one year to the next.

## Turn 14 - Generic Agent

QUESTION: Is there any requirement that the final amount at the end of Year 3 must meet a minimum threshold, or is the sole objective to maximize the total amount with no minimum requirement?

## Turn 14 - User Simulator

The sole objective is to maximize the total amount at the end of Year 3, with no minimum requirement.

## Turn 15 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

**Objective:** Maximize total principal plus interest (cash + matured investments) at the end of Year 3.

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Investment Products:**

| Product | Type | Available | Matures | Return | Capacity |
|---------|------|-----------|---------|--------|----------|
| (1) | 1-year | Beginning of Years 1, 2, 3 | End of same year | 1.20·I | Unlimited |
| (2) | 2-year | Beginning of Year 1 only | End of Year 2 | 1.50·I | ≤ 120,000 |
| (3) | Same-year | Beginning of Year 2 only | End of Year 2 | 1.60·I | ≤ 150,000 |
| (4) | 1-year | Beginning of Year 3 only | End of Year 3 | 1.40·I | ≤ 100,000 |

**Key Rules Confirmed:**
- Cash held idle at end of Year 3 counts at full face value.
- Funds maturing at end of Year 1 can be reinvested at beginning of Year 2.
- Funds maturing at end of Year 2 can be reinvested at beginning of Year 3.
- No minimum investment amounts; any non-negative continuous value allowed.
- No transaction costs, fees, or taxes; stated returns are exact net multipliers.
- Multiple products can be invested in simultaneously in the same year (e.g., products 1 and 3 in Year 2; products 1 and 4 in Year 3).
- Cash can be carried forward without restriction; no requirement to fully invest each year.
- No minimum final amount requirement.
- All decision variables are continuous and non-negative.

**Structure:** This is a 3-period linear program with cash-flow balance constraints at the beginning of each year, capacity constraints on products (2), (3), and (4), and a maximization objective on the end-of-Year-3 total.