from datetime import date
import unittest

from study_planner.collection_tools import take_first
from study_planner.planner import StudyTask


class ZeroLimitTests(unittest.TestCase):
    def test_zero_limit_returns_no_tasks(self) -> None:
        task = StudyTask("A-1", "Only", 30, "high", date(2026, 9, 20))

        self.assertEqual([], take_first([task], 0))
