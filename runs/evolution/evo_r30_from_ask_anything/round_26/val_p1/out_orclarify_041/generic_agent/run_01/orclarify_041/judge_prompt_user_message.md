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

QUESTION: Is the 500,000 yuan initial capital the only source of funds available for investment at the beginning of Year 1, or will additional external funds be injected during the three-year period?

## Turn 1 - User Simulator

The 500,000 yuan initial capital is the only source of funds available at the beginning of Year 1. No additional external funds will be injected during the three-year period.

## Turn 2 - Generic Agent

QUESTION: When you say "maximize total principal plus interest at the end of Year 3," do you mean maximizing the total cash value of all matured investments at the end of Year 3, or do you mean maximizing the net profit (total returns minus the initial 500,000 yuan)?

## Turn 2 - User Simulator

I mean maximizing the total cash value of all matured investments at the end of Year 3.

## Turn 3 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20 multiplier a gross return (meaning you receive 1.20 times your investment, which includes the original principal plus 20% interest), or is it a net interest rate (meaning you receive your original principal plus an additional 1.20 times your investment as interest)?

## Turn 3 - User Simulator

The 1.20 multiplier is a gross return. You receive 1.20 times your investment, which includes the original principal plus 20% interest.

## Turn 4 - Generic Agent

QUESTION: Are the multipliers for products (2), (3), and (4) also gross returns, meaning you receive the stated multiple of your investment including the original principal?

## Turn 4 - User Simulator

Yes, the multipliers for products (2), (3), and (4) are also gross returns. You receive the stated multiple of your investment, which includes the original principal plus interest.

## Turn 5 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integers), or can they be any non-negative real number?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Can you confirm whether the investment amounts must be whole numbers or can they be any non-negative real number?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements for the investment plan that have not been mentioned yet, such as minimum investment amounts, diversification rules, or restrictions on how funds can be carried over between years?

## Turn 7 - User Simulator

No, there are no other constraints or requirements beyond those already mentioned.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1. **Objective:** Maximize the total cash value of all matured investments at the end of Year 3.
2. **Initial Capital:** 500,000 yuan available at the beginning of Year 1. No additional external funds will be injected during the three-year period.
3. **Investment Products:**
   - **Product (1):** 1-year product available at the beginning of Years 1, 2, and 3. Gross return of 1.20x. Unlimited capacity.
   - **Product (2):** 2-year product available only at the beginning of Year 1. Matures at the end of Year 2. Gross return of 1.50x. Maximum investment: 120,000 yuan.
   - **Product (3):** Same-year product available only at the beginning of Year 2. Matures at the end of Year 2. Gross return of 1.60x. Maximum investment: 150,000 yuan.
   - **Product (4):** 1-year product available only at the beginning of Year 3. Matures at the end of Year 3. Gross return of 1.40x. Maximum investment: 100,000 yuan.
4. **Returns:** All multipliers are gross returns (include principal plus interest).
5. **No Additional Constraints:** No minimum investment amounts, diversification rules, or other restrictions beyond those specified.

**Assumptions:**

1. **Investment Amounts:** Investment amounts can be any non-negative real number (continuous variables), as this point was not confirmed by the user.
2. **Fund Flow:** Funds from matured investments can be reinvested in subsequent years. For example, proceeds from Product (2) maturing at the end of Year 2 can be invested in Product (1) or Product (4) at the beginning of Year 3.
3. **Uninvested Funds:** Any funds not invested at the end of Year 3 are included in the total cash value at the end of Year 3.