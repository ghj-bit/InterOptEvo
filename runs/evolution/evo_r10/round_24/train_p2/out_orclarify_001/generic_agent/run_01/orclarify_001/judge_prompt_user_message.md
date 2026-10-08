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

QUESTION: When a worker finishes a 2-week training period, do they become fully productive (at 10 kg/h for food I or 6 kg/h for food II) starting the very next week, or is there any additional ramp-up or delay before they can count toward production?

## Turn 1 - User Simulator

They become fully productive starting the very next week after the training period ends. There is no additional ramp-up or delay.

## Turn 2 - Generic Agent

QUESTION: Can a skilled worker who is currently training new workers also produce food in the same week, or does training consume their full working time so they cannot produce during those weeks?

## Turn 2 - User Simulator

Training consumes their full working time. During the two-week training period, the skilled worker doing the training does not participate in any production.

## Turn 3 - Generic Agent

QUESTION: When a skilled worker trains 3 new workers over a two-week period, is the training load spread evenly (i.e., the worker is fully occupied with training for both weeks), or could a worker train fewer than 3 in one week and more in the other, as long as the total over the two weeks is at most 3?

## Turn 3 - User Simulator

The training load is spread evenly. The skilled worker is fully occupied with training for both weeks of the two-week period.

## Turn 4 - Generic Agent

QUESTION: The brief says a skilled worker can train at most 3 new workers "in any two-week period." Does this mean the constraint is a sliding window (i.e., in any consecutive 2-week span, a given skilled worker can have trained at most 3 new workers total), or does it mean the factory operates in fixed non-overlapping 2-week blocks (weeks 1-2, 3-4, 5-6, 7-8) and the limit of 3 applies per block?

## Turn 4 - User Simulator

The factory operates in fixed non-overlapping 2-week blocks (weeks 1-2, 3-4, 5-6, 7-8), and the limit of 3 applies per block.

## Turn 5 - Generic Agent

QUESTION: Can a skilled worker who finishes training a group in one 2-week block immediately start training another group in the very next 2-week block, or is there a required break period between training assignments?

## Turn 5 - User Simulator

A skilled worker who finishes training a group in one 2-week block can immediately start training another group in the very next 2-week block. There is no required break period between training assignments.

## Turn 6 - Generic Agent

QUESTION: The 50 new workers must be trained "by the end of the 8th week." Does this mean all 50 must have completed their 2-week training by the end of week 8 (so they are available as productive workers from week 9 onward), or does it mean all 50 must have *started* training by the end of week 8 (so some could still be in training during week 8 and only finish in week 9)?

## Turn 6 - User Simulator

All 50 must have completed their 2-week training by the end of week 8, so they are available as productive workers from week 9 onward.

## Turn 7 - Generic Agent

QUESTION: The 50 new workers who complete training by the end of week 8 are available from week 9 onward, but the production plan only covers weeks 1 through 8. Are these 50 new workers relevant to the model only as a constraint (they must be trained within the 8-week horizon), or do they also need to be included in the production capacity for any of weeks 1-8 (e.g., if they finish training mid-horizon, can they produce in the remaining weeks)?

## Turn 7 - User Simulator

They are relevant to the model only as a constraint (they must be trained within the 8-week horizon). They do not need to be included in the production capacity for any of weeks 1-8.

## Turn 8 - Generic Agent

QUESTION: The weekly demand table specifies exact quantities for each week. Is the requirement to meet demand exactly (no overproduction, no underproduction), or is it a minimum that must be met, with overproduction allowed (perhaps stored as inventory for later weeks)?

## Turn 8 - User Simulator

The requirement is to meet demand exactly (no overproduction, no underproduction).

## Turn 9 - Generic Agent

QUESTION: The brief mentions compensation fees for late delivery (0.5 yuan/kg/week for food I, 0.6 yuan/kg/week for food II). Since you've confirmed demand must be met exactly with no overproduction or underproduction, is there any possibility of late delivery in this model, or should I treat the demand as a hard constraint that must be satisfied in each week with no late-delivery option?

## Turn 9 - User Simulator

There is a possibility of late delivery in this model. The demand is not a hard constraint that must be satisfied in each week; late delivery is allowed, and the compensation fees apply to the shortfall.

## Turn 10 - Generic Agent

