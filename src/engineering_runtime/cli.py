"""Read-only project validation and dry-run preview; no agent execution yet."""
import argparse
import json
from pathlib import Path
from .contracts import Project


def main() -> int:
    parser = argparse.ArgumentParser(prog="engineering-runtime")
    parser.add_argument("command", choices=("validate", "plan"))
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    try:
        project = Project.load(args.project)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    if args.command == "validate":
        print(f"Valid project: {project.name}")
    else:
        print(json.dumps({"mode": "DRY_RUN_ONLY", "project": project.name, "next_work_order": project.work_orders[0], "checks": [list(c) for c in project.verification_commands], "max_repairs": project.max_repairs}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
