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

QUESTION: For project (1), is the 20% annual profit paid out at the end of each year while the principal remains available for reinvestment, or is the principal locked in and only the total accumulated amount returned at the end of the third year?

## Turn 1 - User Simulator

The 20% annual profit is paid out at the end of each year, and the entire amount—both your original investment and the 20% profit—can be reinvested in any project the next year.

## Turn 2 - Generic Agent

QUESTION: For project (2), does the "total return of 150%" mean that at the end of the third year you receive back 150% of the original investment amount (i.e., a 50% net gain), or does it mean you receive back 250% of the original investment amount (i.e., a 150% net gain)?

## Turn 2 - User Simulator

The "total return of 150%" means you receive back 150% of the original investment amount, which is a 50% net gain.

## Turn 3 - Generic Agent

QUESTION: For project (3), does the "total return of 160%" mean that at the end of the third year you receive back 160% of the original investment amount (i.e., a 60% net gain)?

## Turn 3 - User Simulator

Yes, the "total return of 160%" means you receive back 160% of the original investment amount, which is a 60% net gain.

## Turn 4 - Generic Agent

QUESTION: For project (4), is the "profit of 40%" a net gain on top of the principal, meaning you receive back 140% of the original investment amount at the end of the third year?

## Turn 4 - User Simulator

Yes, the "profit of 40%" is a net gain on top of the principal, meaning you receive back 140% of the original investment amount at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: For project (1), is the investment amount allowed to vary from year to year, meaning you can choose a different amount to invest in project (1) at the beginning of each of the three years?

## Turn 5 - User Simulator

Yes, you can choose a different amount to invest in project (1) at the beginning of each of the three years.

## Turn 6 - Generic Agent

QUESTION: For projects (3) and (4), can you invest in them at the beginning of any of the three years, or are they only allowed at the beginning of the first year like project (2)?

## Turn 6 - User Simulator

No, they are not allowed at the beginning of the first year. You can only invest in project (3) at the beginning of the second year, and you can only invest in project (4) at the beginning of the third year.

## Turn 7 - Generic Agent

QUESTION: Are there any other constraints or requirements not mentioned in the brief, such as minimum investment amounts for any project, restrictions on splitting funds across multiple projects in the same year, or requirements to maintain a cash reserve?

## Turn 7 - User Simulator

No, there are no other constraints or requirements not mentioned in the brief.

## Turn 8 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total cash available (principal + interest) at the end of Year 3.
2.  **Initial Fund:** 300,000 yuan available at the beginning of Year 1.
3.  **Time Horizon:** 3 years.
4.  **Decision Variables:**
    *   $x_{1,t}$: Amount invested in Project 1 at the beginning of year $t$ (for $t=1, 2, 3$).
    *   $x_{2,1}$: Amount invested in Project 2 at the beginning of Year 1.
    *   $x_{3,2}$: Amount invested in Project 3 at the beginning of Year 2.
    *   $x_{4,3}$: Amount invested in Project 4 at the beginning of Year 3.
    *   $C_t$: Cash available at the beginning of year $t$ (before investment).
5.  **Project Details & Returns:**
    *   **Project 1:**
        *   Available: Beginning of Years 1, 2, and 3.
        *   Return: 20% annual profit paid at the end of each year.
        *   Cash Flow: If you invest $x_{1,t}$ at the start of year $t$, you receive $1.20 \times x_{1,t}$ at the end of year $t$ (which becomes part of the cash available at the start of year $t+1$).
    *   **Project 2:**
        *   Available: Beginning of Year 1 only.
        *   Limit: $x_{2,1} \le 150,000$.
        *   Return: Total return of 150% of investment at the end of Year 3.
        *   Cash Flow: If you invest $x_{2,1}$ at the start of Year 1, you receive $1.50 \times x_{2,1}$ at the end of Year 3.
    *   **Project 3:**
        *   Available: Beginning of Year 2 only.
        *   Limit: $x_{3,2} \le 200,000$.
        *   Return: Total return of 160% of investment at the end of Year 3.
        *   Cash Flow: If you invest $x_{3,2}$ at the start of Year 2, you receive $1.60 \times x_{3,2}$ at the end of Year 3.
    *   **Project 4:**
        *   Available: Beginning of Year 3 only.
        *   Limit: $x_{4,3} \le 100,000$.
        *   Return: Total return of 140% of investment (40% profit) at the end of Year 3.
        *   Cash Flow: If you invest $x_{4,3}$ at the start of Year 3, you receive $1.40 \times x_{4,3}$ at the end of Year 3.
6.  **Cash Flow Constraints (Balance Equations):**
    *   **Year 1:**
        *   Cash Available: $C_1 = 300,000$.
        *   Investments: $x_{1,1} + x_{2,1} \le C_1$.
        *   Cash carried to Year 2: $C_2 = C_1 - x_{1,1} - x_{2,1} + 1.20 x_{1,1}$. (Note: Project 2 yields nothing until Year 3).
    *   **Year 2:**
        *   Cash Available: $C_2$.
        *   Investments: $x_{1,2} + x_{3,2} \le C_2$.
        *   Cash carried to Year 3: $C_3 = C_2 - x_{1,2} - x_{3,2} + 1.20 x_{1,2}$. (Note: Project 3 yields nothing until Year 3).
    *   **Year 3:**
        *   Cash Available: $C_3$.
        *   Investments: $x_{1,3} + x_{4,3} \le C_3$.
        *   Final Wealth: $W = C_3 - x_{1,3} - x_{4,3} + 1.20 x_{1,3} + 1.50 x_{2,1} + 1.60 x_{3,2} + 1.40 x_{4,3}$.
7.  **Constraints:**
    *   $x_{2,1} \le 150,000$
    *   $x_{3,2} \le 200,000$
    *   $x_{4,3} \le 100,000$
    *   All investment variables $\ge 0$.
    *   No minimum investment amounts.
    *   No other constraints.