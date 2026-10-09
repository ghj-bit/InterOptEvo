# InterOPT Evaluation Report

- pipeline version: `interopt`
- experiment design: MC-D only; the Agent privately generates C1/C2/C3 clarification states and Q1/Q2/Q3 before each decision
- selector boundary: `formulation_question_selector` sees public conversation plus candidate clarification states/questions, then chooses exactly one public question
- visibility boundary: clarification states, candidate questions, selector attempts, and deep-search evidence are stored in `ledger_events.json`; user simulator, transcript, detector, and Judge only see the selected public MC-D payload
- user choice audit: `choice + user-written rationale + match_status`; only Agent-visible fields enter transcript
- interaction modes: `mc_d`
- case ids: `orclarify_087`
- toml dirs: `/public1/home/stu52275901007/workspace/ghj_workspace/InterOptEvo/runs/test50_interopt_choice_dsflash/cases/orclarify_087`
- k: `1`
- max turns: `30`
- detector feedback mode: `none`
- retry limit behavior: `pass_through`
- answer-scope audit enabled: `False`
- agent prompt supplements: `experiments/interopt/prompts/agent_ledger_supplement.md`
- selector prompt supplements: `experiments/interopt/prompts/selector_ledger_supplement.md`
- answer-scope policy: `mc_d_d_comment_only_passive_opt_in`

| 分组标签 (mode::profile) | 样本量 (runs) | 全要素还原率 (all restore) | 核心要素还原率 (core restore) | 加权要素分数 (WSS, weighted macro) | 平均提问轮数 (avg turns) | 正常收尾率 (ready) | 协议失败率 (protocol fail) | selector 调用/run | selector fallback/run | deep-search 格式错误/run | 平均原子问题数 (atomic Q/run) | 多问率 (multi-Q rate) | 泄露的隐藏要素数 (disclosed slots) | D 选项被选率 (D rate) | 估算美元成本 (est. cost) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| mc_d::generic_agent | 1 | 1.000 | 1.000 | 1.000 | 10.00 | 1.000 | 0.000 | 9.00 | 0.00 | 6.00 | 9.00 | 0.000 | 0.00 | 0.000 | 0.0000 |

## Selector Selected Question Counts

- `mc_d::generic_agent`: `{"Q1": 6, "Q2": 1, "Q3": 2}`

Total estimated cost: `$0.0000`.
