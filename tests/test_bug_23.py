from datetime import date
import unittest

from study_planner.calendar_tools import days_until
from study_planner.planner import StudyTask


class SignedDayOffsetTests(unittest.TestCase):
    def test_past_due_date_has_a_negative_offset(self) -> None:
        task = StudyTask("A-1", "Past", 30, "high", date(2026, 9, 18))

        self.assertEqual(-2, days_until(task, date(2026, 9, 20)))
