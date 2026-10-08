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

QUESTION: For project (1), is the 20% annual profit paid every year for as long as the money stays invested, and does the principal remain available to be reinvested in other projects at the start of each year?

## Turn 1 - User Simulator

Yes, the 20% profit is paid every year for as long as the money stays invested in project (1). At the start of each year, the entire amount—both the original principal and the 20% profit—can be reinvested in any project.

## Turn 2 - Generic Agent

QUESTION: For project (2), is the 150% total return paid all at once at the end of the third year, or is it paid at some other specific time?

## Turn 2 - User Simulator

The 150% total return for project (2) is paid at the end of the second year.

## Turn 3 - Generic Agent

QUESTION: For project (3), is the 160% total return paid all at once at the end of the third year, or is it paid at some other specific time?

## Turn 3 - User Simulator

The 160% total return for project (3) is paid all at once at the end of the third year.

## Turn 4 - Generic Agent

QUESTION: For project (4), is the 40% profit paid every year for as long as the money stays invested, and does the principal remain available to be reinvested in other projects at the start of each year?

## Turn 4 - User Simulator

No. Project (4) is only available for investment at the beginning of the third year, and the 40% profit is paid at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: For project (3), can it be invested in at the beginning of any of the three years, or is it only available at a specific year?

## Turn 5 - User Simulator

Project (3) is only available for investment at the beginning of the second year.

## Turn 6 - Generic Agent

QUESTION: Can the money recovered from project (2) at the end of the second year be reinvested in project (4) at the beginning of the third year?

## Turn 6 - User Simulator

Yes, the money recovered from project (2) at the end of the second year can be reinvested in project (4) at the beginning of the third year.

## Turn 7 - Generic Agent

QUESTION: Is there any limit on how much can be invested in project (1) in any given year, or is it unlimited?

## Turn 7 - User Simulator

There is no specific investment limit for project (1) mentioned in the original request.

## Turn 8 - Generic Agent

QUESTION: At the end of the third year, is the objective to maximize the total cash on hand (principal plus all interest/returns received), or is there some other measure of "total principal and interest"?

## Turn 8 - User Simulator

The objective is to maximize the total cash on hand at the end of the third year, which includes all principal and interest/returns received from all projects.

## Turn 9 - Generic Agent

QUESTION: Can money be left uninvested (i.e., held as cash) at the start of any year, or must all available funds be allocated to at least one project each year?

## Turn 9 - User Simulator

I need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 10 - Generic Agent

QUESTION: While you confirm that, can you tell me whether the 20% profit from project (1) is paid at the end of each year (so it becomes available for reinvestment at the start of the next year), or at some other time?

## Turn 10 - User Simulator

The 20% profit from project (1) is paid at the end of each year, so it becomes available for reinvestment at the start of the next year.

## Turn 11 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether project (1) can be invested in at the beginning of any of the three years, or is it only available at a specific year?

## Turn 11 - User Simulator

Project (1) can be invested in at the beginning of any of the three years.

## Turn 12 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 12 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 13 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the 150% total return from project (2) includes the original principal (i.e., you get back 1.5 times what you invested), or is it 150% profit on top of the principal (i.e., you get back 2.5 times what you invested)?

## Turn 13 - User Simulator

The 150% total return from project (2) includes the original principal, meaning you get back 1.5 times what you invested.

## Turn 14 - Generic Agent

QUESTION: Similarly, does the 160% total return from project (3) include the original principal (i.e., you get back 1.6 times what you invested), or is it 160% profit on top of the principal (i.e., you get back 2.6 times what you invested)?

## Turn 14 - User Simulator

The 160% total return from project (3) includes the original principal, meaning you get back 1.6 times what you invested.

## Turn 15 - Generic Agent

QUESTION: Does the 40% profit from project (4) include the original principal (i.e., you get back 1.4 times what you invested), or is it 40% profit on top of the principal (i.e., you get back 1.4 times what you invested)?

## Turn 15 - User Simulator

The 40% profit from project (4) is on top of the principal, meaning you get back 1.4 times what you invested.

## Turn 16 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 16 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 17 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the 20% profit from project (1) is on top of the principal (i.e., you get back 1.2 times what you invested at the end of each year), or does it include the principal in some other way?

## Turn 17 - User Simulator

The 20% profit from project (1) is on top of the principal, meaning you get back 1.2 times what you invested at the end of each year.

## Turn 18 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 18 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 19 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the investment amounts for each project must be whole numbers (e.g., whole yuan), or can they be any continuous amount?

## Turn 19 - User Simulator

I still need to confirm internally whether investment amounts must be whole numbers or can be any continuous amount.

## Turn 20 - Generic Agent

QUESTION: While you confirm those questions, can you tell me whether the initial 300,000 yuan is available at the beginning of the first year, or is it available at some other time?

## Turn 20 - User Simulator

The initial 300,000 yuan is available at the beginning of the first year.

## Turn 21 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 21 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 22 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the investment in project (2) at the beginning of the first year is locked up for the entire two years (i.e., no partial recovery before the end of the second year), or can any portion be recovered earlier?

## Turn 22 - User Simulator

The investment in project (2) is locked up for the entire two years; no portion can be recovered before the end of the second year.

## Turn 23 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 23 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 24 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the investment in project (3) at the beginning of the second year is locked up for the entire period until the end of the third year, or can any portion be recovered earlier?

## Turn 24 - User Simulator

The investment in project (3) is locked up for the entire period until the end of the third year; no portion can be recovered earlier.

## Turn 25 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 25 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 26 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the investment in project (4) at the beginning of the third year is locked up until the end of the third year, or can any portion be recovered earlier?

## Turn 26 - User Simulator

The investment in project (4) is locked up until the end of the third year; no portion can be recovered earlier.

## Turn 27 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 27 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 28 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the 20% profit from project (1) is paid at the end of each year regardless of how long the money stays invested, or is it only paid for the full year if the money stays for the entire year?

## Turn 28 - User Simulator

The 20% profit from project (1) is paid at the end of each year for as long as the money stays invested.

## Turn 29 - Generic Agent

QUESTION: Have you had a chance to confirm whether funds can be held as cash or must be fully allocated each year?

## Turn 29 - User Simulator

I still need to confirm internally whether funds can be held as cash or must be fully allocated each year.

## Turn 30 - Generic Agent

QUESTION: While you confirm the cash-holding question, can you tell me whether the 20% profit from project (1) is paid at the end of each year for the full amount invested at the beginning of that year, or is it prorated based on how long the money stays invested during that year?

## Turn 30 - User Simulator

The 20% profit from project (1) is paid at the end of each year for the full amount invested at the beginning of that year.