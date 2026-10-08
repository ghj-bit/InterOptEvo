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

QUESTION: For project (1), is the 20% annual profit paid at the end of each year while the principal remains invested, and can you invest in or withdraw from project (1) at the beginning of any of the three years?

## Turn 1 - User Simulator

Yes, the 20% annual profit is paid at the end of each year while the principal remains invested. And yes, you can invest in project (1) at the beginning of any of the three years.

## Turn 2 - Generic Agent

QUESTION: For project (2), is the 150% total return paid as a single lump sum at the end of the third year (i.e., you get back 1.5 times the amount invested, with nothing before then)?

## Turn 2 - User Simulator

No, that is not correct. The investment in project (2) is recovered at the end of the second year, not the third year.

## Turn 3 - Generic Agent

QUESTION: For project (2), is the 150% total return paid as a single lump sum at the end of the second year (i.e., you get back 1.5 times the amount invested, with nothing before then)?

## Turn 3 - User Simulator

Yes, the 150% total return for project (2) is paid as a single lump sum at the end of the second year.

## Turn 4 - Generic Agent

QUESTION: For project (3), is the 160% total return paid as a single lump sum at the end of the third year (i.e., you get back 1.6 times the amount invested, with nothing before then)?

## Turn 4 - User Simulator

Yes, the 160% total return for project (3) is paid as a single lump sum at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: For project (4), is the 40% profit paid as a single lump sum at the end of the third year (i.e., you get back 1.4 times the amount invested, with nothing before then)?

## Turn 5 - User Simulator

Yes, the 40% profit for project (4) is paid as a single lump sum at the end of the third year, so you get back 1.4 times the amount invested.

## Turn 6 - Generic Agent

QUESTION: For project (3), can you invest in it at the beginning of any of the three years, or only at the beginning of the first year?

## Turn 6 - User Simulator

You can only invest in project (3) at the beginning of the second year.

## Turn 7 - Generic Agent

QUESTION: For project (4), can you invest in it at the beginning of any of the three years, or only at a specific year?

## Turn 7 - User Simulator

You can only invest in project (4) at the beginning of the third year.

## Turn 8 - Generic Agent

QUESTION: When you invest in project (1) at the beginning of a year, is the 20% profit paid only for that one year (i.e., the investment is a one-year instrument you can reinvest each year), or does the principal stay in project (1) and keep earning 20% every year until you choose to withdraw it?

## Turn 8 - User Simulator

The investment in project (1) is a one-year instrument. The 20% profit is paid at the end of that year, and then the entire amount—both the original investment and the 20% profit—can be reinvested in any project the next year.

## Turn 9 - Generic Agent

QUESTION: Is there any limit on how much you can invest in project (1), or is it unlimited?

## Turn 9 - User Simulator

There is no stated limit on how much you can invest in project (1).

## Turn 10 - Generic Agent

QUESTION: At the end of the third year, is the objective to maximize the total cash on hand (principal plus interest from all projects that have matured), with no requirement to hold any investment beyond that point?

## Turn 10 - User Simulator

Yes, the objective is to maximize the total cash on hand at the end of the third year, with no requirement to hold any investment beyond that point.

## Turn 11 - Generic Agent

QUESTION: Can you invest in project (2) at the beginning of the second year as well, or is it strictly only at the beginning of the first year?

## Turn 11 - User Simulator

It is strictly only at the beginning of the first year.

## Turn 12 - Generic Agent

QUESTION: If you invest in project (2) at the beginning of year 1 and it matures at the end of year 2, can the 1.5x lump sum you receive at the end of year 2 be reinvested in project (1) for year 3 (earning 20% by the end of year 3)?

## Turn 12 - User Simulator

Yes, the 1.5x lump sum received at the end of year 2 can be reinvested in project (1) for year 3, earning 20% by the end of year 3.

## Turn 13 - Generic Agent

QUESTION: Is there any minimum investment amount or integrality requirement (e.g., investments must be in whole yuan or in fixed increments), or can you invest any continuous amount in each project?

## Turn 13 - User Simulator

There is no minimum investment amount or integrality requirement. You can invest any continuous amount in each project.

## Turn 14 - Generic Agent

QUESTION: Is there any limit on the total amount you can invest across all projects in a given year, other than the 300,000 yuan initial fund and the cash you have available at that time?

## Turn 14 - User Simulator

No, there is no limit on the total amount you can invest across all projects in a given year, other than the cash you have available at that time.

## Turn 15 - Generic Agent

READY_TO_MODEL

Confirmed understanding:

**Objective:** Maximize total cash on hand at the end of year 3.

**Initial fund:** 300,000 yuan available at the beginning of year 1.

**Projects and their rules:**

- **Project (1):** One-year instrument. 20% profit paid at the end of the year. Can invest at the beginning of any year (1, 2, or 3). No investment limit. The full amount (principal + profit) is available for reinvestment the following year.

- **Project (2):** Can only invest at the beginning of year 1. Maximum investment: 150,000 yuan. Returns 150% of the investment as a single lump sum at the end of year 2. The lump sum can be reinvested in year 3.

- **Project (3):** Can only invest at the beginning of year 2. Maximum investment: 200,000 yuan. Returns 160% of the investment as a single lump sum at the end of year 3.

- **Project (4):** Can only invest at the beginning of year 3. Maximum investment: 100,000 yuan. Returns 140% of the investment (i.e., 40% profit) as a single lump sum at the end of year 3.

**Cash flow / reinvestment rules:**
- At the beginning of each year, you can allocate available cash among the projects that are open in that year.
- At the end of each year, matured returns become available cash for the next year.
- No borrowing; you cannot invest more than available cash in any year.
- No minimum investment, no integrality constraints (continuous variables).
- No requirement to hold investments beyond the end of year 3.

**Decision variables (continuous, non-negative):**
- x1_1, x1_2, x1_3: amount invested in project (1) at the beginning of years 1, 2, 3 respectively.
- x2_1: amount invested in project (2) at the beginning of year 1.
- x3_2: amount invested in project (3) at the beginning of year 2.
- x4_3: amount invested in project (4) at the beginning of year 3.

**Constraints:**
- Year 1: x1_1 + x2_1 ≤ 300,000
- x2_1 ≤ 150,000
- Year 2: x1_2 + x3_2 ≤ 1.2·x1_1 + 1.5·x2_1
- x3_2 ≤ 200,000
- Year 3: x1_3 + x4_3 ≤ 1.2·x1_2
- x4_3 ≤ 100,000

**Objective:** Maximize 1.2·x1_3 + 1.6·x3_2 + 1.4·x4_3