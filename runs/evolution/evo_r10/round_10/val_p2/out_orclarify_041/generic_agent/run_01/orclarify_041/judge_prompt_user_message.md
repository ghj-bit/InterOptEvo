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

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash left idle) counted in the final "total principal plus interest" objective, or is only the proceeds from investments that mature at the end of Year 3 counted?

## Turn 1 - User Simulator

Only the proceeds from investments that mature at the end of Year 3 are counted. Any cash left idle at the end of Year 3 is not included in the final total.

## Turn 2 - Generic Agent

QUESTION: Product (1) is a 1-year product available at the beginning of each year. If you invest in it at the beginning of Year 1, it matures at the end of Year 1 and the proceeds are available to invest again at the beginning of Year 2 — is that the intended reinvestment flow, or does money invested in product (1) in Year 1 simply disappear from the portfolio after Year 1?

## Turn 2 - User Simulator

That is the intended reinvestment flow. The proceeds from product (1) maturing at the end of Year 1 are available to invest at the beginning of Year 2.

## Turn 3 - Generic Agent

QUESTION: At the beginning of Year 2, the money available to invest (initial capital minus what was put into product (2), plus proceeds from product (1) maturing at end of Year 1) must be split between product (1) and product (3) — is there any limit on how much can be invested in product (1) in Year 2, or is it unlimited like in Year 1?

## Turn 3 - User Simulator

Product (1) is unlimited in Year 2, just as it is in Year 1.

## Turn 4 - Generic Agent

QUESTION: At the beginning of Year 3, the money available to invest (proceeds from product (1) maturing at end of Year 2, plus proceeds from product (2) and product (3) maturing at end of Year 2) must be split between product (1) and product (4) — is there any limit on how much can be invested in product (1) in Year 3, or is it unlimited like in Years 1 and 2?

## Turn 4 - User Simulator

Product (1) is unlimited in Year 3, just as it is in Years 1 and 2.

## Turn 5 - Generic Agent

QUESTION: At the beginning of Year 1, the 500,000 yuan must be split between product (1) and product (2) — is there any requirement that all 500,000 yuan must be invested at the beginning of Year 1, or can some of it be held as idle cash and invested in a later year?

## Turn 5 - User Simulator

There is no requirement that all 500,000 yuan must be invested at the beginning of Year 1. Some of it can be held as idle cash and invested in a later year.

## Turn 6 - Generic Agent

QUESTION: If cash is held idle at the beginning of Year 1 and not invested, does it earn any interest while idle, or does it simply carry over at face value (1.00×) to the beginning of Year 2?

## Turn 6 - User Simulator

It simply carries over at face value (1.00×) to the beginning of Year 2.

## Turn 7 - Generic Agent

QUESTION: If cash is held idle at the beginning of Year 2 (i.e., not invested in product (1) or product (3)), does it also carry over at face value (1.00×) to the beginning of Year 3?

## Turn 7 - User Simulator

Yes, it carries over at face value (1.00×) to the beginning of Year 3.

## Turn 8 - Generic Agent

QUESTION: At the beginning of Year 3, the available cash (proceeds from product (1) maturing at end of Year 2, plus proceeds from product (2) and product (3) maturing at end of Year 2, plus any idle cash carried over) must be split between product (1) and product (4) — is there any requirement that all available cash at the beginning of Year 3 must be invested, or can some of it be held idle and simply not counted in the final objective?

## Turn 8 - User Simulator

There is no requirement that all available cash at the beginning of Year 3 must be invested. Some of it can be held idle, and as previously confirmed, any cash left idle at the end of Year 3 is not counted in the final objective.

## Turn 9 - Generic Agent

QUESTION: Are all investment amounts (in products 1, 2, 3, and 4) required to be non-negative, and can they take any continuous value (e.g., 12,345.67 yuan), or must they be whole yuan amounts?

## Turn 9 - User Simulator

All investment amounts must be non-negative. They can take any continuous value; they do not need to be whole yuan amounts.

## Turn 10 - Generic Agent

QUESTION: The caps on products (2), (3), and (4) — are these limits on the total amount invested in each product over its entire availability window, or are they per-period limits (e.g., at most 120,000 in product (2) at the beginning of Year 1, at most 150,000 in product (3) at the beginning of Year 2, at most 100,000 in product (4) at the beginning of Year 3)?

## Turn 10 - User Simulator

They are per-period limits: at most 120,000 yuan in product (2) at the beginning of Year 1, at most 150,000 yuan in product (3) at the beginning of Year 2, and at most 100,000 yuan in product (4) at the beginning of Year 3.

## Turn 11 - Generic Agent

QUESTION: Product (2) is a 2-year product available only at the beginning of Year 1, maturing at the end of Year 2. Is there any intermediate cash flow from product (2) at the end of Year 1, or does the entire investment remain locked until it matures at the end of Year 2?

## Turn 11 - User Simulator

The entire investment remains locked until it matures at the end of Year 2. There is no intermediate cash flow at the end of Year 1.

## Turn 12 - Generic Agent

QUESTION: Product (3) is described as a "same-year product" available at the beginning of Year 2, maturing at the end of Year 2. Does this mean it is a 1-year product (invest at beginning of Year 2, receive proceeds at end of Year 2), or does "same-year" imply something different about its duration?

## Turn 12 - User Simulator

It is a 1-year product: invest at the beginning of Year 2, receive proceeds at the end of Year 2.

## Turn 13 - Generic Agent

