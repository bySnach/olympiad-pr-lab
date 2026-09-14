from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.progress import all_tasks_completed


class AllCompleteTests(unittest.TestCase):
    def test_mixed_completion_state_is_not_all_complete(self) -> None:
        done = StudyTask("A-1", "Done", 30, "high", date(2026, 9, 20), True)
        open_task = StudyTask("A-2", "Open", 30, "medium", date(2026, 9, 21))

        self.assertFalse(all_tasks_completed([done, open_task]))
