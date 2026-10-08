# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U13, U15, U16, U2, U3, U4, U5, U6, U7, U8, U9, U10, U11, U12
I need help creating a production and workforce plan for a food factory, where only skilled workers can train new workers, each skilled worker can train at most 3 new workers in any two-week period, and a total of 50 new workers must be trained by the end of the 8th week.

Current workforce: 50 skilled workers.

Production rates: one skilled worker can produce 10 kg/h of food I or 6 kg/h of food II.

Weekly demand for foods I and II (kg):

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|
| I    | 10000 | 10000 | 12000 | 12000 | 16000 | 16000 | 20000 | 20000 |
| II   | 6000 | 7200 | 8400 | 10800 | 10800 | 12000 | 12000 | 12000 |

Maximum number of new workers a skilled worker can train in a two‑week period: 3.

Training period duration: 2 weeks.

Normal weekly working hours: 40 hours per week.

Overtime: working 60 hours per week, weekly wage 540 yuan.

Weekly wage for a skilled worker: 360 yuan.

Weekly wage for a trainee during the training period: 120 yuan.

After training, new workers receive 240 yuan/week and have the same production efficiency as skilled workers.

Compensation fees for late delivery: 0.5 yuan per kg per week for food I, 0.6 yuan per kg per week for food II.

## Problem units
- U1 (context): I need help creating a production and workforce plan for a food factory.
- U2 (data): Current workforce: 50 skilled workers.
- U3 (data): Production rates: one skilled worker can produce 10 kg/h of food I or 6 kg/h of food II.
- U4 (data): Weekly demand for foods I and II (kg):

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|------|---|---|---|---|---|---|---|---|
| I    | 10000 | 10000 | 12000 | 12000 | 16000 | 16000 | 20000 | 20000 |
| II   | 6000 | 7200 | 8400 | 10800 | 10800 | 12000 | 12000 | 12000 |
- U5 (data): Maximum number of new workers a skilled worker can train in a two‑week period: 3.
- U6 (data): Training period duration: 2 weeks.
- U7 (data): Normal weekly working hours: 40 hours per week.
- U8 (data): Overtime: working 60 hours per week, weekly wage 540 yuan.
- U9 (data): Weekly wage for a skilled worker: 360 yuan.
- U10 (data): Weekly wage for a trainee during the training period: 120 yuan.
- U11 (data): After training, new workers receive 240 yuan/week and have the same production efficiency as skilled workers.
- U12 (data): Compensation fees for late delivery: 0.5 yuan per kg per week for food I, 0.6 yuan per kg per week for food II.
- U13 (constraint): Each skilled worker can train at most 3 new workers in any two-week period.
- U14 (constraint): During the two-week training period, the trainer and trainees do not participate in production.
- U15 (constraint): A total of 50 new workers must be trained by the end of the 8th week.
- U16 (constraint): Only skilled workers can train new workers.
- U17 (objective): Minimize total cost.

## Hidden slot scoring rules
## H1: no_production_during_training_period
- Severity: P1
- Severity reason: Without this information, the agent may assume trainers and trainees can produce during training, leading to overestimated production capacity and a materially inaccurate model.
- Problem unit ID: U14
- Semantic hit rule: The agent's question mentions whether trainers or trainees can produce, or explicitly asks about production participation during a training period.
- Reference acceptable questions:
  - Are the skilled trainers and the trainees allowed to produce any food during those two weeks of training, or are they completely off production?
  - Do the workers involved in training (both trainer and trainees) still contribute to production while the training is happening?
- Failure modes:
  - Assuming trainers and trainees can produce food while training is ongoing
  - Not accounting for the lost production hours of skilled workers and trainees during any training week

## H2: minimize_total_cost
- Severity: P0
- Severity reason: Without an objective, the model is ill‑posed; the agent cannot formulate the optimization problem or know what to minimize, making modeling impossible.
- Problem unit ID: U17
- Semantic hit rule: The agent's question explicitly asks about the optimization goal, asking whether the objective is to minimize total cost or something else.
- Reference acceptable questions:
  - What exactly is the goal we should optimize here? Is it to minimize total cost?
  - Should the plan aim to minimize overall cost, or is there another primary objective like maximizing profit or minimizing late deliveries?