QUESTION: Product (4) is a 1-year product available at the beginning of Year 3, maturing at the end of Year 3. Is it available only at the beginning of Year 3 (i.e., you cannot invest in it at the beginning of Year 1 or Year 2), or is it available at the beginning of any year?

## Turn 13 - User Simulator

It is available only at the beginning of Year 3.

## Turn 14 - Generic Agent

QUESTION: Product (1) is described as "available at the beginning of each year (Years 1–3)." Does this mean you can invest in product (1) at the beginning of Year 1, the beginning of Year 2, AND the beginning of Year 3 (three separate investment opportunities), or is it available at the beginning of Years 1 and 2 only?

## Turn 14 - User Simulator

You can invest in product (1) at the beginning of Year 1, the beginning of Year 2, and the beginning of Year 3.

## Turn 15 - Generic Agent

QUESTION: At the beginning of Year 3, if you invest in product (1), it matures at the end of Year 3 and pays 1.20×I. At the beginning of Year 3, if you invest in product (4), it also matures at the end of Year 3 and pays 1.40×I. Since product (4) has a higher return but a 100,000 cap, and product (1) is unlimited, is there any other product available at the beginning of Year 3 besides product (1) and product (4)?

## Turn 15 - User Simulator

No, there are no other products available at the beginning of Year 3 besides product (1) and product (4).

## Turn 16 - Generic Agent

QUESTION: At the beginning of Year 2, the available cash is split between product (1) and product (3). Product (3) pays 1.60×I and is capped at 150,000, while product (1) pays 1.20×I and is unlimited. Is there any other product available at the beginning of Year 2 besides product (1) and product (3)?

## Turn 16 - User Simulator

No, there are no other products available at the beginning of Year 2 besides product (1) and product (3).

## Turn 17 - Generic Agent

QUESTION: At the beginning of Year 1, the available cash is split between product (1) and product (2). Product (2) pays 1.50×I at the end of Year 2 and is capped at 120,000, while product (1) pays 1.20×I at the end of Year 1 and is unlimited. Is there any other product available at the beginning of Year 1 besides product (1) and product (2)?

## Turn 17 - User Simulator

No, there are no other products available at the beginning of Year 1 besides product (1) and product (2).

## Turn 18 - Generic Agent

QUESTION: The objective is to maximize total principal plus interest at the end of Year 3, counting only proceeds from investments maturing at the end of Year 3. The investments maturing at the end of Year 3 are: product (1) invested at the beginning of Year 3 (pays 1.20×I) and product (4) invested at the beginning of Year 3 (pays 1.40×I). Is the objective simply to maximize 1.20×(amount in product 1 at start of Year 3) + 1.40×(amount in product 4 at start of Year 3)?

## Turn 18 - User Simulator

Yes, the objective is to maximize 1.20×(amount in product 1 at start of Year 3) + 1.40×(amount in product 4 at start of Year 3).

## Turn 19 - Generic Agent

QUESTION: At the beginning of Year 1, the 500,000 yuan can be split between product (1), product (2), and idle cash. At the beginning of Year 2, the available cash (proceeds from product 1 at end of Year 1 + idle cash from Year 1) can be split between product (1), product (3), and idle cash. At the beginning of Year 3, the available cash (proceeds from product 1 at end of Year 2 + proceeds from product 2 at end of Year 2 + proceeds from product 3 at end of Year 2 + idle cash from Year 2) can be split between product (1), product (4), and idle cash. Is this the complete set of cash flow constraints, or are there any additional constraints I should be aware of?

## Turn 19 - User Simulator

This is the complete set of cash flow constraints.

## Turn 20 - Generic Agent

READY_TO_MODEL

**Confirmed understanding:**

**Objective:** Maximize 1.20 × (amount invested in product 1 at start of Year 3) + 1.40 × (amount invested in product 4 at start of Year 3). Only proceeds maturing at end of Year 3 count.

**Decision variables (all continuous, non-negative):**
- x1_1: amount in product (1) at start of Year 1
- x2_1: amount in product (2) at start of Year 1
- c1: idle cash at start of Year 1
- x1_2: amount in product (1) at start of Year 2
- x3_2: amount in product (3) at start of Year 2
- c2: idle cash at start of Year 2
- x1_3: amount in product (1) at start of Year 3
- x4_3: amount in product (4) at start of Year 3
- c3: idle cash at start of Year 3 (not counted in objective)

**Cash flow constraints:**
- Start of Year 1: x1_1 + x2_1 + c1 ≤ 500,000
- Start of Year 2: x1_2 + x3_2 + c2 ≤ 1.20·x1_1 + c1
- Start of Year 3: x1_3 + x4_3 + c3 ≤ 1.20·x1_2 + 1.50·x2_1 + 1.60·x3_2 + c2

**Caps:**
- x2_1 ≤ 120,000
- x3_2 ≤ 150,000
- x4_3 ≤ 100,000

**Product availability:**
- Product (1): available at start of Years 1, 2, 3; 1-year; pays 1.20×I; unlimited
- Product (2): available only at start of Year 1; 2-year (locked until end of Year 2); pays 1.50×I; cap 120,000
- Product (3): available only at start of Year 2; 1-year; pays 1.60×I; cap 150,000
- Product (4): available only at start of Year 3; 1-year; pays 1.40×I; cap 100,000

**Idle cash:** carries over at face value (1.00×); no interest; not counted in final objective.

**No other constraints.**