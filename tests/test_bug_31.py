from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.presentation import format_task_line


class CompletionMarkerTests(unittest.TestCase):
    def test_task_lines_use_correct_completion_markers(self) -> None:
        open_task = StudyTask("A-1", "Open", 30, "high", date(2026, 9, 20))
        done_task = StudyTask("A-2", "Done", 30, "medium", date(2026, 9, 21), True)

        self.assertTrue(format_task_line(open_task).startswith("[ ]"))
        self.assertTrue(format_task_line(done_task).startswith("[x]"))
