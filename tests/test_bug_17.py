from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.progress import completed_task_count


class CompletedTaskCountTests(unittest.TestCase):
    def test_completed_count_excludes_unfinished_tasks(self) -> None:
        done = StudyTask("A-1", "Done", 30, "high", date(2026, 9, 20), True)
        open_first = StudyTask("A-2", "Open", 30, "medium", date(2026, 9, 21))
        open_second = StudyTask("A-3", "Open", 30, "low", date(2026, 9, 22))

        self.assertEqual(1, completed_task_count([done, open_first, open_second]))
