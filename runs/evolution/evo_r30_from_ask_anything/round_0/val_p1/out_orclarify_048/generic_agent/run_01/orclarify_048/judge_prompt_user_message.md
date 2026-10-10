# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U4, U7, U8, U2, U3
I need help creating a production plan for two microcomputer models, A and B, where the total weekly profit must be at least 10,000 yuan, the processing time for Process I must be exactly 150 hours per week, and the regular processing time for Process II must not exceed its maximum weekly capacity of 70 hours.

| Process | Model A | Model B | Maximum Weekly Processing Capacity |
|---------|---------|---------|------------------------------------|
| I (hours/unit) | 4 | 6 | 150 |
| II (hours/unit) | 3 | 2 | 70 |
| Profit (yuan/unit) | 300 | 450 | |

Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan.

## Problem units
- U1 (context): I need help creating a production plan for two microcomputer models, A and B.
- U2 (data): | Process | Model A | Model B | Maximum Weekly Processing Capacity |
|---------|---------|---------|------------------------------------|
| I (hours/unit) | 4 | 6 | 150 |
| II (hours/unit) | 3 | 2 | 70 |
| Profit (yuan/unit) | 300 | 450 | |
- U3 (data): Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan.
- U4 (constraint): Total weekly profit must be at least 10,000 yuan.
- U5 (constraint): At least 10 units of model A must be produced each week.
- U6 (constraint): At least 15 units of model B must be produced each week.
- U7 (constraint): The processing time for Process I must be exactly 150 hours per week.
- U8 (constraint): The regular processing time for Process II must not exceed its maximum weekly capacity of 70 hours.
- U9 (constraint): The overtime processing for Process II must not exceed 30 hours per week.

## Hidden slot scoring rules
## H1: min_weekly_production_A
- Severity: P1
- Severity reason: Without this constraint, the model could produce fewer than 10 units of model A, violating a contractual obligation and making the solution business-invalid.
- Problem unit ID: U5
- Semantic hit rule: The Agent's question must inquire about a minimum or lower bound on the weekly production quantity of model A, or ask if there is any requirement to produce at least a certain number of A.
- Reference acceptable questions:
  - What is the minimum number of model A microcomputers we must produce each week?
  - Are there any minimum production requirements for model A?
- Failure modes:
  - Assuming no minimum production requirement for model A (production can be zero)
  - Assuming a different arbitrary lower bound

## H2: min_weekly_production_B
- Severity: P1
- Severity reason: Missing this constraint would allow the model to produce fewer than 15 units of model B, violating a contract and leading to a business-invalid solution.
- Problem unit ID: U6
- Semantic hit rule: The Agent's question asks for the minimum required weekly output of model B or whether there is a lower bound on B production.
- Reference acceptable questions:
  - How many model B microcomputers do we need to produce at minimum each week?
  - Is there a lower bound on the weekly production of model B?
- Failure modes:
  - Assuming no minimum production requirement for model B
  - Assuming an incorrect lower limit for B

## H3: max_overtime_process_II
- Severity: P1
- Severity reason: Without this limit, the model could treat overtime as unbounded, which would completely distort the feasible region and profit calculations, or could omit overtime entirely.
- Problem unit ID: U9
- Semantic hit rule: The Agent's question must explicitly ask for the upper limit or cap on overtime hours for Process II.
- Reference acceptable questions:
  - What is the maximum allowed overtime for Process II?
  - How many hours of overtime per week are permitted for Process II?
- Failure modes:
  - Assuming unlimited overtime for Process II
  - Assuming no overtime is allowed for Process II
  - Assuming a different arbitrary overtime cap


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Is the 150-hour limit for Process I a strict equality constraint (meaning you must use exactly 150 hours) or is it a maximum capacity constraint (meaning you can use up to 150 hours)?

## Turn 1 - User Simulator

It is a strict equality constraint. The processing time for Process I must be exactly 150 hours per week.

## Turn 2 - Generic Agent

QUESTION: When the regular 70-hour capacity of Process II is exceeded, is there a maximum limit on the total overtime hours allowed per week

## Turn 2 - User Simulator

Yes, the overtime processing for Process II must not exceed 30 hours per week.

## Turn 3 - Generic Agent

QUESTION: Is the total weekly profit target of at least 10,000 yuan a hard constraint that must be met

## Turn 3 - User Simulator

Yes, the total weekly profit must be at least 10,000 yuan.

## Turn 4 - Generic Agent

QUESTION: Are there any minimum production requirements for Model A or Model

## Turn 4 - User Simulator

Yes, we must produce at least 10 units of Model A and at least 15 units of Model B each week.

## Turn 5 - Generic Agent

