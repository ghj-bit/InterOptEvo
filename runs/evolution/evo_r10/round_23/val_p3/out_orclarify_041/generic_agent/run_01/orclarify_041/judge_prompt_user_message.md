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

QUESTION: At the end of Year 3, do you want the objective to include only the cash from investments that mature at the end of Year 3, or should it also include any cash left uninvested (idle cash) at the end of Year 3?

## Turn 1 - User Simulator

The objective should include all cash available at the end of Year 3, which means it should include both the proceeds from investments that mature at the end of Year 3 and any cash left uninvested (idle cash) at that time.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is the 1.20·I payout at year-end the total amount returned (i.e., principal plus 20% interest), or is it just the interest earned on top of the principal?

## Turn 2 - User Simulator

The 1.20·I payout is the total amount returned, meaning it includes the principal plus 20% interest.

## Turn 3 - Generic Agent

QUESTION: For products (2), (3), and (4), are the payouts 1.50·I, 1.60·I, and 1.40·I also the total amount returned (principal plus interest), consistent with product (1)?

## Turn 3 - User Simulator

Yes, the payouts 1.50·I, 1.60·I, and 1.40·I are also the total amount returned, consistent with product (1).

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how much can be invested in product (1) in a given year, or is it truly unlimited as stated?

## Turn 4 - User Simulator

Product (1) is truly unlimited; there is no cap on how much can be invested in it in a given year.

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) using the cash that becomes available from product (2) maturing at the end of Year 2?

## Turn 5 - User Simulator

No. Product (2) matures at the end of Year 2, so its proceeds are not available at the beginning of Year 2. At the beginning of Year 2, you can only invest cash that is already available from your initial capital and any investments that have already matured by that point.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that becomes available from product (2) maturing at the end of Year 2?

## Turn 6 - User Simulator

Yes. Product (2) matures at the end of Year 2, so its proceeds are available at the beginning of Year 3 and can be used to invest in product (1) at that time.

## Turn 7 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) using the cash that becomes available from product (3) maturing at the end of Year 2?

## Turn 7 - User Simulator

No. Product (3) matures at the end of Year 2, so its proceeds are not available at the beginning of Year 2. At the beginning of Year 2, you can only invest cash that is already available from your initial capital and any investments that have already matured by that point.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that becomes available from product (3) maturing at the end of Year 2?

## Turn 8 - User Simulator

Yes. Product (3) matures at the end of Year 2, so its proceeds are available at the beginning of Year 3 and can be used to invest in product (1) at that time.

## Turn 9 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (4) using the cash that becomes available from product (2) maturing at the end of Year 2?

## Turn 9 - User Simulator

Yes. Product (2) matures at the end of Year 2, so its proceeds are available at the beginning of Year 3 and can be used to invest in product (4) at that time.

## Turn 10 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (4) using the cash that becomes available from product (3) maturing at the end of Year 2?

## Turn 10 - User Simulator

Yes. Product (3) matures at the end of Year 2, so its proceeds are available at the beginning of Year 3 and can be used to invest in product (4) at that time.

## Turn 11 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in product (1) using the initial capital of 500,000 yuan?

## Turn 11 - User Simulator

Yes. At the beginning of Year 1, you can invest in product (1) using the initial capital of 500,000 yuan.

## Turn 12 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in product (2) using the initial capital of 500,000 yuan?

## Turn 12 - User Simulator

Yes. At the beginning of Year 1, you can invest in product (2) using the initial capital of 500,000 yuan, subject to the 120,000 yuan cap on that product.

## Turn 13 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) using the cash that becomes available from product (1) maturing at the end of Year 1?

## Turn 13 - User Simulator

Yes. Product (1) invested at the beginning of Year 1 matures at the end of Year 1, so its proceeds are available at the beginning of Year 2 and can be used to invest in product (1) at that time.

## Turn 14 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (3) using the cash that becomes available from product (1) maturing at the end of Year 1?

## Turn 14 - User Simulator

Yes. Product (1) invested at the beginning of Year 1 matures at the end of Year 1, so its proceeds are available at the beginning of Year 2 and can be used to invest in product (3) at that time.

## Turn 15 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) using the cash that becomes available from product (1) maturing at the end of Year 2?

## Turn 15 - User Simulator

Yes. Product (1) invested at the beginning of Year 2 matures at the end of Year 2, so its proceeds are available at the beginning of Year 3 and can be used to invest in product (1) at that time.

