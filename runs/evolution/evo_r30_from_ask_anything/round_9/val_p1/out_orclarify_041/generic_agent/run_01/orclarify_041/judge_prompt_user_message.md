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

QUESTION: For the 1-year product (1) that is available at the beginning of each year, is the 1.20 return multiplier the same for investments made at the start of Year 1, Year 2, and Year 3, or does the rate differ by year

## Turn 1 - User Simulator

The 1.20 return multiplier is the same for investments made at the start of Year 1, Year 2, and Year 3.

## Turn 2 - Generic Agent

QUESTION: When you say "maximize total principal plus interest at the end of Year 3," do you mean the total cash value of all matured investments at the end of Year 3

## Turn 2 - User Simulator

Yes, it means the total cash value of all matured investments at the end of Year 3.

## Turn 3 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief

## Turn 3 - User Simulator

Yes, there is one additional constraint: no borrowing is allowed. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 4 - Generic Agent

QUESTION: For the 2-year product (2) that matures at the end of Year 2, is the 1.50 return multiplier applied to the initial investment amount I

## Turn 4 - User Simulator

Yes, the 1.50 return multiplier is applied to the initial investment amount I.

## Turn 5 - Generic Agent

QUESTION: For the same-year product (3) available at the beginning of Year 2, is the 1.60 return multiplier applied to the initial investment amount

## Turn 5 - User Simulator

Yes, the 1.60 return multiplier is applied to the initial investment amount.

## Turn 6 - Generic Agent

QUESTION: For the 1-year product (4) available at the beginning of Year 3, is the 1.40 return

## Turn 6 - User Simulator

Yes, the 1.40 return multiplier is applied to the initial investment amount.

## Turn 7 - Generic Agent

QUESTION: Are all investment amounts required to be non

## Turn 7 - User Simulator

Yes, all investment amounts must be non-negative.

## Turn 8 - Generic Agent

QUESTION: Are investment amounts required to be integer values

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: Should I assume investment amounts can be any non-negative real number

## Turn 9 - User Simulator

Yes, investment amounts can be any non-negative real number.

## Turn 10 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize total cash value of all matured investments at the end of Year 3. (Confirmed)

2. **Time Horizon:** 3 years (Year 1, Year 2, Year 3). (Confirmed)

3. **Initial Capital:** 500,000 yuan at the beginning of Year 1. (Confirmed)

4. **Investment Products:**
   - **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Return multiplier is 1.20 for all years. Unlimited capacity. (Confirmed)
   - **Product (2):** 2-year product, available only at the beginning of Year 1, matures at end of Year 2. Return multiplier is 1.50. Capped at 120,000 yuan. (Confirmed)
   - **Product (3):** Same-year product, available only at the beginning of Year 2, matures at end of Year 2. Return multiplier is 1.60. Capped at 150,000 yuan. (Confirmed)
   - **Product (4):** 1-year product, available only at the beginning of Year 3, matures at end of Year 3. Return multiplier is 1.40. Capped at 100,000 yuan. (Confirmed)

5. **Constraints:**
   - Investment in Product (2) ≤ 120,000 yuan. (Confirmed)
   - Investment in Product (3) ≤ 150,000 yuan. (Confirmed)
   - Investment in Product (4) ≤ 100,000 yuan. (Confirmed)
   - No borrowing allowed: at the beginning of each year, total investments cannot exceed available cash (initial capital plus proceeds from matured investments). (Confirmed)
   - All investment amounts are non-negative. (Confirmed)
   - Investment amounts can be any non-negative real number (continuous, not integer). (Confirmed)

6. **Cash Flow Logic:**
   - Beginning of Year 1: Available cash = 500,000 yuan. Can invest in Products (1) and (2).
   - Beginning of Year 2: Available cash = proceeds from Product (1) invested in Year 1 (1.20 × I1_Year1). Can invest in Products (1) and (3).
   - Beginning of Year 3: Available cash = proceeds from Product (1) invested in Year 2 (1.20 × I1_Year2) + proceeds from Product (2) (1.50 × I2) + proceeds from Product (3) (1.60 × I3). Can invest in Products (1) and (4).
   - End of Year 3: Total cash = proceeds from Product (1) invested in Year 3 (1.20 × I1_Year3) + proceeds from Product (4) (1.40 × I4). This is the objective to maximize.

**Open Assumptions:** None. All formulation-critical facts have been confirmed.