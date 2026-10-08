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

QUESTION: At the end of Year 3, do you want the objective to include only the proceeds from investments that mature by the end of Year 3 (i.e., cash on hand), or should any capital left uninvested at the end of Year 3 also be counted at face value in the total?

## Turn 1 - User Simulator

Yes, any capital left uninvested at the end of Year 3 should be counted at face value in the total. The objective is to maximize total wealth at the end of Year 3, which includes both the proceeds from matured investments and any cash remaining uninvested.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20·I payout at year-end the total amount received (i.e., principal plus 20% interest), or is it just the interest earned on top of the principal?

## Turn 2 - User Simulator

The 1.20·I payout is the total amount received, meaning it includes the principal plus 20% interest.

## Turn 3 - Generic Agent

QUESTION: For products (2), (3), and (4), are the payouts 1.50·I, 1.60·I, and 1.40·I also total amounts received (principal plus interest), consistent with product (1)?

## Turn 3 - User Simulator

Yes, the payouts 1.50·I, 1.60·I, and 1.40·I are also total amounts received, consistent with product (1).

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how much can be invested in product (1) in a given year, or is it truly unlimited as stated?

## Turn 4 - User Simulator

Product (1) is truly unlimited; there is no cap on how much can be invested in it in a given year.

## Turn 5 - Generic Agent

QUESTION: Can you invest in product (1) at the beginning of Year 3, and if so, does it mature at the end of Year 3 (i.e., is it available in Years 1, 2, and 3 as stated)?

## Turn 5 - User Simulator

Yes, product (1) is available at the beginning of Year 3 and matures at the end of Year 3. It is available at the beginning of Years 1, 2, and 3 as stated.

## Turn 6 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any amount (including zero) in each?

## Turn 6 - User Simulator

There is no minimum investment amount required. You can invest any amount, including zero, in each product.

## Turn 7 - Generic Agent

QUESTION: Are the investment amounts required to be whole numbers (e.g., whole yuan), or can they be any continuous (fractional) amount?

## Turn 7 - User Simulator

The investment amounts can be any continuous (fractional) amount; they do not need to be whole numbers.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint that all available cash at the beginning of each year must be fully invested, or is it allowed to hold cash (uninvested) at the beginning of a year and carry it forward?

## Turn 8 - User Simulator

It is allowed to hold cash (uninvested) at the beginning of a year and carry it forward. There is no requirement to fully invest all available cash.

## Turn 9 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax associated with investing in or redeeming any of the products, or are all transactions cost-free?

## Turn 9 - User Simulator

All transactions are cost-free; there are no transaction costs, fees, or taxes associated with investing in or redeeming any of the products.

## Turn 10 - Generic Agent

QUESTION: Is there any constraint on the total amount that can be invested across all products in a single year, or is the only limit the cash available at the beginning of that year?

## Turn 10 - User Simulator

The only limit is the cash available at the beginning of that year. There is no separate constraint on the total amount that can be invested across all products in a single year.

## Turn 11 - Generic Agent

QUESTION: Can the proceeds from an investment that matures at the end of a year be immediately reinvested in products available at the beginning of the next year, or is there any delay or restriction on reinvesting matured proceeds?

## Turn 11 - User Simulator

The proceeds from an investment that matures at the end of a year can be immediately reinvested in products available at the beginning of the next year. There is no delay or restriction on reinvesting matured proceeds.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

- **Objective:** Maximize total wealth at the end of Year 3, which includes proceeds from all matured investments plus any uninvested cash held at that time.

- **Initial capital:** 500,000 yuan at the beginning of Year 1.

- **Products:**
  1. **Product (1):** 1-year, available at the beginning of Years 1, 2, and 3. Pays 1.20·I (total, including principal) at year-end. Unlimited capacity.
  2. **Product (2):** 2-year, available only at the beginning of Year 1, matures at end of Year 2. Pays 1.50·I (total). Capped at 120,000 yuan.
  3. **Product (3):** Same-year, available only at the beginning of Year 2, matures at end of Year 2. Pays 1.60·I (total). Capped at 150,000 yuan.
  4. **Product (4):** 1-year, available only at the beginning of Year 3, matures at end of Year 3. Pays 1.40·I (total). Capped at 100,000 yuan.

- **Key rules:**
  - All payouts are total amounts (principal + interest).
  - No minimum investment; any continuous (fractional) amount is allowed, including zero.
  - No transaction costs, fees, or taxes.
  - Cash can be held uninvested and carried forward; no requirement to fully invest.
  - The only per-year investment limit is the cash available at the beginning of that year.
  - Matured proceeds can be immediately reinvested at the beginning of the next year.
  - No separate aggregate cap beyond available cash.

- **Decision variables (continuous, non-negative):**
  - I1_1, I1_2, I1_3: amounts invested in Product (1) at the beginning of Years 1, 2, 3.
  - I2: amount invested in Product (2) at the beginning of Year 1.
  - I3: amount invested in Product (3) at the beginning of Year 2.
  - I4: amount invested in Product (4) at the beginning of Year 3.
  - Cash holdings at each decision point (beginning of Years 1, 2, 3 and end of Year 3).

- **Constraints:**
  - Cash flow balance at each year boundary (cash in = cash out + carried cash).
  - I2 ≤ 120,000; I3 ≤ 150,000; I4 ≤ 100,000.
  - All variables ≥ 0.

- **Objective:** Maximize (proceeds from I1_3 + I4 + any uninvested cash at end of Year 3).