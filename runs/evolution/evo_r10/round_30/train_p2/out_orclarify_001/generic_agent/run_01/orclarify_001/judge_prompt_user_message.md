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

QUESTION: What is the objective of this plan — are we minimizing total cost (wages + overtime + late-delivery compensation) over the 8 weeks, or is there another goal such as maximizing profit or meeting all demand on time at minimum workforce?

## Turn 1 - User Simulator

The objective is to minimize total cost over the 8 weeks. This includes wages, overtime, and late-delivery compensation fees.

## Turn 2 - Generic Agent

QUESTION: When a new worker finishes their 2-week training, do they become a fully skilled worker who can themselves train new workers, or do they remain a "new worker" (paid 240 yuan/week) who can only produce and never train?

## Turn 2 - User Simulator

After training, new workers have the same production efficiency as skilled workers.

## Turn 3 - Generic Agent

QUESTION: After finishing training, can a new worker (paid 240 yuan/week) also act as a trainer for other new workers, or is the ability to train restricted to the original 50 skilled workers (paid 360 yuan/week) only?

## Turn 3 - User Simulator

The ability to train is restricted to the original 50 skilled workers only.

## Turn 4 - Generic Agent

QUESTION: The 50 new workers must be trained by the end of week 8 — is this a hard requirement (the plan is infeasible if fewer than 50 are trained), or is it a target that can be missed at some penalty?

## Turn 4 - User Simulator

It is a hard requirement. The plan is infeasible if fewer than 50 new workers are trained by the end of week 8.

## Turn 5 - Generic Agent

QUESTION: When a skilled worker is training new workers during a two-week period, are they still available to produce food (at the normal 10 kg/h or 6 kg/h rates), or is their production capacity reduced or zero while they are training?

## Turn 5 - User Simulator

Their production capacity is zero while they are training.

## Turn 6 - Generic Agent

QUESTION: The 3-new-worker limit is per skilled worker per two-week period — can a skilled worker train in overlapping two-week windows (e.g., train 3 in weeks 1–2 and another 3 in weeks 2–3), or must they wait until the previous two-week training period is fully complete before starting a new one?

## Turn 6 - User Simulator

They must wait until the previous two-week training period is fully complete before starting a new one.

## Turn 7 - Generic Agent

QUESTION: Can a skilled worker train fewer than 3 new workers in a two-week period (e.g., 1 or 2), or must they always train exactly 3 whenever they start a training period?

## Turn 7 - User Simulator

A skilled worker can train fewer than 3 new workers in a two-week period.

## Turn 8 - Generic Agent

QUESTION: The 50 new workers must be trained by the end of week 8 — does this mean their 2-week training must be fully completed by the end of week 8 (so the latest they can start is week 7), or is it enough that they have started training by the end of week 8 even if they finish in week 9?

## Turn 8 - User Simulator

Their 2-week training must be fully completed by the end of week 8.

## Turn 9 - Generic Agent

QUESTION: Can a skilled worker start a training period in any week (e.g., weeks 1–2, 2–3, 3–4, etc.), or are training periods restricted to specific non-overlapping two-week blocks (e.g., only weeks 1–2, 3–4, 5–6, 7–8)?

## Turn 9 - User Simulator

A skilled worker can start a training period in any week.

## Turn 10 - Generic Agent

QUESTION: When demand cannot be met in a given week, is the shortfall carried over as backlogged inventory that must be delivered in a later week (incurring the late-delivery compensation per week of delay), or is the shortfall simply lost (no future delivery obligation)?

## Turn 10 - User Simulator

The shortfall is carried over as backlogged inventory that must be delivered in a later week, incurring the late-delivery compensation per week of delay.

## Turn 11 - Generic Agent

QUESTION: Is there any limit on how many weeks a backlogged order can be delayed before it is simply cancelled, or can backlog be carried indefinitely until it is eventually delivered?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Can the factory produce food in a given week and store it as inventory to meet demand in a later week, or must production in each week be allocated only to that week's demand (and any backlog)?

## Turn 12 - User Simulator

The factory can produce food in a given week and store it as inventory to meet demand in a later week.

## Turn 13 - Generic Agent

