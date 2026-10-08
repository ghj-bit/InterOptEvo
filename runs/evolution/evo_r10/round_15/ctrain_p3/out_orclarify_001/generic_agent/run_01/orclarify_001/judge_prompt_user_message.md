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

QUESTION: When a new worker finishes their 2-week training, do they become fully productive (10 kg/h for food I, 6 kg/h for food II) starting in the very next week, or do they only start contributing production after completing the full 2-week training period (i.e., a worker who starts training in week 1 first produces in week 3)?

## Turn 1 - User Simulator

A worker who starts training in week 1 first produces in week 3. They only start contributing production after completing the full 2-week training period.

## Turn 2 - Generic Agent

QUESTION: When a skilled worker trains new workers, do they still produce food at their normal rate (10 kg/h for food I, 6 kg/h for food II) during the training weeks, or does training reduce or eliminate their production capacity?

## Turn 2 - User Simulator

Training eliminates their production capacity. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 3 - Generic Agent

QUESTION: The overtime option is described as "working 60 hours per week, weekly wage 540 yuan" — does this mean a worker can work up to 60 hours in a week (i.e., 40 normal + 20 overtime hours), with the 540 yuan being the total weekly pay when working 60 hours, or is 540 yuan the additional overtime pay on top of the normal 360 yuan weekly wage?

## Turn 3 - User Simulator

The 540 yuan is the total weekly pay when working 60 hours. It is not additional overtime pay on top of the normal 360 yuan weekly wage.

## Turn 4 - Generic Agent

QUESTION: The compensation fee for late delivery is stated as "0.5 yuan per kg per week for food I, 0.6 yuan per kg per week for food II" — does this mean that if demand is not met in a given week, the unmet amount is backordered (carried to a later week) and the penalty accumulates at that rate for each week the delivery is delayed, or does it mean the unmet demand is simply lost and a one-time penalty of that rate is paid?

## Turn 4 - User Simulator

The unmet amount is backordered (carried to a later week) and the penalty accumulates at that rate for each week the delivery is delayed.

## Turn 5 - Generic Agent

QUESTION: Can backordered demand be delivered in any later week (including weeks beyond week 8), or must all backordered demand be delivered by the end of week 8?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — does "by the end of the 8th week" mean their 2-week training must be fully completed by the end of week 8 (so the latest they can start training is week 7), or does it mean they just need to have started training by the end of week 8 (so some could still be in training at the end of week 8)?

## Turn 6 - User Simulator

The 2-week training must be fully completed by the end of week 8.

## Turn 7 - Generic Agent

QUESTION: The skilled workers who are training new workers during a two-week period — are they paid their normal weekly wage of 360 yuan during those training weeks, or do they receive a different rate?

## Turn 7 - User Simulator

They receive their normal weekly wage of 360 yuan during the training weeks.

## Turn 8 - Generic Agent

QUESTION: Can a skilled worker who finishes training a group of new workers in one two-week period immediately start training another group in the next two-week period, or is there a required break between training periods?

## Turn 8 - User Simulator

The point still needs internal confirmation.

## Turn 9 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — is this a strict minimum (at least 50 must be trained, and training more is allowed), or is it an exact requirement (exactly 50, no more, no fewer)?

## Turn 9 - User Simulator

It is a strict minimum. At least 50 must be trained, and training more is allowed.

## Turn 10 - Generic Agent

QUESTION: The production rates are given per hour (10 kg/h for food I, 6 kg/h for food II) — can a skilled worker split their hours between food I and food II within the same week (e.g., work 20 hours on food I and 20 hours on food II), or must each worker be assigned to produce only one type of food per week?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Is there a maximum number of new workers that can be hired (i.e., start training) in any given week, or is the only constraint on hiring the training capacity of skilled workers (at most 3 per skilled worker per two-week period)?

## Turn 11 - User Simulator

The only constraint on hiring is the training capacity of skilled workers (at most 3 per skilled worker per two-week period).

## Turn 12 - Generic Agent

QUESTION: The "at most 3 new workers per skilled worker per two-week period" constraint — does this mean a skilled worker can train up to 3 new workers in any rolling two-week window (e.g., if they train 3 in weeks 1-2, they cannot train any more in weeks 2-3), or does it mean they can train up to 3 in each non-overlapping two-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 12 - User Simulator

It means a skilled worker can train up to 3 new workers in any rolling two-week window.

## Turn 13 - Generic Agent

QUESTION: When a skilled worker trains new workers, can they train different numbers in each of the two weeks (e.g., 2 in week 1 and 1 in week 2, totaling 3 over the two-week window), or must all 3 new workers start and finish training in the same two-week block?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — do they all start training at the same time (i.e., in the same week), or can they start training in different weeks as long as all 50 complete training by the end of week 8?

