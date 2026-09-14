from datetime import date
import unittest

from study_planner.copies import with_title
from study_planner.planner import StudyTask


class RetitleCopyTests(unittest.TestCase):
    def test_retitling_returns_a_new_task_and_keeps_original(self) -> None:
        original = StudyTask("A-1", "Original", 30, "high", date(2026, 9, 20))

        retitled = with_title(original, "Retitled")

        self.assertIsNot(original, retitled)
        self.assertEqual("Original", original.title)
        self.assertEqual("Retitled", retitled.title)
