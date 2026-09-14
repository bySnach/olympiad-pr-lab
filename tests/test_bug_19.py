from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.progress import total_planned_minutes


class TotalPlannedMinutesTests(unittest.TestCase):
    def test_total_planned_minutes_adds_every_task(self) -> None:
        first = StudyTask("A-1", "First", 25, "high", date(2026, 9, 20))
        second = StudyTask("A-2", "Second", 70, "medium", date(2026, 9, 21))

        self.assertEqual(95, total_planned_minutes([first, second]))