QUESTION: Is there any holding cost for storing inventory of food I or food II between weeks, or is inventory storage free?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: The overtime option is 60 hours per week instead of the normal 40 — does this apply to all workers (skilled, new, and trainees), or only to skilled workers?

## Turn 14 - User Simulator

The point still needs internal confirmation.

## Turn 15 - Generic Agent

QUESTION: Do trainees (during their 2-week training period) contribute any production output, or are they purely in training with zero production capacity for both weeks?

## Turn 15 - User Simulator

They are purely in training with zero production capacity for both weeks.

## Turn 16 - Generic Agent

QUESTION: The 50 skilled workers at the start — are they all available from week 1, or are some already assigned to training or otherwise unavailable in the early weeks?

## Turn 16 - User Simulator

All 50 skilled workers are available from week 1.

## Turn 17 - Generic Agent

QUESTION: The overtime wage of 540 yuan per week — is this the total weekly wage for a worker who works 60 hours (replacing the normal 360 yuan), or is it an additional premium on top of the normal 360 yuan (so total would be 900 yuan)?

## Turn 17 - User Simulator

The point still needs internal confirmation.

## Turn 18 - Generic Agent

QUESTION: The late-delivery compensation is 0.5 yuan per kg per week for food I and 0.6 yuan per kg per week for food II — is this charged for each week the backlog is outstanding (so a kg delayed 3 weeks costs 3 × 0.5), or is it a one-time fee charged once when the delivery is finally made late?

## Turn 18 - User Simulator

It is charged for each week the backlog is outstanding.

## Turn 19 - Generic Agent

QUESTION: For the overtime option (60 hours instead of 40), is the 540 yuan the total weekly wage for that worker (replacing the normal 360 yuan), or is it an additional premium on top of the normal 360 yuan?

## Turn 19 - User Simulator

The point still needs internal confirmation.

## Turn 20 - Generic Agent

QUESTION: Can a skilled worker who is not training produce both food I and food II in the same week (splitting their hours between the two products), or must each worker be dedicated to only one product per week?

## Turn 20 - User Simulator

The point still needs internal confirmation.

## Turn 21 - Generic Agent

QUESTION: Is there any limit on the total number of workers (skilled + new) the factory can employ at any given time, or is the only constraint on workforce size the training capacity of the 50 skilled workers?

## Turn 21 - User Simulator

The point still needs internal confirmation.

## Turn 22 - Generic Agent

QUESTION: Can a skilled worker who is not training split their weekly hours between producing food I and food II in the same week, or must each worker be dedicated to only one product per week?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: Is there any limit on the total number of workers (skilled + new) the factory can employ at any given time, or is the only constraint on workforce size the training capacity of the 50 skilled workers?

## Turn 23 - User Simulator

The point still needs internal confirmation.

## Turn 24 - Generic Agent

QUESTION: Can a skilled worker who is not training split their weekly hours between producing food I and food II in the same week, or must each worker be dedicated to only one product per week?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: Is there any limit on the total number of workers (skilled + new) the factory can employ at any given time, or is the only constraint on workforce size the training capacity of the 50 skilled workers?

## Turn 25 - User Simulator

The point still needs internal confirmation.

## Turn 26 - Generic Agent

QUESTION: Can a skilled worker who is not training split their weekly hours between producing food I and food II in the same week, or must each worker be dedicated to only one product per week?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: Is there any limit on the total number of workers (skilled + new) the factory can employ at any given time, or is the only constraint on workforce size the training capacity of the 50 skilled workers?

## Turn 27 - User Simulator

The point still needs internal confirmation.

## Turn 28 - Generic Agent

QUESTION: Can a skilled worker who is not training split their weekly hours between producing food I and food II in the same week, or must each worker be dedicated to only one product per week?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: Is there any limit on the total number of workers (skilled + new) the factory can employ at any given time, or is the only constraint on workforce size the training capacity of the 50 skilled workers?

## Turn 29 - User Simulator

The point still needs internal confirmation.

## Turn 30 - Generic Agent

QUESTION: Can a skilled worker who is not training split their weekly hours between producing food I and food II in the same week, or must each worker be dedicated to only one product per week?

## Turn 30 - User Simulator

The point still needs internal confirmation.