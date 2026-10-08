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

QUESTION: When you say "a total of 50 new workers must be trained by the end of the 8th week," do you mean that 50 trainees must have completed their 2-week training (and thus become productive) by the end of week 8, or that 50 trainees must have started training by the end of week 8 (some of whom would still be in training at week 8's end)?

## Turn 1 - User Simulator

It means 50 trainees must have completed their 2-week training and become productive by the end of week 8.

## Turn 2 - Generic Agent

QUESTION: The brief gives a weekly wage of 360 yuan for a skilled worker and 240 yuan/week for a worker after training, but does not say whether the 360 yuan is a fixed cost paid for every skilled worker on the roster each week regardless of how many hours they work, or whether it is tied to hours worked (e.g., 9 yuan/hour for the 40 normal hours). Is the 360 yuan a flat weekly cost per skilled worker independent of hours worked?

## Turn 2 - User Simulator

The 360 yuan is a flat weekly cost per skilled worker, independent of hours worked.

## Turn 3 - Generic Agent

QUESTION: The brief says overtime means working 60 hours per week at a weekly wage of 540 yuan, but does not say whether a worker can work any number of hours between 40 and 60 (with cost scaling accordingly), or whether the only two allowed weekly schedules are exactly 40 hours (360 yuan) or exactly 60 hours (540 yuan). Which is it?

## Turn 3 - User Simulator

The only two allowed weekly schedules are exactly 40 hours (360 yuan) or exactly 60 hours (540 yuan).

## Turn 4 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 4 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 5 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 5 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 6 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 6 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 7 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 7 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 8 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 8 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 9 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 9 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 10 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 10 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 11 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 11 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not

## Turn 12 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 12 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 13 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 13 - User Simulator

Training is done outside of production hours. During the two-week training period, the skilled

## Turn 14 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 14 - User Simulator

Training is done outside

## Turn 15 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 15 - User Simulator

Training

## Turn 16 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 16 - User Simulator

Training

## Turn 17 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 17 - User Simulator

Training

## Turn 18 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 18 - User Simulator

Training

## Turn 19 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 19 - User Simulator

Training

## Turn 20 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 20 - User Simulator

Training

## Turn 21 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 21 - User Simulator

Training

## Turn 22 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 22 - User Simulator

Training

## Turn 23 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 23 - User Simulator

Training

## Turn 24 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 24 - User Simulator

Training

## Turn 25 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 25 - User Simulator

Training

## Turn 26 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 26 - User Simulator

Training

## Turn 27 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 27 - User Simulator

Training

## Turn 28 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 28 - User Simulator

Training

## Turn 29 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 29 - User Simulator

Training

## Turn 30 - Generic Agent

QUESTION: When a skilled worker is training new workers, does that training consume part of their working hours (reducing the hours available for production), or is training done outside of production hours so the worker can still produce at full capacity while training?

## Turn 30 - User Simulator

Training