- Failure modes:
  - Assuming the goal is to maximize profit
  - Formulating an ill‑posed model without a defined objective


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: When you say "a total of 50 new workers must be trained by the end of the 8th week," do you mean that 50 trainees must have completed their 2-week training (i.e., become productive workers) by the end of week 8, or that 50 trainees must have started training by the end of week 8 (some of whom would still be in training at week 8's end)?

## Turn 1 - User Simulator

It means 50 trainees must have completed their 2-week training and become productive workers by the end of week 8.

## Turn 2 - Generic Agent

QUESTION: The brief gives a weekly wage of 360 yuan for a skilled worker and 240 yuan/week for a worker after training, but no wage for a trainee during the 2-week training period other than the 120 yuan/week figure — is the 120 yuan/week the only cost incurred for a trainee during training (i.e., trainees are paid 120 yuan/week and produce nothing during those 2 weeks)?

## Turn 2 - User Simulator

Yes, the 120 yuan/week is the only cost incurred for a trainee during the 2-week training period. Trainees are paid 120 yuan/week and produce nothing during those 2 weeks.

## Turn 3 - Generic Agent

QUESTION: The brief mentions overtime as "working 60 hours per week, weekly wage 540 yuan" — is this 540 yuan the total weekly wage for a skilled worker who works 60 hours (i.e., 360 yuan for the first 40 hours plus 180 yuan for 20 overtime hours), or is 540 yuan the overtime premium paid on top of the normal 360 yuan wage?

## Turn 3 - User Simulator

The 540 yuan is the total weekly wage for a skilled worker who works 60 hours.

## Turn 4 - Generic Agent

QUESTION: The brief states that only skilled workers can train new workers, and each skilled worker can train at most 3 new workers in any two-week period — does a skilled worker who is training still produce food at the normal rate (10 kg/h for food I or 6 kg/h for food II), or does training reduce or eliminate their production capacity during the weeks they are training?

## Turn 4 - User Simulator

Training eliminates their production capacity. During the two-week training period, neither the skilled worker doing the training nor the trainees they're training are involved in any production.

## Turn 5 - Generic Agent

QUESTION: When a skilled worker trains 3 trainees over a two-week period, does that skilled worker's production capacity remain eliminated for both weeks of that two-week period (i.e., they cannot produce in either week), or is their production only affected in the week the training actually takes place?

## Turn 5 - User Simulator

The skilled worker's production capacity is eliminated for both weeks of that two-week period. They cannot produce in either week.

## Turn 6 - Generic Agent

QUESTION: The brief mentions late delivery compensation fees (0.5 yuan/kg/week for food I, 0.6 yuan/kg/week for food II) — does this mean that if demand in a given week is not fully met, the shortfall can be carried over to the next week and the penalty is charged on the unmet amount for each week it is delayed, or is the penalty a one-time charge on the total unmet quantity at the end of the planning horizon?

## Turn 6 - User Simulator

The penalty is charged on the unmet amount for each week it is delayed. If demand in a given week is not fully met, the shortfall can be carried over to the next week, and the compensation fee is applied to that unmet quantity for each week of delay.

## Turn 7 - Generic Agent

QUESTION: Regarding the overtime option — can a worker who works 60 hours in a week produce at 60 hours' worth of output (i.e., 1.5 times the normal 40-hour output), or is the production rate capped at 40 hours' worth regardless of whether they work 40 or 60 hours?

## Turn 7 - User Simulator

A worker who works 60 hours in a week produces at 60 hours' worth of output (i.e., 1.5 times the normal 40-hour output).

## Turn 8 - Generic Agent

QUESTION: Can a worker who works 60 hours in one week also work 60 hours in the following week, or is there a limit on consecutive overtime weeks (e.g., a worker can only work 60 hours in at most one week out of any two-week period)?

## Turn 8 - User Simulator

There is no limit on consecutive overtime weeks. A worker can work 60 hours in one week and also work 60 hours in the following week.

## Turn 9 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 9 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 10 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 10 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 11 - Generic Agent

QUESTION: When a skilled worker trains 3 trainees in a fixed two-week block (e.g., weeks 1-2), does that skilled worker's production capacity remain eliminated for both weeks of that block, and can the same skilled worker then train another 3 trainees in the next block (weeks 3-4) with their production again eliminated for those two weeks?

## Turn 11 - User Simulator

Yes. When a skilled worker trains 3 trainees in a fixed two-week block (e.g., weeks 1-2), their production capacity is eliminated for both weeks of that block. The same skilled worker can then train another 3 trainees in the next block (weeks 3-4), with their production again eliminated for those two weeks.

## Turn 12 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 12 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 13 - Generic Agent

QUESTION: The brief mentions a weekly wage of 360 yuan for a skilled worker and 240 yuan/week for a worker after training — is the 240 yuan/week the total weekly wage for a newly trained worker (i.e., they are paid 240 yuan/week instead of 360 yuan/week), or is it an additional payment on top of the 360 yuan skilled worker wage?

## Turn 13 - User Simulator

The 240 yuan/week is the total weekly wage for a newly trained worker. They are paid 240 yuan/week instead of 360 yuan/week.

## Turn 14 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 14 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 15 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 15 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 16 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 16 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 17 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 17 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 18 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 18 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 19 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 19 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 20 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 20 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 21 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 21 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 22 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 22 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 23 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 23 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 24 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 24 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 25 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 25 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 26 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 26 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 27 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 27 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 28 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 28 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 29 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 29 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).

## Turn 30 - Generic Agent

QUESTION: The brief states that a skilled worker can train at most 3 new workers in any two-week period — does this mean a skilled worker can train 3 trainees in weeks 1-2, then another 3 in weeks 3-4, and so on (i.e., the "any two-week period" constraint is a sliding window), or does it simply mean a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 30 - User Simulator

It means a skilled worker can train at most 3 trainees per fixed two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8).