# Engineering Runtime

Reusable, evidence-gated autonomous engineering across project repositories.

**Status: FOUNDATION_SCAFFOLD (not a running autonomous controller).**

## Mission
One approved work order -> isolated Builder -> independent Reviewer -> trusted checks -> deterministic Controller -> ACCEPT / CONTINUE / BLOCKED / RETHINK -> next preapproved task. The system stops for unverified evidence, missing budgets, risk boundaries, or authority decisions. No autonomous merge, production deploy or external financial operations.

## Source projects to audit
- Rally: https://github.com/xcross20/rally_top_signal_tester
- EARS: https://github.com/xcross20/EARS (EARS-003 product ACCEPT does not certify its harness)
- VentureOS: https://github.com/xcross20/ventureos

## Bootstrap plan
- ERT-001: pin and audit source harnesses at exact SHAs; ADOPT/ADAPT/REJECT each module based on tests.
- ERT-002: smallest real Builder/Reviewer/Controller loop; safe headless execution, immutable SHA, worktree isolation, SQLite recovery and leases.
- ERT-003: adversarial provenance gates and bounded repair; replay EARS-003 durability failure.
- ERT-004: same runtime operates EARS and Rally via project-specific adapters; three consecutive approved unattended slices.

No agent calls, tests or acceptance decisions have been executed in this bootstrap commit.
