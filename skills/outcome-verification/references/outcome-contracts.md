# Executable outcome contracts

Each requirement must have a stable ID, source document/version, business meaning, evidence expectation, test command or case identifier, and status.

Rules:
- Outcome assertions are not the same as UI visibility or HTTP 200.
- Map every critical outcome to at least one independently observable assertion.
- Missing evidence => INCONCLUSIVE; missing execution => UNVERIFIED in planning and INCONCLUSIVE in final acceptance.
- Distinguish source contract requirements from new recommendations.
- Denominator zero must not be silently reported as success.
- Keep source version, fixture version, revision and evaluated cohort bound to the report.
- If the contract changes, regenerate mappings and require approval.
