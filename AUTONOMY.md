# Autonomous engineering contract

## Operating model
The application is the product. Autonomous engineering is the operating model. The owner authorizes a mission, budget, security limits and approved work-order queue once; the runtime handles ordinary engineering transitions.

## Roles and separation
- **Owner:** Mission/scope changes, risk boundaries, deployment, merge, external financial effects and budget ceilings.
- **Builder:** Implements one authorized slice on a non-default branch; cannot review or accept itself.
- **Independent Reviewer:** Isolated new session and clean worktree at exact SHA, independently executes approved tests and adversarial checks.
- **Deterministic Controller:** Governs leases, immutable work-order definitions, runtime budgets, check attestations, acceptance and retry/advance decisions. Never trusts agent prose as evidence.
- **Planner:** Drafts bounded future work orders for authorized queue only.

## Lifecycle
READY -> BUILD -> VERIFY -> REVIEW -> GATE
- ACCEPT: all mandatory trusted checks pass, no unresolved P0/P1, exact reviewed SHA and independent provenance; advance only already approved NEXT.
- CONTINUE: verified, in-scope repairable defect and remaining budget. Repair creates new SHA, requiring fresh independent review.
- BLOCKED: missing evidence, failed risk boundaries, budgets, lease conflict, unexpected dependency risk, unavailable trustworthy tool.
- RETHINK: strategy/scope changes or owner-level decisions required.

## Safety invariants
No autonomous merges, deployments, production secrets, real payments, or unrelated filesystem/network access. Agents cannot edit Controller policy/trust roots or revise risk exceptions. Sanitized logs and least-privilege env. All subprocess/network permissions must be explicit and budget enforced. Fail closed if headless model expenses cannot be bounded.

## Evidence
All artifacts bind to immutable candidate/review SHA, session IDs, exact commands/exit codes, trusted verifier run metadata, policy version, findings and Controller decision. If evidence or state is missing, do not claim success.

## Progress
First build one Builder + one Reviewer + one Controller; no multi-agent swarm. Reuse tested components of Rally/EARS/VentureOS where possible. Establish durable SQLite transactional state and crash-safe, fenced lease before unattended run. Test recovery and concurrent workers.
