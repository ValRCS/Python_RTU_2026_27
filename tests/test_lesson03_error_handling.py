"""Smoke tests for Lesson 3 error-handling example."""
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "lessons" / "03_loops_strings" / "05_error_handling.py"


class InputRetryTests(unittest.TestCase):
    def run_example(self, input_text):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input=input_text,
            text=True,
            capture_output=True,
            timeout=5,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def test_bad_text_and_negative_number_are_retried(self):
        output = self.run_example("abc\n-2\n5\n")
        self.assertIn("Nederīga ievade.", output)
        self.assertIn("Skaitlim jābūt nenegatīvam.", output)
        self.assertIn("Ievadītais skaitlis: 5", output)

    def test_zero_is_valid(self):
        output = self.run_example("0\n")
        self.assertIn("Ievadītais skaitlis: 0", output)
        self.assertNotIn("Nederīga ievade.", output)


if __name__ == "__main__":
    unittest.main()
