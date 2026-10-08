# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U10, U11, U12, U15, U18, U20, U21, U2, U3, U4, U5, U6, U7, U8, U9
I need help creating an investment plan over three years, aiming to maximize the total principal and interest at the end of the third year. Investment in project (2) cannot exceed 150,000 yuan and is only allowed at the beginning of the first year. Investment in project (3) cannot exceed 200,000 yuan and can be recovered at the end of the third year, while investment in project (4) cannot exceed 100,000 yuan and can also be recovered at that time.

Initial fund: 300,000 yuan.

Annual profit of project (1): 20% of the investment amount.

Total return of project (2): 150% of the investment amount.

Investment limit for project (2): 150,000 yuan.

Total return of project (3): 160% of the investment amount.

Investment limit for project (3): 200,000 yuan.

Profit of project (4): 40% of the investment amount.

Investment limit for project (4): 100,000 yuan.

## Problem units
- U1 (context): I need help creating an investment plan over three years.
- U2 (data): Initial fund: 300,000 yuan.
- U3 (data): Annual profit of project (1): 20% of the investment amount.
- U4 (data): Total return of project (2): 150% of the investment amount.
- U5 (data): Investment limit for project (2): 150,000 yuan.
- U6 (data): Total return of project (3): 160% of the investment amount.
- U7 (data): Investment limit for project (3): 200,000 yuan.
- U8 (data): Profit of project (4): 40% of the investment amount.
- U9 (data): Investment limit for project (4): 100,000 yuan.
- U10 (constraint): Investment in project (2) cannot exceed 150,000 yuan.
- U11 (constraint): Investment in project (3) cannot exceed 200,000 yuan.
- U12 (constraint): Investment in project (4) cannot exceed 100,000 yuan.
- U13 (constraint): Investment in project (1) can be made at the beginning of any of the three years.
- U14 (constraint): The principal and interest from project (1) can be reinvested in the following year.
- U15 (constraint): Investment in project (2) is only allowed at the beginning of the first year.
- U16 (constraint): Investment in project (2) can be recovered at the end of the second year.
- U17 (constraint): Investment in project (3) is allowed at the beginning of the second year.
- U18 (constraint): Investment in project (3) can be recovered at the end of the third year.
- U19 (constraint): Investment in project (4) is allowed at the beginning of the third year.
- U20 (constraint): Investment in project (4) can be recovered at the end of the third year.
- U21 (objective): Maximize the total principal and interest at the end of the third year.

## Hidden slot scoring rules
## H1: project1_investment_timing
- Severity: P1
- Severity reason: Without this constraint, the agent might assume project (1) investment is restricted to a specific year, missing the multi-year flexibility that influences the entire cash flow and reinvestment strategy.
- Problem unit ID: U13
- Semantic hit rule: Agent asks whether project (1) investment is allowed at the beginning of multiple years, demonstrating an understanding that the timing might be flexible.
- Reference acceptable questions:
  - Is it possible to invest in project (1) at the beginning of any of the three years, or only in certain years?
  - When exactly can I put money into project (1)? Only at the start of the first year, or also in year 2 and 3?
- Failure modes:
  - Assume project (1) can only be invested at the beginning of the first year.
  - Assume project (1) can be invested only once, at any year but not multiple times.

## H2: project1_reinvestment_rule
- Severity: P1
- Severity reason: If the agent assumes no reinvestment of project (1) returns, the model will miss the compounding effect and produce a suboptimal plan, fundamentally altering the objective's attainment.
- Problem unit ID: U14
- Semantic hit rule: Agent asks explicitly about whether the proceeds (principal + interest) from project (1) are reinvestable in the following year, or queries the cash flow availability for reinvestment.
- Reference acceptable questions:
  - After I get the profit and principal back from a project (1) investment at the end of a year, can I reinvest that total amount in the next year?
  - Are the returns from project (1) available for reinvestment in subsequent years, or is that money no longer usable?
- Failure modes:
  - Assume principal and interest are only received at the end of year 3 and cannot be reinvested.
  - Assume the interest can be reinvested but the principal must remain separate.

