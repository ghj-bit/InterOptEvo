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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash left idle) counted in the final "total principal plus interest" objective, or must all funds be invested in products that mature by the end of Year 3?

## Turn 1 - User Simulator

Yes, any cash left idle at the end of Year 3 is counted in the final "total principal plus interest" objective. The goal is to maximize your total wealth at the end of Year 3, which includes both the proceeds from matured investments and any uninvested cash.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20·I payout at year-end the total amount returned (principal plus interest), meaning the net interest earned is 0.20·I?

## Turn 2 - User Simulator

Yes, the 1.20·I payout is the total amount returned, meaning the net interest earned is 0.20·I.

## Turn 3 - Generic Agent

QUESTION: For products (2), (3), and (4), are the payouts 1.50·I, 1.60·I, and 1.40·I also total amounts returned (principal plus interest), so the net interest is 0.50·I, 0.60·I, and 0.40·I respectively?

## Turn 3 - User Simulator

Yes, the payouts 1.50·I, 1.60·I, and 1.40·I are total amounts returned, so the net interest is 0.50·I, 0.60·I, and 0.40·I respectively.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any non-negative amount (including zero) in each?

## Turn 4 - User Simulator

There is no minimum investment amount required. You can invest any non-negative amount, including zero, in each product.

## Turn 5 - Generic Agent

QUESTION: Are the investments in these products continuous (you can invest any fractional yuan amount), or must investments be in whole yuan amounts?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of a year, does the 1.20·I payout arrive at the end of that same year and become available for reinvestment at the beginning of the next year?

## Turn 6 - User Simulator

Yes, the 1.20·I payout arrives at the end of that same year and becomes available for reinvestment at the beginning of the next year.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on the total amount you can invest in product (1) across all three years, or is it truly unlimited as stated?

## Turn 7 - User Simulator

It is truly unlimited as stated.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in both product (1) and product (3) simultaneously, using the funds available at that time?

## Turn 8 - User Simulator

Yes, at the beginning of Year 2, you can invest in both product (1) and product (3) simultaneously, using the funds available at that time.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in both product (1) and product (4) simultaneously, using the funds available at that time?

## Turn 9 - User Simulator

Yes, at the beginning of Year 3, you can invest in both product (1) and product (4) simultaneously, using the funds available at that time.

## Turn 10 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax associated with investing in or redeeming any of these products?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there any constraint that requires you to invest all available funds at the beginning of each year, or can you choose to hold some cash and not invest it?

## Turn 11 - User Simulator

You can choose to hold some cash and not invest it. There is no constraint requiring you to invest all available funds at the beginning of each year.

## Turn 12 - Generic Agent

QUESTION: Does the 2-year product (2) lock up your funds for the full two years, meaning you cannot access or withdraw any portion of it before the end of Year 2?

## Turn 12 - User Simulator

Yes, the 2-year product (2) locks up your funds for the full two years, meaning you cannot access or withdraw any portion of it before the end of Year 2.

## Turn 13 - Generic Agent

QUESTION: Is there any constraint on the total amount you can invest across all products in a single year, or is the only limit the individual product caps?

## Turn 13 - User Simulator

The only limits are the individual product caps and the available cash at the beginning of each year. There is no separate constraint on the total amount invested across all products in a single year beyond those.

## Turn 14 - Generic Agent

QUESTION: Is there any requirement that the initial 500,000 yuan must be fully allocated at the beginning of Year 1, or can some of it be held as cash and invested in later years?

## Turn 14 - User Simulator

You can hold some of the initial 500,000 yuan as cash and invest it in later years. There is no requirement that it must be fully allocated at the beginning of Year 1.

## Turn 15 - Generic Agent

QUESTION: Is there any interest earned on cash that is held idle (not invested) during the years, or does idle cash simply remain at face value until it is invested?

## Turn 15 - User Simulator

The point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: Is this a linear programming problem where you can invest fractional amounts, or is there any integrality requirement (e.g., investments must be in whole units)?

## Turn 16 - User Simulator

The point still needs internal confirmation.

## Turn 17 - Generic Agent

QUESTION: At the end of Year 2, when product (2) matures and pays 1.50·I, does that payout become available for investment at the beginning of Year 3?

## Turn 17 - User Simulator

Yes, the payout from product (2) at the end of Year 2 becomes available for investment at the beginning of Year 3.

## Turn 18 - Generic Agent

QUESTION: At the end of Year 1, when product (1) matures and pays 1.20·I, does that payout become available for investment at the beginning of Year 2?

## Turn 18 - User Simulator

Yes, the payout from product (1) at the end of Year 1 becomes available for investment at the beginning of Year 2.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint that the total wealth (cash plus investments) must never go negative at any point during the three years?

## Turn 19 - User Simulator

Yes, you cannot borrow money. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 20 - Generic Agent

QUESTION: Is there any constraint on how much cash you can hold at the end of Year 3, or is there a maximum amount of idle cash allowed?

## Turn 20 - User Simulator

There is no constraint on how much cash you can hold at the end of Year 3.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) across all three years combined must not exceed some limit, or is it truly unlimited in total?

## Turn 21 - User Simulator

It is truly unlimited in total.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that you must invest in at least one product each year, or can you choose to invest in none of the available products in a given year?

## Turn 22 - User Simulator

You can choose to invest in none of the available products in a given year.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the total wealth at the end of Year 3 must be at least some minimum amount, or is the objective purely to maximize with no lower bound?

## Turn 23 - User Simulator

The objective is purely to maximize total wealth at the end of Year 3, with no lower bound.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the investments in products (2), (3), and (4) must be made in whole yuan amounts, or can they be fractional?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) in a single year must not exceed the cash available at the beginning of that year, or is the only constraint that total investments in a year cannot exceed available cash?

## Turn 25 - User Simulator

The only constraint is that total investments in a year cannot exceed the cash available at the beginning of that year.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the total wealth at the end of Year 3 must be at least the initial 500,000 yuan, or can it theoretically be less?

## Turn 26 - User Simulator

The objective is purely to maximize total wealth at the end of Year 3, with no lower bound.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) at the beginning of Year 1, product (2) at the beginning of Year 1, and any cash held must sum to exactly 500,000 yuan, or can the sum be less than 500,000 yuan?

## Turn 27 - User Simulator

The sum can be less than 500,000 yuan. You are not required to invest all available funds at the beginning of Year 1.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) at the beginning of Year 2, product (3) at the beginning of Year 2, and any cash held must sum to exactly the cash available at the beginning of Year 2, or can the sum be less?

## Turn 28 - User Simulator

The sum can be less than the cash available at the beginning of Year 2.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the total amount invested in product (1) at the beginning of Year 3, product (4) at the beginning of Year 3, and any cash held must sum to exactly the cash available at the beginning of Year 3, or can the sum be less

## Turn 29 - User Simulator

The sum can be less than the cash available at the beginning of Year 3.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the total wealth at the end of Year 3 must be at least the initial

## Turn 30 - User Simulator

The objective is purely to maximize total wealth at the end of Year 3, with no lower bound.