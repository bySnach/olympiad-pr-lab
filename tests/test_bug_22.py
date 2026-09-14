from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.progress import completion_state


class CompletionStateTests(unittest.TestCase):
    def test_mixed_tasks_are_in_progress(self) -> None:
        done = StudyTask("A-1", "Done", 30, "high", date(2026, 9, 20), True)
        open_task = StudyTask("A-2", "Open", 30, "medium", date(2026, 9, 21))

        self.assertEqual("in progress", completion_state([done, open_task]))
