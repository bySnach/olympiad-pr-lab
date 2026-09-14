from datetime import date
import unittest

from study_planner.filters import by_due_date
from study_planner.planner import StudyTask


class DueDateTieBehaviorTests(unittest.TestCase):
    def test_equal_due_dates_keep_input_order(self) -> None:
        first = StudyTask("A-1", "First", 30, "high", date(2026, 9, 20))
        second = StudyTask("A-2", "Second", 30, "medium", date(2026, 9, 20))

        self.assertEqual([first, second], by_due_date([first, second]))