## H3: project2_recovery_timing
- Severity: P1
- Severity reason: Incorrect assumption about when project (2) funds are recovered would misalign cash inflows in the time-stage model, leading to errors in investment opportunity feasibility.
- Problem unit ID: U16
- Semantic hit rule: Agent asks about the specific recovery date of project (2) relative to the year boundaries, confirming it is at the end of year 2.
- Reference acceptable questions:
  - When exactly do I get back the money from project (2)? Is it at the end of the second year?
  - For the second investment option, when can I access the total principal and interest—at the end of year 2?
- Failure modes:
  - Assume project (2) is recovered at the end of the first year.
  - Assume project (2) is recovered at the end of the third year.

## H4: project3_investment_timing
- Severity: P1
- Severity reason: If the agent assumes unrestricted timing for project (3), the model becomes overly permissive and may suggest investments in years that are not actually allowed, yielding an invalid plan.
- Problem unit ID: U17
- Semantic hit rule: Agent asks whether project (3) investment is restricted to the beginning of the second year only, as opposed to being available in other years.
- Reference acceptable questions:
  - Is project (3) only available for investment at the start of the second year, or can I also invest in it earlier or later?
  - Can I invest in project (3) in the first year, or is it strictly the second year?
- Failure modes:
  - Assume project (3) can be invested at the beginning of any year.
  - Assume project (3) can only be invested at the beginning of the third year.

## H5: project4_investment_timing
- Severity: P1
- Severity reason: Without this timing restriction, the agent might include project (4) in earlier years, creating an infeasible or overly optimistic plan that violates the actual investment window.
- Problem unit ID: U19
- Semantic hit rule: Agent asks to confirm that project (4) investment is only permitted at the beginning of the third year.
- Reference acceptable questions:
  - Is it correct that I can only invest in project (4) at the beginning of the third year?
  - Does project (4) only accept investments at the start of year 3, or could I invest earlier?
- Failure modes:
  - Assume project (4) is available for investment at the beginning of any year.
  - Assume project (4) can be invested in the second year as well.


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: For project (1), is the 20% annual profit paid each year for all three years (so the investment stays in place and earns 20% per year), or is it a one-time return at the end of the first year after which the money is recovered?

## Turn 1 - User Simulator

The 20% profit is earned each year. The investment stays in place, and at the end of each year you receive the 20% profit on the amount invested that year. The principal and that year's profit can then be reinvested in the following year.

## Turn 2 - Generic Agent

QUESTION: For project (2), the 150% total return is received at the end of the first year (i.e., you invest at the start of year 1 and get back 150% of the amount at the end of year 1), correct?

## Turn 2 - User Simulator

No, that's not correct. The investment in project (2) is recovered at the end of the second year, not the end of the first year.

## Turn 3 - Generic Agent

QUESTION: For project (3), is the 160% total return received at the end of the third year, and can you invest in it at the beginning of any of the three years (with the return always paid at the end of year 3), or is it only investable at a specific year?

## Turn 3 - User Simulator

You can only invest in project (3) at the beginning of the second year. The 160% total return is received at the end of the third year.

## Turn 4 - Generic Agent

QUESTION: For project (4), at which year's beginning can you invest in it, and is the 40% profit a one-time return received at the end of the third year (so you get back 140% of the amount invested)?

## Turn 4 - User Simulator

You can only invest in project (4) at the beginning of the third year. The 40% profit is a one-time return received at the end of the third year, so you get back 140% of the amount invested.

## Turn 5 - Generic Agent

QUESTION: Is there any limit on how much can be invested in project (1) in each year, or can you invest any amount (up to the available funds) in it?

## Turn 5 - User Simulator

There is no specific investment limit for project (1). You can invest any amount, up to the available funds, at the beginning of any of the three years.

## Turn 6 - Generic Agent

QUESTION: At the end of the third year, is the objective to maximize the total cash on hand (principal plus all profits/returns received), with no requirement to hold any investment in place at that point?

