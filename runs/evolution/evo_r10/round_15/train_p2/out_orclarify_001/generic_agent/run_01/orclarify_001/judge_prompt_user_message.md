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

QUESTION: When you say "a total of 50 new workers must be trained by the end of the 8th week," do you mean that 50 trainees must have completed their 2-week training (and thus become productive workers) by the end of week 8, or that 50 trainees must have started training by the end of week 8 (even if some are still in training at that point)?

## Turn 1 - User Simulator

It means 50 trainees must have completed their 2-week training and become productive workers by the end of week 8.

## Turn 2 - Generic Agent

QUESTION: The brief gives a weekly wage of 360 yuan for a skilled worker and 240 yuan/week for a worker after training, but no wage for the 50 workers who are already skilled at the start — are those 50 initial skilled workers paid the 360 yuan/week rate, or the 240 yuan/week rate?

## Turn 2 - User Simulator

The 50 initial skilled workers are paid the 360 yuan/week rate.

## Turn 3 - Generic Agent

QUESTION: The brief says "Overtime: working 60 hours per week, weekly wage 540 yuan" — does this mean a worker who works overtime in a week is paid a flat 540 yuan for that week (replacing the normal 360/240 wage), or is 540 yuan an additional overtime premium on top of the normal weekly wage?

## Turn 3 - User Simulator

The 540 yuan is a flat weekly wage for a worker who works overtime, replacing the normal weekly wage.

## Turn 4 - Generic Agent

QUESTION: The brief lists weekly demand for foods I and II, and also gives late-delivery compensation fees (0.5 yuan/kg/week for food I, 0.6 yuan/kg/week for food II) — does this mean demand is a soft target that may be under-met, with the shortfall carried as backorder and penalized at those rates, or is demand a hard requirement that must be met exactly each week (making the late-delivery fees irrelevant)?

## Turn 4 - User Simulator

Demand is a soft target. It may be under-met, with the shortfall carried as backorder and penalized at the given late-delivery compensation rates.

## Turn 5 - Generic Agent

QUESTION: When a worker works overtime (60 hours instead of 40), does their production capacity in that week scale up proportionally to 60 hours (i.e., 1.5× the normal 40-hour output), or does overtime only affect the wage cost while production stays capped at 40 hours of output?

## Turn 5 - User Simulator

Production capacity scales up proportionally to 60 hours, so a worker working overtime produces 1.5× the normal 40-hour output.

## Turn 6 - Generic Agent

QUESTION: Can a worker who is currently a trainee (in their 2-week training period) also work overtime, or is overtime only available to workers who have already completed training (skilled/regular workers)?

## Turn 6 - User Simulator

Overtime is only available to workers who have already completed training (skilled/regular workers). Trainees in their 2-week training period do not work overtime.

## Turn 7 - Generic Agent

QUESTION: During their 2-week training period, do trainees produce any food at all, or are they completely non-productive (zero output) for both weeks of training?

## Turn 7 - User Simulator

Trainees are completely non-productive (zero output) for both weeks of their training period.

## Turn 8 - Generic Agent

QUESTION: The training capacity limit says "each skilled worker can train at most 3 new workers in any two-week period" — does this mean a skilled worker can start training up to 3 new trainees in any given 2-week window (e.g., weeks 1-2, weeks 3-4, etc.), or does it mean a skilled worker can have at most 3 trainees in training at any point in time (i.e., the 3 trainees started in weeks 1-2 must finish before they can start new ones in weeks 3-4)?

## Turn 8 - User Simulator

It means a skilled worker can start training up to 3 new trainees in any given 2-week window (e.g., weeks 1-2, weeks 3-4, etc.).

## Turn 9 - Generic Agent

QUESTION: When a skilled worker starts training new workers, does that reduce their available production hours in the training weeks, or can they simultaneously produce at full capacity (40 or 60 hours) while also training up to 3 new workers?

## Turn 9 - User Simulator

It reduces their available production hours. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 10 - Generic Agent

QUESTION: When a skilled worker is training (and thus not producing) during a 2-week window, are they still paid their normal 360 yuan/week wage for those weeks, or do they receive a different rate while training?

## Turn 10 - User Simulator

They are still paid their normal 360 yuan/week wage for those weeks.

## Turn 11 - Generic Agent

