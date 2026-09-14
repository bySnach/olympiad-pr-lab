from datetime import date
import unittest

from study_planner.collection_tools import replace_task
from study_planner.planner import StudyTask


class ReplaceTaskPositionTests(unittest.TestCase):
    def test_replacing_task_keeps_matching_position(self) -> None:
        original = StudyTask("A-1", "Original", 30, "high", date(2026, 9, 20))
        second = StudyTask("A-2", "Second", 30, "medium", date(2026, 9, 21))
        replacement = StudyTask("A-1", "Replacement", 45, "high", date(2026, 9, 22))

        self.assertEqual([replacement, second], replace_task([original, second], replacement))
