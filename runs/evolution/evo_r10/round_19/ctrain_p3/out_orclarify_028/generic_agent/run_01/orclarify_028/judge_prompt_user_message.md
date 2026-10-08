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

QUESTION: For project (1), is the 20% annual profit paid each year for as long as the money stays invested, and can you invest in or withdraw from project (1) at the beginning of any of the three years?

## Turn 1 - User Simulator

Yes, the 20% profit is paid each year for as long as the money stays invested in project (1). And yes, you can invest in project (1) at the beginning of any of the three years.

## Turn 2 - Generic Agent

QUESTION: For project (2), when you say the total return is 150% of the investment amount, do you mean the project pays back 150% of the amount invested (i.e., 1.5 times the principal) at the end of the third year, or that it pays 150% profit on top of the principal (i.e., 2.5 times the principal) at the end of the third year?

## Turn 2 - User Simulator

The total return of 150% means the project pays back 1.5 times the principal at the end of the second year. It is not 150% profit on top of the principal.

## Turn 3 - Generic Agent

QUESTION: For project (3), when you say the total return is 160% of the investment amount and it can be recovered at the end of the third year, do you mean the project pays back 1.6 times the principal at the end of the third year, or that it pays 160% profit on top of the principal (i.e., 2.6 times the principal) at the end of the third year?

## Turn 3 - User Simulator

The total return of 160% means the project pays back 1.6 times the principal at the end of the third year.

## Turn 4 - Generic Agent

QUESTION: For project (4), when you say the profit is 40% of the investment amount and it can be recovered at the end of the third year, do you mean the project pays back 1.4 times the principal (principal plus 40% profit) at the end of the third year, or that it pays 40% profit on top of the principal (i.e., 1.4 times the principal) at the end of the third year?

## Turn 4 - User Simulator

The project pays back 1.4 times the principal (principal plus 40% profit) at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: For project (1), when you withdraw money from project (1) at the end of a year, do you get back the original principal plus the 20% profit for that year, or just the 20% profit?

## Turn 5 - User Simulator

You get back the original principal plus the 20% profit for that year.

## Turn 6 - Generic Agent

QUESTION: For project (2), you said it pays back 1.5 times the principal at the end of the second year. Can you invest in project (2) at the beginning of the second year as well, or is it only available at the beginning of the first year?

## Turn 6 - User Simulator

It is only available at the beginning of the first year.

## Turn 7 - Generic Agent

QUESTION: For project (3), can you invest in it at the beginning of any of the three years, or is there a specific year when it becomes available?

## Turn 7 - User Simulator

You can only invest in project (3) at the beginning of the second year.

## Turn 8 - Generic Agent

QUESTION: For project (4), can you invest in it at the beginning of any of the three years, or is there a specific year when it becomes available?

## Turn 8 - User Simulator

You can only invest in project (4) at the beginning of the third year.

## Turn 9 - Generic Agent

QUESTION: At the end of the third year, is the objective to maximize the total cash on hand (including any uninvested funds plus all returns from projects that mature at that time), or is there a different measure of "total principal and interest" you have in mind?

## Turn 9 - User Simulator

The objective is to maximize the total cash on hand at the end of the third year, including any uninvested funds plus all returns from projects that mature at that time.

## Turn 10 - Generic Agent

QUESTION: If you have uninvested cash at the end of any year (i.e., cash that is not put into any project), does it simply carry over to the next year with no interest, or does it earn some return while sitting idle?

## Turn 10 - User Simulator

I don't have a specific fact about whether uninvested cash earns any return while sitting idle. That point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: For project (1), when you invest at the beginning of a year and withdraw at the end of that same year, do you receive the principal plus 20% profit, or is the 20% profit only paid if the money stays invested for a full year and you can only withdraw at the end of a subsequent year?

## Turn 11 - User Simulator

You receive the principal plus 20% profit when you withdraw at the end of the same year you invested.

## Turn 12 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1 and keep the money in project (1) through year 2 and year 3, do you receive 20% profit each year on the original principal, or does the profit compound (i.e., year 2 profit is calculated on principal plus year 1 profit)?

## Turn 12 - User Simulator

The profit compounds. Year 2 profit is calculated on the principal plus year 1 profit.

## Turn 13 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1 and withdraw at the end of year 2, do you receive the original principal plus 20% profit for year 1 plus 20% profit on that accumulated amount for year 2 (i.e., principal × 1.2 × 1.2), or do you receive the original principal plus 20% profit for each of the two years separately (i.e., principal × 1.2 + principal × 0.2)?

## Turn 13 - User Simulator

You receive the original principal plus 20% profit for year 1 plus 20% profit on that accumulated amount for year 2 (i.e., principal × 1.2 × 1.2).

## Turn 14 - Generic Agent

QUESTION: For project (1), can you invest additional money into project (1) at the beginning of year 2 or year 3, on top of money already invested in year 1, or is the investment in project (1) a single lump sum that you either put in or take out as a whole?

## Turn 14 - User Simulator

You can invest additional money into project (1) at the beginning of year 2 or year 3, on top of money already invested in year 1.

## Turn 15 - Generic Agent

QUESTION: For project (1), can you partially withdraw money from project (1) at the end of a year (keeping some in and taking some out), or must you withdraw the entire amount invested in project (1) at once?

## Turn 15 - User Simulator

I don't have a specific fact about whether partial withdrawals from project (1) are allowed. That point still needs internal confirmation.

## Turn 16 - Generic Agent

QUESTION: For project (2), you said it pays back 1.5 times the principal at the end of the second year. Does this mean the money is locked in for exactly two years (invested at the beginning of year 1, recovered at the end of year 2), and the recovered cash is then available for investment in year 3?

