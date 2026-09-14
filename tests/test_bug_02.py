from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


class InclusiveDateRangeTests(unittest.TestCase):
    def test_date_range_includes_both_requested_boundaries(self) -> None:
        start = date(2026, 9, 20)
        end = date(2026, 9, 22)
        first = StudyTask("A-1", "First", 30, "high", start)
        last = StudyTask("A-2", "Last", 30, "high", end)
        outside = StudyTask("A-3", "Outside", 30, "high", date(2026, 9, 23))

        self.assertEqual([first, last], StudyPlanner([first, last, outside]).tasks_due_between(start, end))
