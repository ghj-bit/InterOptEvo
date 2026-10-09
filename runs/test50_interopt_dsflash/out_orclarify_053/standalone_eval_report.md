# Detector-Agent Standalone Evaluation Report

This run uses independent protocol detectors around the interactive OR modeling pipeline.

- Pipeline mode: `fixed_question_only`
- Detector feedback mode: `visible`
- Retry limit behavior: `pass_through`
- Agent detector records the number of independent clarification questions in each Agent message
- Agent resampling is used only for structurally invalid messages: zero-question non-stop responses or READY_TO_MODEL mixed with questions
- User-answer monitoring enabled: `False`
- If enabled, User answers are passively audited for scope violations and hidden-slot disclosure; they are not retried
- In `none` feedback mode, detector findings are logged but never injected into Agent/User context
- In `protocol_failed` mode, exceeding retry limits stops the current case instead of passing through

## Run Configuration

- TOML dir: `/public1/home/stu52275901007/workspace/ghj_workspace/InterOptEvo/runs/test50_interopt_fp8/cases/orclarify_053`
- K: `1`
- max turns: `30`
- agent profiles: `deepseek_v4_flash`
- detector profile: `deepseek_v4_flash`
- user profile: `deepseek_v4_flash`
- judge profile: `deepseek_v4_flash`
- prompts dir: `/public1/home/stu52275901007/workspace/ghj_workspace/InterOptEvo/experiments/open_interopt/prompts`
- Max agent retries per turn: `3`
- Max user retries per turn: `3`

## Summary

Core exact restore uses only P0/P1 slots. Unresolved P2 slots do not affect this metric.

| agent | runs | all-slot exact restore | core exact restore | weighted macro | weighted micro | accepted turns | attempted turns | ready rate | protocol failure rate | failure types | agent retries/run | atomic questions/run | multi-question turn rate | avg questions/question-turn | question checks/run | structural invalid/run | answer audits/run | answer scope violations/run | answer disclosed slots/run | answer multi-slot disclosures/run | silent assumptions/run | stopping mismatch | est. cost USD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| deepseek_v4_flash | 1 | 0.000 (0) | 0.000 (0) | 0.000 | 0.000 | 2.00 | 3.00 | 0.000 | 1.000 | gap_search_error=1 | 0.00 | 2.00 | 0.000 | 1.00 | 2.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | 3.00 | 1.000 | 0.0000 |

## Candidate Question Selection and READY Confidence

### deepseek_v4_flash

- candidate question events per run: `2.000`
- candidate question parse rate: `1.000`
- candidate question complete rate: `1.000`
- candidate questions per ASK: `3.000`
- selected candidate score mean: `0.925`
- READY confidence count: `0`
- READY confidence parse rate: `0.000`
- mean READY confidence: `NA`
- READY true formulatable rate: `NA`
- high-confidence error rate: `NA`
- Brier score: `NA`


Total estimated cost: `$0.0000`.

Detailed per-run transcripts and judge JSON files are stored under the run directory.
