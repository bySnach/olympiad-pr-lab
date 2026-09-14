from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


class PriorityOrderingTests(unittest.TestCase):
    def test_priority_order_is_high_medium_low_with_stable_ties(self) -> None:
        tasks = [
            StudyTask("H-1", "First high", 30, "high", date(2026, 9, 20)),
            StudyTask("L-1", "Low", 30, "low", date(2026, 9, 20)),
            StudyTask("H-2", "Second high", 30, "high", date(2026, 9, 20)),
            StudyTask("M-1", "Medium", 30, "medium", date(2026, 9, 20)),
        ]

        self.assertEqual(["H-1", "H-2", "M-1", "L-1"], [task.task_id for task in StudyPlanner(tasks).by_priority()])
