import unittest

from study_planner.presentation import due_status


class DueStatusTests(unittest.TestCase):
    def test_due_status_distinguishes_past_today_and_future(self) -> None:
        self.assertEqual("overdue", due_status(-1))
        self.assertEqual("due today", due_status(0))
        self.assertEqual("upcoming", due_status(1))
