from datetime import date
import unittest

from study_planner.calendar_tools import tasks_due_in_month
from study_planner.planner import StudyTask


class YearAwareMonthFilterTests(unittest.TestCase):
    def test_month_filter_matches_year_and_month(self) -> None:
        this_year = StudyTask("A-1", "This year", 30, "high", date(2026, 9, 20))
        other_year = StudyTask("A-2", "Other year", 30, "medium", date(2025, 9, 20))

        self.assertEqual([this_year], tasks_due_in_month([this_year, other_year], 2026, 9))
