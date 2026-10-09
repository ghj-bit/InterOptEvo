# Case facts for Judge

## Initial brief shown to Generic Agent
Visible unit IDs: U1, U5, U7, U10, U12, U2, U3
I need help planning the processing of parts on machines. A one-time setup cost is incurred for a machine if at least one part is processed on it, independent of the number of part types. Additionally, if part 1 is processed on machine A, then part 2 must be processed on machine B or C. Part 4 must be processed on machine B, and the number of parts processed on machine C should not exceed 3 types.

Unit processing costs:
Table 5-6
| Machine/Part | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| A            | $10$ | $20$ | $30$ | $40$ | $50$ | $60$ | $70$ | $80$ | $90$ | $100$ |
| B            | $15$ | $25$ | $35$ | $45$ | $55$ | $65$ | $75$ | $85$ | $95$ | $105$ |
| C            | $20$ | $30$ | $40$ | $50$ | $60$ | $70$ | $80$ | $90$ | $100$ | $110$ |

Setup costs: d_A = 100, d_B = 135, d_C = 200 yuan.

## Problem units
- U1 (context): I need help planning the processing of parts on machines.
- U2 (data): Unit processing costs:
Table 5-6
| Machine/Part | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
|--------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| A            | $10$ | $20$ | $30$ | $40$ | $50$ | $60$ | $70$ | $80$ | $90$ | $100$ |
| B            | $15$ | $25$ | $35$ | $45$ | $55$ | $65$ | $75$ | $85$ | $95$ | $105$ |
| C            | $20$ | $30$ | $40$ | $50$ | $60$ | $70$ | $80$ | $90$ | $100$ | $110$ |
- U3 (data): Setup costs: d_A = 100, d_B = 135, d_C = 200 yuan.
- U4 (objective): Minimize the total cost (processing costs plus setup costs).
- U5 (assumption): A one-time setup cost is incurred for a machine if at least one part is processed on it, independent of the number of part types.
- U6 (constraint): One piece of each of the 10 types of parts needs to be processed.
- U7 (constraint): If part 1 is processed on machine A, then part 2 must be processed on machine B or C.
- U8 (constraint): If part 1 is processed on machine B or C, then part 2 must be processed on machine A.
- U9 (constraint): Part 3 must be processed on machine A.
- U10 (constraint): Part 4 must be processed on machine B.
- U11 (constraint): Part 5 must be processed on machine C.
- U12 (constraint): The number of parts processed on machine C should not exceed 3 types.

## Hidden slot scoring rules
## H1: missing_objective
- Severity: P0
- Severity reason: Without knowing the objective, the agent cannot define what to minimize/maximize, making it impossible to build a valid optimization model.
- Problem unit ID: U4
- Semantic hit rule: The agent's question must explicitly ask about the objective or what is to be minimized/maximized in the problem.
- Reference acceptable questions:
  - What is the goal of this planning? Should we minimize cost, time, or something else?
  - Do we want to minimize the total cost, and does that include both processing and setup costs?
- Failure modes:
  - Assuming the problem is only about minimizing processing cost, ignoring setup costs.
  - Assuming the goal is to minimize the number of machines used.

## H2: exactly_one_piece_per_part
- Severity: P0
- Severity reason: Without this constraint, the agent would not know the required quantity of each part, making the problem fundamentally ambiguous and the model invalid.
- Problem unit ID: U6
- Semantic hit rule: The agent's question must ask about the quantity or number of pieces of each part to be processed, specifically referencing the ten part types.
- Reference acceptable questions:
  - How many pieces of each part type are required? Just one piece per type?
  - Do we need to process exactly one unit of each of the ten parts, or can we process multiple or zero?
- Failure modes:
  - Assuming that some parts may not need to be processed.
  - Assuming multiple pieces per part type are allowed.

## H3: reverse_conditional_part1_part2
- Severity: P1
- Severity reason: Without this reverse conditional, the relationship between parts 1 and 2 is only half-specified, which would lead to a materially inaccurate feasible region in the model.
- Problem unit ID: U8
- Semantic hit rule: The agent's question must explicitly ask about the machine assignment for part 2 when part 1 is processed on machine B or C.
- Reference acceptable questions:
  - Is there any rule for part 2 when part 1 is on machine B or C?
  - Does it also work the other way? If part 1 is on B or C, must part 2 be on A?
- Failure modes:
  - Assuming no restriction applies to part 2 when part 1 is on B or C.
  - Assuming the conditional only applies when part 1 is on machine A.

## H4: part3_on_machine_A
- Severity: P1
- Severity reason: This is a hard assignment constraint; missing it would produce a model that allows invalid machine choices, leading to solutions that do not reflect the real requirement.
- Problem unit ID: U9
- Semantic hit rule: The agent's question must ask about a mandatory machine assignment for part 3 (or the third part).
- Reference acceptable questions:
  - Is part 3 required to be processed on a specific machine?
  - Do we have a fixed machine for part 3?
