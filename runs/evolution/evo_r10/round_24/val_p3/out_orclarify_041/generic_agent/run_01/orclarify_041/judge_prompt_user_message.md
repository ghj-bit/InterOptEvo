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

QUESTION: At the end of Year 3, can you still hold the 2-year product (2) that was invested at the beginning of Year 1 (which matures at the end of Year 2 and pays 1.50·I), or is the objective strictly the cash you have on hand at the end of Year 3 from investments that mature by then?

## Turn 1 - User Simulator

The objective is strictly the cash you have on hand at the end of Year 3. Product (2) matures at the end of Year 2, so its proceeds are received in Year 2 and are not held into Year 3.

## Turn 2 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of Year 2 or Year 3, does the 1.20·I return come back at the end of that same year (so Year 2 money can be reinvested in Year 3, but Year 3 money only counts at Year 3 end), or is there any other timing for when product (1) pays out?

## Turn 2 - User Simulator

The 1.20·I return comes back at the end of that same year. So, money invested in product (1) at the beginning of Year 2 is available at the end of Year 2 to be reinvested in Year 3, and money invested at the beginning of Year 3 is available at the end of Year 3.

## Turn 3 - Generic Agent

QUESTION: At the beginning of Year 3, can you invest in product (1) (the 1-year product available at the beginning of each year) in addition to product (4), or is product (4) the only option available at the beginning of Year 3?

## Turn 3 - User Simulator

Yes, at the beginning of Year 3, you can invest in both product (1) and product (4).

## Turn 4 - Generic Agent

QUESTION: At the beginning of Year 2, can you invest in product (1) (the 1-year product available at the beginning of each year) in addition to product (3), or is product (3) the only option available at the beginning of Year 2?

## Turn 4 - User Simulator

Yes, at the beginning of Year 2, you can invest in both product (1) and product (3).

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 1, can you invest in product (1) (the 1-year product available at the beginning of each year) in addition to product (2), or is product (2) the only option available at the beginning of Year 1?

## Turn 5 - User Simulator

Yes, at the beginning of Year 1, you can invest in both product (1) and product (2).

## Turn 6 - Generic Agent

QUESTION: Do you need to invest all available cash at the beginning of each year, or can you leave some cash idle (uninvested) that simply carries over to the next year?

## Turn 6 - User Simulator

You can leave some cash idle. You are not required to invest all available cash at the beginning of each year.

## Turn 7 - Generic Agent

QUESTION: If you leave cash idle at the beginning of a year, does it carry over to the next year with no interest (i.e., the same amount is available at the beginning of the next year), or does idle cash earn any return?

## Turn 7 - User Simulator

Idle cash carries over to the next year with no interest.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on the total amount you can invest in product (1) across all three years, or is it truly unlimited as stated?

## Turn 8 - User Simulator

Product (1) is truly unlimited. There is no limit on the total amount you can invest in it across all three years.

## Turn 9 - Generic Agent

QUESTION: Are the caps on products (2), (3), and (4) limits on the total amount invested in each product over its entire availability period, or are they per-year limits (which would matter if a product were available in multiple years)?

## Turn 9 - User Simulator

The caps are limits on the total amount invested in each product over its entire availability period. Since products (2), (3), and (4) are each available in only one year, the cap applies to the single investment made in that year.

## Turn 10 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can you invest any amount down to zero?

## Turn 10 - User Simulator

There is no minimum investment amount. You can invest any amount down to zero.

## Turn 11 - Generic Agent

QUESTION: Are the investment amounts continuous (you can invest any fractional amount of yuan), or must they be in whole yuan increments?

## Turn 11 - User Simulator

The investment amounts are continuous. You can invest any fractional amount of yuan.

## Turn 12 - Generic Agent

QUESTION: Is there any constraint that the total invested at the beginning of each year cannot exceed the cash available at that time (i.e., you cannot invest more than you have), or is there some form of borrowing allowed?

## Turn 12 - User Simulator

No borrowing is allowed. The total invested at the beginning of each year cannot exceed the cash available at that time.

## Turn 13 - Generic Agent

QUESTION: At the end of Year 3, does the objective include only the cash from investments that mature at the end of Year 3, or does it also include any idle cash that was carried over and not invested?

## Turn 13 - User Simulator

The objective includes all cash on hand at the end of Year 3, which includes both the proceeds from investments that mature at the end of Year 3 and any idle cash that was carried over and not invested.

## Turn 14 - Generic Agent

QUESTION: At the beginning of Year 1, is the full 500,000 yuan available for investment, or is any portion of it reserved or restricted for other purposes?

## Turn 14 - User Simulator

The full 500,000 yuan is available for investment at the beginning of Year 1.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or considerations I haven't asked about, such as taxes, fees, or liquidity requirements that would affect the investment plan?

## Turn 15 - User Simulator

No, there are no other constraints or considerations such as taxes, fees, or liquidity requirements.

## Turn 16 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash on hand at the end of Year 3 (proceeds from investments maturing at Year 3 end + any idle cash carried over).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Products and timing:**

| Product | Available | Matures | Return | Cap |
|---------|-----------|---------|--------|-----|
| (1) | Beginning of Years 1, 2, 3 | End of same year | 1.20·I | Unlimited |
| (2) | Beginning of Year 1 only | End of Year 2 | 1.50·I | 120,000 |
| (3) | Beginning of Year 2 only | End of Year 2 | 1.60·I | 150,000 |
| (4) | Beginning of Year 3 only | End of Year 3 | 1.40·I | 100,000 |

**Key rules confirmed:**
- At the beginning of each year, you may invest in product (1) plus any product available that year.
- Product (1) returns 1.20·I at the end of the same year, so Year 2 proceeds are available for Year 3 investment.
- Idle cash carries over to the next year with no interest.
- No borrowing: total invested at the beginning of each year ≤ cash available at that time.
- Caps are on total investment per product (each product is available in only one year, so the cap applies to that single investment).
- No minimum investment; amounts are continuous (any fractional yuan).
- No taxes, fees, or other constraints.
- The objective is strictly cash on hand at the end of Year 3 (product (2) proceeds are received at Year 2 end and can be reinvested in Year 3, but are not "held" into Year 3).