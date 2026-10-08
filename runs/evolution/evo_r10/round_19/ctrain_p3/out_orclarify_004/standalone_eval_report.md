# Detector-Agent Standalone Evaluation Report

This run uses independent protocol detectors around the interactive OR modeling pipeline.

- Pipeline mode: `passive_question_audit`
- Detector feedback mode: `none`
- Retry limit behavior: `pass_through`
- Agent detector records the number of independent clarification questions in each Agent message
- Agent resampling is used only for structurally invalid messages: zero-question non-stop responses or READY_TO_MODEL mixed with questions
- User-answer monitoring enabled: `False`
- If enabled, User answers are passively audited for scope violations and hidden-slot disclosure; they are not retried
- In `none` feedback mode, detector findings are logged but never injected into Agent/User context
- In `protocol_failed` mode, exceeding retry limits stops the current case instead of passing through

## Run Configuration

- TOML dirs: `/public1/home/stu52275901007/workspace/ghj_workspace/InterOpt/runs/evolution/cases/orclarify_004`
- K: `1`
- max turns: `30`
- agent profiles: `generic_agent`
- detector profile: `detector`
- user profile: `user_simulator`
- judge profile: `judge`
- prompts dir: `/public1/home/stu52275901007/workspace/ghj_workspace/InterOpt/runs/evolution/evo_r10/policies/r19_candidate`
- Max agent retries per turn: `0`

## Summary

Core exact restore uses only P0/P1 slots. Unresolved P2 slots do not affect this metric.

| agent | runs | all-slot exact restore | core exact restore | weighted macro | weighted micro | accepted turns | attempted turns | ready rate | protocol failure rate | failure types | agent retries/run | atomic questions/run | multi-question turn rate | avg questions/question-turn | question checks/run | structural invalid/run | answer audits/run | answer scope violations/run | answer disclosed slots/run | answer multi-slot disclosures/run | silent assumptions/run | stopping mismatch | est. cost USD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| generic_agent | 1 | 1.000 (1) | 1.000 (1) | 1.000 | 1.000 | 7.00 | 7.00 | 1.000 | 0.000 | none=1 | 0.00 | 7.00 | 0.167 | 1.17 | 7.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.000 | 0.0000 |

Total estimated cost: `$0.0000`.

Detailed per-run transcripts and judge JSON files are stored under the run directory.
