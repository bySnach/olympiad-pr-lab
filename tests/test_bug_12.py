from datetime import date
import unittest

from study_planner.filters import at_least_minutes
from study_planner.planner import StudyTask


class MinimumDurationTests(unittest.TestCase):
    def test_minimum_duration_includes_an_equal_duration(self) -> None:
        exact = StudyTask("A-1", "Exact", 60, "high", date(2026, 9, 20))
        shorter = StudyTask("A-2", "Short", 59, "medium", date(2026, 9, 21))

        self.assertEqual([exact], at_least_minutes([exact, shorter], 60))
