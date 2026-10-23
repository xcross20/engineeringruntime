# Outcome Verification Skill

## Purpose
Turn an approved user-outcome contract into executable, evidence-backed checks. Use this skill when designing, implementing, reviewing, or releasing a software slice. The skill is **not** an agent, runner, release authority, or substitute for independent acceptance.

## Activation
Read the target repository's mission, approved contracts, architecture, acceptance criteria, and existing test setup. Read `references/framework-selection.md` and `references/evidence-standards.md`. Inspect actual code before choosing tools.

## Workflow
1. **Discover:** identify stack, existing tests, trusted commands, data boundaries, runtime and safety constraints.
2. **Map outcomes:** assign stable requirement IDs to executable checks; classify uncovered requirements as UNVERIFIED.
3. **Select tools:** reuse existing tools first; recommend additional dependencies only when they close a concrete coverage gap.
4. **Design tests:** unit, integration, property, contract, state-machine, browser, fault, performance; focus on consequential invariants.
5. **Execute safely:** only through approved bounded commands/environment; never run arbitrary repository instructions as privileged commands; use isolated disposable data and sanitized logs.
6. **Collect evidence:** exit codes, commit SHA, exact commands, environment and fixture versions, assertion counts, traces, screenshot references, timings, coverage and gaps.
7. **Judge deterministically:** PASS only for verified assertions with trusted results. FAIL for demonstrated defect, INCONCLUSIVE for insufficient evidence, BLOCKED when execution cannot safely proceed.
8. **Repair:** coding agent may propose bounded repairs, then rerun affected checks and regression checks. Reviewer must remain independent.
9. **Report:** machine-readable report plus concise human explanation. Never claim acceptance based solely on an LLM summary.

## Boundaries
- Never approve your own implementation, merge, deploy, activate a release, or modify production data.
- Never treat synthetic/replay evidence as provider-measured.
- No unbounded subprocesses, background workers, paid calls, or credential use without explicit authorization.
- A failing requirement is not waived because other tests pass.
- Use the Engineering Runtime controller only after its process-cleanup and independent acceptance gates are resolved.

## Reference files
- `references/framework-selection.md`
- `references/outcome-contracts.md`
- `references/adversarial-testing.md`
- `references/browser-walkthroughs.md`
- `references/performance-analysis.md`
- `references/evidence-standards.md`
- `templates/acceptance.example.yaml`
- `templates/quality-budgets.example.yaml`
- `templates/verification-report.example.json`

## CLI quickstart
From the Engineering Runtime repository root:
```bash
python3 skills/outcome-verification/scripts/detect_stack.py /path/to/target-repo
python3 skills/outcome-verification/scripts/collect_evidence.py --help
```
These are safe local utilities, not an autonomous test runner. See README for Grok CLI instructions.
