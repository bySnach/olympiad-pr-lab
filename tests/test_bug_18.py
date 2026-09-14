from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.progress import completed_minutes


class CompletedMinutesTests(unittest.TestCase):
    def test_completed_minutes_includes_only_completed_work(self) -> None:
        done = StudyTask("A-1", "Done", 25, "high", date(2026, 9, 20), True)
        open_task = StudyTask("A-2", "Open", 70, "medium", date(2026, 9, 21))

        self.assertEqual(25, completed_minutes([done, open_task]))
