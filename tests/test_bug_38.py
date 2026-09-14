from datetime import date
import unittest

from study_planner.collection_tools import unique_priorities
from study_planner.planner import StudyTask


class UniquePriorityOrderTests(unittest.TestCase):
    def test_unique_priorities_preserve_first_occurrence_order(self) -> None:
        tasks = [
            StudyTask("A-1", "Low", 30, "low", date(2026, 9, 20)),
            StudyTask("A-2", "High", 30, "high", date(2026, 9, 21)),
            StudyTask("A-3", "Low again", 30, "low", date(2026, 9, 22)),
            StudyTask("A-4", "Medium", 30, "medium", date(2026, 9, 23)),
        ]

        self.assertEqual(["low", "high", "medium"], unique_priorities(tasks))
