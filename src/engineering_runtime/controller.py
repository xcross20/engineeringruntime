"""Pure demonstration decision gate, NOT a trusted runtime acceptance gate."""
from dataclasses import dataclass
from .contracts import Decision


@dataclass(frozen=True)
class GateEvidence:
    candidate_sha: str
    reviewed_sha: str
    builder_session: str
    reviewer_session: str
    independent_worktree: bool
    mandatory_checks: dict[str, bool]
    missing_evidence: bool = False
    material_defects: bool = False
    repairs_used: int = 0


def evaluate(e: GateEvidence, *, max_repairs: int = 2) -> Decision:
    """Model a decision only; caller assertions are not independently attested."""
    if (not e.candidate_sha or e.candidate_sha != e.reviewed_sha
        or not e.builder_session or not e.reviewer_session
        or e.builder_session == e.reviewer_session or not e.independent_worktree
        or e.missing_evidence or not e.mandatory_checks):
        return Decision.BLOCKED
    if not all(e.mandatory_checks.values()) or e.material_defects:
        return Decision.CONTINUE if e.repairs_used < max_repairs else Decision.BLOCKED
    return Decision.ACCEPT
