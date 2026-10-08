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

QUESTION: At the end of Year 3, should the objective maximize only the cash from investments that mature at the end of Year 3 (i.e., product 1 invested at the start of Year 3 and product 4), or should it also include the value of any money left uninvested as cash?

## Turn 1 - User Simulator

The objective should maximize the total wealth at the end of Year 3, which includes both the cash from investments that mature at the end of Year 3 and any money left uninvested as cash.

## Turn 2 - Generic Agent

QUESTION: Is there any minimum liquidity requirement that must be kept as cash at the end of each year (e.g., a reserve that cannot be invested), or can all available cash be freely allocated to investments each year?

## Turn 2 - User Simulator

There is no minimum liquidity requirement. All available cash can be freely allocated to investments each year.

## Turn 3 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year, is the 1.20 return the same in all three years, or does the return rate differ by year?

## Turn 3 - User Simulator

The 1.20 return is the same in all three years.

## Turn 4 - Generic Agent

QUESTION: Are there any transaction costs, taxes, or fees associated with investing in or redeeming any of the products, or are all returns net of such costs?

## Turn 4 - User Simulator

There are no transaction costs, taxes, or fees. All returns are net of such costs.

## Turn 5 - Generic Agent

QUESTION: Can investments be made in fractional amounts (continuous), or must investments be in whole yuan (integer) amounts?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Since the integrality question is still pending internally, should I proceed by modeling investments as continuous (fractional) amounts, which is the standard assumption for this type of investment planning problem?

## Turn 6 - User Simulator

Yes, please proceed by modeling investments as continuous (fractional) amounts.

## Turn 7 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total wealth at the end of Year 3, which includes cash from investments maturing at the end of Year 3 plus any uninvested cash.

- **Initial capital:** 500,000 yuan at the beginning of Year 1.

- **Products:**
  - **(1)** 1-year product, available at the beginning of Years 1, 2, and 3. Return: 1.20×I at year-end. Unlimited capacity. Same return in all three years.
  - **(2)** 2-year product, available only at the beginning of Year 1, matures at end of Year 2. Return: 1.50×I. Cap: 120,000 yuan.
  - **(3)** Same-year product, available only at the beginning of Year 2, matures at end of Year 2. Return: 1.60×I. Cap: 150,000 yuan.
  - **(4)** 1-year product, available only at the beginning of Year 3, matures at end of Year 3. Return: 1.40×I. Cap: 100,000 yuan.

- **Constraints:**
  - No minimum liquidity requirement; all available cash can be freely allocated each year.
  - No transaction costs, taxes, or fees.
  - Investments are continuous (fractional) amounts.
  - Cash flow balance: money available at the start of each year equals uninvested carry-over plus proceeds from investments maturing at that point.

- **Decision variables:** Amount invested in each product at each available time point, plus uninvested cash carried forward.

- **Model type:** Linear program (LP).