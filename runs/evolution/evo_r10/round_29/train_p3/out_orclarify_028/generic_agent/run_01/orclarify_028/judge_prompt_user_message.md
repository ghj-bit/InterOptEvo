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

QUESTION: For project (1), is the 20% annual profit paid each year for all three years (i.e., you keep the principal and receive 20% of it as interest at the end of each of years 1, 2, and 3), or is it a one-time return paid only once?

## Turn 1 - User Simulator

The 20% profit is paid each year. You keep the principal and receive 20% of it as interest at the end of each year.

## Turn 2 - Generic Agent

QUESTION: For project (2), which pays a total return of 150% of the investment amount, is the 150% received all at once at the end of the third year (meaning you get back 150% of what you put in, with no principal returned separately), or is it 150% interest on top of the principal returned at the end of year 3?

## Turn 2 - User Simulator

The 150% is the total return received all at once at the end of the second year. It includes the principal; there is no separate principal returned.

## Turn 3 - Generic Agent

QUESTION: For project (3), is the 160% total return (which includes the principal) received all at once at the end of the third year, with no payments before that?

## Turn 3 - User Simulator

Yes, the 160% total return is received all at once at the end of the third year, with no payments before that.

## Turn 4 - Generic Agent

QUESTION: For project (4), is the 40% profit paid each year (like project 1, with principal kept and 40% interest received at the end of each year), or is it a one-time return received at the end of the third year?

## Turn 4 - User Simulator

It is a one-time return received at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: For project (4), does the 40% one-time return at the end of the third year include the principal (i.e., you get back 140% of what you invested), or is it 40% interest on top of the principal (i.e., you get back 140% total)?

## Turn 5 - User Simulator

The 40% is the profit on top of the principal. You get back 140% total at the end of the third year.

## Turn 6 - Generic Agent

QUESTION: Can you invest in projects (1), (3), and (4) at the beginning of any of the three years, or are there restrictions on which years you can start investing in them?

## Turn 6 - User Simulator

There are restrictions:

- Project (1): You can invest at the beginning of any of the three years.
- Project (3): You can only invest at the beginning of the second year.
- Project (4): You can only invest at the beginning of the third year.

## Turn 7 - Generic Agent

QUESTION: When you invest in project (1) at the beginning of a year, do you receive the 20% interest at the end of that same year, and can you reinvest that interest (or any other cash you have) into new investments at the beginning of the next year?

## Turn 7 - User Simulator

Yes, you receive the 20% interest at the end of that same year, and you can reinvest that interest (or any other cash you have) into new investments at the beginning of the next year.

## Turn 8 - Generic Agent

QUESTION: Are there any investment limits on project (1), or can you invest any amount in it (up to whatever cash you have available)?

## Turn 8 - User Simulator

There are no investment limits on project (1). You can invest any amount in it, up to whatever cash you have available.

## Turn 9 - Generic Agent

QUESTION: If you have leftover cash at the end of the third year that was not invested in any project, does it simply count toward your final total (principal and interest), or is there a penalty or different treatment for uninvested cash?

## Turn 9 - User Simulator

Leftover cash at the end of the third year simply counts toward your final total. There is no penalty or different treatment for uninvested cash.

## Turn 10 - Generic Agent

QUESTION: For project (2), which pays its 150% total return at the end of the second year, can you reinvest that 150% return at the beginning of the third year into other projects (like project 1 or project 4)?

## Turn 10 - User Simulator

Yes, you can reinvest that 150% return at the beginning of the third year into other projects, such as project 1 or project 4.

## Turn 11 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1, do you receive 20% interest at the end of year 1, 20% at the end of year 2, and 20% at the end of year 3 (three separate interest payments), or do you only receive interest for the years the money is actually held in the project?

## Turn 11 - User Simulator

You only receive interest for the years the money is actually held in the project.

## Turn 12 - Generic Agent

QUESTION: When you invest in project (1) at the beginning of a year, is the investment locked for exactly one year (so you get one 20% payment at the end of that year and the principal is returned), or can you choose to hold it for multiple years and receive 20% each year until you decide to withdraw?

## Turn 12 - User Simulator

The investment is locked for exactly one year. You get one 20% payment at the end of that year and the principal is returned.

## Turn 13 - Generic Agent

QUESTION: Can you invest in project (1) multiple times within the same year (e.g., split your cash into two separate one-year investments in project 1 at the beginning of the same year), or is there at most one investment in project (1) per year?

## Turn 13 - User Simulator

There is at most one investment in project (1) per year.

## Turn 14 - Generic Agent

QUESTION: At the beginning of each year, can you split your available cash across multiple projects (e.g., put some into project 1 and some into project 3 at the beginning of year 2), or must you allocate all your cash to a single project each year?

## Turn 14 - User Simulator

You can split your available cash across multiple projects at the beginning of each year.

## Turn 15 - Generic Agent

QUESTION: Is there any minimum investment amount required for any of the projects, or can you invest any positive amount (including very small amounts) in each project?

## Turn 15 - User Simulator

There is no minimum investment amount required for any of the projects. You can invest any positive amount in each project.

## Turn 16 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the problem:

**Objective:** Maximize total cash (principal + interest + returns) at the end of year 3.

**Initial fund:** 300,000 yuan at the beginning of year 1.

**Projects and their rules:**

- **Project 1:** Can be invested at the beginning of any year (1, 2, or 3). One-year lock. Returns 20% interest at the end of that year plus principal returned. No investment limit. At most one investment per year.

- **Project 2:** Can only be invested at the beginning of year 1. Maximum investment: 150,000 yuan. Returns 150% of the investment amount (total, including principal) at the end of year 2.

- **Project 3:** Can only be invested at the beginning of year 2. Maximum investment: 200,000 yuan. Returns 160% of the investment amount (total, including principal) at the end of year 3.

- **Project 4:** Can only be invested at the beginning of year 3. Maximum investment: 100,000 yuan. Returns 140% of the investment amount (principal + 40% profit) at the end of year 3.

**Cash flow mechanics:**
- At the beginning of each year, you can split available cash across multiple projects.
- Interest/returns received at the end of a year can be reinvested at the beginning of the next year.
- Leftover cash at the end of year 3 counts toward the final total with no penalty.
- No minimum investment amounts.
- At most one investment in project 1 per year.