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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash held idle) counted toward the total principal plus interest you want to maximize?

## Turn 1 - User Simulator

Yes. The objective is to maximize your total wealth at the end of Year 3, which includes any cash that remains uninvested at that time.

## Turn 2 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year, is the amount you can invest in it in any given year limited only by the cash available at that time, with no separate per-year cap?

## Turn 2 - User Simulator

Yes, product (1) has unlimited capacity. The only limit is the cash available at the beginning of that year.

## Turn 3 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of a year, is the entire amount locked up for that full year, so it cannot be used for any other investment until it matures at that year's end?

## Turn 3 - User Simulator

Yes, the entire amount invested in product (1) is locked up for that full year and cannot be used for other investments until it matures at that year's end.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in a single year other than the cash available at the beginning of that year, or is it truly unlimited in each of Years 1, 2, and 3?

## Turn 4 - User Simulator

It is truly unlimited in each of Years 1, 2, and 3. The only limit is the cash available at the beginning of that year.

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) using the cash that matures from product (2) at the end of Year 2, or is product (2)'s return only available at the end of Year 2 (after Year 2 investments are made)?

## Turn 5 - User Simulator

Product (2)'s return is only available at the end of Year 2, after Year 2 investments are made. Therefore, you cannot use it to invest in product (1) at the beginning of Year 2.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that matures from product (2) at the end of Year 2?

## Turn 6 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (1) using the cash that matured from product (2) at the end of Year 2.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) using the cash that matures from product (1) invested at the beginning of Year 1 (i.e., the 1.20·I return received at the end of Year 1)?

## Turn 7 - User Simulator

Yes, at the beginning of Year 2, you can invest in product (1) using the cash that matured from product (1) invested at the beginning of Year 1.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that matures from product (1) invested at the beginning of Year 2 (i.e., the 1.20·I return received at the end of Year 2)?

## Turn 8 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (1) using the cash that matured from product (1) invested at the beginning of Year 2.

## Turn 9 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the four products, or can you invest any amount (including zero) in each?

## Turn 9 - User Simulator

There is no minimum investment amount. You can invest any amount, including zero, in each product.

## Turn 10 - Generic Agent

QUESTION: Are the investment amounts in each product required to be whole yuan amounts (integers), or can they be any fractional amount?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how much cash you can hold idle (uninvested) at the beginning of a year, or can you carry any amount of cash forward without restriction?

## Turn 11 - User Simulator

There is no limit on how much cash you can hold idle. You can carry any amount of cash forward without restriction.

## Turn 12 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (3) using the cash that matured from product (1) invested at the beginning of Year 1 (i.e., the 1.20·I return received at the end of Year 1)?

## Turn 12 - User Simulator

Yes, at the beginning of Year 2, you can invest in product (3) using the cash that matured from product (1) invested at the beginning of Year 1.

## Turn 13 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (4) using the cash that matured from product (2) at the end of Year 2?

## Turn 13 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (4) using the cash that matured from product (2) at the end of Year 2.

## Turn 14 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (4) using the cash that matured from product (1) invested at the beginning of Year 2 (i.e., the 1.20·I return received at the end of Year 2)?

## Turn 14 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (4) using the cash that matured from product (1) invested at the beginning of Year 2.

## Turn 15 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (4) using the cash that matured from product (3) at the end of Year 2?

## Turn 15 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (4) using the cash that matured from product (3) at the end of Year 2.

## Turn 16 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that matured from product (3) at the end of Year 2?

## Turn 16 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (1) using the cash that matured from product (3) at the end of Year 2.

## Turn 17 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that matured from product (4) at the end of Year 3?

## Turn 17 - User Simulator

No, product (4) matures at the end of Year 3, so its proceeds are not available at the beginning of Year 3 to invest in product (1).

## Turn 18 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) using the cash that matured from product (3) at the end of Year 2?

## Turn 18 - User Simulator

