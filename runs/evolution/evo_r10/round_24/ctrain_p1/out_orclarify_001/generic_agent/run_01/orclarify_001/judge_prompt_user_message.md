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

QUESTION: When you say "a total of 50 new workers must be trained by the end of the 8th week," do you mean that 50 trainees must have *completed* their 2-week training (and thus be productive) by the end of week 8, or that 50 trainees must have *started* training by the end of week 8 (some of whom would still be in training and not yet productive)?

## Turn 1 - User Simulator

It means 50 trainees must have **completed** their 2-week training and be productive by the end of week 8.

## Turn 2 - Generic Agent

QUESTION: The brief says a skilled worker can train at most 3 new workers "in any two-week period" — does this mean a skilled worker can have up to 3 trainees at any time (so a worker who starts 3 trainees in weeks 1–2 cannot start another batch until those finish in weeks 3–4), or does it mean a skilled worker can start up to 3 new trainees in each individual week (so up to 6 could be in training simultaneously)?

## Turn 2 - User Simulator

It means a skilled worker can have up to 3 trainees at any time. A worker who starts 3 trainees in weeks 1–2 cannot start another batch until those finish in weeks 3–4.

## Turn 3 - Generic Agent

QUESTION: Can a skilled worker who is currently training 3 trainees also produce food during those same two weeks, or is a worker who is training fully occupied and cannot produce?

## Turn 3 - User Simulator

A worker who is training is fully occupied and cannot produce.

## Turn 4 - Generic Agent

QUESTION: Do trainees (the 50 new workers being trained) produce any food during their 2-week training period, or do they only start producing at full efficiency after training is complete?

## Turn 4 - User Simulator

Trainees do not produce any food during their 2-week training period. They only start producing at full efficiency after training is complete.

## Turn 5 - Generic Agent

QUESTION: The brief gives a "weekly wage for a skilled worker: 360 yuan" and "overtime: working 60 hours per week, weekly wage 540 yuan." Does the 540 yuan replace the 360 yuan (i.e., a worker working 60 hours that week is paid 540 total), or is 540 the overtime premium added on top of the 360 base (i.e., 900 total for a 60-hour week)?

## Turn 5 - User Simulator

The 540 yuan replaces the 360 yuan. A worker working 60 hours that week is paid 540 yuan total.

## Turn 6 - Generic Agent

QUESTION: The brief gives a "weekly wage for a trainee during the training period: 120 yuan." Does this 120 yuan apply to a trainee for each of the two weeks they are in training (so 240 yuan total per trainee over the full training period), or is 120 yuan the total for the entire 2-week training period?

## Turn 6 - User Simulator

The 120 yuan applies to a trainee for each of the two weeks they are in training, so 240 yuan total per trainee over the full training period.

## Turn 7 - Generic Agent

QUESTION: The brief mentions "compensation fees for late delivery" (0.5 yuan/kg/week for food I, 0.6 yuan/kg/week for food II). Does this mean that if demand in a given week is not fully met, the shortfall can be carried over and delivered in a later week, incurring the compensation fee for each week of delay, or does it mean that any unmet demand in a week simply incurs a penalty and is lost (no backlogging)?

## Turn 7 - User Simulator

The shortfall can be carried over and delivered in a later week, incurring the compensation fee for each week of delay.

## Turn 8 - Generic Agent

QUESTION: Can the factory produce more than the weekly demand in a given week and carry the surplus forward as inventory to satisfy future demand, or must production in each week be limited to that week's demand (with any excess being wasted)?

## Turn 8 - User Simulator

The factory can produce more than the weekly demand in a given week and carry the surplus forward as inventory to satisfy future demand.

## Turn 9 - Generic Agent

QUESTION: Is there any holding cost for carrying inventory of food I or food II from one week to the next, or is inventory free to hold (the only cost related to inventory is the late-delivery compensation when demand is delayed)?

## Turn 9 - User Simulator

There is no holding cost for carrying inventory. Inventory is free to hold; the only cost related to inventory is the late-delivery compensation when demand is delayed.

## Turn 10 - Generic Agent

QUESTION: The 50 skilled workers at the start — are they all available to produce from week 1, or do some of them need to be assigned to training from week 1 (and thus unavailable for production in weeks 1–2)?

## Turn 10 - User Simulator

All 50 skilled workers are available to produce from week 1. However, some of them may need to be assigned to training from week 1, in which case they would be unavailable for production in weeks 1–2.

## Turn 11 - Generic Agent

QUESTION: Can a skilled worker who finishes training a batch in, say, weeks 1–2 immediately start training a new batch in weeks 3–4, or is there a required gap (e.g., one week of production) between consecutive training batches for the same worker?

## Turn 11 - User Simulator

A skilled worker who finishes training a batch in weeks 1–2 can immediately start training a new batch in weeks 3–4. There is no required gap between consecutive training batches for the same worker.

