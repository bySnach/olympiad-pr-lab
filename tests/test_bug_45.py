from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.records import task_to_record


class BooleanRecordCompletionTests(unittest.TestCase):
    def test_task_record_keeps_completion_as_a_boolean(self) -> None:
        task = StudyTask("A-1", "Done", 30, "high", date(2026, 9, 20), True)

        self.assertIs(True, task_to_record(task)["completed"])
