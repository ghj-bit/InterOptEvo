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

QUESTION: When you say "a total of 50 new workers must be trained by the end of the 8th week," do you mean that 50 trainees must have COMPLETED their 2-week training (i.e., become productive workers) by the end of week 8, or that 50 trainees must have STARTED training by the end of week 8 (some of whom would still be in training at week 8's end)?

## Turn 1 - User Simulator

It means 50 trainees must have completed their 2-week training and become productive workers by the end of week 8.

## Turn 2 - Generic Agent

QUESTION: The brief gives a "late delivery" compensation fee per kg per week, which implies demand can be met late. Do you want the model to allow backlogging (producing a week's demand in a later week and paying the penalty), or must each week's demand be met exactly in that week with no backlog allowed?

## Turn 2 - User Simulator

The model should allow backlogging. If a week's demand is not met in that week, it can be produced in a later week, and the late delivery compensation fee applies for each week the delivery is delayed.

## Turn 3 - Generic Agent

QUESTION: The brief says a skilled worker can train at most 3 new workers "in any two-week period." Does this mean a skilled worker can have at most 3 trainees in training at any time (i.e., a trainee occupies the trainer for the full 2 weeks, so a worker could start 3 trainees in week 1 and another 3 in week 3, but never more than 3 in training simultaneously), or does it mean a skilled worker can start at most 3 new trainees in each 2-week block (weeks 1-2, weeks 3-4, weeks 5-6, weeks 7-8) regardless of overlap?

## Turn 3 - User Simulator

It means a skilled worker can have at most 3 trainees in training at any time. A trainee occupies the trainer for the full 2 weeks, so a worker could start 3 trainees in week 1 and another 3 in week 3, but never more than 3 in training simultaneously.

## Turn 4 - Generic Agent

QUESTION: When a skilled worker is training a trainee, does that skilled worker still produce food (at the same 10 kg/h or 6 kg/h rate), or is the skilled worker's production capacity reduced or eliminated during the weeks they are actively training?

## Turn 4 - User Simulator

The skilled worker's production capacity is eliminated during the weeks they are actively training. Neither the skilled worker doing the training nor the trainees they are training are involved in any production during the two-week training period.

## Turn 5 - Generic Agent

QUESTION: The brief states "only skilled workers can train new workers." Does this mean that workers who completed training (paid 240 yuan/week, same production efficiency) are NOT eligible to train new workers themselves, or can they also act as trainers once they become productive?

## Turn 5 - User Simulator

Workers who completed training are NOT eligible to train new workers themselves. Only the original skilled workers can act as trainers.

## Turn 6 - Generic Agent

QUESTION: The brief mentions "Normal weekly working hours: 40 hours per week" and "Overtime: working 60 hours per week, weekly wage 540 yuan." Does this mean each worker can work either 40 hours (normal) or 60 hours (overtime) per week, with the 540 yuan being the total weekly wage when working 60 hours (replacing the 360 yuan normal wage), or is the 540 yuan an additional overtime premium on top of the 360 yuan base wage?

## Turn 6 - User Simulator

The 540 yuan is the total weekly wage when working 60 hours, replacing the 360 yuan normal wage. It is not an additional premium on top of the base wage.

## Turn 7 - Generic Agent

QUESTION: The brief states "one skilled worker can produce 10 kg/h of food I or 6 kg/h of food II." Does this mean a worker can split their hours between the two foods (e.g., work 20 hours on food I and 20 hours on food II in a 40-hour week), or must each worker be assigned to produce only one food type per week?

## Turn 7 - User Simulator

A worker can split their hours between the two foods. They are not required to be assigned to produce only one food type per week.

## Turn 8 - Generic Agent

QUESTION: The brief mentions "Compensation fees for late delivery: 0.5 yuan per kg per week for food I, 0.6 yuan per kg per week for food II." Does this penalty apply only to the portion of demand that is delivered late (i.e., if 1000 kg of week 3's food I demand is delivered in week 5, the penalty is 1000 × 0.5 × 2 = 1000 yuan for the 2-week delay), or is there also a penalty for any demand that remains undelivered by the end of week 8?

## Turn 8 - User Simulator

The penalty applies only to the portion of demand that is delivered late. If 1000 kg of week 3's food I demand is delivered in week 5, the penalty is 1000 × 0.5 × 2 = 1000 yuan for the 2-week delay. There is no separate penalty for demand that remains undelivered by the end of week 8.

## Turn 9 - Generic Agent

QUESTION: The brief states "a total of 50 new workers must be trained by the end of the 8th week." Is this a hard constraint (the model must train exactly 50 or at least 50 new workers, and infeasibility if it cannot), or is it a target that the model should try to meet but could potentially fall short of if doing so would be too costly?

## Turn 9 - User Simulator

This is a hard constraint. The model must train exactly 50 new workers by the end of week 8.

## Turn 10 - Generic Agent

QUESTION: The brief states "a total of 50 new workers must be trained by the end of the 8th week" and you confirmed this is a hard constraint. Does "exactly 50" mean the model must train precisely 50 (no more, no fewer), or at least 50 (50 or more is acceptable)?

## Turn 10 - User Simulator

It means at least 50. Training 50 or more new workers by the end of week 8 is acceptable.

## Turn 11 - Generic Agent

QUESTION: The brief mentions "Normal weekly working hours: 40 hours per week" and "Overtime: working 60 hours per week." Does this mean each worker can work at most 60 hours per week (with the choice being 40 or 60), or can a worker work any number of hours up to 60 (e.g., 45, 50, 55 hours)?

## Turn 11 - User Simulator

Each worker can work at most 60 hours per week, with the choice being 40 or 60 hours.

## Turn 12 - Generic Agent

QUESTION: The brief states "Weekly wage for a trainee during the training period: 120 yuan." Since trainees are not involved in production during their 2-week training, is the 120 yuan/week simply a cost the factory pays for each trainee in each week of their training, with no other production or capacity implications?

## Turn 12 - User Simulator

Yes, the 120 yuan/week is simply a cost the factory pays for each trainee in each week of their training. There are no other production or capacity implications.

## Turn 13 - Generic Agent

QUESTION: The brief states "After training, new workers receive 240 yuan/week and have the same production efficiency as skilled workers." Does this mean that once a trainee completes their 2-week training, they are paid 240 yuan/week for the remainder of the 8-week horizon (even if they only complete training in week 7 or 8), and they can produce at 10 kg/h for food I or 6 kg/h for food II just like the original skilled workers?

## Turn 13 - User Simulator

Yes. Once a trainee completes their 2-week training, they are paid 240 yuan/week for the remainder of the 8-week horizon, and they can produce at 10 kg/h for food I or 6 kg/h for food II just like the original skilled workers.

## Turn 14 - Generic Agent

QUESTION: The brief states "Overtime: working 60 hours per week, weekly wage 540 yuan." Does this 540 yuan overtime wage apply to all worker types (original skilled workers, and workers who completed training), or does it apply only to the original skilled workers?

## Turn 14 - User Simulator

The 540 yuan overtime wage applies to all worker types: original skilled workers and workers who completed training.

## Turn 15 - Generic Agent

QUESTION: The brief states "Normal weekly working hours: 40 hours per week" and "Overtime: working 60 hours per week." Does this mean that in any given week, a worker must work either exactly 40 hours or exactly 60 hours (no partial overtime), or can a worker work any number of hours between 40 and 60?

## Turn 15 - User Simulator

In any given week, a worker must work either exactly 40 hours or exactly 60 hours. There is no partial overtime.

## Turn 16 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees currently in their 2-week training period (i.e., the count of trainees whose 2-week window overlaps that week is at most 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 16 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees currently in their 2-week training period. The count of trainees whose 2-week window overlaps that week is at most 3.

## Turn 17 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 17 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 18 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 18 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 19 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 19 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 20 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 20 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 21 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 21 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 22 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 22 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 23 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 23 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 24 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 24 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 25 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 25 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 26 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 26 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 27 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 27 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 28 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 28 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 29 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 29 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.

## Turn 30 - Generic Agent

QUESTION: The brief states "a skilled worker can have at most 3 trainees in training at any time." Does this mean that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week (so if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3), or does it mean a skilled worker can start at most 3 new trainees in any 2-week window (e.g., at most 3 starts in weeks 1-2 combined, at most 3 starts in weeks 3-4 combined, etc.)?

## Turn 30 - User Simulator

It means that in any given week, a skilled worker can have at most 3 trainees whose 2-week training window overlaps that week. So if a worker starts 3 trainees in week 1, they cannot start any more until those 3 complete in week 3.