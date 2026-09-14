from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.reporting import completion_percent


class CompletionPercentTests(unittest.TestCase):
    def test_completion_percent_uses_all_tasks(self) -> None:
        done = StudyTask("A-1", "Done", 30, "high", date(2026, 9, 20), True)
        open_task = StudyTask("A-2", "Open", 30, "low", date(2026, 9, 21))

        self.assertEqual(50.0, completion_percent([done, open_task]))
