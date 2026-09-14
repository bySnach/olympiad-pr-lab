from datetime import date
import unittest

from study_planner.filters import (
    at_least_minutes,
    by_due_date,
    unfinished_tasks,
    with_priority,
)
from study_planner.planner import StudyTask


def task(
    task_id: str, minutes: int = 30, priority: str = "medium"
) -> StudyTask:
    return StudyTask(task_id, "Practice", minutes, priority, date(2026, 9, 20))


class FilterTests(unittest.TestCase):
    def test_one_open_task_is_unfinished(self) -> None:
        algebra = task("A-1")
        self.assertEqual([algebra], unfinished_tasks([algebra]))

    def test_task_above_minimum_duration_is_returned(self) -> None:
        algebra = task("A-1", minutes=61)
        self.assertEqual([algebra], at_least_minutes([algebra], 60))

    def test_exact_priority_is_returned(self) -> None:
        algebra = task("A-1", priority="high")
        self.assertEqual([algebra], with_priority([algebra], "high"))

    def test_one_task_is_its_own_date_order(self) -> None:
        algebra = task("A-1")
        self.assertEqual([algebra], by_due_date([algebra]))