No, product (3) matures at the end of Year 2, so its proceeds are not available at the beginning of Year 2 to invest in product (1).

## Turn 19 - Generic Agent

QUESTION: At the beginning of Year 1, is the initial capital of 500,000 yuan the only source of funds available for investment, or are there other sources of cash at that time?

## Turn 19 - User Simulator

Yes, at the beginning of Year 1, the initial capital of 500,000 yuan is the only source of funds available for investment.

## Turn 20 - Generic Agent

QUESTION: At the beginning of Year 2, is the only source of funds available for investment the cash that matured from product (1) invested at the beginning of Year 1, or are there other sources of cash at that time?

## Turn 20 - User Simulator

No, there are other sources of cash. At the beginning of Year 2, the available funds include the cash that matured from product (1) invested at the beginning of Year 1, plus any cash that was held idle (uninvested) from the beginning of Year 1.

## Turn 21 - Generic Agent

QUESTION: At the beginning of Year 3, is the available cash the sum of: (a) cash matured from product (1) invested at the beginning of Year 2, (b) cash matured from product (2) at the end of Year 2, (c) cash matured from product (3) at the end of Year 2, and (d) any cash held idle from the beginning of Year 2?

## Turn 21 - User Simulator

Yes, at the beginning of Year 3, the available cash is the sum of: (a) cash matured from product (1) invested at the beginning of Year 2, (b) cash matured from product (2) at the end of Year 2, (c) cash matured from product (3) at the end of Year 2, and (d) any cash held idle from the beginning of Year 2.

## Turn 22 - Generic Agent

QUESTION: At the end of Year 3, is the total wealth the sum of: (a) cash matured from product (1) invested at the beginning of Year 3, (b) cash matured from product (4) at the end of Year 3, and (c) any cash held idle from the beginning of Year 3?

## Turn 22 - User Simulator

Yes, at the end of Year 3, the total wealth is the sum of: (a) cash matured from product (1) invested at the beginning of Year 3, (b) cash matured from product (4) at the end of Year 3, and (c) any cash held idle from the beginning of Year 3.

## Turn 23 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in product (1) and product (2) simultaneously using the initial 500,000 yuan, as long as the total does not exceed 500,000?

## Turn 23 - User Simulator

Yes, at the beginning of Year 1, you can invest in product (1) and product (2) simultaneously using the initial 500,000 yuan, as long as the total does not exceed 500,000.

## Turn 24 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) and product (3) simultaneously using the available cash, as long as the total does not exceed the available cash?

## Turn 24 - User Simulator

Yes, at the beginning of Year 2, you can invest in product (1) and product (3) simultaneously using the available cash, as long as the total does not exceed the available cash.

## Turn 25 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) and product (4) simultaneously using the available cash, as long as the total does not exceed the available cash?

## Turn 25 - User Simulator

Yes, at the beginning of Year 3, you can invest in product (1) and product (4) simultaneously using the available cash, as long as the total does not exceed the available cash.

## Turn 26 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax associated with investing in any of the four products?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) at the beginning of Year 1, other than the initial 500,000 yuan?

## Turn 27 - User Simulator

No, there is no limit on how much you can invest in product (1) at the beginning of Year 1, other than the initial 500,000 yuan.

## Turn 28 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) at the beginning of Year 2, other than the available cash at that time?

## Turn 28 - User Simulator

No, there is no limit on how much you can invest in product (1) at the beginning of Year 2, other than the available cash at that time.

## Turn 29 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) at the beginning of Year 3, other than the available cash at that time?

## Turn 29 - User Simulator

No, there is no limit on how much you can invest in product (1) at the beginning of Year 3, other than the available cash at that time.

## Turn 30 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (2) at the beginning of Year 1, other than the 120,000 yuan cap and the initial 500,000 yuan?

## Turn 30 - User Simulator

No, there is no limit on how much you can invest in product (2) at the beginning of Year 1, other than the 120,000 yuan cap and the initial 500,000 yuan.