# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U3, U5, U8, U9, U2
I need help creating a weekly production plan for two types of microcomputers in a factory, where both types require the same two production processes. The goal is to maximize total weekly profit, subject to at least 10 units of Model A being produced per week and the weekly production time for Process II being fully utilized, with potential overtime if necessary.

| Process | Model A (hours/unit) | Model B (hours/unit) | Maximum Weekly Processing Capacity (hours) |
| :---: | :---: | :---: | :---: |
| I | 4 | 6 | 150 |
| II | 3 | 2 | 70 |
| Profit ($ per unit) | 300 | 450 |  |

## Problem units
- U1 (context): I need help creating a weekly production plan for two types of microcomputers in a factory.
- U2 (data): | Process | Model A (hours/unit) | Model B (hours/unit) | Maximum Weekly Processing Capacity (hours) |
| :---: | :---: | :---: | :---: |
| I | 4 | 6 | 150 |
| II | 3 | 2 | 70 |
| Profit ($ per unit) | 300 | 450 |  |
- U3 (objective): Maximize total weekly profit.
- U4 (constraint): Total weekly profit must be at least $10,000.
- U5 (constraint): At least 10 units of Model A must be produced per week.
- U6 (constraint): At least 15 units of Model B must be produced per week.
- U7 (constraint): The weekly production time for Process I must be exactly 150 hours.
- U8 (constraint): The weekly production time for Process II should be fully utilized, with potential overtime if necessary.
- U9 (assumption): Both types of microcomputers require the same two production processes.

## Hidden slot scoring rules
## H1: minimum_profit_target
- Severity: P2
- Severity reason: The omission leaves the model as a still‑coherent pure profit maximization problem; the lower bound is a business target, not a structural necessity.
- Problem unit ID: U4
- Semantic hit rule: The Agent’s question must explicitly ask about a minimum profit requirement or a lower bound of $10,000 on weekly profit.
- Reference acceptable questions:
  - Is there a requirement that the total weekly profit must be at least $10,000?
  - Do we have a minimum profit target of $10,000 per week that must be met?
- Failure modes:
  - Assuming no minimum profit constraint is required
  - Assuming the objective is only to maximize profit without a lower bound

## H2: min_production_model_B
- Severity: P2
- Severity reason: Without this detail the model remains a valid production planning problem; the minimum quantity for Model B is a contractual preference, not a formulation‑critical gap.
- Problem unit ID: U6
- Semantic hit rule: The Agent’s question must ask about the minimum production quantity of Model B, specifically at least 15 units per week.
- Reference acceptable questions:
  - Do we have to produce at least 15 units of Model B every week?
  - Is there a contractual requirement for a minimum of 15 units of Model B per week?
- Failure modes:
  - Assuming that there is no minimum production requirement for Model B
  - Forgetting the contractual obligation for Model B

## H3: exact_process_I_time
- Severity: P2
- Severity reason: The model still works with a ≤150 capacity constraint; the exact‑150 requirement is an extra operational target, not a fatal modeling defect.
- Problem unit ID: U7
- Semantic hit rule: The Agent’s question must ask whether Process I time must be exactly 150 hours (i.e., an equality), not merely a capacity upper bound.
- Reference acceptable questions:
  - Must we use exactly 150 hours of Process I each week, not just up to 150?
  - Is it a hard requirement that Process I time equals 150 hours every week?
- Failure modes:
  - Assuming that Process I time is limited to at most 150 hours, not exactly 150
  - Treating the requirement as a simple capacity constraint


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When you say Process II must be "fully utilized, with potential overtime if necessary," do you mean (1) the base 70 hours must be used exactly and any extra hours beyond 70 are allowed at an overtime cost that reduces profit, (2) the 70 hours is a hard minimum that must be met but no overtime is allowed (so Process II is simply a ≥70 constraint), or (3) the 70 hours is a hard maximum and "fully utilized" just means we should expect it to bind at the optimum?

## Turn 1 - User Simulator

It is option (1). The base 70 hours must be used exactly, and any extra hours beyond 70 are allowed at an overtime cost that reduces profit.

## Turn 2 - Generic Agent

QUESTION: For the overtime on Process II, is the overtime cost a fixed dollar amount per extra hour (for example, $X per hour over 70), and if so, what is that rate?

## Turn 2 - User Simulator

The overtime cost is a fixed dollar amount per extra hour. The rate is $50 per hour over 70.

## Turn 3 - Generic Agent

QUESTION: Is there any limit on how many overtime hours can be used on Process II per week (for example, a maximum of X overtime hours), or can overtime be used without bound as long as the $50/hour cost is paid?

## Turn 3 - User Simulator

There is a limit. The maximum overtime hours allowed on Process II per week is 20 hours.

## Turn 4 - Generic Agent

QUESTION: Is the "at least 10 units of Model A per week" requirement a hard constraint that must always be satisfied, or is it a target that can be relaxed (for example, by paying a penalty) if doing so would increase total profit?

## Turn 4 - User Simulator

It is a hard constraint that must always be satisfied.

