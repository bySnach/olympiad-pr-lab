from datetime import date
import unittest

from study_planner.filters import with_priority
from study_planner.planner import StudyTask


class PriorityFilterNormalizationTests(unittest.TestCase):
    def test_priority_filter_normalizes_case_and_whitespace(self) -> None:
        high = StudyTask("A-1", "High", 30, "high", date(2026, 9, 20))
        low = StudyTask("A-2", "Low", 30, "low", date(2026, 9, 21))

        self.assertEqual([high], with_priority([high, low], " HIGH "))
