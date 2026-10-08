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

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., the sum of all matured proceeds from products 1, 2, 3, and 4 that have paid out by then), or should any capital that was never invested (left idle) also count toward that total?

## Turn 1 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3. This includes all matured proceeds from the investment products as well as any capital that was never invested and remains idle.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), which is available at the beginning of each year, is the 1.20·I return paid at the end of that same year (so Year-1 money matures at end of Year 1, Year-2 money at end of Year 2, Year-3 money at end of Year 3), or is there a different timing?

## Turn 2 - User Simulator

The 1.20·I return is paid at the end of that same year. Year-1 money matures at the end of Year 1, Year-2 money at the end of Year 2, and Year-3 money at the end of Year 3.

## Turn 3 - Generic Agent

QUESTION: Can proceeds that mature at the end of a year be reinvested into products available at the beginning of the following year (for example, money from product 1 maturing at end of Year 1 invested into product 4 at the start of Year 3, or product 2 proceeds at end of Year 2 into product 1 at the start of Year 3)?

## Turn 3 - User Simulator

Yes, proceeds that mature at the end of a year can be reinvested into products available at the beginning of the following year.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum investment amounts or fixed fees for any of the four products, or can you invest any non-negative amount (including zero) in each?

## Turn 4 - User Simulator

There are no minimum investment amounts or fixed fees. You can invest any non-negative amount, including zero, in each product, subject to the stated maximum caps for products (2), (3), and (4).

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in a given year, or is it truly unlimited in each of Years 1, 2, and 3?

## Turn 5 - User Simulator

Product (1) is truly unlimited in each of Years 1, 2, and 3.

## Turn 6 - Generic Agent

QUESTION: Is there any constraint that all available cash at the beginning of a year must be invested (i.e., no cash can be held idle across a year boundary), or can you choose to leave some cash uninvested and carry it forward to a later year?

## Turn 6 - User Simulator

You can choose to leave some cash uninvested and carry it forward to a later year. There is no requirement to invest all available cash at the beginning of a year.

## Turn 7 - Generic Agent

QUESTION: Is there any interest or return earned on cash that is left idle and carried forward from one year to the next, or does idle cash simply carry over at face value (1.00·I)?

## Turn 7 - User Simulator

Idle cash simply carries over at face value (1.00·I). There is no interest or return earned on cash that is left idle.

## Turn 8 - Generic Agent

QUESTION: Is there any constraint that the total amount invested at the beginning of a year cannot exceed the cash available at that time (i.e., no borrowing or external funding allowed)?

## Turn 8 - User Simulator

Yes, there is no borrowing or external funding allowed. The total amount invested at the beginning of a year cannot exceed the cash available at that time, which consists of the initial capital and proceeds from investments that have already matured.

## Turn 9 - Generic Agent

QUESTION: Are there any other constraints or requirements I should know about that haven't been covered yet, such as taxes, transaction costs, or a requirement to have a minimum amount of cash on hand at the end of Year 3?

## Turn 9 - User Simulator

No, there are no other constraints or requirements. There are no taxes, transaction costs, or minimum cash-on-hand requirements at the end of Year 3.

## Turn 10 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of Year 3, which includes all matured investment proceeds plus any idle cash carried forward.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Invest I at the start of a year, receive 1.20·I at the end of that same year. Unlimited capacity.

2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, pays 1.50·I. Capped at 120,000 yuan.

3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, pays 1.60·I. Capped at 150,000 yuan.

4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, pays 1.40·I. Capped at 100,000 yuan.

**Key rules:**
- Proceeds maturing at the end of a year can be reinvested at the beginning of the following year.
- Idle cash carries forward at face value (1.00·I), no interest.
- No borrowing or external funding; investments in a year cannot exceed available cash at that time.
- No minimum investment amounts, no fixed fees, no taxes, no transaction costs.
- No minimum cash-on-hand requirement at the end of Year 3.
- All investment variables are continuous and non-negative.