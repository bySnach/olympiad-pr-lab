from datetime import date
import unittest

from study_planner.calendar_tools import next_due_after
from study_planner.planner import StudyTask


class NextDueAfterTests(unittest.TestCase):
    def test_next_due_task_is_strictly_after_reference_day(self) -> None:
        today = date(2026, 9, 20)
        due_today = StudyTask("A-1", "Today", 30, "high", today)
        tomorrow = StudyTask("A-2", "Tomorrow", 30, "medium", date(2026, 9, 21))

        self.assertIs(tomorrow, next_due_after([due_today, tomorrow], today))