QUESTION: The training capacity limit says "each skilled worker can train at most 3 new workers in any two-week period" — does this mean the 3-trainee limit applies to any sliding 2-week window (e.g., a worker could start 3 in weeks 1-2 and another 3 in weeks 2-3), or does it apply only to fixed non-overlapping 2-week blocks (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8)?

## Turn 11 - User Simulator

It applies to any sliding 2-week window.

## Turn 12 - Generic Agent

QUESTION: Can a worker who has completed training (paid 240 yuan/week) also work overtime at 60 hours, or is overtime only available to the original 50 skilled workers (paid 360 yuan/week)?

## Turn 12 - User Simulator

A worker who has completed training (paid 240 yuan/week) can also work overtime at 60 hours.

## Turn 13 - Generic Agent

QUESTION: When a worker who completed training (normally paid 240 yuan/week) works overtime at 60 hours, what is their flat weekly wage for that week — is it still 540 yuan (same as the skilled workers), or is it a different amount?

## Turn 13 - User Simulator

The point still needs internal confirmation.

## Turn 14 - Generic Agent

QUESTION: The brief says "a total of 50 new workers must be trained by the end of the 8th week" — is this a hard constraint (the model must ensure exactly 50 or at least 50 trainees complete training by end of week 8), or is it a target that the model should try to achieve but could potentially fall short of if it's too costly?

## Turn 14 - User Simulator

It is a hard constraint. The model must ensure at least 50 trainees complete training by the end of week 8.

## Turn 15 - Generic Agent

QUESTION: The objective of this plan — is it to minimize total cost (wages + overtime + late-delivery penalties) subject to meeting the 50-trainee constraint and the soft demand targets, or is there a different objective (e.g., maximize profit, minimize total hours, etc.)?

## Turn 15 - User Simulator

The objective is to minimize total cost, including wages, overtime, and late-delivery penalties, subject to the 50-trainee constraint and the soft demand targets.

## Turn 16 - Generic Agent

QUESTION: For the overtime wage of a worker who completed training (normally 240 yuan/week) — since you said this needs internal confirmation, should I assume it is also 540 yuan flat (same as the skilled workers), or would you prefer I model it as a separate parameter that you'll confirm later?

## Turn 16 - User Simulator

Please model it as a separate parameter that I will confirm later.

## Turn 17 - Generic Agent

QUESTION: The late-delivery penalty is stated as 0.5 yuan per kg per week for food I and 0.6 yuan per kg per week for food II — does this mean that if, say, 1000 kg of food I is short in week 3, the penalty is 1000 × 0.5 × 1 = 500 yuan (one week of delay), or does the penalty accumulate each week the backorder remains unfulfilled (so if it's still short in week 4, it's 1000 × 0.5 × 2 = 1000 yuan)?

## Turn 17 - User Simulator

The penalty accumulates each week the backorder remains unfulfilled.

## Turn 18 - Generic Agent

QUESTION: Can a skilled worker who is training in one 2-week window (e.g., weeks 1-2) immediately start training again in the very next window (weeks 3-4), or is there a mandatory rest/production period between training assignments?

## Turn 18 - User Simulator

A skilled worker can immediately start training again in the very next window. There is no mandatory rest or production period between training assignments.

## Turn 19 - Generic Agent

QUESTION: The sliding 2-week window constraint means a skilled worker can start at most 3 trainees in any 2 consecutive weeks — does this apply to all workers who have completed training (including the 240-yuan workers), or only to the original 50 skilled workers (360-yuan workers)?

## Turn 19 - User Simulator

It applies only to the original 50 skilled workers (360-yuan workers).

## Turn 20 - Generic Agent

QUESTION: When a skilled worker is training during a 2-week window, they are completely non-productive — but can they still work overtime (60 hours) in those weeks for the purpose of training, or does the training simply occupy their full availability with no overtime option?

## Turn 20 - User Simulator

The training simply occupies their full availability with no overtime option.

## Turn 21 - Generic Agent

QUESTION: The 50 initial skilled workers are paid 360 yuan/week — if one of them works overtime (60 hours), their flat wage becomes 540 yuan. But if one of them is training (non-productive), they still get 360 yuan/week. Is there any scenario where a skilled worker could be both training AND working overtime in the same week, or are these mutually exclusive states (a worker is either producing, producing with overtime, or training, but never a combination)?

## Turn 21 - User Simulator

These are mutually exclusive states. A worker is either producing, producing with overtime, or training, but never a combination.

