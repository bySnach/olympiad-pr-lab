from datetime import date
import unittest

from study_planner.calendar_tools import weekday_count


class InclusiveWeekdayCountTests(unittest.TestCase):
    def test_weekday_count_includes_both_endpoints(self) -> None:
        self.assertEqual(2, weekday_count(date(2026, 9, 21), date(2026, 9, 22)))
