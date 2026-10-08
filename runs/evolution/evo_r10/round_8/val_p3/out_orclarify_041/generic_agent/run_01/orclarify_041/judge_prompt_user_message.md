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

QUESTION: If you invest in product (1) at the beginning of Year 3, does the 1.20·I return arrive at the end of Year 3 (counting toward the final objective), or at the end of Year 4 (outside the planning horizon and therefore not counted)?

## Turn 1 - User Simulator

The 1.20·I return arrives at the end of Year 3, so it counts toward the final objective.

## Turn 2 - Generic Agent

QUESTION: Is there any limit on how much can be invested in product (1) in a given year, or is it truly unlimited as stated?

## Turn 2 - User Simulator

Product (1) is truly unlimited as stated.

## Turn 3 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the four products, or can you invest any amount down to zero?

## Turn 3 - User Simulator

There is no minimum investment amount; you can invest any amount down to zero.

## Turn 4 - Generic Agent

QUESTION: Are the investments in the four products required to be whole numbers (e.g., integer yuan), or can you invest any fractional amount?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: When you invest in product (1) at the beginning of a year, is the full amount I locked up for that entire year (i.e., you cannot use it for anything else until the 1.20·I is paid at year's end)?

## Turn 5 - User Simulator

Yes, the full amount I is locked up for that entire year and cannot be used for anything else until the 1.20·I is paid at year's end.

## Turn 6 - Generic Agent

QUESTION: At the beginning of Year 1, can you split the 500,000 yuan freely among product (1) and product (2) in any proportions, or is there any rule restricting how the initial capital must be allocated?

## Turn 6 - User Simulator

You can split the 500,000 yuan freely among product (1) and product (2) in any proportions, subject only to the 120,000 yuan cap on product (2) and the no-borrowing rule.

## Turn 7 - Generic Agent

QUESTION: You mentioned a "no-borrowing rule" — does this mean that at the beginning of each year, the total you invest in that year's available products cannot exceed the cash you have on hand at that moment (i.e., you can never invest more than your available funds)?

## Turn 7 - User Simulator

Yes, that is correct. At the beginning of each year, the total you invest cannot exceed the cash you have on hand at that moment.

## Turn 8 - Generic Agent

QUESTION: At the end of Year 3, is the objective to maximize the total cash on hand (i.e., all matured returns plus any uninvested cash), or only the sum of the matured investment returns?

## Turn 8 - User Simulator

The objective is to maximize the total cash on hand at the end of Year 3, which includes all matured returns plus any uninvested cash.

## Turn 9 - Generic Agent

QUESTION: If you have cash on hand at the beginning of a year that you do not invest in any product, does that cash simply carry over to the next year unchanged (no interest, no penalty)?

## Turn 9 - User Simulator

Yes, any uninvested cash simply carries over to the next year unchanged, with no interest and no penalty.

## Turn 10 - Generic Agent

QUESTION: Product (2) is a 2-year product available only at the beginning of Year 1, maturing at the end of Year 2 — does this mean the full 1.50·I is paid as a single lump sum at the end of Year 2, with no intermediate payment at the end of Year 1?

## Turn 10 - User Simulator

Yes, the full 1.50·I is paid as a single lump sum at the end of Year 2, with no intermediate payment at the end of Year 1.

## Turn 11 - Generic Agent

QUESTION: At the beginning of Year 2, the available products are (1) and (3) — can you split your Year 2 cash freely between product (1) and product (3) in any proportions, subject only to the 150,000 yuan cap on product (3) and the no-borrowing rule?

## Turn 11 - User Simulator

Yes, you can split your Year 2 cash freely between product (1) and product (3) in any proportions, subject only to the 150,000 yuan cap on product (3) and the no-borrowing rule.

## Turn 12 - Generic Agent

QUESTION: At the beginning of Year 3, the available products are (1) and (4) — can you split your Year 3 cash freely between product (1) and product (4) in any proportions, subject only to the 100,000 yuan cap on product (4) and the no-borrowing rule?

## Turn 12 - User Simulator

Yes, you can split your Year 3 cash freely between product (1) and product (4) in any proportions, subject only to the 100,000 yuan cap on product (4) and the no-borrowing rule.

## Turn 13 - Generic Agent

QUESTION: Regarding the integrality question you deferred earlier — should the investment amounts be modeled as continuous (any real number of yuan) or as integers (whole yuan amounts)?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: Is there any transaction cost, fee, or tax applied to any of the four products, or are the stated return multipliers (1.20, 1.50, 1.60, 1.40) the exact net amounts you receive?

## Turn 14 - User Simulator

The stated return multipliers (1.20, 1.50, 1.60, 1.40) are the exact net amounts you receive; there are no transaction costs, fees, or taxes.

## Turn 15 - Generic Agent

QUESTION: Are there any other constraints or rules I haven't asked about — for example, a maximum total portfolio value at any point in time, a requirement to invest at least some fraction of available cash each year, or any other business rule that would restrict the plan?

## Turn 15 - User Simulator

No, there are no other constraints or rules. The only restrictions are the individual product caps, the no-borrowing rule, and the availability windows for each product.

## Turn 16 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of Year 3 (all matured returns plus any uninvested cash).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Products and timing:**
- Product (1): 1-year, available at the beginning of Years 1, 2, and 3. Invest I at start of year → receive 1.20·I at end of that same year. Unlimited capacity.
- Product (2): 2-year, available only at the beginning of Year 1. Invest I at start of Year 1 → receive 1.50·I as a lump sum at end of Year 2. Cap: 120,000 yuan.
- Product (3): Same-year (1-year), available only at the beginning of Year 2. Invest I at start of Year 2 → receive 1.60·I at end of Year 2. Cap: 150,000 yuan.
- Product (4): 1-year, available only at the beginning of Year 3. Invest I at start of Year 3 → receive 1.40·I at end of Year 3. Cap: 100,000 yuan.

**Constraints:**
- No borrowing: at the beginning of each year, total investment in that year's available products ≤ cash on hand at that moment.
- Product caps: P2 ≤ 120,000; P3 ≤ 150,000; P4 ≤ 100,000.
- No minimum investment; amounts can be zero.
- Uninvested cash carries over to the next year unchanged (no interest, no penalty).
- Full investment is locked for the product's duration (no partial withdrawal).
- No transaction costs, fees, or taxes; stated multipliers are exact net returns.
- No other constraints.

**Integrality:** Deferred (client pending internal confirmation). I will model investment amounts as continuous variables; if integer yuan is later required, the model can be adjusted with integer declarations.

**Cash flow structure:**
- Beginning of Year 1: invest in P1 (Year 1) and P2; remainder carries to Year 2.
- End of Year 1: P1 (Year 1) matures → 1.20·I₁,₁.
- Beginning of Year 2: cash = carried-over + P1 (Year 1) return; invest in P1 (Year 2) and P3; remainder carries to Year 3.
- End of Year 2: P1 (Year 2) matures → 1.20·I₁,₂; P2 matures → 1.50·I₂; P3 matures → 1.60·I₃.
- Beginning of Year 3: cash = carried-over + all Year 2-end returns; invest in P1 (Year 3) and P4; remainder carries to end of Year 3.
- End of Year 3: P1 (Year 3) matures → 1.20·I₁,₃; P4 matures → 1.40·I₄; plus any uninvested cash. Objective = sum of all these.