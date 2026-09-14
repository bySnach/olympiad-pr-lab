from datetime import date
import unittest

from study_planner.planner import StudyTask
from study_planner.reporting import (
    completion_percent,
    earliest_due_task,
    longest_task,
    remaining_minutes,
)


def task(task_id: str, minutes: int = 30) -> StudyTask:
    return StudyTask(task_id, "Practice", minutes, "medium", date(2026, 9, 20))


class ReportingTests(unittest.TestCase):
    def test_single_open_task_has_remaining_minutes(self) -> None:
        self.assertEqual(30, remaining_minutes([task("A-1")]))

    def test_no_completed_tasks_have_zero_completion_percent(self) -> None:
        self.assertEqual(0.0, completion_percent([task("A-1")]))

    def test_single_task_is_its_own_longest_task(self) -> None:
        algebra = task("A-1")
        self.assertIs(algebra, longest_task([algebra]))

    def test_single_task_is_its_own_earliest_task(self) -> None:
        algebra = task("A-1")
        self.assertIs(algebra, earliest_due_task([algebra]))
