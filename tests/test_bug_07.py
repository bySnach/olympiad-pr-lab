from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.reporting import remaining_minutes


class RemainingMinutesTests(unittest.TestCase):
    def test_remaining_minutes_excludes_completed_work(self) -> None:
        open_task = StudyTask("A-1", "Open", 25, "high", date(2026, 9, 20))
        done_task = StudyTask("A-2", "Done", 70, "medium", date(2026, 9, 21), True)

        self.assertEqual(25, remaining_minutes([open_task, done_task]))
