from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.reporting import earliest_due_task


class EarliestDueTaskTests(unittest.TestCase):
    def test_earliest_due_task_selects_earliest_date(self) -> None:
        early = StudyTask("A-1", "Early", 30, "high", date(2026, 9, 20))
        late = StudyTask("A-2", "Late", 30, "medium", date(2026, 9, 25))

        self.assertIs(early, earliest_due_task([early, late]))