## Turn 22 - Generic Agent

QUESTION: The brief mentions "Normal weekly working hours: 40 hours per week" and overtime at 60 hours — is the choice between 40 and 60 hours a binary decision per worker per week (each worker either works 40 or 60 hours), or can a worker work any number of hours between 40 and 60?

## Turn 22 - User Simulator

It is a binary decision per worker per week: each worker either works 40 or 60 hours.

## Turn 23 - Generic Agent

QUESTION: The 50 initial skilled workers are paid 360 yuan/week when producing normally and 540 yuan/week when working overtime. For the workers who complete training (paid 240 yuan/week normally), I'll model their overtime wage as a separate parameter. But for the 50 initial skilled workers who are training (non-productive), they get 360 yuan/week — is there any overtime wage applicable to them during training, or is 360 yuan/week the only wage they receive while training?

## Turn 23 - User Simulator

360 yuan/week is the only wage they receive while training.

## Turn 24 - Generic Agent

QUESTION: The production rates are given as 10 kg/h for food I and 6 kg/h for food II — can a worker split their hours between the two foods within a week (e.g., 20 hours on food I and 20 hours on food II), or must each worker be assigned to produce only one food per week?

## Turn 24 - User Simulator

A worker can split their hours between the two foods within a week.

## Turn 25 - Generic Agent

QUESTION: The 50 initial skilled workers can each train up to 3 new workers in any sliding 2-week window, and they are non-productive while training. Is there any limit on how many of the 50 skilled workers can be training simultaneously, or can all 50 be training at the same time (leaving zero skilled workers for production)?

## Turn 25 - User Simulator

There is no limit on how many of the 50 skilled workers can be training simultaneously. All 50 can be training at the same time.

## Turn 26 - Generic Agent

QUESTION: The 50 initial skilled workers can each train up to 3 new workers in any sliding 2-week window. When a skilled worker starts training 3 new workers in, say, weeks 1-2, those 3 trainees complete training at the end of week 2 and become productive workers (paid 240 yuan/week). Do these newly trained workers then also count toward the "50 new workers must be trained by end of week 8" requirement, or is the 50-trainee target only about the initial cohort of trainees started by the original 50 skilled workers?

## Turn 26 - User Simulator

The 50-trainee target is only about the initial cohort of trainees started by the original 50 skilled workers.

## Turn 27 - Generic Agent

QUESTION: The 50 initial skilled workers can each train up to 3 new workers in any sliding 2-week window, and they are non-productive while training. When a skilled worker is training, they are completely non-productive for both weeks of the training period. Does this mean that if a skilled worker starts training 3 trainees in weeks 1-2, they are non-productive in both week 1 and week 2, and then can resume production in week 3?

## Turn 27 - User Simulator

Yes, if a skilled worker starts training 3 trainees in weeks 1-2, they are non-productive in both week 1 and week 2, and can resume production in week 3.

## Turn 28 - Generic Agent

QUESTION: The sliding 2-week window constraint means a skilled worker can start at most 3 trainees in any 2 consecutive weeks. If a skilled worker starts 3 trainees in week 1, can they start another 3 in week 2 (since weeks 1-2 is a 2-week window with 6 total trainees started), or does the constraint mean at most 3 total trainees started across any 2 consecutive weeks (so starting 3 in week 1 means 0 more can be started in week 2)?

## Turn 28 - User Simulator

The constraint means at most 3 total trainees started across any 2 consecutive weeks. So starting 3 in week 1 means 0 more can be started in week 2.

## Turn 29 - Generic Agent

QUESTION: The 50 initial skilled workers can each train up to 3 new workers in any sliding 2-week window, and they are non-productive while training. When a skilled worker is training, they are non-productive for both weeks of the training period. Does the training period always align with the start of a week (e.g., a trainee starts at the beginning of week 1 and completes at the end of week 2), or can training start mid-week?

## Turn 29 - User Simulator

The training period always aligns with the start of a week.

## Turn 30 - Generic Agent

QUESTION: The 50 initial skilled workers can each train up to 3 new workers in any sliding 2-week window, and they are non-productive while training. When a skilled worker is training, they are non-productive for both weeks of the training period. Does the training period always align with the start of a week (e.g., a trainee starts at the beginning of week 1 and completes at the end of week 2), or can training start mid-week?

## Turn 30 - User Simulator

The training period always aligns with the start of a week.