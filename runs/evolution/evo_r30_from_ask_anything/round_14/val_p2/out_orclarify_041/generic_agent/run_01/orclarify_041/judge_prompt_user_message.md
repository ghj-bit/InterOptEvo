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

QUESTION: For the 1-year product (1) that is available at the beginning of each year, is the 1.20 return rate the same for investments made at the start of Year 1, Year 2, and Year 3, or does the rate differ by year?

## Turn 1 - User Simulator

The 1.20 return rate is the same for investments made at the start of Year 1, Year 2, and Year 3.

## Turn 2 - Generic Agent

QUESTION: Is the 500,000 yuan initial capital the only source of funds available at the beginning of Year 1, or can you also borrow or receive additional external funds during the three-year horizon?

## Turn 2 - User Simulator

The 500,000 yuan initial capital is the only source of funds available at the beginning of Year 1. You cannot borrow or receive additional external funds during the three-year horizon.

## Turn 3 - Generic Agent

QUESTION: When funds from a maturing investment are received at the end of a year, can they be immediately reinvested into products available at the beginning of the next year, or is there a delay or restriction on reinvesting those proceeds?

## Turn 3 - User Simulator

Funds from a maturing investment received at the end of a year can be immediately reinvested into products available at the beginning of the next year. There is no delay or restriction on reinvesting those proceeds.

## Turn 4 - Generic Agent

QUESTION: At the end of Year 3, is it required that all funds be invested in a product that matures at the end of Year 3, or can you hold uninvested cash (which earns no interest) at the end of Year 3?

## Turn 4 - User Simulator

You can hold uninvested cash at the end of Year 3. It is not required that all funds be invested in a product that matures at the end of Year 3.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts in each product required to be whole numbers (integer yuan), or can you invest any fractional amount of yuan?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: For the 2-year product (2) that is available only at the beginning of Year 1, is the 120,000 yuan cap a total limit on the single investment made at the start of Year 1, or is it a per-year limit that could apply if the product were available in multiple years?

## Turn 6 - User Simulator

The 120,000 yuan cap is a total limit on the single investment made at the start of Year 1.

## Turn 7 - Generic Agent

QUESTION: Are there any additional constraints or requirements not mentioned in the brief, such as minimum investment amounts for any product, conditional linkages between investments, or other restrictions on how funds can be allocated?

## Turn 7 - User Simulator

There are no additional constraints or requirements beyond those already mentioned.

## Turn 8 - Generic Agent

QUESTION: Is the 150,000 yuan cap on product (3) a total limit on the single investment made at the beginning of Year 2, or is it a per-year limit that could apply if the product were available in multiple years?

## Turn 8 - User Simulator

The 150,000 yuan cap is a total limit on the single investment made at the beginning of Year 2.

## Turn 9 - Generic Agent

QUESTION: Is the 100,000 yuan cap on product (4) a total limit on the single investment made at the beginning of Year 3, or is it a per-year limit that could apply if the product were available in multiple years?

## Turn 9 - User Simulator

The 100,000 yuan cap is a total limit on the single investment made at the beginning of Year 3.

## Turn 10 - Generic Agent

QUESTION: Is the objective to maximize the total value of all funds (including both matured investment proceeds and any uninvested cash) at the end of Year 3, or is it to maximize only the total investment proceeds excluding uninvested cash?

## Turn 10 - User Simulator

The objective is to maximize the total value of all funds, including both matured investment proceeds and any uninvested cash, at the end of Year 3.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

- **Objective:** Maximize total value of all funds (matured investment proceeds plus any uninvested cash) at the end of Year 3.
- **Initial Capital:** 500,000 yuan at the beginning of Year 1. This is the only source of funds; no borrowing or external funds are allowed.
- **Reinvestment:** Funds from maturing investments received at the end of a year can be immediately reinvested at the beginning of the next year with no delay or restriction.
- **Uninvested Cash:** You may hold uninvested cash at the end of Year 3; it is not required to invest all funds.

**Investment Products:**

1. **Product (1):** 1-year product available at the beginning of Years 1, 2, and 3. Return rate is 1.20×I (i.e., 20% interest) for all three years. Unlimited capacity.
2. **Product (2):** 2-year product available only at the beginning of Year 1, maturing at the end of Year 2. Return is 1.50×I. Total investment cap: 120,000 yuan.
3. **Product (3):** Same-year product available only at the beginning of Year 2, maturing at the end of Year 2. Return is 1.60×I. Total investment cap: 150,000 yuan.
4. **Product (4):** 1-year product available only at the beginning of Year 3, maturing at the end of Year 3. Return is 1.40×I. Total investment cap: 100,000 yuan.

**Constraints:**

- Investment in Product (2) ≤ 120,000 yuan (total, single investment at start of Year 1).
- Investment in Product (3) ≤ 150,000 yuan (total, single investment at start of Year 2).
- Investment in Product (4) ≤ 100,000 yuan (total, single investment at start of Year 3).
- No additional constraints beyond those listed.

**Assumptions:**

- **Investment granularity:** It was not confirmed whether investment amounts must be whole numbers (integer yuan) or can be fractional. I will assume investments can be any non-negative real number (continuous, non-negative). If integer constraints are required, the model can be adjusted accordingly.