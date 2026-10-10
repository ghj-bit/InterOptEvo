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

QUESTION: Is the 500,000 yuan initial capital the only source of funds, or can you also invest money received from maturing products in subsequent years?

## Turn 1 - User Simulator

The 500,000 yuan is not the only source of funds. You can also invest money received from maturing products in subsequent years. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20 return a total multiplier (meaning you get back 1.20 times your investment) or a 20% interest rate (meaning you get back 1.20 times your investment)?

## Turn 2 - User Simulator

The 1.20 is a total multiplier. If you invest I at the start of a year, you receive 1.20·I at that year’s end.

## Turn 3 - Generic Agent

QUESTION: Are the returns for products (2), (3), and (4) also total multipliers, meaning you receive 1.50·I, 1.60·I, and 1.40·I respectively at maturity?

## Turn 3 - User Simulator

Yes, the returns for products (2), (3), and (4) are also total multipliers. You receive 1.50·I, 1.60·I, and 1.40·I respectively at maturity.

## Turn 4 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as minimum investment amounts, mandatory diversification, or restrictions on how much you can leave uninvested?

## Turn 4 - User Simulator

No, there are no other constraints or requirements not mentioned in the brief.

## Turn 5 - Generic Agent

QUESTION: Can you leave cash uninvested at the end of any year, or must all available cash be invested in at least one product each year?

## Turn 5 - User Simulator

You can leave cash uninvested. There is no requirement that all available cash must be invested in at least one product each year.

## Turn 6 - Generic Agent

QUESTION: Is the investment amount in each product required to be a whole number of yuan, or can it be any non-negative real number?

## Turn 6 - User Simulator

The point still needs internal confirmation.

## Turn 7 - Generic Agent

QUESTION: Should I assume investment amounts can be any non-negative real number (continuous), or must they be integer yuan values?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is the objective to maximize the total cash available at the end of Year 3, including any uninvested cash plus proceeds from maturing investments?

## Turn 8 - User Simulator

Yes, the objective is to maximize the total cash available at the end of Year 3, including any uninvested cash plus proceeds from maturing investments.

## Turn 9 - Generic Agent

READY_TO_MODEL

**Confirmed Facts:**

1. **Objective:** Maximize total cash available at the end of Year 3 (proceeds from maturing investments plus any uninvested cash).
2. **Initial Capital:** 500,000 yuan at the beginning of Year 1.
3. **Cash Flow Rule:** At the beginning of each year, available cash equals initial capital (Year 1 only) plus proceeds from investments that have already matured. You can invest any portion of available cash and leave the rest uninvested.
4. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Invest I at start of year, receive 1.20·I at end of that year. Unlimited capacity.
5. **Product (2):** 2-year product, available only at the beginning of Year 1. Invest I at start of Year 1, receive 1.50·I at end of Year 2. Capped at 120,000 yuan.
6. **Product (3):** Same-year product, available only at the beginning of Year 2. Invest I at start of Year 2, receive 1.60·I at end of Year 2. Capped at 150,000 yuan.
7. **Product (4):** 1-year product, available only at the beginning of Year 3. Invest I at start of Year 3, receive 1.40·I at end of Year 3. Capped at 100,000 yuan.
8. **Uninvested Cash:** Permitted. No requirement to invest all available cash each year.
9. **No Other Constraints:** No minimum investments, no diversification requirements, no other restrictions.

**Assumed (Unconfirmed):**

1. **Variable Domain:** Investment amounts are assumed to be continuous non-negative real numbers (not restricted to integer yuan). This was flagged as needing internal confirmation but was not resolved. If integer constraints are required, the model would need to be adjusted accordingly.