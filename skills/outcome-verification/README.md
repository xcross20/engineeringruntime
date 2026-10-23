# Outcome Verification

Reusable skill for turning user-outcome requirements into trusted verification evidence. It is housed in `engineeringruntime`, but targets any repository.

## Start with Grok CLI
Open Grok CLI in the **target** project repository. Provide the absolute path to this skill's `SKILL.md` and ask the agent to read it, inspect the target repo, and produce a verification plan before adding dependencies or running tests.

Example instruction:

> Use the Outcome Verification skill at /absolute/path/engineeringruntime/skills/outcome-verification/SKILL.md. Target this repository. Inspect existing contracts, tests, dependencies and constraints. Produce a requirement-to-test matrix, propose the smallest necessary framework additions, and implement only approved verification scaffolding. Run trusted bounded tests, save evidence, and report PASS/FAIL/INCONCLUSIVE/BLOCKED. Do not merge, deploy, or self-approve.

If Grok CLI supports custom skills, register this directory according to the CLI's installed version. Otherwise reference the SKILL.md path explicitly. Do not assume a particular Grok command or skills directory without checking `grok --help`.

## What exists in v0
- Stack-detection utility using filenames only (no execution).
- Evidence report writer from an explicitly supplied JSON input.
- Reference methodology, acceptance and budget templates.
- Unit tests for the utilities.

## What does not exist yet
- Automated framework installation.
- Running untrusted commands or starting sandboxes.
- Integrated Playwright/Testcontainers/Schemathesis orchestration.
- Autonomous reviewer or release authority.

## Safe rollout
1. Run `detect_stack.py` on RE-001 and review suggested coverage gaps.
2. Have Grok implement RE-001-specific pytest/Hypothesis/Testcontainers/Schemathesis/Playwright checks **in RE-001**, not inside this generic skill.
3. Define acceptance IDs and capture structured evidence.
4. Integrate the approved bounded runner only after ERT-002 safety defects are resolved.
5. Promote stable reusable adapters into this skill only after real project proof.
