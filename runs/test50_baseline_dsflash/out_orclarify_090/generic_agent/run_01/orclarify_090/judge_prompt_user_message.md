# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U6, U7, U8, U2, U3, U4
I need help designing promotional packages to clear out last season's inventory. Total shirts used in packages cannot exceed 200, total pants used in packages cannot exceed 100, and the number of A packages sold must be at least 20 while the number of B packages sold must be at least 10.

Available inventory: 200 shirts, 100 pairs of pants.

Package A: 1 shirt, 2 pairs of pants, price £30. Package B: 3 shirts, 1 pair of pants, price £50.

Minimum desired sales: 20 package A, 10 package B.

## Problem units
- U1 (context): I need help designing promotional packages to clear out last season's inventory.
- U2 (data): Available inventory: 200 shirts, 100 pairs of pants.
- U3 (data): Package A: 1 shirt, 2 pairs of pants, price £30. Package B: 3 shirts, 1 pair of pants, price £50.
- U4 (data): Minimum desired sales: 20 package A, 10 package B.
- U5 (constraint): Total shirts used in packages cannot exceed 200.
- U6 (constraint): Total pants used in packages cannot exceed 100.
- U7 (constraint): Number of A packages sold must be at least 20.
- U8 (constraint): Number of B packages sold must be at least 10.
- U9 (objective): Maximize total revenue from selling packages A and B.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without knowing the objective, a modeling agent cannot define the optimization criterion. The entire problem formulation is impossible without specifying what should be maximized.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must explicitly ask about the optimization goal, mentioning "revenue" or "objective" or "maximize" in the context of what to optimize.
- Reference acceptable questions:
  - What exactly are we trying to maximize? Is it total revenue, profit, or something else?
  - Should we just focus on getting the most money from selling the packages?
- Failure modes:
  - Silent assumption that the goal is to maximize profit rather than revenue.
  - Incorrectly assuming the objective is to minimize leftover inventory.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the objective you want the package mix to achieve—maximize total revenue, clear as much inventory as possible, or something else?

## Turn 1 - User Simulator

Maximize total revenue.

## Turn 2 - Generic Agent

QUESTION: Do you need the number of packages sold to be whole numbers (integer packages), or is it acceptable to plan fractional packages?

## Turn 2 - User Simulator

The number of packages sold must be whole numbers.

## Turn 3 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of your problem:

**Goal:** Maximize total revenue from promotional packages.

**Decision variables:**
- A = number of Package A sold (integer)
- B = number of Package B sold (integer)

**Resource constraints (available inventory):**
- Shirts: 1·A + 3·B ≤ 200
- Pants: 2·A + 1·B ≤ 100

**Minimum sales requirements:**
- A ≥ 20
- B ≥ 10

**Revenue:**
- Package A: £30 each
- Package B: £50 each
- Maximize: 30·A + 50·B

**Integrality:** A and B must be whole numbers.

Let me solve this integer program.

**Step 1 — Check the binding constraints.**
Pants are the scarcer resource (only 100, and Package A uses 2 each). The pants constraint 2A + B ≤ 100 will likely bind.

**Step 2 — Solve the LP relaxation.**
Maximize 30A + 50B subject to:
- A + 3B ≤ 200
- 2A + B ≤ 100
- A ≥ 20, B ≥ 10

Revenue per pant: A = £30/2 = £15 per pant; B = £50/1 = £50 per pant. So B is far more valuable per pant. Push B as high as possible.

From pants: B ≤ 100 − 2A. From shirts: B ≤ (200 − A)/3.

Set the two equal: 100 − 2A = (200 − A)/3 → 300 − 6A = 200 − A → 100 = 5A → A = 20, B = 60.

Check shirts: 20 + 3(60) = 200 ✓ (binds exactly)
Check pants: 2(20) + 60 = 100 ✓ (binds exactly)

This is the LP optimum: A = 20, B = 60, and it is already integer.

**Step 3 — Verify optimality.**
Both constraints bind at A = 20, B = 60. Revenue = 30(20) + 50(60) = 600 + 3000 = **£3,600**.

Since B earns more per unit of both scarce resources (per pant: £50 vs £15; per shirt: £16.67 vs £30 — note A is better per shirt, but pants are the tighter limit), the corner solution at the intersection of both constraints is optimal. The minimum A = 20 is exactly satisfied, so no need to reduce A.

**Final answer:**

| Package | Quantity | Revenue |
|---------|----------|---------|
| A | 20 | £600 |
| B | 60 | £1,000... |

Correction — let me restate cleanly:

- Package A: 20 units × £30 = £600
- Package B: 60 units × £50 = £3,000
- **Total revenue: £3,600**

**Inventory used:**
- Shirts: 20 + 180 = 200 (all 200 used)
- Pants: 40 + 60 = 100 (all 100 used)

**Recommendation:** Sell 20 Package A and 60 Package B. This maximizes revenue at **£3,600**, fully clears both shirts and pants, and satisfies the minimum sales requirements (A ≥ 20, B ≥ 10).