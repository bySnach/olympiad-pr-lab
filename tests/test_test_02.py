import unittest

from study_planner.reporting import (
    completion_percent,
    earliest_due_task,
    longest_task,
    remaining_minutes,
)


class EmptyReportingBehaviorTests(unittest.TestCase):
    def test_reporting_helpers_return_documented_empty_results(self) -> None:
        self.assertEqual(0, remaining_minutes([]))
        self.assertEqual(0.0, completion_percent([]))
        self.assertIsNone(longest_task([]))
        self.assertIsNone(earliest_due_task([]))
