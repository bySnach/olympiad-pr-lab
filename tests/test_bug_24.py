from datetime import date
import unittest

from study_planner.calendar_tools import is_overdue
from study_planner.planner import StudyTask


class OverdueTodayTests(unittest.TestCase):
    def test_task_due_today_is_not_overdue(self) -> None:
        today = date(2026, 9, 20)
        task = StudyTask("A-1", "Today", 30, "high", today)

        self.assertFalse(is_overdue(task, today))
