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

QUESTION: At the end of Year 3, should the objective maximize only the cash actually received from maturing investments (i.e., exclude any uninvested cash held as idle balance), or should it include any leftover uninvested cash carried to the end of Year 3?

## Turn 1 - User Simulator

The objective should include any leftover uninvested cash carried to the end of Year 3. The goal is to maximize total wealth at the end of Year 3, which encompasses all available funds, whether they are proceeds from matured investments or uninvested cash.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is it allowed to invest in it at the beginning of Year 3 (so it matures at the end of Year 3), or is it only available at the beginning of Years 1 and 2?

## Turn 2 - User Simulator

It is allowed to invest in product (1) at the beginning of Year 3. It is available at the beginning of each year (Years 1–3).

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how much can be invested in product (1) in any given year, or is it truly unlimited as stated?

## Turn 3 - User Simulator

It is truly unlimited as stated.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum investment amounts or divisibility requirements for any of the products, or can investments be any non-negative continuous amount?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax that reduces the amount invested or the amount received at maturity for any of the products?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: Can cash received from a maturing investment at the end of a year be immediately reinvested in products available at the beginning of the next year, or is there a timing gap that prevents same-cycle reinvestment?

## Turn 6 - User Simulator

Cash received from a maturing investment at the end of a year can be immediately reinvested in products available at the beginning of the next year.

## Turn 7 - Generic Agent

QUESTION: Is there any constraint that requires all available cash at the beginning of each year to be fully invested, or is it permissible to hold some cash idle (earning no return) at the beginning of a year?

## Turn 7 - User Simulator

It is permissible to hold some cash idle at the beginning of a year. There is no constraint requiring all available cash to be fully invested.

## Turn 8 - Generic Agent

QUESTION: Can cash received from product (3) at the end of Year 2 be reinvested in product (1) at the beginning of Year 3, or is product (1) at the beginning of Year 3 only available to cash that was already held at the start of Year 3?

## Turn 8 - User Simulator

Cash received from product (3) at the end of Year 2 can be reinvested in product (1) at the beginning of Year 3.

## Turn 9 - Generic Agent

QUESTION: Is there any constraint that the total amount invested across all products in a single year cannot exceed the available cash at the beginning of that year, or can you invest more than available cash (e.g., by borrowing)?

## Turn 9 - User Simulator

No borrowing is allowed. The total amount invested in any year cannot exceed the available cash at the beginning of that year, which comes from initial capital and proceeds from matured investments.

## Turn 10 - Generic Agent

QUESTION: Regarding the two points still pending internal confirmation (minimum investment amounts/divisibility, and transaction costs/fees/taxes), should I proceed by assuming no minimums, continuous divisibility, and zero transaction costs, or would you prefer to wait for confirmation before I finalize the model?

## Turn 10 - User Simulator

Please proceed by assuming no minimums, continuous divisibility, and zero transaction costs.

## Turn 11 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total wealth at the end of Year 3, which includes all proceeds from matured investments plus any uninvested cash carried to the end of Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

1. **Product (1):** 1-year product, available at the beginning of each year (Years 1, 2, 3). Invest I at the start of a year → receive 1.20·I at that year's end. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Invest I at the start of Year 1 → receive 1.50·I at the end of Year 2. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Invest I at the start of Year 2 → receive 1.60·I at the end of Year 2. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Invest I at the start of Year 3 → receive 1.40·I at the end of Year 3. Capped at 100,000 yuan.

**Key rules confirmed:**
- No borrowing; total investment in any year ≤ available cash at the beginning of that year.
- Cash from maturing investments at the end of a year can be immediately reinvested at the beginning of the next year.
- It is permissible to hold cash idle (earning no return) at the beginning of any year.
- No minimum investment amounts; investments are continuous (any non-negative real amount).
- Zero transaction costs, fees, or taxes.
- All decision variables are continuous and non-negative.

**Model structure:**
- Decision variables: investment amounts in each product at each available time point, plus idle cash at each year's beginning.
- Constraints: cash-flow balance at the beginning of each year (available cash = initial capital + proceeds from prior-year maturities; allocated to investments + idle cash), upper bounds on products (2), (3), (4), non-negativity.
- Objective: maximize (proceeds from all products maturing at end of Year 3) + (idle cash at end of Year 3).