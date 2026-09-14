from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


class AverageDurationTests(unittest.TestCase):
    def test_average_uses_each_task_once(self) -> None:
        planner = StudyPlanner(
            [
                StudyTask("A-1", "First", 30, "high", date(2026, 9, 20)),
                StudyTask("A-2", "Second", 60, "medium", date(2026, 9, 21)),
            ]
        )

        self.assertEqual(45.0, planner.average_minutes())
