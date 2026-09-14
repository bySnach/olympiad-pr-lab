from datetime import date
import unittest

from study_planner.calendar_tools import tasks_due_on
from study_planner.planner import StudyTask


class ExactDueDateFilterTests(unittest.TestCase):
    def test_due_date_filter_returns_only_the_requested_day(self) -> None:
        target = date(2026, 9, 20)
        matching = StudyTask("A-1", "Matching", 30, "high", target)
        other = StudyTask("A-2", "Other", 30, "medium", date(2026, 9, 21))

        self.assertEqual([matching], tasks_due_on([matching, other], target))
