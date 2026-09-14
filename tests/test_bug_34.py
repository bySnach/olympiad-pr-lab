import unittest

from study_planner.presentation import format_task_count


class TaskCountPluralizationTests(unittest.TestCase):
    def test_only_one_task_uses_singular_form(self) -> None:
        self.assertEqual("0 tasks", format_task_count(0))
        self.assertEqual("1 task", format_task_count(1))
        self.assertEqual("2 tasks", format_task_count(2))
