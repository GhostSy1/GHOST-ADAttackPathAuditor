import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


class ADAuditorTests(unittest.TestCase):
    def test_hashes_real_input_and_detects_delegation(self):
        module_path = Path(__file__).parents[1] / "tools" / "ghost_extension.py"
        spec = importlib.util.spec_from_file_location("ghost_extension", module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "ad_dump.txt"
            content = b"Account configured with unconstrained delegation and adminCount=1\n"
            target.write_bytes(content)
            report = module.analyze(target)
        self.assertEqual(report["artifacts"][0]["sha256"], hashlib.sha256(content).hexdigest())
        self.assertTrue(any(f["rule_id"] == "AD-DELEGATION" for f in report["findings"]))
        self.assertFalse(report["metadata"]["execution_performed"])


if __name__ == "__main__":
    unittest.main()
