from datetime import date
import unittest

from study_planner import StudyPlanner, StudyTask


def task(task_id: str, title: str, minutes: int = 30) -> StudyTask:
    return StudyTask(task_id, title, minutes, "medium", date(2026, 9, 20))


class StudyPlannerTests(unittest.TestCase):
    def test_add_get_and_complete_task(self) -> None:
        planner = StudyPlanner()
        algebra = task("A-1", "Algebra warm-up")

        planner.add_task(algebra)

        self.assertIs(planner.get_task("A-1"), algebra)
        self.assertTrue(planner.complete_task("A-1"))
        self.assertTrue(algebra.completed)

    def test_missing_task_cannot_be_completed(self) -> None:
        self.assertFalse(StudyPlanner().complete_task("missing"))

    def test_exact_search_finds_a_task(self) -> None:
        planner = StudyPlanner([task("A-1", "Algebra warm-up")])

        found = planner.search("Algebra")

        self.assertEqual(["A-1"], [item.task_id for item in found])

    def test_empty_planner_has_zero_average(self) -> None:
        self.assertEqual(0.0, StudyPlanner().average_minutes())
