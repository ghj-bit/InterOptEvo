## Turn 1 - Generic Agent

QUESTION: At the end of Year 3, can you still hold uninvested cash (i.e., is there a "do nothing / keep cash" option that carries over at 1.00 with no interest), or must all available funds be allocated to one of the listed products each year?

## Turn 1 - User Simulator

You can hold uninvested cash. There is no requirement to allocate all available funds to the listed products each year. Any cash not invested simply carries over to the next period with no interest (i.e., it remains at face value).

## Turn 2 - Generic Agent

QUESTION: For product (1), the 1-year product available at the beginning of each year — is the 1.20 return the same in all three years (Years 1, 2, and 3), or does the rate differ by year?

## Turn 2 - User Simulator

The 1.20 return is the same in all three years (Years 1, 2, and 3).

## Turn 3 - Generic Agent

QUESTION: Product (2) is a 2-year product available only at the beginning of Year 1, maturing at the end of Year 2. During Year 2, is the money locked (i.e., cannot be used for product (3) or anything else in Year 2), or is it accessible?

## Turn 3 - User Simulator

The money is locked during Year 2. It cannot be used for product (3) or any other investment in Year 2. It only becomes available at the end of Year 2 when it matures.

## Turn 4 - Generic Agent

QUESTION: Is there any limit on how much you can invest in product (1) in a given year, or is it truly unlimited as stated?

## Turn 4 - User Simulator

It is truly unlimited. There is no cap on the amount you can invest in product (1) in any given year.

## Turn 5 - Generic Agent

QUESTION: Are there any minimum investment amounts for any of the products, or can you invest any amount (including fractional yuan) in each product?

## Turn 5 - User Simulator

There are no minimum investment amounts. You can invest any amount, including fractional yuan, in each product.

## Turn 6 - Generic Agent

QUESTION: Is there any limit on the total amount you can invest across all products in a single year, or is the only constraint the per-product caps and the available cash at the beginning of that year?

## Turn 6 - User Simulator

There is no limit on the total amount you can invest across all products in a single year. The only constraints are the per-product caps and the available cash at the beginning of that year.

## Turn 7 - Generic Agent

QUESTION: At the end of Year 3, is the objective simply the total cash on hand (principal plus all interest from matured products), with no additional costs, taxes, or fees to account for?

## Turn 7 - User Simulator

Yes. The objective is simply the total cash on hand at the end of Year 3, consisting of principal plus all interest from matured products. There are no additional costs, taxes, or fees to account for.

## Turn 8 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash on hand at the end of Year 3 (principal + interest from all matured investments).

**Initial capital:** 500,000 yuan at the beginning of Year 1.

**Investment products:**

1. **Product (1):** 1-year product, available at the beginning of Years 1, 2, and 3. Invest I at the start of a year → receive 1.20·I at that year's end. Unlimited capacity. Same 1.20 rate in all three years.

2. **Product (2):** 2-year product, available only at the beginning of Year 1. Invest I at the start of Year 1 → receive 1.50·I at the end of Year 2. Funds are locked during Year 2 (not available for other investments). Capped at 120,000 yuan.

3. **Product (3):** Same-year product, available only at the beginning of Year 2. Invest I at the start of Year 2 → receive 1.60·I at the end of Year 2. Capped at 150,000 yuan.

4. **Product (4):** 1-year product, available only at the beginning of Year 3. Invest I at the start of Year 3 → receive 1.40·I at the end of Year 3. Capped at 100,000 yuan.

**Cash carry-over:** Uninvested cash carries over to the next period at face value (no interest).

**Constraints:**
- Per-product caps: Product (2) ≤ 120,000; Product (3) ≤ 150,000; Product (4) ≤ 100,000.
- No cap on Product (1).
- No minimum investment amounts; fractional yuan allowed.
- No total annual investment limit beyond available cash.
- No taxes, fees, or other costs.
- All decision variables are continuous and non-negative.

**Structure:** Three decision periods (beginning of Years 1, 2, 3). Cash flow must be balanced at each period: available cash at the start of a year = carry-over from prior year + matured investments, and total investments in that year ≤ available cash.