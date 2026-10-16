import json
import pytest
from engineering_runtime.contracts import Project


def test_valid_project(tmp_path):
    path = tmp_path / "project.json"
    path.write_text(json.dumps({"name": "EARS", "repository": "xcross20/EARS", "work_orders": ["ERT-001"], "verification_commands": [["npm", "test"]], "forbidden_actions": ["merge"], "max_repairs": 2}))
    assert Project.load(path).max_repairs == 2


@pytest.mark.parametrize("override", [{"work_orders": []}, {"verification_commands": ["npm test"]}, {"max_repairs": True}, {"unexpected": "not allowed"}])
def test_rejects_invalid_project(tmp_path, override):
    data = {"name": "EARS", "repository": "xcross20/EARS", "work_orders": ["ERT-001"], "verification_commands": [["npm", "test"]], "forbidden_actions": [], "max_repairs": 2}
    data.update(override)
    path = tmp_path / "invalid.json"
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError):
        Project.load(path)