QUESTION: Are the production quantities for Model A and Model

## Turn 5 - User Simulator

The production quantities for Model A and Model B must be non-negative integers.

## Turn 6 - Generic Agent

QUESTION: Is there a specific objective for the production plan, such as minimizing total production

## Turn 6 - User Simulator

No, there is no specific objective like minimizing total production cost. The goal is to find a feasible production plan that satisfies all the constraints: at least 10,000 yuan profit, exactly 150 hours for Process I, regular Process II time not exceeding 70 hours, overtime Process II not exceeding 30 hours, at least 10 units of Model A, and at least 15 units of Model B.

## Turn 7 - Generic Agent

READY_TO_MODEL
I have confirmed the following understanding of your production planning problem:

**Decision Variables:**
- Let $x_A$ be the number of units of Model A produced per week.
- Let $x_B$ be the number of units of Model B produced per week.
- Both $x_A$ and $x_B$ must be non-negative integers.

**Constraints:**
1. **Process I (Strict Equality):** The total processing time for Process I must be exactly 150 hours.
   - $4x_A + 6x_B = 150$
2. **Process II (Regular + Overtime Capacity):**
   - Regular capacity is 70 hours.
   - Overtime capacity is up to 30 hours.
   - Total available capacity for Process II is $70 + 30 = 100$ hours.
   - The total processing time for Process II must not exceed 100 hours.
   - $3x_A + 2x_B \le 100$
   - *Note: The problem states "regular processing time... must not exceed 70 hours" and "overtime... must not exceed 30 hours". This implies that if the total Process II time exceeds 70, the excess is treated as overtime. The constraint is effectively that the total time used is $\le 100$, and the portion used beyond 70 is the overtime portion which is $\le 30$. Since we are just checking feasibility, the combined constraint $3x_A + 2x_B \le 100$ covers the capacity limit. However, we must also ensure that the "regular" part doesn't exceed 70, which is inherently true if we define overtime as the excess. But wait, the profit calculation depends on how much is regular vs overtime. Let's look at the profit constraint.*
3. **Minimum Production:**
   - $x_A \ge 10$
   - $x_B \ge 15$
4. **Profit Constraint:** The total weekly profit must be at least 10,000 yuan.
   - The profit depends on whether the production falls within regular or overtime hours for Process II.
   - Let $T_{II} = 3x_A + 2x_B$ be the total Process II hours.
   - If $T_{II} \le 70$, all units are produced in regular time.
     - Profit $P = 300x_A + 450x_B$.
   - If $T_{II} > 70$, the first 70 hours are regular, and the remaining $T_{II} - 70$ hours are overtime.
     - The problem states "Profit per unit when produced during overtime in Process II: Model A 280 yuan, Model B 425 yuan."
     - This implies that units produced during overtime hours yield lower profit.
     - We need to determine how many units of A and B are produced in regular vs overtime.
     - Usually, in such linear programming contexts, if the profit per unit changes based on the "mode" of production, we might need to split the variables or assume a specific allocation. However, a common interpretation is that the *total* profit is calculated by assigning the regular hours to the most profitable units first, or simply that the profit per unit is reduced for the portion of production that consumes overtime hours.
     - Let's re-read carefully: "Profit per unit when produced during overtime in Process II". This suggests that if a unit is produced using overtime hours, its profit is lower.
     - To maximize profit (or just check if it's $\ge 10,000$), we would want to assign regular hours to the units with the highest regular profit, or perhaps the problem implies a simpler model where we just calculate the total profit based on the total hours?
     - Actually, a standard interpretation for this type of problem is that we have two "types" of production for each model: Regular and Overtime.
     - Let $x_{A,reg}$ and $x_{A,ot}$ be units of A produced in regular and overtime hours.
     - Let $x_{B,reg}$ and $x_{B,ot}$ be units of B produced in regular and overtime hours.
     - $x_A = x_{A,reg} + x_{A,ot}$
     - $x_B = x_{B,reg} + x_{B,ot}$
     - Regular hours constraint: $3x_{A,reg} + 2x_{B,reg} \le 70$
     - Overtime hours constraint: $3x_{A,ot} + 2x_{B,ot} \le 30$
     - Process I constraint: $4(x_{A,reg} + x_{A,ot}) + 6(x_{B,reg} + x_{B,ot}) = 150$
     - Profit constraint: $300x_{A,reg} + 450x_{B,reg} + 280x_{A,ot} + 425x_{B,ot} \ge 10,000$
     - Minimum production: $x_A \ge 10, x_B \ge 15$
     - All variables are non-negative integers.

This formulation is more complex but accurately reflects the "profit per unit when produced during overtime" statement. I will proceed with this interpretation.