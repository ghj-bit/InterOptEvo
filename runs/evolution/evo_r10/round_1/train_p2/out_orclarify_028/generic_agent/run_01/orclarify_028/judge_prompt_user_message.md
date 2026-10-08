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

QUESTION: For project (1), is the 20% annual profit paid each year and the principal returned at the end of the third year, or is the 20% compounded annually so that the amount grows by 20% each year?

## Turn 1 - User Simulator

The 20% is an annual profit. Each year, you receive 20% of the amount you invested that year, and the full principal plus that year's profit is available to be reinvested in the following year. It is not a single lump-sum return at the end of the third year.

## Turn 2 - Generic Agent

QUESTION: For projects (2), (3), and (4), are the stated total returns (150%, 160%, 40%) paid as a single lump sum at the end of the third year, or do they accrue annually like project (1)?

## Turn 2 - User Simulator

The stated returns for projects (2), (3), and (4) are paid as a single lump sum at the time each project is recovered. They do not accrue annually like project (1).

## Turn 3 - Generic Agent

QUESTION: When you say project (2) is "recovered" at the end of the third year, does the 150% total return mean you receive 150% of the investment (i.e., 1.5x the principal) at that time, or do you receive the original principal plus an additional 150% profit (i.e., 2.5x the principal)?

## Turn 3 - User Simulator

The 150% total return means you receive 150% of the investment amount (1.5x the principal) at the time of recovery.

## Turn 4 - Generic Agent

QUESTION: For projects (3) and (4), do the 160% and 40% total returns also mean you receive 160% and 40% of the investment amount (1.6x and 0.4x the principal) at the time of recovery, respectively?

## Turn 4 - User Simulator

Yes, the 160% and 40% total returns mean you receive 160% and 40% of the investment amount (1.6x and 0.4x the principal) at the time of recovery, respectively.

## Turn 5 - Generic Agent

QUESTION: Can you invest in projects (3) and (4) at the beginning of any of the three years, or are they only available at specific times?

## Turn 5 - User Simulator

Project (3) is only available at the beginning of the second year, and project (4) is only available at the beginning of the third year.

## Turn 6 - Generic Agent

QUESTION: Can you invest in project (1) at the beginning of each of the three years, or is it only available at specific times?

## Turn 6 - User Simulator

You can invest in project (1) at the beginning of any of the three years.

## Turn 7 - Generic Agent

QUESTION: At the end of the third year, is the objective to maximize the total cash on hand (including any unrecovered investments that are still outstanding), or do all investments need to be fully recovered by the end of the third year?

## Turn 7 - User Simulator

The objective is to maximize the total cash on hand at the end of the third year. All investments in projects (2), (3), and (4) are recovered by the end of the third year, so there are no outstanding unrecovered investments at that time.

## Turn 8 - Generic Agent

QUESTION: When you say the full principal plus that year's profit is available to be reinvested in the following year for project (1), does that mean the principal is returned at the end of each year along with the profit, or does the principal remain locked in project (1) and only the 20% profit is paid out annually?

## Turn 8 - User Simulator

The principal is returned at the end of each year along with the 20% profit. The full amount (principal plus profit) is available to be reinvested in the following year.

## Turn 9 - Generic Agent

QUESTION: If you invest in project (1) at the beginning of year 3, do you receive the 20% profit and the principal back at the end of year 3, making it available for the final cash count?

## Turn 9 - User Simulator

Yes, if you invest in project (1) at the beginning of year 3, you receive the 20% profit and the principal back at the end of year 3, making it available for the final cash count.

## Turn 10 - Generic Agent

QUESTION: Is there any limit on how much you can invest in project (1) in any given year, or is it unlimited?

## Turn 10 - User Simulator

There is no stated limit on how much you can invest in project (1) in any given year.

## Turn 11 - Generic Agent

QUESTION: Can you invest in project (2) at the beginning of the first year only, or can you also invest in it at the beginning of years 2 or 3?

## Turn 11 - User Simulator

You can only invest in project (2) at the beginning of the first year.

## Turn 12 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the projects, or can you invest any amount (including zero) up to the stated limits?

## Turn 12 - User Simulator

There is no minimum investment amount required. You can invest any amount, including zero, up to the stated limits for each project.

## Turn 13 - Generic Agent

QUESTION: Are the investment amounts for each project required to be whole numbers (e.g., whole yuan), or can they be any continuous value?

## Turn 13 - User Simulator

The investment amounts can be any continuous value; they do not need to be whole numbers.

