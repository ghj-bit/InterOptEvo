## Turn 1 - Generic Agent

QUESTION: At the end of Year 3, is any money that has not been invested in a maturing product (i.e., cash held idle) counted in the final total principal plus interest, or must all funds be invested in products that mature by the end of Year 3?

## Turn 1 - User Simulator

Cash held idle at the end of Year 3 is counted in the final total. The objective is to maximize total wealth at the end of Year 3, which includes both the proceeds from matured investments and any uninvested cash remaining.

## Turn 2 - Generic Agent

QUESTION: For the 1-year product (1), is it available at the beginning of Year 2 and Year 3 as well, or only at the beginning of Year 1?

## Turn 2 - User Simulator

Product (1) is available at the beginning of each year (Years 1–3).

## Turn 3 - Generic Agent

QUESTION: Can money received from a product maturing at the end of Year 1 be reinvested in products available at the beginning of Year 2, and can money received from a product maturing at the end of Year 2 be reinvested in products available at the beginning of Year 3?

## Turn 3 - User Simulator

Yes. Money received from a product maturing at the end of Year 1 can be reinvested in products available at the beginning of Year 2, and money received from a product maturing at the end of Year 2 can be reinvested in products available at the beginning of Year 3.

## Turn 4 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the products, or can any non-negative amount be invested in each product?

## Turn 4 - User Simulator

There is no minimum investment amount. Any non-negative amount can be invested in each product, subject to the maximum caps for products (2), (3), and (4).

## Turn 5 - Generic Agent

QUESTION: Is there any limit on the total amount that can be invested in product (1) across all three years, or is it truly unlimited in each year?

## Turn 5 - User Simulator

Product (1) is unlimited in each year. There is no cap on the total amount invested in product (1) across the three years.

## Turn 6 - Generic Agent

QUESTION: Is there any constraint that the total investment at the beginning of each year cannot exceed the available cash at that time, or can you invest more than what you have available (i.e., borrowing is allowed)?

## Turn 6 - User Simulator

No borrowing is allowed. At the beginning of each year, you can only invest the cash you have at that moment, which comes from your initial capital and the proceeds of investments that have already matured.

## Turn 7 - Generic Agent

QUESTION: Is there any constraint that all available cash must be invested at the beginning of each year, or can you choose to hold some cash idle during a year and invest it later?

## Turn 7 - User Simulator

You can choose to hold some cash idle during a year and invest it later. There is no requirement to invest all available cash at the beginning of each year.

## Turn 8 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total wealth at the end of Year 3, which includes proceeds from all matured investments plus any uninvested cash held idle.

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Products:**
1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Returns 1.20×I at the end of that year. Unlimited capacity.
2. **Product (2):** 2-year product, available only at the beginning of Year 1. Matures at the end of Year 2, returns 1.50×I. Capped at 120,000 yuan.
3. **Product (3):** Same-year product, available only at the beginning of Year 2. Matures at the end of Year 2, returns 1.60×I. Capped at 150,000 yuan.
4. **Product (4):** 1-year product, available only at the beginning of Year 3. Matures at the end of Year 3, returns 1.40×I. Capped at 100,000 yuan.

**Key rules:**
- No borrowing: investments in any year are limited to available cash (initial capital plus proceeds from previously matured investments).
- Reinvestment is allowed: proceeds from products maturing at the end of Year 1 can be invested at the beginning of Year 2; proceeds from products maturing at the end of Year 2 can be invested at the beginning of Year 3.
- Cash can be held idle: there is no requirement to invest all available cash in any given year.
- No minimum investment: any non-negative amount can be invested in each product.
- Product (1) has no cap in any year.