from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.reporting import longest_task


class LongestTaskTests(unittest.TestCase):
    def test_longest_task_selects_greatest_duration(self) -> None:
        short = StudyTask("A-1", "Short", 30, "high", date(2026, 9, 20))
        long = StudyTask("A-2", "Long", 75, "medium", date(2026, 9, 21))

        self.assertIs(long, longest_task([short, long]))
