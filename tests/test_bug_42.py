from datetime import date
import unittest

from study_planner.collection_tools import group_by_due_date
from study_planner.planner import StudyTask


class DueDateGroupingTests(unittest.TestCase):
    def test_grouping_retains_all_tasks_with_shared_due_date(self) -> None:
        shared = date(2026, 9, 20)
        first = StudyTask("A-1", "First", 30, "high", shared)
        second = StudyTask("A-2", "Second", 30, "medium", shared)

        self.assertEqual({shared: [first, second]}, group_by_due_date([first, second]))
