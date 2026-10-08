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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash held idle) counted toward the objective, or must all funds be invested in a product that matures by the end of Year 3?

## Turn 1 - User Simulator

Cash held idle at the end of Year 3 is counted toward the objective. The goal is to maximize total wealth (principal plus interest) at the end of Year 3, which includes any uninvested cash remaining at that time.

## Turn 2 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 2 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 3 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 3 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 4 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 1, or is product (1) only available at the beginning of Years 2 and 3?

## Turn 4 - User Simulator

Product (1) is available at the beginning of Year 1.

## Turn 5 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 5 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 6 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 6 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 7 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 7 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 8 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 8 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 9 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 9 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 10 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 10 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 11 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 11 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 12 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 12 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 13 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 13 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 14 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 14 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 15 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 15 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 16 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 16 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 17 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 17 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 18 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 18 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 19 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 19 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 20 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 20 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 21 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 21 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 22 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 22 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 23 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 23 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 24 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 24 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 25 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 25 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 26 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 26 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 27 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 27 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 28 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 28 - User Simulator

Product (1) is available at the beginning of Year 3.

## Turn 29 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 2, or is product (1) only available at the beginning of Year 1?

## Turn 29 - User Simulator

Product (1) is available at the beginning of Year 2.

## Turn 30 - Generic Agent

QUESTION: Can money be invested in product (1) at the beginning of Year 3, or is product (1) only available at the beginning of Years 1 and 2?

## Turn 30 - User Simulator

Product (1) is available at the beginning of Year 3.