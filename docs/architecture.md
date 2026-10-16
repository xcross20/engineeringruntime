# Architecture

Approved mission + project adapter -> deterministic Controller -> isolated Builder -> candidate SHA -> independent Reviewer -> trusted verifier -> evidence validator -> ACCEPT / CONTINUE / BLOCKED / RETHINK. Persistent Controller state and leases live outside Builder worktrees. Project adapters define argv checks and permitted paths; they do not define or override Controller trust policies.

Initial technical bias: Python 3.11+, subprocess CLI adapters, git worktrees, SQLite transactions, JSON schema evidence, and pytest. No cloud, graphs, UI or multi-agent swarm until a real verified loop exists. Mandatory threat cases: injected instructions in target repository, falsified reviewer reports, missing check results, stale SHA, two workers taking same lease, mid-cycle crash and unaudited policy exceptions.
