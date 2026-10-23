#!/usr/bin/env python3
"""Validate and save a supplied verification report; does not run commands."""
import argparse
import json
from pathlib import Path

STATUSES = {"PASS", "FAIL", "INCONCLUSIVE", "BLOCKED"}

def validate(report: dict) -> dict:
    if not isinstance(report, dict) or not report.get("source_commit") or not report.get("contract_id"):
        raise ValueError("source_commit and contract_id are required")
    checks = report.get("checks")
    if not isinstance(checks, list) or not checks:
        raise ValueError("at least one check required")
    for check in checks:
        if check.get("status") not in STATUSES or not check.get("requirement_id"):
            raise ValueError("invalid check")
        if check["status"] == "PASS" and check.get("exit_code") != 0:
            raise ValueError("PASS requires captured exit_code 0")
    statuses = {check["status"] for check in checks}
    report["overall_status"] = (
        "FAIL" if "FAIL" in statuses else
        "BLOCKED" if "BLOCKED" in statuses else
        "INCONCLUSIVE" if "INCONCLUSIVE" in statuses else "PASS"
    )
    return report

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    report = validate(json.loads(args.input.read_text(encoding="utf-8")))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(report["overall_status"])

if __name__ == "__main__":
    main()
