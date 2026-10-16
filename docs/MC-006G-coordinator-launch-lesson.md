# MC-006F / MC-006G: diagnose the coordinator before rebuilding the provider environment

**Decision record — 2026-10-16.** Applies to Engineering Runtime and Rally. This documents user-provided execution reports, not an independently reproduced live pilot.

## Confirmed in the reported host workflow

- `grok models` responded `You are logged in with grok.com` and default model `grok-4.7`.
- Host authentication uses an existing OIDC session (`~/.grok/auth.json`, `auth_mode=oidc`, issuer `auth.x.ai`); `XAI_API_KEY`, `GROK_DEPLOYMENT_KEY`, and `GROK_CODE_XAI_API_KEY` were unset. **Unset API-key environment variables do not imply missing CLI authentication.**
- An interactive Grok session and an earlier `grok -p` ping worked. The interactive host development session had sandbox off; it was **not** an isolated worker.
- Auto Top-up's `enabled` is a proto3 boolean. The Grok client interprets an omitted JSON `enabled` field as false; its test corroborates that behavior. The live response omitted the field. Separate settings showed `on_demand_enabled=null` and `onDemandCap=0`. A saved payment method is not by itself an enabled automatic charge. Record exact provider/client evidence and do not infer a per-session dollar cap.
- The coordinator's `start_session` returned `started=False` **before executing argv**. Its planned `--sandbox strict` was also different from the known working host command. **The immediate launch failure was coordinator refusal, not an API-key failure.**
- On the tested Mac, Grok's in-process tools could access host OIDC credentials, and child-network denial did not provide the claimed boundary. Therefore a working host session is not proof of isolated autonomous execution.
- Reported Rally source: `docs/integration/MC-006F-host-workflow.md` at `710deae`. Earlier MC-006D container experiment demonstrated a Linux Grok CLI could print its version in a no-host-home container, but not an authenticated isolated implementation.

## Required debugging sequence

1. **Reproduce the last known working CLI command.** Check `grok models`, actual login mode, supported flags, cwd, sandbox profile, and a separately authorized harmless command. Never print, copy or commit auth tokens.
2. **Trace the caller before changing infrastructure.** Instrument assignment selection → authorization → adapter → `start_session` → process spawn. For every `started=False`, report exact source location, evaluated condition, observed value, and whether any argv executed.
3. **Classify the stop:** (a) incorrect launch logic; (b) intentional policy refusal; (c) unsupported CLI flag; (d) missing provider capability; (e) missing isolated execution boundary. Fix (a) with regression tests; preserve (b) unless its policy is properly satisfied.
4. **Maintain two explicit profiles.** `HOST_DEVELOPMENT` uses the existing authenticated CLI under its actual host trust model and does not claim sandbox isolation. `ISOLATED_AUTONOMOUS_WORKER` requires independent credential/isolation/spend/assignment verification. Do not weaken the latter or re-label the former.
5. **Do not create credentials by assumption.** Never demand `XAI_API_KEY` for a functioning OIDC CLI. Introduce a separate credential only when a genuinely isolated topology requires it and the provider supports it.
6. **Read provider schemas, not just JSON presence.** In proto3, omitted non-optional scalar bool can represent false. Corroborate with client code/tests and account state; don't require an impossible explicit `false` field.
7. **Separate authorization from verification.** Owner-attested spending permission is not proof of technically enforced spending controls. Keep project flags semantically accurate; no purchases, extra charges, or secret exposure without applicable authorization.
8. **Measure the actual milestone.** A green test suite, fixture, model ping, or successful host interactive session is not a completed isolated autonomous pilot. Require coordinator-spawned session identity, real implementation candidate, independent verification/review, accepted integration (if authorized), and checkpoint.
9. **After two identical blocked cycles, stop adding gates.** Produce a differential report: known-working invocation vs generated invocation, launch decision trace, smallest falsifiable next experiment. Continue separately authorized offline engineering while live isolated execution remains blocked.

## Regression requirements for adapters and coordinators

- OIDC-authenticated CLI with API-key env vars absent does **not** trigger a fabricated `MISSING_API_KEY` error.
- `started=False` emits a structured refusal reason and `argv_executed=false`; no report may claim the CLI itself failed.
- Host profile never inherits `--sandbox strict` from isolated profile without compatibility validation.
- An isolated profile cannot silently fall back to sandbox-off host mode.
- Omitted proto3 `enabled` is parsed according to schema, with evidence of the exact semantics; other charging mechanisms remain separately checked.
- No credential is copied into an untrusted container or printed in logs.
- A successful ping does not set `PILOT_ACCEPTED`.

## Actionable next step

Implement MC-006G as a **launch-decision trace and minimal host-development integration test**, not another billing framework. Inspect the coordinator's real `start_session` branch and compare its argv with the working host invocation. Repair incorrect refusals without bypassing valid isolation or spending gates. The isolated autonomous pilot remains a separate unsatisfied milestone until its own requirements are demonstrated.

**Cross-reference:** Engineering Runtime also has a pending PR documenting the broader MC-006 authorization/isolation case study; these two records are complementary.