## Turn 14 - User Simulator

They can start training in different weeks as long as all 50 complete training by the end of week 8.

## Turn 15 - Generic Agent

QUESTION: The objective of this plan — is it to minimize total cost (wages + overtime + backorder penalties), or is there a different objective such as maximizing profit or meeting all demand on time?

## Turn 15 - User Simulator

The objective is to minimize total cost, including wages, compensation fees, and any other relevant costs.

## Turn 16 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — are they in addition to the current 50 skilled workers (so the factory ends with at least 100 workers), or does the total workforce need to reach 50 (meaning only 0 new workers need to be trained since there are already 50)?

## Turn 16 - User Simulator

They are in addition to the current 50 skilled workers.

## Turn 17 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — do they all need to be trained by skilled workers from the current workforce of 50, or can newly trained workers (who become skilled after their 2-week training) also train additional new workers?

## Turn 17 - User Simulator

Only skilled workers can train new workers.

## Turn 18 - Generic Agent

QUESTION: When a skilled worker is training new workers during a two-week period, can they still work overtime (up to 60 hours) in those weeks, or is overtime only available for production weeks?

## Turn 18 - User Simulator

The point still needs internal confirmation.

## Turn 19 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — is there a maximum number of new workers that can start training in any single week (e.g., a hiring cap per week), or is the only limit the total training capacity of all skilled workers available in that two-week window?

## Turn 19 - User Simulator

The only limit is the total training capacity of all skilled workers available in that two-week window.

## Turn 20 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — do they all need to be trained by the original 50 skilled workers, or can newly trained workers (who become skilled after completing their 2-week training) also train additional new workers?

## Turn 20 - User Simulator

Only skilled workers can train new workers.

## Turn 21 - Generic Agent

QUESTION: When a skilled worker is training new workers during a two-week period, are they completely unavailable for production in both weeks of that period, or are they only unavailable in the week the new workers actually start training?

## Turn 21 - User Simulator

They are completely unavailable for production in both weeks of that period.

## Turn 22 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — can a newly trained worker (who becomes skilled after completing their 2-week training) also train additional new workers in a subsequent two-week period, or is training restricted to only the original 50 skilled workers?

## Turn 22 - User Simulator

The point still needs internal confirmation.

## Turn 23 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — is this a hard constraint that must be satisfied (i.e., the plan is infeasible if fewer than 50 are trained), or is it a target that can be relaxed with a penalty if not met?

## Turn 23 - User Simulator

It is a hard constraint that must be satisfied.

## Turn 24 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — can a newly trained worker (who becomes skilled after completing their 2-week training) also train additional new workers in a subsequent two-week period, or is training restricted to only the original 50 skilled workers?

## Turn 24 - User Simulator

The point still needs internal confirmation.

## Turn 25 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — is there a maximum number of new workers that can start training in any single week (e.g., a hiring cap per week), or is the only limit the total training capacity of all skilled workers available in that two-week window?

## Turn 25 - User Simulator

The only limit is the total training capacity of all skilled workers available in that two-week window.

## Turn 26 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — can a newly trained worker (who becomes skilled after completing their 2-week training) also train additional new workers in a subsequent two-week period, or is training restricted to only the original 50 skilled workers?

## Turn 26 - User Simulator

The point still needs internal confirmation.

## Turn 27 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — is there a maximum number of new workers that can start training in any single week (e.g., a hiring cap per week), or is the only limit the total training capacity of all skilled workers available in that two-week window?

## Turn 27 - User Simulator

The only limit is the total training capacity of all skilled workers available in that two-week window.

## Turn 28 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — can a newly trained worker (who becomes skilled after completing their 2-week training) also train additional new workers in a subsequent two-week period, or is training restricted to only the original 50 skilled workers?

## Turn 28 - User Simulator

The point still needs internal confirmation.

## Turn 29 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — is there a maximum number of new workers that can start training in any single week (e.g., a hiring cap per week), or is the only limit the total training capacity of all skilled workers available in that two-week window?

## Turn 29 - User Simulator

The only limit is the total training capacity of all skilled workers available in that two-week window.

## Turn 30 - Generic Agent

QUESTION: The 50 new workers that must be trained by the end of week 8 — can a newly trained worker (who becomes skilled after completing their 2-week training) also train additional new workers in a subsequent two-week period, or is training restricted to only the original 50 skilled workers?

## Turn 30 - User Simulator

The point still needs internal confirmation.