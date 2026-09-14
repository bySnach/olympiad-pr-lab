from datetime import date
import unittest

from study_planner.aggregation import minutes_by_priority
from study_planner.planner import StudyTask


class PriorityMinuteTotalsTests(unittest.TestCase):
    def test_minutes_are_summed_for_each_priority(self) -> None:
        tasks = [
            StudyTask("A-1", "First", 20, "high", date(2026, 9, 20)),
            StudyTask("A-2", "Second", 35, "high", date(2026, 9, 21)),
            StudyTask("A-3", "Third", 10, "low", date(2026, 9, 22)),
        ]

        self.assertEqual({"high": 55, "low": 10}, minutes_by_priority(tasks))
