import unittest
from contextlib import redirect_stdout
from io import StringIO

from study_planner.__main__ import main


class CliTests(unittest.TestCase):
    def test_list_command_prints_demo_tasks(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            exit_code = main(["list"])

        self.assertEqual(0, exit_code)
        self.assertIn("Algebra warm-up", output.getvalue())
