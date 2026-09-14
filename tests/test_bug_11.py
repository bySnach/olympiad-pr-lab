from datetime import date
import unittest

from study_planner.filters import unfinished_tasks
from study_planner.planner import StudyTask


class UnfinishedTaskFilterTests(unittest.TestCase):
    def test_unfinished_filter_excludes_completed_tasks(self) -> None:
        open_task = StudyTask("A-1", "Open", 30, "high", date(2026, 9, 20))
        done_task = StudyTask("A-2", "Done", 30, "medium", date(2026, 9, 21), True)

        self.assertEqual([open_task], unfinished_tasks([open_task, done_task]))
