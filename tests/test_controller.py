from engineering_runtime.contracts import Decision
from engineering_runtime.controller import GateEvidence, evaluate


def evidence(**overrides):
    inputs = dict(candidate_sha="abc", reviewed_sha="abc", builder_session="builder", reviewer_session="reviewer", independent_worktree=True, mandatory_checks={"unit": True, "security": True})
    inputs.update(overrides)
    return GateEvidence(**inputs)


def test_positive_demonstration_gate():
    assert evaluate(evidence()) == Decision.ACCEPT


def test_session_reuse_blocks():
    assert evaluate(evidence(reviewer_session="builder")) == Decision.BLOCKED


def test_sha_mismatch_blocks():
    assert evaluate(evidence(reviewed_sha="def")) == Decision.BLOCKED


def test_missing_evidence_blocks():
    assert evaluate(evidence(missing_evidence=True)) == Decision.BLOCKED


def test_failing_checks_continue_only_with_budget():
    assert evaluate(evidence(mandatory_checks={"security": False})) == Decision.CONTINUE
    assert evaluate(evidence(mandatory_checks={"security": False}, repairs_used=2)) == Decision.BLOCKED


def test_material_defects_continue():
    assert evaluate(evidence(material_defects=True)) == Decision.CONTINUE