- Failure modes:
  - Assuming part 3 can be assigned to any machine.
  - Assuming part 3 must be processed on machine B or C.

## H5: part5_on_machine_C
- Severity: P1
- Severity reason: This fixed assignment directly restricts the solution space; without it the model would not enforce the intended machine choice and would produce incorrect solutions.
- Problem unit ID: U11
- Semantic hit rule: The agent's question must ask about a specific machine requirement for part 5 (or the fifth part).
- Reference acceptable questions:
  - Is there a prescribed machine for part 5?
  - Must part 5 be on machine C?
- Failure modes:
  - Assuming part 5 can be processed on any machine.
  - Assuming part 5 must be on machine A or B.


# Atomic Question Map

Q1 (turn 1): Must each part type be processed on exactly one machine, or can a part type be processed on multiple machines?
Q2 (turn 2): What is the objective for planning the processing of parts on machines?
Q3 (turn 3): Must all 10 part types be processed, or can some part types be left unprocessed?
Q4 (turn 4): Is the requirement that if part 1 is processed on machine A then part 2 must be processed on machine B or C a hard constraint that must always be satisfied, or a soft preference that can be violated at a cost?
Q5 (turn 5): Is the requirement that the number of part types processed on machine C should not exceed 3 a hard constraint that must always be satisfied, or a soft preference that can be violated at a cost?
Q6 (turn 6): Is the one-time setup cost incurred once for each machine that processes at least one part type, or once for each machine-part type combination?
Q7 (turn 7): Is the requirement only that if part 1 is processed on machine A, then part 2 must be processed on machine B or C, or does it also require that if part 2 is processed on machine B or C, then part 1 must be processed on machine A?

# Full Transcript

## Turn 1 - Generic Agent

QUESTION: Must each part type be processed on exactly one machine, or can a part type be processed on multiple machines?

## Turn 1 - User Simulator

Each part type is processed on exactly one machine.

## Turn 2 - Generic Agent

QUESTION: What is the objective for planning the processing of parts on machines?

## Turn 2 - User Simulator

Minimize the total cost, which includes both the processing costs per part on each machine and any one-time setup costs if a machine is used.

## Turn 3 - Generic Agent

QUESTION: Must all 10 part types be processed, or can some part types be left unprocessed?

## Turn 3 - User Simulator

All 10 part types must be processed — exactly one piece of each.

## Turn 4 - Generic Agent

QUESTION: Is the requirement that if part 1 is processed on machine A then part 2 must be processed on machine B or C a hard constraint that must always be satisfied, or a soft preference that can be violated at a cost?

## Turn 4 - User Simulator

It's a hard constraint that must always be satisfied.

## Turn 5 - Generic Agent

QUESTION: Is the requirement that the number of part types processed on machine C should not exceed 3 a hard constraint that must always be satisfied, or a soft preference that can be violated at a cost?

## Turn 5 - User Simulator

It's a hard constraint that must always be satisfied.

## Turn 6 - Generic Agent

QUESTION: Is the one-time setup cost incurred once for each machine that processes at least one part type, or once for each machine-part type combination?

## Turn 6 - User Simulator

It's incurred once for each machine that processes at least one part type, independent of the number of part types.

## Turn 7 - Generic Agent

QUESTION: Is the requirement only that if part 1 is processed on machine A, then part 2 must be processed on machine B or C, or does it also require that if part 2 is processed on machine B or C, then part 1 must be processed on machine A?

## Turn 7 - User Simulator

It's only the one direction: if part 1 is processed on machine A, then part 2 must be processed on machine B or C. There's no requirement going the other way.

## Turn 8 - Generic Agent

READY_TO_MODEL

Formulatable confidence: 0.950

Confidence rationale: The request is sufficiently specified for a unique optimization formulation. The objective is to minimize total processing plus one-time setup costs; each of the 10 part types must be assigned to exactly one machine; setup cost is a fixed charge per used machine; the conditional rule is a one-way hard implication; part 4 must be on machine B; and machine C may process at most 3 distinct part types. The only minor residual ambiguity is the exact interpretation of the machine C limit, but the wording '3 types' supports the distinct-part-type reading.

Summary: Formulate a binary assignment model for 10 part types and 3 machines (A, B, C). Decision variables assign each part type to exactly one machine, with binary machine-use indicators. Objective: minimize sum of processing costs plus setup costs d_A=100, d_B=135, d_C=200 for each used machine. Constraints: each part type assigned to exactly one machine; machine-use indicators linked to assignments; part 4 must be on machine B; if part 1 is on machine A then part 2 must be on machine B or C; at most 3 distinct part types may be assigned to machine C.