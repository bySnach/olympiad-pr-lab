from datetime import date
import unittest

from study_planner.filters import by_due_date
from study_planner.planner import StudyTask


class DueDateOrderingTests(unittest.TestCase):
    def test_due_dates_are_ascending_and_equal_dates_are_stable(self) -> None:
        first = StudyTask("A-1", "First", 30, "high", date(2026, 9, 20))
        same_day = StudyTask("A-2", "Same day", 30, "medium", date(2026, 9, 20))
        later = StudyTask("A-3", "Later", 30, "low", date(2026, 9, 21))

        self.assertEqual([first, same_day, later], by_due_date([later, first, same_day]))