## Turn 5 - Generic Agent

QUESTION: Are the weekly production quantities of Model A and Model B required to be whole numbers (integer units), or can they be treated as continuous values (allowing fractional units)?

## Turn 5 - User Simulator

The weekly production quantities of Model A and Model B are required to be whole numbers (integer units).

## Turn 6 - Generic Agent

QUESTION: For Process I, is the 150-hour capacity a hard maximum that cannot be exceeded (no overtime allowed on Process I), or can Process I also use overtime beyond 150 hours at some cost?

## Turn 6 - User Simulator

The 150-hour capacity for Process I is a hard maximum that cannot be exceeded. No overtime is allowed on Process I.

## Turn 7 - Generic Agent

QUESTION: Is there any upper limit on the total weekly production of Model B (for example, a maximum number of Model B units that can be produced per week), or is Model B only limited by the process capacities?

## Turn 7 - User Simulator

There is no upper limit on the total weekly production of Model B. It is only limited by the process capacities.

## Turn 8 - Generic Agent

QUESTION: Is there any upper limit on the total weekly production of Model A (for example, a maximum number of Model A units that can be produced per week), or is Model A only limited by the process capacities and the minimum of 10 units?

## Turn 8 - User Simulator

There is no upper limit on the total weekly production of Model A. It is only limited by the process capacities and the minimum of 10 units.

## Turn 9 - Generic Agent

QUESTION: Regarding the "base 70 hours must be used exactly" requirement for Process II: if the optimal production plan would naturally use fewer than 70 hours on Process II, is the factory required to produce extra units (of either model) specifically to fill up to 70 hours, even if that extra production reduces total profit?

## Turn 9 - User Simulator

Yes, the factory is required to produce extra units (of either model) specifically to fill up to 70 hours, even if that extra production reduces total profit.

## Turn 10 - Generic Agent

QUESTION: When the factory produces extra units just to fill the 70-hour minimum on Process II, are those extra units still sold at the normal profit (i.e., they contribute their full $300 or $450 profit), or are they produced at a loss / with no profit contribution?

## Turn 10 - User Simulator

Those extra units are still sold at the normal profit. They contribute their full $300 or $450 profit.

## Turn 11 - Generic Agent

QUESTION: Is there any other constraint or business rule I should know about that isn't captured in the table or what we've discussed so far (for example, a minimum production requirement for Model B, a maximum total number of units of both models combined, or a requirement that both models must be produced every week)?

## Turn 11 - User Simulator

Yes, there is a contractual requirement to produce at least 15 units of Model B each week.

## Turn 12 - Generic Agent

QUESTION: Is the "at least 15 units of Model B per week" requirement a hard constraint that must always be satisfied, or is it a target that can be relaxed (for example, by paying a penalty) if doing so would increase total profit?

## Turn 12 - User Simulator

It is a hard constraint that must always be satisfied.

## Turn 13 - Generic Agent

QUESTION: Is there any requirement that both Model A and Model B must be produced in positive quantities every week (i.e., at least 1 unit of each), or is it acceptable for one of the models to have zero production in a given week as long as all other constraints are satisfied?

## Turn 13 - User Simulator

It is acceptable for one of the models to have zero production in a given week as long as all other constraints are satisfied.

## Turn 14 - Generic Agent

QUESTION: Are there any other constraints, costs, or business rules I should know about that we haven't covered yet (for example, setup costs, demand limits, or a maximum total number of units of both models combined)?

## Turn 14 - User Simulator

No, there are no other constraints, costs, or business rules beyond what we have discussed.

## Turn 15 - Generic Agent

READY_TO_MODEL

Here is my confirmed understanding of the weekly production planning problem:

**Decision variables:**
- x_A = number of Model A units produced per week (integer, ≥ 0)
- x_B = number of Model B units produced per week (integer, ≥ 0)
- OT = overtime hours used on Process II (continuous, ≥ 0)

**Objective:** Maximize total weekly profit
- Profit = 300·x_A + 450·x_B − 50·OT

**Constraints:**

1. **Process I capacity (hard max, no overtime):**
   4·x_A + 6·x_B ≤ 150

2. **Process II base hours must be used exactly (minimum 70 hours):**
   3·x_A + 2·x_B ≥ 70

3. **Process II overtime definition:**
   OT = max(0, 3·x_A + 2·x_B − 70)
   (i.e., OT ≥ 3·x_A + 2·x_B − 70, and OT ≥ 0)

4. **Process II overtime cap:**
   OT ≤ 20

5. **Minimum Model A production (hard):**
   x_A ≥ 10

6. **Minimum Model B production (hard, contractual):**
   x_B ≥ 15

7. **Integrality:**
   x_A and x_B are non-negative integers; OT is continuous.

**Notes confirmed:**
- No upper bound on x_A or x_B beyond the process capacities.
- No overtime allowed on Process I.
- Extra units produced to meet the 70-hour minimum still earn full profit.
- No setup costs, demand limits, or other hidden rules.
- It is acceptable for one model to have zero production in a given week (though the minimums of 10 and 15 make this moot in practice).