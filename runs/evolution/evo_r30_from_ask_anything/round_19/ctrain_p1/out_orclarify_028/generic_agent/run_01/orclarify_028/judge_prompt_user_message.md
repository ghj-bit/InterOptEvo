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

QUESTION: Does the 20% annual profit from project (1) get paid out at the end of each year and become available for reinvestment in the following year, or is it only paid at the end of the third year?

## Turn 1 - User Simulator

The 20% annual profit from project (1) is paid out at the end of each year. Both the original investment and the 20% profit become available for reinvestment in the following year.

## Turn 2 - Generic Agent

QUESTION: Is the 150% total return from project (2) paid out at the end of the first year, or is it paid out at the end of the third year?

## Turn 2 - User Simulator

The 150% total return from project (2) is paid out at the end of the second year.

## Turn 3 - Generic Agent

QUESTION: Is the 160% total return from project (3) paid out at the end of the third year, or is it paid out at a different time?

## Turn 3 - User Simulator

The 160% total return from project (3) is paid out at the end of the third year.

## Turn 4 - Generic Agent

QUESTION: Is the 40% profit from project (4) paid out at the end of the third year, or is it paid out at a different time?

## Turn 4 - User Simulator

The 40% profit from project (4) is paid out at the end of the third year.

## Turn 5 - Generic Agent

QUESTION: Can you invest in project (1) at the beginning of each of the three years, or is it restricted to specific years?

## Turn 5 - User Simulator

You can invest in project (1) at the beginning of each of the three years.

## Turn 6 - Generic Agent

QUESTION: Can you invest in project (3) at the beginning of each of the three years, or is it restricted to specific years?

## Turn 6 - User Simulator

You can only invest in project (3) at the beginning of the second year.

## Turn 7 - Generic Agent

QUESTION: Can you invest in project (4) at the beginning of each of the three years, or is it restricted to specific years?

## Turn 7 - User Simulator

You can only invest in project (4) at the beginning of the third year.

## Turn 8 - Generic Agent

QUESTION: Are there any minimum investment amounts required for any of the four projects, or can you invest any amount up to the stated limits?

## Turn 8 - User Simulator

There are no minimum investment amounts required for any of the four projects. You can invest any amount up to the stated limits.

## Turn 9 - Generic Agent

QUESTION: Is the 300,000 yuan initial fund the only source of money available for investment, or can you add external funds during the three-year period?

## Turn 9 - User Simulator

The 300,000 yuan initial fund is the only source of money available for investment.

## Turn 10 - Generic Agent

QUESTION: Are there any other constraints or requirements not yet mentioned, such as mandatory diversification, maximum number of projects active at once, or specific reinvestment rules?

## Turn 10 - User Simulator

No, there are no other constraints or requirements beyond what has already been mentioned.

## Turn 11 - Generic Agent

READY_TO_MODEL

**Confirmed Understanding:**

1.  **Objective:** Maximize the total principal and interest available at the end of Year 3.
2.  **Initial Capital:** 300,000 yuan available at the beginning of Year 1. No external funds can be added.
3.  **Time Horizon:** 3 years.
4.  **Decision Variables:** Amount invested in each project at the allowed times. Investments are continuous (any amount up to the limit).
5.  **Project Details:**
    *   **Project 1:**
        *   **Timing:** Can invest at the beginning of Year 1, Year 2, and Year 3.
        *   **Return:** 20% annual profit.
        *   **Cash Flow:** Principal + 20% profit is paid out at the end of each year and becomes available for reinvestment in the following year.
    *   **Project 2:**
        *   **Timing:** Can only invest at the beginning of Year 1.
        *   **Limit:** Maximum 150,000 yuan.
        *   **Return:** 150% total return.
        *   **Cash Flow:** The 150% total return (interpreted as 150% of the investment amount, i.e., 1.5x principal) is paid out at the end of Year 2.
    *   **Project 3:**
        *   **Timing:** Can only invest at the beginning of Year 2.
        *   **Limit:** Maximum 200,000 yuan.
        *   **Return:** 160% total return.
        *   **Cash Flow:** The 160% total return (interpreted as 160% of the investment amount, i.e., 1.6x principal) is paid out at the end of Year 3.
    *   **Project 4:**
        *   **Timing:** Can only invest at the beginning of Year 3.
        *   **Limit:** Maximum 100,000 yuan.
        *   **Return:** 40% profit.
        *   **Cash Flow:** Principal + 40% profit is paid out at the end of Year 3.
6.  **Constraints:**
    *   No minimum investment amounts.
    *   No other constraints (e.g., diversification, exclusivity).
    *   Funds must be non-negative at all times.
    *   Cash flow balance: Money available at the start of a year = Previous year's ending cash + Returns from projects maturing at the end of the previous year. Money invested at the start of a year cannot exceed the available cash.

**Assumptions:**
*   "Total return of 150%" for Project 2 means the investor receives 1.5 times the invested amount (principal + 50% profit).
*   "Total return of 160%" for Project 3 means the investor receives 1.6 times the invested amount (principal + 60% profit).
*   "Profit of 40%" for Project 4 means the investor receives 1.4 times the invested amount (principal + 40% profit).
*   "Annual profit of 20%" for Project 1 means the investor receives 1.2 times the invested amount at the end of each year it is held.