## Turn 16 - User Simulator

Yes, the money is locked in for exactly two years: invested at the beginning of year 1 and recovered at the end of year 2. The recovered cash is then available for investment in year 3.

## Turn 17 - Generic Agent

QUESTION: For project (3), you said it pays back 1.6 times the principal at the end of the third year and can only be invested at the beginning of the second year. Does this mean the money is locked in for two years (invested at the beginning of year 2, recovered at the end of year 3)?

## Turn 17 - User Simulator

Yes, the money is locked in for two years: invested at the beginning of year 2 and recovered at the end of year 3.

## Turn 18 - Generic Agent

QUESTION: For project (4), you said it pays back 1.4 times the principal at the end of the third year and can only be invested at the beginning of the third year. Does this mean the money is locked in for one year (invested at the beginning of year 3, recovered at the end of year 3)?

## Turn 18 - User Simulator

Yes, the money is locked in for one year: invested at the beginning of year 3 and recovered at the end of year 3.

## Turn 19 - Generic Agent

QUESTION: Are there any minimum investment amounts for any of the four projects, or can you invest any amount (including zero) up to the stated limits?

## Turn 19 - User Simulator

I don't have a specific fact about minimum investment amounts for any of the four projects. That point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Are the investment amounts for each project required to be whole numbers (e.g., whole yuan), or can they be any continuous amount?

## Turn 20 - User Simulator

I don't have a specific fact about whether investment amounts must be whole numbers or can be any continuous amount. That point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: At the beginning of year 1, you have 300,000 yuan. Can you split this initial fund across multiple projects (e.g., some into project 1, some into project 2), or must you allocate the entire 300,000 to a single project?

## Turn 21 - User Simulator

You can split the initial fund across multiple projects.

## Turn 22 - Generic Agent

QUESTION: At the beginning of year 2, the cash available for investment includes any uninvested cash from year 1 plus any returns from projects that mature at the end of year 1. Is this correct, or are there other sources of cash at the beginning of year 2?

## Turn 22 - User Simulator

Yes, that is correct. At the beginning of year 2, the cash available for investment includes any uninvested cash from year 1 plus any returns from projects that mature at the end of year 1.

## Turn 23 - Generic Agent

QUESTION: At the beginning of year 3, the cash available for investment includes any uninvested cash from year 2 plus the return from project (2) (1.5 times its principal) plus any returns from projects that mature at the end of year 2. Is this correct, or are there other sources of cash at the beginning of year 3?

## Turn 23 - User Simulator

Yes, that is correct. At the beginning of year 3, the cash available for investment includes any uninvested cash from year 2 plus the return from project (2) (1.5 times its principal) plus any returns from projects that mature at the end of year 2.

## Turn 24 - Generic Agent

QUESTION: At the end of year 3, the total cash on hand includes any uninvested cash from year 3 plus the return from project (3) (1.6 times its principal) plus the return from project (4) (1.4 times its principal) plus any returns from project (1) that mature at the end of year 3. Is this correct, or are there other sources of cash at the end of year 3?

## Turn 24 - User Simulator

Yes, that is correct. At the end of year 3, the total cash on hand includes any uninvested cash from year 3 plus the return from project (3) (1.6 times its principal) plus the return from project (4) (1.4 times its principal) plus any returns from project (1) that mature at the end of year 3.

## Turn 25 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1 and keep it in through year 3, the amount recovered at the end of year 3 is principal × 1.2 × 1.2 × 1.2. If you also invest additional money at the beginning of year 2, does that additional money also compound at 20% per year for the remaining years it stays in project (1)?

## Turn 25 - User Simulator

Yes, the additional money invested at the beginning of year 2 also compounds at 20% per year for the remaining years it stays in project (1).

## Turn 26 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1 and withdraw at the end of year 1, and then reinvest the recovered amount (principal plus 20% profit) back into project (1) at the beginning of year 2, does the year 2 profit compound on the full recovered amount (i.e., principal × 1.2 × 1.2)?

## Turn 26 - User Simulator

Yes, the year 2 profit compounds on the full recovered amount (i.e., principal × 1.2 × 1.2).

## Turn 27 - Generic Agent

QUESTION: For project (1), is there any limit on the total amount you can invest in it across the three years, or is the only constraint the cash available at the beginning of each year?

## Turn 27 - User Simulator

I don't have a specific fact about a total investment limit for project (1) across the three years. That point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1 and withdraw at the end of year 2, the amount recovered is principal × 1.2 × 1.2. If you then reinvest that recovered amount back into project (1) at the beginning of year 3, does the year 3 profit compound on the full recovered amount (i.e., principal × 1.2 × 1.2 × 1.2)?

## Turn 28 - User Simulator

Yes, the year 3 profit compounds on the full recovered amount (i.e., principal × 1.2 × 1.2 × 1.2).

## Turn 29 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 1 and keep it in through year 3 without any intermediate withdrawals, the amount recovered at the end of year 3 is principal × 1.2 × 1.2 × 1.2. Is this correct, or is there a different compounding convention for money that stays continuously in project (1)?

## Turn 29 - User Simulator

Yes, that is correct. If you invest at the beginning of year 1 and keep it in through year 3 without any intermediate withdrawals, the amount recovered at the end of year 3 is principal × 1.2 × 1.2 × 1.2.

## Turn 30 - Generic Agent

QUESTION: For project (1), if you invest at the beginning of year 2 and keep it in through year 3, the amount recovered at the end of year 3 is principal × 1.2 × 1.2. Is this correct?

## Turn 30 - User Simulator

Yes, that is correct.