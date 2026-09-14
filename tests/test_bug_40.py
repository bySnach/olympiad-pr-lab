from datetime import date
import unittest

from study_planner.collection_tools import without_task_id
from study_planner.planner import StudyTask


class RemoveTaskTests(unittest.TestCase):
    def test_removing_id_keeps_every_other_task(self) -> None:
        first = StudyTask("A-1", "First", 30, "high", date(2026, 9, 20))
        second = StudyTask("A-2", "Second", 30, "medium", date(2026, 9, 21))

        self.assertEqual([second], without_task_id([first, second], "A-1"))
