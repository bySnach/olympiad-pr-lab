from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.progress import first_unfinished_task


class FirstUnfinishedTaskTests(unittest.TestCase):
    def test_first_unfinished_task_uses_input_order(self) -> None:
        first_open = StudyTask("A-1", "First", 30, "high", date(2026, 9, 20))
        done = StudyTask("A-2", "Done", 30, "medium", date(2026, 9, 21), True)
        last_open = StudyTask("A-3", "Last", 30, "low", date(2026, 9, 22))

        self.assertIs(first_open, first_unfinished_task([first_open, done, last_open]))
