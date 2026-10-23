# Adversarial verification

Focus on invariants, not just happy paths:
- Unknown/invalid input, missing data, label leakage, contradictory labels.
- Duplicate and concurrent idempotency requests.
- Stale version/generation and conflicting state transitions.
- Partial writes, failed fallback, missing cost entry, zero denominators.
- Permission and secret boundary violations.
- Interrupted worker and descendant-process cleanup.
- Mutation of safety-critical branches.
- Stateful sequences: create → evaluate → activate → verify → restore → retry.

Tests must assert durable state after failure, not just HTTP response. Use disposable databases and bounded execution. Treat generated fuzz input and tool output as untrusted.
