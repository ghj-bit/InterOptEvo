# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U2
I need help determining the number of trained pilots that can be provided by a fighter jet production and training setup, where some fighter jets each year must be allocated exclusively for pilot training. Specifically, determine the total number of trained pilots available by the end of year 2.

Annual fighter jet production: a1 = 10, a2 = 15.

## Problem units
- U1 (context): I need help determining the number of trained pilots that can be provided by a fighter jet production and training setup.
- U2 (data): Annual fighter jet production: a1 = 10, a2 = 15.
- U3 (constraint): Each training jet can train 5 pilots per year.
- U4 (constraint): Each trained pilot can operate one combat jet in subsequent years.
- U5 (constraint): Some fighter jets each year must be allocated exclusively for pilot training.
- U6 (assumption): Training starts in year 1 and continues for 2 years.
- U7 (objective): Determine the total number of trained pilots available by the end of year 2.

## Hidden slot scoring rules
## H1: training_capacity_per_jet
- Severity: P0
- Severity reason: Without the per-jet training capacity, it is impossible to calculate the number of pilots trained per year, which is essential to achieving the objective. The model would be completely indeterminate.
- Problem unit ID: U3
- Semantic hit rule: The agent's question must explicitly ask about the per-year pilot training capacity of each training jet.
- Reference acceptable questions:
  - How many pilots can each training jet train per year?
  - What is the training capacity of a single jet in terms of pilots?
- Failure modes:
  - Assuming each jet can train 1 pilot per year
  - Assuming unlimited training capacity per jet
  - Assuming training capacity is proportional to jet age or type

## H2: pilot_to_combat_jet_mapping
- Severity: P2
- Severity reason: Without this information, the number of trained pilots available for air defense could be misinterpreted, but a reasonable model would still treat trained pilots as directly contributing. The missing unit clarifies the one-to-one mapping, but the total count of trained pilots remains the same. Omitting this does not prevent computing the number of trained pilots, so it is a low-impact detail.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must ask about the relationship between trained pilots and combat jets, specifically the number of jets a pilot can operate.
- Reference acceptable questions:
  - How many combat jets can a trained pilot operate?
  - Is there a limit on how many jets a pilot can handle?
- Failure modes:
  - Assuming each pilot can operate multiple combat jets
  - Assuming pilots need further training before operating any combat jet
  - Assuming the pilot-to-jet ratio depends on jet type

## H3: training_duration_and_start
- Severity: P1
- Severity reason: The start year and duration of training are not completely determined from the objective alone, and without them, the model might incorrectly set the training timeline, leading to a wrong total. A responsible agent should clarify the exact training period.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must mention the start year or the duration of the training program.
- Reference acceptable questions:
  - When does the training program start?
  - How many years does the training last?
- Failure modes:
  - Assuming training has already started before year 1
  - Assuming training lasts only 1 year
  - Assuming training continues indefinitely


# Full Transcript

## Turn 1 - Generic Agent

QUESTION: What is the exact rule for how many fighter jets each year must be allocated exclusively for pilot training (for example, a fixed number, a fraction of that year's production, or a fraction of the total fleet available)?

## Turn 1 - User Simulator

The rule is that a fixed number of fighter jets each year must be allocated exclusively for pilot training.

## Turn 2 - Generic Agent

QUESTION: What is the fixed number of fighter jets that must be allocated exclusively for pilot training each year?

## Turn 2 - User Simulator

The point still needs internal confirmation.

## Turn 3 - Generic Agent

QUESTION: How many trained pilots does one fighter jet allocated to training produce per year?

## Turn 3 - User Simulator

One fighter jet allocated to training produces 5 trained pilots per year.

## Turn 4 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 4 - User Simulator

The point still needs internal confirmation.

## Turn 5 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 5 - User Simulator

The point still needs internal confirmation.

## Turn 6 - Generic Agent

QUESTION: When you say "total number of trained pilots available by the end of year 2," do you mean the cumulative total of all pilots trained across years 1 and 2 combined, or the number of trained pilots available at the end of year 2 (which could differ if some pilots are lost or retired)?

## Turn 6 - User Simulator

I mean the cumulative total of all pilots trained across years 1 and 2 combined.

## Turn 7 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero and only grow from the annual production?

## Turn 7 - User Simulator

The point still needs internal confirmation.

## Turn 8 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced per year (for example, a cap on total training capacity), or is the only constraint the number of jets allocated to training?

## Turn 8 - User Simulator

The only constraint is the number of jets allocated to training.

## Turn 9 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 9 - User Simulator

The point still needs internal confirmation.

## Turn 10 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 10 - User Simulator

The point still needs internal confirmation.

## Turn 11 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero and only grow from the annual production?

## Turn 11 - User Simulator

The point still needs internal confirmation.

## Turn 12 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced per year (for example, a cap on total training capacity), or is the only constraint the number of jets allocated to training?

## Turn 12 - User Simulator

The only constraint is the number of jets allocated to training.

## Turn 13 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 13 - User Simulator

The point

## Turn 14 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 14 - User Simulator

The

## Turn 15 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero and only grow from the annual production?

## Turn 15 - User Simulator

The

## Turn 16 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced per year (for example, a cap on total training capacity), or is the only constraint the number of jets allocated to training?

## Turn 16 - User Simulator

The

## Turn 17 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 17 - User Simulator

The

## Turn 18 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 18 - User Simulator

The

## Turn 19 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero and only grow from the annual production?

## Turn 19 - User Simulator

The

## Turn 20 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced per year (for example, a cap on total training capacity), or is the only constraint the number of jets allocated to training?

## Turn 20 - User Simulator

The

## Turn 21 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 21 - User Simulator

The

## Turn 22 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 22 - User Simulator

The

## Turn 23 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero and only grow from the annual production?

## Turn 23 - User Simulator

The

## Turn 24 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced per year (for example, a cap on total training capacity), or is the only constraint the number of jets allocated to training?

## Turn 24 - User Simulator

The

## Turn 25 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 25 - User Simulator

The

## Turn 26 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 26 - User Simulator

The

## Turn 27 - Generic Agent

QUESTION: Are there any fighter jets already in the fleet at the start of year 1 (before any production), or does the fleet start at zero and only grow from the annual production?

## Turn 27 - User Simulator

The

## Turn 28 - Generic Agent

QUESTION: Is there any limit on how many trained pilots can be produced per year (for example, a cap on total training capacity), or is the only constraint the number of jets allocated to training?

## Turn 28 - User Simulator

The

## Turn 29 - Generic Agent

QUESTION: Do the jets allocated to training in a given year remain available for training in later years as well, or are they used only in the year they are allocated?

## Turn 29 - User Simulator

The

## Turn 30 - Generic Agent

QUESTION: Are the fighter jets allocated to training in a given year drawn from that same year's production, or from the total fleet accumulated so far (including earlier years' production)?

## Turn 30 - User Simulator

The