## Turn 1 - Generic Agent

QUESTION: When you say "a total of 50 new workers must be trained by the end of the 8th week," do you mean that 50 trainees must have *completed* their 2-week training (and thus be productive) by the end of week 8, or that 50 trainees must have *started* training by the end of week 8 (some of whom would still be in training at week 8's end)?

## Turn 1 - User Simulator

It means 50 trainees must have completed their 2-week training and be productive by the end of week 8.

## Turn 2 - Generic Agent

QUESTION: The brief says each skilled worker can train at most 3 new workers "in any two-week period" — does this mean a skilled worker who starts training 3 trainees in weeks 1–2 cannot start another batch until week 3 (i.e., the 3-per-2-weeks cap is a rolling window), or does it simply mean a skilled worker can have at most 3 trainees at a time and can start a fresh batch of up to 3 the week after the previous batch finishes?

## Turn 2 - User Simulator

It means a skilled worker can have at most 3 trainees at a time and can start a fresh batch of up to 3 the week after the previous batch finishes.

## Turn 3 - Generic Agent

QUESTION: While a skilled worker is training a batch of trainees, can that skilled worker still produce food (at the normal 10 kg/h or 6 kg/h rate), or is the skilled worker fully occupied with training and produces nothing during those two weeks?

## Turn 3 - User Simulator

The skilled worker is fully occupied with training and produces nothing during those two weeks.

## Turn 4 - Generic Agent

QUESTION: Can a skilled worker start a new batch of trainees in any week (e.g., week 1, week 2, week 3, ...), or can new training batches only start at the beginning of a two-week period (i.e., only in odd weeks 1, 3, 5, 7)?

## Turn 4 - User Simulator

A skilled worker can start a new batch of trainees in any week.

## Turn 5 - Generic Agent

QUESTION: When a skilled worker starts a batch of trainees in week t, do those trainees finish training and become productive at the end of week t+1 (i.e., they are available for production starting in week t+2), or do they become productive at the end of week t+2 (available starting in week t+3)?

## Turn 5 - User Simulator

They finish training and become productive at the end of week t+1, so they are available for production starting in week t+2.

## Turn 6 - Generic Agent

QUESTION: The brief gives a "weekly wage" of 360 yuan for a skilled worker and 120 yuan for a trainee during training — are these the only labor costs I should include, or is there also a separate cost (e.g., a hiring or training fee) incurred when a new worker is hired or starts training?

## Turn 6 - User Simulator

These are the only labor costs to include. There is no separate hiring or training fee.

## Turn 7 - Generic Agent

QUESTION: The brief mentions overtime at 60 hours/week with a weekly wage of 540 yuan — is 540 yuan the total weekly wage for a skilled worker who works 60 hours (i.e., 360 for the normal 40 hours plus 180 for the 20 overtime hours), or is 540 yuan an additional overtime premium paid on top of the normal 360 yuan weekly wage?

## Turn 7 - User Simulator

540 yuan is the total weekly wage for a skilled worker who works 60 hours.

## Turn 8 - Generic Agent

QUESTION: The overtime option (60 hours/week) — does it apply to all productive workers (skilled workers and newly-trained workers), or only to the original 50 skilled workers?

## Turn 8 - User Simulator

It applies to all productive workers, including both the original skilled workers and newly-trained workers.

## Turn 9 - Generic Agent

QUESTION: The brief gives compensation fees for late delivery (0.5 yuan/kg/week for food I, 0.6 yuan/kg/week for food II) — does this mean that if demand in a given week is not fully met, the shortfall can be carried over and delivered in a later week, incurring the compensation fee for each week of delay, or does it mean that any unmet demand in a week is simply lost and the compensation fee is a one-time penalty for the shortfall in that week?

## Turn 9 - User Simulator

The shortfall can be carried over and delivered in a later week, incurring the compensation fee for each week of delay.

## Turn 10 - Generic Agent

QUESTION: If demand is carried over to a later week, is there a limit on how many weeks a unit of demand can be delayed before it must be delivered (e.g., it must be delivered by the end of week 8), or can it be delayed indefinitely as long as the compensation fee is paid?

## Turn 10 - User Simulator

There is no limit on how many weeks a unit of demand can be delayed, as long as the compensation fee is paid.

## Turn 11 - Generic Agent

QUESTION: Is there any inventory holding cost for food that is produced in one week but delivered in a later week (beyond the late-delivery compensation fee), or is the late-delivery compensation fee the only cost associated with carrying unmet demand forward?

## Turn 11 - User Simulator

The late-delivery compensation fee is the only cost associated with carrying unmet demand forward.

## Turn 12 - Generic Agent

QUESTION: Is there any inventory holding cost for food that is produced in one week and stored to be delivered in a later week (i.e., producing ahead of demand), or is there no cost to holding finished goods inventory?

## Turn 12 - User Simulator

There is no cost to holding finished goods inventory.

## Turn 13 - Generic Agent

QUESTION: Is there any limit on the amount of finished goods inventory that can be held at the end of any week, or can inventory be carried forward without any capacity constraint?

## Turn 13 - User Simulator

There is no limit on the amount of finished goods inventory that can be held.

## Turn 14 - Generic Agent

QUESTION: The 50 newly-trained workers must be productive by the end of week 8 — does this mean they must have completed training by the end of week 8 (i.e., they can be used for production in weeks 7 and 8 if they finish early enough), or does it mean they must have completed training by the end of week 6 so that they are available for the full production weeks 7 and 8?

## Turn 14 - User Simulator

They must have completed training by the end of week 8. They can be used for production in weeks 7 and 8 if they finish early enough.

## Turn 15 - Generic Agent

QUESTION: Can a skilled worker who is currently training a batch of trainees (and thus producing nothing) also start a second batch of trainees in the same week, as long as the total number of trainees they have at any time does not exceed 3?

## Turn 15 - User Simulator

No, a skilled worker cannot start a second batch while already training a batch.

## Turn 16 - Generic Agent

QUESTION: When a skilled worker starts a batch of up to 3 trainees in week t, must they train exactly 3, or can they train fewer (e.g., 1 or 2) in that batch?

## Turn 16 - User Simulator

They can train fewer than 3 in a batch.

## Turn 17 - Generic Agent

QUESTION: The 50 newly-trained workers must be productive by the end of week 8 — does this mean they must have completed training by the end of week 8 (i.e., they can be used for production in weeks 7 and 8 if they finish early enough), or does it mean they must have completed training by the end of week 6 so that they are available for the full production weeks 7 and 8?

## Turn 17 - User Simulator

They must have completed training by the end of week 8. They can be used for production in weeks 7 and 8 if they finish early enough.

## Turn 18 - Generic Agent

QUESTION: The brief states "a total of 50 new workers must be trained by the end of the 8th week" — is this a hard constraint (exactly 50 must be trained, no more, no less), or is it a minimum (at least 50 must be trained, and training more is allowed)?

## Turn 18 - User Simulator

It is a minimum: at least 50 must be trained, and training more is allowed.

## Turn 19 - Generic Agent

QUESTION: Is the objective to minimize total cost (labor wages + overtime + late-delivery compensation), or is there a different objective (e.g., maximize profit, minimize total hours, etc.)?

## Turn 19 - User Simulator

The objective is to minimize total cost, including wages, overtime, and late-delivery compensation.

## Turn 20 - Generic Agent

QUESTION: The brief states that newly-trained workers "have the same production efficiency as skilled workers" — does this mean they can produce 10 kg/h of food I and 6 kg/h of food II, exactly like the original skilled workers?

## Turn 20 - User Simulator

Yes, they can produce 10 kg/h of food I and 6 kg/h of food II, exactly like the original skilled workers.

## Turn 21 - Generic Agent

QUESTION: The brief states that newly-trained workers receive 240 yuan/week — is this their weekly wage for all 8 weeks (i.e., they are paid 240 yuan/week from the week they start training through week 8), or is it their weekly wage only after they complete training (i.e., they are paid 120 yuan/week during the 2-week training period and 240 yuan/week after)?

## Turn 21 - User Simulator

They are paid 120 yuan/week during the 2-week training period and 240 yuan/week after they complete training.

## Turn 22 - Generic Agent

QUESTION: The brief states that a skilled worker who works 60 hours/week is paid 540 yuan total — is the production rate for those 60 hours simply 60 hours × the per-hour rate (e.g., 60 × 10 = 600 kg of food I), or is there a reduced efficiency during overtime hours?

## Turn 22 - User Simulator

The production rate for those 60 hours is simply 60 hours × the per-hour rate.

## Turn 23 - Generic Agent

QUESTION: Can a skilled worker who is training a batch of trainees in a given week also work overtime (60 hours) for training purposes, or is the training period fixed at 40 hours/week regardless of overtime?

## Turn 23 - User Simulator

The training period is fixed at 40 hours/week regardless of overtime.

## Turn 24 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 24 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.

## Turn 25 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 25 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.

## Turn 26 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 26 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.

## Turn 27 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 27 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.

## Turn 28 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 28 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.

## Turn 29 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 29 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.

## Turn 30 - Generic Agent

QUESTION: The brief states that a skilled worker who is training a batch of trainees is "fully occupied with training and produces nothing during those two weeks" — does this mean the skilled worker is paid the normal 360 yuan/week during those two weeks (since they are not producing), or are they paid a different rate while training?

## Turn 30 - User Simulator

The skilled worker is paid the normal 360 yuan/week during those two weeks.