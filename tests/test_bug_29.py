from datetime import date
import unittest

from study_planner.calendar_tools import is_weekend


class WeekendTests(unittest.TestCase):
    def test_saturday_and_sunday_are_weekend_days(self) -> None:
        self.assertTrue(is_weekend(date(2026, 9, 19)))
        self.assertTrue(is_weekend(date(2026, 9, 20)))