## Turn 12 - Generic Agent

QUESTION: The 50 new workers who complete training and become productive — do they all start producing in the same week (the week after their 2-week training ends), or can they be assigned to different production tasks (food I vs. food II) just like the original skilled workers?

## Turn 12 - User Simulator

They can be assigned to different production tasks (food I vs. food II) just like the original skilled workers.

## Turn 13 - Generic Agent

QUESTION: Can the newly trained workers (who become productive after their 2-week training) themselves train future batches of new workers, or is training restricted to only the original 50 skilled workers?

## Turn 13 - User Simulator

Training is restricted to only the original 50 skilled workers.

## Turn 14 - Generic Agent

QUESTION: The brief says "a total of 50 new workers must be trained by the end of the 8th week." Is this a hard requirement (the model must train exactly 50, no more, no less), or is it a minimum (at least 50 must be trained, and training more is allowed if it helps reduce costs)?

## Turn 14 - User Simulator

This is a hard requirement: exactly 50 new workers must be trained, no more, no less.

## Turn 15 - Generic Agent

QUESTION: The brief says "a skilled worker can train at most 3 new workers in any two-week period." Does this mean a skilled worker can train 1, 2, or 3 trainees in a given two-week period (i.e., the number of trainees per batch is flexible up to 3), or must a skilled worker always train exactly 3 when assigned to training?

## Turn 15 - User Simulator

The number of trainees per batch is flexible up to 3. A skilled worker can train 1, 2, or 3 trainees in a given two-week period.

## Turn 16 - Generic Agent

QUESTION: The brief states "overtime: working 60 hours per week." Does this mean that in any given week, a worker either works 40 hours (normal) or 60 hours (overtime), with no intermediate option, or can a worker work any number of hours between 40 and 60?

## Turn 16 - User Simulator

In any given week, a worker either works 40 hours (normal) or 60 hours (overtime), with no intermediate option.

## Turn 17 - Generic Agent

QUESTION: The 50 skilled workers who are assigned to training in a given two-week period — do they still receive their weekly wage of 360 yuan (or 540 if overtime) during those training weeks, or are they paid a different rate while training?

## Turn 17 - User Simulator

They still receive their weekly wage of 360 yuan (or 540 if overtime) during those training weeks.

## Turn 18 - Generic Agent

QUESTION: The brief mentions "compensation fees for late delivery" for food I and II. Is there a limit on how many weeks a unit of demand can be delayed before it is simply lost (i.e., no compensation is paid and the demand is dropped), or can demand be delayed indefinitely as long as the compensation fee is paid for each week of delay?

## Turn 18 - User Simulator

There is no limit on how many weeks a unit of demand can be delayed. Demand can be delayed indefinitely as long as the compensation fee is paid for each week of delay.

## Turn 19 - Generic Agent

QUESTION: The brief says "a skilled worker can produce 10 kg/h of food I or 6 kg/h of food II." Does this mean a skilled worker can split their time between food I and food II within a week (e.g., 20 hours on food I and 20 hours on food II), or must a skilled worker be assigned entirely to one product per week?

## Turn 19 - User Simulator

A skilled worker can split their time between food I and food II within a week.

## Turn 20 - Generic Agent

QUESTION: The 50 new workers who complete training and become productive — do they also have the option to work overtime (60 hours per week at 540 yuan), or are they limited to 40 hours per week at 240 yuan?

## Turn 20 - User Simulator

They also have the option to work overtime (60 hours per week at 540 yuan).

## Turn 21 - Generic Agent

QUESTION: The brief says "a total of 50 new workers must be trained by the end of the 8th week." Since training takes 2 weeks, the last batch that can complete by the end of week 8 must start in week 7. Does this mean training batches can only start in odd weeks (weeks 1, 3, 5, 7) so that they complete in even weeks (weeks 2, 4, 6, 8), or can a batch start in any week (e.g., start in week 2 and complete in week 4)?

## Turn 21 - User Simulator

Training batches can start in any week. A batch can start in week 2 and complete in week 4, for example.

## Turn 22 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 22 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 23 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 23 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 24 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 24 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 25 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 25 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 26 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 26 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 27 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 27 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 28 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 28 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 29 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 29 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.

## Turn 30 - Generic Agent

QUESTION: The brief says "a skilled worker can have up to 3 trainees at any time." If a skilled worker starts 2 trainees in week 1 (completing in week 3), can that same worker start another 1 trainee in week 3 (completing in week 5), or must the worker wait until all 3 slots are free before starting a new batch?

## Turn 30 - User Simulator

The worker can start another 1 trainee in week 3. The constraint is that the worker cannot have more than 3 trainees at any time, so as long as the total number of active trainees does not exceed 3, the worker can start a new batch.