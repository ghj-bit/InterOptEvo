## Turn 1 - Generic Agent

QUESTION: At the end of Year 3, can you still hold any un-matured investments (for example, a product-1 investment made at the start of Year 3 that has not yet paid out), or must all funds be in cash by the end of Year 3 so that only matured amounts count toward the objective?

## Turn 1 - User Simulator

All funds must be in cash by the end of Year 3. Only matured amounts count toward the objective.

## Turn 2 - Generic Agent

QUESTION: Product (1) is described as available at the beginning of each year (Years 1–3) and matures at that year's end — so a product-1 investment made at the start of Year 3 would mature at the end of Year 3 and count toward the objective. Is that correct, or should product (1) be available only at the beginnings of Years 1 and 2 (so that no new product-1 investment can be made in Year 3)?

## Turn 2 - User Simulator

That is correct. Product (1) is available at the beginning of Year 3, and an investment made then matures at the end of Year 3, so it counts toward the objective.

## Turn 3 - Generic Agent

QUESTION: Are there any minimum investment amounts or fixed fees for any of the four products, or can you invest any non-negative amount (including zero) in each product at each time it is available?

## Turn 3 - User Simulator

You can invest any non-negative amount, including zero, in each product at each time it is available. There are no minimum investment amounts or fixed fees.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in a given year, or is it truly unlimited as stated?

## Turn 4 - User Simulator

It is truly unlimited. There is no limit on how much you can invest in product (1) in a given year.

## Turn 5 - Generic Agent

QUESTION: Are there any other constraints I should know about, such as a maximum total amount that can be invested in any single year, a requirement to keep a minimum cash reserve, or any taxes or transaction costs on the returns?

## Turn 5 - User Simulator

No. There are no maximum total investment limits per year, no minimum cash reserve requirements, and no taxes or transaction costs on the returns.

## Turn 6 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash (principal + interest) at the end of Year 3. Only matured amounts count; all funds must be in cash by the end of Year 3.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

| Product | Type | Available | Matures | Return | Capacity |
|---------|------|-----------|---------|--------|----------|
| (1) | 1-year | Beginning of Years 1, 2, 3 | End of same year | 1.20·I | Unlimited |
| (2) | 2-year | Beginning of Year 1 only | End of Year 2 | 1.50·I | ≤ 120,000 |
| (3) | Same-year | Beginning of Year 2 only | End of Year 2 | 1.60·I | ≤ 150,000 |
| (4) | 1-year | Beginning of Year 3 only | End of Year 3 | 1.40·I | ≤ 100,000 |

**Key facts confirmed:**
- Product (1) is available at the beginning of Year 3 and matures at the end of Year 3, so it counts toward the objective.
- Any non-negative amount (including zero) can be invested in each product; no minimums, no fixed fees.
- Product (1) has no capacity limit.
- No per-year total investment cap, no minimum cash reserve, no taxes, no transaction costs.
- All funds must be in cash by the end of Year 3 (no un-matured holdings allowed at the terminal date).

**Structure:** This is a three-period cash-flow allocation problem. At the beginning of each year, available cash is split among the products offered that year (plus possibly held as cash). At the end of each year, matured products return their proceeds to the cash pool for the next year's allocation. The terminal objective is the cash on hand at the end of Year 3.