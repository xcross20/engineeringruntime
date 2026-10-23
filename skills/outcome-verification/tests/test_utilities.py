import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class SkillUtilitiesTest(unittest.TestCase):
    def test_detect_stack(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "pyproject.toml").write_text("[project]\n")
            result = load("detect_stack").detect(root)
            self.assertIn("python", result["markers"])

    def test_pass_requires_exit_code(self):
        report = {"source_commit": "abc", "contract_id": "X", "checks": [
            {"requirement_id": "X-1", "status": "PASS", "exit_code": None}]}
        with self.assertRaises(ValueError):
            load("collect_evidence").validate(report)

    def test_failed_check_fails_report(self):
        report = {"source_commit": "abc", "contract_id": "X", "checks": [
            {"requirement_id": "X-1", "status": "FAIL", "exit_code": 1}]}
        self.assertEqual(load("collect_evidence").validate(report)["overall_status"], "FAIL")

if __name__ == "__main__":
    unittest.main()