QUESTION: If demand is not met in a given week, does the unmet quantity carry over to the next week (i.e., it becomes part of the next week's demand that must still be fulfilled), or is it simply a one-time penalty paid for that week's shortfall and the demand is considered "lost" (not carried forward)?

## Turn 10 - User Simulator

The unmet quantity carries over to the next week. It becomes part of the next week's demand that must still be fulfilled.

## Turn 11 - Generic Agent

QUESTION: If demand carries over to the next week, is there a final deadline by which all accumulated demand must be fulfilled (e.g., by the end of week 8), or can demand remain unfulfilled beyond week 8 with the compensation fee continuing to accrue indefinitely?

## Turn 11 - User Simulator

There is a final deadline by which all accumulated demand must be fulfilled by the end of week 8.

## Turn 12 - Generic Agent

QUESTION: The compensation fee is stated as 0.5 yuan per kg per week for food I. If a unit of food I demand from week 3 is not met in week 3 but is met in week 5, is the penalty 0.5 × 2 = 1.0 yuan per kg (one week of lateness for week 4, one week for week 5), or is it 0.5 × 1 = 0.5 yuan per kg (a flat penalty regardless of how late it is)?

## Turn 12 - User Simulator

The penalty is 0.5 × 2 = 1.0 yuan per kg. The fee accrues for each week the demand remains unmet.

## Turn 13 - Generic Agent

QUESTION: The brief states normal weekly working hours are 40 hours per week and overtime is 60 hours per week. Is the choice between 40 and 60 hours a binary decision per worker per week (each worker either works 40 or 60 hours), or can workers work any number of hours between 40 and 60?

## Turn 13 - User Simulator

The choice between 40 and 60 hours is a binary decision per worker per week. Each worker either works 40 or 60 hours.

## Turn 14 - Generic Agent

QUESTION: The weekly wage for a skilled worker is 360 yuan, and overtime is 60 hours per week with a weekly wage of 540 yuan. Is the 540 yuan the total weekly wage when a worker works 60 hours (i.e., it replaces the 360 yuan), or is it an additional 540 yuan on top of the 360 yuan base wage?

## Turn 14 - User Simulator

The 540 yuan is the total weekly wage when a worker works 60 hours. It replaces the 360 yuan base wage.

## Turn 15 - Generic Agent

QUESTION: The brief states that after training, new workers receive 240 yuan/week and have the same production efficiency as skilled workers. Since these 50 new workers are only relevant as a training constraint and do not produce in weeks 1-8, is the 240 yuan/week wage for them relevant to the model at all, or should I ignore it since they don't work during the planning horizon?

## Turn 15 - User Simulator

The 240 yuan/week wage for them is not relevant to the model. It can be ignored since they do not work during the planning horizon.

## Turn 16 - Generic Agent

QUESTION: During the 2-week training period, the trainees receive 120 yuan per week. Is this 120 yuan/week paid to each individual trainee for each week of their 2-week training (so each trainee costs 240 yuan total over the training period), or is it a flat 120 yuan total per trainee for the entire 2-week period?

## Turn 16 - User Simulator

The 120 yuan/week is paid to each individual trainee for each week of their 2-week training. Each trainee costs 240 yuan total over the training period.

## Turn 17 - Generic Agent

QUESTION: A skilled worker who is training new workers during a 2-week block does not produce. Does this worker still receive their normal weekly wage of 360 yuan during those training weeks, or is their wage different (e.g., reduced or zero) while they are occupied with training?

## Turn 17 - User Simulator

The skilled worker still receives their normal weekly wage of 360 yuan during those training weeks.

## Turn 18 - Generic Agent

QUESTION: Can a skilled worker who is training new workers in a given 2-week block also be assigned to produce food in the other weeks of that same block, or does the training commitment occupy the worker for the entire 2-week block (both weeks), meaning they produce zero in both weeks of that block?

## Turn 18 - User Simulator

The training commitment occupies the worker for the entire 2-week block (both weeks), meaning they produce zero in both weeks of that block.

## Turn 19 - Generic Agent

QUESTION: The 50 skilled workers at the start of the plan — are they all available for production and/or training from week 1, or are some of them already committed to training or other duties before the planning horizon begins?

## Turn 19 - User Simulator

All 50 skilled workers are available for production and/or training from week 1.

## Turn 20 - Generic Agent

QUESTION: The objective of this plan — is it to minimize total cost (wages + overtime premium + training costs + late-delivery penalties), or is there a different objective such as maximizing profit, minimizing total hours, or something else?

## Turn 20 - User Simulator

The objective is to minimize total cost, including wages, compensation fees, and any other relevant costs.

## Turn 21 - Generic Agent

QUESTION: The overtime wage is 540 yuan/week (total) versus the normal 360 yuan/week. Is the overtime premium (the extra 180 yuan) the only additional cost of using overtime, or are there other costs associated with overtime (e.g., a fixed setup cost, a cap on how many workers can do overtime in a week, or a limit on how many weeks in a row a worker can do overtime)?

## Turn 21 - User Simulator

The overtime premium (the extra 180 yuan) is the only additional cost of using overtime. There are no other costs, caps, or limits associated with overtime.

## Turn 22 - Generic Agent

QUESTION: Can a skilled worker who is assigned to produce food in a given week split their production time between food I and food II (e.g., work 20 hours on food I and 20 hours on food II), or must each worker be dedicated to producing only one type of food per week?

## Turn 22 - User Simulator

A skilled worker can split their production time between food I and food II in a given week.

## Turn 23 - Generic Agent

QUESTION: The 50 new workers must be trained by the end of week 8, and training happens in fixed 2-week blocks (weeks 1-2, 3-4, 5-6, 7-8). Since all 50 must complete training by the end of week 8, the latest they can start is the block covering weeks 7-8. Does this mean training can only begin in the first week of each block (i.e., weeks 1, 3, 5, or 7), or can a training group start in any week as long as it fits within a 2-week block?

## Turn 23 - User Simulator

Training can only begin in the first week of each block (i.e., weeks 1, 3, 5, or 7).

## Turn 24 - Generic Agent

QUESTION: The skilled workers who are training in a given 2-week block are fully occupied and produce zero. Does the number of skilled workers available for production in a given week equal 50 minus the number of skilled workers assigned to training in that week's block, or is there any other factor that reduces the available skilled workforce (e.g., leave, turnover, or a cap on how many can train simultaneously)?

## Turn 24 - User Simulator

The number of skilled workers available for production in a given week equals 50 minus the number of skilled workers assigned to training in that week's block. There are no other factors that reduce the available skilled workforce.

## Turn 25 - Generic Agent

QUESTION: The 50 skilled workers can each train at most 3 new workers per 2-week block. With 50 skilled workers, the maximum number of new workers that can be trained in a single block is 150. Since only 50 new workers need to be trained total, is there any constraint on how many skilled workers can be assigned to training in a single block (e.g., a minimum number that must remain available for production), or can all 50 skilled workers be assigned to training in a block if needed?

## Turn 25 - User Simulator

There is no constraint on how many skilled workers can be assigned to training in a single block. All 50 skilled workers can be assigned to training in a block if needed.

## Turn 26 - Generic Agent

QUESTION: The production rates are given as 10 kg/h for food I and 6 kg/h for food II. Are these rates per skilled worker per hour, meaning one skilled worker working 40 hours in a week can produce 400 kg of food I or 240 kg of food II (and 600 kg or 360 kg respectively if working 60 hours)?

## Turn 26 - User Simulator

Yes, these rates are per skilled worker per hour. One skilled worker working 40 hours in a week can produce 400 kg of food I or 240 kg of food II (and 600 kg or 360 kg respectively if working 60 hours).

## Turn 27 - Generic Agent

QUESTION: The demand for food I in week 1 is 10,000 kg. With 50 skilled workers each producing at most 400 kg of food I in a 40-hour week (or 600 kg in a 60-hour week), the maximum food I production in week 1 is 20,000 kg (all at 40 hours) or 30,000 kg (all at 60 hours). Given that some workers may be training, is there any constraint that would make it infeasible to meet the week 1 demand of 10,000 kg for food I, or should I assume the model will determine the optimal allocation and any infeasibility is handled by the late-delivery mechanism?

## Turn 27 - User Simulator

There is no constraint that would make it infeasible to meet the week 1 demand of 10,000 kg for food I. The model will determine the optimal allocation, and any infeasibility is handled by the late-delivery mechanism.

## Turn 28 - Generic Agent

QUESTION: The late-delivery penalty accrues per week that demand remains unmet. If demand from week 1 is not met in week 1 but is met in week 2, the penalty is 0.5 × 1 = 0.5 yuan/kg for food I. If it is not met until week 3, the penalty is 0.5 × 2 = 1.0 yuan/kg. Does this penalty apply to the original week's demand only, or does it also apply to the carried-over portion when it is eventually met (i.e., is the penalty calculated based on the original week the demand was due, or the week it was actually fulfilled)?

## Turn 28 - User Simulator

The penalty is calculated based on the original week the demand was due.

## Turn 29 - Generic Agent

QUESTION: The 50 new workers must be trained by the end of week 8, and training can only start in weeks 1, 3, 5, or 7. Since each skilled worker can train at most 3 new workers per block, and there are 4 blocks, the maximum total new workers that can be trained is 50 × 3 × 4 = 600, which far exceeds 50. Is there any constraint that limits the total number of new workers that can be trained across all blocks to exactly 50, or could the model choose to train fewer than 50 if it is cheaper (e.g., if the training cost outweighs the benefit)?

## Turn 29 - User Simulator

There is a constraint that limits the total number of new workers that can be trained across all blocks to exactly 50. The model must train exactly 50 new workers.

## Turn 30 - Generic Agent

QUESTION: The 50 new workers must be trained exactly, and they are not available for production during weeks 1-8. Since they don't contribute to production in the planning horizon, is the only cost associated with training them the 120 yuan/week wage paid to each trainee during their 2-week training period (240 yuan per trainee total), or are there other costs (e.g., a fixed training material cost, a cost for the skilled worker's time beyond their regular wage, or a cost for the training facility)?

## Turn 30 - User Simulator

The only cost associated with training them is the 120 yuan/week wage paid to each trainee during their 2-week training period (240 yuan per trainee total).