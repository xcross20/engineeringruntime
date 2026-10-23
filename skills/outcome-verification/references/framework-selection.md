# Framework selection

Prefer existing test tools and lockfiles; do not add packages merely to appear comprehensive.

| Context | Candidate tools | Evidence |
|---|---|---|
| Python pure domain logic | pytest, pytest-cov, Hypothesis | assertions, property counterexamples, coverage |
| PostgreSQL transactional integration | Testcontainers for Python, pytest | real migrations, isolation, concurrent transactions |
| FastAPI/OpenAPI | Schemathesis, httpx, pytest | contract fuzzing, schema errors, stateful API behavior |
| Next.js/React | Playwright Test, @axe-core/playwright | journeys, traces, screenshots, accessibility violations |
| Critical branch test strength | mutmut | surviving mutations and impacted requirements |
| Performance | Locust or focused repeatable benchmarks; OpenTelemetry | fixed-load latency, trace spans, query counts |
| Stateful business operations | Hypothesis RuleBasedStateMachine | invariant violations across operation sequences |

Do not require all tools on every iteration. Fast tier: static checks + focused unit tests. Integration tier: real DB, API, browser. Adversarial tier: mutation, concurrency, fault injection, bounded load.

Prefer deterministic fixtures and versioned seed data. Record tool versions, environment, seed, time and resource budgets. Never claim performance improvement without equivalent baseline and candidate environments.
