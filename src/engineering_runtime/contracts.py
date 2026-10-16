"""Strict JSON project adapter contract; loading it never executes a command."""
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import json


class Decision(str, Enum):
    ACCEPT = "ACCEPT"
    CONTINUE = "CONTINUE"
    BLOCKED = "BLOCKED"
    RETHINK = "RETHINK"


@dataclass(frozen=True)
class Project:
    name: str
    repository: str
    work_orders: tuple[str, ...]
    verification_commands: tuple[tuple[str, ...], ...]
    forbidden_actions: tuple[str, ...]
    max_repairs: int

    @classmethod
    def load(cls, path: Path) -> "Project":
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("project must be an object")
        required = {"name", "repository", "work_orders", "verification_commands", "forbidden_actions", "max_repairs"}
        if set(data) != required:
            raise ValueError(f"invalid project fields: {sorted(set(data) ^ required)}")
        for field in ("name", "repository"):
            if not isinstance(data[field], str) or not data[field].strip():
                raise ValueError(f"{field} must be a nonempty string")
        orders = data["work_orders"]
        if not isinstance(orders, list) or not orders or not all(isinstance(x, str) and x.strip() for x in orders):
            raise ValueError("work_orders must contain nonempty strings")
        commands = data["verification_commands"]
        if not isinstance(commands, list) or not commands or not all(isinstance(c, list) and c and all(isinstance(x, str) and x for x in c) for c in commands):
            raise ValueError("verification_commands must contain nonempty argv arrays")
        actions = data["forbidden_actions"]
        if not isinstance(actions, list) or not all(isinstance(x, str) for x in actions):
            raise ValueError("forbidden_actions must contain strings")
        repairs = data["max_repairs"]
        if isinstance(repairs, bool) or not isinstance(repairs, int) or not 0 <= repairs <= 5:
            raise ValueError("max_repairs must be an integer between 0 and 5")
        return cls(data["name"], data["repository"], tuple(orders), tuple(tuple(c) for c in commands), tuple(actions), repairs)
