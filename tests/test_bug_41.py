from datetime import date
import unittest

from study_planner.collection_tools import task_slice
from study_planner.planner import StudyTask


class TaskSliceOffsetTests(unittest.TestCase):
    def test_slice_starts_at_zero_based_offset(self) -> None:
        tasks = [
            StudyTask("A-1", "First", 30, "high", date(2026, 9, 20)),
            StudyTask("A-2", "Second", 30, "medium", date(2026, 9, 21)),
            StudyTask("A-3", "Third", 30, "low", date(2026, 9, 22)),
        ]

        self.assertEqual([tasks[1]], task_slice(tasks, 1, 1))
