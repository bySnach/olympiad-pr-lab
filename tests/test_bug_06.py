from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


class DuplicateTaskIdTests(unittest.TestCase):
    def test_duplicate_id_is_rejected_without_replacing_original_task(self) -> None:
        original = StudyTask("A-1", "Original", 30, "high", date(2026, 9, 20))
        replacement = StudyTask("A-1", "Replacement", 45, "low", date(2026, 9, 21))
        planner = StudyPlanner([original])

        with self.assertRaises(ValueError):
            planner.add_task(replacement)

        self.assertIs(original, planner.get_task("A-1"))
