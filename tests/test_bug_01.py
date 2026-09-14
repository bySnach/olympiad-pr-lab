from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


class SearchNormalizationTests(unittest.TestCase):
    def test_search_ignores_query_case_and_surrounding_whitespace(self) -> None:
        matching = StudyTask(
            "A-1", "Algebra Warm-Up", 30, "high", date(2026, 9, 20)
        )
        planner = StudyPlanner(
            [matching, StudyTask("G-1", "Geometry", 45, "medium", date(2026, 9, 21))]
        )

        self.assertEqual([matching], planner.search("  algebra warm-up  "))