## Turn 14 - Generic Agent

QUESTION: Is there any transaction cost, tax, or fee associated with investing in or recovering from any of the projects?

## Turn 14 - User Simulator

There are no transaction costs, taxes, or fees associated with investing in or recovering from any of the projects.

## Turn 15 - Generic Agent

QUESTION: At the beginning of each year, can you split your available cash arbitrarily among the projects available that year, or must you invest all available cash?

## Turn 15 - User Simulator

You can split your available cash arbitrarily among the projects available that year. You are not required to invest all available cash.

## Turn 16 - Generic Agent

QUESTION: If you choose not to invest some of your available cash in a given year, does that cash simply carry over to the next year with no interest or return?

## Turn 16 - User Simulator

Yes, if you choose not to invest some of your available cash in a given year, that cash simply carries over to the next year with no interest or return.

## Turn 17 - Generic Agent

QUESTION: Is there any constraint that requires you to invest in at least one project in each year, or can you choose to invest in none of the available projects in a given year?

## Turn 17 - User Simulator

There is no constraint requiring you to invest in at least one project in each year. You can choose to invest in none of the available projects in a given year.

## Turn 18 - Generic Agent

QUESTION: Can you invest in multiple projects in the same year, or are you limited to investing in only one project per year?

## Turn 18 - User Simulator

You can invest in multiple projects in the same year, as long as the total does not exceed your available cash and each project's individual limit is respected.

## Turn 19 - Generic Agent

QUESTION: Is there any constraint on the total amount you can invest across all projects in a single year, other than your available cash and the individual project limits?

## Turn 19 - User Simulator

No, there is no additional constraint on the total amount you can invest across all projects in a single year, other than your available cash and the individual project limits.

## Turn 20 - Generic Agent

QUESTION: At the end of the third year, is the final cash count simply the sum of all cash received from project recoveries and any uninvested cash carried over, with no other adjustments?

## Turn 20 - User Simulator

Yes, the final cash count at the end of the third year is simply the sum of all cash received from project recoveries and any uninvested cash carried over, with no other adjustments.

## Turn 21 - Generic Agent

QUESTION: Is there any constraint that the total investment in project (1) across all three years must not exceed some overall limit, or is the only constraint on project (1) the available cash in each year?

## Turn 21 - User Simulator

There is no overall limit on the total investment in project (1) across all three years. The only constraint is the available cash in each year.

## Turn 22 - Generic Agent

QUESTION: Is there any constraint that the total investment in projects (2), (3), and (4) combined must not exceed some overall limit, or are the only constraints the individual project limits and available cash?

## Turn 22 - User Simulator

There is no overall limit on the combined investment in projects (2), (3), and (4). The only constraints are the individual project limits and available cash.

## Turn 23 - Generic Agent

QUESTION: Is there any constraint that the total investment in all projects combined must not exceed some overall limit, or are the only constraints the individual project limits and available cash?

## Turn 23 - User Simulator

There is no overall limit on the total investment in all projects combined. The only constraints are the individual project limits and available cash.

## Turn 24 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the beginning of each year must be fully allocated (i.e., no cash can be held as idle cash), or is it acceptable to hold idle cash that carries over to the next year?

## Turn 24 - User Simulator

It is acceptable to hold idle cash that carries over to the next year. There is no constraint requiring all available cash to be fully allocated each year.

## Turn 25 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the beginning of each year must be non-negative, or can it be negative (i.e., can you borrow)?

## Turn 25 - User Simulator

The total cash available at the beginning of each year must be non-negative. You cannot borrow.

## Turn 26 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the end of the third year must be non-negative, or can it be negative?

## Turn 26 - User Simulator

The total cash available at the end of the third year must be non-negative.

## Turn 27 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the end of each year (years 1 and 2) must be non-negative, or can it be negative?

## Turn 27 - User Simulator

The total cash available at the end of each year (years 1 and 2) must be non-negative.

## Turn 28 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the beginning of each year must be non-negative, or can it be negative?

## Turn 28 - User Simulator

The total cash available at the beginning of each year must be non-negative.

## Turn 29 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the end of the third year must be non-negative, or can it be negative?

## Turn 29 - User Simulator

The total cash available at the end of the third year must be non-negative.

## Turn 30 - Generic Agent

QUESTION: Is there any constraint that the total cash available at the beginning of each year must be non-negative, or can it be negative?

## Turn 30 - User Simulator

The total cash available at the beginning of each year must be non-negative.