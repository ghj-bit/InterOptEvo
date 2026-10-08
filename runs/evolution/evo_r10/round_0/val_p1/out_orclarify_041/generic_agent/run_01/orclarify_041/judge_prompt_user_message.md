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

QUESTION: Is the 500,000 yuan initial capital the only source of funds, so that in each year the total invested (plus any amount left uninvested) cannot exceed the cash available at the start of that year?

## Turn 1 - User Simulator

Yes. The 500,000 yuan initial capital is the only source of funds. You cannot borrow money. In each year, the total amount invested (plus any cash left uninvested) cannot exceed the cash available at the start of that year, which consists of the initial capital and proceeds from investments that have already matured.

## Turn 2 - Generic Agent

QUESTION: If you invest in product (1) at the start of a year and it matures at that year's end, can the proceeds be immediately reinvested in product (4) at the start of Year 3 (i.e., do Year 2-end proceeds count as available at the start of Year 3)?

## Turn 2 - User Simulator

Yes. Proceeds from investments that mature at the end of Year 2 are available at the start of Year 3 and can be reinvested in product (4) or other products available at that time.

## Turn 3 - Generic Agent

QUESTION: At the end of Year 3, is the objective to maximize the total value of all holdings (including any cash left uninvested and any product (1) invested at the start of Year 3 that matures at Year 3's end), or only the cash actually received at Year 3's end?

## Turn 3 - User Simulator

The objective is to maximize the total value of all holdings at the end of Year 3, including any cash left uninvested and the proceeds from product (1) invested at the start of Year 3 that matures at Year 3's end.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum investment amount or divisibility requirement for the products, or can you invest any continuous (fractional) amount in each product?

## Turn 4 - User Simulator

There is no minimum investment amount or divisibility requirement. You can invest any continuous (fractional) amount in each product, subject to the stated caps and available cash.

## Turn 5 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Goal:** Maximize total value of all holdings at the end of Year 3 (cash left uninvested + proceeds from any product maturing at Year 3's end).

- **Funds:** The only source of funds is the 500,000 yuan initial capital at the start of Year 1. No borrowing. In each year, total invested plus cash left uninvested cannot exceed the cash available at the start of that year (initial capital plus proceeds from investments that have already matured).

- **Products:**
  1. **Product (1):** 1-year, available at the start of Years 1, 2, and 3. Invest I at start of year → receive 1.20·I at that year's end. Unlimited capacity.
  2. **Product (2):** 2-year, available only at the start of Year 1, matures at end of Year 2, pays 1.50·I. Cap: 120,000 yuan.
  3. **Product (3):** Same-year, available only at the start of Year 2, matures at end of Year 2, pays 1.60·I. Cap: 150,000 yuan.
  4. **Product (4):** 1-year, available only at the start of Year 3, matures at end of Year 3, pays 1.40·I. Cap: 100,000 yuan.

- **Cash flow timing:** Proceeds maturing at the end of a year are available at the start of the next year for reinvestment.

- **Variables:** Continuous (fractional) amounts allowed; no minimum investment; no divisibility constraints.

- **Caps:** Product (2) ≤ 120,000; Product (3) ≤ 150,000; Product (4) ≤ 100,000.