## Turn 16 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (4) using the cash that becomes available from product (1) maturing at the end of Year 2?

## Turn 16 - User Simulator

Yes. Product (1) invested at the beginning of Year 2 matures at the end of Year 2, so its proceeds are available at the beginning of Year 3 and can be used to invest in product (4) at that time.

## Turn 17 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any amount (including zero) in each product?

## Turn 17 - User Simulator

There is no minimum investment amount required. You can invest any amount, including zero, in each product.

## Turn 18 - Generic Agent

QUESTION: Are the investment amounts for each product required to be whole numbers (integer yuan), or can they be any non-negative real number?

## Turn 18 - User Simulator

The investment amounts can be any non-negative real number; they do not need to be whole numbers.

## Turn 19 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested across all products in a given year, or is the only constraint the cash available at that time?

## Turn 19 - User Simulator

There is no separate limit on the total amount that can be invested across all products in a given year. The only constraint is the cash available at that time, which comes from the initial capital and proceeds from investments that have already matured.

## Turn 20 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in both product (1) and product (2) simultaneously, as long as the total does not exceed the initial capital of 500,000 yuan?

## Turn 20 - User Simulator

Yes. At the beginning of Year 1, you can invest in both product (1) and product (2) simultaneously, as long as the total investment does not exceed the initial capital of 500,000 yuan and the investment in product (2) does not exceed its 120,000 yuan cap.

## Turn 21 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in both product (1) and product (3) simultaneously, as long as the total does not exceed the cash available at that time?

## Turn 21 - User Simulator

Yes. At the beginning of Year 2, you can invest in both product (1) and product (3) simultaneously, as long as the total investment does not exceed the cash available at that time and the investment in product (3) does not exceed its 150,000 yuan cap.

## Turn 22 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in both product (1) and product (4) simultaneously, as long as the total does not exceed the cash available at that time?

## Turn 22 - User Simulator

Yes. At the beginning of Year 3, you can invest in both product (1) and product (4) simultaneously, as long as the total investment does not exceed the cash available at that time and the investment in product (4) does not exceed its 100,000 yuan cap.

## Turn 23 - Generic Agent

QUESTION: Is there any requirement that all available cash must be invested at the beginning of each year, or is it allowed to leave some cash uninvested (idle) at the beginning of a year?

## Turn 23 - User Simulator

It is allowed to leave some cash uninvested (idle) at the beginning of a year. There is no requirement that all available cash must be invested.

## Turn 24 - Generic Agent

QUESTION: If cash is left uninvested (idle) at the beginning of a year, does it earn any interest or return, or does it simply carry over to the next period with no gain?

## Turn 24 - User Simulator

Idle cash does not earn any interest or return. It simply carries over to the next period with no gain.

## Turn 25 - Generic Agent

QUESTION: At the end of Year 3, does the idle cash that was carried over from previous years count toward the objective, or only the idle cash remaining at the very end of Year 3?

## Turn 25 - User Simulator

Only the idle cash remaining at the very end of Year 3 counts toward the objective.

## Turn 26 - Generic Agent

QUESTION: Is there any requirement that the investment in product (2) must be made at the beginning of Year 1, or could it be made at any other time?

## Turn 26 - User Simulator

Product (2) is available only at the beginning of Year 1. It cannot be invested in at any other time.

## Turn 27 - Generic Agent

QUESTION: Is there any requirement that the investment in product (3) must be made at the beginning of Year 2, or could it be made at any other time?

## Turn 27 - User Simulator

Product (3) is available only at the beginning of Year 2. It cannot be invested in at any other time.

## Turn 28 - Generic Agent

QUESTION: Is there any requirement that the investment in product (4) must be made at the beginning of Year 3, or could it be made at any other time?

## Turn 28 - User Simulator

Product (4) is available only at the beginning of Year 3. It cannot be invested in at any other time.

## Turn 29 - Generic Agent

QUESTION: Is there any requirement that the investment in product (1) must be made at the beginning of a year, or could it be made at any time during the year?

## Turn 29 - User Simulator

Product (1) is available only at the beginning of each year (Years 1–3). It cannot be invested in at any other time during the year.

## Turn 30 - Generic Agent

QUESTION: Is there any requirement that the proceeds from investments maturing at the end of a year must be reinvested at the beginning of the next year, or can they be held as idle cash?

## Turn 30 - User Simulator

There is no requirement that proceeds from investments maturing at the end of a year must be reinvested at the beginning of the next year. They can be held as idle cash.