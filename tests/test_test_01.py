from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


class PriorityTieBehaviorTests(unittest.TestCase):
    def test_tasks_with_equal_priority_keep_their_input_order(self) -> None:
        first = StudyTask("H-1", "First", 30, "high", date(2026, 9, 20))
        second = StudyTask("H-2", "Second", 30, "high", date(2026, 9, 21))

        self.assertEqual([first, second], StudyPlanner([first, second]).by_priority())
