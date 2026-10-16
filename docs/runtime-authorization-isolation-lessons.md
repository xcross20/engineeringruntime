# Runtime authorization and isolation: Rally MC-006 case study

**Status:** Engineering decision record and preflight guidance, not evidence that the runtime is live or safe.
**Recorded:** 2026-10-16
**Origin:** Rally MC-006 through MC-006C, Grok Build CLI 1.0.60 on macOS.

## The failure mode

Rally repeatedly completed offline adapter and security work, yet launched **zero autonomous coding-agent implementation sessions**. Passing suites (123, 144, 151 tests) and independent reviews did not establish a working end-to-end pilot. The coordinator conflated (a) owner authorization, (b) provider billing facts, (c) a technically enforceable cost ceiling, (d) runtime isolation, and (e) assignment authorization. Subsequent work orders restated blockers instead of finding a viable topology.

An owner-attested authorization was recorded, but `BILLING_POLICY_VERIFIED` and `OVERAGE_CONTROL_VERIFIED` correctly remained false under their original definitions. Do not set verification flags merely to satisfy a gate, and do not treat an owner statement as proof of technical enforcement.

## Evidence observed on the reported seat (not a general Grok guarantee)

- Grok Build weekly pool reported 43% used, period ending 2026-10-19T04:22:26Z.
- Prepaid balance reported 629 cents ($6.29).
- On-demand cap/used reported 0/0; monthly additional-usage limit/used reported 629/0 cents. **These are distinct controls; the monthly limit was not zero.**
- Auto-top-up rule had no enabled field and negative top-up/max values; a saved payment method existed. The report inferred no enabled auto-top-up rule; independently verify provider semantics before relying on this for future seats.
- A single `grok -p` ping reached the live endpoint; a subsequent billing read showed no change. **This was not an implementation pilot, nor proof that all later sessions are free.**
- Grok 1.0.60 exposed no per-session dollar-cap flag; finished-session usage could omit total cost. This does not itself disprove provider-side account-level caps.
- On this Mac, the current Grok process could read `~/.grok`; its attempted child-network denial was ineffective. `GROK_SANDBOX_MODE=enforce` refused shell commands without a platform backend. A stricter `sandbox-exec` profile denied home/network but also prevented the Grok executable and authentication from operating. The attempted CLI proxy override was not supported.
- Docker Desktop was installed but the daemon was not running. A container or VM can separate host filesystems, but **does not automatically isolate credentials from tools in the same guest**.
- Four Rally departments remained read-only, no pilot assignment was authorized, and the sealed verifier only supported constrained literal assertions.

## Durable operating rules

1. **Separate the development environment from the autonomous runtime under construction.** A blocked autonomous pilot must not automatically prohibit offline implementation, fixture tests, documentation, or independent review using separately authorized development tools.
2. **Represent distinct evidence explicitly:** `OWNER_ATTESTED`, `PROVIDER_ACCOUNT_CONTROL_VERIFIED`, `SESSION_COST_ENFORCED`, `RUNTIME_ISOLATION_VERIFIED`, and `ASSIGNMENT_AUTHORIZED` are different claims. Preserve existing project flag semantics and fail closed on unsatisfied required claims.
3. **Do not invent controls.** Never mark spending technically enforced based on a JSON field, owner attestation, a post-hoc usage report, or a CLI option that does not exist.
4. **Inspect provider-side controls before designing a bespoke billing gate.** Record plan/tier, weekly-pool treatment of headless calls, on-demand cap, monthly additional-usage cap, prepaid balance, auto-top-up status, payment-method exposure, timestamp, source, and the exact policy implication. A zero on-demand cap does not erase a nonzero monthly limit. Never publish account secrets.
5. **Choose a feasible runtime topology before adding policy layers.** If authenticated Grok and shell tools run in one process, a host seatbelt that blocks the credential also blocks Grok. Investigate an actual tool-execution boundary, then a disposable container/VM running the complete worker. Do not assume either approach solves in-guest credential access.
6. **Treat credential exposure separately from host containment.** No host home, repository, coordinator-state or reviewer-secret mounts in an untrusted worker. Prefer scoped, revocable, time-limited authentication where supported. Independently probe filesystem, network, subprocess and secret access. If the provider requires credentials accessible to arbitrary candidate commands, document and gate that residual risk rather than calling it isolated.
7. **Use one real, narrow pilot.** A dedicated writable, nontrading assignment with protected acceptance criteria must be authorized; existing read-only departments remain unchanged. A model ping, fixture worker, mock, or green unit-test suite does not count as an autonomous implementation.
8. **Evidence-backed outcomes only.** `PILOT_ACCEPTED` requires a real coding-agent session, provenance-bound candidate, independent verification and review, coordinator-only integration, regression and durable checkpoint. Otherwise report the specific blocker.
9. **Bound iteration.** After repeated identical blocking decisions, require a topology/capability review and a smallest falsifiable experiment, not another administrative gate or general-purpose orchestration layer.
10. **Do not bypass explicit constraints.** Owner permission to use an existing allowance does not authorize unexpected charges, exposing credentials, trading, deployment, or changing security flags without their stipulated evidence.

## Preflight decision sequence

1. Is there a separately authorized development tool? If yes, continue safe offline engineering even if the autonomous pilot is blocked.
2. Can the actual CLI run headlessly and execute a harmless tool command in the proposed isolated environment? If not, identify the missing runtime capability.
3. Is the provider's *account-level* charging behavior evidenced, and is any required hard stop actually enforced? If not, block chargeable execution, not unrelated offline work.
4. Does the chosen container/VM/tool boundary protect host resources, and is in-guest credential risk explicitly resolved or approved under the applicable policy? If not, block live tool execution.
5. Is one task narrowly authorized with protected tests and an independent reviewer? If not, prepare that assignment without expanding permissions globally.
6. Run one end-to-end pilot, capture actual session/commit/review/integration evidence, and stop.

## Next experiment

Evaluate a disposable Grok worker in Docker **only after starting the daemon and proving the actual CLI/tool behavior**, with no host-home or coordinator mounts. If Docker is unsuitable, evaluate a disposable Linux VM. Establish a credible authentication boundary and enforceable provider spending policy before any chargeable live run. Do not claim the container alone solves credential access. Keep the first pilot nontrading and one-shot.

**Source record:** User-supplied Rally MC-006C execution report, `docs/integration/MC-006C-execution-gap.md` at commit `1f27cafe6ad45a118dfed00e58e836bdef722260` (not independently inspected in this repository).
