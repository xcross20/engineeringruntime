# Evidence standards

Every executed check should record: requirement_id, status, trusted command, exit_code, duration_ms, source_commit, fixture_version, environment identifier, artifact references, and failure summary. Artifacts may include JUnit XML, traces, screenshots, SQL evidence and profiler output.

Statuses: PASS, FAIL, INCONCLUSIVE, BLOCKED. A tool invocation or agent claim without captured exit code is not PASS. Reports should record skipped checks and reasons. Hash artifacts when practical. Redact credentials, personal data and connection strings; never attach secrets. Reviewers must verify independently and cannot accept their own code.