## Turn 6 - User Simulator

Yes, the objective is to maximize the total cash on hand (principal plus all profits/returns received) at the end of the third year.

## Turn 7 - Generic Agent

QUESTION: When you receive the 20% annual profit from project (1) at the end of a year, is that profit cash that you can freely reinvest in any project (including project 1) at the beginning of the next year, or does it automatically stay in project (1) and compound?

## Turn 7 - User Simulator

The profit is cash that you can freely reinvest in any project, including project (1), at the beginning of the next year. It does not automatically stay in project (1).

## Turn 8 - Generic Agent

QUESTION: At the end of the first year, the project (1) principal itself is still locked in project (1) (only the 20% profit is released as cash), so the only cash available to invest at the beginning of year 2 is the year-1 profit from project (1) plus any other returns received, correct?

## Turn 8 - User Simulator

No, that's not correct. At the end of the first year, both the principal and the 20% profit from project (1) are released as cash. The entire amount can be reinvested in any project at the beginning of the next year.

## Turn 9 - Generic Agent

QUESTION: So project (1) works like this: you invest an amount at the beginning of a year, and at the end of that same year you get back 120% of it (principal plus 20% profit) as cash, which you can then reinvest at the beginning of the next year — is that the correct understanding?

## Turn 9 - User Simulator

Yes, that is the correct understanding. You invest an amount at the beginning of a year, and at the end of that same year you get back 120% of it (principal plus 20% profit) as cash, which you can then reinvest at the beginning of the next year.

## Turn 10 - Generic Agent

QUESTION: At the end of the third year, is the project (1) investment also released as cash (i.e., you get back 120% of the year-3 investment at the end of year 3), so that all cash on hand at the end of year 3 includes the year-3 project (1) principal and profit?

## Turn 10 - User Simulator

Yes, at the end of the third year, the project (1) investment is released as cash. You get back 120% of the year-3 investment (principal plus 20% profit), and this is included in the total cash on hand at the end of year 3.

## Turn 11 - Generic Agent

QUESTION: Are there any other constraints or rules I should know about, such as minimum investment amounts, transaction costs, or a requirement to invest all available funds each year (rather than being able to hold cash idle)?

## Turn 11 - User Simulator

No, there are no minimum investment amounts, transaction costs, or a requirement to invest all available funds each year. You can hold cash idle if you choose.

## Turn 12 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of year 3.

**Initial fund:** 300,000 yuan at the beginning of year 1.

**Projects:**

- **Project (1):** Investable at the beginning of any year (1, 2, or 3). No investment limit. At the end of the same year, you receive back 120% of the amount invested (principal + 20% profit) as cash, freely reinvestable the following year.

- **Project (2):** Investable only at the beginning of year 1. Maximum investment: 150,000 yuan. At the end of year 2, you receive back 150% of the amount invested (total return) as cash.

- **Project (3):** Investable only at the beginning of year 2. Maximum investment: 200,000 yuan. At the end of year 3, you receive back 160% of the amount invested (total return) as cash.

- **Project (4):** Investable only at the beginning of year 3. Maximum investment: 100,000 yuan. At the end of year 3, you receive back 140% of the amount invested (principal + 40% profit) as cash.

**Cash flow / reinvestment rules:**
- All returns received at the end of a year become available cash at the beginning of the next year.
- You may hold cash idle (no requirement to invest all funds each year).
- No minimum investment amounts, no transaction costs.

**Timeline of cash availability:**
- Beginning of year 1: 300,000 yuan available.
- End of year 1: 120% of year-1 project (1) investment is released.
- Beginning of year 2: year-1 project (1) returns + any idle cash from year 1.
- End of year 2: 120% of year-2 project (1) investment + 150% of project (2) investment are released.
- Beginning of year 3: year-2 project (1) returns + project (2) returns + any idle cash from year 2.
- End of year 3: 120% of year-3 project (1) investment + 160% of project (3) investment + 140% of project (4) investment + any idle cash from year 3 = total cash on hand (objective).