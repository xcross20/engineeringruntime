# Efficiency and performance

Define baseline and budgets before measuring. Measure:
- test wall time, retry count, flaky failures
- DB query count and query duration per operation
- p50/p95 latency under fixed concurrency
- browser journey duration and failed requests
- mutation score on critical code
- requirement coverage and evidence completeness
- agent repair cycles and changed-file churn

Use identical fixtures, environment, concurrency and warmup. Distinguish synthetic measurements from provider production results. Treat noisy differences as INCONCLUSIVE.
