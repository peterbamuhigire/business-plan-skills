import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
DOC = ROOT / "docs/operations/runtime-agnostic-orchestration-2026-09-07.md"


class RuntimeOrchestrationGuidanceTests(unittest.TestCase):
    def test_contract_is_linked_and_has_required_controls(self):
        doc = DOC.read_text(encoding="utf-8")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("runtime-agnostic-orchestration-2026-09-07.md", readme)
        for heading in ("## Phase contract", "## Agency and security rules", "## Source basis and limits"):
            self.assertIn(heading, doc)
        for marker in ("scoped", "checkpoint", "NOT_ASSESSED", "untrusted", "Rollback", "Claude", "Codex"):
            self.assertIn(marker, doc)
        for url in ("the-shortform-guide.md", "the-longform-guide.md", "the-security-guide.md"):
            self.assertIn("https://raw.githubusercontent.com/affaan-m/ECC/main/" + url, doc)


if __name__ == "__main__":
    unittest.main()
