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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment, or can you also use funds received from maturing investments in subsequent years to make new investments

## Turn 1 - User Simulator

You can use funds received from maturing investments in subsequent years to make new investments. The 500,000 yuan is the starting capital, but as investments mature, the proceeds become available cash that can be reinvested in the following years.

## Turn 2 - Generic Agent

QUESTION: Can you invest in the 1-year product (1) at the beginning of Year

## Turn 2 - User Simulator

Yes, you can invest in the 1-year product (1) at the beginning of Year 1, Year 2, and Year 3.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum investment amounts

## Turn 3 - User Simulator

No, there are no minimum investment amounts.

## Turn 4 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year

## Turn 4 - User Simulator

Yes, the objective is to maximize the total cash available at the end of Year 3.

## Turn 5 - Generic Agent

READY_TO_MODEL

I have confirmed the following understanding of your investment planning problem:

**Objective:** Maximize total cash available at the end of Year 3.

**Initial Capital:** 500,000 yuan at the beginning of Year 1.

**Cash Flow Rule:** Proceeds from maturing investments become available cash that can be reinvested in subsequent years.

**Investment Products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at the end of that year. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, paying 1.50×I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, paying 1.60×I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, paying 1.40×I. Capped at 100,000 yuan.

**Constraints:**
- No minimum investment amounts.
- Investment in Product (2) ≤ 120,000 yuan.
- Investment in Product (3) ≤ 150,000 yuan.
- Investment in Product (4) ≤ 100,000 yuan.
- At the beginning of each year, total investments cannot exceed available cash (initial capital plus proceeds from maturing investments).

**Decision Variables:**
- Amount invested in Product (1) at the beginning of Year 1, Year 2, and Year 3.
- Amount invested in Product (2) at the beginning of Year 1.
- Amount invested in Product (3) at the beginning of Year 2.
- Amount invested in Product (4) at the beginning of Year 3.

I am ready to formulate and solve this linear programming problem to determine the optimal investment allocation that maximizes your total cash at the end of Year 3.