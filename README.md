# Engineering Runtime

Reusable evidence-gated autonomous engineering runtime.

**Status: foundation scaffold only. Not autonomous or production-certified.**

## Mission
One approved work order -> Builder in isolated worktree -> genuinely independent Reviewer -> trusted tests -> deterministic Controller -> bounded repair or ACCEPT -> next approved work order. Humans retain merge, deployment and external side-effect authority.

## Bootstrap
- [MISSION](MISSION.md), [STRATEGY](STRATEGY.md), [AUTONOMY](AUTONOMY.md), [AGENTS](AGENTS.md)
- [Architecture](docs/architecture.md), [Threat Model](docs/threat-model.md)
- [Next](NEXT.md), [Progress](STATE.md), [Decisions](DECISION.md)
- Work orders: [ERT-001](work_orders/ERT-001.md), [ERT-002](work_orders/ERT-002.md), [ERT-003](work_orders/ERT-003.md), [ERT-004](work_orders/ERT-004.md)

## Local smoke check

```bash
python3 -m pip install -e '.[dev]'
python3 -m pytest -q
engineering-runtime validate examples/ears.project.json
engineering-runtime plan examples/ears.project.json
```

The CLI validates and shows a **dry-run** plan; no coding agent will launch. ERT-001 audits Rally, EARS and VentureOS to decide what tested components to extract.
